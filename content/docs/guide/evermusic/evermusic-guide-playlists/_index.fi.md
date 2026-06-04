---
title: "Soittolistat"
date: 2020-01-01
description: "Opi luomaan, tuomaan, mukauttamaan ja hallinnoimaan soittolistoja Evermusic-sovelluksessa. Sisältää yksityiskohtaiset vaiheet muokkaukseen, lajitteluun, offline-tilaan ja esteettömyyteen."
keywords: [
  "Evermusic", "soittolistat", "soittolistojen hallinta", "tuo M3U-soittolista",
  "muokkaa soittolistaa", "offline-soittolista", "muuta soittolistan järjestystä", "soittolistan kansi",
  "soittolistan esteettömyys", "äänisoitin"
]
tags: ["evermusic", "opas", "soittolistat"]
readingTime: 6
---


## Yleiskatsaus

Soittolistat-osio tarjoaa sinulle työkalut kappaleiden järjestämiseen listoihin. Se sisältää sisältönäkymän, jossa näkyvät kaikki luomasi soittolistat, "..."-painikkeen navigointipalkissa, joka tarjoaa erilaisia soittolistaan liittyviä toimintoja, sekä navigointityökalupalkin, jossa on "Haku", "Toista kaikki" ja "Sekoita kaikki" -painikkeet. Lisäksi jokaisella yksittäisellä soittolistalla on "..."-painike soittolistan otsikon lähellä, joka tarjoaa valikoiman kyseiselle soittolistalle erityisiä toimintoja.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evermusicin soittolistasnäyttö" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-main.webp" >}}
{{< /cards >}}

## Soittolistan luominen

Luodaksesi uuden soittolistan napauta joko "+"-painiketta tai "..."-painiketta navigointipalkin oikeassa yläkulmassa, valitse "Uusi soittolista" ja anna soittolistallesi nimi. Nimettyäsi sen napauta "Tallentaa".

{{< cards cols="1">}}
  {{< card title="" subtitle="Luo uusi soittolista" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-add-new.webp" >}}
{{< /cards >}}

Tämä avaa "Lisää kappaleita" -dialogin, jossa voit valita, mitkä kappaleet lisätään uuteen soittolistaan. Kappaleet luokitellaan lähdetyypin mukaan, ja sinulla on useita vaihtoehtoja:

- **Kirjasto**: Kappaleet musiikkikirjastostasi.
- **Tiedostot tässä sovelluksessa**: Äänitiedostot tallennettu sovelluksen Asiakirjat-hakemistoon.
- **Tiedostot tällä iPhone/iPad/Mac-laitteella**: Äänitiedostot, jotka sijaitsevat muissa kansioissa laitteessasi sovelluksen ulkopuolella.
- **Yhteydet**: Verkkotiedostot tallennettu yhdistetyissä pilvipalveluissa.

Oletuksena voit lisätä kappaleen soittolistaan vain kerran. Salliaksesi kaksoiskappaleet soittolistassa ota tämä ominaisuus käyttöön sovelluksen asetuksissa - Musiikkikirjasto - Soittolistat - Kaksoiskappaleet soittolistassa - Ota käyttöön.

## Soittolistan tuominen

Evermusic-sovelluksessa olemme lisänneet M3U-tiedostojen tuontitoiminnallisuuden, joten sinun ei tarvitse luoda soittolistoja manuaalisesti.

{{< cards cols="1">}}
  {{< card title="" subtitle="Tuo soittolista tiedostolähteestä" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-import-from-files.webp" >}}
{{< /cards >}}

Siirry ensin "Soittolistat"-osioon. Napauta sitten "Lisää"-painiketta oikeassa yläkulmassa. Valitse näkyviin tulevasta valikosta "Tuo soittolista" -vaihtoehto.

Valitse seuraavalta näytöltä tiedoston sijainti. Tuetut vaihtoehdot ovat:

- Yhdistetty pilvipalvelutallennustila
- Tiedostot sovelluksessa
- Tiedostot laitteessasi

Valitaan yhdistetty pilvipalvelutallennustila ja avataan soittolistatiedoston sisältävä kansio. Tuetut soittolistapäätteet ovat M3U, M3U8 ja CUE. Valitse soittolistatiedosto ja napauta "Valmis" vahvistaaksesi valintasi.

Sovellus jäsentää soittolistatiedoston, luo kappalelistan ja paikallistaa nämä tiedostot tallennustilasta kootakseen lopullisen soittolistan, joka tuodaan musiikkikirjastoon. On tärkeää, että M3U/CUE-tiedostosi sisältää oikeat polut mediatiedostoille, ja tiedostojen tulee sijaita kyseisillä poluilla tallennustilassasi. Voit lukea lisää soittolistojen tuomisesta [täällä](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox).

## Soittolistan yksityiskohtanäyttö

Kun avaat soittolistan, näkyviin tulee "Soittolistan yksityiskohtanäyttö". Tällä näytöllä löydät "..."-painikkeen oikeassa yläkulmassa soittolistan valinnoilla, ja kolme painiketta artwork-kuvan alla: "Haku", "Jatka toistoa", "Toista kaikki" ja "Sekoita kaikki". Lisäksi on "Offline-tila"-valintaruutu.

{{< cards cols="1">}}
  {{< card title="" subtitle="Soittolistan yksityiskohtanäyttö" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-detail-screen.webp" >}}
{{< /cards >}}

- **Jatka toistoa**: Palauta toistosijainti tälle soittolistalle.
- **Haku**: Suorita haku nykyisessä soittolistassa.
- **Toista kaikki**: Lisää kaikki kappaleet nykyisestä soittolistasta soittojonoon.
- **Sekoita kaikki**: Samankaltainen kuin "Toista kaikki", mutta sekoittaa kappaleet ennen lisäämistä äänisoittimen jonoon.
- **Offline-tila**: Lataa kaikki kappaleet tästä soittolistasta paikallisiin tiedostoihin. Kaikki uudet soittolistaan lisätyt kohteet ladataan automaattisesti.

## Lisää toimintoja soittolistalle soittolistanäytössä

Voit käyttää soittolistan toimintoja napauttamalla "..."-painiketta soittolistan otsikon lähellä. Käytettävissä olevat toiminnot ovat:

- **Toista kaikki:** Lisää soittolistan kappaleet uuteen soittojonoon.
- **Toista seuraavaksi:** Lisää soittolistan kappaleet olemassa olevan soittojonon alkuun.
- **Toista myöhemmin:** Lisää soittolistan kappaleet olemassa olevan soittojonon loppuun.
- **Muokkaa kuvaa:** Muokkaa soittolistan artwork-kuvaa.
- **Ota offline-tila käyttöön:** Ottaa offline-tilan käyttöön soittolistalle. Tässä skenaariossa sekä olemassa olevat että uudet kappaleet ladataan automaattisesti. Lue lisää offline-tilasta [täällä](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).
- **Vie kappalelista:** Voit viedä tämän soittolistan eri muodoissa kuten on kuvattu [täällä](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lisää arkistoon:** Voit arkistoida tämän soittolistan sisältäen m3u-tiedoston, albumikansikuvan ja kaikki kappaleet kuten on kuvattu [täällä](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Lisää kappaleita:** Lisää lisää kappaleita nykyiseen soittolistaan.
- **Nimeä uudelleen:** Nimeä soittolista uudelleen.
- **Poista soittolista:** Poista soittolista musiikkikirjastosta. Huomaa, että tätä toimintoa ei voi kumota.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lisää toimintoja -valikko soittolistalle" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-more-actions-for-separate-playlist.webp" >}}
{{< /cards >}}

## Lisää toimintoja soittolistalle yksityiskohtanäytössä

Voit käyttää soittolistan toimintoja napauttamalla "..."-painiketta oikeassa yläkulmassa. Käytettävissä olevat toiminnot ovat:

- **Valita:** Aktivoi kappaleiden valintatilanteen, hyödyllinen useamman kappaleen poistamiseen soittolistasta tai järjestyksen muuttamiseen.
- **Toista seuraavaksi:** Lisää soittolistan kappaleet olemassa olevan soittojonon alkuun.
- **Toista myöhemmin:** Lisää soittolistan kappaleet olemassa olevan soittojonon loppuun.
- **Lisää kappaleita:** Lisää uusia kappaleita soittolistaan.
- **Järjestä kappaleet uudelleen:** Muuta kappaleiden järjestystä soittolistassa manuaalisesti vetämällä ja pudottamalla.
- **Nimeä uudelleen:** Nimeä nykyinen soittolista uudelleen.
- **Muokkaa kuvaa:** Muokkaa albumin kansikuvaa nykyiselle soittolistalle.
- **Vie kappalelista:** Vie tämä soittolista eri muodoissa. Voit lukea lisää [täällä](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).
- **Lisää arkistoon:** Pakkaa nykyinen soittolista sisältäen kaikki kappaleet ja m3u-tiedoston. Voit lukea lisää [täällä](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to).
- **Lajittele:** Muuta kappaleiden järjestystä soittolistassa. Lajitteluvaihtoehdot sisältävät "Kappaleen nimi", "Kappaleen numero", "Albumi", "Artisti", "Albumiartisti", "Genre", "Säveltäjä", "Arviointi", "Vuosi", "Lyönnit minuutissa", "Kesto", "Tiedostonimi", "Tiedoston muokkauspäivämäärä", "Tiedoston luomispäivämäärä" ja "Manuaalinen". "Manuaalinen" lajitteluvaihtoehto mahdollistaa kappaleiden manuaalisen uudelleenjärjestämisen vetämällä ja pudottamalla.
- **Haku:** Hae tiettyä kappaletta nykyisessä soittolistassa.
- **Ruudukko/Lista:** Muuta näytön asettelun esitystä.
- **Poista soittolista:** Poista soittolista musiikkikirjastosta. Tärkeää: tämä toiminto ei poista kappaleita tallennustilastasi, eikä sitä voi kumota.

## Kappaleiden järjestyksen muuttaminen soittolistassa

Muuttaaksesi kappaleiden järjestystä soittolistassa napauta "..."-painiketta oikeassa yläkulmassa ja valitse "Valita" siirtyäksesi valintatilanteen. Käytä järjestyssäätöä ja vedä-ja-pudota-eleitä kunkin kappaleen lähellä siirtääksesi niitä ylös tai alas. Napauttamalla järjestyssäätöä kappale siirtyy listan ylhäälle. Poistuaksesi valintatilanteesta ja soveltaaksesi muutokset napauta "Valmis".

{{< cards cols="1">}}
  {{< card title="" subtitle="Kappaleiden järjestyksen muuttaminen soittolistassa" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-change-songs-order.webp" >}}
{{< /cards >}}

## Soittolistan kansikuvan muuttaminen

Muuttaaksesi soittolistan kansikuvaa napauta "..."-painiketta oikeassa yläkulmassa ja valitse "Muokkaa kuvaa". Valitse kuva käytettävissä olevista lähteistä ja vahvista muutokset napauttamalla "Valmis".

## Kappaleiden lisääminen soittolistaan

Avaa soittolista ja napauta "..."-painiketta oikeassa yläkulmassa, valitse sitten "Lisää kappaleita" avataksesi dialogin. Valitse haluamasi kappaleet ja vahvista muutokset napauttamalla "Valmis".

## Useiden kappaleiden poistaminen soittolistasta

Avaa soittolista, napauta "..."-painiketta oikeassa yläkulmassa ja valitse "Valita" siirtyäksesi valintatilanteen. Valitse poistettavat kappaleet ja napauta "Poista soittolistasta" -painiketta näytön alareunassa. Vahvista muutokset napauttamalla "Valmis".

{{< cards cols="1">}}
  {{< card title="" subtitle="Valittatilanne soittolistan sisällä" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-selection-mode-in-playlist-details-screen.webp" >}}
{{< /cards >}}

## Kappalevaihtoehdot

Jokaisella kappaleella soittolistassa on toimintolista, johon pääset napauttamalla "..."-painiketta. Jos et näe kaikkia toimintoja, vieritä alas nähdäksesi ne. Voit poistaa kappaleen soittolistasta, ladata sen, muokata äänitunnisteita ja paljon muuta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Kappalevaihtoehtovalikko soittolistassa" image="/docs/guide/evermusic/evermusic-guide-playlists/img/playlists-track-options.webp" >}}
{{< /cards >}}

- **Toista seuraavaksi:** Lisää kappaleen soittojonon alkuun.
- **Toista myöhemmin:** Lisää kappaleen soittojonon loppuun.
- **Lisää soittolistaan:** Lisää kappaleen soittolistaan.
- **Lisää suosikkeihin:** Merkitsee kappaleen suosikiksi nopeaa käyttöä varten.
- **Ladata:** Tekee kappaleesta saatavilla offline-tilassa. Se ilmestyy siirtojonoon ja "Paikalliset tiedostot" -välilehdelle musiikkikirjaston "Ladattu musiikki" -osiossa.
- **Muokata äänitunnisteita:** Avaa sisäänrakennetun tunnistemuokkaimen kappaleen metatietojen muuttamiseen.
- **Avaa sovelluksessa:** Vie kappaleen ja avaa sen toisessa sovelluksessa.
- **Näytä kansiossa:** Paljastaa kansion, johon äänitiedosto sijaitsee.
- **Näytä Finderissä:** Macilta tuoduille tiedostoille tämä toiminto paljastaa kansion, johon äänitiedosto sijaitsee Mac-tietokoneellasi.
- **Poista soittolistasta:** Poistaa kappaleen soittolistasta.
- **Poista pilvipalvelusta:** Poistaa kappaleen soittolistasta ja siihen liittyvästä pilvipalvelusta. Huomaa, että tätä toimintoa ei voi kumota.
- **Poista musiikkikirjastosta:** Poistaa kappaleen musiikkikirjastosta jättäen tiedoston tallennustilaan koskemattomana.

## Esteettömyys

Sovelluksemme on täysin saavutettavissa VoiceOver-teknologialla, mikä varmistaa, että jokaisella komponentilla on hyvin suunniteltu tunniste ja kuvaus. Kun VoiceOver on aktiivinen, sovellus kääntää käyttöliittymän tekstitilaan ja näyttää vain saavutettavissa olevat ja hyödylliset elementit navigointinopeuden ja mukavuuden parantamiseksi. Voit myös aktivoida tekstitilan kohdassa Asetukset > Esteettömyys > Tekstitila.

Kappaleen sijainnin säätäminen soittolistassa VoiceOverilla:

1. Avaa soittolista ja napauta "Lisää"-painiketta.
2. Valitse "Muuta kappaleiden järjestystä." Näkymä vaihtuu muokkaustilaan.
3. Napauta kappaleen otsikon lähellä olevaa järjestysilmaisimen kuvaketta antaaksesi sille kohdistuksen.
4. Kaksoisnapauta järjestysilmaisimen kuvaketta nopeasti. Toisella napautuksella älä nosta sormeasi — pidä sitä alhaalla, kunnes kuulet äänen, joka osoittaa solun olevan valmis siirrettäväksi.
5. Nyt voit siirtää solun uuteen sijaintiin.

Muut komponentit toimivat odotetulla tavalla käyttäen järjestelmän tarjoamia VoiceOver-malleja.
