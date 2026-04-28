---
title: "Ako pripojiť Synology NAS a počúvať hudbu na iPhone alebo Mac"
date: 2024-09-19
description: "Naučte sa, ako pripojiť Synology NAS pomocou natívneho API alebo QuickConnect a streamovať vysokokvalitnú hudbu na iPhone alebo Mac s Evermusic a Flacbox."
keywords: ["synology nas", "streamovanie hudby", "quickconnect", "evermusic synology", "flacbox synology", "nas hudobný prehrávač", "iphone nas hudba"]
tags: ["hudba", "streamovanie", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Zhrnutie:** Pripojte svoj Synology NAS k Evermusic alebo Flacbox pomocou natívneho API Synology -- buď manuálne cez IP adresu, alebo automaticky cez QuickConnect ID. QuickConnect vám umožňuje streamovať hudbu na diaľku bez presmerovania portov. Obe aplikácie podporujú FLAC, MP3, WAV a ďalšie hi-res formáty.

Ak hľadáte bezproblémový spôsob pripojenia Synology NAS a užívania si hudobnej knižnice na iPhone alebo Mac, aplikácie Evermusic a Flacbox sú ideálnym riešením. Tieto aplikácie podporujú širokú škálu audio formátov vrátane FLAC, MP3 a WAV, čo uľahčuje streamovanie a počúvanie vysokokvalitnej hudby priamo zo Synology NAS.

V tejto príručke vám ukážeme, ako pripojiť Synology NAS k aplikácii Evermusic alebo Flacbox pomocou natívneho API Synology a funkcie QuickConnect. Využitím priameho API Synology môžete bezpečne pristupovať k hudobnej knižnici mimo domácej siete bez potreby komplikovaných konfigurácií ako WebDAV, SMB, DLNA. S QuickConnect budete môcť streamovať a spravovať hudbu odkiaľkoľvek pomocou iPhone alebo Mac.

## Krok 1: Konfigurácia oprávnení zdieľaného priečinka (voliteľné)

1. Otvorte **Ovládací panel** a prejdite do sekcie **Zdieľaný priečinok**.

![Zdieľaný priečinok](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Vyberte priečinok **Music** a kliknite na **Upraviť**.

3. Na karte **Oprávnenia** nakonfigurujte oprávnenia. Povoľte hosťovský prístup s právami Len na čítanie, ak potrebujete len počúvať hudbu, alebo Čítanie/Zápis, ak potrebujete upravovať súbory. Uložte zmeny.

![Oprávnenia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Krok 2: Nájdite IP adresu Synology NAS

1. Otvorte **Ovládací panel** a prejdite na kartu **Sieťové rozhranie**.

![Sieťové rozhranie](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Alebo použite webový prehliadač na návštevu [find.synology.com](http://find.synology.com).

![Nájsť Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Poznačte si IP adresu vášho Synology NAS (napr. 192.168.18.137).

## Krok 3: Nájdite sieťové porty Synology NAS

Oficiálnu dokumentáciu Synology pre predvolené sieťové porty DSM nájdete v tomto [článku Centra znalostí Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM používa nasledujúce predvolené porty:
- **HTTP (Webový prístup):** Port **5000**
- **HTTPS (Zabezpečený webový prístup):** Port **5001**

Toto sú predvolené porty na prístup k rozhraniu DSM.

![Sieťové porty](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Krok 4: Povoľte funkciu QuickConnect ID

Synology QuickConnect ID je jedinečný identifikátor, ktorý vám umožňuje vzdialený prístup k Synology NAS cez internet bez potreby konfigurácie komplikovaných sieťových nastavení, ako je presmerovanie portov. QuickConnect zjednodušuje vzdialený prístup využitím serverov Synology na vytvorenie spojenia medzi NAS a vaším zariadením, ako je smartfón alebo počítač, prostredníctvom QuickConnect ID.

**Ako nájsť alebo nastaviť QuickConnect ID:**

1. **Prihláste sa do DSM.**
2. Prejdite na **Ovládací panel > Externý prístup > QuickConnect**.
3. **Povoľte QuickConnect** a vytvorte alebo zobrazte svoj jedinečný QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Krok 5: Pripojenie k Synology NAS na iPhone/Mac pomocou Evermusic alebo Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) a [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) sú hudobné prehrávače navrhnuté pre zariadenia iOS a macOS, pričom každý ponúka jedinečné funkcie a schopnosti na správu a užívanie si hudobnej knižnice.

1. Otvorte aplikáciu Evermusic alebo Flacbox a prejdite na kartu **Pripojenia**.

![Pripojenia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Vyberte **Pripojiť cloudovú službu** a zvoľte **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Máte dve možnosti pripojenia: **manuálne** pomocou IP adresy a portu servera, alebo **automatické** cez QuickConnect ID.

### Manuálne pripojenie

Pre manuálnu metódu budete potrebovať priamu IP adresu a číslo portu získané v predchádzajúcich krokoch.

1. Zadajte URL servera získanú v kroku 2 v nasledujúcom formáte: PROTOKOL://IP_ADRESA:ČÍSLO_PORTU
   - Použite **port 5000** pre HTTP a **port 5001** pre HTTPS pripojenia.

   Napríklad:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Skutočné číslo portu je možné potvrdiť v kroku 3 vášho nastavenia.
3. Zadajte **prihlasovacie meno** a **heslo** pre Synology NAS.
4. Ťuknite na **Prihlásiť sa** na vytvorenie pripojenia.

![Manuálne pripojenie](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatické pripojenie

Pre automatické pripojenie použijete **QuickConnect ID** z kroku 4. Namiesto manuálneho zadávania IP adresy a čísla portu Synology NAS jednoducho zadajte **QuickConnect ID**. Aplikácia automaticky získa potrebné informácie o pripojení.

Táto metóda vám umožňuje pristupovať k NAS na diaľku, aj mimo domácej siete, takže môžete spravovať svoje súbory z internetu bez potreby konfigurácie presmerovania portov alebo statických IP adries.

![Automatické pripojenie](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Dvojfaktorová autentifikácia

Od verzie DSM 4.2 Synology zaviedlo **dvojstupňové overenie** na zvýšenie bezpečnosti. Táto funkcia vyžaduje kód **jednorazového hesla (OTP)**, generovaný autentifikačnou aplikáciou, okrem vašich bežných prihlasovacích údajov. Ak ste povolili dvojstupňové overenie, po zadaní mena používateľa a hesla budete musieť zadať aj OTP na prihlásenie do relácie DSM.

Upozorňujeme, že po vypršaní relácie bude potrebné aplikáciu manuálne znova autorizovať. Na opätovnú autorizáciu:

1. Prejdite na kartu **Pripojenia** v aplikácii.
2. Ťuknite na tlačidlo **Viac akcií** vedľa názvu servera.
3. Vyberte **Nastavenia** z ponuky na zadanie nového autentifikačného kódu a dokončenie procesu opätovnej autorizácie.

Toto zabezpečuje, že aj keď pristupujete k NAS z nedôveryhodnej siete, vaše dáta zostanú v bezpečí.

## Krok 6: Navigácia a prehrávanie hudby

1. Po pripojení sa zariadenie zobrazí v zozname **Pripojené zariadenia**.

![Pripojené zariadenia](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Prejdite do priečinka **Music** a ťuknite na ľubovoľný audio súbor na spustenie prehrávania.

![Prehrať hudbu](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Krok 7: Pridajte pripojený cloudový priečinok do hudobnej knižnice

1. Otvorte sekciu **Hudobná knižnica** v aplikácii.
2. Vyberte **Pridať hudbu** a zvoľte **Pripojenia**.
3. Vyberte pripojený NAS server a zvoľte priečinok **Music**. Ťuknite na **Hotovo**.
4. Aplikácia prehľadá hudobný priečinok a pridá podporované audio súbory do hudobnej knižnice. Metadáta sa načítajú a vaše skladby budú zoskupené podľa albumu, interpreta a žánru.

## Záver

Podľa týchto krokov môžete jednoducho nastaviť pripojenie k Synology NAS a streamovať celú hudobnú knižnicu na iPhone alebo Mac pomocou Evermusic alebo Flacbox. Či ste doma alebo na cestách, užívajte si bezproblémový a vysokokvalitný prístup k obľúbeným skladbám odkiaľkoľvek pomocou QuickConnect. Využite flexibilitu a pohodlie, ktoré tieto aplikácie ponúkajú, a začnite jednoducho spravovať svoju hudobnú zbierku na všetkých zariadeniach.

S bezpečným vzdialeným prístupom cez QuickConnect a podporou širokej škály audio formátov nikdy nebudete ďaleko od svojej hudby. Teraz sú vaše súbory uložené na NAS len na jedno ťuknutie!

## FAQ

{{% details title="Aký je rozdiel medzi manuálnym pripojením a QuickConnect?" closed="true" %}}
Manuálne pripojenie používa IP adresu a port NAS, čo funguje vo vašej lokálnej sieti. QuickConnect používa službu prenosu Synology na vytvorenie pripojenia odkiaľkoľvek cez internet bez presmerovania portov.
{{% /details %}}

{{% details title="Môžem streamovať hudbu zo Synology NAS mimo domácej siete?" closed="true" %}}
Áno. Povoľte QuickConnect na Synology NAS a použite QuickConnect ID v Evermusic alebo Flacbox na streamovanie hudby odkiaľkoľvek s internetovým pripojením.
{{% /details %}}

{{% details title="Aké audio formáty sú podporované pri streamovaní zo Synology NAS?" closed="true" %}}
Evermusic a Flacbox podporujú FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD a mnoho ďalších formátov. Všetky podporované formáty fungujú pri streamovaní zo Synology NAS.
{{% /details %}}

{{% details title="Potrebujem dvojfaktorovú autentifikáciu na pripojenie?" closed="true" %}}
Nie, 2FA je voliteľná. Ak ste však povolili dvojstupňové overenie na Synology DSM, aplikácia si vyžiada jednorazové heslo pri prihlásení. Po vypršaní relácie budete musieť znova autorizovať.
{{% /details %}}

{{% details title="Mám použiť natívne API Synology, WebDAV alebo SMB na pripojenie?" closed="true" %}}
Natívne API Synology s QuickConnect je najlepšou voľbou pre vzdialený prístup. Pre použitie v lokálnej sieti je SMB zvyčajne najrýchlejšou možnosťou. WebDAV funguje dobre pre lokálny aj vzdialený prístup. Evermusic a Flacbox podporujú všetky tri protokoly.
{{% /details %}}
