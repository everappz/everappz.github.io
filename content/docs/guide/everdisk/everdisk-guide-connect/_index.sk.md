---
title: "Pripojenie vašich zariadení"
date: 2026-08-20
description: "Podrobné pokyny na pripojenie k vášmu bezdrôtovému disku Everdisk: sledujte na smart TV cez DLNA, otvorte svoje súbory v akomkoľvek webovom prehliadači, pripojte zariadenie ako sieťový disk vo Finderi, vo Windowse alebo v Linuxe cez WebDAV alebo SMB (s voliteľným šifrovaním SMB3/AES), pripojte súborové aplikácie cez FTP a prenášajte cez USB kábel na Mac bez potreby Wi-Fi."
keywords: ["pripojenie k Everdisku", "streamovanie do TV cez DLNA", "otvorenie súborov v prehliadači", "pripojenie sieťového disku vo Finderi", "WebDAV Windows Linux", "súborová aplikácia FTP", "prenos cez USB kábel na Mac", "pripojenie iPhonu k počítaču", "sieťový disk iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Keď na obrazovke [Zdieľanie](/docs/guide/everdisk/everdisk-guide-sharing) ťuknete na **Start**, ostatné zariadenia sa môžu k vašim súborom pripojiť piatimi rôznymi spôsobmi. Vyberte si metódu, ktorá zodpovedá zariadeniu, ktoré chcete použiť. V každom prípade sa presná **adresa**, ktorú potrebujete, zobrazuje v sekcii **Ako sa pripojiť** na obrazovke Zdieľanie.

> Obe zariadenia musia byť v **rovnakej sieti Wi-Fi** - alebo, v prípade Macu, pripojené **USB káblom** (pozri poslednú časť).

## Sledovanie na TV (DLNA)

Túto metódu použite na zobrazenie fotografií, videí a hudby na smart TV alebo mediálnom prehrávači.

1. V **Nastaveniach → Zdieľanie → Pripojenia** sa uistite, že je zapnuté **Televízor a mediálne centrum** (štandardne je zapnuté).
2. Na obrazovke Zdieľanie ťuknite na **Start**.
3. Na svojej TV otvorte jej vstavaný mediálny prehrávač alebo aplikáciu mediálneho servera (môže sa volať Media Player, SmartShare, AllShare a podobne).
4. Vaše zariadenie sa objaví v zozname mediálnych serverov pod svojím názvom (napríklad "Speedy-Hare"). Vyberte ho.
5. Prehliadajte svoje zdieľané fotografie, videá a hudbu a spustite prehrávanie. Náhľady sa zobrazia automaticky.

Poznámky:

- DLNA sa nedá chrániť heslom, takže toto pripojenie je otvorené pre každého v rovnakej sieti Wi-Fi, kým je zapnuté.
- Ak sa video na staršej TV neprehráva, znížte kvalitu videa v **Nastaveniach → Zdieľanie → Videá**, aby ho Everdisk skonvertoval do kompatibilnejšieho formátu.

## Otvorenie vo webovom prehliadači (HTTP)

Túto metódu použite, keď chcete súbory odovzdať komukoľvek s webovým prehliadačom - bez inštalácie akejkoľvek aplikácie.

1. V **Nastaveniach → Zdieľanie → Pripojenia** sa uistite, že je zapnutý **Prehliadač**.
2. Ťuknite na **Start**.
3. Na obrazovke Zdieľanie skopírujte adresu **Prehliadača** (alebo zobrazte jej QR kód).
4. Na druhom telefóne, tablete alebo počítači otvorte akýkoľvek webový prehliadač (Safari, Chrome, Edge, Firefox) a zadajte túto adresu.
5. Otvorí sa stránka s vašimi zdieľanými súbormi.

V prehliadači môže druhá osoba:

- prepínať medzi **zoznamovým** a **mriežkovým** zobrazením a triediť podľa názvu, dátumu alebo veľkosti,
- vidieť skutočné **náhľady** pre fotografie, videá, súbory PDF a obaly hudby,
- otvoriť fotografiu do celoobrazovkovej **galérie** s posúvaním, priblížením štipnutím a prezentáciou,
- prehrávať hudbu vo vstavanom **prehrávači** s frontou, náhodným prehrávaním a opakovaním,
- **stiahnuť** akýkoľvek súbor alebo stiahnuť celý priečinok (prípadne niekoľko vybraných položiek) ako jeden **Archive.zip**,
- **nahrať** súbory späť do vášho zariadenia - len ak ste zapli **Úprava súborov** (pozri [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access)).

## Použitie ako sieťový disk (WebDAV)

Túto metódu použite, aby sa vaše zariadenie zobrazilo ako bežný disk na Macu, Windows PC alebo počítači s Linuxom, takže môžete presúvať súbory oboma smermi.

**Na Macu (Finder)**

1. V **Nastaveniach → Zdieľanie → Pripojenia** sa uistite, že je zapnutý **Počítač**.
2. Ťuknite na **Start** a poznačte si adresu **Počítač (WebDAV)**.
3. Vo Finderi zvoľte **Prejsť → Pripojiť k serveru** (alebo stlačte **⌘K**).
4. Zadajte adresu WebDAV presne tak, ako je zobrazená, a kliknite na **Pripojiť**.
5. Ak ste nastavili prihlásenie a heslo, zadajte ich, inak sa pripojte ako hosť.
6. Vaše zariadenie sa otvorí ako každý iný sieťový disk. Presúvajte súbory dnu i von.

**Vo Windowse**

1. Otvorte **Prieskumník súborov**, kliknite pravým tlačidlom na **Tento počítač** a zvoľte **Pridať sieťové umiestnenie** (alebo priradiť sieťovú jednotku).
2. Zadajte adresu WebDAV zobrazenú v Everdisku.
3. Ak ste nastavili prihlásenie a heslo, zadajte ich.

**V Linuxe**

1. Otvorte svojho správcu súborov a zvoľte **Pripojiť k serveru** (alebo použite `davs://` / `dav://`).
2. Zadajte adresu WebDAV zobrazenú v Everdisku.

Či bude spojenie len na čítanie alebo obojsmerné, závisí od nastavenia **Úprava súborov**. Keď je zapnuté, môžete kopírovať súbory do svojho zariadenia a premenovávať ich či mazať; keď je vypnuté, disk je len na čítanie.

## Pripojenie cez SMB (šifrovaný sieťový disk)

SMB je sieťový disk pre Mac, Windows a Linux, postavený na zdieľaní súborov, ktoré už tieto systémy majú, takže sa vaše zariadenie zobrazí ako bežný sieťový disk - a je to jediné pripojenie, ktoré môžete zašifrovať.

1. V **Nastaveniach → Zdieľanie → Pripojenia** sa uistite, že je zapnuté **Počítač (pokročilé)** (pripojenie SMB).
2. Ťuknite na **Start** a poznačte si adresu **SMB**, ktorá vyzerá ako `smb://192.168.1.20:4455/Share`.
3. Pripojte sa zo svojho počítača:
   - **Mac:** vaše zariadenie sa objaví samostatne v **bočnom paneli Finderu** v časti **Locations** (Sieť) - stačí naň kliknúť a prihlásiť sa. Ak sa chcete pripojiť ručne, zvoľte **Prejsť → Pripojiť k serveru** (**⌘K**) a zadajte adresu.
   - **Windows:** otvorte **Prieskumník súborov**, kliknite pravým tlačidlom na **Tento počítač** a zvoľte **Namapovať sieťový disk**, potom zadajte `\\<address>\Share` s použitím hostiteľa a názvu zdieľania z obrazovky Zdieľanie (alebo zadajte adresu `smb://` do adresného riadka).
   - **Linux:** vo svojom správcovi súborov zvoľte **Pripojiť k serveru** a zadajte adresu.
4. Zadajte prihlásenie a heslo, ak ste ich nastavili, inak sa pripojte ako hosť.
5. Zdieľanie sa volá **Share**. So zapnutým **Úprava súborov** môžete kopírovať súbory oboma smermi; s vypnutým je len na čítanie.

**Zapnutie šifrovania (odporúčané na nedôveryhodnej Wi-Fi)**

SMB je jediné pripojenie Everdisku, ktoré sa dá zašifrovať. Ak chcete každý prenos chrániť **šifrovaním SMB3 (AES)**:

1. V **Nastaveniach → Zdieľanie → Prístup** nastavte **Prihlasovacie meno** a **Heslo** - šifrované pripojenia nemôžu byť anonymné.
2. V **Nastaveniach → Zdieľanie** zapnite **Vyžadovať šifrovanie SMB**.
3. **Zastavte a znova spustite** zdieľanie, aby sa zmena prejavila.

Váš klient musí podporovať SMB3 - Finder na modernom Macu alebo **Windows 10 a novší**. Šifrovanie SMB je funkcia Premium.

## Pripojenie súborovej aplikácie (FTP)

Túto metódu použite pre správcov súborov a prenosové aplikácie, ktoré ovládajú FTP (napríklad FileZilla alebo Cyberduck na počítači).

1. V **Nastaveniach → Zdieľanie → Pripojenia** sa uistite, že sú zapnuté **Ostatné aplikácie a zariadenia**.
2. Ťuknite na **Start** a poznačte si adresu **FTP**.
3. Vo svojej FTP aplikácii pridajte nové pripojenie s touto adresou.
4. Ak ste nastavili prihlásenie a heslo, zadajte ich, alebo ich nechajte prázdne pre anonymný prístup.

## Prenos cez USB kábel (Mac, bez potreby Wi-Fi)

Túto metódu použite, keď nie je k dispozícii Wi-Fi alebo keď chcete najrýchlejší a najsúkromnejší prenos. Funguje len s **Macom**.

1. Pripojte svoj iPhone alebo iPad k Macu bežným nabíjacím káblom.
2. Ak vás na zariadení požiada, ťuknite na **Dôverovať tomuto počítaču**.
3. V Everdisku ťuknite na **Start**. Objaví sa poznámka **Dostupné rýchle pripojenie** a na obrazovke Zdieľanie sa zobrazí ďalšia adresa s odznakom **Pripojenie cez kábel**, ktorá končí na `.local`.
4. Na Macu otvorte Finder → **Prejsť → Pripojiť k serveru** (**⌘K**) a zadajte túto adresu `.local` (funguje pre pripojenie cez Prehliadač aj cez Počítač).
5. Vaše zariadenie sa otvorí cez kábel - rýchlejšie než cez Wi-Fi a dáta sa nikdy nedotknú smerovača ani internetu.

Poznámky:

- Použite **názov `.local`**, nie IP adresu (IP adresy fungujú len cez Wi-Fi) a nikdy nie `localhost`.
- Cesta cez kábel je **len pre Mac**. Windows PC a zariadenia s Androidom musia použiť Wi-Fi.
- Súbory môžete do priečinka Everdisk presúvať aj pomocou Finderu na Macu alebo aplikácie Apple Devices (prípadne iTunes) vo Windowse, cez štandardné zdieľanie súborov v iOS.

## Ďalšie kroky

- [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access) - pridajte heslo, povoľte nahrávanie, zablokujte zariadenie.
- [Fotografie, hudba a video](/docs/guide/everdisk/everdisk-guide-media) - zdieľajte celú knižnicu a nastavte kvalitu.
- [Pripojenie k serverom](/docs/guide/everdisk/everdisk-guide-devices) - dostaňte sa z Everdisku k ďalším zariadeniam.
