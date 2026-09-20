---
title: "Näin määrität DLNA/UPnP-mediapalvelimen iPhonelle ja iPadille suoratoistoa varten"
description: "Muuta iPhone tai iPad DLNA/UPnP-mediapalvelimeksi Everdiskillä ja suoratoista kuvat, videot ja musiikki älytelevisioon, pelikonsoliin, VLC:hen tai Kodiin Wi-Fin kautta. Täysi käyttöönotto sekä ohjeet yhdistämiseen Samsung-, LG- ja Sony-televisioista, Windowsista, Macista, Linuxista, Androidista ja toisesta iPhonesta."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "mediapalvelin", "suoratoisto", "älytelevisio", "iphone", "ipad", "wifi"]
keywords: ["DLNA-palvelin iPhone", "UPnP-palvelin iPad", "näin määrität DLNAn iPhonella", "suoratoisto älytelevisioon iPhonesta", "DLNA-mediapalvelin iOS", "videoiden suoratoisto televisioon ilman kaapelia", "iPhonen kuvien toisto televisiossa", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA-mediapalvelin", "UPnP AV -mediapalvelin iOS", "musiikin suoratoisto televisioon iPhonesta", "iPhone-mediapalvelinsovellus"]
readingTime: 9
---

{{< author-byline >}}

DLNA (jota kutsutaan myös nimellä UPnP AV) on hiljainen työjuhta useimpien älytelevisioiden taustalla. Se on yhteinen kieli, jonka avulla televisio tai mediasoitin löytää samassa Wi-Fi-verkossa olevan mediakirjaston ja toistaa siitä ilman, että televisioon tarvitsee asentaa mitään. Jos iPhonesi tai iPadisi voi toimia tuona kirjastona, kuvasi, videosi ja musiikkisi ilmestyvät isolle ruudulle itsestään.

Tämä opas näyttää, miten muutat iPhonen tai iPadin DLNA/UPnP-mediapalvelimeksi [Everdiskillä](/products/everdisk) ja miten avaat kyseisen kirjaston älytelevisiosta, pelikonsolista, VLC:stä, Kodista, tietokoneelta, Android-puhelimesta ja jopa toisesta iPhonesta. Kaikki tapahtuu paikallisen Wi-Fi-verkkosi kautta, joten mitään ei ladata mihinkään.

## Mitä tarvitset

- iPhonen tai iPadin, johon on asennettu [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Television, soittimen tai tietokoneen **samassa Wi-Fi-verkossa** kuin laitteesi.
- Kuvat, videot tai musiikin, jotka haluat toistaa, valmiiksi iPhonellasi (Kuvat-sovelluksessa, Musiikki-sovelluksessa tai Everdiskin Dokumentit-kansiossa).

## Määritä DLNA-palvelin Everdiskissä

### Vaihe 1: Valitse mitä jaat

Avaa Everdisk ja siirry **Jakaminen**-välilehdelle. Napauta **Mitä jaetaan** ja valitse sisältösi:

- Ota käyttöön **Salli pääsy koko kuvakirjastoon** jakaaksesi jokaisen albumin, tai napauta **Lisää kuvia** valitaksesi muutaman.
- Ota käyttöön **Salli pääsy koko musiikkikirjastoon** jakaaksesi kappaleesi, tai napauta **Lisää kappaleita** tehdäksesi valinnan.
- Lisää kansioita tai tiedostoja toiminnoilla **Lisää kansio** ja **Lisää tiedosto**. Sovelluksen oma Dokumentit-kansio jaetaan oletuksena.

Ennen kuin jakaminen voi alkaa, sinulla on oltava vähintään yksi kohde valittuna.

### Vaihe 2: Ota käyttöön Televisio ja mediakeskus (DLNA)

Siirry kohtaan **Asetukset**, sitten **Jakaminen** ja sitten **Yhteydet**. Varmista, että **Televisio ja mediakeskus** on päällä. Se on oletuksena päällä ja kantaa DLNA-merkintää. Tämä on palvelin, jota televisiot ja soittimet etsivät.

### Vaihe 3: Aloita jakaminen

Napauta takaisin **Jakaminen**-välilehdellä isoa **Aloita**-painiketta. Laitteesi on nyt mediapalvelin Wi-Fi-verkossasi. Se näkyy muille laitteille ystävällisellä nimellään, sillä joka näkyy sovelluksessa laitteesi nimenä (jotain kuten "Speedy-Hare", kunnes muutat sen).

DLNA-suoratoisto on aina avoin, joten televisioon ei tarvitse syöttää salasanaa. Pidä Everdisk avoinna näytöllä katselun aikana, koska iOS pysäyttää sovellukset, jotka työnnetään kokonaan taustalle.

## Toista älytelevisiossa

Tämä on yleisin tapaus, ja se kestää yleensä noin kolmekymmentä sekuntia.

1. Aseta televisio **samaan Wi-Fi-verkkoon** kuin iPhonesi.
2. Avaa television sisäänrakennettu mediasoitin. Nimi riippuu merkistä: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** tai **SmartThings** (Samsung), **Content Share** tai **SimplyShare**.
3. Etsi mediapalvelinten tai lähteiden luettelo. Laitteesi näkyy siellä nimellään.
4. Valitse se, selaa kuviisi, videoihisi tai musiikkiisi ja paina toista.

Esikatselukuvat ilmestyvät automaattisesti, joten löydät oikean loma-albumin tai elokuvan ilman arvailua.

### Mitkä televisiot toimivat

Useimmissa **Samsung-, LG-, Sony BRAVIA-, Panasonic (VIERA-laiteohjelmisto)-, Philips- ja Hisense**-televisioissa on DLNA sisäänrakennettuna ja ne toimivat heti. Myös **PlayStation- ja Xbox-konsolit sekä useimmat AV-vastaanottimet** toimivat.

Muutamat alustat jättävät sen pois: **Roku-televisiot, Amazon Fire TV, Vizio SmartCast ja pelkkä Google TV** ilman valmistajan mediasovellusta. Jos televisiosi on jokin näistä eikä se löydä laitettasi, se on yleensä syy. Asenna näihin televisioihin DLNA-soitinsovellus, kuten VLC tai Kodi, tai tavoita tiedostosi verkkoselaimen kautta käyttämällä [WebDAV-käyttöönotto-opasta](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Jotkin merkit pitivät DLNAn toiminnassa vielä senkin jälkeen, kun virallinen DLNA-logo poistettiin, joten jos se näyttää puuttuvan, etsi jotain yllä mainituista mediasoittimien nimistä.

## Toista VLC:ssä tai Kodissa Windowsissa, Macissa ja Linuxissa

VLC ja Kodi ovat ilmaisia, toimivat jokaisessa työpöytäjärjestelmässä ja puhuvat DLNAa hyvin. Ne ovat luotettava tapa avata Everdisk-kirjastosi tietokoneella.

**VLC (Windows, Mac, Linux):**

1. Avaa VLC.
2. Näytä soittolista (Windowsissa ja Linuxissa paina **Ctrl+L**, Macissa avaa **Playlist** View-valikosta).
3. Avaa sivupalkissa **Universal Plug'n'Play** kohdan Local Network alta.
4. Laitteesi näkyy luettelossa. Klikkaa sen sisään ja valitse tiedosto.

**Kodi (Windows, Mac, Linux):**

1. Siirry kohtaan **Videos**, **Music** tai **Pictures**, sitten **Files** ja sitten **Add source** (tai **Browse**).
2. Valitse **UPnP devices**.
3. Valitse laitteesi ja selaa kirjastoasi.

Windowsissa voit myös avata **Windows Media Playerin**, laajentaa sivupalkissa **Other Libraries** -kohdan, ja laitteesi näkyy siellä.

## Toista Androidilla

Android-puhelimissa ja -tableteissa ei ole järjestelmän DLNA-selainta, joten käytä sovellusta:

- **VLC for Android**: avaa sivuvalikko, napauta **Local Network**, ja laitteesi näkyy UPnP-palvelinten alla.
- **BubbleUPnP** tai vastaava UPnP-sovellus: laitteesi näkyy palvelinluettelossa, ja nämä sovellukset voivat myös työntää toiston televisioon.

## Toista toisella iPhonella tai iPadilla

Kaksi laitetta, yksi kirjasto. Sanotaan, että kuvat ovat iPhonellasi ja haluat katsoa niitä iPadillasi.

- Yksinkertaisin reitti on Everdiskin oma **Laitteet**-välilehti toisella laitteella. Se toimii sekä DLNA-asiakkaana että -palvelimena. Avaa Everdisk iPadilla, siirry kohtaan **Laitteet**, ja iPhonesi näkyy kohdassa **Käytettävissä olevat laitteet**. Napauta sitä selataksesi ja toistaaksesi.
- Mikä tahansa iOS:n DLNA-soitinsovellus toimii myös, kuten VLC tai UPnP-selain. Avaa sen paikallisverkkonäkymä ja valitse iPhonesi.

## Toista pelikonsolilla

- **PlayStation 5 ja 4**: avaa **Media**-sovellus (Media Gallery), ja laitteesi näkyy mediapalvelimena, jota voit selata.
- **Xbox**: käytä DLNAa tukevaa mediasoitinsovellusta ja valitse sitten laitteesi palvelinluettelosta.

## Jos laitteesi ei näy luettelossa

Jotkin soittimet antavat sinun lisätä mediapalvelimen osoitteella sen sijaan, että odottaisit sen löytymistä. Everdiskin **Jakaminen**-näytöllä DLNA-kortti näyttää laitekuvausosoitteen, joka päättyy muotoon `/device-desc.xml`. Syötä tuo osoite soittimen palvelimen lisäyskenttään.

Jos se ei vieläkään näy, tarkista kolme asiaa: molemmat laitteet ovat samassa Wi-Fi-verkossa (ei vierasverkossa, joka estää laitteiden välisen liikenteen), Everdisk on avoinna ja jakaminen on aloitettu, ja **Televisio ja mediakeskus** on päällä Asetuksissa.

## Jos video ei toistu

DLNA luovuttaa tiedoston televisiolle sellaisenaan, ja television on pystyttävä purkamaan se. Jos leike kieltäytyy toistumasta, sen muotoa ei todennäköisesti tueta kyseisessä televisiossa. Kaksi korjausta:

- Avaa **Asetukset**, sitten **Jakaminen** ja sitten **Videot**, ja alenna **Laatu**-asetusta. Everdisk muuntaa videon tällöin yhteensopivampaan muotoon suoratoiston aikana. (Muunnos on Premium-ominaisuus.)
- Tai avaa sama tiedosto verkkoselaimessa Everdiskin selainlinkin kautta, joka on joustavampi muotojen suhteen.

## Tosielämän tapoja käyttää tätä

- **Perheen elokuvailta.** Puhelimella kuvatut videot toistuvat olohuoneen televisiossa ilman kaapelia tai Apple TV:tä.
- **Lomakuvat isolla ruudulla.** Avaa kuvakirjastosi televisiossa ja selaa matkaa läpi kaikkien läsnä ollessa.
- **Taustamusiikkia juhliin.** Osoita DLNA-kaiutin tai AV-vastaanotin Musiikki-kirjastoosi ja anna sen soida.
- **Katselu hotellin televisiossa**, jossa on mediasoitin, kun molemmat laitteet ovat huoneen Wi-Fi-verkossa.

## Muutama vinkki

- Pidä Everdisk avoinna suoratoiston aikana. Jos lukitset puhelimen pitkäksi aikaa, iOS voi pysäyttää sovelluksen ja toisto keskeytyy.
- Kytke puhelin virtalähteeseen pitkiä elokuvahetkiä varten.
- Nopeimman suoratoiston takaamiseksi pidä **Muoto** ja **Laatu** asetuksella **Alkuperäinen** Asetuksissa, ja alenna niitä vain, jos tietty televisio kamppailee tiedoston kanssa.
- DLNA on pelkkää suoratoistoa. Kukaan television puolella ei voi muuttaa tai poistaa tiedostojasi. Kaksisuuntaista tiedostonsiirtoa varten käytä sen sijaan [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/)-, [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/)- tai [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/)-palvelinta.

## Usein kysytyt kysymykset

{{% details title="Mikä ero on DLNAn ja UPnP:n välillä?" closed="true" %}}
Ne liittyvät läheisesti toisiinsa. UPnP on taustalla oleva verkkostandardi, ja DLNA on sen päälle rakennettu mediaprofiili, jota televisiot ja soittimet käyttävät kuvien, videoiden ja musiikin jakamiseen ja toistamiseen. Jokapäiväisessä käytössä sanat ovat keskenään vaihdettavissa. Kun otat Everdiskissä käyttöön Televisio ja mediakeskus, laitteesi muuttuu DLNA/UPnP-mediapalvelimeksi, jota mikä tahansa DLNA-asiakas voi selata.
{{% /details %}}

{{% details title="Tarvitseeko televisiooni asentaa mitään?" closed="true" %}}
Ei. Jos televisiosi tukee DLNAa, siinä on jo mediasoitin, joka voi löytää laitteesi Wi-Fi-verkosta. Asennat Everdiskin vain siihen iPhoneen tai iPadiin, joka sisältää sisällön. Jos televisiosi ei tue DLNAa, asenna soitin, kuten VLC tai Kodi, siihen kytketylle laitteelle.
{{% /details %}}

{{% details title="Miksi iPhoneni ei näy televisiossa?" closed="true" %}}
Tarkista, että molemmat laitteet ovat samassa Wi-Fi-verkossa. Vierasverkot sekä jotkin toimisto- tai hotelliverkot estävät laitteita näkemästä toisiaan, mikä estää DLNAn. Varmista sitten, että Everdisk on avoinna jakamisen ollessa aloitettu, ja että Televisio ja mediakeskus on päällä kohdassa Asetukset, Jakaminen, Yhteydet. Jos televisio ei vieläkään löydä sitä, lisää palvelin käsin käyttämällä laitekuvausosoitetta, joka päättyy muotoon /device-desc.xml.
{{% /details %}}

{{% details title="Tarvitseeko DLNA-suoratoisto salasanan?" closed="true" %}}
Ei. DLNA on aina avoin kaikille samassa Wi-Fi-verkossa oleville sen ollessa päällä, minkä vuoksi television puolella ei ole kirjautumista. Tämä on hyvä kotiverkossa, johon luotat. Verkossa, johon et luota, sammuta Televisio ja mediakeskus, kun olet valmis, tai käytä sen sijaan salattua SMB-palvelinta.
{{% /details %}}

{{% details title="Voinko suoratoistaa Chromecastiin tai Rokuun?" closed="true" %}}
Chromecast ja Roku eivät toimi DLNA-soittimina suoraan, joten ne eivät löydä laitettasi suoraan. Kiertotie on asentaa DLNA-sovellus, joka voi lähettää suoratoiston, kuten VLC tai BubbleUPnP puhelimeen, ja työntää toisto sieltä Chromecastiin tai Rokuun. Useimmissa muissa älytelevisioissa DLNA toimii ilman tätä kaikkea.
{{% /details %}}

{{% details title="Video toistuu ilman ääntä tai ei avaudu. Mitä voin tehdä?" closed="true" %}}
Se on muoto, jota televisio ei voi purkaa. Avaa Everdiskissä Asetukset, Jakaminen, Videot ja alenna Laatu-asetusta, jotta sovellus muuntaa videon yhteensopivampaan muotoon suoratoiston aikana. Voit myös avata saman tiedoston selainlinkin kautta, joka käsittelee useampia muotoja.
{{% /details %}}

{{% details title="Voinko suoratoistaa musiikkia, en pelkkiä videoita?" closed="true" %}}
Kyllä. Ota käyttöön Salli pääsy koko musiikkikirjastoon, tai lisää tietyt kappaleet, ja aloita sitten jakaminen. Kappaleesi näkyvät missä tahansa DLNA-kaiuttimessa, AV-vastaanottimessa tai televisiossa kansikuvineen ja kappaletietoineen. Musiikki jaetaan aina alkuperäisessä laadussaan.
{{% /details %}}

{{% details title="Täytyykö sovelluksen pysyä auki katselun aikana?" closed="true" %}}
Kyllä. iPhonesi toimii palvelimena, ja iOS pysäyttää sovellukset, jotka työnnetään kokonaan taustalle pitkäksi aikaa. Pidä Everdisk näytöllä suoratoiston aikana ja kytke virtalähteeseen pitkiä hetkiä varten.
{{% /details %}}

{{% details title="Miten suoratoistan yhdestä iPhonesta toiseen iPadiin?" closed="true" %}}
Aloita jakaminen iPhonella, avaa sitten Everdisk iPadilla ja siirry Laitteet-välilehdelle. iPhone näkyy kohdassa Käytettävissä olevat laitteet mediapalvelimena. Napauta sitä selataksesi ja toistaaksesi. Everdisk toimii sekä DLNA-asiakkaana että -palvelimena, joten et tarvitse muuta sovellusta.
{{% /details %}}

{{% details title="Onko Everdisk ilmainen?" closed="true" %}}
Kyllä, Everdiskin voi ladata ilmaiseksi ja DLNA-mediapalvelin sisältyy siihen. Valinnainen kertaostoksena hankittava Premium Lifetime lisää lisäominaisuuksia, kuten kuvien ja videoiden muunnoksen vanhemmille televisioille, mukautetut portit ja muuta. Voit ottaa DLNA-suoratoiston käyttöön ja käyttää sitä maksamatta.
{{% /details %}}

Valmis kokeilemaan? [Lataa Everdisk App Storesta](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) ja suoratoista ensimmäinen albumisi televisioon parissa minuutissa. Kysymyksiä tai palautetta? Lähetä meille sähköpostia osoitteeseen **support@everappz.com**.
