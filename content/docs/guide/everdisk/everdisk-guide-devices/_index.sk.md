---
title: "Pripojenie k serverom"
date: 2026-08-20
description: "Použite kartu Zariadenia v Everdisku na pripojenie k ďalším serverom vo vašej sieti. Pridávajte a prehliadajte servery DLNA, WebDAV, FTP, SFTP a SMB a disky NAS, streamujte zvuk a video, sťahujte súbory a na serveroch, ktoré to umožňujú, vytvárajte, nahrávajte, premenovávajte, presúvajte či mažte."
keywords: ["karta Zariadenia Everdisk", "pripojenie k NAS", "klient DLNA iPhone", "klient WebDAV iPhone", "klient FTP iPhone", "klient SFTP iPhone", "SMB klient iPhone", "pripojenie k SMB zdieľaniu", "prehliadanie sieťového servera", "streamovanie z NAS", "sťahovanie zo servera", "pripojenie k cloudu cez WebDAV"]
tags: ["everdisk", "guide", "devices", "connections"]
readingTime: 9
---


Everdisk nie je len bezdrôtový disk - je aj klientom pre ostatné zariadenia vo vašej sieti. Karta **Zariadenia** vám umožňuje pripojiť sa k serverom **DLNA**, **WebDAV**, **FTP**, **SFTP** a **SMB**, vrátane Macov, Windows PC, Linux počítačov, diskov NAS a mediálnych serverov, a potom ich súbory prehliadať, streamovať a sťahovať.

## Obrazovka Zariadenia

Karta Zariadenia má dve časti:

- **Pripojenia** - servery, ktoré ste si už uložili.
- **Dostupné zariadenia** - servery, ktoré Everdisk automaticky nájde vo vašej lokálnej sieti.

Ak sa chcete pripojiť k niečomu, čo už Everdisk našiel, stačí na to ťuknúť v časti **Dostupné zariadenia**. Ak chcete server pridať ručne, ťuknite na tlačidlo **plus (+)** alebo na **Nové pripojenie**.

## Pridanie nového pripojenia

Ťuknite na **Nové pripojenie** a vyberte typ servera, ku ktorému sa chcete dostať:

- **DLNA / UPnP** - najlepšie pre mediálne servery. Streamujte video, hudbu a fotografie z mediálnych knižníc, sieťových úložísk a TV či počítačov s podporou DLNA. DLNA je len na čítanie: môžete prehliadať, streamovať a sťahovať, ale nemôžete nahrávať ani meniť súbory.
- **WebDAV** - pripojte sa k súborovým serverom, sieťovým úložiskám a cloudovým diskom, ktoré podporujú WebDAV. Čítanie i zápis, keď to server umožňuje.
- **FTP** - bežné na smerovačoch, sieťových úložiskách a webhostingu. Predvolený port je 21 (990 pre zabezpečené FTPS); vlastný port môžete nastaviť v adrese, napríklad `ftp://host:2121`. Pre anonymný prístup nechajte prihlásenie a heslo prázdne.
- **SFTP** - pripojte sa bezpečne cez SSH. Predvolený port je 22; v prípade potreby použite v adrese vlastný port, napríklad `sftp://host:2222`.
- **SMB** - pripojte sa k Macom, Windows PC, Linux serverom a sieťovým úložiskám (NAS), ktoré zdieľajú priečinky cez **SMB / CIFS**. Zadajte adresu ako `smb://server-address/share-name/` (príklady: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB pridáva dve voliteľné polia: názov **Pracovná skupina** a **Verzia protokolu**, ktorú môžete ponechať na **Automatická** alebo vynútiť **SMB1** či **SMB2**. Ak sa súbory alebo priečinky so špeciálnymi znakmi nedajú otvoriť, skúste prepnúť verziu na **SMB1**.

> Everdisk sa pripája len k týmto protokolom v lokálnej sieti a s priamou adresou. Neprihlasuje sa do cloudových účtov ako Google Drive alebo Dropbox. Cloudový disk je dostupný len vtedy, ak daná služba ponúka adresu **WebDAV**, ktorú môžete zadať.

## Zadanie adresy a prihlásenie

V editore pripojenia vyplňte:

- **Názov** - priateľský názov pre pripojenie.
- **URL / adresa** - adresa servera (pre každý typ sú zobrazené príklady).
- **Prihlasovacie meno** a **Heslo** - obe nechajte prázdne, ak server umožňuje anonymný prístup.

Pri WebDAV môžete povoliť neplatné certifikáty, ak váš server používa vlastnoručne podpísaný. Ak sa identita zabezpečeného servera nedá overiť, Everdisk vás pred jeho dôverovaním požiada o potvrdenie.

Bezplatní používatelia si môžu uložiť až **10** pripojení. Premium toto obmedzenie odstraňuje.

## Prehliadanie, streamovanie a sťahovanie

Po pripojení ťuknite na server a otvorte ho:

- **Prehliadajte** priečinky v zozname alebo mriežke, triedte ich a pozerajte náhľady. Servery DLNA zobrazujú aj detaily hudby a obaly.
- **Streamujte** zvuk a video. Zvuk ide do fronty mini prehrávača; video sa prehráva na celej obrazovke. Počas streamovania súboru funguje aj posúvanie.
- **Sťahujte** súbory do svojho zariadenia. Vyberte naraz viacero pre hromadné sťahovanie. Sťahovania sa objavia v **Prenosy súborov** a pristanú vo vašom priečinku **Dokumenty**.
- **Informácie** pri ktorejkoľvek položke zobrazí jej typ, veľkosť, dátum, cestu a mediálne detaily.

## Zmena súborov na serveri

Na serveroch, ktoré umožňujú zápis - **WebDAV, FTP, SFTP a SMB** - môžete súbory aj spravovať:

- **Nový priečinok**
- **Nahrať súbory** z vášho zariadenia
- **Premenovať**, **Presunúť** a **Odstrániť** (jednu položku alebo naraz viacero)

Servery **DLNA** sú len na čítanie, takže tieto akcie tam nie sú dostupné.

## Sledovanie vašich prenosov

Sťahovania a nahrávania bežia na pozadí a objavia sa v **Prenosy súborov**, ktoré otvoríte vľavo hore na karte **Dokumenty**. Tam môžete sledovať priebeh a úlohy pozastaviť, obnoviť, zopakovať, zrušiť alebo vymazať. Prenosy môžete doladiť aj v [Nastaveniach → Sieť](/docs/guide/everdisk/everdisk-guide-settings) (len Wi-Fi alebo Wi-Fi a mobilné dáta, koľko ich beží naraz a či pokračujú na pozadí).

## Ďalšie kroky

- [Súbory a dokumenty](/docs/guide/everdisk/everdisk-guide-files) - spravujte všetko, čo stiahnete.
- [Fotografie, hudba a video](/docs/guide/everdisk/everdisk-guide-media) - prehrávajte to, čo streamujete.
- [Nastavenia](/docs/guide/everdisk/everdisk-guide-settings) - obmedzenia pripojení a možnosti prenosov.
