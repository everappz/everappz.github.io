---
title: "Kuinka käyttää äänitehosteita ja DSP:tä Flacboxissa: kompressori, Freeverb, ristisyöttö, kaiku, äänenvoimakkuuden normalisointi ja paljon muuta (jokainen esiasetus ja säätö selitettynä)"
date: 2026-07-24
description: "Täydellinen opas Flacboxin äänentoistoon iPhonella, iPadilla ja Macilla. Opi, miten BASS-moottori toimii, mitä lisäformaatteja se toistaa (mukaan lukien MOD- ja trackermusiikki sekä DSD) ja mitä tarkalleen jokainen tehoste, jokainen liukusäädin ja jokainen esiasetus tekee äänellesi, sekä 10-kaistainen taajuuskorjain ja mukautettu DSP-ketju."
keywords: ["Flacbox äänitehosteet", "Flacbox esiasetukset selitettynä", "Flacbox BASS-moottori", "BASS-äänikirjasto iOS", "MOD-musiikkisoitin iPhone", "trackermusiikkisoitin iOS", "toista MOD XM IT S3M iPhone", "DSD-soitin iOS", "FLAC-soitin iPhone", "häviötön musiikkisoitin iOS", "Flacbox taajuuskorjaimen esiasetukset", "10-kaistainen taajuuskorjain iPhone", "äänenvoimakkuuden normalisointi iPhone", "EBU R128 iOS", "äänekkyyden normalisointi musiikkisoitin", "ristisyöttö kuulokkeet iOS", "bs2b ristisyöttö", "kompressorin esiasetukset musiikkisoitin", "freeverb kaiku iOS", "kaiku viive musiikkisoitin", "DSP-ketju musiikkisoitin", "basson korostus iPhone", "kuinka lisätä tehosteita musiikkiin Flacbox", "parhaat taajuuskorjaimen asetukset iPhone"]
tags: ["Flacbox", "Äänitehosteet", "Kuinka tehdä", "BASS", "Taajuuskorjain", "Basson korostus", "Kompressori", "Freeverb", "Ristisyöttö", "Kaiku", "Äänenvoimakkuuden normalisointi", "EBU R128", "MOD-musiikki", "Trackermusiikki", "DSD", "FLAC", "DSP", "Kuulokkeet", "Esiasetukset"]
readingTime: 30
---

{{< author-byline >}}

**Lyhyt vastaus:** Flacboxissa valitset yhden **toistomoottorin** kohdasta **Asetukset > Äänisoitin**: **Standard** (Applen järjestelmämoottori), **Universal** (FFmpeg-moottori) tai **Sound FX** (**BASS™-moottori**). Valitsemasi moottori määrää, mitkä tiedostomuodot toistuvat, joten valinnalla on väliä. **Sound FX** -moottori toistaa lisäformaatteja, jotka useimmat iPhone-sovellukset ohittavat (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus sekä vanha **MOD- ja trackermusiikki** kuten MOD, XM, IT ja S3M), ja se on ainoa moottori, joka käyttää äänityökaluja: **10-kaistainen taajuuskorjain**, **äänenvoimakkuuden normalisointi**, **kompressori**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **kaiku**, **Chorus**, **säröytys**, **kierto**, **ristisyöttö** ja itse rakennettava **DSP-ketju**. Jotta voisit siis käyttää tämän oppaan tehosteita, aseta toistomoottoriksi ensin **Sound FX**. Jokaisella työkalulla on valmiit **esiasetukset**. Avaa ne kohdasta **Asetukset > Äänisoitin** (Äänitehosteet, Äänen taajuuskorjain, Signaalinkäsittely), tai napauta soittimen **⋯ (Lisää)** -painiketta ja valitse **Äänitehosteet**. Mikään täällä tekemäsi ei koskaan muuta tiedostojasi.

> Alla olevat liukusäätimien ja esiasetusten selitykset ovat samat lyhyet kuvaukset, jotka Flacbox näyttää sinulle sovelluksen sisällä, täydennettynä pienellä lisätaustalla, jotta saat kokonaiskuvan ennen napautusta.

## Kuinka lukea tätä opasta

Jokainen työkalu toimii samalla tavalla:

1. **Kytke se päälle.** Jokaisella tehosteella on oma päälle/pois-kytkin. Ne ovat kaikki alussa pois päältä. Voit kytkeä päälle niin monta kuin haluat samanaikaisesti.
2. **Valitse esiasetus.** Esiasetus on valmis asetus. Napauta yhtä, ja ääni muuttuu heti. Tässä oppaassa luetellaan, mitä **jokainen** esiasetus tekee.
3. **Hienosäädä (valinnainen).** Avaa liukusäätimet säätääksesi käsin. Sillä hetkellä kun liikutat liukusäädintä, tehoste näyttää **Manual**, jotta tiedät poistuneesi esiasetuksesta. Jokaisella liukusäätimellä on nollauspainike.

Mitään ei tallenneta tiedostoihisi. Nämä ovat reaaliaikaisia tehosteita. Kytke tehoste pois päältä, ja alkuperäinen äänesi palaa heti.

## Valitse toistomoottori (Sound FX sisältää tehosteet)

Flacbox ei sekoita moottoreita keskenään. Valitset **yhden** kohdasta **Asetukset > Äänisoitin > Toistomoottori**, ja valitsemasi moottori määrää, mitkä tiedostomuodot voit toistaa ja ovatko tehosteet käytettävissä. Vaihtoehtoja on kolme, ja ne näkyvät sovelluksessa näillä tarkoilla nimillä:

1. **Standard.** Applen sisäänrakennettu järjestelmämoottori. Käyttää laitteistopurkua alhaisempaan akun kulutukseen.
2. **Universal.** FFmpeg-moottori, joka avaa erittäin laajan valikoiman formaatteja.
3. **Sound FX.** **BASS™-moottori**. Se toistaa häviöttömät ja korkearesoluutioiset tiedostot täydellä tarkkuudella, lisää moduuli- (tracker-) musiikin ja käyttää tämän oppaan jokaista tehostetta, 10-kaistaista taajuuskorjainta ja DSP-ketjua.

Koska jokainen moottori tukee omaa formaattijoukkoaan, toistettavissa olevat tiedostot vaihtelevat valitsemasi moottorin mukaan. Vielä tärkeämpää on, että tehosteet, taajuuskorjain ja DSP-ketju toimivat **vain** **Sound FX** -moottorilla, joten valitse se ensin, jos haluat käyttää niitä.

Sound FX perustuu **BASS™**-kirjastoon, ammattitason äänikirjastoon Un4seen Developmentsilta. Voit lukea siitä lisää sen kotisivulta osoitteessa [un4seen.com](https://www.un4seen.com/).

## Musiikkiformaatit: mitä Sound FX (BASS™) -moottori lisää (mukaan lukien MOD- ja trackermusiikki)

Kun **Sound FX (BASS™)** -moottori on valittuna, Flacbox toistaa alla olevat erikoisformaatit tavallisten päälle. Kaikkein erikoisin on **moduulimusiikki**, jota kutsutaan myös **trackermusiikiksi**. Moduulitiedosto ei ole tavallinen nauhoitus. Se sisältää pieniä soitinääniä sekä «partituurin», joka kertoo, miten niitä soitetaan, ja Flacbox rakentaa kappaleen uudelleen reaaliajassa tuosta partituurista, sillä tavalla kuin nämä tiedostot oli tarkoitettu toistettaviksi. Tavalliset soittimet eivät osaa tätä.

| Musiikin tyyppi | Formaatit | Hyvä tietää |
|---|---|---|
| **Moduuli- / trackermusiikki** | MOD, XM, IT, S3M, MTM, UMX, MO3 | BASS™-moduulisoitin rakentaa reaaliajassa uudelleen. Loistava chiptunelle ja vanhalle demoscene- tai Amiga-musiikille. |
| **Moderni häviötön** | FLAC | Täysi laatu, pienempi kuin WAV. |
| **Muu häviötön** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Harvinaisemmat häviöttömät tyypit, kaikki tuettuina. |
| **Korkearesoluutioinen DSD** | DSF, DFF | Toistuu tavallisella laitteistolla käyttäen DSD over PCM -menetelmää. |
| **Moderni häviöllinen** | Opus, Ogg Vorbis, MP3 | Tavalliset suoratoisto- ja lataustyypit. |

Sound FX -moottori toistaa myös yleiset Apple-formaatit (AAC, ALAC, M4A, WAV, AIFF) ja suoratoistot, joten tehosteet ja taajuuskorjain toimivat myös niissä.

**Miksi tästä on hyötyä sinulle:** jos sinulla on sekoitus FLAC-albumeja, korkearesoluutioisia DSD-tiedostoja ja kansiollinen vanhoja MOD- tai XM-trackerkappaleita, Flacbox toistaa ne kaikki, ja taajuuskorjain sekä tehosteet toimivat jokaisessa niistä.

## Kolme valikkoa, joita käytät

Flacbox pitää äänityökalunsa kolmessa paikassa, kaikki äänisoittimen asetusten sisällä. Varmista ensin, että **toistomoottoriksi** on asetettu **Sound FX** (Asetukset > Äänisoitin > Toistomoottori), koska tehosteet, taajuuskorjain ja DSP-ketju ovat käytettävissä vain tuolla moottorilla.

- **Äänitehosteet** (tehostetelakka): avaa soitin, napauta **⋯ (Lisää)**, napauta **Äänitehosteet**. Tai mene kohtaan **Asetukset > Äänisoitin > Äänitehosteet**.
- **Äänen taajuuskorjain** (10 kaistaa ja esiasetukset): **Asetukset > Äänisoitin > Äänen taajuuskorjain**.
- **Signaalinkäsittely** (oma DSP-ketjusi): **Asetukset > Äänisoitin > Signaalinkäsittely**.

Voit myös asettaa **lähdön näytteenottotaajuuden**, **kanavat** ja **puskurin koon** kohdassa **Asetukset > Äänisoitin**.

## 10-kaistainen taajuuskorjain

**Mitä se tekee:** Muuttaa musiikin sävyä syvästä bassosta kirkkaaseen diskanttiin. Tämä on paras työkalu puhtaaseen **basson korostukseen** tai kirkkaampaan, selkeämpään yläpäähän. Ajattele sitä kymmenenä äänenvoimakkuusnuppina, joista jokainen vastaa eri äänen viipaletta. Nosta kaistaa tuodaksesi kyseisen osan esiin, laske vetääksesi se taakse. Muutaman dB:n pienet muutokset kuulostavat yleensä parhailta, ja se toimii kaikessa, mitä toistat.

**Miten se toimii:** Kymmenen liukusäädintä taajuuksilla **32, 64, 125, 250, 500 Hz sekä 1, 2, 4, 8, 16 kHz**. Jokainen vaihtelee välillä **-12 dB (leikkaus)** ja **+12 dB (korostus)**. Lisäksi on **esivahvistin** väliltä **-24 ja +24 dB** kokonaistasoa varten. Voit tallentaa omia esiasetuksiasi ja **viedä tai tuoda** niitä laitteiden välillä.

**Mitä jokainen sisäänrakennettu esiasetus tekee (22 esiasetusta):**

| Esiasetus | Mitä se tekee äänellesi |
|---|---|
| **Flat** | Ei muutosta. Kaikki kaistat nollassa. Puhdas lähtökohta. |
| **Acoustic** | Lämmin basso ja terävät, läsnä olevat diskantit. Saa akustiset kitarat ja äänet tuntumaan luonnollisilta ja eläviltä. |
| **Bass Booster** | Vahva nosto matalassa päässä, keskialue ja diskantit koskemattomina. Lisää potkua ja painoa. |
| **Bass Reducer** | Leikkaa matalaa päätä. Kätevä jyriseviin tiloihin, halpoihin nappikuulokkeisiin tai raskaisiin kappaleisiin. |
| **Treble Booster** | Nostaa vain diskantteja. Lisää kimallusta ja ilmavuutta, enemmän yksityiskohtia. |
| **Treble Reducer** | Pehmentää diskantteja. Kesyttää kovia tai teräviä nauhoituksia. |
| **Classical** | Täysi matala pää ja lempeät diskantit pienellä keskialueen kuopalla. Pehmeä ja tilava orkesterimusiikille. |
| **Dance** | Suuret matalat ja kirkkaat diskantit kuopatuilla keskitaajuuksilla. Napakka ja energinen klubikappaleille. |
| **Deep** | Lämmin, paksu matala pää pehmeämmillä diskanteilla. Kotoisa, rento ääni. |
| **Electronic** | Vahva basso ja kirkkaat diskantit syntetisaattoreille ja biiteille. Leveä ja moderni. |
| **Hip-Hop** | Raskas basso ja selkeät diskantit hallituilla keskitaajuuksilla. Painava ja napakka. |
| **Jazz** | Lämmin ja pehmeä, pienellä keskialueen kuopalla. Helppo ja luonnollinen akustiselle jazzille. |
| **Latin** | Korostetut matalat ja diskantit puhtailla keskitaajuuksilla. Kirkas ja eloisa. |
| **Loudness** | Korostaa bassoa ja diskanttia voimakkaasti («hymy»-käyrä). Kuulostaa täyteläisemmältä matalalla äänenvoimakkuudella. |
| **Lounge** | Eteen tuodut keskitaajuudet pehmein reunoin. Rentoutunut ja lauluäänelle sopiva. |
| **Piano** | Selkeät keskitaajuudet ja diskantit, jotta pianonuotit soivat puhtaasti. |
| **Pop** | Nostetut keskitaajuudet lauluäänelle, matalat ja diskantit vedettyinä taakse. Äänet istuvat edessä. |
| **R&B** | Erittäin vahva ala-keskialueen lämpö ja selkeät diskantit. Pehmeä ja täyteläinen. |
| **Rock** | Korostetut matalat ja diskantit kitaroille ja rummuille. Energinen ja täyteläinen. |
| **Small Speakers** | Korostaa matalia ja leikkaa diskantteja auttaakseen pieniä kaiuttimia kuulostamaan täyteläisemmiltä. |
| **Spoken Word** | Nostaa ääni-aluetta ja leikkaa syvää bassoa. Tekee puheesta selkeää. |
| **Vocal Booster** | Työntää keskialuetta, jossa äänet elävät, leikkaa niiden ympäriltä. Lauluäänet erottuvat. |

**Vinkki bassoon:** Aloita **Bass Boosterilla**, ja jos se kuulostaa sameelta, vedä esivahvistinta alas 1–2 dB, jottei mikään säröydy.

## Äänenvoimakkuuden normalisointi (tasainen äänekkyys)

**Mitä se tekee:** Jotkin kappaleet soivat kovempaa kuin toiset, joten muutat äänenvoimakkuutta jatkuvasti. Tämä saa jokaisen kappaleen soimaan suunnilleen samalla äänenvoimakkuudella itsestään, joten sinun ei tarvitse. Se sopii täydellisesti satunnaistetuille soittolistoille, jotka sekoittavat vanhoja ja uusia nauhoituksia, eri albumeja tai eri lähteitä, joissa yksi kappale voi olla paljon kovempi kuin seuraava.

**Miten se toimii:** Se kuuntelee jokaisen kappaleen todellista äänekkyyttä käyttäen **EBU R128** -standardia (mitattuna **LUFS**-yksikössä, saman idean, jota suoratoistopalvelut käyttävät), ja säätää sitten jokaisen kappaleen kohti tavoitettasi. Se ei tarvitse tunnisteita tiedostoihisi eikä koskaan muuta ääntä. EBU R128 mittaa äänekkyyden, jonka korvasi todella tuntevat koko kappaleen aikana, ei vain korkeinta huippua, minkä vuoksi se vastaa sitä, miltä kappaleet todella tuntuvat sinusta. Flacbox laskee tämän reaaliajassa musiikin soidessa (ja tarkistaa äänekkyyden etukäteen kun voi), ja soveltaa sitten kappaleeseen yhden tasaisen äänenvoimakkuusmuutoksen. **Max boost** -raja estää erittäin hiljaisia nauhoituksia tulemasta työnnetyiksi ylös niin voimakkaasti, että ne säröytyvät. Koska se lukee itse ääntä, se toimii missä tahansa lähteessä, mukaan lukien pilvitiedostot, suoratoistot ja moduulimusiikki, silloinkin kun tiedostoissa ei ole lainkaan äänekkyystunnisteita.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Target loudness** | Asettaa äänekkyyden, jota kohti jokainen kappale tasataan. Korkeammat arvot saavat kaiken soimaan kokonaisuutena kovempaa. | -30 – -6 LUFS (-16) |
| **Max boost** | Rajoittaa, kuinka paljon hiljaisia kappaleita voidaan vahvistaa. Korkeammat arvot tuovat pehmeät nauhoitukset lähemmäs tavoitetta. | 0 – 24 dB (12) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Light** | Lempeä tasaus rentoon kuunteluun. Tasoittaa ilmeiset äänenvoimakkuuden hypyt työntämättä hiljaisia kappaleita voimakkaasti. |
| **Standard** | Yleiskäyttöinen oletus. Suoratoistotyylinen äänekkyystavoite, joka sopii useimpaan musiikkiin. Aloita tästä. |
| **Strong** | Aggressiivinen sovitus, joka työntää hiljaisia kappaleita ylös lujasti. Paras sekakirjastoille, joissa on suuria tasoeroja. |
| **Night** | Hiljaisempi kokonaistavoite, joka silti nostaa pehmeitä kohtia, jotta myöhäisillan kuuntelu pysyy tasaisena ja matalana. |

## Kompressori (tasoita kovat ja hiljaiset osat)

**Mitä se tekee:** Yhdessä kappaleessa hiljaiset osat voivat olla liian pehmeitä ja kovat osat liian kovia. Tämä tuo ne lähemmäs toisiaan, joten koko kappale on helppo kuulla, jopa autossa tai meluisassa paikassa. Se kääntää lempeästi kovimmat hetket alas ja nostaa pehmeämmät, joten et enää tavoittele äänenvoimakkuutta yhden kappaleen aikana. Tämä eroaa äänenvoimakkuuden normalisoinnista: kompressori tasoittaa asioita **yhden** kappaleen **sisällä**, kun taas äänenvoimakkuuden normalisointi sovittaa äänekkyyttä kappaleiden **välillä**. Nämä kaksi toimivat hyvin yhdessä. Aloita esiasetuksesta ja avaa liukusäätimet vain, jos haluat lisää hallintaa.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Threshold** | Taso, jolla kompressio alkaa. Matalammat arvot litistävät enemmän ääntä pitäen hiljaiset ja kovat osat lähempänä toisiaan. | -60 – 0 dB (-20) |
| **Ratio** | Kuinka voimakkaasti kovia osia pidätellään sen jälkeen, kun ne ylittävät kynnyksen. Korkeammat arvot pakkaavat kovempaa pitäen äänen tasaisempana. | 1:1 – 30:1 (4:1) |
| **Attack** | Kuinka nopeasti tehoste reagoi äkilliseen kovaan huippuun. Lyhyet arvot nappaavat transientit; pidemmät päästävät ne läpi. | 0.1 – 1000 ms (10 ms) |
| **Release** | Kuinka nopeasti tehoste päästää irti kovan osan mentyä. Lyhyet arvot voivat pumpata; pidemmät kuulostavat pehmeämmiltä. | 10 ms – 5 s (100 ms) |
| **Master gain** | Lopullinen lähdön korostus käsittelyn jälkeen. Nosta tätä nostaaksesi kokonaisäänekkyyttä, kun dynamiikka on tasattu. | -30 – +30 dB (0) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Transparent** | Tuskin havaittava turvaverkko. Säilyttää dynamiikan lähes kokonaan ja nappaa vain kovimmat huiput. |
| **Soft** | Kevyt tasaus hi-fi-kuunteluun kotona. Hienovarainen tasoitus musiikkia litistämättä. |
| **Standard** | Järkevä oletus jokapäiväiseen musiikin toistoon. Ensimmäinen kokeiltava esiasetus. |
| **Heavy** | Aggressiivinen tasaus meluisiin ympäristöihin. Auto, täysi huone, matalan äänenvoimakkuuden kuuntelu. |
| **Voice / Podcast** | Puheeseen viritetty. Hitaampi attack päästää sihahdukset läpi, antelias korvausvahvistus nostaa lauluäänet ylös. |
| **Old Recordings** | Vanhat albumit ja entisöity vinyyli, joissa keskimääräinen taso on modernien julkaisujen alapuolella. |
| **Late Night** | Raskas kompressio sekä suuri korostus hiljaiseen kuunteluun, kun naapurit tai nukkuva perhe merkitsevät. |
| **Movie Dialog** | Tuo puheen esiin musiikkia ja äänitehosteita vasten vaihtelevassa ääniraidassa. |
| **Streaming Match** | Tavoittelee suunnilleen modernien suoratoistopalveluiden äänekkyyden normalisointia noin -14 LUFS. |
| **Maximum Loudness** | Kaikki peliin. Osuu rajoittimeen; odota litistettyä, erittäin tasaista signaalia. Kirjaimellinen maksimiäänenvoimakkuuden esiasetus. |

## Freeverb (kaiku, tilan tuntu)

**Mitä se tekee:** Lisää musiikkiin tilan tuntua, pienestä huoneesta suureen saliin. Valitse esiasetus tai hienosäädä itse kuivan ja märän sekoitusta, huoneen kokoa, vaimennusta ja leveyttä. Kaiku on luonnollinen kaiku, jonka kuulet missä tahansa oikeassa tilassa, ja Freeverb luo sen uudelleen ohjelmistolla. Pieni määrä saa litteät tai lähimikitetyt nauhoitukset tuntumaan avoimemmilta ja elävämmiltä. Suuri määrä sijoittaa musiikin suureen, kaukaiseen tilaan. Se on luova tehoste, joten pidä märkä sekoitus maltillisena luonnollisiin tuloksiin.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Dry mix** | Kuinka paljon alkuperäistä, koskematonta ääntä säilytetään. Korkeammat arvot jättävät enemmän kuivaa signaalia sekoitukseen. | 0 – 1 (0.0) |
| **Wet mix** | Kuinka paljon kaikuvaa ääntä lisätään. Korkeammat arvot tekevät kaiusta kovemman ja ilmeisemmän. | 0 – 3 (1.0) |
| **Room size** | Kuvitellun tilan koko. Korkeammat arvot antavat pidemmän, suuremman kaikuhännän, pienestä huoneesta katedraaliin. | 0 – 1 (0.5) |
| **Damp** | Kuinka nopeasti korkeat taajuudet häviävät hännässä. Korkeammat arvot tekevät kaiusta tummemman ja lämpimämmän. | 0 – 1 (0.5) |
| **Width** | Kaiun stereolevitys. Korkeammat arvot tekevät tilasta leveämmän vasemman ja oikean kanavan välillä. | 0 – 1 (1.0) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Room** | Pieni, tiivis tila. Hienovarainen tunnelma, joka lisää paikan tuntua huuhtomatta ääntä pois. |
| **Studio** | Kuiva, hallittu nauhoitustila. Juuri tarpeeksi heijastusta kuulostaakseen luonnolliselta. |
| **Hall** | Suuri konserttisali. Pitkä, rehevä häntä, joka sopii orkesteri- ja akustiselle musiikille. |
| **Cathedral** | Valtava, kaikuva kivitila. Pisin, dramaattisin kaikuhäntä. |
| **Plate** | Kirkas, tiheä studion levykaiku. Klassinen lauluäänille ja rummuille. |
| **Ambience** | Lyhyt, ilmava tunnelma. Lisää kevyen tilan tunnun pysyen enimmäkseen kuivana. |

## Auto Wah (funkahtava suodatinpyyhkäisy)

**Mitä se tekee:** Suodatin, joka pyyhkäisee ylös ja alas itsestään funkahtavaan, lauluäänen kaltaiseen wah-ääneen. Valitse esiasetus tai aseta itse märkä sekoitus, takaisinkytkentä, nopeus, alue ja taajuus. Se on sama «wah»-pyyhkäisy, jonka kitaran wah-pedaali tekee, mutta täällä se liikkuu itsestään musiikin tahdissa. Se kuulostaa loistavalta funk-, disco- ja elektronisissa kappaleissa. Se on rohkea, ilmeinen tehoste, joten pieni määrä riittää pitkälle jokapäiväisessä kuuntelussa.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Wet mix** | Kuinka voimakas wah-tehoste on sekoituksessa. Korkeammat arvot tekevät pyyhkäisevästä suodattimesta ilmeisemmän. | -2 – +2 (1.5) |
| **Feedback** | Kuinka paljon lähtöä kytketään takaisin tehosteeseen. Korkeammat arvot tekevät wah:sta resonoivamman ja korostetumman. | -1 – +1 (0.5) |
| **Rate** | Kuinka nopeasti suodatin pyyhkäisee ylös ja alas. Korkeammat arvot antavat nopeamman, rytmisemmän wah:n. | 0.1 – 9 Hz (2.0) |
| **Range** | Kuinka pitkälle suodatin pyyhkäisee, oktaaveina. Korkeammat arvot antavat leveämmän, dramaattisemman pyyhkäisyn. | 0.1 – 9 oktaavia (4.3) |
| **Frequency** | Perustaajuus, jonka ympärillä suodatin pyyhkäisee. Matalammat arvot kuulostavat syvemmiltä; korkeammat kirkkaammilta. | 1 – 1000 Hz (50) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Classic** | Tasapainoinen, klassinen wah-pyyhkäisy. Hyvä lähtökohta funkille ja rockille. |
| **Slow** | Hidas, leveä pyyhkäisy, joka ajautuu lempeästi ylös ja alas. Loistava padeille ja pitkille nuoteille. |
| **Funky** | Nopea, napakka pyyhkäisy runsaalla liikkeellä. Lisää rytmistä puraisua kitaroihin ja syntetisaattoreihin. |
| **Deep** | Syvä, leveä pyyhkäisy, joka alkaa matalasta taajuudesta. Suuri ja dramaattinen. |
| **Subtle** | Lempeä, huomaamaton liike. Lisää luonnetta hallitsematta ääntä. |
| **Resonant** | Terävä, resonoiva wah korkealla takaisinkytkennällä. Lauluäänen kaltainen ja ilmaisuvoimainen. |

## Phaser (pyörteilevä humahdus)

**Mitä se tekee:** Pyyhkäisevä suodatin, joka lisää ääneen pyörteilevän, humahtavan liikkeen. Valitse esiasetus tai aseta itse takaisinkytkentä, nopeus, alue ja taajuus. Se lisää lempeää liikettä ja kimallusta muuttamatta nuotteja. Se on hienovarainen lauluäänillä ja padeilla ja dramaattinen syntetisaattoreilla ja kitaroilla. Kokeile Slow:ta unenomaiseen tuntuun tai Jet:iä voimakkaaseen pyörteeseen.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Feedback** | Kuinka paljon lähtöä kytketään takaisin tehosteeseen. Korkeammat arvot tekevät phaserista resonoivamman ja korostetumman. | -1 – +1 (0.0) |
| **Rate** | Kuinka nopeasti suodatin pyyhkäisee ylös ja alas. Korkeammat arvot antavat nopeamman, rytmisemmän vaiheistuksen. | 0.1 – 9 Hz (1.0) |
| **Range** | Kuinka pitkälle suodatin pyyhkäisee, oktaaveina. Korkeammat arvot antavat leveämmän, dramaattisemman pyyhkäisyn. | 0.1 – 9 oktaavia (4.0) |
| **Frequency** | Perustaajuus, jonka ympärillä suodatin pyyhkäisee. Matalammat arvot kuulostavat syvemmiltä; korkeammat kirkkaammilta. | 1 – 1000 Hz (100) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Classic** | Tasapainoinen, klassinen phaser-pyyhkäisy. Hyvä lähtökohta kitaroille ja koskettimille. |
| **Slow** | Hidas, leveä pyyhkäisy, joka ajautuu lempeästi ylös ja alas. Loistava padeille ja pitkille nuoteille. |
| **Fast** | Nopea, kimalteleva pyyhkäisy runsaalla liikkeellä. Lisää liikettä ja energiaa. |
| **Deep** | Syvä, leveä pyyhkäisy, joka alkaa matalasta taajuudesta. Suuri ja dramaattinen. |
| **Subtle** | Lempeä, huomaamaton liike. Lisää luonnetta hallitsematta ääntä. |
| **Jet** | Voimakas, resonoiva pyyhkäisy korkealla takaisinkytkennällä, klassinen suihkukoneen humahdus. |

## Flanger (suihkukoneen pyyhkäisy)

**Mitä se tekee:** Lyhyt, liikkuva viive, joka antaa äänelle suihkukoneen kaltaisen, pyyhkäisevän humahduksen. Valitse esiasetus tai aseta itse syvyys, takaisinkytkentä, nopeus ja viive. Se on phaserin voimakkaampi, metallisempi serkku, kuuluisa klassisen rockin ja elektronisen musiikin humahtavasta pyyhkäisystä. Hienovaraiset asetukset lisäävät lempeää liikettä, kun taas syvät asetukset ovat dramaattisia ja ilmeisiä. Käytä parhaiten säästeliäästi, tehostukseen.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Depth** | Kuinka voimakas pyyhkäisevä tehoste on. Korkeammat arvot tekevät flangingista ilmeisemmän. | 0 – 100% (25) |
| **Feedback** | Kuinka paljon lähtöä kytketään takaisin tehosteeseen. Korkeammat arvot tekevät flangerista resonoivamman ja metallisemman. | -99 – +99% (-50) |
| **Rate** | Kuinka nopeasti pyyhkäisy liikkuu ylös ja alas. Korkeammat arvot antavat nopeamman, kimaltelevamman liikkeen. | 0 – 10 Hz (0.25) |
| **Delay** | Perusviiveaika, jolle pyyhkäisy rakentuu. Korkeammat arvot antavat syvemmän, onttomman luonteen. | 0 – 4 ms (2.0) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Classic** | Tasapainoinen, klassinen flanger. Hyvä lähtökohta kitaroille ja koskettimille. |
| **Subtle** | Lempeä, huomaamaton pyyhkäisy. Lisää liikettä hallitsematta ääntä. |
| **Deep** | Syvä, raskas pyyhkäisy vahvalla takaisinkytkennällä. Suuri ja dramaattinen. |
| **Jet** | Voimakas pyyhkäisy positiivisella takaisinkytkennällä, klassinen suihkukoneen humahdus. |
| **Fast** | Nopea, kimalteleva pyyhkäisy runsaalla liikkeellä ja energialla. |
| **Wide** | Hidas, leveä pyyhkäisy pitkällä viiveellä. Rehevä ja tilava. |

## Kaiku (toistot)

**Mitä se tekee:** Toistaa äänen häipyvinä kaikuina tilan ja syvyyden tunnun luomiseksi. Valitse esiasetus tai aseta itse märkä sekoitus, takaisinkytkentä ja viive. Se on kuin huutaisit kanjonissa: ääni palaa kerran tai useammin lyhyen tauon jälkeen. Yksittäinen lyhyt toisto lisää täyteläisyyttä ja retrotunnun, kun taas pidemmät toistot suuremmalla takaisinkytkennällä luovat tilavia, laahaavia häntiä. Ping Pong -esiasetus pomppauttaa toistoja vasemman ja oikean korvasi välillä, mikä on hauskaa kuulokkeilla. Pidä märkä sekoitus maltillisena, jotta kaiut tukevat musiikkia peittämisen sijaan.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Wet mix** | Kuinka kovia kaiut ovat verrattuna alkuperäiseen ääneen. Korkeammat arvot saavat toistot erottumaan enemmän. | -2 – +2 (0.6) |
| **Feedback** | Kuinka monta kertaa kaiku toistuu. Korkeammat arvot antavat enemmän toistoja, jotka häipyvät hitaammin. | -1 – +1 (0.5) |
| **Delay** | Kaikujen välinen aika. Lyhyemmät arvot antavat tiiviin slap-backin; pidemmät antavat väljästi sijoitettuja toistoja. | 0.01 – 2 s (0.4) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Slapback** | Yksittäinen, tiivis toisto heti äänen takana. Klassinen rockabilly-slap-back. |
| **Room** | Lyhyt, luonnollinen kaiku, kuin pieni huone. Lisää tilaa tahraamatta ääntä. |
| **Tape** | Lämpimät, keskipitkät toistot, jotka häipyvät vähitellen, kuin vanha nauhaviive. |
| **Dub** | Pitkät, raskaat toistot vahvalla takaisinkytkennällä. Suuri, dub-henkinen ja tilava. |
| **Ping Pong** | Kaiut pomppaavat vasemman ja oikean kaiuttimen välillä leveään stereotehosteeseen. |
| **Long** | Hitaat, väljästi sijoitetut toistot, jotka laahaavat kauas äänen taakse. |

## Chorus (paksumpi, leveämpi ääni)

**Mitä se tekee:** Paksuntaa ja leventää ääntä kerrostamalla siirtyvän kopion alkuperäisen päälle. Valitse esiasetus tai aseta itse märkä/kuiva-sekoitus, syvyys, nopeus ja takaisinkytkentä. Se saa yhden soittimen tai äänen kuulostamaan usealta yhdessä soittavalta lisäämällä hieman epävireisiä, liikkuvia kopioita. Tämä lisää täyteläisyyttä ja lempeää kimallusta. Hienovaraiset asetukset lämmittävät, kun taas voimakkaat asetukset kuulostavat reheviltä ja unenomaisilta. Se on suosittu kitaroilla, koskettimilla ja lauluäänillä.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Wet/Dry** | Kuinka paljon chorusta kuulet verrattuna alkuperäiseen ääneen. Korkeammat arvot tekevät tehosteesta ilmeisemmän. | 0 – 100% (50) |
| **Depth** | Kuinka pitkälle sävelkorkeus horjuu ylös ja alas. Korkeammat arvot antavat paksumman, kimaltelevamman äänen. | 0 – 100% (25) |
| **Rate** | Kuinka nopeasti kimallus liikkuu. Hitaammat tahdit kuulostavat lempeiltä ja reheviltä; nopeammat enemmän vibratolta. | 0 – 10 Hz (1.1) |
| **Feedback** | Kuinka paljon tehostetta kytketään takaisin itseensä. Korkeammat arvot tekevät choruksesta resonoivamman ja voimakkaamman. | -99 – +99% (25) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Subtle** | Lempeä paksunnus, joka lisää lämpöä kiinnittämättä itseensä huomiota. |
| **Lush** | Rikas, klassinen chorus. Loistava yleisasetus kitaroille ja koskettimille. |
| **Ensemble** | Täysi, kerrostunut kimallus, joka saa yhden soittimen kuulostamaan usealta. |
| **Vibrato** | Täysin märkä nopealla tahdilla, huojuvaan vibratoon hienovaraisen choruksen sijaan. |
| **Wide** | Hidas, leveä kimallus, joka avaa stereokuvan. Tilava ja unenomainen. |
| **Twelve-String** | Kirkas, resonoiva kimallus, joka muistuttaa kaksitoistakielistä kitaraa. |

## Säröytys (rosoa ja särmää)

**Mitä se tekee:** Lisää rosoa ja särmää ylikuormittamalla ääntä. Valitse esiasetus tai aseta itse ajo, lähtö ja sävy. Se karhentaa ääntä tarkoituksella, lämpimästä, rosoisesta särmästä rikkinäiseen, fuzz-sävyyn. Se on luova, hauskuuden vuoksi tehty tehoste eikä tapa parantaa laatua, joten käytä sitä pieninä määrinä. Se on hauska elektronisissa, rock- ja kokeellisissa kappaleissa. Laske lähtöä (Output), jos raskas esiasetus tulee liian kovaksi.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Drive** | Kuinka kovaa ääntä säröytetään. Korkeammat arvot ovat rosoisempia ja aggressiivisempia. | 0 – 100% (15) |
| **Output** | Lähdön taso säröytyksen jälkeen. Laske sitä, jos raskas asetus tulee liian kovaksi. | -60 – 0 dB (-18) |
| **Tone** | Vierittää diskantteja pois ennen säröytystä. Matalammat arvot kuulostavat tummemmilta ja lämpimämmiltä. | 100 – 8000 Hz (8000) |
| **Center** | Minkä taajuuden ympärille säröytys keskittyy. Siirtää luonnetta kirkkaammaksi tai tummemmaksi. | 100 – 8000 Hz (2400) |
| **Width** | Kuinka leveä tuo keskitys on. Kapea kuulostaa terävältä ja nenäkkäältä; leveä kuulostaa täyteläiseltä ja avoimelta. | 100 – 8000 Hz (2400) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Warm Drive** | Kevyt, lämmin roso, joka lisää särmää muuttamatta luonnetta paljoakaan. |
| **Crunch** | Klassinen rouskuva overdrive, napakka ja rytminen. |
| **Overdrive** | Kirkas, ajettu sävy runsaalla puraisulla. Loistava soolo-äänille. |
| **Fuzz** | Paksu, kylläinen fuzz. Raskas ja täynnä yläsäveliä. |
| **Metal** | Tiukka, keskialueeseen keskittyvä korkean vahvistuksen sävy aggressiivisiin, raskaisiin ääniin. |
| **Screamer** | Keskialueeseen korostettu overdrive, joka lävistää, kuin putkiscreamer. |
| **LoFi** | Murskattu, kapeakaistainen säröytys rosoiseen lo-fi-luonteeseen. |

## Kierto (pyörivä stereo)

**Mitä se tekee:** Pyörittää ääntä stereokentän ympäri pyörivään, pyörteilevään tehosteeseen. Valitse esiasetus tai aseta itse nopeus. Se liikuttaa ääntä hitaasti vasemman ja oikean kanavasi ympäri, hieman kuin pyörivä kaiutin, mikä lisää pyörteilevän, hypnoottisen tunnun. Hitaat asetukset ovat lempeitä ja leveitä, kun taas nopeat asetukset ovat huimaavia ja ilmeisiä. Se on stereotehoste, joten se on huomattavin kuulokkeilla tai hyvin sijoitetuilla kaiuttimilla.

**Liukusäädin:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Rate** | Kuinka nopeasti ääni pyörii stereokentän ympäri. Negatiiviset arvot pyörittävät toiseen suuntaan; nolla pitää sen paikallaan. | -5 – +5 Hz (1.0) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Slow Pan** | Hidas, lempeä ajautuminen puolelta toiselle. Hienovarainen ja leveä. |
| **Sway** | Tasainen vasen-oikea-keinunta. Lisää lempeää liikettä stereokuvaan. |
| **Rotary** | Keskinopea pyöriminen, joka muistuttaa pyörivää kaiutinta. |
| **Fast Spin** | Nopea pyöriminen stereokentän ympäri huimaavaan, pyörteilevään tehosteeseen. |
| **Reverse** | Keskinopea pyöriminen vastakkaiseen suuntaan. |
| **Whirl** | Erittäin nopea pyöre. Voimakas ja hämmentävä. |

## Ristisyöttö (luonnollinen ääni kuulokkeilla)

Kaiuttimilla kumpikin korvasi kuulee sekä vasemman että oikean kaiuttimen, vain hieman eri aikoina ja voimakkuuksilla. Kuulokkeilla tuo luonnollinen sekoittuminen on poissa: vasen korvasi kuulee vain vasemman kanavan ja oikea korvasi vain oikean. Tämä «superstereo» voi saada musiikin tuntumaan siltä, kuin se olisi jakautunut pääsi sisään, ja kovasti panoroidut nauhoitukset, joissa soitin istuu kokonaan yhdellä puolella, voivat tuntua epäluonnollisilta tai väsyttäviltä pitkillä kuunteluilla.

Ristisyöttö korjaa tämän sekoittamalla pienen, suodatetun määrän kutakin kanavaa toiseen, pienellä viiveellä ja lempeällä korkeiden taajuuksien vaimennuksella. Tämä on lähellä sitä, miten ääni oikeista kaiuttimista saavuttaa molemmat korvasi, mukaan lukien tapa, jolla pääsi hieman varjostaa kauempaa korvaa. Tuloksena on luonnollisempi, kaiuttimenkaltainen kuva, joka istuu hieman edessäsi pääsi sisällä olemisen sijaan, ja se vähentää kuunteluväsymystä pitkillä istunnoilla. Flacbox käyttää tunnettua **bs2b (Bauer stereophonic-to-binaural)** -menetelmää, arvostettua avoimen lähdekoodin ristisyöttöä, jota monet audiofiilisoittimet käyttävät. Voit lukea algoritmista [bs2b-projektisivulta](https://bs2b.sourceforge.net/).

**Cutoff** hallitsee, kuinka lämpimältä sekoitus kuulostaa, ja **Feed level** hallitsee, kuinka vahva se on. Esiasetukset kattavat klassiset bs2b-tasot, tuskin havaittavasta kosketuksesta lujaan, kaiuttimenkaltaiseen sekoitukseen. Ristisyöttö on kuulokkeiden tehoste, joten jätä se pois päältä, kun kuuntelet kaiuttimilla.

**Liukusäätimet:**

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Cutoff** | Asettaa, missä kanavien välinen vuoto alkaa vaimentua. Matalammat arvot antavat lämpimämmän, korostetumman tehosteen. | 300 – 2000 Hz (700) |
| **Feed level** | Hallitsee, kuinka paljon yksi kanava vuotaa toiseen. Korkeammat arvot tuottavat kaiuttimenkaltaisemman äänen. | 1 – 15 dB (4.5) |

**Esiasetukset:**

| Esiasetus | Mitä se tekee |
|---|---|
| **Subtle** | Tuskin havaittava ristisyöttö rentoon kuunteluun. Pehmentää kovasti panoroitua stereoa muuttamatta sävytasapainoa. |
| **Chu Moy** | Klassinen yleiskäyttöinen oletus. Tasapainoinen ja kevyesti lämmin, se toimii lähes millä tahansa materiaalilla. Aloita tästä. |
| **Strong** | Vahvempi vuoto kovemmin panoroiduille miksauksille. Ilmeisempi stereon kaventuminen. |
| **Jan Meier** | Suosittu kuulokeharrastajien keskuudessa. Leveämpi syöttö, kaiuttimenkaltaisempi esitys, pieni basson nosto. |
| **Speaker-like** | Viritetty luonnollisimpaan kaiutintyyliseen toistoon kuulokkeilla. |
| **Vintage Stereo** | Aggressiivinen ristisyöttö, joka on viritetty 1960- ja 1970-lukujen miksauksille kovasti panoroiduilla rummuilla ja lauluäänillä. |

## Signaalinkäsittely: rakenna oma DSP-ketjusi

Valmiiden tehosteiden lisäksi Flacbox antaa sinun rakentaa oman ketjusi kohdassa **Asetukset > Äänisoitin > Signaalinkäsittely**. Kuten sovellus selittää, kun ketju on tyhjä: *«Napauta + lisätäksesi tehosteen. Kytke jokainen päälle tai pois sen kytkimellä, vedä järjestääksesi uudelleen, napauta muokataksesi sen parametreja ja paina pitkään monistaaksesi tai poistaaksesi.»*

**Järjestyksellä on väliä**: suodatin ennen säröytystä kuulostaa erilaiselta kuin sama suodatin sen jälkeen. Voit myös kohdistaa koko ketjun kohteeseen **Kaikki kanavat**, **Vasen kanava** tai **Oikea kanava**.

Alla on jokainen lohko sovelluksen omalla tekstillä kutakin liukusäädintä ja kutakin esiasetusta varten.

### Gain (tason säätö)

Nostaa tai laskee tasoa yhdessä kohdassa ketjua.

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Gain** | Korostaa tai leikkaa tasoa tässä kohdassa ketjua. Käytä sitä täyttääksesi tasoa muiden tehosteiden jälkeen tai ajaaksesi seuraavia. | -24 – +24 dB (0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Unity** | Ei muutosta tasossa. Neutraali lähtökohta. |
| **Cut** | Suuri leikkaus. Kesyttää kovan lähteen tai tekee tilaa ennen seuraavia tehosteita. |
| **Trim** | Lempeä leikkaus vetämään tasoa hieman taakse. |
| **Lift** | Vaatimaton korostus tuomaan hiljainen lähde ylös. |
| **Boost** | Vahva korostus hiljaiselle materiaalille tai ajaaksesi seuraavia tehosteita kovempaa. |
| **Max** | Maksimikorostus. Kova, varo leikkautumista myöhemmin ketjussa. |

### Low Pass (poistaa diskantit)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Cutoff** | Asettaa, missä suodatin alkaa vaimentaa diskantteja. Laske sitä tummentaaksesi ja pehmentääksesi ääntä; nosta huipulle avataksesi täysin. | 20 Hz – 20 kHz (20 kHz) |
| **Resonance** | Korostaa taajuuksia juuri raja-arvon kohdalla. Pidä matalana puhtaaseen vaimennukseen; nosta piikikkääseen, vinkuvaan särmään. | 0.1 – 10 (0.707) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Air** | Leikkaa vain aivan yläpään. Ottaa hieman särmää pois tylsistämättä ääntä. |
| **Warm** | Lempeä diskanttien vaimennus lämpimämpään, pyöreämpään sävyyn. |
| **Mellow** | Huomattavasti pehmennetty. Vetää kirkkautta taakse rentoon tuntuun. |
| **Muffled** | Tumma ja vaimennettu, kuin seinän läpi kuultuna. |
| **Telephone** | Kapea, resonoiva piikki alhaalla alueella. Ohut, puhelimenkaltainen ääni. |

### High Pass (poistaa basson)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Cutoff** | Asettaa, missä suodatin alkaa vaimentaa bassoa. Nosta ohentaaksesi matalaa päätä ja poistaaksesi jyrinän; laske pohjalle avataksesi täysin. | 20 Hz – 20 kHz (20 Hz) |
| **Resonance** | Korostaa taajuuksia juuri raja-arvon kohdalla. Pidä matalana puhtaaseen vaimennukseen; nosta piikikkääseen, vinkuvaan särmään. | 0.1 – 10 (0.707) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Rumble Cut** | Poistaa infraäänijyrinän ja DC-poikkeaman koskematta kuuluvaan matalaan päähän. |
| **Tighten** | Leikkaa jyrisevät matalat taajuudet tiukempaan, puhtaampaan bassoon. |
| **Thin** | Leikkaa lämmön ja täyteläisyyden jättäen kevyemmän, ohuemman äänen. |
| **Radio** | Vain keskitaajuudet ja diskantit jäävät, kuin pieni radiokaiutin. |
| **Telephone** | Kapea, resonoiva piikki ylhäällä alueella. Ohut, puhelimenkaltainen ääni. |

### Band Pass (säilyttää keskikaistan)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Center** | Asettaa taajuuden, jonka suodatin päästää läpi. Kaikki sen ylä- ja alapuolella vaimennetaan. Pyyhkäise poimiaksesi bassoa, keskitaajuuksia tai diskantteja. | 20 Hz – 20 kHz (1 kHz) |
| **Resonance** | Hallitsee, kuinka leveä kaista on. Matalat arvot päästävät laajan alueen läpi; nosta kaventaaksesi keskukseen terävään, resonoivaan sävyyn. | 0.1 – 10 (0.707) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Voice** | Leveä kaista keskialueen ympärillä, jossa useimmat lauluäänet istuvat. Neutraali lähtökohta. |
| **Bass** | Eristää matalan pään jättäen vain basson ja bassorummun. |
| **Body** | Keskittyy ala-keskialueeseen lämpimään, laatikkomaiseen täyteläisyyteen. |
| **Presence** | Nostaa ylä-keskitaajuuksia selkeyteen ja läsnäoloon. |
| **Telephone** | Kapea keskialueen kaista. Ohut, puhelimenkaltainen ääni. |
| **Wah** | Erittäin kapea, resonoiva piikki. Pyyhkäise keskusta wah-tehosteeseen. |

### Notch (poistaa yhden kapean kaistan)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Frequency** | Asettaa taajuuden, jonka suodatin poistaa. Kaikki sen ylä- ja alapuolella pääsee läpi. Viritä huminan tai resonanssin päälle leikataksesi sen pois. | 20 Hz – 20 kHz (60 Hz) |
| **Resonance** | Hallitsee, kuinka leveä leikkaus on. Matalat arvot kaivavat laajan alueen; nosta poistaaksesi vain pistemäisen kaistan ja jättääksesi loput koskemattomaksi. | 0.1 – 10 (8.0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Mains Hum 60** | Poistaa 60 Hz:n sähköhuminan (Pohjois-Amerikan verkkovirta). Neutraali lähtökohta. |
| **Mains Hum 50** | Poistaa 50 Hz:n sähköhuminan (Euroopan ja muun verkkovirta). |
| **Rumble** | Leikkaa matalataajuisen jyrinän tai resonanssin ohentamatta koko pohjaa. |
| **Mud** | Kaivaa ala-keskialueen samennuksen puhtaampaan, selkeämpään ääneen. |
| **Boxy** | Poistaa laatikkomaisen keskialueen töräyksen. |
| **Harsh** | Kesyttää karkean, lävistävän piikin ylä-keskitaajuuksissa. |

### Peaking (parametrinen EQ-kaista)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Frequency** | Korostettavan tai leikattavan kaistan keskus. Pyyhkäise löytääksesi muokattavan taajuuden. | 20 Hz – 20 kHz (1 kHz) |
| **Gain** | Kuinka paljon korostaa tai leikata keskuksessa. Positiivinen nostaa kaistaa; negatiivinen kaivaa sen. | -15 – +15 dB (0) |
| **Q factor** | Asettaa, kuinka leveä kaista on. Matalat arvot muokkaavat laajaa aluetta; korkeat kaventavat kirurgisiin, pistemäisiin muutoksiin. | 0.1 – 10 (1.0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Presence** | Leveä ylä-keskialueen nosto selkeyteen ja läsnäoloon. Neutraali lähtökohta. |
| **Warmth** | Leveä ala-keskialueen korostus, joka lisää täyteläisyyttä ja lämpöä. |
| **Vocal Boost** | Nostaa lauluäänen ydinaluetta tuodakseen äänet esiin. |
| **Cut Mud** | Kaivaa laatikkomaisen ala-keskialueen samennuksen puhtaampaan ääneen. |
| **Tame Harsh** | Kapea leikkaus kesyttämään karkean, lävistävän piikin. |
| **Punch** | Matala korostus, joka lisää potkua ja iskua matalaan päähän. |
| **Sub Boost** | Syvä korostus aivan pohjalla ylimääräiseen alabasson painoon. |
| **Air** | Leveä nosto huipulla avoimeen, ilmavaan kiiltoon. |
| **Clarity** | Nostaa ylä-keskitaajuuksia lisätäkseen määrittelyä ja särmää. |
| **De-Ess** | Kapea leikkaus sihinäalueella kesyttämään karkeat S-äänet. |
| **De-Boom** | Leikkaa jyrisevän matalataajuisen kertymän tiukempaan matalaan päähän. |
| **Scoop** | Leveä keskialueen kuoppa kuopatun, modernin sävyn saamiseksi. |

### Low Shelf (basson hallinta ja basson korostus)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Frequency** | Asettaa kulmataajuuden, jonka alapuolella hylly vaikuttaa. Kaikki sen alla korostetaan tai leikataan yhdessä. | 20 – 2000 Hz (200) |
| **Gain** | Kuinka paljon nostaa tai laskea matalaa päätä. Positiivinen lisää painoa ja lämpöä; negatiivinen ohentaa sitä. | -15 – +15 dB (0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Warmth** | Lempeä matalan pään nosto lämpöön ja täyteläisyyteen. Neutraali lähtökohta. |
| **Bass Boost** | Kiinteä korostus bassoon painon ja potkun saamiseksi. |
| **Fullness** | Täyttää ala-keskitaajuudet täyteläisempään, pyöreämpään ääneen. |
| **Trim Bass** | Vaatimaton leikkaus keventämään bassopainotteista miksausta. |
| **Cut Lows** | Vahva leikkaus ohentamaan tai de-boomaamaan matalaa päätä. |
| **Big Bottom** | Suuri matalan pään korostus maksimaaliseen painoon ja jyrinään. |

### High Shelf (diskantin hallinta)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Frequency** | Asettaa kulmataajuuden, jonka yläpuolella hylly vaikuttaa. Kaikki sen yllä korostetaan tai leikataan yhdessä. | 1 – 20 kHz (8 kHz) |
| **Gain** | Kuinka paljon nostaa tai laskea korkeaa päätä. Positiivinen lisää kirkkautta ja ilmavuutta; negatiivinen tasoittaa ja tummentaa. | -15 – +15 dB (0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Presence** | Lempeä korkean pään nosto selkeyteen ja yksityiskohtiin. Neutraali lähtökohta. |
| **Air** | Avaa aivan yläpään ilmavaan, avoimeen ääneen. |
| **Bright** | Vahva korostus terävään, kirkkaaseen, eteen tuotuun sävyyn. |
| **Soften** | Vaatimaton leikkaus ottamaan särmää pois karkeista diskanteista. |
| **Tame Highs** | Vahva leikkaus tummentamaan ja tasoittamaan liian kirkasta ääntä. |
| **Sparkle** | Suuri yläpään korostus maksimaaliseen kimallukseen. |

### Soft Clip (lämmin kyllästys)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Drive** | Työntää signaalia kovempaa aaltomuotoiluun. Pienet määrät lisäävät lempeää lämpöä; suuret määrät pyöristävät huiput paksuun kyllästykseen ja rosoon. | 0 – 40 dB (0) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Warm** | Ripaus ajoa lempeään, analogityyliseen lämpöön. |
| **Drive** | Huomattava kyllästys, joka paksuntaa ja värittää ääntä. |
| **Crunch** | Raskas ajo kuuluvalla rouskuvalla särmällä. |
| **Fuzz** | Paksu, fuzz-henkinen säröytys. Huiput litistetään kovaa. |
| **Destroy** | Maksimaalinen ajo. Aggressiivinen, täysin kyllästetty roso. |

### Bit Crusher (retro lo-fi)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Bit depth** | Asettaa, kuinka monta bittiä kuvaa kutakin näytettä. Vähemmän bittejä tarkoittaa karkeampia askeleita ja enemmän kvantisointikohinaa, rouskuvaan, rosoiseen digitaaliseen ääneen. | 1 – 16 bittiä (16) |
| **Sample rate** | Alinäytteistää äänen. Sadalla prosentilla taajuus on koskematon; laske sitä pitääksesi kutakin näytettä pidempään, tylsistäen diskantteja ja lisäten karkean, laskostuneen särmän. | 1% – 100% (100%) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Vintage** | Hienovarainen laadun pudotus, kuin varhainen digitaalinen sampleri. |
| **LoFi** | Klassinen 8-bittinen, puolinopeuksinen lo-fi. Rakeinen ja retro. |
| **Crunch** | Raskaampi murskaus kuuluvalla rouskuvalla särmällä. |
| **Gritty** | Karkea ja rosoinen. Tasojen väliset askeleet ovat ilmeisiä. |
| **Destroy** | Äärimmäinen vähennys. Karkea, rikkinäinen, tuskin tunnistettava. |

### Ring Modulator (metalliset ja robottimaiset sävyt)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Carrier** | Asettaa sävelen taajuuden, jolla signaali kerrotaan. Muutama hertsi antaa tremolohuojunnan; korkeammat taajuudet lisäävät metallisia, kellomaisia ja robottimaisia yläsäveliä. | 1 – 4000 Hz (440) |
| **Mix** | Sekoittaa moduloidun äänen alkuperäiseen. Nollalla prosentilla kuulet vain kuivan signaalin; sadalla prosentilla vain täysin moduloidun sävelen. | 0% – 100% (0%) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Tremolo** | Erittäin matala kantoaalto muuttaa sen amplituditremoloksi, huojuttaen äänenvoimakkuutta. |
| **Robot** | Keskitason kantoaalto lisää kilahtavia yläsäveliä klassiseen robottiäänitehosteeseen. |
| **Metallic** | Tiheät, epäharmoniset yläsävelet karkeaan, metalliseen sävyyn. |
| **Bell** | Korkeampi kantoaalto antaa kirkkaan, kellomaisen soinnin. |
| **Alien** | Täysin märkä korkealla kantoaallolla. Äärimmäinen, avaruusolentomainen, tuskin tunnistettava. |

### Tremolo (äänenvoimakkuuden huojunta)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Rate** | Asettaa, kuinka nopeasti äänenvoimakkuus sykkii. Hitaammat tahdit antavat pehmeän keinunnan; nopeammat antavat nopean nykimisen. | 0.1 – 20 Hz (5) |
| **Depth** | Asettaa, kuinka paljon äänenvoimakkuus laskee kussakin sykähdyksessä. Nollalla prosentilla taso on tasainen; sadalla prosentilla se laskee aina hiljaisuuteen asti. | 0% – 100% (0%) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Gentle** | Hidas, matala keinunta. Hienovarainen liike kiinnittämättä huomiota. |
| **Classic** | Klassinen vahvistimen tremolo: keskitason tahti ja kohtuullinen syvyys. |
| **Deep** | Vahva, syvä sykähdys, joka laskee lähes hiljaisuuteen joka syklissä. |
| **Fast** | Nopea lepatus kimaltelevaan, hermostuneeseen tuntuun. |
| **Chop** | Nopea ja täysi syvyys. Kova, nykivä katkonta. |

### Delay (kaiku)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Time** | Asettaa tauon ennen kutakin kaikua. Lyhyet ajat antavat tiiviin slapbackin; pidemmät ajat välittävät toistot kauemmas toisistaan. | 0.01 – 2 s (0.25) |
| **Feedback** | Asettaa, kuinka paljon kutakin kaikua kytketään takaisin. Matalat arvot antavat yksittäisen toiston; korkeammat arvot rakentavat pitkän, laahaavan kaikusarjan. | 0 – 0.95 (0.4) |
| **Mix** | Sekoittaa kaiut alkuperäiseen. Nollalla prosentilla kuulet vain kuivan signaalin; sadalla prosentilla vain kaiut. | 0% – 100% (0%) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Slapback** | Yksittäinen lyhyt kaiku, tiiviisti alkuperäistä vasten. Rockabilly ja lauluäänen kahdennus. |
| **Echo** | Klassinen kaiku: selkeä toisto muutamalla laahaavalla hännällä. |
| **Ping** | Nopea, pomppaava toisto, joka lisää rytmistä liikettä. |
| **Ambient** | Pidemmät, pehmeämmät toistot, jotka huuhtoutuvat tilavaan häntään. |
| **Dub** | Korkea takaisinkytkentä pitkiin, dub-henkisiin kaikuvyöryihin. |
| **Cavern** | Pitkät, syvät toistot, kuin ääni kaikuisi valtavan tilan läpi. |

### Stereo Width (kavenna tai leventä)

| Säädin | Mitä se tekee | Alue (oletus) |
|---|---|---|
| **Width** | Kaventaa tai leventää stereokuvaa. Nolla prosenttia romahtaa monoksi, sata prosenttia jättää sen koskemattomaksi ja korkeammat arvot työntävät sivuja leveämmälle. Vaikuttaa vain stereokappaleisiin Kaikki kanavat -kohteella. | 0% – 200% (100%) |

| Esiasetus | Mitä se tekee |
|---|---|
| **Wide** | Lempeä leventäminen, joka avaa stereokuvan. Neutraali lähtökohta. |
| **Wider** | Vahvempi levitys suureen, mukaansatempaavaan stereokenttään. |
| **Max** | Maksimileveys. Erittäin leveä, mutta varo mono-yhteensopivuusongelmia. |
| **Narrow** | Vetää sivut sisään tiukempaan, keskitetympään kuvaan. |
| **Focused** | Lähes keskitetty, vain vihjeellä stereota. |
| **Mono** | Täysin romahtanut monoksi. Molemmat kaiuttimet toistavat saman signaalin. |

## Kuinka kaikki toimii konepellin alla (yksinkertainen versio)

- **Moottorit:** valitset yhden kohdasta Asetukset > Äänisoitin > Toistomoottori: **Standard** (järjestelmä), **Universal** (FFmpeg) tai **Sound FX** (**BASS™-moottori** [Un4seen Developmentsilta](https://www.un4seen.com/)). Valitsemasi moottori määrää, mitkä formaatit toistuvat, ja tehosteet, taajuuskorjain sekä DSP-ketju toimivat vain Sound FX -moottorissa.
- **Formaatit:** BASS™-moottori lisää FLAC:n, DSD:n, WavPackin, APE:n, Musepackin, TrueAudion, Opuksen ja moduuli- (tracker-) musiikin järjestelmä- ja FFmpeg-formaattien päälle.
- **Tehosteet:** taajuuskorjain, kompressori ja useimmat tehosteet käyttävät BASS™-tehostelisäosia. Freeverb on Freeverb-kaiku. Chorus, Flanger ja säröytys käyttävät klassisia DirectX-tyylisiä tehosteita omine säätimineen.
- **Äänenvoimakkuuden normalisointi:** reaaliaikainen **EBU R128** -äänekkyyden tasaaja (lähetys- ja suoratoistokäytössä käytetty äänekkyysstandardi).
- **Ristisyöttö:** **bs2b (Bauer)** -ristisyöttö, ajettuna BASS™-moottorin sisällä.
- **DSP-ketju:** mukautetut lohkosi, sovellettuna tarkalleen asettamassasi järjestyksessä, kaikilla kanavilla tai vain yhdellä puolella.
- **Lähtö:** voit asettaa näytteenottotaajuuden, kanavamäärän ja puskurin koon vastaamaan laitteitasi.

Koska kaikki tämä ajetaan reaaliajassa musiikin soidessa, tehosteet:

- Toimivat **reaaliajassa** kaikessa, mukaan lukien pilvitiedostot, suoratoistot ja moduulimusiikki.
- **Eivät koskaan muuta tai tallenna uudelleen** tiedostojasi. Kytke tehoste pois päältä, ja alkuperäinen palaa.
- **Muistavat asetuksesi** jokaiselle tehosteelle.
- Voidaan **sekoittaa ja yhdistellä** vapaasti, koska jokainen on erillinen.

## Yksinkertaisia reseptejä kokeiltavaksi

**Jokapäiväinen kuuntelu**

- **Enemmän bassoa, puhtaasti:** Taajuuskorjain > Bass Booster, ja laske sitten esivahvistinta 1–2 dB. Tai lisää DSP Low Shelf Bass Boostilla.
- **Tasainen äänenvoimakkuus sekasoittolistalla:** Äänenvoimakkuuden normalisointi > Standard, plus Kompressori > Soft.
- **Lempeä yleiskiillotus:** Kompressori > Transparent, plus Äänenvoimakkuuden normalisointi > Light.
- **Selkeämmät lauluäänet:** Taajuuskorjain > Vocal Booster, tai DSP Peaking -lohko Vocal Boostilla.
- **Täyteläisempi ääni pienillä puhelimen kaiuttimilla:** Taajuuskorjain > Small Speakers.

**Kuulokkeet**

- **Miellyttävämpi, vähemmän väsyttävä kuulokkeilla:** Ristisyöttö > Chu Moy tai Jan Meier.
- **Leveämpi ääni kuulokkeilla:** DSP Stereo Width > Wide, plus Ristisyöttö > Chu Moy.
- **Korjaa kovasti panoroidut 1960- ja 1970-lukujen levyt:** Ristisyöttö > Vintage Stereo.
- **Hieman ilmaa ja tilaa:** Freeverb > Ambience, pidettynä matalana, plus Ristisyöttö > Subtle.

**Hiljaiset hetket ja puheääni**

- **Myöhäisillan hiljainen kuuntelu:** Äänenvoimakkuuden normalisointi > Night, plus Kompressori > Late Night.
- **Podcastit ja äänikirjat:** Kompressori > Voice / Podcast, plus Taajuuskorjain > Spoken Word.
- **Kovin, tasaisin ääni meluisassa autossa:** Äänenvoimakkuuden normalisointi > Strong, plus Kompressori > Heavy.

**Ongelmien korjaaminen**

- **Kesytä karkea, kirkas nauhoitus:** Taajuuskorjain > Treble Reducer, tai DSP Peaking -lohko Tame Harshilla.
- **Poista sähköhumina:** DSP-ketju > Notch > Mains Hum 60 (tai Mains Hum 50 Euroopassa).
- **Tiukempi, puhtaampi basso:** DSP High Pass > Tighten, leikataksesi jyrisevän matalan pään.
- **Vähemmän jyrinää bassopainotteisessa miksauksessa:** DSP Low Shelf > Trim Bass, tai Peaking > De-Boom.

**Luova ja hauska**

- **Lämmin, tilava tuntu:** Freeverb > Hall, pidettynä matalana.
- **Unenomaiset, tilavat kitarat:** Chorus > Wide, plus Kaiku > Long.
- **Retro lo-fi:** DSP-ketju > Bit Crusher (LoFi) Soft Clipiin (Warm).
- **Funkahtavaa liikettä elektronisiin kappaleisiin:** Auto Wah > Funky, tai Phaser > Fast.
- **Klassinen suihkukoneen pyyhkäisy:** Flanger > Jet.

## UKK

{{% details title="Mitä äänimoottoria Flacbox käyttää?" closed="true" %}}
Valitset yhden toistomoottorin kohdasta Asetukset > Äänisoitin: Standard (Applen järjestelmämoottori), Universal (FFmpeg-moottori) tai Sound FX (BASS™-moottori Un4seen Developmentsilta, un4seen.com). Valitsemasi moottori määrää, mitkä tiedostomuodot toistuvat. Sound FX on se, joka toistaa lisäformaatteja kuten FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus sekä MOD- tai trackermusiikkia, ja se on ainoa moottori, joka tarjoaa reaaliaikaiset tehosteet, 10-kaistaisen taajuuskorjaimen ja DSP-ketjun. Käyttääksesi tehosteita, aseta toistomoottoriksi Sound FX.
{{% /details %}}

{{% details title="Voiko Flacbox toistaa MOD-, XM-, IT- ja muuta tracker- tai moduulimusiikkia?" closed="true" %}}
Kyllä. BASS™-moottorissa on sisäänrakennettu moduulisoitin, joka lataa MOD-, XM-, IT-, S3M-, MTM-, UMX- ja MO3-tiedostoja ja rakentaa kappaleen reaaliajassa uudelleen sen kuvioista ja soitinäänistä, sillä tavalla kuin trackermusiikki on tarkoitettu soitettavaksi. Tavalliset iPhone-soittimet eivät osaa tätä. Tehosteet ja taajuuskorjain toimivat myös moduulimusiikissa.
{{% /details %}}

{{% details title="Tukeeko Flacbox DSD:tä ja korkearesoluutioisia tiedostoja?" closed="true" %}}
Kyllä. Flacbox toistaa DSD-tiedostoja (DSF ja DFF) BASS™-moottorin kautta käyttäen DSD over PCM -menetelmää, jotta ne toimivat tavallisella lähtölaitteistolla, sekä FLAC:n, WavPackin, Monkey's Audion (APE), Musepackin ja TrueAudion häviöttömään toistoon.
{{% /details %}}

{{% details title="Mitä äänitehosteita Flacboxissa on?" closed="true" %}}
10-kaistainen taajuuskorjain, äänenvoimakkuuden normalisointi, kompressori, Freeverb, Auto Wah, Phaser, Flanger, kaiku, Chorus, säröytys, kierto ja ristisyöttö, sekä itse rakennettava DSP-ketju suodattimilla, hyllyillä, vahvistuksella, soft clipillä, bit crusherilla, ring modulatorilla, tremololla, viiveellä ja stereoleveydellä. Jokainen on erillinen ja voidaan yhdistää muihin.
{{% /details %}}

{{% details title="Mikä on esiasetus?" closed="true" %}}
Esiasetus on valmis asetus tehosteelle. Sen sijaan, että liikuttaisit liukusäätimiä itse, napautat esiasetusta ja ääni muuttuu vastaamaan. Jokaisella Flacboxin tehosteella on useita esiasetuksia, ja tässä oppaassa luetellaan, mitä kukin tekee. Jos liikutat liukusäädintä esiasetuksen valinnan jälkeen, tehoste näyttää «Manual» kertoakseen, että se käyttää nyt omia arvojasi.
{{% /details %}}

{{% details title="Kuinka avaan äänitehosteet Flacboxissa?" closed="true" %}}
Avaa Nyt soi -soitin, napauta ⋯ (Lisää) -painiketta ja valitse Äänitehosteet. Tai mene kohtaan Asetukset > Äänisoitin > Äänitehosteet. Napauta tehostetta, kytke sen kytkin päälle ja valitse esiasetus, tai avaa liukusäätimet hienosäätöön.
{{% /details %}}

{{% details title="Missä taajuuskorjain on, ja mitkä ovat parhaat asetukset?" closed="true" %}}
Mene kohtaan Asetukset > Äänisoitin > Äänen taajuuskorjain. Siinä on 10 kaistaa 32 Hz:stä 16 kHz:iin, jokainen väliltä -12 ja +12 dB, sekä -24 – +24 dB esivahvistin ja 22 esiasetusta. Enemmän bassoa: käytä Bass Boosteria. Selkeämmät äänet: käytä Vocal Boosteria tai Popia. Kirkkaampi ääni: käytä Treble Boosteria. Säädä sitten yksittäisiä kaistoja maun mukaan.
{{% /details %}}

{{% details title="Kuinka korostan bassoa Flacboxissa?" closed="true" %}}
Kaksi helppoa tapaa. Äänen taajuuskorjaimessa valitse Bass Booster (tai nosta 32 Hz:n ja 64 Hz:n kaistoja muutama dB). Tai Signaalinkäsittelyssä lisää Low Shelf -lohko asetettuna Bass Boostiin. Kummassakin tapauksessa laske esivahvistinta tai lisää Gain-lohko 1–2 dB, jotta basso pysyy puhtaana eikä säröydy.
{{% /details %}}

{{% details title="Mikä taajuuskorjaimen esiasetus on paras musiikilleni?" closed="true" %}}
Rock ja Electronic lisäävät energiaa vahvoilla matalilla ja diskanteilla. Acoustic, Jazz ja Classical pysyvät lämpiminä ja luonnollisina. Pop ja Vocal Booster tuovat äänet esiin. Bass Booster ja Hip-Hop lisäävät painoa. Deep ja Loudness kuulostavat täyteläisemmiltä matalalla äänenvoimakkuudella. Aloita genreesi sopivalla, ja hienosäädä sitten.
{{% /details %}}

{{% details title="Mikä on äänenvoimakkuuden normalisointi, ja miten se eroaa ReplayGainista?" closed="true" %}}
Se saa jokaisen kappaleen soimaan suunnilleen samalla äänekkyydellä. Se mittaa todellisen äänekkyyden käyttäen EBU R128 -standardia (LUFS-yksikössä, kuten suoratoistopalvelut) ja säätää jokaisen kappaleen kohti tavoitettasi max-boost-rajalla. Toisin kuin ReplayGain, se ei tarvitse tunnisteita tiedostoihisi ja toimii missä tahansa lähteessä, reaaliajassa, muuttamatta ääntä. Esiasetukset: Light, Standard, Strong ja Night.
{{% /details %}}

{{% details title="Mikä on ristisyöttö, ja pitäisikö minun käyttää sitä?" closed="true" %}}
Ristisyöttö sekoittaa hieman vasenta ja oikeaa kanavaa yhteen, jotta kuulokkeet tuntuvat enemmän oikeilta kaiuttimilta ja vähemmän siltä, että ääni on jumissa pääsi sisällä. Se on vain kuulokkeille, joten kytke se pois kaiuttimilta. Flacbox käyttää bs2b (Bauer) -menetelmää esiasetuksilla kuten Chu Moy ja Jan Meier.
{{% /details %}}

{{% details title="Mikä on kompressorin ja äänenvoimakkuuden normalisoinnin ero?" closed="true" %}}
Äänenvoimakkuuden normalisointi sovittaa äänekkyyttä eri kappaleiden välillä. Kompressori tasoittaa kovat ja hiljaiset osat yhden kappaleen sisällä. Ne ratkaisevat eri ongelmia ja toimivat hyvin yhdessä, erityisesti autossa tai meluisassa paikassa.
{{% /details %}}

{{% details title="Mikä on Signaalinkäsittely (DSP) -ketju?" closed="true" %}}
Se on itse rakennettava telakka kohdassa Asetukset > Äänisoitin > Signaalinkäsittely. Lisää lohkoja kuten suodattimet, hyllyt, vahvistus, soft clip, bit crusher, ring modulator, tremolo, viive ja stereoleveys, laita ne mihin tahansa järjestykseen, kytke jokainen päälle tai pois ja kohdista ketju kaikkiin kanaviin, vasempaan tai oikeaan. Koska järjestyksellä on väliä, voit suunnitella tarkalleen haluamasi äänen.
{{% /details %}}

{{% details title="Mikä on taajuuskorjaimen, tehosteiden ja DSP-ketjun ero?" closed="true" %}}
Taajuuskorjain on yksinkertainen 10-kaistainen sävynsäätö. Äänitehosteet ovat valmiita työkaluja (kompressori, kaiku, viivekaiku ja niin edelleen) esiasetuksineen. DSP-ketju on paikka, jossa rakennat oman tehostejärjestyksesi yksittäisistä lohkoista. Voit ajaa kaikkia kolmea samanaikaisesti.
{{% /details %}}

{{% details title="Muuttavatko tai vahingoittavatko tehosteet musiikkitiedostojani?" closed="true" %}}
Ei. Kaikki sovelletaan reaaliajassa musiikin soidessa. Tiedostojasi ei koskaan muuteta tai tallenneta uudelleen. Kytke tehoste pois päältä, ja alkuperäinen ääni palaa heti.
{{% /details %}}

{{% details title="Voinko käyttää useampaa kuin yhtä tehostetta samanaikaisesti?" closed="true" %}}
Kyllä. Jokaisella tehosteella on oma kytkin eikä pääkytkintä ole, joten mikä tahansa yhdistelmä toimii. Esimerkiksi äänenvoimakkuuden normalisointi plus kompressori tasaiseen kuunteluun, tai Freeverb plus ristisyöttö kuulokkeilla, taajuuskorjain päällä.
{{% /details %}}

{{% details title="Miksi tehosteen säätimet ovat harmaana?" closed="true" %}}
Tehoste on kytketty pois päältä. Kytke sen kytkin päälle muokkaimen yläreunassa käyttääksesi säätimiä. Jokainen tehoste on oletuksena pois päältä.
{{% /details %}}

{{% details title="Mitä Manual-merkintä tarkoittaa?" closed="true" %}}
Se tarkoittaa, että liikutit liukusäädintä pois esiasetuksesta, joten tehoste käyttää nyt omia mukautettuja arvojasi nimetyn esiasetuksen sijaan. Jokaisella liukusäätimellä on nollauspainike, ja esiasetuksen valitseminen uudelleen korvaa manuaaliset arvosi.
{{% /details %}}

{{% details title="Voinko tallentaa ja jakaa taajuuskorjaimen esiasetuksiani?" closed="true" %}}
Kyllä. 22 sisäänrakennetun esiasetuksen lisäksi voit tehdä omia, järjestää niitä uudelleen ja viedä tai tuoda niitä siirtääksesi asetuksesi toiseen laitteeseen.
{{% /details %}}

{{% details title="Toimivatko tehosteet CarPlayn, suoratoiston ja taustatoiston kanssa?" closed="true" %}}
Kyllä. Tehosteet ajetaan BASS™-moottorin sisällä, joten ne pätevät paikallisiin tiedostoihin, pilviasemiin, mediapalvelimiin, suoratoistoihin ja moduulimusiikkiin, ja ne jatkavat toimintaansa CarPlayn ja taustatoiston aikana.
{{% /details %}}

{{% details title="Voinko muuttaa äänen lähtölaatua?" closed="true" %}}
Kyllä. Kohdassa Asetukset > Äänisoitin voit asettaa lähdön näytteenottotaajuuden, kanavien määrän ja puskurin koon vastaamaan kuulokkeitasi, kaiuttimiasi tai DAC:tasi.
{{% /details %}}

{{% details title="Mikä on hyvä aloitusasetus kuulokkeille?" closed="true" %}}
Kytke päälle äänenvoimakkuuden normalisointi (Standard), lisää kevyt kompressori (Soft), valitse pitämäsi taajuuskorjaimen esiasetus ja kytke päälle ristisyöttö (Chu Moy tai Jan Meier). Jätä kaiku, kaiku ja säröytys pois päältä, ellet halua luovaa ääntä.
{{% /details %}}

---

*BASS on Un4seen Developments Ltd:n tavaramerkki. Katso [un4seen.com](https://www.un4seen.com/). Ristisyöttö käyttää bs2b (Bauer stereophonic-to-binaural) -algoritmia; katso [bs2b-projektisivu](https://bs2b.sourceforge.net/).*
