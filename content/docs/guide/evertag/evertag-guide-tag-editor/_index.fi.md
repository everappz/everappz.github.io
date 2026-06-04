---
title: "Tunnistemuokkain"
date: 2020-02-01
description: "Opi käyttämään Evertagin tunnistemuokkainta musiikin metatietojen päivittämiseen, albumin kansikuvien muokkaamiseen, useiden tiedostojen erämuokkaukseen ja MusicBrainz-tunnisteiden hallintaan. Ihanteellinen musiikkikirjastosi järjestämiseen iOS:lla ja Macilla."
keywords: [
  "Evertag tunnistemuokkain", "äänen metatietoeditori", "musiikin tunnistemuokkain",
  "äänitunnisteiden muokkaus iPhone", "albumin kansikuvaeditori", "äänitunnisteiden erämuokkaus",
  "MusicBrainz metatiedot", "musiikin järjestyssovellus", "Evertag opas", "ID3 tunnistemuokkain"
]
tags: ["opas", "evertag", "tunnistemuokkain"]
readingTime: 5
---


**Tunnistemuokkain** on Evertag-sovelluksen päänäyttö, jossa voit tarkastella ja muokata äänitiedostojen metatietoja. Avaa tämä näyttö napauttamalla tiedostoa **Paikalliset tiedostot** -osiosta tai mistä tahansa yhdistetystä **pilvipalvelu**-tilistä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Muokkaustilat

Evertag tarjoaa kaksi muokkaustilaa:

- **Yksittäinen tiedosto -tila**
  - Selaa tiedostojen välillä pyyhkäisemällä vasemmalle tai oikealle kansikuvakarusellissa.

- **Eräkäsittelytila**
  - Muokkaa useita tiedostoja kerralla ja sovella jaettuja metatietoja.
  - Aktivoidaksesi, selaa alas ja napauta **Muokkaa tiedostoja samanaikaisesti**.

## Yksittäinen Tiedosto -tila

Oletusarvoisesti sovellus avaa tunnistemuokkaimen yksittäinen tiedosto -tilassa vain tärkeimmillä muokkausvaihtoehdoilla. Tässä tilassa voit muokata yleisimpiä metatietokenttiä, kuten:

**Kappaleen otsikko, Alaotsikko, Albumin artisti, Albumi, Artisti, Säveltäjä, Esittäjä, Genre, Kommentti, Tahteja minuutissa, Podcast, Kokoelma, Levyn numero, Raidan numero, Raitojen kokonaismäärä, Arvio, Vuosi**

Päästäksesi kaikkiin saatavilla oleviin tunnisteisiin, selaa näytön alareunaan ja napauta **Näytä laajennetut tunnisteet** -vaihtoehtoa. Tämä vaihtaa editorin laajennettuun tilaan, jolloin voit muokata yli **120 metatietokenttää**, mukaan lukien **MusicBrainz-tunnisteet**, **sanoitukset**, **vanhempien ohjausta koskevat arviot**, replay-gain-arvot, lajittelujärjestykset, podcast-metatiedot ja paljon muuta. Käytä **Asetukset → Äänitunnistemuokkain → Painikkeet päänäytöllä** pysyvän Näytä laajennetut tunnisteet -kytkimen aktivoimiseen, jolloin se on aina päällä.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Eräkäsittelytila

Voit siirtyä erämuokkaukseen kahdella tavalla:

1. **Tiedostonhallinnasta**
   - Napauta **Lisää toimintoja** (•••) oikeassa yläkulmassa.
   - Napauta **Valita**, valitse useita tiedostoja ja napauta sitten **Muokata äänitunnisteita**.

2. **Tunnistemuokkaimesta**
   - Avaa mikä tahansa tiedosto, selaa alas ja napauta **Muokkaa tiedostoja samanaikaisesti** ladataksesi kaikki saman kansion tiedostot.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Muokkaamisen jälkeen napauta **Tallentaa** muutosten soveltamiseksi.

## Sanoitusten muokkaaminen

Laajennettu editori näyttää **Sanoitukset**-kentän. Napauta sitä avataksesi sanoitusluettelon — jokaisella sanoitusmerkinnällä on oma kielensä ja kuvauksensa, joten yksittäinen kappale voi tallentaa useita käännöksiä.

Sanoituksia ei tarvitse kirjoittaa alusta asti. Editori sisältää yhden napin hakupikavalinnat suosituimpiin verkon sanoitustietokantoihin, esitäytettyinä nykyisen kappaleen artistilla ja otsikolla:

- **Lrclib** — ensisijainen julkinen tietokanta **ajoitetuille (LRC-tyylisille) sanoituksille**. Käytä sitä, kun haluat synkronoituja sanoituksia, jotka vierittyvät rivi riviltä soittimissa, jotka tukevat niitä.
- **Genius** — laaja luettelo huomautusten ja tarkkojen pelkkä teksti -sanoitusten kanssa.
- **Lyricsify** — yhteisölähtöinen tietokanta yksinkertaisilla ja ajoitetuilla sanoituksilla.
- **Google** — yleinen verkkohaku varasuunnitelmana, kun erillisistä tietokannoista ei löydy vastaavuutta.

Jokainen pikavalikko näkyy vain, kun vastaava palvelu on tavoitettavissa laitteeltasi. Napauta palvelua, kopioi haluamasi sanoitukset (tai LRC-aikaleimat), palaa Evertagiin ja liitä ne tekstikenttään — sitten **Tallentaa** kirjoittaaksesi sanoitukset takaisin äänitiedoston tunnisteisiin.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Valitse kieli valitsimesta:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Liitä tai kirjoita sitten sanoitusteksti. Evertag tukee sekä pelkkää tekstiä että ajoitettuja (synkronoituja) sanoituksia — paikkamerkki näyttää esimerkin LRC-tyylisestä muodosta, joka on täsmälleen se, mitä Lrclib ja Lyricsify palauttavat synkronoiduille tuloksille.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Arvion ja Sisältöluokituksen Asettaminen

Laajennettu editori tarjoaa tähti-**Arvio**-säätimen ja **Sisältöluokitus**-segmenttiohjaimen vierekkäin.

### Tähtiarvio

Käytä **Arvio**-kenttää antaaksesi kappaleelle henkilökohtainen pisteet yhdestä viiteen tähteen. Arvo kirjoitetaan tiedoston standardiarvio-tunnistekenttään (POPM ID3:lle, `rate` MP4:lle, `RATING` Vorbis/APE:lle jne.), joten muut sovellukset, jotka lukevat tätä tunnistetta — mukaan lukien Musiikki-sovellus, Plex, Roon ja useimmat työpöydän tunnistemuokkaimet — poimivat arvosi välittömästi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Sisältöluokitus

**Sisältöluokitus** merkitsee kappaleen sisällön käyttämällä yhtä iTunes Store -kaupan ja useimpien musiikkialustojen käyttämän Parental Advisory -standardin arvoista:

- **Haitaton** — oletus kappaleille ilman vanhempien neuvontaa koskevia tietoja. Tiedostoa käsitellään kaikille kuuntelijoille sopivana, eikä siinä näy neuvontaetiketti soittimissa, jotka kunnioittavat tunnistetta.
- **Eksplisiittinen** — kappale sisältää eksplisiittistä kieltä tai sisältöä. Soittimet, jotka noudattavat lapsilukituksia (Musiikki-sovellus, Apple TV -sovellus, Spotify-viennit, Plex jne.) näyttävät **E**-merkin otsikon vieressä, ja kun laitteen tai tilin rajoitukset ovat käytössä, voivat piilottaa kappaleen lasten profiileista tai kieltäytyä toistamasta sitä.
- **Puhdas** — muuten eksplisiittisen kappaleen sensuroitu tai muokattu versio. Soittimet näyttävät **C**-merkin, jotta kuuntelijat voivat erottaa puhtaan muokkauksen alkuperäisestä eksplisiittisestä masterista, mikä on hyödyllistä, kun molemmat versiot ovat samassa kirjastossa.

Sinun kannattaa asettaa tai korjata tämä kenttä, kun:

- Tiedostolla on väärä merkintä (esimerkiksi puhdas radioversio, joka on virheellisesti merkitty eksplisiittiseksi, tai päinvastoin).
- Kappaleet on äänitetty tai ladattu ilman tunnistetta ja näkyvät nyt haitattomina, vaikka ne sisältävät eksplisiittistä sisältöä.
- Valmistat albumia lähetystä tai jakamista varten ja sinun on varmistettava, että jokaisella kappaleella on johdonmukaiset metatiedot.
- Haluat CarPlayn, lukitusnäytön, Apple Music -tyylisten soitinten tai DJ-ohjelmiston näyttävän oikean **E** / **C** -merkin kappaleen otsikon vieressä.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Albumin Kansikuvan Muokkaaminen

Albumin kansikuvan vaihtaminen:

1. Napauta **Kamera-kuvaketta** kansikuvakarusellissa.
2. Valitse kuvan sijainti: Paikalliset tiedostot, Pilvi, Lataukset tai Kuvat-kirjasto.
3. Valitse kuva, jota käytetään kansikuvana.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Lisää Toimintoja Tunnistemuokkaimessa

Lisämuokkausvaihtoehdot ovat saatavilla kansikuvanäkymän alla olevan työkalupalkin kautta.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Automaattinen Äänitunnisteiden Haku

Tämä toiminto aktivoi älykkään tunnistehakukoneen, joka löytää ja täyttää äänitiedostosi täydelliset metatiedot olemassa olevien tietojen perusteella.
Sovellus käyttää MusicBrainz-tietokantaa — yhtä kattavimmista tunnistekannoista — yli **50 miljoonalla** kappaleella.

### Etsi Albumin Kansikuvaa

Käytä metatietoja hakemaan verkosta oikea albumin kansikuva.

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Kun löydetty, tallenna kuva **Kuviin** järjestelmän kontekstivalikon avulla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Sen jälkeen palaa tunnistemuokkaimeen, napauta Kamera-kuvaketta, siirry **Kuvat-kirjastoon** ja valitse tallennettu kuva. Sovellus asettaa sen äänitiedostosi kansikuvaksi.

Voit säätää, miten kansikuvat skaalataan sovelluksen asetuksissa.

### Tallenna Albumin Kansitaide

Tämä toiminto tallentaa nykyisen albumin kansitaiteen **Documents**-kansioon, jotta voit käyttää sitä myöhemmin uudelleen.

### Normalisoi Koodaus

Tämä toiminto normalisoi kaikkien äänitiedoston metatietojen tunnisteiden tekstikoodauksen. Se on erityisen hyödyllinen, jos siirryt Windows-tietokoneelta, jossa tiedostot saattavat käyttää eri koodauksia, jotka näkyvät Macilla lukukelvottomina tai vioittuneina merkkeinä.

### Manuaalinen Tunnistehaku

Etsi albumin metatietoja manuaalisesti MusicBrainz-tietokannan avulla.

- Valitse albumi

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Valitse oikea kappale

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Valitse, mitkä tunnisteet otetaan käyttöön

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Napauta **Valmis** soveltaaksesi valitut metatiedot kappaleellesi.

### Poista Äänitunnisteet

Tyhjennä kaikki tiedoston metatietokentät. Hyödyllinen aloittaessa alusta. Vahvista napauttamalla **Tallentaa**.

## Tunnistemuokkaimen Asetukset

Siirry kohtaan **Asetukset → Äänitunnistemuokkain** käytöksen mukauttamiseksi.

### Albumin Kansikuvan Skaalaus

Valitse, miten albumin kansikuvat tulisi skaalata tallennettaessa äänitiedostoihin. Voit poistaa skaalauksen käytöstä alkuperäisen kuvan koon säilyttämiseksi, mutta muista, että jotkin soittimet eivät välttämättä tue suuria kansikuvatiedostoja. «Alkuperäinen koko» -vaihtoehto on osa Premium-personointiin liittyviä ominaisuuksia.

### Tunnisteiden Tallennusasetukset

- **ID3v2.4** — Kun käytössä, sovellus tallentaa tunnisteet ID3v2.4-muodossa mahdollisuuksien mukaan. Poista käytöstä palataksesi laajemmin tuettuun ID3v2.3:een, jos äänitunnisteesi eivät näy oikein vanhemmissa soittimissa tai laitteissa.
- **Kopiotunnisteet** — Kun käytössä, yleiset metatietokentät kopioidaan tiedoston molempiin tunnisteosuuksiin. Tämä parantaa yhteensopivuutta vanhempien äänisoitinten kanssa, mutta useimmissa tapauksissa se ei ole tarpeen.

### Pilvipalvelutiedostojen Metatietojen Päivitysasetukset

Voit hallita, miten sovellus päivittää pilvipalveluihin tallennettujen äänitiedostojen metatiedot:

- **Näytä vahvistusviesti**
  Kysy ennen metatietomuutosten soveltamista pilvipalvelutiedostoihin.

- **Päivitä tiedoston metatiedot automaattisesti**
  Tallenna metatietomuutokset pilvipalvelutiedostoon automaattisesti muokkaamisen jälkeen.

- **Älä päivitä tiedoston metatietoja**
  Ohita pilvipalvelutiedostojen päivittäminen — muutokset sovelletaan vain paikallisesti.

### Online-tiedostojen Muokkaaminen

Valitse, mitä paikallisesti ladatuille kopioille pilvipalvelutiedostoista tapahtuu muokkaamisen jälkeen:

- **Poista ladattu tiedosto aina**
  Poista paikallinen kopio muutosten tallentamisen jälkeen.

- **Älä poista ladattua tiedostoa**
  Säilytä ladattu tiedosto laitteellasi muokkaamisen jälkeen.

### Päänaytön Painikkeet

Mukauta, mitkä toiminnot näkyvät tunnistemuokkaimen päänäytöllä (Automaattinen tunnisteiden haku, Manuaalinen tunnisteiden haku, Etsi albumin kansitaidetta, Tallenna albumin kansitaide, Normalisoi koodaus, Poista äänitunnisteet). Voit myös kytkeä **Näytä laajennetut tunnisteet** ja **Muokkaa tiedostoja samanaikaisesti** päälle, jotta editori avautuu aina haluamassasi tilassa.
