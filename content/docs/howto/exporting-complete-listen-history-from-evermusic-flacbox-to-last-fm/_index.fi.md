---
title: "Vie koko kuunteluhistoriasi Evermusicista ja Flacboxista Last.fm:iin"
date: 2024-01-30
description: "Opi viemään musiikkihistoriasi Evermusicista ja Flacboxista ja lataamaan se Last.fm:iin CSV-tiedostojen ja Last.fm Scrubbler -työkalun avulla Windowsissa."
keywords: ["evermusic", "flacbox", "lastfm", "musiikkihistoria", "scrobbling", "vie kappaleet", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "äskettäin", "lastfm", "vienti", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Yhteenveto:** Vie kuunteluhistoriasi Evermusicista tai Flacboxista CSV-tiedostona ja lataa se sitten Last.fm:iin käyttämällä ilmaista Last.fm-Scrubbler-WPF-työkalua Windowsissa. Automaattinen scrobbling on myös saatavilla natiivisti molemmissa sovelluksissa.

**Päivitys:** Automaattinen scrobbling on nyt saatavilla! Lue lisää täältä: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Scrobbling on yksinkertainen tapa tallentaa automaattisesti perustiedot, kuten kuuntelemasi kappaleen nimi ja esittäjä, verkkopalveluun. Myöhemmin voit tarkastella kuunteluhistoriaasi.

[Last.fm](https://www.last.fm/home), jota tukee musiikkisuositusjärjestelmä nimeltä Audioscrobbler, tarjoaa tämän palvelun ilmaiseksi. Se luo yksityiskohtaisen profiilin musiikkimaustasi tallentamalla kuuntelemasi kappaleet, olivatpa ne internetradioasemilta, tietokoneeltasi tai erilaisista kannettavista musiikkilaitteista. Voit vierailla verkkosivustolla myöhemmin saadaksesi suosituksia uusista artisteista tai albumeista, jotka vastaavat musiikkimakuasi.

Voit ladata kuunteluhistoriasi [Last.fm](http://Last.fm):iin Evermusic- ja Flacbox-sovelluksista ilmaisella työkalulla, ja opastamme sinua prosessin läpi.

Avaa sovelluksen 'Musiikkikirjasto'-osio ja vieritä 'Pikakäyttö'-osioon. Napauta 'Äskettäin'-valikkovalintaa.

![musiikkikirjaston näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

'Äskettäin'-näytöllä napauta 'Lisää'-painiketta oikeassa yläkulmassa aktivoidaksesi 'Lisää toimintoja'-valikon. Napauta 'Vie kappaleluettelo'-valikkovalintaa.

![äskettäin-näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

'Valitse tiedostomuoto'-näytöllä voit valita kohdetiedoston muodon. Käytettävissä olevat vaihtoehdot - CSV, TXT, M3U.

![valitse tiedostomuoto -näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Tämä tarkoittaa pilkuilla erotettuja arvoja, täydellinen tietojesi järjestämiseen siistiin taulukkomuotoon. Kohdetiedostosta löydät parametrit kuten Artistin nimi, Albumin nimi, Kappaleen nimi, Aikaleima (aika jolloin kuuntelit kappaleita), Albumin artistin nimi ja Kappaleen kesto.

TXT: Tässä puhutaan pelkkää tekstitiedostoa. Se on yksinkertainen ja suoraviivainen, ja parametreihin kuuluvat Artistin nimi, Albumin nimi, Kappaleen nimi ja Kesto.

M3U: Tämä muoto on oleellisesti soittolistojen luomisen standardi. Se on loistava, koska voit viedä kappaleluettelosi ja nauttia kappaleistasi millä tahansa laitteella, vaikka sinulla ei olisi alkuperäisiä tiedostoja (edellyttäen, että valitset mediatiedostojen absoluuttisen URL-osoitteen vaihtoehdon). Tulostiedostosta löydät parametrit kuten Kesto, Artistin nimi, Kappaleen nimi ja Mediatiedoston sijainti.

Tehtäväämme varten CSV:n valitseminen on oikea tapa. Käytämme tätä tiedostoa ilmaisen Last.fm-Scrubbler-WPF-ohjelmiston kanssa kuunteluhistoriamme lataamiseen [Last.fm](http://Last.fm)-palveluun. Valitse yksinkertaisesti CSV ja paina 'Vie'-painiketta.

![vienti valmis -näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Viennin valmistuttua napauta yksinkertaisesti 'Näytä tiedosto'-painiketta, ja sovellus paljastaa luodun tiedoston asiakirjakansiossasi. Napauta sitten 'Lisää toimintoja'-painiketta tiedostonimen vieressä ja valitse valikosta 'Avaa kohteessa' -vaihtoehto. Seuraava askeleemme on kopioida viety tiedosto pöytätietokoneellesi. Voit tehdä tämän helposti valitsemalla AirDrop-vaihtoehdon 'Avaa kohteessa' -valikosta.

![lisää toimintoja viedylle tiedostolle](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Seuraavaksi käytämme ilmaista avoimen lähdekoodin [Last.FM](http://Last.FM)-asiakasohjelmaa, joka on saatavilla vain Windows-alustalla. Tämä asiakasohjelma mahdollistaa kuunteluhistoriasi tehokkaan päivittämisen [Last.FM](http://Last.FM):ssä käyttämällä juuri viemäämme CSV-tiedostoa.

Jos et tällä hetkellä käytä Windows-tietokonetta, älä huoli. Voit silti käyttää tätä asiakasohjelmaa asentamalla VirtualBoxin Mac-tietokoneellesi ja käyttämällä virallista Windows-kehitysympäristön levykuvatiedostoa.

Tässä on mitä sinun täytyy tehdä:

- Asenna VirtualBox seuraavasta linkistä: [Lataa VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Lataa ja asenna Windows-kehitysympäristö tästä linkistä: [Windows-kehitysympäristö](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Windows-tietokoneellasi (tai VirtualBox-sovelluksessa Windows Development -levykuvalla) lataa ja asenna [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - ilmainen avoimen lähdekoodin ohjelmisto saatavilla GitHubissa. Testasimme versiota 1.28, jonka voit ladata täältä: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![Last.fm-Scrubbler-WPF-lataussivu](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

'Assets'-osiossa napauta [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) ladataksesi asennusarkiston. Pura ladattu tiedosto ja avaa purettu kansio.

- TÄRKEÄÄ

Tämä sovellus on edelleen beta-vaiheessa. Sovelluksen tekijät eivät ole testanneet sitä paljon. He suosittelevat kokeilemaan scrobblausta testitilille ensin ja katsomaan, toimivatko scrobblattavat asiat oikein. Erityisesti jos scrobblaat paljon kappaleita kerralla. Ole varovainen tiliesi kanssa.

Suorita Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Sovelluksen päänäytöllä napauta yksinkertaisesti 'Ei kirjautuneena', joka sijaitsee vasemmassa alakulmassa, aktivoidaksesi 'Lisää tili' -näytön.

![lisää tili -näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Syötä kirjautumistietosi.

![kirjautumistietojen syöttö -näyttö](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Napauta 'Kirjaudu'-painiketta lisätäksesi tilisi.

![Napauta Kirjaudu-painiketta lisätäksesi tilisi.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Avaa 'File Parse Scrobbler' -välilehti aloittaaksesi CSV-tiedoston tuomisen Evermusic-sovelluksesta.

![Avaa File Parse Scrobbler -välilehti aloittaaksesi CSV-tiedoston tuomisen Evermusic-sovelluksesta.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Valitse 'Parser: CSV' ja napauta 'Asetukset'-painiketta.

Seuraavalla näytöllä voit valita CSV-tiedostosi parametrien järjestyksen.

Yksittäiset kentät voidaan sulkea lainausmerkkeihin ja NE TÄYTYY sulkea lainausmerkkeihin, jos kenttä sisältää jonkin asetetuista erottimista. Esimerkiksi:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Jätä siis kaikki asetukset oletusarvoihin, ainoa asia jonka sinun täytyy muuttaa on valintaruudun ottaminen käyttöön 'Has Fields Enclosed In Quotes' -kentässä.

Napauta 'Tallenna ja sulje' ottaaksesi muutokset käyttöön.

![valitse CSV-tiedostosi parametrien järjestys.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Tiedostojen jäsennys-scrobblauksella on kaksi tilaa. Ne voidaan vaihtaa 'Scrobbling Mode' -pudotusvalikosta.

Normaali tila: Tässä tilassa kappaleet scrobblataan jäsennetyn scrobblen aikaleimalla. Vain alle 14 päivää vanhat scrobblaukset voidaan scrobblata.

Tuontitila: Tässä tilassa kappaleet scrobblataan aikaleimalla, joka lasketaan 'Lopetusajasta' ja valitusta kestosta jokaisen kappaleen välillä. Tämä mahdollistaa kappaleiden scrobblauksen, vaikka jäsennetyn scrobblen aikaleima olisi vanhempi kuin 14 päivää. Siksi ensimmäinen (ylin) kappale CSV-tiedostossa scrobblataan 'Lopetusajalla'.

Valitse aiemmin luotu CSV-tiedosto Evermusic-sovelluksesta 'File:'-kentässä ja napauta 'Parse'. Joissakin tapauksissa saatat nähdä virheilmoituksen, joka kertoo, että joitakin scrobblauksia ei voitu jäsentää. Se on OK, jos sinulla on joitakin kappaleita ilman täydellisiä metatietoja kuten Artistin nimi.

![joitakin scrobblauksia ei voitu jäsentää](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Napauta 'Valitse kaikki' -painiketta valitaksesi kaikki jäsennetyt kappaleet.

![Napauta Valitse kaikki -painiketta valitaksesi kaikki jäsennetyt kappaleet.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Napauta 'Esikatselu'-painiketta tarkistaaksesi kaikki muutokset, jotka lähetetään palvelimelle.

![Napauta Esikatselu-painiketta tarkistaaksesi kaikki muutokset, jotka lähetetään palvelimelle.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Napauta 'Scrobble'-painiketta ladataksesi kaikki muutokset palvelimelle.

![Napauta Scrobble-painiketta ladataksesi kaikki muutokset palvelimelle.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Aiemmin Last.fm-Scrubbler-WPF:llä ei ollut päivittäistä scrobble-rajaa. Tämä on nyt muuttunut, koska jotkut ihmiset käyttivät Scrubbleria scrobblaamaan niin paljon kappaleita, että se aiheutti ongelmia Last.fm-sivulle. Scrobble-raja on tällä hetkellä 2800 scrobblausta päivässä. Kun yrität scrobblata enemmän, saat virheilmoituksen. Suunnitelmissa on lisätä 'scrobble-jono', joten jos sinun täytyy scrobblata yli 2800 kappaletta, ne lisätään jonoon ja scrobblataan automaattisesti jonkin ajan kuluttua. Voit tarkistaa käyttäjän valinnan näkymästä, kuinka monta scrobblausta sinulla on jäljellä.

Kun kaikki tietueet on ladattu onnistuneesti palvelimelle, näet sovelluksen ikkunan alareunassa viestin, joka vahvistaa: 'Valitut kappaleet scrobblattu onnistuneesti.'

![Valitut kappaleet scrobblattu onnistuneesti.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Nyt voit avata profiilisi [Last.fm](http://Last.fm)-sivulla ja tarkistaa kaikki muutokset.

![profiilisi Last.fm-sivulla](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Usein kysytyt kysymykset

{{% details title="Voinko scrobblata automaattisesti ilman CSV-tiedostojen vientiä?" closed="true" %}}
Kyllä. Sekä Evermusic että Flacbox tukevat nyt automaattista Last.fm-scrobblausta. Katso opas: [Kuinka scrobblata Last.fm:iin](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="Entä jos CSV-tiedostossani on yli 14 päivää vanhoja kappaleita?" closed="true" %}}
Käytä Tuontitilaa Last.fm-Scrubbler-WPF:ssä. Se laskee aikaleimat uudelleen Lopetusajasta, jolloin voit scrobblata kappaleita riippumatta niiden alkuperäisestä päivämäärästä.
{{% /details %}}

{{% details title="Minulla ei ole Windows-tietokonetta. Voinko silti käyttää Last.fm-Scrubbleria?" closed="true" %}}
Kyllä. Asenna VirtualBox Mac-tietokoneellesi ja lataa ilmainen Windows-kehitysympäristön levykuva Microsoftilta. Suorita Last.fm-Scrubbler-WPF virtuaalikoneessa.
{{% /details %}}

{{% details title="Miksi joitakin scrobblauksia ei jäsennetä?" closed="true" %}}
Kappaleita, joista puuttuu oleellisia metatietoja (kuten artistin nimi), ei voida jäsentää. Tämä on odotettua eikä vaikuta muihin tiedoston kappaleisiin.
{{% /details %}}

{{% details title="Onko päivittäistä scrobble-rajaa?" closed="true" %}}
Kyllä. Last.fm-Scrubbler-WPF sallii enintään 2 800 scrobblausta päivässä. Jos sinun täytyy scrobblata enemmän, jaa prosessi useille päiville.
{{% /details %}}
