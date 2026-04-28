---
title: "Kako spojiti NAS pohranu pomoću WebDAV-a i slušati glazbu na iPhoneu ili Macu"
date: 2024-07-28
description: "Naučite kako konfigurirati WebDAV na vašem Synology NAS-u i streamati glazbu na iPhone ili Mac koristeći Evermusic ili Flacbox. Slijedite naš vodič korak po korak."
keywords: ["spojiti nas", "webdav synology", "streamati glazbu nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["glazba", "streaming", "pohrana", "nas", "spojiti", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Ukratko:** Instalirajte i omogućite WebDAV na vašem Synology NAS-u, konfigurirajte dozvole dijeljene mape, zatim se povežite iz Evermusica ili Flacboxa koristeći IP adresu NAS-a i WebDAV port (zadano 5005/5006). Možete streamati i upravljati cijelom glazbenom bibliotekom bez kopiranja datoteka na uređaj.

Otkrijte kako spojiti vašu NAS pohranu pomoću WebDAV-a i bez napora streamati glazbenu biblioteku na iPhone ili Mac. WebDAV (Web-based Distributed Authoring and Versioning) je protokol koji vam omogućuje upravljanje i dijeljenje datoteka putem interneta. Postavljanjem WebDAV-a na vašem NAS-u, možete pristupiti i streamati svoju glazbenu kolekciju, osiguravajući da su vaše omiljene pjesme uvijek nadohvat ruke.

U ovom vodiču pokazat ćemo vam kako postaviti WebDAV vezu na jednom od najpopularnijih NAS poslužitelja, Synology NAS-u. Slijedite naše jednostavne korake za konfiguraciju WebDAV-a na vašem Synology NAS-u i moći ćete pregledavati, streamati i upravljati glazbenom bibliotekom izravno s iPhonea ili Maca.

## Korak 1: Instaliranje WebDAV-a na Synology NAS

1. Prijavite se na Synology NAS i otvorite **Centar za pakete**.
2. Potražite "webdav" i instalirajte WebDAV paket ako još nije instaliran. Otvorite WebDAV poslužitelj za konfiguraciju.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instaliranje WebDAV-a na Synology" width="600" >}}

## Korak 2: Konfiguriranje WebDAV poslužitelja

1. Na stranici WebDAV postavki označite potvrdne okvire za **Omogući HTTP**, **Omogući HTTPS**, **Omogući anonimni WebDAV** i **Omogući DavDepthInfinity**.
2. Kliknite **Primijeni** za spremanje promjena. Zabilježite brojeve portova za HTTP i HTTPS veze, koji su zadano 5005 i 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfiguriranje WebDAV postavki" width="600" >}}

## Korak 3: Konfiguriranje dozvola dijeljene mape

1. Otvorite **Upravljačku ploču** i idite na odjeljak **Dijeljena mapa**.
2. Odaberite mapu **Glazba** i kliknite **Uredi**.
3. Na kartici **Dozvole** konfigurirajte dozvole. Omogućite pristup gostu s Samo za čitanje ako samo trebate slušati glazbu, ili Čitanje/Pisanje ako trebate mijenjati datoteke. Spremite promjene.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Dozvole dijeljene mape" width="600" >}}

## Korak 4: Pronalaženje IP adrese Synology NAS-a

1. Otvorite **Upravljačku ploču** i idite na karticu **Mrežno sučelje**, ili koristite web preglednik za posjet [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Pronalaženje IP adrese NAS-a" width="600" >}}

2. Zabilježite IP adresu vašeg Synology NAS-a (npr. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="IP adresa Synology NAS-a" width="600" >}}

## Korak 5: Povezivanje na Synology NAS pomoću Evermusica/Flacboxa

1. Otvorite aplikaciju Evermusic ili Flacbox i idite na karticu **Povezivanja**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Kartica Povezivanja u Evermusicu" width="600" >}}

2. Za automatsko povezivanje pronađite Synology NAS u odjeljku **Dostupni uređaji** i dodirnite ga za povezivanje.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Popis dostupnih uređaja" width="600" >}}

3. Za ručno povezivanje odaberite **Poveži oblačnu uslugu** i odaberite **WebDAV**. Unesite adresu poslužitelja u formatu: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (npr. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ručna konfiguracija WebDAV-a" width="600" >}}

4. Ostavite polja za prijavu i lozinku prazna za pristup gostu, ili unesite svoje Synology vjerodajnice. Dodirnite **Prijava**.

## Korak 6: Navigacija i reprodukcija glazbe

1. Nakon povezivanja, uređaj će se pojaviti na popisu **Povezani dodaci**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Povezani uređaji u Evermusicu" width="600" >}}

2. Navigirajte do mape **Glazba** i dodirnite bilo koju audio datoteku za pokretanje reprodukcije.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Pregledavanje mape s glazbom" width="600" >}}

## Korak 7: Dodavanje povezane oblačne mape u glazbenu biblioteku

1. Otvorite odjeljak **Glazbena biblioteka** u aplikaciji.
2. Odaberite **Dodaj glazbu** i odaberite **Povezivanja**.
3. Odaberite svoj povezani NAS poslužitelj i odaberite mapu **Glazba**. Dodirnite **Završeno**.
4. Aplikacija će skenirati glazbenu mapu i dodati podržane audio datoteke u glazbenu biblioteku. Metapodaci će se učitati, a vaše skladbe bit će grupirane po albumu, izvođaču i žanru.

## Zaključak

Slijedeći ove korake, možete jednostavno postaviti WebDAV vezu na vašem Synology NAS-u i streamati glazbenu biblioteku na iPhone ili Mac koristeći Evermusic ili Flacbox. Uživajte u besprijekornom pristupu vašim omiljenim pjesmama u bilo koje vrijeme.

## Česta pitanja

{{% details title="Koji NAS uređaji podržavaju WebDAV?" closed="true" %}}
Većina popularnih NAS brendova podržava WebDAV, uključujući Synology, QNAP, TrueNAS i Western Digital. Provjerite dokumentaciju proizvođača vašeg NAS-a za upute za postavljanje WebDAV-a.
{{% /details %}}

{{% details title="Koja je razlika između WebDAV-a i SMB-a za streaming glazbe s NAS-a?" closed="true" %}}
WebDAV radi preko HTTP/HTTPS i bolje je prilagođen za udaljeni pristup putem interneta. SMB je obično brži na lokalnim mrežama. Evermusic i Flacbox podržavaju oba protokola, pa odaberite ovisno o tome trebate li lokalni ili udaljeni pristup.
{{% /details %}}

{{% details title="Trebam li korisničko ime i lozinku za WebDAV na Synologyju?" closed="true" %}}
Ne, ako omogućite anonimni WebDAV pristup i konfigurirate dozvole gosta na dijeljenoj mapi. Za bolju sigurnost možete koristiti svoje Synology vjerodajnice.
{{% /details %}}

{{% details title="Mogu li streamati FLAC i druge formate visoke rezolucije s NAS-a putem WebDAV-a?" closed="true" %}}
Da. I Evermusic i Flacbox podržavaju FLAC, ALAC, WAV, DSD i druge formate visoke rezolucije pri streamanju s NAS pohrane putem WebDAV-a.
{{% /details %}}

{{% details title="Zašto aplikacija ne može pronaći moj NAS u Dostupnim uređajima?" closed="true" %}}
Provjerite da su vaš iPhone/Mac i NAS na istoj Wi-Fi mreži. Ako automatsko otkrivanje ne radi, koristite opciju ručnog povezivanja i izravno unesite IP adresu NAS-a i WebDAV port.
{{% /details %}}
