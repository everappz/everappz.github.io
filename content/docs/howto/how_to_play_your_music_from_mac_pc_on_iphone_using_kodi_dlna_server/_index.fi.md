---
title: "Kuinka toistaa musiikkia Mac / PC / Linux / NAS -laitteesta iPhonessa Kodi DLNA -palvelimen avulla"
date: 2025-07-25
description: "Suoratoista musiikkia tietokoneeltasi tai NAS-laitteelta iPhoneen Wi-Fi:n kautta Kodi DLNA:n ja Evermusic-sovelluksen avulla."
keywords: ["kodi dlna palvelin", "suoratoista musiikkia iphoneen", "toista musiikkia nas-laitteesta", "evermusic dlna", "mac-musiikki iphoneen", "windows-musiikki iphoneen", "kodi dlna iphone", "dlna äänisuoratoisto"]
tags: ["dlna", "kodi", "evermusic", "iphone", "musiikin suoratoisto", "mac", "nas", "linux", "paikallisverkko"]
readingTime: 5
---

{{< author-byline >}}


**Yhteenveto:** Asenna Kodi Mac-, PC-, Linux- tai NAS-laitteellesi, ota käyttöön sen DLNA/UPnP-palvelin ja suoratoista koko musiikkikirjastosi iPhoneen tai iPadiin ilmaisella Evermusic- tai Flacbox-sovelluksella Wi-Fi:n kautta. Tilauksia ei tarvita.

## Johdanto

Jos sinulla on **Mac, Windows PC, Linux-kone tai NAS-laite**, voit helposti muuttaa sen **henkilökohtaiseksi musiikkipalvelimeksi** kotona käyttämällä [Kodi](https://kodi.tv/)-ohjelmistoa, joka on ilmainen ja avoimen lähdekoodin mediaalusta. Kodin sisäänrakennetulla **DLNA/UPnP-palvelimella** voit suoratoistaa koko musiikkikirjastosi mille tahansa DLNA-yhteensopivalle laitteelle — mukaan lukien iPhonellesi tai iPadillesi.

Tässä oppaassa näytämme sinulle vaihe vaiheelta, kuinka:

- Asentaa Kodi Mac- tai PC-tietokoneellesi  
- Määrittää musiikkikansiot jakamista varten  
- Ottaa käyttöön DLNA-musiikkipalvelimen  
- Käyttää musiikkia **Evermusic**- tai **Flacbox**-sovelluksella iOS:ssa

Tämä asennus on 100% ilmainen — ei tilauksia, vain omaa musiikkiasi suoratoistettuna Wi-Fi-verkossasi. Halusitpa sitten järjestää suuren MP3-kokoelmasi, kuunnella FLAC-tiedostoja Wi-Fi:n kautta tai yksinkertaisesti nauttia paikallisesta musiikistasi ilman iTunes-synkronointia, tämä asennus on täydellinen sinulle.

## Lataa ja asenna Kodi Mac / PC / Linux / NAS -laitteellesi

Vieraile ensin Kodin virallisilla verkkosivuilla:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodin pääsivu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Napsauta **Lataukset** ja vieritä löytääksesi version tietokoneellesi.
Valitse käyttöjärjestelmäsi. Tässä esimerkissä käytämme **macOS**:ää.

{{< cards cols="1">}}
{{< card subtitle="Kodin lataussivu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Napsauta **Intel (x86/64)**, jos sinulla on Intel Mac, tai **Apple Silicon** M1, M2, M3 Mac -mallille aloittaaksesi latauksen.

{{< cards cols="1">}}
{{< card subtitle="Valitse macOS-asennusohjelma" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Odota hetki, kun asennusohjelma latautuu.

{{< cards cols="1">}}
{{< card subtitle="Kodi ladattu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Latauksen jälkeen etsi `.dmg`-tiedosto **Lataukset**-kansiostasi.

{{< cards cols="1">}}
{{< card subtitle="Asenna Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Kaksoisnapsauta ladattua tiedostoa käynnistääksesi asennusohjelman.
Vedä Kodi **Ohjelmat**-kansioon asentaaksesi sen.

{{< cards cols="1">}}
{{< card title="" subtitle="Asenna Kodi vetämällä se Ohjelmiin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Käynnistä Kodi. Sinun täytyy ehkä sallia se kohdassa **Järjestelmäasetukset → Turvallisuus ja yksityisyys → Avaa joka tapauksessa**.

{{< cards cols="1">}}
{{< card subtitle="Kodin päänäkymä" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Lisää musiikkia Kodin kirjastoon

Napsauta **rataskuvaketta** (Asetukset) aloitusnäkymässä.

{{< cards cols="1">}}
{{< card subtitle="Kodin asetukset" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Siirry kohtaan **Media-asetukset → Kirjasto**. Ota käyttöön **Päivitä kirjasto käynnistettäessä** video- ja musiikkikirjastolle automaattista indeksointia varten.

{{< cards cols="1">}}
{{< card subtitle="Kirjaston asetukset" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Siirry sitten **Musiikki**-osioon ja napsauta **Lisää musiikkia**.

{{< cards cols="1">}}
{{< card subtitle="Lisää musiikkikansio" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Selaa ja valitse kansio, johon musiikkisi on tallennettu.

{{< cards cols="1">}}
{{< card subtitle="Valitse musiikin lähde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Lisää musiikin lähde Kodiin.

{{< cards cols="1">}}
{{< card subtitle="Lisää musiikin lähde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Vahvista ja anna Kodin skannata musiikkikirjastosi.

{{< cards cols="1">}}
{{< card subtitle="Vahvista musiikin lähteet" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Odota hetki, kun kirjastosi skannataan ja rakennetaan kokonaan.

{{< cards cols="1">}}
{{< card subtitle="Musiikkikirjaston skannaus" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Ota Kodin DLNA-palvelin käyttöön

Siirry kohtaan **Asetukset → Palvelut → UPnP/DLNA**.

Ota käyttöön vaihtoehto: **Jaa kirjastoni**.

Kodi toimii nyt DLNA-palvelimena paikallisessa Wi-Fi-verkossasi.

{{< cards cols="1">}}
{{< card subtitle="Ota DLNA käyttöön Kodissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Avaa Kodin kirjasto

Napsauta hiiren oikealla painikkeella sulkeaksesi asetusikkunan ja avataksesi Kodin pääkirjaston.

{{< cards cols="1">}}
{{< card title="" subtitle="Napsauta hiiren oikealla painikkeella päästäksesi Kodin kirjastoon" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Lataa musiikin suoratoistosovellus iOS:lle

Hanki ilmainen iOS DLNA -asiakassovellus, jonka avulla voit suoratoistaa musiikkia monista pilvipalveluista ja DLNA-palvelimista.

- Käytä **Evermusic**-sovellusta, jos kokoelmasi on pääasiassa MP3- ja muita standardiäänimuotoja.
- Valitse **Flacbox**, jos sinulla on korkealaatuinen musiikkikirjasto muodoissa kuten FLAC, ALAC tai DSD.

Molemmat sovellukset ovat saatavilla **iOS**:lle ja **macOS**:lle, ja ne ovat ilmaisia käyttää.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Lataa Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Lataa Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Lisää DLNA-lähde

Kun olet ladannut iOS-sovelluksen, avaa **Kaikki Yhteydet** -osio.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic-sovelluksen pääsivupalkki" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Vieritä alas ja napauta **Paikallisverkko - Saatavilla olevat laitteet** löytääksesi DLNA-palvelimia.
Tässä osiossa näet kaikki paikallisverkossasi saatavilla olevat laitteet. **Kodi DLNA -palvelimesi** pitäisi näkyä täällä. Napauta Kodi-palvelinta yhdistääksesi.

{{< cards cols="1">}}
{{< card title="" subtitle="Saatavilla olevat DLNA-laitteet Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic näyttää Kodin kautta jaetut kirjastokansiot.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodin musiikkikirjasto Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Siirry **Kappaleet**-kansioon nähdäksesi kaikki DLNA-palvelimellasi saatavilla olevat äänitiedostot.

{{< cards cols="1">}}
{{< card title="" subtitle="Kappaleet etäkansiosta" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Napauta mitä tahansa äänitiedostoa aloittaaksesi suoratoiston välittömästi.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3-tiedoston toisto Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Palaa **Yhteydet**-osioon. Lisätty DLNA-palvelin näkyy nyt täällä. Napauta sen kuvaketta yhdistääksesi milloin tahansa. Voit myös yhdistää muita pilvipalveluita tästä näkymästä samoilla vaiheilla.

Voit myös ottaa käyttöön **Last.fm-seurannan** täällä. Toistotilastot tallennetaan Last.fm-tilillesi, tarjoten henkilökohtaisia musiikkisuosituksia myöhemmin.

{{< cards cols="1">}}
{{< card title="" subtitle="Yhteydet Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Rakenna musiikkikirjasto

Sekä **Evermusic** että **Flacbox** antavat sinun lisätä musiikkia kirjastoosi ja järjestää sen **metatietotunnisteilla** kuten artistit, albumit, genret ja säveltäjät.

Aloita avaamalla **Musiikkikirjasto**-osio. Vieritä alas kohtaan **Työkalut ja asetukset** ja napauta **Lisää musiikkia**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusicin musiikkikirjasto" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Valitse musiikin lähde — tässä tapauksessa valitse **Yhteydet**.

{{< cards cols="1">}}
{{< card title="" subtitle="Lisää uutta musiikkia Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Etsi **Kodi DLNA -palvelin** Yhteyksissä ja napauta nähdäksesi kansiot ja tiedostot.

{{< cards cols="1">}}
{{< card title="" subtitle="Valitse DLNA-palvelin musiikin tuontiin" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Valitse kansiot tai tiedostot, jotka haluat lisätä, ja napauta **Valmis**.

{{< cards cols="1">}}
{{< card title="" subtitle="Valitse lisättävä musiikkikansio" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Sovellus skannaa valitsemasi tiedostot ja järjestää ne metatietojen avulla osioihin kuten Artistit, Albumit, Genret ja Säveltäjät.

{{< cards cols="1">}}
{{< card title="" subtitle="Musiikkikirjasto kategorioilla" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Luo soittolistoja

Voit myös luoda omia soittolistoja.

Avaa ensin **Soittolistat**-välilehti.

{{< cards cols="1">}}
{{< card title="" subtitle="Soittolistat-välilehti Evermusicissa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Napauta **plus (+)** -painiketta ja valitse **Uusi soittolista**.

{{< cards cols="1">}}
{{< card title="" subtitle="Luo uusi soittolista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Kirjoita soittolistan nimi ja napauta **Tallentaa**.

{{< cards cols="1">}}
{{< card title="" subtitle="Kirjoita soittolistan nimi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Valitse seuraavaksi lähde, josta lisätä kappaleita — tässä valitsemme **Kirjaston**.

{{< cards cols="1">}}
{{< card title="" subtitle="Lisää kappaleita uuteen soittolistaan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Valitse haluamasi kappaleet ja napauta **Valmis** lisätäksesi ne.

{{< cards cols="1">}}
{{< card title="" subtitle="Lisää musiikkia kirjastosta soittolistaan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Valitsemasi kappaleet näkyvät nyt luodussa soittolistassa.

{{< cards cols="1">}}
{{< card title="" subtitle="Luotu soittolista näkyy listassa" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Oletuksena kappaleet ovat saatavilla suoratoistoa varten. Kuunnellaksesi offline-tilassa, ota käyttöön **Offline-tila** — sovellus lataa kaikki soittolistan kappaleet.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline-tila käytössä soittolistalle" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Napauta **Lisää toimintoja** -painiketta tutkiaksesi lisävaihtoehtoja. Voit:

- Arkistoida soittolistan  
- Vaihtaa albumin kannen  
- Järjestää kappaleet uudelleen  
- Ja muita hyödyllisiä toimintoja

{{< cards cols="1">}}
{{< card title="" subtitle="Lisää soittolistan toimintoja saatavilla" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Yhteenveto

**Evermusic**- ja **Flacbox**-sovelluksilla iPhonen, iPadin tai Macin muuttaminen tehokkaaksi DLNA-musiikkisoittimeksi on helppoa. Tallensitpa musiikkisi pilveen, NAS-laitteelle tai kotimediapalvelimelle kuten **Kodi**, nämä sovellukset antavat sinun suoratoistaa, järjestää ja nauttia kokoelmastasi ilman rajoituksia.

- Suoratoista MP3 tai korkealaatuista FLAC suoraan **Kodi DLNA -palvelimeltasi**  
- Rakenna henkilökohtainen musiikkikirjasto ryhmiteltynä metatietojen mukaan (albumit, genret, säveltäjät)  
- Luo ja hallitse **mukautettuja soittolistoja**  
- Ota käyttöön **offline-tila** kuuntelua varten liikkeellä  
- Yhdistä **useisiin pilvipalveluihin** ja **paikallisverkon laitteisiin**  
- Seuraa kuuntelutottumuksiasi **Last.fm-integraatiolla**

Oletpa audiofiilin tai satunnainen kuuntelija, Evermusic ja Flacbox tarjoavat kaiken tarvitsemasi saumattomaan musiikin suoratoistoon ja järjestämiseen.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Lataa Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Lataa Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Aloita henkilökohtaisen musiikkikokemuksesi rakentaminen tänään.

## UKK

{{% details title="Onko Kodi ilmainen DLNA-palvelimena?" closed="true" %}}
Kyllä. Kodi on täysin ilmainen ja avoimen lähdekoodin. Se toimii macOS:ssä, Windowsissa, Linuxissa ja monissa NAS-laitteissa.
{{% /details %}}

{{% details title="Tukevatko Evermusic ja Flacbox FLAC-suoratoistoa DLNA:n kautta?" closed="true" %}}
Kyllä. Flacbox on optimoitu korkealaatuisille muodoille kuten FLAC, ALAC ja DSD. Evermusic tukee myös FLAC-toistoa MP3:n ja muiden standardimuotojen lisäksi.
{{% /details %}}

{{% details title="Voinko kuunnella offline-tilassa Kodista suoratoiston jälkeen?" closed="true" %}}
Kyllä. Ota Offline-tila käyttöön missä tahansa soittolistassa, ja sovellus lataa kaikki kappaleet laitteellesi kuuntelua varten ilman verkkoyhteyttä.
{{% /details %}}

{{% details title="Tarvitsenko premium-tilauksen DLNA:n käyttämiseen?" closed="true" %}}
Ilmaisversio tukee enintään 3 pilvi- tai verkkoyhteyttä. Premium poistaa tämän rajoituksen ja antaa sinun yhdistää rajattomasti palveluita ja DLNA-palvelimia.
{{% /details %}}

{{% details title="Täytyykö iPhoneni olla samassa Wi-Fi-verkossa kuin Kodi?" closed="true" %}}
Kyllä. DLNA-suoratoisto toimii paikallisverkon kautta. Sekä Kodi-palvelimen että iOS-laitteesi on oltava yhdistettynä samaan Wi-Fi-verkkoon.
{{% /details %}}

{{% details title="Voinko käyttää tätä asennusta NAS-laitteella Macin tai PC:n sijaan?" closed="true" %}}
Kyllä. Monet NAS-laitteet (Synology, QNAP jne.) tukevat Kodia tai niissä on oma sisäänrakennettu DLNA-palvelin. Evermusic ja Flacbox voivat yhdistää mihin tahansa standardiin DLNA/UPnP-palvelimeen.
{{% /details %}}
