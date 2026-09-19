---
title: "Zdieľanie"
date: 2026-08-20
description: "Zistite, ako funguje zdieľanie v Everdisku: ťuknutím na Start premeníte svoj iPhone alebo iPad na bezdrôtový disk, vyberiete, čo zdieľať (súbory, priečinky, fotografie a hudbu), spustíte päť serverov (DLNA, HTTP, WebDAV, SMB, FTP), zašifrujete pripojenie SMB pomocou SMB3 (AES), prečítate si adresy na pripojenie, uvidíte, kto je pripojený, a udržíte zdieľanie bežať cez Wi-Fi alebo USB kábel."
keywords: ["zdieľanie Everdisk", "bezdrôtový disk iPhone", "spustenie zdieľania", "zdieľanie súborov iPhone", "zdieľanie fotografií cez sieť", "DLNA HTTP WebDAV FTP", "čo zdieľať", "ako sa pripojiť", "nechať aplikáciu otvorenú", "zdieľanie cez Wi-Fi alebo USB kábel"]
tags: ["everdisk", "guide", "sharing"]
readingTime: 9
---


Karta **Zdieľanie** je srdcom Everdisku. Práve tu premeníte svoj iPhone alebo iPad na bezdrôtový disk, vyberiete presne to, čo chcete zdieľať, a získate adresy, cez ktoré sa pripoja ostatné zariadenia. Je to prvá karta, ktorú uvidíte po otvorení aplikácie.

## Spustenie a zastavenie zdieľania

V strede obrazovky Zdieľanie je veľké okrúhle tlačidlo.

- Ťuknutím na **Start** naraz zapnete všetky povolené servery. Tlačidlo najprv zobrazí **Starting...** a po spustení zdieľania **Stop**.
- Ťuknutím na **Stop** všetko opäť vypnete. Pripojené zariadenia sa odpoja.

Kým zdieľanie beží, vaše vybrané súbory, fotografie a hudba sú dostupné pre každé zariadenie v rovnakej sieti, ktoré sa pripojí niektorou z piatich metód uvedených nižšie.

> Zdieľanie beží len vtedy, keď je aplikácia otvorená. Prečo je to tak a ako udržať veľké prenosy bežať, sa dozviete v časti **Nechajte aplikáciu otvorenú** takmer na konci tejto stránky.

## Vyberte, čo chcete zdieľať

Než začnete, ťuknite na hlavičku **Čo zdieľať** a otvoria sa tri skupiny. Môžete zdieľať ich ľubovoľnú kombináciu a pred spustením zdieľania musíte vybrať aspoň jednu položku.

**Súbory a priečinky**

- Vlastný priečinok **Dokumenty** vašej aplikácie sa zdieľa štandardne. Ak chcete, jeho zdieľanie môžete zastaviť.
- Ťuknutím na **Pridať priečinok** zdieľate priečinok z ktorejkoľvek časti vášho zariadenia, alebo cez **Pridať súbor** zdieľate jednotlivé súbory.
- Každá zdieľaná položka má tlačidlo **Informácie** a tlačidlo **Zastaviť zdieľanie**.

**Fotografie a videá**

- Zapnite **Povoliť prístup k celej knižnici fotiek**, aby ste zdieľali celú svoju knižnicu fotografií a videí, alebo
- ťuknite na **Pridať fotky** a ručne vyberte len tie fotografie a videá, ktoré chcete zdieľať.

**Hudba**

- Zapnite **Povoliť prístup k celej hudobnej knižnici**, aby ste zdieľali celú svoju hudobnú knižnicu, alebo
- ťuknite na **Pridať skladby** a zdieľajte len vybrané skladby.
- Skladby, ktoré sú chránené (DRM) alebo uložené len v cloude, sa zdieľať nedajú.

Ak sa pokúsite spustiť zdieľanie bez akéhokoľvek výberu, Everdisk zobrazí poznámku **Niet čo zdieľať**. Ak zmeníte to, čo sa zdieľa, počas bežiaceho zdieľania, **zastavte a znova spustite** zdieľanie, aby sa zmena prejavila.

## Päť serverov

Everdisk zdieľa rovnaký obsah piatimi spôsobmi naraz. Každý je určený pre iný druh zariadenia a každý sa dá zapnúť alebo vypnúť v **Nastaveniach → Zdieľanie → Pripojenia**. Štandardne je zapnutých všetkých päť.

- **Televízor a mediálne centrum (DLNA)** - pre smart TV a mediálne prehrávače. Vaše zariadenie si nájdu samy a zobrazia vaše fotografie, videá a hudbu spolu s náhľadmi.
- **Prehliadač (HTTP)** - pre akýkoľvek telefón, tablet alebo počítač. Druhá osoba otvorí odkaz vo webovom prehliadači a prehliada si či sťahuje vaše súbory. Netreba nič inštalovať.
- **Počítač (WebDAV)** - pre Mac, Windows PC alebo počítač s Linuxom. Vaše zariadenie sa zobrazí ako bežný sieťový disk, takže môžete presúvať súbory oboma smermi.
- **Počítač (pokročilé) (SMB)** - sieťový disk pre Mac, Windows a Linux. Na Macu sa zobrazí samostatne v bočnom paneli Finderu; vo Windowse ho otvoríte v Prieskumníkovi súborov adresou `smb://`. Je to jediné pripojenie, ktoré môžete **zašifrovať**, pomocou šifrovania SMB3 (AES).
- **Ostatné aplikácie a zariadenia (FTP)** - pre súborové aplikácie a pokročilých používateľov, ktorí ovládajú FTP.

Podrobné pokyny na pripojenie pre každý typ nájdete v časti [Pripojenie vašich zariadení](/docs/guide/everdisk/everdisk-guide-connect).

## Ako sa pripojiť a adresy na pripojenie

Keď ťuknete na Start, sekcia **Ako sa pripojiť** zobrazí kartu pre každý aktívny server s presnou **adresou**, ktorú zadáte na druhom zariadení. Každú adresu je jednoduché skopírovať - ťuknutím ju skopírujete, tlačidlom **Zdieľať** ju odošlete alebo tlačidlom **info (ⓘ)** zobrazíte podrobné pokyny pre daný protokol.

- Karta DLNA zobrazuje adresu s popisom zariadenia, ktorá končí na `/device-desc.xml`, pre prehrávače, ktoré ju vyžadujú.
- Keď je vaše zariadenie pripojené k Macu káblom, objaví sa ďalšia adresa s odznakom **Pripojenie cez kábel**, ktorá používa názov `.local` vášho zariadenia.

Adresu si môžete otvoriť aj ako **QR kód**, aby fotoaparát iného zariadenia skočil rovno na ňu.

## Kto je pripojený

Sekcia **Kto je pripojený** v reálnom čase zobrazuje zariadenia, ktoré sú k vám práve pripojené. Ťuknite na tlačidlo ďalších akcií vedľa ktoréhokoľvek zariadenia a cez **Blokovať toto zariadenie** ho zablokujte, ak ho nepoznáte. Zablokované zariadenia spravujete v časti [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access).

## Názov a avatar vášho zariadenia

Každé zariadenie má priateľský názov (napríklad "Speedy-Hare") a farebný avatar. Práve tento názov zobrazí TV, počítač alebo iná aplikácia pre vaše zariadenie v sieti, takže sa dá ľahko rozpoznať. Názov a avatar si môžete vygenerovať nanovo zadarmo alebo s Premium nastaviť vlastný názov, ikonu či fotografický avatar. Pozrite si [Nastavenia](/docs/guide/everdisk/everdisk-guide-settings).

## Zdieľanie cez Wi-Fi alebo USB kábel

Zdieľanie môže bežať v dvoch situáciách:

- **Cez Wi-Fi** - vaše zariadenie a ostatné zariadenia sú v rovnakej sieti Wi-Fi.
- **Cez USB kábel** - vaše zariadenie je pripojené k **Macu** káblom, a to aj vtedy, keď žiadne Wi-Fi vôbec nie je. Toto je rýchlejšie než Wi-Fi a funguje aj v lietadle, v hoteli alebo v uzamknutej sieti.

Ak nie je k dispozícii ani Wi-Fi, ani kábel, tlačidlo **Start** je neaktívne a objaví sa poznámka **Žiadne Wi-Fi pripojenie**. Ak sa počas zdieľania spojenie preruší, Everdisk zdieľanie automaticky zastaví a upozorní vás. Ťuknutím na tlačidlo info pri ktorejkoľvek z týchto poznámok získate úplné vysvetlenie.

## Nechajte aplikáciu otvorenú

Keďže váš iPhone alebo iPad funguje ako server, **zdieľanie funguje len vtedy, keď je Everdisk otvorený na obrazovke**. Ak aplikáciu zatvoríte alebo zariadenie na dlhší čas uzamknete, systém môže aplikáciu pozastaviť a zdieľanie sa zastaví.

Pri veľkých prenosoch:

- Nechajte Everdisk otvorený a v popredí.
- Pripojte zariadenie k napájaniu.
- Počas prenosu nastavte v aplikácii Nastavenia iOS **Automatické uzamknutie** na **Nikdy**.

Môžete zapnúť **Upozorniť pred odpojením** (v Nastaveniach → Zdieľanie), aby vám Everdisk pripomenul znovu otvoriť aplikáciu skôr, než ju systém pozastaví. Ťuknutím na tlačidlo info na banneri **Nechajte aplikáciu otvorenú** získate viac podrobností.

## Ďalšie kroky

- [Pripojenie vašich zariadení](/docs/guide/everdisk/everdisk-guide-connect) - pripojte TV, počítač, prehliadač, telefón alebo USB kábel.
- [Prístup a súkromie](/docs/guide/everdisk/everdisk-guide-access) - pridajte heslo a ovládajte úpravy.
- [Nastavenia](/docs/guide/everdisk/everdisk-guide-settings) - zapnite alebo vypnite servery a doladíte kvalitu.
