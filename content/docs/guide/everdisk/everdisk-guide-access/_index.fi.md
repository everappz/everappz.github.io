---
title: "Kaytto ja yksityisyys"
date: 2026-08-20
description: "Pida Everdisk-jakamisesi turvallisena: suojaa paasy kayttajatunnuksella ja salasanalla, hallitse voivatko yhdistetyt laitteet lahettaa, nimeta uudelleen ja poistaa Tiedostojen muokkaus -asetuksella, esta tuntemattomat laitteet, valitse roskakori vai pysyva poisto ja ymmarra, miksi kaikki pysyy paikallisverkossasi."
keywords: ["Everdisk salasanasuojaus", "tiedostojen muokkaus kytkin", "esta laite", "estetyt laitteet", "poista tiedostot pysyvasti", "vain paikallisverkko", "yksityinen tiedostojen jako", "DLNA ei salasanaa", "verkon turvallisuus"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk pitaa tiedostosi omassa verkossasi ja antaa sinulle yksinkertaiset saatimet siihen, kuka voi paasta niihin ja mita he voivat tehda. Loydat nama saatimet kohdasta **Asetukset -> Jakaminen -> Kaytto** seka muutaman niihin liittyvan asetuksen Tiedostonhallinnasta.

## Suojaa paasy kayttajatunnuksella ja salasanalla

Oletuksena kuka tahansa samassa verkossa oleva, jolla on osoitteesi, voi avata jaetut tiedostosi. Vaatiaksesi sisaankirjautumisen:

1. Siirry kohtaan **Asetukset -> Jakaminen -> Kaytto**.
2. Syota **Kayttajatunnus** ja **Salasana**.
3. Nyt **Selain (HTTP)**-, **Tietokone (WebDAV)**- ja **Muut sovellukset ja laitteet (FTP)** -yhteydet kysyvat nama tiedot ennen kuin ne nayttavat tiedostosi.

Jata molemmat kentat tyhjiksi avointa paasya varten. Salasanasi tallennetaan turvallisesti laitteen Keychainiin.

> **DLNA on aina avoin.** TV ja mediakeskus (DLNA) -yhteytta ei voi suojata salasanalla, joten kun se on paalla, mika tahansa samassa Wi-Fi-verkossa oleva laite voi selata jaettua mediaasi. Kytke se pois paalta, jos haluat vain suojattuja yhteyksia, ja jaa vain verkoissa, joihin luotat.

## Salli tai esta muokkaus (Tiedostojen muokkaus)

**Tiedostojen muokkaus** -kytkin maaraa, voivatko yhdistetyt laitteet vain katsoa tiedostojasi vai myos muuttaa niita.

- **Paalla** (oletus): yhdistetyt laitteet voivat **lahettaa, nimeta uudelleen ja poistaa** jaettuja tiedostojasi - joten laitteesi toimii kuin oikea kaksisuuntainen verkkoasema.
- **Pois**: jaetut tiedostosi ovat **vain luku**. Muut voivat katsoa ja ladata, mutta eivat voi lisata tai muuttaa mitaan.

Sen kytkeminen paalle nayttaa lyhyen varoituksen, koska se antaa muiden muokata tiedostojasi. Silla on **Tarkea**-merkinta ollessaan paalla.

## Esta laite

Jos naet laitteen, jota et tunnista:

1. Etsi se Jakaminen-naytolta kohdasta **Kuka on yhdistettyna**.
2. Napauta sen lisaa toimintoja -painiketta ja valitse **Esta tama laite**.

Estetyt laitteet on listattu kohdassa **Asetukset -> Jakaminen -> Kaytto -> Estetyt laitteet**, jossa voit **poistaa eston** yhdesta tai valita **Poista kaikki estot**. Esto seuraa laitetta, vaikka sen verkko-osoite muuttuisi (Selain-, Tietokone- ja TV-yhteyksien osalta).

## Roskakori vs. pysyva poisto

Kun tiedosto poistetaan - joko sinun toimestasi tiedostonhallinnassa tai yhdistetyn laitteen toimesta - se menee normaalisti palautettavaan **roskakoriin**, jotta voit saada sen takaisin.

Jos haluat tiedostojen poistuvan valittomasti ilman palautusmahdollisuutta, ota kayttoon **Poista tiedostot pysyvasti** kohdassa **Asetukset -> Tiedostonhallinta -> Tiedostojen poisto**. Tama on oletuksena pois paalta. **Se vaikuttaa laitteen tiedostonhallintaan** ja **verkon yli tehtyihin poistoihin**; se ei muuta sita, miten jarjestelman Kuvat-kirjasto tai Musiikki-kirjasto kasittelevat poistoa.

## Kaikki pysyy paikallisena

Everdisk jakaa vain **paikallisverkkosi** yli - mitaan ei ladata internetiin eika valissa ole pilvitilia. Muutama asia kannattaa tietaa:

- Everdisk tarvitsee iOS:n **Paikallisverkko**-luvan, jotta lahella olevat laitteet loytavat sen. Jos tama lupa on pois paalta, huomautus selittaa, miten sen saa takaisin paalle iOS-asetuksissa.
- Parhaan yksityisyyden saavuttamiseksi jaa vain ollessasi **koti- tai yksityisessa Wi-Fi-verkossa**, johon luotat, ja ole varovainen julkisessa Wi-Fissa. Kayttajatunnus ja salasana auttavat, mutta ne eivat korvaa luotettavaa verkkoa.
- **Kaikkein yksityisin vaihtoehto on USB-kaapeli Maciin** - data kulkee suoraan kaapelin kautta eika koskaan kulje reitittimen tai internetin lapi. Katso [Yhdista laitteesi](/docs/guide/everdisk/everdisk-guide-connect).

## Seuraavat vaiheet

- [Jakaminen](/docs/guide/everdisk/everdisk-guide-sharing) - valitse mita jaat ja aloita jakaminen.
- [Asetukset](/docs/guide/everdisk/everdisk-guide-settings) - kaikki Kaytto- ja Tiedostonhallinta-asetukset yhdessa paikassa.
