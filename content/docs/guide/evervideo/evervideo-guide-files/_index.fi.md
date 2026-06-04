---
title: "Tiedostot"
date: 2020-02-01
lastmod: 2026-06-01
description: "Opi käyttämään Tiedostot-välilehteä Evervideossa iPhonella, iPadilla ja Macilla. Yhdistä pilvipalvelut, NAS-laitteet, mediapalvelimet ja RTSP-virrat yhdessä paikassa. Hallinnoi offline-videoita, siirtojonoa, latauksia, Wi-Fi Drivea, iTunes / Finderin tiedostonjakoa ja USB-asemia. Sisältää iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA ja S3-yhteensopivan tallennustilan."
keywords: [
  "Evervideo tiedostot", "Evervideo yhteydet", "Evervideo paikalliset tiedostot",
  "pilvivideon asetukset iPhone", "yhdistä video Google Drive", "SMB videosuoratoisto",
  "WebDAV videosoitin iOS", "DLNA video iPhone", "NAS videosuoratoisto",
  "Wi-Fi Drive videosiirto", "iTunes tiedostonjako Evervideo", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "Evervideo offline-tila video", "Evervideo siirtojono",
  "Evervideo tiedostohallinta", "Evervideo asiakirjakansio",
  "videosoitin Synology", "videosoitin QNAP",
  "videosoitin Apple Time Capsule", "USB DAC video",
  "iXpand videosoitin", "S3 videosoitin"
]
tags: ["opas", "evervideo", "tiedostot", "yhteydet", "pilvi", "NAS", "Plex", "RTSP"]
readingTime: 14
---

Tiedostot-välilehti on Evervideo-sovelluksen all-in-one-tiedostohallinta. Toisin kuin useimmat videosovellukset, jotka jakavat pilvitallennuksen ja paikalliset tiedostot eri välilehtiin, Evervideo yhdistää molemmat yhteen vieritettävään näyttöön, joten voit siirtyä Plex-palvelimelta pilvikansioon iPhonen Asiakirjat-kansioon vaihtamatta välilehtiä.

Tiedostot-välilehti on jaettu selkeisiin osioihin, jotka näkyvät tässä järjestyksessä näytölläsi:

- **Pikakäyttö** — äskettäin katsotut ja suosikit tiedostoille ja kansioille, jotka avasit viimeksi.
- **Tiedostot tässä sovelluksessa** — mitä Evervideo-sovelluksen hiekkalaatikkotettuun Asiakirjat-kansioon on tallennettu.
- **Tiedostot tällä iPhone / iPad / Mac** — videot muualla laitteellasi, jotka näkyvät järjestelmätiedostonvalitsimen kautta.
- **Pilvitallennus** — jokainen yhdistetty pilvitili, NAS ja mediapalvelin.
- **Saatavilla olevat laitteet** — Bonjour / mDNS-tunnistetut palvelimet ja asemat paikallisessa verkossasi.

Tiedostot-näytön oikeassa yläkulmassa on Siirrot-painike (pyörivien nuolten kuvake). Napauta sitä avataksesi Siirtojono, jossa tarkkailet jokaista latausta ja lähetystä kaikista lähteistäsi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo tiedostot yhdistettyjen tallennusten yli" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Yhdistä Pilvitallennukseen

Tiedostot-välilehden Pilvitallennus-osio on paikka, jossa jokainen yhdistetty tili, NAS, mediapalvelin ja virta sijaitsee — rinnakkain yhdessä vieritettävässä listassa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Pilvitallennus-osio Tiedostot-välilehdessä" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Avaa **Tiedostot**-välilehti.
- Vieritä **Pilvitallennus**-osioon.
- Napauta **Yhdistä pilvitallennukseen** valikosta.
- Valitse pilvitallennuspalvelu listasta.
- Syötä tunnistetietosi pilvipalveluntarjoajan virallisella valtuutussivulla ja napauta sitten **Valmis**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Yhdistä pilvipalveluun" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Jos kohtaat ongelmia, tarkista internet-yhteytesi ja käyttäjänimesi / salasanasi. Sovelluksen Premium-versiossa voit lisätä rajattoman määrän palveluja; ilmainen versio tukee enintään kolmea.

## Tuetut Pilvitallennuspalvelut, Mediapalvelimet ja Protokollat

Evervideo tukee poikkeuksellisen laajaa valikoimaa videolähteitä. Kaikki alla toimii yhdestä Yhdistä pilvitallennukseen -virrasta.

**Henkilökohtainen pilvitallennus:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Itse isännöidyt mediapalvelimet:** Plex · Jellyfin · Emby · Subsonic (ja jokainen Subsonic-yhteensopiva palvelin — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (ja ownCloud jaetun API:n kautta) · Synology Drive · QNAP.

**NAS- ja tiedostonjakoprotokolaat:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, salasana tai julkisen avaimen todennus) · NFS · DLNA / UPnP (toisto ja lataus).

**Live- ja IP-kameravirrat:** RTSP — osoita Evervideo mihin tahansa `rtsp://`-osoitteeseen ja se toistaa heti. Loistava turvakameroille, IPTV-virroille, ovikellon kameroille, vauvamonitoreille ja vastaaville live-lähteille.

**S3-yhteensopiva objektitallennus:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ja mikä tahansa muu S3-API-päätepiste.

**Laitteen sisäiset kirjastot:** Kuvat-kirjasto (kaikki videot, näytön tallenteet, kuva-albumit) ja Musiikki-sovelluksen kirjasto (Albumit, Lajit, Soittolistat) — molemmat näkyvät Mediakirjastossa, joten sinun ei tarvitse kopioida mitään.

**Paikallisverkon tunnistaminen:** Saatavilla olevat laitteet -osio listaa automaattisesti kaikki Bonjour / mDNS-palvelut Wi-Fi-verkossasi — Plex, Jellyfin, Emby-palvelimet, Synology, QNAP, AirPort-reitittimet liitetyillä asemilla, Apple Time Capsule — joten voit napauttaa yhdistääksesi ilman IP-osoitteen kirjoittamista.

Jokainen yhteys käyttää palvelun virallista SDK:ta tai avointa protokollaa, OAuth-pohjainen valtuutuksella missä tuettu. Voit yhdistää useita tilejä samasta palvelusta (esimerkiksi kaksi Google Drive -tiliä tai sekä Plex- että Jellyfin-palvelin) ja selata niitä rinnakkain Pilvitallennus-osiossa.

## Turvallisuus ja Yksityisyys

Evervideo käyttää vain virallisia SDK:ita ja suojattuja yhteyksiä vuorovaikutuksessa yhdistettyjen pilvipalvelujen kanssa. Käyttäjänimesi ja salasanasi eivät ole sovelluksen käytettävissä — kaikki siirrot ovat TLS-salattuja.

Kun syötät käyttäjänimesi ja salasanasi, sovellus näyttää sinulle pilvipalveluntarjoajan virallisen valtuutussivun, ja koko valtuutusprosessi tapahtuu sovelluksen ulkopuolella. Pilvipalveluntarjoaja lähettää sitten auth-tokenin sovellukselle onnistuneen valtuutuksen jälkeen, ja kyseistä tokenia käytetään API-kutsuihin.

Auth-token on digitaalinen avain, joka mahdollistaa kolmansien osapuolien sovellusten vuorovaikutuksen pilvitallennuksen kanssa puolestasi. Token tallennetaan laitteellesi Applen turvalliseen järjestelmätallennustilaan (Keychain), joka on salattu levossa ja suojattu laitteen pääsykoodilla tai biometrisellä lukolla. Voit ladata tiedostoja yhdistettyleistä pilvipalveluista laitteellesi; nämä tiedostot sijoitetaan sovelluksen Asiakirjat-hakemistoon ja ne voidaan poistaa milloin tahansa sisäänrakennetun tiedostonhallinnan avulla.

Sovellus ei jaa mitään tietoja yhdistettyistä pilvitileistäsi Everappzille, mainostajille tai kolmansille osapuolille. Voit peruuttaa pääsyn pilvipalvelutiliisi milloin tahansa avaamalla tilin asetusten sivun verkkoselaimessasi.

## Auth-Tokenin Hylkääminen

Peruuttaaksesi auth-tokenin, kirjaudu pilvitilillesi verkkoselaimessa ja siirry suojaus- tai yhdistetyt sovellukset -sivulle. Siellä löydät kaikki kolmannen osapuolen sovellukset, jotka on yhdistetty pilvitiliisi, ja voit poistaa minkä tahansa niistä, jos et enää halua käyttää sitä. Yksityiskohtaiset ohjeet Google-tileille ovat saatavilla [täällä](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Voit myös irrottaa pilvipalvelutilin itse sovelluksen sisällä — kun teet niin, auth-token poistetaan välittömästi laitteeltasi. Jos poistat sovelluksen laitteeltasi, kaikki ladatut tiedot ja käyttötunnukset poistetaan automaattisesti sen mukana.

## Pilvitallennuksen Irrottaminen tai Kokoonpanon Muuttaminen

- **Pääsy pilvitallennusvaihtoehtoihin** — etsi yhdistetty palvelu Tiedostot-välilehden **Pilvitallennus**-osiosta.
- **Napauta "..."-painiketta** palvelun otsikon vieressä avataksesi lisävaihtoehdot:
  - **Nimeä uudelleen** — muuta pilvipalvelun nimeä, kuten se näkyy listassasi.
  - **Asetukset** — muokkaa kokoonpanoa tai todennustietoja. Joskus saatat joutua valtuuttamaan uudelleen yhdistetyn pilvipalvelun, jos valtuutustoken on vanhentunut.
  - **Irrottaa** — katkaise yhteys kokonaan sovelluksen ja pilvipalvelun välillä. Tämä poistaa kaikki kyseiseen palveluun liittyvät videot mediakirjastostasi, mutta jättää ne palvelimelle koskemattomiksi.

## Yhdistäminen Tietokoneeseen tai NASiin

Voit yhdistää tietokoneesi, henkilökohtaisen NASin tai muun verkkolaitteen SMB-, WebDAV-, FTP / FTPS-, SFTP-, NFS- tai DLNA-protokollaa käyttäen. Tämä on helpoin tapa tuoda olemassa oleva kotimediakirjasto — olipa se Macissa, Windows-tietokoneessa, Synologyssa, QNAPissa, Apple Time Capsulessa tai WD My Cloud Homessa — Evervideoon kopioimatta mitään.

### Yhdistäminen Tietokoneeseen SMB:llä

- Napauta **Yhdistä pilvitallennukseen → SMB**.
- Syötä tietokoneen IP-osoite ja jaetun kansion nimi muodossa `smb://computer-ip-address/shared-folder-name`.
- Valitse protokollaversio: **Auto**, **SMB1** tai **SMB2**.
- Syötä käyttäjänimesi ja salasanasi (jos tarvitaan).
- Napauta **Valmis**.

Jos yhteys onnistuu, jako näkyy Pilvitallennus-osiossa. Täydellinen opaskirja Mac- tai PC-tietokoneesi yhdistämisestä SMB:llä on saatavilla [täällä](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Yhdistäminen NASiin WebDAV:lla

Kaikki vaiheet ovat samat kuin SMB:ssä, paitsi URL-kenttä. Käytä `http://server-name` tai `https://server-name` jos palvelin tukee SSL:ää. WebDAV toimii Synologyn, QNAPin, Nextcloudin, ownCloudin, WD My Cloud Homen ja minkä tahansa muun WebDAV-päätepisteellä varustetun palvelimen kanssa.

Täydellinen WebDAV-opaskirja on saatavilla [täällä](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Yhdistäminen DLNA / UPnP:llä

Jaa mediakirjasto Windows-tietokoneellasi tai NASilla DLNA / UPnP-protokollaa käyttäen ja käytä sitä Evervideossa kuten kuvattu [täällä](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA on laajasti tuettu, mutta sen avulla voit vain toistaa tai ladata videoita — et voi ladata tiedostoja tai luoda uusia kansioita DLNA-palvelimelle.

### Yhdistäminen FTP:llä, FTPS:llä tai SFTP:llä

Evervideo tukee myös klassisia tiedostonsiirtoprotokollia. Yhdistääksesi palvelimen FTP:llä tai FTPS:llä, napauta Yhdistä pilvitallennukseen → FTP, syötä isäntäosoite muodossa `ftp://server-name` (tai `ftps://server-name` salatulle yhteydelle), anna käyttäjänimesi ja salasanasi, napauta sitten Valmis. SFTP:lle (SSH File Transfer Protocol) valitse SFTP ja anna joko salasana tai SSH-avainpari.

### Yhdistäminen NFS-jakoon

Evervideo sisältää NFS (Network File System) -tuen — kätevä Linux-isännille, BSD-palvelimille ja NAS-laitteille, jotka haluavat näyttää videokirjastot NFS:n kautta SMB:n sijaan. Valitse NFS Yhdistä pilvitallennukseen -valikosta, syötä palvelinosoite ja viedty polku, napauta Valmis.

## Plex Media Serverin Yhdistäminen

Evervideo voi yhdistää suoraan Plex Media Serveriin ja selata elokuva-, TV-ohjelma- ja kotivideokirjastojasi. Napauta Yhdistä pilvitallennukseen → Plex, kirjaudu Plex-tililläsi, valitse palvelin, ja kirjasto näkyy pilvipalvelujesi rinnalla. Samassa paikallisverkossa olevat Plex-palvelimet löydetään myös automaattisesti Saatavilla olevat laitteet -osiossa.

## Jellyfin- tai Emby-Palvelimen Yhdistäminen

Sekä Jellyfin (avoimen lähdekoodin) että Emby (kaupallinen) mediapalvelimet toimivat natiivisti Evervideossa. Napauta Yhdistä pilvitallennukseen → Jellyfin tai Emby, syötä palvelimesi URL (tyypillisesti jotain `http://server-ip:8096`) ja tunnistetiedot, ja kirjastosi on valmis toistettavaksi.

## Subsonic- tai Navidrome-Palvelimen Yhdistäminen

Evervideo puhuu Subsonic API:a, mikä tarkoittaa, että se toimii itse Subsonicin, Navidrömen ja kaikkien muiden Subsonic-yhteensopivien palvelimien kanssa — mukaan lukien Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) ja Ampache. Napauta Yhdistä pilvitallennukseen → Subsonic, syötä palvelimen URL ja tunnistetiedot, ja kirjasto näkyy Pilvitallennus-osiossa.

## RTSP-Virran Yhdistäminen (IP-Kamerat, Live-TV, IPTV)

Evervideolla on natiivi RTSP-tuki, joten voit osoittaa sen mihin tahansa RTSP-lähteeseen — turvakamerat, oven kamerat, IPTV-tarjoajat, vauvamonitorit, lähetysvirrat — ja Evervideo vetää ja dekoodaa virran reaaliajassa. Napauta Online-linkit → Lisää linkki, liitä täydellinen URL (`rtsp://camera-ip:port/stream-path`), anna käyttäjänimi ja salasana tarvittaessa, napauta Valmis.

## Yhdistäminen S3-Yhteensopivaan Objektitallennukseen

Itse isännöiville ja tehokäyttäjille, jotka käyttävät pilviolijektiallennusta, Evervideo sisältää S3-yhteensopivan liittimen. Napauta Yhdistä pilvitallennukseen → S3-tallennus, syötä sitten päätepisteosoite, alue, käyttöavain, salainen avain ja bucket-nimi. Tämä toimii AWS S3:lla, Backblaze B2:lla, Wasabilla, Cloudflare R2:lla, MinIO:lla, DigitalOcean Spacesilla ja millä tahansa muulla S3-API-päätepisteellä.

## Saatavilla Olevat Laitteet

Tässä osiossa näkyvät kaikki paikalliverkossasi olevat laitteet, joihin voit yhdistää Evervideosta Bonjour / mDNS-tunnistuksen kautta — Plex, Jellyfin, Emby-palvelimet, Synology, QNAP, AirPort-reitittimet liitetyillä asemilla, Apple Time Capsule jne. Yhteyden muodostamiseksi:

- Vieritä Saatavilla olevat laitteet -osioon Tiedostot-välilehdessä.
- Napauta laitetta, johon haluat yhdistää.
- Tarvittaessa syötä kirjautumistietosi viimeistelläksesi yhteyden.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Saatavilla Olevat Laitteet Paikallisverkossa" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive mahdollistaa tiedostojen siirtämisen langattomasti tietokoneeltasi iOS-laitteellesi minkä tahansa pöytäkoneen selaimen, Finderin tai Resurssienhallinnon kautta. Laitteesi ja tietokoneesi on oltava samassa Wi-Fi-verkossa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Driven Ottaminen Käyttöön

- Tiedostot-välilehdessä vieritä Pilvitallennus → Yhdistä Wi-Fin kautta avataksesi Wi-Fi Driven päänäytön.
- (Valinnainen) Aseta käyttäjänimi ja salasana sisäänrakennetulle web-palvelimelle.
- Napauta Käynnistä Wi-Fi Drive.

### Wi-Fi Driven Käyttö Tietokoneeltasi

- Avaa verkkoselain tietokoneellasi (Chrome, Firefox, Safari jne.).
- Syötä sovelluksen näyttämä URL.
- Vedä ja pudota tiedostoja tietokoneeltasi verkkosivulle — ne alkavat siirtyä iOS-laitteellesi.

Voit myös liittää Wi-Fi Driven suoraan **Finderiin** macOS:ssä (Siirry → Yhdistä palvelimeen…) tai Resurssienhallintaan Windowsissa (Yhdistä verkkoasema…) ja käsitellä iPhoneasi tai iPadiasi tavallisena verkkoasemana.

Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finderin Tiedostonjako

iTunes-tiedostonjako (nyt Finder-tiedostonjako macOS Catalinassa ja uudemmissa) mahdollistaa tiedostojen siirtämisen Lightning- tai USB-C-kaapelilla. Yhdistä laite, avaa Finder Macissa (tai iTunes Windowsissa), etsi Evervideo sovellushakemistosta ja kopioi tiedostoja sen jaettuun kansioon.

## USB Flash -Aseman tai SD-Kortin Yhdistäminen

Liitä USB-asema tai SD-kortti iPhoneen, iPadiin tai Maciin Lightning-USB / USB-C -sovittimen tai kortinlukijan kautta. Avaa Tiedostot → Tiedostot tällä iPhonella → Avaa kansio, siirry asemaan ja valitse videotiedosto tai kansio. Evervideo toistaa tiedostot suoraan asemalta kopioimatta niitä sisäiseen tallennustilaan — kätevä erittäin suurille 4K-kirjastoille.

## Kansioiden Selaaminen Yhdistetyissä Tallennuksissa

Napauta mitä tahansa yhdistettyä pilvipalvelua avataksesi sen tiedostonselaimen. Kansiot näyttävät videopienoiskuvia kun saatavilla, ja videon napauttaminen aloittaa toiston välittömästi samalla kun tiedoston loppuosa jatkaa suoratoistoa taustalla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Kansioiden selaaminen yhdistetyissä tallennuksissa" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Pikakäyttö

Pikakäyttö-osio sijaitsee Tiedostot-välilehden yläosassa. Se antaa sinulle nopean pääsyn suosikki- ja äskettäin avattuihin tiedostoihin ja kansioihin — sekä pilvipalveluista että laitteen tallennuksesta. Aina kun avaat tiedoston tai kansion pilvestä, se lisätään Äskettäin avattujen listaan. Voit merkitä syvälle sisäkkäisiä kansioita Suosikeiksi päästäksesi niihin nopeasti ilman hakemistorakenteen läpikäymistä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Online-linkit ja Pikakäyttö" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Tiedostot Tässä Sovelluksessa

Tässä osiossa näkyvät tiedostot ja kansiot, jotka on tallennettu Evervideo-sovelluksen hiekkalaatikkotettuun Asiakirjat-hakemistoon — kaikki, mitä olet ladannut pilvestä, siirtänyt Wi-Fi Driven kautta, kopioinut Finder-tiedostonjaon kautta tai tuonut toisesta sovelluksesta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Tiedostot tässä sovelluksessa" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Asiakirjat-Kansio

Asiakirjat-kansio on kaiken juuri Tiedostot tässä sovelluksessa -osiossa. Voit luoda alikansioita, nimetä tiedostoja uudelleen, siirtää niitä ja ryhmitellä ne haluamallasi tavalla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Paikalliset tiedostot — Asiakirjat-kansio" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Tiedostot Tällä iPhone / iPad / Mac

Tässä osiossa näkyvät laitteellasi olevat videot, mutta eri sovelluksissa. Voit tuoda ne Evervideoon järjestelmätiedostonvalitsimella:

- Napauta Avaa tiedostot… valitaksesi tiettyjä tiedostoja.
- Napauta Avaa kansio… valitaksesi kokonaisen kansion.

Voit myös käyttää Yhdistä kansio -toimintoa luodaksesi linkin laitteellasi olevaan kansioon luku- / kirjoitusoikeuksilla — täydellinen iCloud Drive -kansion tai liitetyn USB-aseman käyttöön kopioimatta mitään.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Tiedostot tällä laitteella" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Erikoiskansiot

Tiedostot-välilehdessä näet useita erikoiskansioita, joita Evervideo luo ja käyttää automaattisesti:

- **Lataukset** — jokainen pilvestä ladattu tiedosto näkyy täällä oletuksena. Mukauta kohdassa Asetukset → Tiedostohallinta → Tallenna ladatut tiedostot.
- **Soittimen välimuisti** — mediasoittimen välimuisti. Oletuksena soitin lataa tulevia videoita sujuvan toiston varmistamiseksi. Voit poistaa välimuistin käytöstä sovelluksen asetuksissa tai yksinkertaisesti poistaa tämän kansion.
- **iCloud** — tässä kansiossa olevat tiedostot synkronoidaan kaikilla laitteillasi, jotka on yhdistetty samaan iCloud-tiliin.
- **Offline-kansiot** — kun merkitset kansion, soittolistan, albumin tai lajin offline-käytettäväksi, tiedostot ladataan tähän kansioon.

## Ylätyökalupalkki

Navigointipalkin alla oleva ylätyökalupalkki tarjoaa useita toimintoja, jotka voit näyttää tai piilottaa alaspäin pyyhkäisemällä:

- **Haku** — suorita haku nykyisessä kansiossa tai osiossa.
- **Jatka toistoa** — jos asetuksissa on käytössä, palauta soittimen jono ja viimeinen videosijainti nykyiselle kansiolle.
- **Toista kaikki** — skannaa nykyinen kansio ja sen alikansiot ja lisää tiedostot soittimen jonoon.
- **Sekoita kaikki** — kuten Toista kaikki, mutta sekoittaa ennen lisäämistä.

## Kansion Vaihtoehdot

Kun avaat kansion, napauta **"..."**-painiketta oikeassa yläkulmassa näiden toimintojen saamiseksi:

- **Valita** — aktivoi tiedoston valintamoodi.
- **Uusi kansio** — luo uusi kansio nykyisen kansion sisälle.
- **Ota offline-tila käyttöön** — ota offline-synkronointi käyttöön nykyiselle kansiolle. Verkossa lisätyt uudet tiedostot ladataan automaattisesti.
- **Lataa tiedostoja** — lataa tiedostoja laitteeltasi online-kansioon.
- **Haku** — hae kansion sisältä.
- **Lajittele** — lajittele tiedostot nimen, koon, muokkauspäivämäärän tai metatietojen mukaan.
- **Ruudukko / Listaasetus** — vaihda taulukoitunäkymän ja pienoiskuvanäkymän välillä. Pienoiskuvanäkymässä näkyvät suuret videoposter-esikatselut.

## Valintamoodi

Napauta **"..."** oikeassa yläkulmassa ja valitse **Valita** aktivoidaksesi valintamoodin. Jokaisen tiedoston ja kansion vieressä näkyvät valintaruudut. Napauta valitaksesi yhden tai useamman kohteen, suorita sitten erätoimintoja: Toista seuraavaksi, Toista myöhemmin, Lisää mediakirjastoon, Lisää soittolistaan, Kopioi, Lataa, Siirrä, Nimeä uudelleen tai Poista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo valintamoodi tiedostohallinnassa" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Jos haluat mieluummin käsitellä yhdistettyä pilvitallennusta vain luku -tilassa (vahingollisten poistojen estämiseksi), ota käyttöön Asetukset → Tiedostohallinta → Muokkaa online-tiedostoja → Pois käytöstä piilottaaksesi kaikki tuhoavat toiminnot käyttöliittymästä.

## Tiedostotoiminnot

Napauta **"..."**-kuvaketta tiedoston otsikon lähellä paljastaaksesi toimintovalikon:

- **Toista seuraavaksi** — lisää tiedosto soittimen jonon alkuun.
- **Toista myöhemmin** — lisää tiedosto soittimen jonon loppuun.
- **Lisää mediakirjastoon** — sisällytä tiedosto mediakirjastoosi, järjestettynä albumin ja lajin mukaan.
- **Lisää soittolistaan** — lisää tiedosto olemassa olevaan soittolistaan tai luo uusi.
- **Muokata äänitunnisteita** — avaa sisäänrakennettu tunnisteiden muokkausohjelma metatietojen muuttamiseksi. Online-tiedostoille tiedosto ladataan tilapäisesti, muokataan ja ladataan uudelleen vahvistuksesi jälkeen.
- **Lisää suosikkeihin** — lisää tiedosto suosikillistasi pikakäyttöä varten.
- **Ladata** — lataa tiedosto tai kansio laitteellesi offline-käyttöä varten.
- **Nimeä uudelleen** — nimeä tiedosto uudelleen suoraan etätallennuksessa.
- **Siirrä** — siirrä tiedosto eri kansioon pilvitallennuksessasi.
- **Lisää arkistoon** — niputa tiedosto yksittäiseen ZIP-tiedostoon (Premium-ominaisuus).
- **Avaa sovelluksessa** — vie tiedosto toiseen yhteensopivaan sovellukseen järjestelmän Jaa-arkin kautta.
- **Poistaa** — poista tiedosto pysyvästi. **Tätä toimintoa ei voi kumota.**

## Kansiotoiminnot

Jokaiselle pilvitallennuksessasi olevalle kansiolle on monia toimintoja saatavilla napauttamalla **"..."**-kuvaketta kansion otsikon vieressä.

- **Toista kaikki** — korvaa nykyinen soittimen jono kaikilla kansion videoilla.
- **Toista seuraavaksi / Toista myöhemmin** — lisää koko kansio jonoon.
- **Lisää mediakirjastoon** — sisällytä kansion sisältö mediakirjastoosi.
- **Lisää soittolistaan** — lisää koko kansio soittolistaan.
- **Lisää suosikkeihin** — lisää kansio suosikkeihisi.
- **Ota offline-tila käyttöön** — pelkän latauksen lisäksi tämä seuraa jatkuvasti kansiota uusien tiedostojen varalta ja lataa ne automaattisesti niiden ilmestyessä verkossa.
- **Ladata** — lataa kaikki kansion sisällöt laitteellesi offline-käyttöä varten.
- **Nimeä uudelleen / Siirrä** — nimeä uudelleen tai siirrä kansio etätallennuksessa.
- **Lisää arkistoon** — niputa kansion sisällöt ZIP-tiedostoon (Premium-ominaisuus).
- **Poistaa** — poista kansio ja sen sisältö pysyvästi. **Tätä toimintoa ei voi kumota.**

## Siirtojono

Tiedostot-välilehden oikeassa yläkulmassa on **Siirrot**-painike (pyörivien nuolten kuvake). Napauta sitä avataksesi Siirtojono — luettelo kaikista aktiivisista latauksista ja lähetyksistä kaikissa lähteissäsi reaaliaikaisella edistymisellä, nopeudella ja ETA:lla per tiedosto.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Tiedostojen siirtojono" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Voit keskeyttää, jatkaa, yrittää uudelleen epäonnistuneita siirtoja, järjestää kohteita uudelleen priorisoidaksesi tiettyjä latauksia tai peruuttaa niitä yksitellen. Voit myös säätää siirtojonon nopeutta (enimmäismäärä rinnakkaisia tehtäviä), verkkotyyppiä (vain Wi-Fi tai Wi-Fi + mobiilidata) ja taustasiirtoja kohdassa Asetukset → Tiedostohallinta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Toiminnot tiedostojen siirtojonossa" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Offline-Tila ja Synkronoidut Offline-Kansiot

Offline-tila on kätevä ominaisuus, jonka avulla voit katsella suosikkivideoitasi, vaikka et olisi yhteydessä internetiin. Kun otat offline-tilan käyttöön mille tahansa kansiolle, soittolistalle, albumille tai lajille, kaikki kyseisen kokoelman tiedostot ladataan automaattisesti laitteellesi offline-toistoa varten. Ne näkyvät Offline-kansiot-osiossa.

Kun lisäät uusia tiedostoja etäpalvelimelle, ne ladataan myös automaattisesti — joten offline-kokoelmasi pysyy ajan tasalla ilman, että sinun tarvitsee tehdä mitään. Synkronoidaksesi manuaalisesti uudelleen, napauta kolmea pistettä offline-kansion oikeassa yläkulmassa ja valitse Synkronoida.

Voit säätää synkronointiaikakatkaisua kohdassa Asetukset → Tiedostohallinta → Synkronoidut offline-kansiot → Aikaväli.

Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personointi

Kohdassa Asetukset → Personointi voit määrittää, miten Tiedostot-välilehti esitetään:

- **Tiedostonäytön tyyli** — Yksinkertainen valikko (näyttää kansiolistan suoraan) tai Ryhmitelty valikko (ryhmittelee sisällön kategorian mukaan — Pikakäyttö, Erikoiskansiot, Pilvitallennus jne.).
