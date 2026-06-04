---
title: "Yhteydet"
date: 2020-02-01
description: "Opi yhdistämään pilvipalveluja ja NAS-laitteita Flacboxiin. Suoratoista korkearesoluutioista musiikkia iCloud Drivesta, Dropboxista, Google Drivesta, OneDrivesta, MEGAsta, Boxista, pCloudista, Synology Drivesta, Yandex Diskistä ja muualta. Käytä SMB:tä, WebDAVia, DLNAa, FTP / SFTP:tä, Wi-Fi Drivea, iTunes / Finder File Sharingia ja USB-muistitikkuja."
keywords: [
  "Flacbox cloud-asetukset", "Google Driven yhdistäminen Flacboxiin", "SMB musiikin suoratoisto",
  "WebDAV iOS-toistin", "DLNA musiikkisovellus", "NAS äänen suoratoisto", "Wi-Fi Drive iPhone",
  "tiedostojen siirto iPhoneen", "Flacbox iTunes File Sharing", "NAS:n yhdistäminen iPhoneen",
  "Synology Drive musiikkisovellus", "QNAP musiikkisovellus", "Bluesound musiikkisovellus",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "Last.fm scrobbling musiikkisovellus",
  "iXpand Flash Drive musiikki", "USB DAC iPhone"
]
tags: ["opas", "flacbox", "yhteydet", "cloud", "NAS"]
readingTime: 12
---


Tällä näytöllä voit yhdistää jokaisen lähteen, joka sisältää musiikkiasi. Voit integroida suosittuja pilvipalveluja kuten Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive ja paljon muuta, sekä Mac-, PC- tai NAS-laitteesi vakioprotokollia käyttäen.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Yhteydet-näyttö" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Yhdistäminen Pilvivarastoon

- Avaa **Yhteydet**-välilehti.
- Valitse **Yhdistä pilvivarastoon** valikosta.
- Valitse pilvivarastopalvelu luettelosta.
- Anna tunnistetietosi pilvipalveluntarjoajan virallisella valtuutussivulla ja napauta sitten **Valmis**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lisää Pilvivarastopalvelu" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Jos kohtaat ongelmia, tarkista internet-yhteytesi ja kirjautumistietosi. Premium-versiossa voit lisätä rajattoman määrän palveluja; ilmaisversiossa enintään kolme.

## Tuetut Pilvivarastopalvelut, Mediapalvelimet ja Protokollat

Flacbox tukee poikkeuksellisen laajaa valikoimaa lähteitä musiikillesi.

**Henkilökohtainen pilvivarasto:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Itse isännöidyt palvelimet:** Plex · Jellyfin · Emby · Subsonic (ja jokainen yhteensopiva palvelin — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (ja ownCloud jaetun API:n kautta) · Synology Drive · QNAP.

**NAS- ja tiedostonjako-protokollat:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, salasana tai julkisen avaimen todennus) · NFS · DLNA / UPnP (toisto ja lataus).

**S3-yhteensopiva objektivarastointi:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ja mikä tahansa muu S3-API-päätepiste.

**Paikallisverkon löytäminen:** Saatavilla olevat laitteet -osio listaa automaattisesti kaikki Bonjour / mDNS-palvelut Wi-Fi-verkossasi.

## Turvallisuus ja Tietosuoja

Käytämme vain virallisia SDK-kirjastoja ja suojattuja yhteyksiä vuorovaikutuksessa yhdistettyjen pilvipalvelujen kanssa. Kirjautumistietosi eivät ole sovelluksen käytettävissä — kaikki siirrot ovat TLS-salattuja.

Auth-token tallennetaan laitteellesi Applen turvallisessa järjestelmätallenteessa (Keychain).

Sovellus ei jaa mitään tietoja yhdistettyistä pilvitileistäsi Everappzin, mainostajien tai kolmansien osapuolien kanssa.

## Auth-Tokenin Peruuttaminen

Peruuttaaksesi auth-tokenin, kirjaudu pilvitilillesi selaimessa ja siirry suojaus- tai yhdistetyt sovellukset -sivulle. Yksityiskohtaiset ohjeet Google-tileille ovat saatavilla [täällä](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

## Pilvivaraston Irrottaminen tai Asetusten Muuttaminen

- **Pilvivarastoon pääsy** — etsi yhdistetty palvelu **Yhteydet**-näytöltä.
- **Napauta "..."-painiketta** palvelun nimen vieressä:
  - **Nimeä uudelleen** — muuta pilvipalvelun nimeä luettelossasi.
  - **Asetukset** — muuta asetuksia tai todennustietoja.
  - **Irrottaa** — katkaise yhteys kokonaan sovelluksen ja pilvipalvelun välillä.

## Yhdistäminen Tietokoneeseen tai NAS:iin

Voit myös yhdistää tietokoneesi, henkilökohtaisen NAS-laitteen tai muita verkkolaitteita SMB-, DLNA- tai WebDAV-protokollilla.

## Yhdistäminen Tietokoneeseen SMB:llä

- Napauta **Yhdistä pilvivarastoon → SMB**.
- Syötä tietokoneen IP-osoite ja jaetun kansion nimi URL-kenttään: `smb://tietokoneen-ip-osoite/jaettu-kansio`.
- Valitse protokollaversio: **Auto**, **SMB1** tai **SMB2**.
- Syötä kirjautumistietosi (tarvittaessa).
- Napauta **Valmis**.

Täydellinen opas on saatavilla [täällä](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## NAS:iin Yhdistäminen WebDAVilla

Kaikki vaiheet ovat samat kuin SMB:ssä, paitsi URL-kenttä. URL:n tulee olla muodossa `http://palvelin-nimi` tai `https://palvelin-nimi`. WebDAV toimii **Synologyn, QNAPin, Nextcloudin, ownCloudin** ja monien muiden palvelinten kanssa.

Täydellinen opas on saatavilla [täällä](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Tietokoneeseen tai NAS:iin Yhdistäminen DLNAlla

Voit myös jakaa musiikkikirjaston DLNA / UPnP-protokollan kautta, kuten kuvataan [täällä](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone).

## NAS:iin tai Palvelimeen Yhdistäminen FTP:llä, FTPS:llä tai SFTP:llä

Napauta **Yhdistä pilvivarastoon → FTP**, syötä palvelimen URL muodossa `ftp://palvelin-nimi` (tai `ftps://palvelin-nimi`), anna kirjautumistiedot ja napauta **Valmis**. **SFTP**:lle valitse **SFTP** ja anna joko salasana tai SSH-avainpari.

## NFS-Jaon Yhdistäminen

Flacbox sisältää **NFS** (Network File System) -tuen. Valitse **NFS** **Yhdistä pilvivarastoon** -valikosta, syötä palvelimen osoite ja vientireitti ja napauta **Valmis**.

## Plex Media Serverin Yhdistäminen

Napauta **Yhdistä pilvivarastoon → Plex**, kirjaudu Plex-tililläsi, valitse palvelin ja kirjasto ilmestyy pilvipalvelujesi rinnalle.

## Jellyfin- tai Emby-Palvelimen Yhdistäminen

Napauta **Yhdistä pilvivarastoon → Jellyfin** tai **Emby**, syötä palvelimen URL ja tunnistetiedot, ja musiikkikirjastosi on valmis toistettavaksi.

## Subsonic- tai Navidrome-Palvelimen Yhdistäminen

Napauta **Yhdistä pilvivarastoon → Subsonic**, syötä palvelimen URL ja tunnistetiedot ja kirjasto ilmestyy Yhteydet-näyttöön.

## S3-Yhteensopivaan Objektivarastoon Yhdistäminen

Napauta **Yhdistä pilvivarastoon → S3-varasto**, syötä sitten päätepiste-URL, alue, pääsyavain, salainen avain ja bucket-nimi.

## Saatavilla Olevat Laitteet

Tässä osiossa näkyy jokainen laite paikallisverkossasi, johon voit yhdistää Bonjour-löytämisen kautta.

- Avaa sovellus ja siirry **Saatavilla olevat laitteet** -osioon Yhteyksissä.
- Napauta laitetta, johon haluat yhdistää.
- Syötä tarvittaessa kirjautumistietosi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Saatavilla Olevat Laitteet Paikallisverkossa" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive on kätevä teknologia, joka mahdollistaa langattoman tiedostonsiirron tietokoneelta iOS-laitteellesi minkä tahansa pöytäselaimen kautta.

### Wi-Fi Driven Käyttöönotto

- Avaa sovellus ja siirry **Yhteydet**-välilehdelle.
- Valitse **Yhdistä Wi-Fi:n kautta** päästäksesi Wi-Fi Drive -päänäyttöön.
- (Valinnainen) Aseta käyttäjätunnus ja salasana upotettu verkkopalvelimelle.
- Napauta **Käynnistä Wi-Fi Drive**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Wi-Fi Driven Käyttö Tietokoneella

- Avaa tietokoneellasi selain (Chrome, Firefox tai Safari).
- Kirjoita selaimen osoiteriville sovelluksen antama URL.

### Tiedostojen Langaton Siirto

Kun iOS-laitteesi verkkosivu avautuu selaimessa, voit vetää ja pudottaa tiedostoja tietokoneelta sille.

Voit myös liittää Wi-Fi Driven suoraan Finderiin macOS:ssä (Siirry → Yhdistä palvelimeen…) tai Resurssienhallintaan Windowsissa (Yhdistä verkkolevy…).

Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (nyt Finder File Sharing macOS Catalinassa ja uudemmissa) on toinen tapa siirtää tiedostoja Lightning- tai USB-C-kaapelilla.

- Yhdistä laite tietokoneeseen kaapelilla ja avaa **Finder** Macilla (tai **iTunes** Windowsissa).
- Avaa **Sijainnit → Yhdistetty laitteesi → Tiedostot** ja etsi Flacbox-sovellus.
- Napauta sovelluksen kuvaketta nähdäksesi kaikki jaetut kansiot.
- Kopioi tiedostoja vetämällä ja pudottamalla.

Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## USB-Muistitikun Yhdistäminen

Jos sinulla on SD-kortti tai USB-asema, voit yhdistää sen Lightning-USB/SD-kortinlukijalla tai USB-C-asemalla (iPadilla ja iPhone 15 / 16 / 17 / Pro:lla).

Yksityiskohtaiset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Tiedostohallinta

Kun olet yhdistänyt pilvivarastopalvelun, napauta sen kuvaketta nähdäksesi kaikki saatavilla olevat tiedostot ja kansiot.

## Ylätyökalupalkki

Ylätyökalupalkki tarjoaa useita hyödyllisiä toimintoja.

- **Hae** — nopea haku nykyisessä hakemistossa.
- **Jatka toistoa** — palauttaa äänisoittimen jonon ja viimeisen mediasijainnin nykyiselle kansiolle.
- **Toista kaikki** — skannaa nykyisen kansion ja sen alikansiot ja lisää kaikki löydetyt äänitiedostot uuteen jonoon.
- **Toista kaikki satunnaisessa järjestyksessä** — kuten Toista kaikki, mutta sekoittaa tiedostot ensin.

## Kansion Asetukset

Kun avaat kansion, löydät toimintoja napauttamalla **"..."**-painiketta oikeassa yläkulmassa.

- **Valita** — aktivoi tiedostojen valintatilaisen.
- **Uusi kansio** — luo uuden kansion nykyiseen kansioon.
- **Ota offline-tila käyttöön** — ota offline-tila käyttöön nykyiselle kansiolle.
- **Lataa tiedostoja** — lataa tiedostoja laitteeltasi online-kansioon.
- **Hae** — etsi tiettyjä tiedostoja.
- **Lajittele** — lajittele tiedostoja nimen, koon, muokkauspäivän tai metatietojen mukaan.
- **Ruudukko / Lista** — vaihda taulukkonäkymän ja pikkukuvanäkymän välillä.

## Online-Tiedostojen Muokkaaminen

Useiden tiedostojen hallintaan käytä **Valintatilaa**:

- **Aktivoi valintatila** — napauta **"..."** oikeassa yläkulmassa ja valitse **Valita**.
- **Valitse tiedostot** — valintaruudut ilmestyvät jokaisen tiedoston ja kansion viereen.
- **Suorita toimintoja** — Toista seuraavaksi, Toista myöhemmin, Lisää musiikkikirjastoon, Lisää soittolistaan, Kopioi, Lataa, Siirrä, Nimeä uudelleen ja Poistaa.

## Tiedostotoiminnot

Napauta tiedoston nimen vieressä olevaa **"..."**-kuvaketta avataksesi toimintovalikon:

- **Toista seuraavaksi** — lisää tiedosto soittimen jonon alkuun.
- **Toista myöhemmin** — liitä tiedosto jonon loppuun.
- **Lisää musiikkikirjastoon** — liitä tiedosto musiikkikirjastoosi.
- **Lisää soittolistaan** — lisää olemassa olevaan soittolistaan tai luo uusi.
- **Muokata äänitunnisteita** — avaa sisäänrakennettu tunniste-editori.
- **Lisää suosikkeihin** — lisää suosikkiluetteloosi.
- **Ladata** — lataa tiedosto tai kansio offline-käyttöön.
- **Nimeä uudelleen** — nimeä tiedosto uudelleen suoraan etätallenteessa.
- **Siirrä** — siirrä tiedosto eri kansioon.
- **Avaa sovelluksessa** — vie tiedosto toiseen yhteensopivaan sovellukseen.
- **Poistaa** — poista tiedosto pysyvästi pilvivarastostasi. **Tätä toimintoa ei voi peruuttaa.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Lisää toimintoja tiedostolle yhdistetyssä pilvivarastossa" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Kansiotoiminnot

Jokaiselle kansiolle napauta **"..."**-kuvaketta kansion nimen vieressä:

- **Toista kaikki** — korvaa nykyinen soittojono.
- **Toista seuraavaksi** — lisää koko kansio jonon alkuun.
- **Toista myöhemmin** — liitä kansion sisältö jonon loppuun.
- **Lisää musiikkikirjastoon** — liitä kansion sisältö kirjastoon.
- **Lisää soittolistaan** — lisää koko kansio soittolistaan.
- **Lisää suosikkeihin** — lisää kansio suosikkeihin.
- **Ota offline-tila käyttöön** — tarkkaile kansiota jatkuvasti uusien tiedostojen varalta.
- **Ladata** — lataa kaikki sisältö.
- **Nimeä uudelleen** — nimeä kansio uudelleen.
- **Siirrä** — siirrä eri sijaintiin.
- **Arkistoi (ZIP)** — pakkaa kansion sisältö yhdeksi ZIP-tiedostoksi (Premium-ominaisuus).
- **Poistaa** — poista pysyvästi. **Tätä toimintoa ei voi peruuttaa.**

## Pikakäyttö

Pikakäyttö-osio sijaitsee näytön yläosassa ja antaa nopean pääsyn suosikki- ja äskettäin avattuihin tiedostoihin yhdistettyistä pilvipalveluista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Online-linkit ja Pikakäyttö" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Muut Palvelut

Tässä osiossa näytetään lisäominaisuuksia. Tällä hetkellä sovellus tukee **Last.fm**-scrobblausta — kun se on yhdistetty, toistotilastosi lähetetään automaattisesti Last.fm-tilillesi. Yksityiskohtaiset asennusohjeet ovat saatavilla [täällä](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Last.fm Yhdistäminen" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
