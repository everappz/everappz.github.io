---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Opi käyttämään Evervideota — all-in-one-pilviviestintoistinta iPhonelle, iPadille ja Macille. Suoratoista ja lataa videoita iCloud Drivesta, Google Drivesta, Dropboxista, OneDrivesta, MEGAsta, Boxista, pCloudista, Synologysta, QNAPilta, NASilta, WebDAV:lla, SMB:llä, NFS:llä, FTP / SFTP:llä, DLNAlla ja S3:lla — sekä Plexistä, Jellyfinistä, Embystä, Sonicista ja Navidrömestä. Picture-in-Picture, ensisijaiset ja toissijaiset tekstitykset, ääni- ja videotaajuuskorjaimet, RTSP IP-kamera-virrat, Chromecast, AirPlay 2, laitteistokiihdytetty H.264/HEVC-dekoodaus, Kuvat- ja Apple Music -kirjaston integrointi sekä kompakti aina näytöllä oleva soitin.'
keywords: [
  "Evervideo-opas", "kuinka käyttää Evervideoita", "pilvivideosoitin iPhone", "videosoitin Mac",
  "MKV-soitin iOS", "FFmpeg-videosoitin", "HEVC-videosoitin iPhone",
  "Picture-in-Picture video iPhone", "PiP-videosoitin iPad",
  "RTSP-soitin iPhone", "IP-kamerakatseluohjelma", "DLNA-videosoitin",
  "Plex-asiakas iPhone", "Jellyfin-asiakas iOS", "Emby-asiakas iPad",
  "tekstityssoitin iOS", "SRT VTT ASS tekstitykset", "toissijaiset tekstitykset iPhone",
  "videotaajuuskorjain iOS", "äänentaajuuskorjain videosoitin", "ulkoinen DAC video",
  "suoratoista video Google Drivesta", "suoratoista video Dropboxista",
  "suoratoista video OneDrivesta", "suoratoista video iCloud Drivesta",
  "suoratoista video MEGAsta", "suoratoista video NASilta",
  "Chromecast video iPhone", "AirPlay 2 video", "iCloud-videosoitin",
  "Kuvat-kirjaston videosoitin", "Apple Music -videosoitin",
  "Wi-Fi Drive -videosirto", "M3U-videosoittolista",
  "Evervideo Premium", "Family Sharing -videosovellus"
]
tags: ["evervideo", "opas", "videosoitin", "PiP", "tekstitykset", "RTSP", "pilvi", "FFmpeg"]
---


### Tervetuloa Evervideo-oppaaseen

Evervideo on täysiverinen pilvi-mediasoitin iPhonelle, iPadille ja Macille, joka muuttaa minkä tahansa pilvipalvelun, NASin tai mediapalvelimen henkilökohtaiseksi mediakirjastoksesi ilman tarvetta ladata tiedostoja uudelleen ja pitäen täyden hallinnan tiedostoistasi.

Rakennettu mukautettuun FFmpeg-pohjaiseen soitinmoottoriin laitteistokiihdytetyllä H.264- ja HEVC-dekoodauksella, Evervideo toistaa käytännössä mitä tahansa nykyaikaista konttia ja codeciä — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS ja pitkän listan FFmpeg-formaatteja — täydessä laadussa, älykkäällä puskuroinnilla sujuvaan suoratoistoon Wi-Fin tai mobiiliverkon kautta. Picture-in-Picture pitää videosi kaikkien muiden sovellusten päällä, kompakti aina näytöllä oleva soitin antaa sinun katsella videoita samalla kun selaat kirjastoa, ja Chromecast sekä AirPlay 2 lähettävät toiston televisiollesi, HomePodille tai kaiutinjärjestelmääsi yhdellä napautuksella.

Evervideo yhdistää poikkeuksellisen laajaan listaan lähteitä, kaikki yhdestä sovelluksesta:

- **Henkilökohtainen pilvipalvelu:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Itse isännöidyt mediapalvelimet:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (ja ownCloud jaetun API:n kautta) · Synology Drive · QNAP.
- **NAS- ja tiedostonjakoprotokolaat:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (salasana tai julkisen avaimen todennus) · NFS · DLNA · UPnP.
- **Live- ja IP-kameravirrat:** RTSP — osoita Evervideo mihin tahansa RTSP-osoitteeseen (`rtsp://camera-ip/stream`) ja se toistaa heti.
- **S3-yhteensopiva objektitallennus:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces ja mikä tahansa muu S3-API-päätepiste.
- **Laitteen sisäiset lähteet:** Kuvat-kirjasto (Kaikki videot, Lyhyet / Keskipitkät / Pitkät, Näytön tallenteet sekä Kuva-albumisi), Musiikki-sovelluksen kirjasto (Albumit, Lajit, Soittolistat), USB / SD-korttiasemat ja Paikalliset tiedostot.

### Yksi soitin jokaiselle formaatille ja codecille

Kun useimmat iOS-sovellukset pysähtyvät H.264 / H.265:een MP4:ssä / MOVissa, Evervideo sisällyttää FFmpegin Applen järjestelmäcodecien rinnalle, jotta voit toistaa formaatteja, joita järjestelmä ei tunnista — MKV-kontit, VP9, AV1, MPEG-2, OGG, Vorbis ja paljon muuta — ja vaihtaa automaattisesti laitteisto-H.264/HEVC-dekoodauksen ja ohjelmistodekoodauksen välillä tiedoston ja laitteen perusteella.

Voit valita videoraitatun (monivirtaiset Blu-ray-ripit), ääniraitatun (kommentaariraidat, vaihtoehtoiset dubbaukset) ja tekstitysraitatun. Ulkoiset SRT-, VTT- ja ASS/SSA-tekstitystiedostot ladataan yhdellä napautuksella; edistynyt ASS/SSA-tyyli renderöidään oikein sisällytetyn libass-kirjaston ansiosta.

### Älykkäät tekstitykset

- **Tekstitysraidan valinta** täydellinen kielten opiskeluun.
- **Ulkoiset tekstitystiedostot** (`.srt`, `.vtt`, `.ass`, `.ssa`) ladattu mistä tahansa laitteeltasi tai pilvestä.
- **libass** täysin tyyliteltyyn ASS/SSA-renderöintiin.
- **Raita- ja globaali fonttivalinta** tekstityksille.
- **Ääniraitatun valinta** — valitse dubbaus, kommentaari tai ohjaajan raita.
- **Videoraitatun valinta** monikulmaisille tai moniversioisille tiedostoille.

### Kuvan ja äänen säätäminen

Kaksi taajuuskorjainta rinnakkain: äänitaajuuskorjain bassojen ja diskanttien säätämiseen (mukautettujen esiasetusten tuonti / vienti) ja videotaajuuskorjain kirkkauden, kontrastin, kylläisyyden ja värisävyn säätämiseen (myös tuonti / vienti). Molemmat moottorit tarjoavat myös audiofiilikontrollit: äänilähdön näytteenottotaajuus, kanavamäärä, IO-puskurin kesto ja sekamoodi — käyttäjille, joilla on ulkoisia DAC-laitteita ja kotiteatterivastaanottimet.

### Cast, AirPlay ja Picture-in-Picture

- **Picture-in-Picture (PiP):** jatka katselua muiden sovellusten käytön aikana.
- **AirPlay 2:** lähetä video Apple TV:lle, HomePodille tai mille tahansa AirPlay 2 -kaiuttimelle / -televisiolle.
- **Google Chromecast:** heitä suoraan Chromecastiin tai Cast-yhteensopivaan televisioon.
- **Kompakti soitin:** pysyvä mini-soitin jokaisen näytön päällä, jotta voit selata kirjastoa menettämättä videota.

### Yksityisyys ja turvallisuus

Evervideo käyttää virallisia SDK-paketteja ja OAuth-pohjaisia kirjautumisia jokaiselta pilvipalveluntarjoajalta, joten salasanasi ei koskaan pääse sovellukseen. Käyttötunnukset säilytetään salattuna iOS/MacOS-avaimenperässä, jokainen siirto on TLS-suojattu, ja pilvitilin käyttöoikeuden peruuttaminen (tai Evervideo-sovelluksen poistaminen laitteelta) poistaa kaiken välittömästi. Suojaa kirjastosi valinnaisella 4-numeroisella pääsykoodilla lisäyksitikyisyyden takaamiseksi.

### Evervideo-käytön aloittaminen

Tämä opas opastaa sinut jokaisen Evervideo-osan läpi iPhonella, iPadilla ja Macilla — pilvipalveluiden yhdistämisestä, kirjaston selaamisesta, tiedostojen lataamisesta ja siirtämisestä, soittolistojen hallinnasta aina mediasoittimen, taajuuskorjainten, tekstitysten ja Picture-in-Picture-toiminnon hienosäätöön. Käytä alla olevia kortteja hypätäksesi suoraan tarvitsemaasi osioon.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigointi" subtitle="Välilehtipalkit iPhonella, vasen valikko iPadilla ja Macilla, kompakti aina näytöllä oleva mediasoitin." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Tiedostot" subtitle="Yksi yhtenäinen välilehti pilvelle, NASille, RTSP-virroille, paikallisille tiedostoille, USB-asemille ja siirtojonoon." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Mediakirjasto" subtitle="Selaa albumeita, lajeja, äskettäin katsottuja, suosikkeja — sekä iOS:n Kuvat-kirjastoa ja Apple Music -kirjastoa." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Soittolistat" subtitle="Luo soittolistoja pilvestä, paikallisista tiedostoista, Kuvista tai Musiikki-kirjastosta, tuo M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Mediasoitin" subtitle="Picture-in-Picture, ääni- ja videoraidat, tekstitykset, ääni- + videotaajuuskorjaimet, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Asetukset" subtitle="Äänimoottori, videodekooderi, tekstitykset, kirjasto, tiedostohallinta, widgetit, personointi, kieli, varmuuskopiointi." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Löydä vastauksia yleisimpiin Evervideoita koskeviin kysymyksiin." >}}

{{< /cards >}}
