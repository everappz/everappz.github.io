---
title: "Nastavenia"
date: 2026-08-20
description: "Kompletný prehľad nastavení Everdisku: profil zariadenia (názov a avatar), päť pripojovacích serverov, ovládanie prístupu, šifrovanie SMB (SMB3/AES), kvalita fotografií a videa, vlastné porty, náhľady DLNA, sieťové a prenosové možnosti, možnosti správcu súborov a Premium."
keywords: ["nastavenia Everdisk", "názov a avatar zariadenia", "pripojovacie servery", "kvalita fotografií a videa", "vlastné porty HTTP WebDAV FTP", "náhľady DLNA", "paralelné prenosy", "trvalé mazanie súborov", "vyrovnávacia pamäť náhľadov", "Everdisk Premium"]
tags: ["everdisk", "guide", "settings"]
readingTime: 12
---


Karta **Nastavenia** zoskupuje všetko do troch hlavných oblastí - **Zdieľanie**, **Sieť** a **Správca súborov** - plus Premium, spätná väzba a právne odkazy. Táto stránka vysvetľuje každé nastavenie a jeho predvolenú hodnotu.

## Premium

V hornej časti Nastavení vidíte svoj stav Premium alebo tlačidlo **Odomknúť všetky funkcie**. Everdisk sa dá používať zadarmo s niekoľkými obmedzeniami; jednorazový nákup **Premium Lifetime** ich odstráni. Pozri [Premium](#premium-lifetime) na konci tejto stránky.

## Nastavenia zdieľania

### Všeobecné

- **Automaticky spustiť zdieľanie zariadenia** - spustí zdieľanie hneď po otvorení aplikácie. *(Premium.)*
- **Zdieľať priečinok Dokumenty** - zdieľa vlastný priečinok Dokumenty aplikácie. Štandardne zapnuté.
- **Upozorniť pred odpojením** - pripomenie vám znovu otvoriť aplikáciu skôr, než ju systém na pozadí pozastaví. Štandardne vypnuté; pri prvom raze si vyžiada povolenie na oznámenia.

### Profil zariadenia

- **Názov zariadenia** - názov, ktorý pre vás vidia ostatné zariadenia v sieti. Ťuknutím ho upravíte. *(Premium.)*
- **Avatar zariadenia** - ikona a farba pozadia vášho zariadenia. Môžete si vybrať ikonu, gradient pozadia alebo **vybrať avatar z Fotografií**. *(Premium.)*
- **Vygenerovať názov a avatar** a **Vygenerovať nový avatar** - získate nový náhodný názov alebo avatar. *(Zadarmo.)*

### Prístup

- **Prihlasovacie meno** a **Heslo** - vyžiadajte prihlásenie pre pripojenia Prehliadač, Počítač a Ostatné aplikácie.
- **Úprava súborov** - umožnite pripojeným zariadeniam nahrávať, premenovávať a mazať. Štandardne zapnuté.
- **Blokované zariadenia** - spravujte zariadenia, ktoré ste zablokovali.

Podrobnosti nájdete v časti [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access).

### Pripojenia

Zapnite alebo vypnite každý server. Štandardne je zapnutých všetkých päť a každý má tlačidlo info (ⓘ) s pokynmi na pripojenie:

- **Televízor a mediálne centrum** (DLNA)
- **Prehliadač** (HTTP)
- **Počítač** (WebDAV)
- **Počítač (pokročilé)** (SMB) - sieťový disk pre Mac, Windows a Linux; na Macu sa zobrazí samostatne v bočnom paneli Finderu. Jediné pripojenie, ktoré sa dá zašifrovať.
- **Ostatné aplikácie a zariadenia** (FTP)

### Fotografie

- **Formát** - Pôvodný alebo Najkompatibilnejší (JPEG).
- **Kvalita** - Pôvodná, Vysoká, Stredná alebo Nízka.

Čokoľvek iné než Pôvodný konvertuje fotografie počas zdieľania, čo je pomalšie. Konverzia je funkcia Premium.

### Videá

- **Formát** - Pôvodný alebo Najkompatibilnejší (H.264 MP4).
- **Kvalita** - Pôvodná, Vysoká, Stredná alebo Nízka.

Rovnaký princíp ako pri Fotografiách: Pôvodný je najrýchlejší a konverzia je Premium. Ak staršia TV nedokáže prehrať video, znížte kvalitu.

### Rozšírené

- **Port HTTP** (predvolene 80), **Port WebDAV** (predvolene 8080), **Port SMB** (predvolene 4455), **Port FTP** (predvolene 2121). DLNA si port vyberá automaticky. *(Zmena portov je Premium; bezplatní používatelia vidia hodnoty.)*

### Šifrovanie SMB

- **Vyžadovať šifrovanie SMB** - zašifruje každý prenos SMB pomocou **šifrovania SMB3 (AES)**, takže nikto iný v sieti nedokáže čítať vaše súbory. Štandardne vypnuté. Vyžaduje nastavené **prihlásenie a heslo** vyššie (šifrované pripojenia nemôžu byť anonymné) a klienta, ktorý podporuje SMB3, napríklad Finder na modernom Macu alebo Windows 10 a novší. Zmeny sa prejavia pri ďalšom spustení zdieľania. *(Premium.)*

### Náhľady DLNA

- **Zobraziť miniatúry** - publikuje náhľadové obrázky pre TV. Štandardne zapnuté (zadarmo).
- Zvoľte, ktoré veľkosti publikovať: **Malá (160px)**, **Stredná (640px)**, **Veľká (1024px)**, **Extra veľká (4096px)**.

## Sieťové nastavenia

- **Prenosy súborov** - pre sťahovania a nahrávania použite len **Wi-Fi**, alebo **Wi-Fi a mobilné dáta**. Predvolene Wi-Fi.
- **Limit paralelných prenosov** - koľko prenosov beží naraz. Predvolene 5.
- **Prenosy na pozadí** - udržte prenosy bežať, aj keď používate iné obrazovky. Štandardne zapnuté.
- **Náhľady súborov** - či sa majú náhľady pre súbory na iných zariadeniach načítavať len cez Wi-Fi, alebo aj cez mobilné dáta. Predvolene Wi-Fi.

## Nastavenia správcu súborov

- **Trvalo mazať súbory** - mazať okamžite bez koša. Štandardne vypnuté. Pozri [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access).
- **Obnoviť všetky správy upozornení** - vráti tipové bannery, ktoré ste zavreli.
- **Vyrovnávacia pamäť náhľadov** - zobrazí, koľko miesta zaberajú uložené náhľady, a **Vymazať vyrovnávaciu pamäť náhľadov**.

## Spätná väzba a právne informácie

V dolnej časti môžete **Ohodnotiť túto aplikáciu**, **Odoslať spätnú väzbu**, **Získať ďalšie aplikácie** a otvoriť **Zmluvné podmienky** a **Zásady ochrany súkromia**.

## Premium Lifetime

Everdisk sa dá používať zadarmo. Jediný nákup **Premium Lifetime** - jednorazová platba, nie predplatné - odomkne:

- **Neobmedzené priečinky** - zdieľajte viac než 5 priečinkov.
- **Neobmedzené pripojenia** - uložte viac než 10 serverov na karte Zariadenia.
- **Konverzia fotiek a videí** - zdieľajte v akejkoľvek kvalite inej než Pôvodná.
- **Šifrovanie SMB** - chráňte prenosy SMB pomocou šifrovania SMB3 (AES).
- **Vlastné porty** - nastavte si vlastné porty HTTP, WebDAV, SMB a FTP.
- **Automaticky spustiť zdieľanie** - spustite zdieľanie automaticky pri otvorení aplikácie.
- **Prispôsobenie zariadenia** - vlastný názov zariadenia, ikona avatara, gradient pozadia alebo fotografický avatar.

Premium je viazané na vaše Apple ID. Pomocou **Obnoviť nákupy** ho odomknete na svojich ďalších zariadeniach prihlásených s rovnakým Apple ID.

## Ďalšie kroky

- [Zdieľanie](/docs/guide/everdisk/everdisk-guide-sharing) - obrazovka Zdieľanie do detailu.
- [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access) - heslá, úpravy a blokovanie.
- [Časté otázky](/docs/faq/everdisk) - rýchle odpovede na bežné otázky.
