---
title: "Prístup a súkromie"
date: 2026-08-20
description: "Udržte svoje zdieľanie v Everdisku bezpečné: chráňte prístup prihlásením a heslom, zašifrujte pripojenie SMB pomocou SMB3 (AES), určte, či môžu pripojené zariadenia nahrávať, premenovávať a mazať pomocou Files Editing, blokujte neznáme zariadenia, zvoľte kôš verzus trvalé mazanie a pochopte, prečo všetko zostáva vo vašej lokálnej sieti."
keywords: ["ochrana heslom Everdisk", "šifrovanie SMB", "SMB3 AES šifrovanie", "prepínač úprav súborov", "blokovanie zariadenia", "zablokované zariadenia", "trvalé mazanie súborov", "len lokálna sieť", "súkromné zdieľanie súborov", "DLNA bez hesla", "bezpečnosť siete"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk uchováva vaše súbory vo vašej vlastnej sieti a dáva vám jednoduché ovládanie nad tým, kto sa k nim dostane a čo s nimi môže robiť. Tieto ovládacie prvky nájdete v **Nastaveniach → Zdieľanie → Prístup** a niekoľko súvisiacich nastavení v Správcovi súborov.

## Ochrana prístupu prihlásením a heslom

Štandardne môže vaše zdieľané súbory otvoriť ktokoľvek v rovnakej sieti, kto pozná vašu adresu. Ak chcete vyžadovať prihlásenie:

1. Prejdite do **Nastavenia → Zdieľanie → Prístup**.
2. Zadajte **Prihlasovacie meno** a **Heslo**.
3. Teraz pripojenia **Prehliadač (HTTP)**, **Počítač (WebDAV)**, **Počítač (pokročilé) (SMB)** a **Ostatné aplikácie a zariadenia (FTP)** vyžiadajú tieto údaje ešte pred zobrazením vašich súborov.

Pre otvorený prístup nechajte obe polia prázdne. Vaše heslo je bezpečne uložené v Keychain zariadenia.

> **DLNA je vždy otvorené.** Pripojenie Televízor a mediálne centrum (DLNA) sa nedá chrániť heslom, takže keď je zapnuté, môže vaše zdieľané médiá prehliadať ktorékoľvek zariadenie v rovnakej sieti Wi-Fi. Vypnite ho, ak chcete len chránené pripojenia, a zdieľajte len v sieťach, ktorým dôverujete.

## Zašifrovanie pripojenia SMB (SMB3 / AES)

Prihlásenie a heslo určujú, **kto** sa môže pripojiť, ale samotné dáta putujú na väčšine pripojení stále nezašifrované. **SMB je jediné pripojenie, ktoré Everdisk dokáže zašifrovať**, čím sa každý prenos zakóduje tak, že ho nikto iný v tej istej sieti nedokáže prečítať.

Ako ho zapnúť:

1. Nastavte **Prihlasovacie meno** a **Heslo** ako vyššie - šifrované pripojenia nemôžu byť anonymné.
2. Prejdite do **Nastavenia → Zdieľanie** a zapnite **Vyžadovať šifrovanie SMB**.
3. **Zastavte a znova spustite** zdieľanie, aby sa zmena prejavila.

Každý prenos SMB je potom chránený **šifrovaním SMB3 (AES)**. Pripájajúce sa zariadenie musí podporovať SMB3 - Finder na modernom Macu alebo **Windows 10 a novší**. Je to skvelá voľba na Wi-Fi, ktorej úplne nedôverujete. Šifrovanie SMB je funkcia Premium.

## Povolenie alebo blokovanie úprav (Úprava súborov)

Prepínač **Úprava súborov** určuje, či môžu pripojené zariadenia vaše súbory iba prezerať, alebo aj meniť.

- **Zapnuté** (predvolené): pripojené zariadenia môžu vaše zdieľané súbory **nahrávať, premenovávať a mazať** - takže vaše zariadenie funguje ako skutočný obojsmerný sieťový disk.
- **Vypnuté**: vaše zdieľané súbory sú **len na čítanie**. Ostatní ich môžu prezerať a sťahovať, ale nemôžu nič pridať ani zmeniť.

Jeho zapnutie zobrazí krátke upozornenie, pretože umožňuje iným ľuďom upravovať vaše súbory. Kým je zapnuté, nesie odznak **Dôležité**.

## Blokovanie zariadenia

Ak uvidíte zariadenie, ktoré nepoznáte:

1. Na obrazovke Zdieľanie ho nájdite v časti **Kto je pripojený**.
2. Ťuknite na jeho tlačidlo ďalších akcií a zvoľte **Blokovať toto zariadenie**.

Zablokované zariadenia sú uvedené v **Nastaveniach → Zdieľanie → Prístup → Blokované zariadenia**, kde môžete niektoré **odblokovať** alebo dať **Odblokovať všetky**. Blokovanie sleduje zariadenie aj vtedy, keď sa jeho sieťová adresa zmení (pre pripojenia Prehliadač, Počítač a TV).

## Kôš verzus trvalé mazanie

Keď sa súbor odstráni - či už vami v správcovi súborov, alebo pripojeným zariadením - bežne ide do obnoviteľného **koša**, aby ste ho mohli získať späť.

Ak uprednostňujete, aby sa súbory odstránili okamžite bez možnosti obnovy, zapnite **Trvalo mazať súbory** v **Nastaveniach → Správca súborov → Odstraňovanie súborov**. Toto je štandardne vypnuté. **Ovplyvňuje to správcu súborov v zariadení** aj **mazanie vykonané cez sieť**; nemení to, ako mazanie spracúva systémová knižnica Fotografie alebo knižnica Hudba.

## Všetko zostáva lokálne

Everdisk zdieľa iba cez vašu **lokálnu sieť** - na internet sa nič nenahráva a v strede nie je žiadny cloudový účet. Niekoľko vecí, ktoré je dobré vedieť:

- Everdisk potrebuje povolenie iOS **Lokálna sieť**, aby ho blízke zariadenia mohli nájsť. Ak je toto povolenie vypnuté, poznámka vysvetlí, ako ho znova zapnúť v aplikácii Nastavenia iOS.
- Pre čo najväčšie súkromie zdieľajte len vtedy, keď ste v **domácej alebo súkromnej sieti Wi-Fi**, ktorej dôverujete, a buďte opatrní na verejnej Wi-Fi. Prihlásenie a heslo pomáhajú, ale nenahrádzajú dôveryhodnú sieť.
- **Vôbec najsúkromnejšou možnosťou je USB kábel k Macu** - dáta idú rovno cez kábel a nikdy sa nedotknú smerovača ani internetu. Pozri [Pripojenie vašich zariadení](/docs/guide/everdisk/everdisk-guide-connect).

## Ďalšie kroky

- [Zdieľanie](/docs/guide/everdisk/everdisk-guide-sharing) - vyberte, čo zdieľať, a spustite zdieľanie.
- [Nastavenia](/docs/guide/everdisk/everdisk-guide-settings) - všetky nastavenia Prístupu a Správcu súborov na jednom mieste.
