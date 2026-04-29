---
title: "Kuinka viedä kappalekokoelma M3U-, CSV- ja TXT-muotoon Evermusicissa ja Flacboxissa"
date: 2024-01-31
description: "Opi viemään äskettäin kuunnellut, suosikit, soittolistat ja albumit Evermusicista ja Flacboxista M3U-, CSV- tai TXT-muotoon. Täydellinen Last.fm-scrobbaukseen ja toistoon muilla laitteilla."
keywords: ["evermusic vienti", "flacbox vienti", "vie m3u-muotoon", "vie soittolista csv-muotoon", "m3u txt csv soittolista", "musiikin vienti"]
tags: ["evermusic", "äskettäin", "suosikit", "vienti", "m3u", "soittolista", "csv", "txt", "albumi"]
---

{{< author-byline >}}


**Lyhyesti:** Evermusic ja Flacbox mahdollistavat minkä tahansa kappalekokoelman (Äskettäin, Suosikit, soittolistat, albumit) viemisen CSV-, TXT- tai M3U-tiedostoihin. Käytä näitä vientejä scrobbataksesi Last.fm:ään, varmuuskopioidaksesi kirjastosi tai toistaaksesi soittolistojasi muilla laitteilla.

## Johdanto

Äskettäin kuunneltujen, suosikkien, albumien ja soittolistojen vieminen sovelluksesta ulkoiseen tiedostoon voi olla erittäin hyödyllistä. Voit käyttää näitä tiedostoja kuunteluhistoriasi päivittämiseen scrobbler-palveluissa kuten [Last.fm](http://Last.fm) tai kuunnella soittolistojasi ulkoisilla laitteilla. Evermusicin ja Flacboxin avulla tämä prosessi on helppoa. Näytämme tässä, kuinka viet äskettäin kuunnellut CSV/TXT-muotoon ja soittolistasi M3U-muotoon. Tämä toiminto on kuitenkin käytettävissä mille tahansa kappalekokoelmalle sovelluksessa.

## Valitse muoto

Viedäksesi äskettäin kuunnellut avaa 'Musiikkikirjasto'-osio ja valitse 'Äskettäin'-valikosta.

![musiikkikirjasto](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Seuraavalla näytöllä napauta 'Lisää'-painiketta oikeassa yläkulmassa ja valitse 'Vie kappaleluettelo'.

![vie äskettäin kuunnellut](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

'Valitse tiedostomuoto' -näytöllä sinulla on useita vaihtoehtoja - CSV, TXT, M3U.

- CSV

Tämä tarkoittaa pilkuilla erotettuja arvoja, joka on täydellinen tietojesi järjestämiseen siistiin taulukkomuotoon. Kohdetiedostosta löydät parametrit kuten Esittäjän nimi, Albumin nimi, Kappaleen nimi, Aikaleima (kappaleiden kuunteluajankohta), Albumiesittäjän nimi ja Kappaleen kesto. Voit käyttää tätä tiedostoa myöhemmin kuunteluhistoriasi päivittämiseen scrobbler-palveluissa kuten [Last.fm](http://Last.fm), kuten on kuvattu [täällä](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Tässä puhutaan pelkkä teksti -tiedostosta. Se on yksinkertainen ja suoraviivainen, ja sisältää parametrit kuten Esittäjän nimi, Albumin nimi, Kappaleen nimi ja Kesto. Hyödyllinen, jos tarvitset vain luettelon kappaleista tekstimuodossa.

- M3U

Tämä muoto on käytännössä ensisijainen valinta soittolistojen luomiseen. Se on erinomainen, koska voit viedä kappaleluettelosi ja nauttia kappaleistasi millä tahansa laitteella, vaikka sinulla ei olisi alkuperäisiä tiedostoja (jos valitset absoluuttisen URL-osoitteen mediatiedostoille viennin yhteydessä). Tulostiedostosta löydät parametrit kuten Kesto, Esittäjän nimi, Kappaleen nimi ja Mediatiedoston sijainti.

## CSV-muoto

Valitaan nyt CSV ja katsotaan mitä saamme. Valitse yksinkertaisesti CSV ja paina 'Vie'-painiketta.

![valitse tiedostomuoto](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Kun vienti on valmis, näet ilmoituksen kahdella vaihtoehdolla. 'Näytä tiedosto' -napauttaminen paljastaa tulostiedoston asiakirjakansiossasi.

![vienti valmis](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Nyt voit lähettää tiedoston, avata sen ulkoisessa tekstieditorissa tai käyttää sitä kuuntelutietojesi päivittämiseen [Last.fm](http://Last.fm):ssä.

![vientikansio tulostiedostoilla](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

CSV-tulostiedosto sisältää kentät seuraavassa muodossa:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Esimerkiksi:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![viety csv-tiedosto](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## TXT-muoto

TXT-tulostiedosto sisältää kentät seuraavassa muodossa:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Esimerkiksi:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![viety txt-tiedosto](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## M3U-muoto

Seuraavaksi opastamme sinut soittolistan viemisessä M3U-muotoon, joka on de facto -standardi soittolistatiedostoille. Onnistuneen soittolistan viennin pääedellytys on, että kaikkien soittolistan tiedostojen tulee sijaita samassa tallennustilassa, olipa kyseessä pilvipalvelu kuten Google Drive, paikalliset tiedostot tai laitteellasi olevat tiedostot. Aloittaaksesi vientiprosessin avaa mikä tahansa soittolista ja napauta 'Lisää'-painiketta oikeassa yläkulmassa, valitse sitten 'Vie kappaleluettelo' -valikosta.

![soittolistanäyttö](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Seuraavalla näytöllä valitse 'M3U'-tiedostomuoto, jossa kohtaat kaksi vaihtoehtoa 'Mediatiedoston sijaintityypille':

![valitse viennin tiedostomuoto -näyttö](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Jos valitset 'Suhteellinen polku', soittolista luodaan mediatiedostojen sijainneilla kirjoitettuna suhteessa soittolistatiedostoon. Esimerkiksi:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   Tässä tapauksessa vältä M3U-tiedoston sijainnin muuttamista viennin jälkeen, sillä se rikkoo mediatiedostojen polut. Aloittaaksesi soittolistan toiston napauta vain vietyä soittolistatiedostoa, ja sovellus löytää automaattisesti mediatiedostot tallennustilastasi ja aloittaa toiston. Voit jopa viedä soittolistasi tallennustilaan ja tuoda ne sitten uudelleen uudella laitteellasi.

2. Jos valitset 'Absoluuttinen URL', sovellus luo suorat URL-osoitteet mediatiedostoillesi. Tämä mahdollistaa soittolistan toistamisen millä tahansa laitteella/sovelluksella ilman, että kaikkien mediatiedostojen tarvitsee sijaita samassa tallennustilassa soittolistatiedoston kanssa. Tätä vaihtoehtoa tuetaan vain pilvitallennuspalveluille, jotka pystyvät luomaan suoria tiedosto-URL-osoitteita. Huomaa kuitenkin, että joissakin tapauksissa luoduilla URL-osoitteilla voi olla rajallinen voimassaoloaika ja ne voivat vanhentua ajan myötä. Tässä on luettelo tuetuista pilvipalveluista: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (vierastilassa)  

Tulostiedoston mediatiedoston URL on jotain tällaista:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Kun olet valinnut 'Mediatiedoston sijaintityypin', napauta 'Vie'. Sovellus pyytää sinua valitsemaan kohdekansion M3U-tiedoston vientiä varten. Napauta 'Valmis' vahvistaaksesi valintasi.

![valitse kansio](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

Sovellus luo M3U-tiedoston ja lataa/siirtää sen kohdekansioon.

![ladataan m3u-tiedostoa](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Kun vienti on valmis, järjestelmäilmoitus ilmestyy 'Näytä tiedosto' -vaihtoehdolla.

![vienti valmis -ilmoitus](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Napauttamalla tätä paljastuu viety tiedosto sovelluksessa.

![viety m3u-tiedosto tiedostoluettelossa](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Jos valitsit 'Suhteellinen polku' 'Mediatiedoston sijaintityypiksi' edellisessä vaiheessa, tulostiedosto on seuraavassa muodossa:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![m3u-esimerkki suhteellisilla poluilla](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

'Absoluuttinen URL' -vaihtoehdolla sovellus luo M3U-tiedoston muodossa:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![m3u-esimerkki absoluuttisilla tiedosto-URL-osoitteilla](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Voit avata tämän tiedoston millä tahansa laitteella/sovelluksella, joka tukee M3U-soittolistoja.

![m3u-soittolista avattuna ulkoisessa sovelluksessa](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Loppuajatukset

Kappaleiden vieminen Evermusicista ja Flacboxista antaa sinulle täyden hallinnan musiikkitiedoistasi. Olitpa varmuuskopioimassa kuunteluhistoriaasi, scrobbaamassa Last.fm:ään tai nauttimassa soittolistoista ulkoisilla laitteilla, nämä vientivaihtoehdot: M3U, CSV ja TXT - ovat tehokkaita työkaluja joustavuuteen ja yhteensopivuuteen. Hyödynnä näitä ominaisuuksia parantaaksesi tapaa, jolla järjestät, jaat ja palaat musiikkikokoelmaasi eri alustoilla.

## UKK

{{% details title="Mitä vientimuotoa minun tulisi käyttää Last.fm-scrobbaukseen?" closed="true" %}}
Käytä CSV:tä. Se sisältää aikaleimat ja täydelliset metatiedot, joita scrobbaustyökalut kuten Last.fm-Scrubbler-WPF vaativat.
{{% /details %}}

{{% details title="Voinko viedä minkä tahansa kappalekokoelman, en vain soittolistoja?" closed="true" %}}
Kyllä. Voit viedä äskettäin kuunnellut, suosikit, albumit, soittolistat ja minkä tahansa muun kappalekokoelman sovelluksessa samoilla vaiheilla.
{{% /details %}}

{{% details title="Toimiiko M3U-soittolistani muilla laitteilla?" closed="true" %}}
Jos valitset absoluuttinen URL -vaihtoehdon viennin aikana, M3U-tiedostoa voidaan toistaa millä tahansa laitteella, joka tukee M3U-soittolistoja. Huomaa, että jotkin pilvi-URL-osoitteet voivat vanhentua ajan myötä.
{{% /details %}}

{{% details title="Onko vientiominaisuus ilmainen?" closed="true" %}}
Kyllä. Kappalekokoelmien vienti M3U-, CSV- ja TXT-muotoon on saatavilla sekä Evermusicin että Flacboxin ilmaisissa ja premium-versioissa.
{{% /details %}}

{{% details title="Mitkä pilvipalvelut tukevat absoluuttisen URL:n vientiä?" closed="true" %}}
Absoluuttisen URL:n vientiä tuetaan iCloud Drivelle, pCloudille, PanBaidulle, MyCloudHomelle, DLNA:lle, MediaFirelle, OneDrivelle, Boxille, Dropboxille, Google Drivelle ja WebDAV:lle (vierastilassa).
{{% /details %}}
