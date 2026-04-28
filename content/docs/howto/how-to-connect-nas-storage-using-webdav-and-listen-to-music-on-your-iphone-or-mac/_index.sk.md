---
title: "Ako pripojiť úložisko NAS pomocou WebDAV a počúvať hudbu na iPhone alebo Mac"
date: 2024-07-28
description: "Naučte sa, ako nakonfigurovať WebDAV na vašom Synology NAS a streamovať hudbu na iPhone alebo Mac pomocou Evermusic alebo Flacbox. Postupujte podľa nášho podrobného sprievodcu."
keywords: ["pripojiť nas", "webdav synology", "streamovať hudbu nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["hudba", "streamovanie", "úložisko", "nas", "pripojenie", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Zhrnutie:** Nainštalujte a povoľte WebDAV na vašom Synology NAS, nakonfigurujte oprávnenia zdieľaného priečinka a potom sa pripojte z Evermusic alebo Flacbox pomocou IP adresy NAS a portu WebDAV (predvolené 5005/5006). Môžete streamovať a spravovať celú hudobnú knižnicu bez kopírovania súborov do zariadenia.

Zistite, ako pripojiť úložisko NAS pomocou WebDAV a jednoducho streamovať hudobnú knižnicu na iPhone alebo Mac. WebDAV (Web-based Distributed Authoring and Versioning) je protokol, ktorý vám umožňuje spravovať a zdieľať súbory cez internet. Nastavením WebDAV na vašom NAS môžete pristupovať k svojej hudobnej zbierke a streamovať ju, takže budete mať svoje obľúbené skladby vždy na dosah.

V tomto sprievodcovi vám ukážeme, ako nastaviť pripojenie WebDAV na jednom z najpopulárnejších serverov NAS, Synology NAS. Postupujte podľa našich jednoduchých krokov na konfiguráciu WebDAV na vašom Synology NAS a budete môcť prehliadať, streamovať a spravovať svoju hudobnú knižnicu priamo z iPhone alebo Mac.

## Krok 1: Inštalácia WebDAV na Synology NAS

1. Prihláste sa do svojho Synology NAS a otvorte **Centrum balíkov**.
2. Vyhľadajte "webdav" a nainštalujte balík WebDAV, ak ešte nie je nainštalovaný. Otvorte server WebDAV na jeho konfiguráciu.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Inštalácia WebDAV na Synology" width="600" >}}

## Krok 2: Konfigurácia servera WebDAV

1. Na stránke nastavení WebDAV zaškrtnite políčka **Povoliť HTTP**, **Povoliť HTTPS**, **Povoliť anonymný WebDAV** a **Povoliť DavDepthInfinity**.
2. Kliknite na **Použiť** na uloženie zmien. Poznačte si čísla portov pre pripojenia HTTP a HTTPS, ktoré sú predvolene 5005 a 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurácia nastavení WebDAV" width="600" >}}

## Krok 3: Konfigurácia oprávnení zdieľaného priečinka

1. Otvorte **Ovládací panel** a prejdite do sekcie **Zdieľaný priečinok**.
2. Vyberte priečinok **Hudba** a kliknite na **Upraviť**.
3. Na karte **Oprávnenia** nakonfigurujte oprávnenia. Povoľte prístup hosťa s oprávnením Len na čítanie, ak potrebujete len počúvať hudbu, alebo Čítanie/Zápis, ak potrebujete upravovať súbory. Uložte zmeny.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Oprávnenia zdieľaného priečinka" width="600" >}}

## Krok 4: Zistenie IP adresy Synology NAS

1. Otvorte **Ovládací panel** a prejdite na kartu **Sieťové rozhranie** alebo použite webový prehliadač na návštevu [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Zistenie IP adresy NAS" width="600" >}}

2. Poznačte si IP adresu vášho Synology NAS (napr. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="IP adresa Synology NAS" width="600" >}}

## Krok 5: Pripojenie k Synology NAS pomocou Evermusic/Flacbox

1. Otvorte aplikáciu Evermusic alebo Flacbox a prejdite na kartu **Pripojenia**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Karta Pripojenia v Evermusic" width="600" >}}

2. Pre automatické pripojenie nájdite svoj Synology NAS v sekcii **Dostupné zariadenia** a ťuknutím sa pripojte.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Zoznam dostupných zariadení" width="600" >}}

3. Pre ručné pripojenie vyberte **Pripojiť cloudovú službu** a zvoľte **WebDAV**. Zadajte adresu servera vo formáte: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (napr. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ručná konfigurácia WebDAV" width="600" >}}

4. Pre prístup hosťa nechajte polia pre prihlásenie a heslo prázdne, alebo zadajte svoje prihlasovacie údaje Synology. Ťuknite na **Prihlásiť sa**.

## Krok 6: Navigácia a prehrávanie hudby

1. Po pripojení sa zariadenie zobrazí v zozname **Pripojené príslušenstvo**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Pripojené zariadenia v Evermusic" width="600" >}}

2. Prejdite do priečinka **Hudba** a ťuknite na ľubovoľný zvukový súbor na spustenie prehrávania.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Prehliadanie priečinka s hudbou" width="600" >}}

## Krok 7: Pridanie pripojeného cloudového priečinka do hudobnej knižnice

1. Otvorte sekciu **Hudobná knižnica** v aplikácii.
2. Vyberte **Pridať hudbu** a zvoľte **Pripojenia**.
3. Vyberte pripojený server NAS a zvoľte priečinok **Hudba**. Ťuknite na **Hotovo**.
4. Aplikácia prehľadá hudobný priečinok a pridá podporované zvukové súbory do hudobnej knižnice. Načítajú sa metadáta a vaše skladby sa zoskupia podľa albumu, interpreta a žánru.

## Záver

Podľa týchto krokov môžete jednoducho nastaviť pripojenie WebDAV na vašom Synology NAS a streamovať hudobnú knižnicu na iPhone alebo Mac pomocou Evermusic alebo Flacbox. Užite si bezproblémový prístup k obľúbeným skladbám kedykoľvek.

## Často kladené otázky

{{% details title="Ktoré zariadenia NAS podporujú WebDAV?" closed="true" %}}
Väčšina populárnych značiek NAS podporuje WebDAV, vrátane Synology, QNAP, TrueNAS a Western Digital. Skontrolujte dokumentáciu výrobcu vášho NAS pre pokyny na nastavenie WebDAV.
{{% /details %}}

{{% details title="Aký je rozdiel medzi WebDAV a SMB pre streamovanie hudby z NAS?" closed="true" %}}
WebDAV funguje cez HTTP/HTTPS a je vhodnejší pre vzdialený prístup cez internet. SMB je zvyčajne rýchlejší v lokálnych sieťach. Evermusic a Flacbox podporujú oba protokoly, takže si vyberte podľa toho, či potrebujete lokálny alebo vzdialený prístup.
{{% /details %}}

{{% details title="Potrebujem používateľské meno a heslo pre WebDAV na Synology?" closed="true" %}}
Nie, ak povolíte anonymný prístup WebDAV a nakonfigurujete oprávnenia hosťa pre zdieľaný priečinok. Pre lepšiu bezpečnosť môžete namiesto toho použiť svoje prihlasovacie údaje Synology.
{{% /details %}}

{{% details title="Môžem streamovať FLAC a iné formáty vo vysokom rozlíšení z NAS cez WebDAV?" closed="true" %}}
Áno. Evermusic aj Flacbox podporujú FLAC, ALAC, WAV, DSD a iné formáty vo vysokom rozlíšení pri streamovaní z úložiska NAS cez WebDAV.
{{% /details %}}

{{% details title="Prečo aplikácia nemôže nájsť môj NAS v Dostupných zariadeniach?" closed="true" %}}
Uistite sa, že váš iPhone/Mac a NAS sú na rovnakej sieti Wi-Fi. Ak automatické vyhľadávanie nefunguje, použite možnosť ručného pripojenia a zadajte IP adresu NAS a port WebDAV priamo.
{{% /details %}}
