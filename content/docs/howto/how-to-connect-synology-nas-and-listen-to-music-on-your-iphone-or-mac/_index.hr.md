---
title: "Kako povezati Synology NAS i slušati glazbu na iPhoneu ili Macu"
date: 2024-09-19
description: "Naučite kako povezati Synology NAS koristeći nativni API ili QuickConnect i streamati visokokvalitetnu glazbu na iPhone ili Mac s Evermusic i Flacbox."
keywords: ["synology nas", "streamanje glazbe", "quickconnect", "evermusic synology", "flacbox synology", "nas glazbeni player", "iphone nas glazba"]
tags: ["glazba", "streamanje", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Sažetak:** Povežite svoj Synology NAS s Evermusic ili Flacbox koristeći Synologyjev nativni API -- ručno putem IP adrese ili automatski putem QuickConnect ID-a. QuickConnect vam omogućuje streamanje glazbe na daljinu bez prosljeđivanja portova. Obje aplikacije podržavaju FLAC, MP3, WAV i druge hi-res formate.

Ako tražite besprijekoran način za povezivanje vašeg Synology NAS-a i uživanje u glazbenoj biblioteci na iPhoneu ili Macu, aplikacije Evermusic i Flacbox savršena su rješenja. Ove aplikacije podržavaju širok raspon audio formata, uključujući FLAC, MP3 i WAV, što olakšava streamanje i slušanje visokokvalitetne glazbe izravno s vašeg Synology NAS-a.

U ovom vodiču pokazat ćemo vam kako povezati Synology NAS s aplikacijom Evermusic ili Flacbox koristeći Synologyjev nativni API i QuickConnect značajku. Korištenjem Synologyjevog izravnog API-ja možete sigurno pristupiti svojoj glazbenoj biblioteci izvan kućne mreže bez potrebe za kompliciranim konfiguracijama poput WebDAV, SMB, DLNA. S QuickConnectom moći ćete streamati i upravljati svojom glazbom s bilo kojeg mjesta, koristeći svoj iPhone ili Mac.

## Korak 1: Konfiguriranje dozvola dijeljene mape (opcionalno)

1. Otvorite **Upravljačku ploču** i idite na odjeljak **Dijeljena mapa**.

![Dijeljena mapa](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Odaberite mapu **Glazba** i kliknite **Uredi**.

3. Na kartici **Dozvole** konfigurirajte dozvole. Omogućite pristup gostima sa samo čitanjem ako samo trebate slušati glazbu, ili čitanje/pisanje ako trebate mijenjati datoteke. Spremite promjene.

![Dozvole](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Korak 2: Pronađite IP adresu Synology NAS-a

1. Otvorite **Upravljačku ploču** i idite na karticu **Mrežno sučelje**.

![Mrežno sučelje](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Ili koristite web preglednik za posjet [find.synology.com](http://find.synology.com).

![Pronađi Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Zabilježite IP adresu vašeg Synology NAS-a (npr. 192.168.18.137).

## Korak 3: Pronađite mrežne portove Synology NAS-a

Možete pronaći službenu Synology dokumentaciju za zadane mrežne portove DSM-a u ovom [članku Synology centra znanja](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM koristi sljedeće zadane portove:
- **HTTP (Web pristup):** Port **5000**
- **HTTPS (Siguran web pristup):** Port **5001**

To su zadani portovi za pristup DSM sučelju.

![Mrežni portovi](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Korak 4: Omogućite značajku QuickConnect ID

Synology QuickConnect ID jedinstven je identifikator koji vam omogućuje daljinski pristup Synology NAS-u putem interneta bez potrebe za konfiguriranjem kompliciranih mrežnih postavki poput prosljeđivanja portova. QuickConnect pojednostavljuje daljinski pristup korištenjem Synologyjevih poslužitelja za uspostavljanje veze između vašeg NAS-a i vašeg uređaja, poput pametnog telefona ili računala, putem QuickConnect ID-a.

**Kako pronaći ili postaviti vaš QuickConnect ID:**

1. **Prijavite se u DSM.**
2. Idite na **Upravljačka ploča > Vanjski pristup > QuickConnect**.
3. **Omogućite QuickConnect** i stvorite ili pogledajte svoj jedinstveni QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Korak 5: Povežite se sa Synology NAS-om na iPhoneu/Macu koristeći Evermusic ili Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) i [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) su aplikacije za reprodukciju glazbe dizajnirane za iOS i macOS uređaje, svaka nudeći jedinstvene značajke i mogućnosti za upravljanje i uživanje u vašoj glazbenoj biblioteci.

1. Otvorite aplikaciju Evermusic ili Flacbox i idite na karticu **Povezivanja**.

![Povezivanja](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Odaberite **Poveži oblak uslugu** i odaberite **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Imate dvije opcije povezivanja: **ručno** koristeći IP adresu i port poslužitelja, ili **automatski** putem QuickConnect ID-a.

### Ručno povezivanje

Za ručnu metodu trebat ćete izravnu IP adresu i broj porta koji ste dobili u prethodnim koracima.

1. Unesite URL poslužitelja koji ste dobili u koraku 2, koristeći sljedeći format: PROTOKOL://IP_ADRESA:BROJ_PORTA
   - Koristite **port 5000** za HTTP i **port 5001** za HTTPS veze.

   Na primjer:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Stvarni broj porta može se potvrditi u koraku 3 vaše postavke.
3. Unesite svoju **prijavu** i **lozinku** za Synology NAS.
4. Dodirnite **Prijava** za uspostavljanje veze.

![Ručno povezivanje](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatsko povezivanje

Za automatsko povezivanje koristit ćete **QuickConnect ID** iz koraka 4. Umjesto ručnog unosa IP adrese i broja porta vašeg Synology NAS-a, jednostavno unesite **QuickConnect ID**. Aplikacija će automatski dohvatiti potrebne informacije o vezi.

Ova metoda omogućuje pristup vašem NAS-u na daljinu, čak i izvan kućne mreže, tako da možete upravljati svojim datotekama s interneta bez potrebe za konfiguriranjem prosljeđivanja portova ili statičkih IP adresa.

![Automatsko povezivanje](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Dvofaktorska autentifikacija

Počevši od DSM 4.2, Synology je uveo **verifikaciju u 2 koraka** za poboljšanje sigurnosti. Ova značajka zahtijeva kod **jednokratne lozinke (OTP)**, generiran od strane aplikacije za autentifikaciju, uz vaše redovne vjerodajnice za prijavu. Ako ste omogućili verifikaciju u 2 koraka, nakon unosa korisničkog imena i lozinke, trebat ćete unijeti i OTP za prijavu u DSM sesiju.

Imajte na umu da nakon isteka sesije, aplikacija će morati biti ručno reautorizirana. Za reautorizaciju:

1. Idite na karticu **Povezivanja** u aplikaciji.
2. Dodirnite gumb **Više radnji** pokraj naziva poslužitelja.
3. Odaberite **Postavke** iz izbornika za unos novog koda za autentifikaciju i dovršetak procesa reautorizacije.

To osigurava da čak i ako pristupate NAS-u s nepouzdane mreže, vaši podaci ostaju sigurni.

## Korak 6: Pregledavanje i reprodukcija glazbe

1. Nakon povezivanja, uređaj će se pojaviti na popisu **Povezani uređaji**.

![Povezani uređaji](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navigirajte do mape **Glazba** i dodirnite bilo koju audio datoteku za pokretanje reprodukcije.

![Reprodukcija glazbe](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Korak 7: Dodajte povezanu oblak mapu u glazbenu biblioteku

1. Otvorite odjeljak **Glazbena biblioteka** u aplikaciji.
2. Odaberite **Dodaj glazbu** i odaberite **Povezivanja**.
3. Odaberite povezani NAS poslužitelj i odaberite mapu **Glazba**. Dodirnite **Završeno**.
4. Aplikacija će skenirati glazbenu mapu i dodati podržane audio datoteke u glazbenu biblioteku. Metapodaci će biti učitani, a vaše će se pjesme grupirati po albumu, izvođaču i žanru.

## Zaključak

Slijedeći ove korake, možete lako postaviti vezu na svom Synology NAS-u i streamati cijelu glazbenu biblioteku na iPhone ili Mac koristeći Evermusic ili Flacbox. Bilo da ste kod kuće ili u pokretu, uživajte u besprijekornom, visokokvalitetnom pristupu vašim omiljenim pjesmama s bilo kojeg mjesta koristeći QuickConnect. Iskoristite fleksibilnost i praktičnost koju ove aplikacije nude i počnite upravljati svojom glazbenom kolekcijom s lakoćom na svim uređajima.

Sa sigurnim daljinskim pristupom putem QuickConnect-a i podrškom za širok raspon audio formata, nikada nećete biti daleko od svoje glazbe. Sada su vaše datoteke pohranjene na NAS-u samo jedan dodir daleko!

## Često postavljana pitanja

{{% details title="Koja je razlika između ručnog povezivanja i QuickConnect-a?" closed="true" %}}
Ručno povezivanje koristi IP adresu i port NAS-a, što funkcionira na vašoj lokalnoj mreži. QuickConnect koristi Synologyjevu relay uslugu za uspostavljanje veze s bilo kojeg mjesta putem interneta, bez prosljeđivanja portova.
{{% /details %}}

{{% details title="Mogu li streamati glazbu sa Synology NAS-a izvan kućne mreže?" closed="true" %}}
Da. Omogućite QuickConnect na svom Synology NAS-u i koristite QuickConnect ID u Evermusicju ili Flacboxu za streamanje glazbe s bilo kojeg mjesta s internetskom vezom.
{{% /details %}}

{{% details title="Koji audio formati su podržani pri streamanju sa Synology NAS-a?" closed="true" %}}
Evermusic i Flacbox podržavaju FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD i mnoge druge formate. Svi podržani formati rade pri streamanju sa Synology NAS-a.
{{% /details %}}

{{% details title="Trebam li dvofaktorsku autentifikaciju za povezivanje?" closed="true" %}}
Ne, dvofaktorska autentifikacija je opcionalna. Međutim, ako ste omogućili verifikaciju u 2 koraka na svom Synology DSM-u, aplikacija će zatražiti jednokratnu lozinku tijekom prijave. Trebat ćete reautorizirati kada sesija istekne.
{{% /details %}}

{{% details title="Trebam li koristiti Synology nativni API, WebDAV ili SMB za povezivanje?" closed="true" %}}
Synology nativni API s QuickConnect-om najbolji je izbor za daljinski pristup. Za korištenje lokalne mreže, SMB je obično najbrža opcija. WebDAV dobro funkcionira za lokalni i daljinski pristup. Evermusic i Flacbox podržavaju sva tri protokola.
{{% /details %}}
