---
title: "Kuinka yhdistää Bluesound VAULTin sisäinen tallennustila Evermusicista, Flacboxista, Evertagista"
date: 2022-03-10
description: "Opi, miten pääset käsiksi Bluesound VAULTin sisäiseen kiintolevyyn Evermusicista, Flacboxista ja Evertagista SMB-protokollan avulla äänitiedostojen hallintaan, muokkaamiseen ja toistamiseen."
keywords: ["bluesound vault", "yhdistä smb-tallennustila", "evermusic smb", "flacbox vault", "evertag smb", "nas-tallennustila musiikki", "vault sisäinen asema"]
tags: ["evermusic", "yhdistä", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Yhteenveto:** Yhdistä Bluesound VAULTin sisäiseen tallennustilaan SMB:n kautta käyttämällä Evermusicia, Flacboxia tai Evertagia. Etsi VAULTin IP-osoite BluOS-sovelluksesta, syötä se SMB-yhteytenä vieraskäyttöoikeudella ja aloita musiikkitiedostojesi toistaminen tai hallinta.

Bluesound VAULTissa on sisäinen kiintolevy ja se toimii verkkoon liitettynä tallennustilana (NAS). Pääsy VAULTin sisäiselle kiintolevylle mahdollistaa tiedostojen lisäämisen/poistamisen ja metatietotunnisteiden muokkaamisen sovelluksistamme Evermusic, Flacbox, Evertag.

**Seuraavat ovat vaiheet VAULTin sisäiselle kiintolevylle pääsemiseksi:**

1. Valitse BluOS-sovelluksessa **Ohje > Diagnostiikka**.

2. Hanki **Diagnostiikka**-sivulta VAULTin **IP-osoite**. Tätä **IP-osoitetta** käytetään seuraavissa vaiheissa.

3. Avaa Evermusic, Flacbox tai Evertag.

   ![Everappz-sovellukset](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Avaa "Yhteydet"-näyttö ja valitse valikosta "Yhdistä pilvipalvelu".

   ![Evermusic Yhteydet-näyttö](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Valitse "SMB"-pilvipalvelu.

   ![Evermusic Yhdistä pilvipalvelu -näyttö](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Syötä "SMB-määritysnäytöllä" URL seuraavassa muodossa:

   ```
   SMB://<<VAULT-IP>>
   ```

   Korvaa `<<VAULT-IP>>` vaiheessa 2 saadulla **IP-osoitteella**.

   **Huomautus:** Jätä Kirjautumistunnus- ja Salasana-kentät tyhjiksi, koska VAULT-tallennustila tukee VIERAS-tilaa.

   ![Evermusic SMB-yhteysnäyttö](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Napauta "Kirjaudu sisään" -painiketta tallentaaksesi asetukset.

8. Avaa yhdistetty pilvitallennustila, siirry äänitiedostojen kansioon ja napauta mitä tahansa tiedostoa käynnistääksesi äänisoittimen.

   ![Evermusic Avattu SMB-palvelin-näyttö](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Voit myös muokata tiedostoja sisäänrakennetun tiedostonhallinnan avulla.

   ![Evermusic Tiedostonhallintanäyttö](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Näillä yksinkertaisilla vaiheilla voit vaivattomasti käyttää Bluesound VAULTin sisäistä kiintolevyä ja hallita musiikkikirjastoasi Evermusicin, Flacboxin tai Evertagin avulla.

## UKK

{{% details title="Tarvitsenko käyttäjätunnuksen ja salasanan yhdistääkseni Bluesound VAULTiin?" closed="true" %}}
Ei. Bluesound VAULT tukee vieraskäyttöä (anonyymiä) SMB:n kautta. Jätä Kirjautumistunnus- ja Salasana-kentät tyhjiksi yhteyden määrittämisen yhteydessä.
{{% /details %}}

{{% details title="Voinko muokata musiikkitunnisteita Bluesound VAULTissa?" closed="true" %}}
Kyllä. Evertag-sovelluksella voit muokata metatietotunnisteita (nimi, esittäjä, albumi jne.) suoraan VAULTin sisäiselle kiintolevylle tallennetuista äänitiedostoista.
{{% /details %}}

{{% details title="Mitä protokollia Bluesound VAULT tukee?" closed="true" %}}
Bluesound VAULT tarjoaa sisäisen tallennustilansa SMB:n (Server Message Block) kautta. Evermusic, Flacbox ja Evertag tukevat kaikki SMB-yhteyksiä, mikä tekee yhdistämisestä helppoa.
{{% /details %}}

{{% details title="Voinko suoratoistaa musiikkia VAULTista kopioimatta tiedostoja iPhoneen?" closed="true" %}}
Kyllä. Kun olet yhdistänyt SMB:n kautta, voit suoratoistaa äänitiedostoja suoraan VAULTin sisäiseltä asemalta kopioimatta niitä laitteeseesi.
{{% /details %}}
