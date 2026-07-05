---
title: "Evertag 4.2: uudet pilviyhteydet, tunnistemerkintäeditorin asetukset selitettyinä"
date: 2026-05-09
description: "Evertag 4.2 lisää yhteydet Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP ja NFS, päivittää Wi-Fi Driven ja kohdistaa käyttöliittymän Liquid Glassiin. Tämä julkaisu selittää myös jokaisen tunnistemerkintäeditorin asetuksen — ID3v2.4 vs ID3v2.3, albumin kannen skaalauksen, tunnisteiden kahdennuksen, pilvilatausmuodot ja oikeat valinnat Spotifyn ja muiden suoratoistopalveluiden suhteen."
keywords: ["Evertag 4.2", "Evertag-päivitys", "ID3-tunnistemerkintäeditori iPhone", "ID3v2.4 vs ID3v2.3", "FLAC-tunnisteiden muokkaus iOS", "MP3-tunnisteiden muokkaus iPhone", "albumin kannen muokkaus iOS", "tunnistemerkintäeditori Spotifylle", "tunnistemerkintäeditori Plex", "tunnistemerkintäeditori Apple Music", "Evertag pilvitunnistemerkintäeditori", "Internxt-tunnistemerkintäeditori", "Proton Drive -tunnistemerkintäeditori", "QNAP-tunnistemerkintäeditori", "Nextcloud-tunnistemerkintäeditori", "Amazon S3 -tunnistemerkintäeditori", "SFTP-tunnistemerkintäeditori iPhone", "FTP-äänitunnistemerkintäeditori", "NFS-tunnistemerkintäeditori iPhone", "Wi-Fi Drive -tunnistemerkintäeditori", "ID3-tunnisteiden kahdennus", "albumin kannen skaalaus", "Liquid Glass -suunnittelu", "äänen metatietojen editori iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Tunnistemerkintäeditori", "ID3", "ID3v2.4", "ID3v2.3", "FLAC-tunnisteet", "MP3-tunnisteet", "Albumin kansi", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Mitä uutta"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**Tiivistelmä:** [Evertag 4.2](/products/evertag) on iso päivitys äänen tunnistemerkintäeditoriin iPhonelle, iPadille ja Macille. Korjasimme keskeiset tunnisteenmuokkausvirheet ja lisäsimme yli 6 uutta pilvi- ja palvelinyhteyttä — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** ja protokollat **FTP**, **SFTP** ja **NFS**. Wi-Fi Drive sai päivitetyn käyttöliittymän, monivalintatilan, fiksumman lähetysjonon ja nopeammat siirrot. Koko sovellus on viritetty **Liquid Glass** -suunnittelua varten. Tämä julkaisu pureutuu syvällisesti myös Evertagin tunnistemerkintäeditorin asetuksiin — selittäen **ID3v2.4 vs ID3v2.3**, **albumin kannen skaalauksen**, **tunnisteiden kahdennuksen**, **pilvilatausmuodot**, **ladatun tiedoston poiston** ja tarkalleen mitkä asetukset valita, jos valmistelet ääntä **Spotifyyn**, **Apple Musiciin**, **Plexiin**, **Jellyfiniin** tai johonkin muuhun suoratoistopalveluun.

---

## Hei kaikki!

Iso Evertag-päivitys on täällä. Korjasimme keskeiset tunnisteenmuokkausvirheet ja lisäsimme **yli 6 uutta pilvi- ja palvelinyhteyttä**, jotta äänen metatietojen hallinta on helpompaa kuin koskaan — riippumatta siitä, asuuko kirjastosi yksityisyyttä korostavassa pilvessä, itseisännöitävällä NAS:lla vai yleisellä FTP/SFTP/NFS-palvelimella.

[Lataa Evertag 4.2 App Storesta](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) tai päivitä nykyisestä versiostasi.

## Laajennettu pilvi- ja palvelintuki

Evertag liittyy nyt natiivisti laajempaan joukkoon pilvi- ja itse-isännöityjä tallennusvaihtoehtoja. Voit muokata ID3-, MP4-, FLAC-, OGG- ja APE-tunnisteita tiedostoissa missä tahansa.

### Yksityisyyteen keskittyvät pilvet: Internxt ja Proton Drive

Jos välität end-to-end-salauksesta ja zero-knowledge-tallennuksesta, kaksi yksityisyysasia-edellä-pilven arvostetuinta nimeä on nyt natiivisti Evertagissa:

- **Internxt** — avoimen lähdekoodin espanjalainen pilvi, jossa on post-kvanttisalaus ja GDPR-yhteensopivuus. Ilmainen taso saatavilla.
- **Proton Drive** — end-to-end-salattu tallennus Proton Mailin ja Proton VPN:n tekijöiltä, päämaja Sveitsissä. Ilmainen taso ja maksullisia paketteja suuremmille kirjastoille.

Voit nyt muokata metatietoja suoraan kummassakin palvelussa olevissa äänitiedostoissa — tiedosto pysyy salattuna siirron aikana, ja vain uudet tunnisteet kirjoitetaan takaisin.

### Itse-isännöitävät ratkaisut: QNAP, Nextcloud, Amazon S3

Käyttäjille, jotka pyörittävät omaa infraa:

- **QNAP** — natiivi API-yhteys QNAP NAS -laitteisiin. Muokkaa tunnisteita QNAP-tiedostoissa paikallisen Wi-Fin tai etäkäytön kautta.
- **Nextcloud** — yhdistä mihin tahansa Nextcloud-instanssiin, joko itse-isännöityyn tai hallinnoituun.
- **Amazon S3** — osoita Evertag mihin tahansa S3-buckettiin (tai S3-yhteensopivaan tallennukseen kuten Backblaze B2, Wasabi, MinIO, Cloudflare R2) ja muokkaa metatietoja paikan päällä.

### Uudet verkkoprotokollat: FTP, SFTP, NFS

Evertag 4.2 lisää kolme klassista protokollaa käyttäjille, joilla on omia palvelimia, kotilaboratorioita tai geneerisiä NAS-laitteita:

- **SFTP (SSH File Transfer Protocol)** — oikea vastaus **turvalliseen etätunnistemerkintämuokkaukseen omalta palvelimelta**. SFTP toimii SSH:n päällä, joten koko siirto (todennus ja äänidata) on salattu. Jos sinulla on VPS, dedikoitu palvelin tai Linux-kone kotona SSH-yhteydellä, voit muokata tunnisteita etätiedostoissa paljastamatta mitään muuta. Tukee sekä salasana- että avainpohjaista todennusta.
- **FTP** — pitkäaikainen tiedostonsiirron standardi. Hyödyllinen vanhemmille kotinas-laitteille, jotka tarjoavat FTP:n mutta eivät natiivia API-integraatiota.
- **NFS (Network File System)** — Linuxin ja useimpien NAS-laitteiden tosiasiallinen jakoprotokolla. Pienempi yleiskustannus kuin SMB:llä samalla laitteistolla.

> **Vinkki:** SFTP on protokolla, jota haluat etämuokkaukseen avoimen internetin yli. FTP ja NFS toimivat parhaiten paikallisverkossa — älä julkaise niitä internettiin, ellet kääri niitä VPN:llä.

## Wi-Fi Driven päivitykset

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) on Evertagin sisäänrakennettu ominaisuus **äänitiedostojen langattomaan siirtämiseen tietokoneen ja iPhonen tai iPadin välillä — ilman iTunesia, ilman kaapeleita, ilman pilvitiliä**. Molempien laitteiden tulee olla samassa Wi-Fi-verkossa.

Evertag 4.2:ssa Wi-Fi Drive saa:

- **Päivitetyn, modernin käyttöliittymän** — siistimpi, nopeampi luettavuus ja päivitetty Liquid Glassiin.
- **Monivalintatilan** — valitse useita tiedostoja tai kansioita ja toimi niihin pakettina.
- **Fiksumman lähetysjonon** — parempi etenemispalaute ja kestävyys verkkohäiriöille.
- **Paremman nopeuden ja yleisen luotettavuuden** — nopeammat siirrot suurille kirjastoille.

Tämä on nopein tapa siirtää erä äänitiedostoja tietokoneelta puhelimeen, muokata niiden tunnisteita ja lähettää ne takaisin — ilman kolmannen osapuolen palveluja.

## Tunnistemerkintäeditorin asetukset: syväluotaus

Tämä on osa, jota useimmat käyttäjät eivät koskaan lue — ja se osa, joka ratkaisee, toimivatko tunnisteesi kaikkialla vai vain joissakin sovelluksissa. Avaa Evertag ja siirry **äänitunnistemerkintäeditorin asetukset** -osioon. Tässä mitä kukin vaihtoehto todella tekee ja mikä valita riippuen tavoitteestasi.

### Albumin kannen skaalaus

Kun tallennat albumin kannen äänitiedostoon, Evertag voi skaalata kuvan ennen upottamista. Käytettävissä olevat vaihtoehdot:

- **Pieni** — pienin vaikutus tiedoston kokoon, alhaisempi kuvan laatu.
- **Keskikokoinen** — tasapainoinen valinta useimmille käyttäjille.
- **Suuri** — korkea laatu, sopii suurinäyttöisille soittimille ja CarPlaylle.
- **Erittäin suuri** — erittäin korkea laatu, huomattava tiedostokoon kasvu.
- **Alkuperäinen (Pois käytöstä)** — upottaa kannen alkuperäisellä resoluutiolla. **Ei skaalausta lainkaan.**

**Miksi tämä on tärkeää:**

- **Korkeampi laatu = isompi tiedosto.** 3 000 × 3 000 pikselin kansi voi lisätä useita megatavuja jokaiseen kappaleeseen. Kerrottuna koko albumiin levytilan kuluma kasvaa nopeasti.
- **Jotkut soittimet eivät käsittele suuria upotettuja kuvia hyvin.** Vanhemmat laitteet, jotkin auton päälaitteet ja jotkut perinneversiot pöytäkoneen soittimista voivat juuttua yli ~1 500 px:n kansiin tai kieltäytyä näyttämästä niitä.
- **Useimpiin pilvi- ja suoratoistotyönkulkuihin** **Keskikokoinen** tai **Suuri** on optimaalinen valinta. Käytä **Alkuperäistä** vain kun tarvitset arkistolaatua tai valmistelet tiedostoja luotettavalle soittimelle.

> **Alkuperäinen**-kokovaihtoehto kuuluu Evertagin premium-personointipäivitykseen. Vakiokoot (Pieni/Keskikokoinen/Suuri/Erittäin suuri) ovat ilmaisia.

### Tunnisteiden tallennusvaihtoehdot: ID3v2.4 vs ID3v2.3

Tämä on yksittäinen tärkein asetus yhteensopivuudelle. ID3v2 on MP3-tiedostojen sisällä käytettävä metatietomuoto. Käytössä on kaksi laajalti käytettyä versiota, jotka eroavat toisistaan hienovaraisilla mutta tärkeillä tavoilla.

#### ID3v2.4

- Uudempi, tukee **UTF-8-tekstikoodausta** — käsittelee oikein ei-latinalaisia kirjoituksia (kiinaa, venäjää, japania, arabiaa, hepreaa jne.).
- Enemmän kehystyyppejä (suhteellinen äänenvoimakkuus, taajuuskorjaimen esiasetukset jne.).
- **Suositellaan moderneille soittimille**, jotka tukevat sitä.

#### ID3v2.3

- Vanhempi mutta **yleisimmin tuettu** ID3-versio.
- Ei tue UTF-8:aa suoraan (käyttää UTF-16:ta Unicode-tekstille).
- **Suositellaan, kun tarvitset maksimiyhteensopivuuden** vanhempien soittimien, autoradioiden ja tiettyjen pöytäkoneen sovellusten kanssa.

#### Milloin ottaa ID3v2.4 käyttöön Evertagissa

- Käytät **moderneja äänisoittimia**, kuten Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (nykyiset versiot) tai modernit Android-soittimet. ✅ **Kytke ID3v2.4 päälle.**
- Kirjastosi sisältää **ei-latinalaisia merkkejä** (kiinaa, koreaa, japania, venäjää, arabiaa, kreikkaa, hepreaa). ✅ **Kytke ID3v2.4 päälle** — UTF-8 käsittelee niitä paljon puhtaammin.

#### Milloin poistaa ID3v2.4 käytöstä Evertagissa (käytä ID3v2.3 sen sijaan)

- Valmistelet tiedostoja **vanhemmalle autoradiolle tai kojelautayksikölle**, joka ei lue v2.4-tunnisteita.
- Näet **rikkoutunutta tekstiä tai puuttuvia tunnisteita** joissakin sovelluksissa muokkauksen jälkeen — se on vahva merkki siitä, että v2.4 ei ole tuettu siellä. Vaihda takaisin v2.3:een.
- Kohdistat **vanhempiin pöytäkoneen soittimiin** tai vanhempiin kannettaviin soittimiin (varhaiset iPodit, jotkut MP3-soittimet 2000–2010-luvuilta).

> **Nyrkkisääntö:** jos tunnisteesi näkyvät oikein kaikkialla v2.4:llä, jätä se päälle. Jos jopa yksi tärkeä soitin näyttää vääriä merkkejä, tyhjää tai ei lue tunnisteita, kytke v2.4 pois ja tallenna uudelleen.

#### Tunnisteiden kahdennus

Kun otat **Tunnisteiden kahdennuksen** käyttöön, Evertag kirjoittaa yhteiset metatietokentät (otsikko, esittäjä, albumi jne.) tiedoston **molempiin ID3v1- ja ID3v2-osioihin**. Tämä parantaa yhteensopivuutta hyvin vanhojen soittimien kanssa, jotka lukevat vain ID3v1:tä (alkuperäinen 128-tavun tunniste tiedoston lopussa).

- **Useimmat käyttäjät eivät tarvitse tätä.** Modernit soittimet lukevat ID3v2:n ensin.
- **Ota se käyttöön vain, jos** käytät vintage-laitteistoa tai tiettyä ohjelmistoa, joka jättää ID3v2:n huomiotta.

### Päivitä verkkotiedostoja: kuinka Evertag käsittelee pilvimuokkauksia

Kun muokkaat tunnisteita yhdistettyyn pilveen tallennetussa tiedostossa (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP jne.), Evertagin on lähetettävä muokattu tiedosto takaisin. Sinä päätät kuinka:

- **Näytä vahvistusviesti** *(oletus, suositeltu)* — Evertag kysyy ennen lähettämistä. Paras varovaisille käyttäjille ja jaetuille kirjastoille.
- **Päivitä tiedoston metatiedot automaattisesti** — lähettää hiljaa jokaisen muokkauksen jälkeen. Paras yksin käyttäville, joilla on nopea, luotettava yhteys ja jotka muokkaavat paljon.
- **Älä päivitä tiedoston metatietoja** — Evertag muokkaa vain paikallista kopiota. Hyödyllinen muutosten esikatseluun ennen niiden lähettämistä pilveen.

### Muokkaa verkkotiedostoja: paikallisen tiedoston siivous

Etätiedoston muokkaamiseksi Evertag lataa sen ensin laitteeseesi. Muokkauksen jälkeen valitset, mitä tuolle paikalliselle kopiolle tapahtuu:

- **Poista ladattu tiedosto aina** — Evertag poistaa väliaikaisen tiedoston muokkauksen jälkeen. **Suositellaan**, jos tilaa on vähän tai työskentelet jonkun muun tiedostoissa.
- **Älä poista ladattua tiedostoa** — säilyttää muokatun tiedoston laitteessasi. Hyödyllinen, kun haluat sekä offline-kopion että päivitetyn pilvikopion.

### Päänäytön painikkeet

Evertagin tunnistemerkintäeditorin etusivu voi näyttää tai piilottaa painikkeita yksittäisille toiminnoille. Aktivoi vain ne, joita todella käytät, jotta käyttöliittymä pysyy keskittyneenä:

- **Etsi äänitunnisteet automaattisesti** — etsii puuttuvat metatiedot verkosta tiedoston äänisormenjäljen perusteella.
- **Etsi äänitunnisteet manuaalisesti** — etsi otsikon/esittäjän mukaan, kun automaattinen haku epäonnistuu.
- **Etsi albumin kansi** — etsii ja upottaa korkealaatuisia kansia.
- **Tallenna albumin kansi** — vie upotetun kannen valokuvakirjastoosi tai tiedostoihisi.
- **Normalisoi koodaus** — korjaa rikkoutuneet ei-latinalaiset tekstit, jotka johtuvat vanhoista koodauksista (erittäin hyödyllinen kyrillisille, kiinalaisille ja japanilaisille kappaleille, jotka on rippattu vanhalla ohjelmistolla).
- **Poista äänitunnisteet** — poistaa kaikki tunnisteet tiedostosta. Hyödyllinen ennen puhdasta uudelleentaggausta.

### Näytä laajennetut tunnisteet

Vaihda tämä päälle näyttääksesi koko metatietokenttäjoukon perusotsikon/esittäjän/albumin/vuoden lisäksi — mukaan lukien BPM, kapellimestari, alkuperäinen esittäjä, tunnelma, tekijänoikeus, koodain, kommentit, sanoitukset ja muut. Tehokäyttäjien ominaisuus; useimmat satunnaiskäyttäjät eivät tarvitse sitä.

### Muokkaa tiedostoja samanaikaisesti

Kun käytössä, Evertag antaa sinun muokata metatietoja **useissa valituissa tiedostoissa kerralla** — aseta sama album artist, vuosi tai genre koko albumille yhdellä toiminnolla. Tämä on nopein tapa siivota suuri sekainen kirjasto.

## Tunnisteiden muokkaus Spotifylle, Apple Musicille ja suoratoistoalustoille

Yleinen kysymys: «muokkasin tunnisteet Evertagissa, latasin tiedostot ja suoratoistopalvelu näyttää väärät metatiedot. Mitä on tekeillä?»

Lyhyt vastaus: **suoratoistopalvelut eivät aina kunnioita paikallisia tunnisteitasi.** Apple Musicilla ja Spotifyllä on omat sisäiset tietokantansa — kun ne tunnistavat kappaleen, ne korvaavat näkyvät metatiedot omillaan. Mutta **ladattujen tiedostojen**, paikallisten tiedostojesi (Apple Musicin «Kirjasto»-ominaisuus, Spotify Local Files) ja **jakelijoiden lähetysten suoratoistoalustoille** osalta tunnisteilläsi on aivan ehdottomasti merkitystä. Näin asetat Evertagin kuhunkin skenaarioon:

### Tiedostojen valmistelu Apple Musicille (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music käsittelee UTF-8:aa oikein.
- **Albumin kansi: Suuri** — Applen sovellukset esittävät isoja kansia hyvin; Alkuperäinen on liikaa.
- **Tunnisteiden kahdennus: OFF** — ei tarvita.
- Varmista, että **Album Artist** on täytetty oikein — Apple Music käyttää sitä ryhmittelyyn.

### Tiedostojen valmistelu Spotify Local Filesille

Spotify Local Files näyttää vain hyvin merkittyjä tiedostoja. Tunnisteet, joita Spotify lukee, ovat rajoitetut.

- **ID3v2.4: ON** useimmissa tapauksissa. Jos kappale ei ilmesty oikein Spotifyssä muokkauksen jälkeen, **kokeile tallentaa ID3v2.4: OFF -asetuksella** (eli ID3v2.3:na) — Spotifyn jäsentäjä on historiallisesti suhtautunut konservatiivisesti v2.4:ään.
- **Albumin kansi: Keskikokoinen tai Suuri** — Spotify pienentää sen joka tapauksessa.
- Täytä vähintään **Otsikko**, **Esittäjä**, **Albumi** ja **Kappaleen numero**.

### Tiedostojen valmistelu jakelijan lähetykseen (DistroKid, TuneCore, CD Baby jne.)

Jos olet artisti, joka lataa omaa työtään suoratoistoalustoille, jakelijasi yleensä lukee tunnisteet mutta pyytää myös metatietoja käyttöliittymässään. Joka tapauksessa:

- **ID3v2.3** on usein turvallisempi oletus — monet jakelijoiden putkistot rakennettiin vuosia sitten ja suosivat vanhempaa muotoa.
- Upota **Suuri** kansi (useimmat jakelijat vaativat ≥ 1 400 × 1 400 px:n kannen — tarkista heidän ohjeensa).
- Älä luota laajennettuihin tunnisteisiin — jakelijat lukevat vain ydinkenttiä.

### Tiedostojen valmistelu Plexille, Jellyfinille, Navidromelle, Subsonicille, Embylle

Nämä itse-isännöidyt mediapalvelimet ovat erittäin sietokykyisiä. Ne lukevat sekä v2.3:n että v2.4:n puhtaasti ja käsittelevät UTF-8:aa hyvin.

- **ID3v2.4: ON** on hyvä.
- **Albumin kansi: Suuri** tai **Erittäin suuri** — nämä palvelimet syöttävät kannet mobiiliasiakkaille ja CarPlay-näytöille, joten laatu on tärkeää.
- **Album Artist** suositellaan vahvasti — sitä Plex/Jellyfin käyttävät albumien ryhmittelyyn esittäjittäin oikein.

### Tiedostojen valmistelu autoradioille ja vanhemmalle laitteistolle

- **ID3v2.4: OFF** (käytä ID3v2.3:a) — vanhemmat päälaitteet eivät usein tue v2.4:ää.
- **Albumin kansi: Keskikokoinen** — monet autonäytöt jumiutuvat suuriin upotettuihin kansiin.
- **Tunnisteiden kahdennus: ON** — vanhemmat autoradiot lukevat joskus vain ID3v1-varajärjestelmää.

## Muut parannukset

### Liquid Glass -suunnittelu

Evertag 4.2:n käyttöliittymä on viritetty Applen uudelle **Liquid Glass** -materiaalille koko sovelluksen ajan — läpikuultavat pinnat, sulavammat animaatiot ja viimeistellyt säätimet, jotka istuvat luonnollisesti iOS:iin, iPadOS:iin ja macOS:iin.

### Päivitetyt yhteyskirjastot

Päivitimme sisäiset kirjastot, joita Evertag käyttää keskusteluun **WebDAV**:n, **SMB**:n, **DLNA**:n, **Dropboxin**, **Google Driven**, **OneDriven** ja muiden palveluiden kanssa. Tulos: vähemmän yhteyden epäonnistumisia reunatapauksissa, parempi tuki uudemmille palvelinversioille ja parantunut luotettavuus etätiedostojen tunnisteiden muokkaamisessa.

### Käännös- ja lokalisointikorjaukset

Useita kielikorjauksia käyttöliittymässä käyttäjien suoran palautteen perusteella. Parempi tekstin sopivuus pieniin painikkeisiin useissa kielissä.

### Pienempiä parannuksia palautteenne innoittamana

Monet pienet parannukset perustuvat App Storen arvosteluihin ja sähköposteihin osoitteeseen support@everappz.com. Luemme jokaisen viestin.

## Hanki Evertag 4.2

[**Lataa Evertag App Storesta**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) tai päivitä App Storen kautta. Evertag on ilmainen lataus valinnaisilla sovelluksen sisäisillä päivityksillä edistyneitä ominaisuuksia varten. Uudet pilviyhteydet, verkkoprotokollat, Wi-Fi Driven parannukset ja Liquid Glass -käyttöliittymä kuuluvat perustepäivitykseen.

Jos pidät sovelluksesta, jätä arvio App Storeen — se auttaa todella. Onko palautetta tai kohtasitko ongelman? Lähetä sähköpostia osoitteeseen **support@everappz.com**. Luemme jokaisen viestin.

## Usein kysytyt kysymykset

{{% details title="Mitä uutta Evertag 4.2:ssa on?" closed="true" %}}
Evertag 4.2 lisää yli 6 uutta pilvi- ja palvelinyhteyttä (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), päivitetyn Wi-Fi Driven monivalinnalla ja fiksummalla lähetysjonolla, Liquid Glass UI -päivityksiä, päivitetyt yhteyskirjastot, keskeiset tunnisteenmuokkausvirheiden korjaukset ja käännösparannuksia.
{{% /details %}}

{{% details title="Pitäisikö minun käyttää ID3v2.4:ää vai ID3v2.3:ää Evertagissa?" closed="true" %}}
Käytä **ID3v2.4:ää** moderneille soittimille (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, modernit Android-sovellukset) ja kirjastoille, joissa on ei-latinalaisia merkkejä — UTF-8-tuki tarkoittaa puhtaampia tunnisteita kiinaksi, koreaksi, japaniksi, venäjäksi, arabiaksi ja hepreaksi. Käytä **ID3v2.3:ää**, jos tunnisteesi näkyvät väärin joissakin sovelluksissa, jos kohdistat vanhempiin autoradioihin tai jos suoratoistojakelijan putkisto hylkää v2.4:n. Voit aina vaihtaa ja tallentaa uudelleen.
{{% /details %}}

{{% details title="Miksi tunnisteeni ovat väärin Spotifyssä muokkauksen jälkeen?" closed="true" %}}
Spotify näyttää enimmäkseen metatietoja omasta luettelostaan — paikallisia tunnisteitasi käytetään vain «Local Filesissa» tai sisällössä, jonka olet ladannut artistina. Jos taggaat tiedostoja Spotify Local Filesia varten ja ne eivät näy oikein, kokeile poistaa ID3v2.4 käytöstä Evertagissa ja tallentaa ID3v2.3:na — Spotifyn jäsentäjä on historiallisesti suhtautunut konservatiivisesti v2.4:ään.
{{% /details %}}

{{% details title="Minkä kokoisen albumin kannen valitsen Evertagissa?" closed="true" %}}
Useimmille käyttäjille: **Suuri**. Näyttää hyvältä puhelimissa, iPadeissa, Maceissa ja moderneissa autonäytöissä paisuttamatta tiedostoja liikaa. Käytä **Keskikokoista**, jos kirjastosi on valtava ja haluat säästää levyä. Käytä **Alkuperäistä** (ei skaalausta) vain arkistomastereille tai kun todella tarvitset maksimilaadun — mutta huomaa, että jotkut vanhemmat soittimet kamppailevat erittäin suurten upotettujen kansien kanssa. **Alkuperäinen** kuuluu Evertagin premium-personointipäivitykseen.
{{% /details %}}

{{% details title="Tekevätkö suuremmat albumin kannet tiedostoistani isompia?" closed="true" %}}
Kyllä. 3 000 × 3 000 px:n kannen upottaminen voi lisätä useita megatavuja yhteen äänitiedostoon. 1 000 kappaleen kirjastossa se kasvaa gigatavuiksi. Jos tila on tiukalla, käytä Keskikokoista tai Suurta; jos suoratoistat NAS:lta, jossa koolla ei ole väliä, Erittäin suuri tai Alkuperäinen ovat hyviä.
{{% /details %}}

{{% details title="Mikä on Tunnisteiden kahdennus ja pitäisikö se ottaa käyttöön?" closed="true" %}}
Tunnisteiden kahdennus kirjoittaa ydinmetadatan sekä ID3v1- (legacy 128-tavun) että ID3v2- (moderniin) osioon tiedostossa. Ota se käyttöön vain, jos kohdistat erittäin vanhoihin soittimiin tai laitteistoihin, jotka lukevat ID3v1:tä. Kaikkeen moderniin (älypuhelimet, tietokoneet, uudemmat autoradiot) jätä se pois.
{{% /details %}}

{{% details title="Muokkaako Evertag tunnisteita suoraan pilvitiedostoissa?" closed="true" %}}
Kyllä. Yhdistä pilveesi (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3 jne.) tai FTP/SFTP/NFS:n kautta, avaa tiedosto ja muokkaa tunnisteita ikään kuin se olisi paikallinen. Evertag lataa tiedoston, soveltaa muokkauksesi ja lähettää päivitetyn version takaisin. Voit valita asetuksissa «Kysy aina», «Lähetä automaattisesti» tai «Älä lähetä» -tilojen välillä.
{{% /details %}}

{{% details title="Voinko muokata FLAC-tunnisteita iPhonella Evertagilla?" closed="true" %}}
Kyllä. Evertag tukee FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE ja muita tärkeitä formaatteja täydellä tunnisteiden luku-/kirjoitustuella, mukaan lukien upotettu kansi.
{{% /details %}}

{{% details title="Kuinka muokkaan tunnisteita turvallisesti kotipalvelimellani SFTP:llä?" closed="true" %}}
Avaa Evertag, mene Yhteydet-kohtaan, valitse SFTP ja syötä palvelimesi isäntänimi tai IP, portti (yleensä 22), käyttäjätunnus ja joko salasana tai SSH-yksityisavain. Evertag selaa etäkansiosi ja muokkaa tunnisteita suoraan SSH:n päälle päästä-päähän-salauksella.
{{% /details %}}

{{% details title="Voinko muokata tunnisteita useissa tiedostoissa kerralla?" closed="true" %}}
Kyllä. Ota **Muokkaa tiedostoja samanaikaisesti** käyttöön asetuksissa. Valitse useita tiedostoja, avaa tunnistemerkintäeditori, ja jokainen muuttamasi kenttä koskee kaikkia valittuja tiedostoja. Tämä on nopein tapa asettaa sama album artist, vuosi tai genre koko albumille.
{{% /details %}}

{{% details title="Onko päivitys Evertag 4.2:een ilmainen?" closed="true" %}}
Kyllä. Evertag on ilmainen lataus App Storesta, ja 4.2 on ilmainen päivitys kaikille olemassa oleville käyttäjille. Uudet pilvi-integraatiot, Wi-Fi Driven parannukset ja Liquid Glass -käyttöliittymä kuuluvat perustepäivitykseen.
{{% /details %}}

{{% details title="Millä laitteilla Evertag 4.2 on saatavilla?" closed="true" %}}
Evertag 4.2 toimii iPhonella, iPadilla ja Macilla. iCloud Drive -synkronointi pitää tunnistemerkintäeditorin asetuksesi yhdenmukaisina laitteiden välillä.
{{% /details %}}
