---
title: "Asetukset"
date: 2020-02-01
description: "Tutki jokaista Flacboxin asetusta — toiston mieltymyksistä, FFmpeg / järjestelmän äänimoottorista, Hi-Res äänilähdöstä, taajuuskorjaimen säädöistä, sävelkorkeuden korjauksesta, IO-puskurin kestosta, metatietojen synkronoinnista, soittolistan hallinnasta, tiedostosiirroista, aloitusnäytön widgeteistä, Apple CarPlaysta, UI-personoinnista, kielestä, pääsykoodista, varmuuskopioinnista ja palautuksesta sekä Premium-päivityksestä."
keywords: [
  "Flacbox asetukset", "äänisoittimen konfigurointi", "premium-päivitys Flacbox",
  "WiFi Drive", "metatietojen synkronointi", "taajuuskorjain", "toistonopeus",
  "kaksoiskappaleet soittolistassa", "tiedostonhallinta asetukset", "offline-musiikin synkronointi",
  "äänitunnisteiden muokkaustyökalu", "tummamalli", "ota ostokset uudelleen käyttöön", "varmuuskopiointiasetukset",
  "Flacbox widgettiasetukset", "Flacbox CarPlay-asetukset",
  "Flacbox FFmpeg-asetukset", "Flacbox näytteenottotaajuusasetukset",
  "Flacbox sävelkorkeuden korjausasetukset", "Flacbox IO-puskuri",
  "Flacbox pääsykoodi", "Flacbox kieli", "Flacbox personointi",
  "Flacbox analytiikka"
]
tags: ["opas", "flacbox", "asetukset"]
readingTime: 16
---


Asetukset-ruutu on Flacboxin hallintakeskus. Täältä voit päivittää Premiumiin, konfiguroida äänimoottoria (järjestelmäkoodekit tai FFmpeg), hallita musiikkikirjastoasi, asettaa tiedostonhallinnan, mukauttaa äänitunnisteiden muokkaustyökalua, ottaa käyttöön aloitusnäytön widgettejä ja Apple CarPlayta, varmuuskopioida tietosi sekä käyttää ohjeita ja oikeudellisia tietoja. Osiot on ryhmitelty otsikoiden alle: Ostokset ja Päivitykset, Sovelluksen Asetukset, Ohje ja Juridiikka ja Yksityisyys.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacboxin Asetusten Pääruutu" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Päivitä Premiumiin

Päivitä sovellus Premium-versioon poistaaksesi kaikki rajoitukset. Sovelluksen ilmaisversio tarjoaa kertaluontoisen eliniän sisäisen oston ja kaksi tilausvaihtoehtoa (1 kuukausi ja 1 vuosi) kaikkien rajoitusten poistamiseksi ja Premiumiin päivittämiseksi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Päivitä Premiumiin" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Perhejako** on käytössä kaikille ostoille ja suunnitelmille, joten voit jakaa Premium-version jopa viiden perheenjäsenesi kanssa ilman lisäkustannuksia.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Valitse Premium-suunnitelma" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Voit lukea lisää ostoista ja Premium-versiosta täältä: [Mikä on ero Flacboxin ja Flacbox Premiumin välillä](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Ostojen Jakaminen iOS:n ja Macin Välillä

Elinaikaiset ostot ja tilaukset jaetaan iOS:n ja Macin välillä käyttämällä iCloudia tietojen synkronointiin. Jos sinulla on Premium-versio iOS-laitteellasi, varmista, että sinulla on uusin versio asennettuna ja iCloud on käytössä. Käynnistä sovellus iOS:ssä ja odota minuutti, jotta ostotietosi ladataan iCloudiin.

Voit myös yrittää napauttaa Palauta Ostokset -painiketta sovelluksen asetuksissa. Asenna sen jälkeen uusin sovellusversio App Storesta Macillesi ja käynnistä sovellus. Varmista, että sinulla on internetyhteys ja käytät samaa iCloud- ja App Store -tiliä Macilla kuin iOS:ssä. Odota minuutti, jotta sovellus lataa ostotiedot iCloudista.

## Ostojen Palauttaminen Uudelle Laitteelle

Palauttaaksesi ostosi uudelle laitteelle käytä valikkoa Ostokset → Palauta Ostokset. Näet ostolistasi. Jos et näe kaikkia, vahvista, että laite on yhteydessä samaan Apple ID:hen, jota käytettiin ostoksiin, ja varmista, että iCloud on käytössä.

## Kokeile Premiumia Ilmaiseksi

Voit päivittää Premium-versioon ilmaiseksi rajoitetuksi ajaksi tällä valikolla. Katso vain mainos tai kerro ystävillesi sovelluksesta saadaksesi Premiumin ilmaiseksi.

## Ostokset

Voit palauttaa aikaisemmat ostokset tästä valikosta. Jos kohtaat aktivointivirheitä, yritä ottaa käyttöön Palauta Ostokset Sovelluksen Käynnistyksen Yhteydessä -vaihtoehto.

## Ohjelmistopäivitys

Napauta Ohjelmistopäivitys tarkistaaksesi, onko Flacboxin uudempi versio saatavilla. Sovellus vertaa asennettua versiotasi App Storen uusimpaan versioon.

## Uudet Ominaisuudet

Tämä valikko on saatavilla uuden version julkaisun jälkeen. Se näyttää yhteenvedon muutoksista ja uusista ominaisuuksista.

## Äänisoitin

Tämä osio konfiguroi äänisoittimen ja taustalla olevan äänimoottoria, mukaan lukien FFmpeg / järjestelmäkoodekin valinta ja Hi-Res äänilähtövaihtoehdot.

### Yleinen

Nämä asetukset kattavat äänisoittimen perusnäkökohdat — toistojono, äänilähtö ja soittimen tilan tallentaminen.

- **Toistotila** — valitse, miten äänisoitin käyttäytyy kappaleen päättyessä:
  - **Toista Kaikki** — toistaa kaikki jonon kappaleet uudelleen.
  - **Toista Yksi** — toistaa vain nykyisen kappaleen.
  - **Toisto Stop** — pausauttaa toiston, kun nykyinen kappale päättyy.
  - **Ei Toistoa** — antaa jonon soida läpi toistamatta.
- **Satunnaistila** — satunnaistaa kappaleiden järjestyksen jonossa. Voit kytkeä sen **Satunnaisjärjestys pois** tai **Satunnaisjärjestys päälle**.
- **Äänikoodekki** — valitse toistoon käytettävä äänimoottori:
  - **Järjestelmän Koodekki + FFmpeg** — priorisoi järjestelmän koodekkin missä mahdollista. Sävelkorkeuden korjaus ja näytteenottotaajuus voivat olla rajoitettuja.
  - **FFmpeg** — pakottaa FFmpeg-koodekkin kaikille tiedostoille, avaten sävelkorkeuden korjauksen ja näytteenottotaajuuden.
- **Äänilähdön Näytteenottotaajuus** — säädä äänenlaatuun optimoimiseksi, erityisen hyödyllinen ulkoisen DAC:n kanssa. Saatavilla olevat arvot: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** ja **96 kHz**.
- **Äänilähdön Kanavien Määrä** — monikanavaisille järjestelmille ulkoisen DAC:n kanssa: Mono, Stereo, Keski / Vasen / Oikea, Keski / Vasen / Oikea / Surround, ITU BS.775-1, 5.1 Surround ja SDDS.
- **Äänilähdön Suositeltu IO-puskurin Kesto** — konfiguroi puskurin kesto. Tyypillinen arvo latenssin minimoimiseksi: noin **5 millisekuntia (0,005 sekuntia)**.
- **Äänilähtötila (vain iOS)** — konfiguroi sekoitettu äänilähtö. Yksityiskohtaiset ohjeet [täällä](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Tallenna Toistokohta** — tallentaa ja palauttaa toistokohdan.
- **Tallenna Äänisoittimen Tila** — säilyttää soittimen tilan ennen sovelluksen sulkemista.

Kun olet ottanut käyttöön sekä **Tallenna Toistokohta** että **Tallenna Äänisoittimen Tila**, avaa mikä tahansa kansio, albumi, artisti tai genre ja näet **Jatka Toistoa** -painikkeen ruudun yläosassa.

### Personointi

Personointi antaa sinulle mahdollisuuden mukauttaa äänisoittimen ruudun ulkoasua, muuttaa käytettävissä olevia säätimiä ja konfiguroida ohitusaikasäätimiä.

- **Äänisoittimen Ruututyyli** — konfiguroi elementtien sijoittelu.
- **Albumikuvien Vieritytyyli** — konfiguroi suositeltu albumikuvien vieritytyyli.
- **Lisäelementit** — ota käyttöön lisäelementtejä. Äänimuodon Tiedot näyttää äänitiedot kansikuvan yläpuolella; Äänenvoimakkuuden Liukusäädin näyttää liukusäätimen toistopaikkien alapuolella.
- **Pääruudun Toiminnot** — konfiguroi, mitkä painikkeet näkyvät oletuksena: Toisto- ja Satunnaistila, Seuraava ja Edellinen Kappale, Ohitusaika, Unitajastin, Google Chromecast, AirPlay ja Bluetooth, Äänitaajuuskorjain, Hae, Kirjanmerkit, Nopeus, Lisää Kirjanmerkki, Lisää Suosikkeihin, Kommentit ja lisää.
- **Toistopaikkien Lukitusnäytöllä** — valitse, mitkä säätimet näkyvät. Mahdolliset arvot: Ohitusaika, Lisää Kirjanmerkki, Lisää Suosikkeihin.
- **Ohitusaika-painikkeet** — valitse aikaväli ohituspainikkeille.

### Tiedostojen Lataaminen

Voit muuttaa verkkotyyppiä kappaleiden lataamiseen. Saatavilla olevat vaihtoehdot: **Wi-Fi**, **Wi-Fi ja Mobiilidatat**.

- **Esilatausaika** — aseta puskurointiaikaväli.
- **Käytä Suoraa URL:ää** — kun käytössä, suoraa URL:ää käytetään, jos palvelin tukee sitä.

### Äänitaajuuskorjain

Konfiguroi 10-kanaavainen äänitaajuuskorjain, esiasetukset ja esivahvistin. Lue lisää [täältä](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Toistonopeus

Säädä nopeutta **0,02× – 3,00×**. Napauta konfigurointikuvaketta **tarkkaan tilaan** siirtymiseksi.

### Sävelkorkeuden Korjaus

Muuta asetuksia ennalta määritetyillä arvoilla tai **tarkalla tilalla**. Saatavilla FFmpeg-koodekissa, vaihteluvälillä **-1000 – +1000**.

### Toistokätkö

Kappaleet ladataan automaattisesti sujuvan toiston varmistamiseksi. Voit poistaa tämän käytöstä kaksoiskappaleiden välttämiseksi.

### Unitajastin

Aktivoi ajastin toiston automaattiseen pysäyttämiseen. Napauta konfigurointikuvaketta **tarkkaan tilaan** minuutti kerrallaan tarkkuudella.

## Kirjasto

Musiikkikirjastosi asetukset — automaattinen synkronointi, metatietojen lukeminen, albumikuvien lataaminen, soittolistat, äskettäin kuunnellut ja suosikit — ovat täällä.

### Metatietojen Lukeminen

Kun lisäät kappaleita kirjastoon, **metatietojen lukija** aloittaa työskentelyn. Tämä taustaprosessi lukee kaikki metatiedot ja organisoi ne Artistin, Albumin, Genren ja Säveltäjän mukaan.

Metatietojen lukija **päivittää vain metatiedot kirjastossasi** eikä muuta tiedostoja. Metatietojen muokkaamiseksi itse tiedostoissa, käytä sisäänrakennettua **tunnisteiden muokkaustyökalua**.

Kun **Metatietojen Lukeminen Taustalla** on käytössä, lukija jatkaa taustamoodissa.

**Ladata metadata uudelleen** merkitsee kaikki tiedostot puuttuvien metatietojen saamiseksi päivitystä varten.

**Käynnistä Metatietojen Lukeminen** aktivoi lukijan manuaalisesti.

### Online-synkronointi

Automaattinen online-musiikin synkronointi lisää kappaleita yhdistetyistä pilvipalveluista automaattisesti.

Online-synkronointi toimii vain kun sovellus on etualalla. Voit valita kuinka usein se toimii. Asetus **Heti** käynnistää synkronoinnin joka kerta, kun avaat sovelluksen.

### Offline-synkronointi

Konfiguroi offline-musiikin synkronointi.

#### Synkronoidut offline-kansiot

Kun merkitset online-kansion offline-tilaan saatavaksi, se ilmestyy tänne. Sisältö ladataan **Paikalliset Tiedostot → Offline-kansiot** -kohtaan.

#### Aikaväli

Valitse kuinka usein sovellus tarkistaa offline-kansiot muutosten varalta.

#### Käynnistä Paikallisten Kansioiden Skannaus

Skannaa kaikki paikalliset kansiot sovelluksen **Documents**-hakemistossa tuettuja äänitiedostoja varten.

### Personointi

Konfiguroi musiikkikirjaston ruututyyli. Kolme vaihtoehtoa: **Yksinkertainen valikko, Ryhmitelty valikko, Välilehtivalikko**.

### Albumikuvat

Konfiguroi, miten sovellus lataa ja tallentaa kansitaidetta.

- **Verkkotyyppi** — valitse **Wi-Fi** tai **Wi-Fi ja Mobiilidatat**.
- **Lataa Albumikuvat Online-tiedostoille** — lataa upotetut albumikuvat pilvivarastossa oleville tiedostoille.
- **Hae Kansiosta** — jos kappaleella ei ole upotettua kantta, sovellus etsii JPEG- tai PNG-kuvia samasta kansiosta.
- **Kansikuvan Laatu** — valitse albumikuvien laatu.
- **Näytä Kansiossa** — avaa kansio, johon albumikuvat tallennetaan.
- **Poista Kaikki** — poistaa tallennetut albumikuvat tallennustilan vapauttamiseksi.

### Soittolistat

Ota käyttöön mahdollisuus lisätä sama kappale soittolistaan kahdesti. Oletuksena tämä vaihtoehto on poissa käytöstä.

### Äskettäin

Hallinnoi äskettäin toistettujen kappaleiden listaa.

- **Poista Lista** — poistaa koko listan.
- **Muuta Listan Kokoa** — aseta elementtien määrä.
- **Vie Kappalelista** — vie M3U, CSV tai TXT -muodossa. Ohjeet [täällä](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Suosikit

Hallinnoi suosikkikappaleidesi listaa.

- **Samanaikainen Muokkaus** — kun käytössä, kappaleen lisääminen suosikkeihin lisää sen sekä kirjastoon että tiedostoihin.
- **Poista Lista** — poistaa koko suosikkilistan.
- **Vie Kappalelista** — vie M3U, CSV tai TXT -muodossa.

### Poista Musiikkikirjasto

Poista musiikkikirjaston tietokanta. Tallennustilassa olevat musiikkitiedostot jätetään koskemattomiksi.

## Pääsykoodi

Aktivoi pääsykoodi-ruutu sovelluksen tietojen suojaamiseksi 4-numeroisella numerokoodilla. Yhdistä se iOS:n Face ID / Touch ID -toiminnolla lisäsuojaukseksi.

## Tiedostonhallinta

Tiedostonhallinta-osio hallitsee, miten tiedostoja siirretään, tallennetaan ja esikatsellaan.

### Tiedostosiirrot

Valitse verkkomieltymyksesi tiedostojen lataamiseen laitteellesi.

### Rinnakkaisten Tehtävien Enimmäismäärä

Aseta rinnakkaisten lataussäikeiden määrä.

### Tiedostonsiirtotehtävät

Näyttää tällä hetkellä aktiiviset lähetys- ja lataustehtävät.

### Taustasiirrot

Salli lataukset sovelluksen ollessa taustalla.

### Tallenna Ladatut Tiedostot Kohteeseen

Valitse oletuslatauksen hakemisto tai anna sovelluksen kysyä joka kerta.

### Synkronoidut Offline-kansiot

Hallinnoi offline-synkronointia valituille kansioille. Lue lisää [täällä](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Aikaväli

Valitse kuinka usein offline-kansiot synkronoidaan.

### Näytä Täydelliset Tiedostonimet

Näytä täydelliset tiedostonimet mukaan lukien tiedostopäätteet.

### Muokkaa Online-tiedostoja

Poista online-tiedostojen muokkaus käytöstä siirtyäksesi vain luku -tilaan.

### Kopioi Tiedostot Avattaessa

Määrittele, miten sovellus käsittelee muista sovelluksista tuotuja tiedostoja.

### Esikatselukuvat Tiedostoille

Hallinnoi ja poista luotuja esikatselukuvia tallennustilan vapauttamiseksi.

### Poista Väliaikaiset Tiedostot

Tyhjennä sovelluksen kätkökansio tallennustilan palauttamiseksi.

## Äänitunnisteiden Muokkaustyökalu

Konfiguroi sisäänrakennettu äänitunnisteiden muokkaustyökalu.

### Albumikuvan Skaalaus

Valitse skaalaustapa albumikuvan tallentamiseen äänitunnisteisiin.

### Päivitä Online-tiedostot

Kun käytössä, sovellus päivittää automaattisesti tiedoston metatiedot pilvipalvelimella muokkauksen jälkeen.

### Poista Tiedosto Online-muokkauksen Jälkeen

Valitse, poistaako sovellus ladatun kopion online-tiedoston muokkauksen jälkeen.

### Pääruudun Painikkeet

Valitse, mitkä painikkeet ovat näkyvissä äänitunnisteiden muokkaustyökalun pääruudulla.

Syvempää erämuokkausta varten monille tiedostoille kerrallaan, asenna seuralaissovelluksemme **Evertag**.

## Widgetit

Ota widgetit käyttöön, jotta sovellus päivittää widgettitiedot toiston aikana. Ota käyttöön vain jos käytät widgettejä aloitusnäytöllä tai lukitusnäytöllä.

Voit lisätä Flacbox-widgettejä painamalla pitkään Aloitusnäyttöäsi tai Lukitusnäyttöäsi, napauttamalla **+**, hakemalla **Flacbox** ja valitsemalla widgetin koon.

## CarPlay

Muuta CarPlay-asetuksia täällä.

### Lajittele

Konfiguroi lajitteluvaihtoehdot kaikille CarPlay-ruuduille.

### Sisällön Latausraja

Valitse, käyttääkö sovellus sivutusta CarPlay-ruudulla.

### Valikon Kuvakkeiden Liukuvärin Väri

Valitse värimaailma CarPlay-aloitusnäytölle.

### Näytä Kuvat

Poista kuvat käytöstä CarPlay-ruudulla latausnopeuden optimoimiseksi.

### Keskeytä Toisto Yhdistettäessä

Ota käyttöön äkillisen kovan äänen välttämiseksi CarPlayyn yhdistettäessä.

## Wi-Fi Drive

Aktivoi **Wi-Fi Drive** tiedostojen siirtämiseksi tietokoneelta. Yksityiskohtaiset ohjeet [täällä](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personointi

Mukauta käyttöliittymä mieltymystesi mukaan.

### Sovelluksen Kuvake

Valitse vaihtoehtoinen sovelluksen kuvake aloitusnäytöllesi (Premium).

### Värimaailma

Valitse käyttöliittymän teema ja ota tummamalli käyttöön.

### Taustatyyli

Muokkaa sovelluksen taustatyyliä. Ainoa vaihtoehto tällä hetkellä on **Hämärretty Albumin Kansi**.

### Listankohteiden Ulkoasu

Säädä, miten kohteet näytetään listoissa.

### Sisällön Latausraja

Oletuksena sovellus käyttää sivutusta. Voit poistaa sivutuksen käytöstä kaiken lataamiseksi kerralla.

### Paikallisten Tiedostojen Ruututyyli

Muuta **Paikalliset Tiedostot** -osion esitystapaa.

### Musiikkikirjaston Ruututyyli

Mukauta **Musiikkikirjasto**-ruudun ulkoasua.

### Äänisoittimen Ruututyyli

Konfiguroi **Äänisoitin**-ruudun ulkoasu.

### Kontekstivalikon Tyyli

Valitse kontekstivalikon tyyli, joka näytetään **Lisää toimintoja** -painiketta napautettaessa.

## Ikkuna

Saatavilla Macilla ja Catalystilla. Konfiguroi ikkunaan liittyviä asetuksia.

## Näyttö

Valitse, pysyykö näyttö aktiivisena sovelluksen käytön aikana.

## Saavutettavuus

Aktivoi **Tekstimoodi** kaikkien kuvien piilottamiseksi käyttöliittymässä. Aktivoituu automaattisesti, kun VoiceOver on aktiivinen.

## Kieli

Muuta sovelluksen kieltä. Muutos astuu voimaan, kun suljet Flacboxin kokonaan ja avaat sen uudelleen. Tällä hetkellä tuetut lokalisoinnit sisältävät: Afrikaansi, Akan, Albania, Amhara, Arabia, Armenia, Assami, Aymara, Azerbaidžan, Bambara, Bengali, Baski, Valkovenäjä, Bosnia, Bulgaria, Burma, Katalaani, Cebuano, Kiina (yksinkertaistettu), Kiina (perinteinen), Korsika, Kroatia, Tšekki, Tanska, Dhivehi, Dogri, Hollanti, Englanti, Esperanto, Viro, Ewe, Filipino, Suomi, Ranska, Galicia, Ganda, Georgia, Saksa, Kreikka, Guarani, Gujarati, Haitin kreoli, Hausa, Havaiji, Heprea, Hindi, Hmong, Unkari, Islanti, Igbo, Iloko, Indonesia, Iiri, Italia, Japani, Jaava, Kannada, Kazakki, Khmer, Kinyarwanda, Korea, Krio, Kurdi, Kurdi Sorani, Kirgiisi, Lao, Latina, Latvia, Lingala, Liettua, Luxemburg, Makedonia, Maithili, Malagasy, Malaiji, Malayalam, Malta, Māori, Marathi, Mizo, Mongolia, Nepali, Pohjoinen Sotho, Norjan Bokmål, Nyanja, Odia, Oromo, Pashto, Persia, Puola, Portugali, Punjabi, Romania, Venäjä, Samoa, Sanskrit, Gaeli (Skotlanti), Serbia, Shona, Sindhi, Sinhala, Slovakia, Sloveenia, Somalia, Etelä-Sotho, Espanja, Sunda, Swahili, Ruotsi, Tadžikki, Tamili, Tataari, Telugu, Thai, Tsonga, Turkki, Turkmeeni, Ukraina, Urdu, Uiguuri, Uzbekki, Vietnam, Wales, Xhosa, Jiddiš, Yoruba, Zulu.

## Varmuuskopiointi ja Palautus

Käytä tätä ominaisuutta kaikkien sovellustietojesi varmuuskopiointiin tai siirtämiseen toiselle laitteelle. Voit valita, mitä sisällyttää:

- **Tietokanta** — kaikki musiikkikirjastosi kappaleet, mukaan lukien soittolistat.
- **Albumikuvat** — kaikki tallennetut albumikuvat.
- **Asetukset** — kaikki sovelluksesi asetukset.

Napauta **Varmuuskopioi Sovellustiedot** aloittaaksesi varmuuskopioinnin. Sovellustiedot kirjoitetaan yhteen tiedostoon, jota voit myöhemmin käyttää sovelluksen tilan palauttamiseen uudelle laitteelle tai asennuksen jälkeen.

Palauttaaksesi sovellustiedot uudelle laitteelle, siirrä varmuuskopiointitiedosto uudelle laitteelle käyttämällä yhdistettyä pilvipalvelua tai iCloudia ja avaa se uudella laitteella.

Yksityiskohtaiset vaiheittaiset ohjeet: [Miten Siirtää Musiikkikirjastosi Laitteiden Välillä: Vaiheittainen Opas](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ohje

Käytä sovelluksen opasta saadaksesi apua ja ohjausta sovelluksen tehokkaaseen käyttöön.

## Usein Kysytyt Kysymykset

Löydä vastauksia yleisiin kysymyksiin UKK-osiosta.

## Lähetä Palautetta

Onko sinulla palautetta tai tarvitsetko apua? Lähetä palautteesi tukitiimillemme suoraan sovelluksesta.

## Jaa Tämä Sovellus

Jaa sovellus ystävillesi levittääksesi sanaa.

## Tutustu Lisää Sovelluksiin

Tutustu muihin Everappzin sovelluksiin.

## Käyttöehdot

Kuvailee sovelluksen käyttöehdot. Ole hyvä ja lue ne ennen sovelluksen käyttöä.

## Tietosuojakäytäntö

Käy tietosuojakäytäntösivulla ymmärtääksesi tietojenkäsittelytapamme. Ole hyvä ja lue se ennen sovelluksen käyttöä.

## Analytiikka ja Tietojen Keruu

Tarkista, mitkä palvelut ovat käytössä analytiikan ja tietojen keruun osalta, ja poista käytöstä ne, joita et halua.

## Lakisääteiset Tiedotteet

Sisältää tietoja sovelluksessa käytetyistä kirjastoista sekä sovelluksen versionumeron ja koontitiedot.
