---
title: "Yhteydet"
date: 2020-01-01
description: "Opi yhdistämään pilvipalvelut, tietokoneet, NAS-laitteet ja hallitsemaan musiikkitiedostoja Evermusicillä. Vaiheittainen opas Wi-Fi Driveen, SMB:hen, DLNAan, WebDAViin, iTunes File Sharingiin ja muuhun."
keywords: [
  "Evermusic", "pilvimusiikin soitin", "NAS-suoratoisto", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "yhdistä pilvipalvelu", "musiikin siirto iPhone", "tiedostonhallinta iOS"
]
tags: ["evermusic", "opas", "yhteydet"]
readingTime: 11
---


Yhteydet-näytöllä voit yhdistää jokaisen lähteen, joka sisältää musiikkisi — suositut pilvipalvelut, itse isännöidyt mediapalvelimet, Mac tai PC, henkilökohtainen NAS, Apple Time Capsule, WD My Cloud Home, jopa USB-muistitikku — ja käyttää niitä kaikkia yhdestä yhtenäisestä käyttöliittymästä. Yhteydet on myös paikka, jossa määrität Pikakäytön syvälle sisäkkäisiin pilvisiin kansioihin ja johon todennat Last.fm scrobbling-toimintoa varten.

Näyttö on jaettu selkeästi merkittyihin osioihin: Pikakäyttö yläosassa (suosikkipilvikansiosi), Pilvipalvelu (lisäämäsi tilit), Paikallinen verkko (Bonjour-löydetyt laitteet), Tietokone (Wi-Fi Drive, iTunes File Sharing, SMB), Ulkoiset lisävarusteet (yhdistetyt USB-muistitikut) ja Muut palvelut (Last.fm ja vastaavat).

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusic Yhteydet-näyttö" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Yhdistä pilvipalveluun

- Avaa Yhteydet-välilehti.
- Valitse valikosta 'Yhdistä pilvipalveluun'.
- Valitse pilvipalvelu listasta.
- Kirjaudu sisään palveluntarjoajan virallisella valtuutussivulla (Evermusic ei koskaan näe salasanaasi).
- Napauta Valmis.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pilvipalveluntarjoajan valitsin" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Jos kohtaat ongelmia, tarkista internet-yhteytesi ja kirjautumistietosi sekä varmista, että kaksivaiheinen todennus on määritetty oikein kyseiselle palvelulle.  
Sovelluksen Premium-versiossa voit lisätä rajoittamattoman määrän palveluja. Ilmaiset käyttäjät voivat yhdistää yhden pilvitilin kerrallaan.

## Tuetut pilvipalvelut

Evermusic tukee kaikkia suosittuja pilvi- ja itse isännöityjä palveluja. Ilmaiset käyttäjät saavat saman palveluntarjoajaluettelon mutta yhden tilin rajoituksella; Premium avaa rajattomat tilit ja poistaa useimmat muut rajoitukset.

- **Henkilökohtaiset pilvitilit:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Itse isännöidyt palvelimet ja mediakirjastot:** Plex · Jellyfin · Emby · Subsonic (ja jokainen Subsonic-yhteensopiva palvelin — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ja Owncloud jaetun API:n kautta) · Synology Drive · QNAP.
- **NAS- ja tiedostonjako-protokollat:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (salasana tai julkisen avaimen todennus), NFS ja DLNA (vain luku — toisto ja lataus).
- **S3-yhteensopiva objektitallennustila:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage tai mikä tahansa S3-API-päätepiste.
- **Lähiverkon löytäminen:** 'Saatavilla olevat laitteet' -osio listaa automaattisesti kaikki Wi-Fi-verkossasi olevat Bonjour / mDNS -laitteet — Plex, Jellyfin, Emby-palvelimet, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, AirPort-reitittimet liitettyine asemineen jne.

## Turvallisuus ja yksityisyys

Käytämme vain virallista SDK:ta ja suojattua yhteyttä vuorovaikutukseen yhdistettyjen pilvipalvelujen kanssa. Kirjautumisesi ja salasanasi eivät ole sovelluksen käytettävissä. Kaikki sovelluksen pyynnöt pilvipalveluun on salattu.

Kun syötät kirjautumistietosi, sovellus näyttää pilvipalveluntarjoajan virallisen valtuutussivun, ja koko valtuutusprosessi tapahtuu sovelluksen ulkopuolella. Pilvipalveluntarjoaja lähettää onnistuneen valtuutuksen jälkeen auth-tokenin sovellukselle, jota käytetään API-kutsuissa.

Auth-token on digitaalinen avain, jonka avulla kolmannen osapuolen sovellukset voivat vuorovaikuttaa pilvipalvelun kanssa. Auth-token tallennetaan laitteellesi turvalliseen järjestelmävarastoon nimeltä Keychain. Voit ladata tiedostoja yhdistetystä pilvipalvelusta laitteellesi, ja ne sijoitetaan sovelluksen 'Asiakirjat'-hakemistoon. Voit poistaa nämä tiedostot milloin tahansa sisäänrakennetulla tiedostonhallinnalla.

Sovellus ei jaa mitään tietoja yhdistetystä pilvitilistä. Voit peruuttaa pilvitilisi käyttöoikeuden milloin tahansa avaamalla tilin asetussivun selaimessasi.

## Auth-tokenin hylkääminen

Kirjaudu tilillesi selaimessa ja siirry asetussivulle. Siellä löydät kaikki kolmannen osapuolen sovellukset, jotka on yhdistetty pilvitiliisi, ja voit poistaa minkä tahansa niistä, jos et enää halua käyttää sovellusta. Yksityiskohtaiset ohjeet ovat saatavilla [täältä](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Voit myös irrottaa yhdistetyt pilvitilit sovelluksessa, jolloin auth-token poistetaan myös laitteeltasi. Jos poistat sovelluksen laitteeltasi, kaikki ladatut tiedot ja käyttöoikeustunnukset poistetaan myös.

## Pilvipalvelun irrottaminen tai kokoonpanon muuttaminen

- Pilvipalvelun asetusten käyttäminen: etsi ensin hallittava pilvipalvelu sovelluksen käyttöliittymässä.
- Napauta '...'-painiketta: palvelun otsikon vieressä näet '...'-painikkeen. Napauta sitä lisävaihtoehtojen käyttämiseksi.
  - **Nimeä uudelleen**: jos haluat muuttaa pilvipalvelun nimen listassasi, valitse 'Nimeä uudelleen'.
  - **Asetukset**: pilvipalvelun kokoonpanon tai todennustietojen muuttamiseksi valitse 'Asetukset'. Joskus voit joutua uudelleenvaltuuttamaan yhdistetyn pilvipalvelun, jos valtuutustoken on vanhentunut.
  - **Irrottaa**: jos haluat katkaista yhteyden sovelluksen ja pilvipalvelun väliltä kokonaan, valitse 'Irrottaa'. Huomaa, että tämän vaihtoehdon valitseminen poistaa kaikki tähän pilvipalveluun liittyvät kappaleet sovelluksen musiikkikirjastosta, mutta ne pysyvät palvelimella.

{{< cards cols="1">}}
  {{< card title="" subtitle="Yhdistetyn pilvipalvelun lisätoimintojen valikko" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Yhdistä tietokoneeseen tai NAS-laitteeseen

Voit myös yhdistää tietokoneesi, henkilökohtaisen NAS-laitteesi tai muut verkkolaitteet käyttämällä SMB-, DLNA- tai WebDAV-protokollaa.

## Yhdistä tietokoneeseen SMB:n avulla

- Napauta 'Yhdistä pilvipalveluun' → SMB.
- Syötä tietokoneen IP-osoite ja jaetun kansion nimi URL-kenttään muodossa smb://tietokoneen-ip-osoite/jaetun-kansion-nimi
- Valitse protokollaversio: Auto, SMB1, SMB2
- Syötä käyttäjätunnus ja salasana (tarvittaessa)
- Napauta 'Valmis'.

Jos yhteys onnistuu, näet yhdistetyn tallennustilan 'Pilvipalvelu'-osiossa.  
Täydellinen opas Mac- tai PC-yhteyden muodostamiseen SMB:n avulla on saatavilla [täältä](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="SMB-yhteysasetukset" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Yhdistä NAS-laitteeseen WebDAV:n avulla

Kaikki vaiheet ovat samat paitsi URL-kentässä.  
URL:n tulee olla muodossa http://palvelimen-nimi tai https://palvelimen-nimi, jos palvelin tukee SSL:ää.
Täydellinen opas NAS-laitteen yhdistämiseen WebDAV-protokollalla on saatavilla [täältä](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="WebDAV-yhteysasetukset" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Yhdistä tietokoneeseen tai NAS-laitteeseen DLNA:n avulla

Voit myös jakaa Windows PC:lle tai henkilökohtaiselle NAS-laitteelle tallennetun musiikkikirjaston DLNA-protokollan avulla ja käyttää sitä sovelluksessa kuten kuvattu [täällä](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA on suosittu ja laajalti käytetty protokolla, mutta se sallii vain musiikin toistamisen tai lataamisen. Et voi ladata tiedostoja tai luoda uusia kansioita palvelimella.

{{< cards cols="1">}}
  {{< card title="" subtitle="DLNA-yhteysasetukset" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Saatavilla olevat laitteet

Tämä osio näyttää kaikki lähiverkossasi olevat laitteet, joihin voit yhdistää sovelluksen kautta.  
Luo yhteys laitteeseen seuraavasti:

- Avaa sovellus ja siirry 'Saatavilla olevat laitteet' -osioon.
- Napauta laitetta, johon haluat yhdistää, listasta.
- Syötä tarvittaessa kirjautumistietosi yhteyden muodostamiseksi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Saatavilla olevat laitteet lähiverkossa" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive on kätevä teknologia, joka mahdollistaa langattoman tiedostonsiirron tietokoneeltasi iOS-laitteellesi työpöytäselaimen kautta.  
Käyttääksesi tätä ominaisuutta tehokkaasti, varmista, että laitteesi ja tietokoneesi on yhdistetty samaan Wi-Fi-verkkoon.  
Tässä on vaiheittainen opas Wi-Fi Driven käyttöön.

## Ota Wi-Fi Drive käyttöön

- Avaa sovellus ja siirry 'Yhteydet'-välilehteen.
- Valitse 'Yhdistä Wi-Fi-verkon kautta' siirtyäksesi Wi-Fi Drive -päänäyttöön.
- Napauta 'Käynnistä Wi-Fi Drive' ottaaksesi Wi-Fi Drive käyttöön.

## Käytä Wi-Fi Drivea tietokoneellasi

- Avaa tietokoneellasi (pöytäkone tai kannettava) selain (kuten Chrome, Firefox tai Safari).
- Syötä selaimen osoitepalkkiin sovelluksen antama URL.

## Siirrä tiedostoja langattomasti

Kun selaimessa aukeaa iOS-laitettasi vastaava verkkosivu, voit helposti vetää ja pudottaa tiedostoja tietokoneeltasi verkkosivulle.  
Vetämäsi ja pudottamasi tiedostot siirretään iOS-laitteellesi ja ne ovat käytettävissä sovelluksessa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive -palvelimen asetukset" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Yksityiskohtaiset ohjeet tiedostojen langattomaan siirtämiseen WiFi-Driven avulla ovat saatavilla [täältä](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing on toinen teknologia, jonka avulla voit siirtää tiedostoja tietokoneelta laitteelle Macin Finder-sovelluksen ja Lightning-kaapelin avulla.  
- Yhdistä vain laite tietokoneeseen kaapelilla ja käynnistä Finder-sovellus Macillasi.
- Avaa 'Sijainnit' → 'Yhdistetty laitteesi' → 'Tiedostot' → ja etsi Evermusic-sovellus.
- Napauta sovelluksen kuvaketta nähdäksesi kaikki jaetut kansiot.
- Kopioi tiedostoja tietokoneelta laitteen jaettuun kansioon vetämällä ja pudottamalla.

Yksityiskohtaiset ohjeet iTunes File Sharingin käyttöön ovat saatavilla [täältä](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing Macilla" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Yhdistä USB-muistikortti

Jos sinulla on SD-kortti, voit yhdistää sen Lightning-kortinlukijan avulla. Sovellus tukee tällä hetkellä Apple Certified -kortinlukijoita ja iXpand Flash Driveja. Jos sinulla on iXpand Flash Drive — aseta se Lightning-porttiin ja avaa sovellus. Näet 'Ulkoinen laite yhdistetty' -viestin ja laitteen tiedot. Napauta flash drive -kuvaketta siirtyäksesi musiikkikansioon ja napauta mitä tahansa äänitiedostoa aloittaaksesi toiston. Yksityiskohtaiset ohjeet USB-muistikortin yhdistämiseen iPhoneen ovat saatavilla [täältä](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Tiedostonhallinta

Kun olet yhdistänyt pilvipalvelun, napauta sen kuvaketta nähdäksesi kaikki saatavilla olevat tiedostot ja kansiot. Voit käyttää sisäänrakennettua tiedostonhallintaa näiden tiedostojen käsittelyyn — lataaminen, uudelleennimeäminen, siirtäminen ja paljon muuta. Kun aloitat latauksen, tiedosto ilmestyy siirtojonoon. Nähdäksesi siirtojonon, siirry 'Paikalliset tiedostot' -välilehteen ja napauta pyöriviä nuolia vasemmassa yläkulmassa. Kaikki ladatut tiedostot ja kansiot ovat käytettävissä 'Paikalliset tiedostot' -osiossa.

## Ylätyökalupalkki

Navigointipalkin alla sijaitseva ylätyökalupalkki tarjoaa useita hyödyllisiä toimintoja. Voit näyttää tai piilottaa sen yksinkertaisella alaspäin pyyhkäisyelkeellä. Käytettävissä olevat toiminnot:

- **Haku**: Tämä vaihtoehto mahdollistaa nopean haun nykyisessä hakemistossa tiettyjen tiedostojen tai kansioiden löytämiseksi.
- **Jatka toistoa**: Jos sovelluksen asetuksissa on otettu käyttöön, tämä ominaisuus palauttaa äänentoisttimen jonon ja viimeisen mediaposition nykyiselle kansiolle.
- **Toista kaikki**: Tämä toiminto skannaa nykyisen kansion ja sen alikansiot lisäten kaikki löydetyt äänitiedostot uuteen soittimeen.
- **Toista satunnaisessa järjestyksessä**: Samanlainen kuin 'Toista kaikki', mutta sekoittaa tiedostot ennen niiden lisäämistä äänentoistimen jonoon.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ylätyökalupalkki pilvisessä kansiossa" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Kansioasetukset

Kun avaat kansion sovelluksessa, löydät kätevän joukon toimintoja napauttamalla '...'-painiketta näytön oikeassa yläkulmassa.  
Tässä on erittely näistä toiminnoista:

- **Valita**: Aktivoi tiedoston valintamoodi. Tämä moodi mahdollistaa yhden tai useamman tiedoston valitsemisen kansiossa.
- **Uusi kansio**: Luo uusi kansio nykyiseen kansioon.
- **Ota offline-tila käyttöön**: Aktivoi offline-tila nykyiselle kansiolle. Se seuraa aktiivisesti kansiota muutosten varalta. Jos lisäät uusia tiedostoja verkkoon, sovellus lataa ne automaattisesti laitteellesi.
- **Lataa tiedostoja**: Lataa tiedostoja laitteeltasi verkkoon.
- **Haku**: Etsi tiettyjä tiedostoja nykyisessä kansiossa.
- **Lajittele**: Lajittele tiedostot kansioissa kriteerien mukaan, kuten nimi, koko tai muokattu päivämäärä.
- **Ruudukko/listakatselunäkymä**: Vaihda taulukkonäkymän ja pikkukuvanäkymän välillä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Nykyisen kansion lisätoimintojen valikko" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Muokkaa verkkotiedostoja

Kun sinun täytyy hallita useita tiedostoja pilvipalvelussa Evermusicillä, voit käyttää valintamoodia. Seuraa näitä ohjeita:

- **Aktivoi valintamoodi**: Avaa sovellus laitteellasi ja siirry pilvipalvelusi sisältävään osioon. Etsi '...' (ellipsis) -painike oikeassa yläkulmassa. Napauta sitä ja valitse 'Valita' aktivoidaksesi valintamoodin.
- **Valitse tiedostoja**: Näet valintaruudut jokaisen tiedoston tai kansion vieressä. Valitse yksi tai useampi napauttamalla valintaruutuja.
- **Suorita erilaisia toimintoja**: Kun olet valinnut hallittavat tiedostot tai kansiot, sinulla on pääsy useisiin toimintoihin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Valintamoodi verkkotiedostoille" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Tiedostotoiminnot

Tiedoston otsikon lähellä näet ellipsis-symbolin '...' (kolme pistettä) — tämä on toimintovalikko.  
Napauta sitä paljastaaksesi käytettävissä olevien toimintojen listan:

- **Toista seuraavana**: Lisää valitun tiedoston soittimen jonosi yläosaan.
- **Toista myöhemmin**: Tämä vaihtoehto lisää tiedoston soittimen jonosi alaosaan.
- **Lisää musiikkikirjastoon**: Tämä toiminto mahdollistaa tiedoston lisäämisen musiikkikirjastoosi.
- **Lisää soittolistaan**: Käytä tätä toimintoa lisätäksesi tiedoston olemassa olevaan soittolistaan tai luodaksesi uuden.
- **Muokata äänitunnisteita**: Tällä vaihtoehdolla voit käyttää Evermusicin sisäänrakennettua tunnistemuokkainta. Tiedosto ladataan väliaikaisesti ja ladataan sitten palvelimelle, kun vahvistat muutokset.
- **Lisää suosikkeihin**: Tämä toiminto lisää tiedoston suosikkitiedostojesi listaan.
- **Ladata**: Valitse tämä toiminto ladataksesi tiedoston tai kansion laitteellesi.
- **Nimeä uudelleen**: Tämä vaihtoehto mahdollistaa tiedoston uudelleennimeämisen suoraan etätallennustilassa.
- **Siirrä**: Valitse tämä toiminto siirtääksesi tiedoston eri kansioon pilvipalvelussasi.
- **Avaa sovelluksessa**: Käytä tätä toimintoa viedäksesi tiedoston toiseen yhteensopivaan sovellukseen.
- **Poistaa**: Ole varovainen tämän toiminnon kanssa, sillä se poistaa tiedoston pysyvästi pilvipalvelustasi. Tätä poistoa ei voi kumota.

{{< cards cols="1">}}
  {{< card title="" subtitle="Yksittäisen tiedoston lisätoimintojen valikko" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Jos toimintojen lista ylittää käytettävissä olevan näyttötilan, vierittää alaspäin toimintovalikossa.

## Kansiotoiminnot

Jokaiselle pilvipalvelusi kansiolle on saatavilla erilaisia toimintoja. Napauta ellipsis-kuvaketta '...' kansion otsikon vieressä. Käytettävissä olevat toiminnot:

- **Toista kaikki**: Korvaa nykyinen soittimen jono kaikilla valitun kansion kohteilla.
- **Toista seuraavana**: Lisää koko kansio soittimen jonon yläosaan.
- **Toista myöhemmin**: Liitä kansion sisältö soittimen jonon alaosaan.
- **Lisää musiikkikirjastoon**: Tämä toiminto integroi kansion sisällön saumattomasti musiikkikirjastoosi.
- **Lisää soittolistaan**: Voit sisällyttää koko kansion soittolistaan; kansion nimi liitetään automaattisesti.
- **Lisää suosikkeihin**: Käytä tätä toimintoa lisätäksesi kansion suosikkitiedostojesi listaan.
- **Ota offline-tila käyttöön**: Aktivoimalla offline-tilan sovellus skannaa jatkuvasti muutoksia ja uudet tiedostot ladataan automaattisesti.
- **Ladata**: Lataa kaikki kansion sisällöt laitteellesi offline-käyttöä varten.
- **Nimeä uudelleen**: Nimeä kansio uudelleen suoraan etätallennustilassa.
- **Siirrä**: Siirrä kansio eri sijaintiin pilvipalvelussasi.
- **Poistaa**: Ole varovainen, sillä tämä toiminto poistaa kansion ja sen sisällön pysyvästi. Tätä toimintoa ei voi kumota.


## Pikakäyttö

Pikakäyttö-osio sijaitsee näytön yläosassa. Se antaa sinulle nopean pääsyn suosikkikansioihisi ja viimeksi avattuihin tiedostoihin yhdistettyjen pilvipalvelujen kautta.
Aina kun avaat tiedoston tai kansion pilvestä, se lisätään 'Äskettäin avattu' -listaan. Tyhjentääksesi tämän listan, avaa 'Äskettäin', napauta 'Lisää toimintoja' -painiketta ja valitse 'Poista lista'. Voit myös merkitä syvälle sisäkkäisiä kansioita Suosikeiksi päästäksesi niihin nopeasti ilman hakemistorakenteen selaamista.

## Muut palvelut

Tässä osiossa näytetään lisäominaisuuksia. Tällä hetkellä sovellus tukee Last.fm-scrobblausta. Kun yhdistetty, toistostatistiikkasi lähetetään automaattisesti Last.fm-tilillesi. Voit vierailla Last.fm-profiilissasi myöhemmin tarkastellaksesi kuunteluanalytiikkaa ja saadaksesi personoituja musiikkisuosituksia. Yksityiskohtaiset asennusohjeet ovat saatavilla [täältä](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
