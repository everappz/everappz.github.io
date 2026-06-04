---
title: "Äänisoitin"
date: 2020-02-01
description: "Opi käyttämään Flacboxin äänisoitinta iPhonella, iPadilla ja Macilla. Hallitse toistoa, hallinnoi jonoja, konfiguroi FFmpeg / järjestelmän äänimoottori, muuta näytteenottotaajuutta, sävelkorkeuden korjausta, IO-puskurin kestoa, taajuuskorjainta, äänikirjanmerkkejä, AirPlay 2, Google Cast, CarPlay, widgettejä ja Macin pikanäppäimiä."
keywords: [
  "Flacbox soittimen opas", "äänisoittimen asetukset", "Flacbox taajuuskorjain",
  "AirPlay musiikin suoratoisto", "Google Cast musiikki", "äänikirjanmerkit",
  "Flacbox toistojono", "Flacbox toisto-satunnaisjärjestys", "Flacbox äänenvoimakkuuden säätö",
  "macOS mini-soitin", "musiikkisovellus voiceover",
  "Flacbox FFmpeg", "Flacbox sävelkorkeuden korjaus", "Flacbox näytteenottotaajuus",
  "Flacbox ulkoinen DAC", "Flacbox surround-ääni", "Flacbox IO-puskuri",
  "Flacbox toistonopeus", "Flacbox unitajastin"
]
tags: ["opas", "flacbox", "soitin"]
readingTime: 14
---


Äänisoitin on sovelluksen pääruutu, jossa hallitset musiikkia ja useimpia toisto-ominaisuuksia. Se on myös paikka, jossa Flacboxin korkearesoluutioinen äänimoottori — joka on rakennettu järjestelmäkoodekkien ja mukana toimitetun **FFmpeg**-kirjaston päälle — tekee raskaan työn. Tutustutaan sen käyttöön.

## Äänisoittimen Avaaminen

Pääset koko näytön soittimeen mini-soittimen palkista. iPhonessa mini-soitin on pääruudun alareunassa. iPadilla ja Macilla se on vasemmalla puolella. Piilottaaksesi mini-soittimen iPhonessa napauta sitä kerran ja pyyhkäise alas. Sulkeaksesi koko näytön soittimen kokonaan napauta sulkemispainiketta oikeassa alakulmassa.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Äänisoittimen Pääruutu" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Tuetut Äänimuodot

Flacbox toistaa suosituimmat äänimuodot — sekä Applen järjestelmäkoodekit että monet lisämuodot, joita mukana toimitettu FFmpeg-moottori käsittelee:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Tämä kattaa käytännössä kaikki modernit häviölliset ja häviöttömät muodot, joita sinulla saattaa olla henkilökohtaisessa musiikkikokoelmassasi.

## Toistosäätimet

Soittimen ruudun alareunassa näet painikkeet Toisto, Tauko, Seuraava kappale ja Edellinen kappale. On myös valinnaisia painikkeita kuten Seuraavat 30 sek ja Edelliset 30 sek, jotka voit ottaa käyttöön sovelluksen asetuksissa (kätevä äänikirjoille). Voit kelata eteenpäin tai taaksepäin pitämällä Seuraava / Edellinen -painikkeita painettuna. Hypätäksesi kappaleen tiettyyn kohtaan vedä toistoliukusäädintä.

## Toisto ja Satunnaisjärjestys

Napauta toistopainiketta kiertääksesi toistomuodot:

- **Toista Kaikki** — toistaa kaikki kappaleet jonossasi silmukassa.
- **Toista Yksi** — toistaa vain nykyisen kappaleen.
- **Toisto Stop** — pausauttaa, kun nykyinen kappale päättyy.
- **Ei Toistoa** — toistaa jonon kerran läpi toistamatta.

Käytä **Satunnaisjärjestys**-painiketta satunnaistamaan kappaleiden järjestyksen jonossa.

## Äänenvoimakkuuden Säätö

Avaa Ääniasetukset-ruutu napauttamalla äänikuvaketta toistopaikkien alla päästäksesi äänenvoimakkuuden liukusäätimeen. Löydät täältä myös painikkeet **Google Cast** ja **AirPlay**, jotta voit nopeasti vaihtaa toiston toiselle laitteelle.

## Google Cast (Chromecast)

Google Cast -käyttäjille **Cast**-kuvake näkyy soittimen alareunassa. Napauta sitä valitaksesi laitteen ja aloittaaksesi suoratoiston. Varmista, että laitteesi ja Google Cast -vastaanotin ovat samassa Wi-Fi-verkossa. Huomio: kaikki äänimuodot eivät ole yhteensopivia Google Castin kanssa — jotkut korkearesoluutioiset muodot saattavat vaatia transkoodauksen.

## AirPlay

AirPlaylle etsi **AirPlay**-painike soittimen alareunasta. Napauta sitä ja valitse laite suoratoistoa varten. Flacbox tukee **AirPlay 2:ta**, joten voit toistaa useille HomePodeille, Apple TV:ille tai AirPlay 2 -yhteensopiville kaiuttimille samanaikaisesti.

## Äänitaajuuskorjain

Flacbox sisältää **10-kanavaiseen taajuuskorjaimen** iPod-tyylisillä esiasetuksilla. Napauta Taajuuskorjain äänenvoimakkuusnäkymässä, sitten kytke se päälle oikeassa yläkulmassa. Voit käyttää esiasetuksia kuten Akustinen ja Basso-tehostin, tai säätää jokaista taajuuskaistaa liukusäätimillä. Tee omat esiasetukset, tallenna ne minkä nimisiksi tahansa ja lisää kokonaisäänenvoimakkuutta esivahvistimella. Meillä on yksityiskohtaisemmat ohjeet taajuuskorjaimen käyttöön [täällä](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Äänisoittimen Taajuuskorjain" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Soittimen Tilan Työkalupalkki

Joillekin soittimen tyyleille on koko näytön soittimen yläosassa omistettu työkalupalkki. Tässä työkalupalkissa on kolme hyödyllistä painiketta:

- **Hae** — paikanna nopeasti tietty kappale toistojononsa.
- **Toistonopeuden Säätö** — säädä toistonopeutta välillä 0,02× – 3,00×. Täydellinen äänikirjoille, podcasteille ja luennoille. Napauta Normaali palataksesi oletushopeuteen.
- **Äänikirjanmerkit** — luo useita kirjanmerkkejä kappaleelle. Meillä on täydelliset ohjeet kirjanmerkkien käyttöön [täällä](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Toistojono

Nähdäksesi toistojononsa napauta jonopainiketta nykyisen kappaleen oikealla puolella. Jokaisella jonon kappaleella on lisää toimintoja — napauta kolmea pistettä nähdäksesi ne. Järjestääksesi uudelleen kappaleen jonossa käytä uudelleenjärjestyssymbolia otsikon lähellä ja vedä se uuteen paikkaan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Toistojono" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Kommentit / Lyriikat

Nähdäksesi kappaleen kommentit ja upotetut lyriikat sekä LRC-tiedostot, seuraa näitä vaiheita:

1. Avaa **Asetukset**.
2. Siirry kohtaan **Äänisoitin**.
3. Valitse **Personointi**.
4. Napauta **Painikkeet pääruudulla**.
5. Ota käyttöön **Kommentit**.

Tämän jälkeen napauta toistojono-painiketta ruudun alareunassa useita kertoja vaihtaaksesi kansikuva / jono -näkymästä kommenttinäkymään. Kommentit-ruudulla, pyyhkäise oikealle vaihtaaksesi **Kommenttien**, **Upotettujen Lyriikoiden** ja **LRC-tiedoston** välillä. Täydelliset ohjeet ovat saatavilla [täällä](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Lyriikat ja Kommentit -ruutu" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Valintavalikko

Jokaisella äänisoittimen jonon kappaleella on valikko lisätoiminnoille, joihin pääsee napauttamalla kolmen pisteen painiketta kappaleen otsikon lähellä.

- **Toista Seuraavaksi** — lisää kappaleen toistojono-jonon alkuun.
- **Lisää Soittolistaan** — sisällyttää kappaleen soittolistaan, jossa on mahdollisuus luoda uusi.
- **Lisää Suosikkeihin** — merkitsee kappaleen suosikiksi nopeaa käyttöä varten.
- **Ladata** — tallentaa kappaleen paikallisiin tiedostoihin, jotka näkyvät **Paikalliset Tiedostot** -välilehdellä ja **Offline-musiikki**-osiossa.
- **Muokata Äänitunnisteita** — avaa sisäänrakennetun äänitunnisteiden muokkaustyökalun puuttuvien metatietojen korjaamiseksi, muokaten kappaletta tallennustilassasi.
- **Näytä Kansiossa** — paljastaa kansion, johon äänitiedosto on tallennettu.
- **Näytä Finderissa** — Macistasi tuoduille tiedostoille tämä paljastaa kansion, johon äänitiedosto sijaitsee Macillasi.
- **Avaa Sovelluksessa** — vie äänitiedoston toiseen sovellukseen.
- **Poista Jonosta** — poistaa valitun kappaleen äänisoittimen jonosta.
- **Poista Pilvipalvelusta** — poistaa kappaleen sekä musiikkikirjastosta että pilvivarastosta. **Tätä toimintoa ei voi kumota.**
- **Poista Paikallisista Tiedostoista** — poistaa kappaleen sekä musiikkikirjastosta että paikallisesta tallennustilasta. **Tätä toimintoa ei voi kumota.**
- **Poista Musiikkikirjastosta** — poistaa kappaleen musiikkikirjastosta, säilyttäen tiedoston tallennustilassa.

Samat vaihtoehdot ovat käytettävissä parhaillaan toistettavalle kohteelle äänisoittimen jonossa, johon pääset napauttamalla **Lisää toimintoja** -kuvaketta kappaleen otsikon lähellä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Vaihtoehdot Toistojono-kohteelle" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Soittimen Lisätoiminnot

Napauta **Lisää toimintoja** "..."-painiketta parhaillaan toistettavan kappaleen otsikon vasemmalla puolella nähdäksesi lisätoiminnot.

- **Jatka Toistoa** — jatka siitä, mihin jäit, mukaan lukien jono ja median asema. Erityisen hyödyllinen äänikirjoille. Aktivoidaan sovelluksen asetuksissa.
- **Hae** — löydä nopeasti tietty kappale äänisoittimen jonosta.
- **Kirjanmerkit** — näytä luotujen äänikirjanmerkkien lista.
- **Kommentit** — näytä kappaleen kommentit ja upotetut lyriikat sekä LRC-tiedostot. Täydelliset ohjeet [täällä](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Nopeus** — säädä toistonopeutta mieltymystesi mukaan.
- **Äskettäin** — pääse äskettäin toistettujen kappaleiden listaan.
- **Suosikit** — näytä suosikkikappaleidesi kokoelma.
- **Äänitaajuuskorjain** — aktivoi äänitaajuuskorjain.
- **Unitajastin** — aseta ajastin pysäyttämään toisto määritellyn ajan kuluttua. Loistava niille hetkille, kun haluat nukahtaa musiikkisi parissa.
- **Tallenna Jono Soittolistaksi** — tallenna nykyinen äänisoittimen jono uutena soittolistana.
- **Poista Jono** — tyhjennä soittimen jono ja pysäytä toisto.
- **Asetukset** — pääse äänisoittimen asetuksiin.
- **Ohje** — löydä apua ja ohjausta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Äänisoittimen Lisätoiminnot -ruutu" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Äänikirjanmerkit

Tämä ominaisuus antaa sinun luoda useita kirjanmerkkejä musiikkikirjastosi kappaleille — täydellinen äänikirjoille, luennoille, pitkille DJ-miksauksille tai suosikkikappaleen kertosäkeen merkitsemiseen.

Uuden kirjanmerkin luominen:

- Aloita haluamasi kappaleen toistaminen.
- Avaa soittimen ruutu.
- Napauta **Kirjanmerkit**-painiketta soittimen tilan työkalupalkissa.
- Valitse **Lisää Kirjanmerkki**.
- Valitse kirjanmerkin aika ja napauta **Valmis** oikeassa yläkulmassa.

Nykyisen kappaleen kirjanmerkkien muokkaaminen on helppoa: napauta Muokkaa oikeassa yläkulmassa siirtyäksesi muokkaustilaan. Tässä tilassa voit järjestää kirjanmerkkejä uudelleen, poistaa niitä, säätää kirjanmerkin aikaa ja muuttaa kirjanmerkin otsikkoja. Yksityiskohtaisemmat ohjeet äänikirjanmerkeistä ovat saatavilla [täällä](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Äänikirjanmerkit-ruutu" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Äskettäin ja Suosikit

Soittimen ruudulla napauta kolmea pistettä päästäksesi Äskettäin-osioon ja Suosikkeihin. Molemmissa osioissa voit hakea kappaleita, toistaa kaikki, sekoittaa kaikki, viedä listan ja tyhjentää listan. Meillä on yksityiskohtaiset ohjeet kappalelistan vientiin [täällä](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Yhdistä iPhonesi autoosi USB:n tai langattoman Apple CarPlayn kautta ja Flacbox ilmestyy CarPlay-aloitusnäyttöösi, valmiina toistamaan musiikkia turvallisesti ajaessasi. CarPlay-käyttöliittymä sisältää omistetut välilehdet Kirjastolle, Yhteyksille, Paikallisille Tiedostoille ja Asetuksille, toistohallinnoilla, satunnaisjärjestyksellä, toistolla, jonon hallinnalla ja äänitaajuuskorjaimella kaikki saatavilla ilman puhelimen ottamista käteen. Konfiguroi CarPlay-kokemus lisää kohdassa Asetukset → CarPlay — lajitteluvaihtoehdot, sivutus, valikon kuvakkeiden liukuvärin väri, ladataanko kuvia ja vaihtoehto keskeyttää toisto automaattisesti CarPlayyn yhdistettäessä.

[Lue täydellinen CarPlay-opas](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Apple CarPlayssa" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Aloitusnäytön Widgetit (iPhone ja iPad)

Flacbox tukee iOS-aloitusnäytön ja lukitusnäytön widgettejä, jotta voit nähdä ja hallita toistoa yhdellä silmäyksellä. Varmista, että Widgetit on otettu käyttöön kohdassa Asetukset → Widgetit → Ota Widgetit Käyttöön, sitten paina pitkään Aloitusnäyttöäsi tai Lukitusnäyttöäsi, napauta **+**, hae **Flacbox** ja lisää widget. Widget päivittyy toiston aikana näyttämään parhaillaan toistetun kappaleen kansikuvan, otsikon ja artistin.

## Mini-soittimen Ikkuna (Vain Mac)

Mac-käyttäjät voivat käyttää kompaktia, aina päällimmäistä mini-soitinta. Siirrä kursori Flacbox-ikkunan oikeaan alakulmaan, pienennä se pienimpään kokoonsa ja napauta tiivistämispainiketta. Pidä se jokaisen muun ikkunan päällä valitsemalla Ikkuna → Näytä Ikkuna Aina Päällimmäisenä valikkoriviltä — täydellinen pitämään musiikkisäätimet näkyvissä samalla kun työskentelet toisessa sovelluksessa.

## Pikanäppäimet (Vain Mac)

Mac-käyttäjille tilapalkissa on saatavilla järjestelmän toistovalikko pikanäppäimillä. Esimerkiksi paina välilyöntiä Toisto / Tauko. Pikanäppäimet Pysäytä, Seuraava Kappale, Edellinen Kappale, Hyppää, Toista, Satunnaisjärjestys ja Toistonopeus ovat myös saatavilla.

## Äänisoittimen Asetukset

Päästäksesi asetuksiin napauta Lisää-painiketta soittimen ruudulla ja valitse Asetukset. Täältä löydät useita osioita, jotka on lueteltu alla.

### Yleinen

Nämä asetukset kattavat äänisoittimen perusnäkökohdat, mukaan lukien toistojono, äänilähtö ja soittimen tilan tallentaminen.

- **Toistotila** — valitse, miten äänisoitin käyttäytyy kappaleen päättyessä:
  - **Toista Kaikki** — toistaa kaikki jonosi kappaleet uudelleen.
  - **Toista Yksi** — toistaa vain nykyisen kappaleen.
  - **Toisto Stop** — pausauttaa toiston, kun nykyinen kappale päättyy.
  - **Ei Toistoa** — antaa jonosi soida läpi toistamatta.
- **Satunnaistila** — satunnaistaa kappaleiden järjestyksen jonossasi. Voit kytkeä sen **Satunnaisjärjestys pois** tai **Satunnaisjärjestys päälle**.
- **Äänikoodekki** — valitse toistoon käytettävä äänimoottori:
  - **Järjestelmän Koodekki + FFmpeg** — priorisoi järjestelmän äänikoodekkin missä mahdollista, parantaen yhteensopivuutta ja vakautta. Sävelkorkeuden korjaus ja äänilähdön näytteenottotaajuuden säädöt voivat olla rajoitettuja tässä tilassa.
  - **FFmpeg** — pakottaa FFmpeg-koodekkin kaikille äänitiedostoille, antaen sinulle mahdollisuuden säätää sävelkorkeuden korjausta ja äänilähdön näytteenottotaajuutta.
- **Äänilähdön Näytteenottotaajuus** — säädä äänilähdön näytteenottotaajuutta äänenlaatuun optimoimiseksi, erityisen hyödyllinen ulkoisen DAC:n kanssa. Saatavilla olevat arvot: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** ja **96 kHz**.
- **Äänilähdön Kanavien Määrä** — monikanavaisille äänijärjestelmille ulkoisen DAC:n kanssa, määrittele kanavien määrä: **Mono, Stereo, Keski / Vasen / Oikea, Keski / Vasen / Oikea / Surround, ITU BS.775-1, 5.1 Surround** ja **SDDS**.
- **Äänilähdön Suositeltu IO-puskurin Kesto** — konfiguroi tulo / lähtö -puskurin kesto äänitoistoa varten. Tyypillinen arvo latenssin minimoimiseksi korkearesoluutioista ääntä toistettaessa on noin **5 millisekuntia (0,005 sekuntia)**. Hyväksyttävä puskurin koko riippuu laitteistostasi ja ohjelmistoympäristöstäsi, joten testaa eri kestoja kohdella ja valitse se, joka parhaiten tasapainottaa matalan latenssin ja häiriöttömän toiston.
- **Äänilähtötila (vain iOS)** — konfiguroi sekoitettu äänilähtötila, jotta ääni Flacboxista sekoittuu muiden sovellusten kanssa. Yksityiskohtaiset ohjeet ovat [täällä](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Tallenna Toistokohta** — varmistaa, että sovellus tallentaa ja palauttaa toistokohdan musiikkikirjastosi kappaleille.
- **Tallenna Äänisoittimen Tila** — säilyttää äänisoittimesi tilan ennen sovelluksen sulkemista. Jatkaaksesi toistoa napauta **Jatka Toistoa** minkä tahansa kansion, albumin, artistin tai genren yläosassa, kun avaat sovelluksen uudelleen. Voit myös palauttaa yksittäisten tiedostojen toiston napauttamalla kyseistä kappaletta.

Kun olet ottanut käyttöön sekä **Tallenna Toistokohta** että **Tallenna Äänisoittimen Tila**, avaa mikä tahansa kansio, albumi, artisti tai genre ja näet ruudun yläosassa **Jatka Toistoa** -painikkeen sekä viimeisimmän tallennetun kappaleen ja kohdan. Napauta sitä jatkaaksesi siitä, mihin jäit.

### Personointi

Personointi antaa sinulle mahdollisuuden mukauttaa äänisoittimen ruudun ulkoasua, muuttaa pääruudun, lukitusnäytön ja tilapalkin käytettävissä olevia säätimiä ja konfiguroida ohitusnäppäinsäätimet.

- **Äänisoittimen Ruututyyli** — konfiguroi elementtien sijoittelu äänisoittimen ruudulla.
- **Albumikuvien Vieritytyyli** — konfiguroi suositeltu albumikuvien vieritytyyli.
- **Lisäelementit** — ota käyttöön lisäelementtejä äänisoittimen ruudulla. **Äänimuodon Tiedot** näyttää parhaillaan toistettavan kappaleen äänitiedot kansikuvan yläpuolella; **Äänenvoimakkuuden Liukusäädin** näyttää äänilähdön liukusäätimen toistopaikkien alapuolella.
- **Pääruudun Toiminnot** — konfiguroi, mitkä painikkeet tulisi näkyä äänisoittimen pääruudulla oletuksena: **Toisto- ja Satunnaistila, Seuraava ja Edellinen Kappale, Ohitusaika, Unitajastin, Google Chromecast, AirPlay ja Bluetooth, Äänitaajuuskorjain, Hae, Kirjanmerkit, Nopeus, Lisää Kirjanmerkki, Lisää Suosikkeihin, Kommentit** ja lisää.
- **Toistopaikkien Lukitusnäytöllä** — valitse, mitkä säätimet näkyvät lukitusnäytöllä. Mahdolliset arvot: **Ohitusaika, Lisää Kirjanmerkki, Lisää Suosikkeihin**.
- **Ohitusaika-painikkeet** — valitse aikaväli **Ohitusaika**-painikkeille.

### Tiedostojen Lataaminen

Tiedostojen lataamisprosessin aikana voit muuttaa kappaleiden lataamiseen käytettävää verkkotyyppiä. Saatavilla olevat vaihtoehdot: **Wi-Fi**, **Wi-Fi ja Mobiilidatat**.

- **Esilatausaika** — aseta puskurointiaikaväli. Lisää tätä, jos sinulla on huono verkkoyhteys.
- **Käytä Suoraa URL:ää** — kun käytössä, suoraa URL:ää käytetään kappaleen lataamiseen, jos palvelin tukee sitä. Tämä voi nopeuttaa kappaleen lataamista, mutta saattaa vaikuttaa toiston vakauteen.

### Äänitaajuuskorjain

Mukauta äänitaajuuskorjaimen asetuksia. Voit lukea lisää äänitaajuuskorjaimen konfiguroinnista [täällä](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Toistonopeus

Säädä äänisoittimen toistonopeutta välillä **0,02× – 3,00×**. Napauta konfigurointikuvaketta oikeassa yläkulmassa vaihtaaksesi **tarkkaan tilaan** hienommille säädöille.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Toistonopeus-ruutu" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Sävelkorkeuden Korjaus

Muuta sävelkorkeuden korjauksen asetuksia käyttäen ennalta määritettyjä arvoja. Voit myös vaihtaa ennalta määritettyjen arvojen ja tarkan tilan välillä napauttamalla painiketta oikeassa yläkulmassa. Sävelkorkeuden korjaus on saatavilla FFmpeg-koodekkipolulla, vaihteluvälillä **-1000 – +1000**.

### Toistokätkö

Äänisoittimen jonon kappaleet ladataan automaattisesti sujuvan toiston varmistamiseksi. Jos lataat äänitiedostoja manuaalisesti, voit poistaa tämän vaihtoehdon käytöstä kaksoiskappaleiden välttämiseksi. Voit myös konfiguroida äänisoittimen kätkön koon täällä.

### Unitajastin

Aktivoi ajastin pysäyttämään toisto automaattisesti määritellyn ajan kuluttua — kätevä, kun haluat nukahtaa musiikin parissa. Napauta konfigurointikuvaketta oikeassa yläkulmassa **tarkan tilan** käyttämiseksi minuutti kerrallaan tarkkuudella.

## Saavutettavuus

Flacbox on täysin saavutettavissa **VoiceOver**-toiminnolla. Jokaisella komponentilla on hyvin suunniteltu tunniste ja kuvaus. Kun VoiceOver on aktiivinen, sovellus vaihtaa **Tekstimoodi**-tilaan, jotta vain merkitykselliset elementit näytetään — parantaen navigointinopeutta ja selkeyttä. Voit myös aktivoida Tekstimoodin kohdassa **Asetukset → Saavutettavuus → Tekstimoodi**.

### Liukusäätimien Säätäminen VoiceOver-toiminnolla

1. **Valitse liukusäädin** — pyyhkäise vasemmalle tai oikealle, kunnes VoiceOver ilmoittaa siitä.
2. **Säädä arvoa** — kaksoisnapauta ja pidä liukusäädintä, sitten vedä ylös tai alas muuttaaksesi arvoa nopeasti. VoiceOver ilmoittaa uuden arvon samalla.

### Kappaleen Sijainnin Säätäminen Listassa VoiceOver-toiminnolla

1. Napauta uudelleenjärjestyssymbolin kuvaketta kappaleen otsikon lähellä antaaksesi sille fokuksen.
2. Napauta nopeasti kahdesti uudelleenjärjestyssymbolia. Toisella napautuksella älä vapauta sormeasi — pidä, kunnes kuulet äänen, joka osoittaa, että solu on valmis siirrettäväksi.
3. Siirrä solu uuteen sijaintiinsa.

Muut komponentit toimivat odotetulla tavalla järjestelmän tarjoamia VoiceOver-malleja käyttäen.
