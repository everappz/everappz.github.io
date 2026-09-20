---
title: "Ako nastaviť server WebDAV na iPhone a iPade na prístup k súborom a zdieľanie"
description: "Premeňte svoj iPhone alebo iPad na server WebDAV s aplikáciou Everdisk a pripojte ho ako sieťový disk vo Finderi na Macu, v Prieskumníkovi súborov Windowsu, na Linuxe, Androide alebo ďalšom iPhone cez Wi-Fi. Kompletné nastavenie, adresa a port WebDAV a pripojenie krok za krokom pre každé zariadenie."
date: 2026-09-19
tags: ["everdisk", "webdav", "sieťový disk", "zdieľanie súborov", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV server iPhone", "WebDAV server iPad", "ako nastaviť WebDAV na iPhone", "pripojiť iPhone ako sieťový disk", "pripojiť iPhone WebDAV Mac Finder", "WebDAV Prieskumník súborov Windows iPhone", "iphone sieťový disk Windows", "WebDAV Linux iPhone", "prístup k súborom iPhonu z počítača", "webdav iphone na iphone", "zdieľanie súborov iPhone WebDAV", "namapovať sieťový disk iphone", "prenos súborov iphone webdav", "adresa port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV premení priečinok na sieťový disk, ktorý počítač otvorí vo svojom bežnom správcovi súborov. Beží cez ten istý webový protokol, ktorý používa váš prehliadač, a preto dobre putuje naprieč Macom, Windowsom a Linuxom bez špeciálnych ovládačov. S aplikáciou [Everdisk](/products/everdisk) môžete spustiť server WebDAV na svojom iPhone alebo iPade, takže telefón sa zobrazí ako disk, ktorý dokážete prechádzať, kopírovať z neho aj naň takmer z akéhokoľvek počítača.

WebDAV je najlepšia voľba, keď je v hre Windows, pretože Prieskumník súborov Windowsu sa k nemu pripája čisto. Táto príručka pokrýva nastavenie a spôsob pripojenia z Macu, Windowsu, Linuxu, Androidu a druhého iPhonu.

## Čo potrebujete

- iPhone alebo iPad s nainštalovanou aplikáciou [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Počítač alebo iné zariadenie v **tej istej Wi-Fi sieti**.
- Súbory, ktoré chcete zdieľať, v priečinku Dokumenty aplikácie Everdisk alebo v priečinkoch, ktoré pridáte.

## Nastavenie servera WebDAV v aplikácii Everdisk

### Krok 1: Vyberte, čo chcete zdieľať a nastavte prístup

Otvorte Everdisk, prejdite na kartu **Zdieľanie** a ťuknite na **Čo zdieľať**. Priečinok Dokumenty sa zdieľa štandardne. Pridajte ďalšie pomocou **Pridať priečinok** a **Pridať súbor**.

Otvorte **Nastavenia**, potom **Zdieľanie**, potom **Prístup**. Zapnite **Úprava súborov**, ak chcete, aby pripojené počítače mohli kopírovať súbory do vášho telefónu a premenovať alebo mazať ich, alebo ju vypnite pre disk len na čítanie. Nastavte tu **Prihlasovacie meno** a **Heslo**, ak chcete prihlásenie, alebo ich nechajte prázdne pre hosťovský prístup.

### Krok 2: Zapnite server WebDAV

Prejdite do **Nastavenia**, potom **Zdieľanie**, potom **Pripojenia** a zapnite **Počítač**. To je server WebDAV (nesie značku WebDAV).

### Krok 3: Spustite zdieľanie a poznačte si adresu

Vráťte sa na kartu **Zdieľanie** a ťuknite na **Štart**. Sekcia **How to Connect** zobrazuje adresu WebDAV. Vyzerá takto:

```
http://192.168.1.20:8080
```

Číslo za dvojbodkou je **port**, ktorý je štandardne **8080**. Prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vaša bude odlišná. Nechajte Everdisk otvorený na obrazovke, kým je zariadenie pripojené.

## Pripojenie z Macu

1. Otvorte **Finder**, zvoľte **Go**, potom **Connect to Server** (alebo stlačte **Command a K**).
2. Napíšte adresu WebDAV zobrazenú v aplikácii Everdisk, napríklad `http://192.168.1.20:8080`.
3. Kliknite na **Connect**, potom zvoľte **Guest** alebo zadajte svoje **Prihlasovacie meno** a **Heslo**.

Váš iPhone sa otvorí v okne Finderu a správa sa ako bežný priečinok. Súbory kopírujte v oboch smeroch, ak je zapnutá Úprava súborov.

## Pripojenie z Windowsu

Windows má zabudovaného klienta WebDAV, takže toto funguje z Prieskumníka súborov.

1. Otvorte **File Explorer**, kliknite pravým tlačidlom na **This PC** v bočnom paneli a zvoľte **Add a network location** (môžete použiť aj **Map network drive**).
2. Keď sa vás spýta na adresu, napíšte tú istú adresu WebDAV z aplikácie Everdisk, napríklad `http://192.168.1.20:8080`, potom kliknite na **Next**.
3. Zadajte svoje **Prihlasovacie meno** a **Heslo**, ak ste ich nastavili.

Zariadenie sa potom zobrazí pod This PC ako sieťové umiestnenie, ktoré môžete otvoriť a kopírovať z neho súbory. Ak sa Windows prvýkrát odmietne pripojiť, uistite sa, že služba **WebClient** beží (vyhľadajte Services v ponuke Štart, nájdite WebClient a nastavte ju na spustenie), potom to skúste znova.

## Pripojenie z Linuxu

1. Otvorte svojho správcu súborov a zvoľte **Connect to Server** alebo **Other Locations**.
2. Zadajte adresu s prefixom WebDAV, napríklad `dav://192.168.1.20:8080` (`davs://` použite len vtedy, ak ste nastavili TLS).
3. Pripojte sa ako hosť alebo zadajte svoje prihlásenie.

## Pripojenie z Androidu

Android nemá systémový prehliadač WebDAV, preto použite správcu súborov, ktorý ho podporuje:

1. Nainštalujte aplikáciu ako **Solid Explorer** alebo **CX File Explorer**.
2. Pridajte nové pripojenie **WebDAV**.
3. Zadajte hostiteľa a **port 8080**, zvoľte schému `http` a pridajte svoje prihlásenie, ak ste ho nastavili.

## Pripojenie z ďalšieho iPhonu alebo iPadu

Aplikácia Súbory v iOS neobsahuje klienta WebDAV, preto použite jednu z týchto možností:

- **Vlastná karta Zariadenia aplikácie Everdisk.** Na druhom zariadení otvorte Everdisk, prejdite na **Zariadenia**, ťuknite na **Nové pripojenie**, zvoľte **WebDAV** a zadajte adresu, napríklad `http://192.168.1.20:8080`. Toto je najjednoduchšia cesta a nepotrebuje nič navyše.
- **Aplikácia WebDAV** ako Documents by Readdle, ktorá dokáže pridať pripojenie WebDAV s tou istou adresou a prihlásením.

## Radšej rýchly odkaz namiesto disku?

Ak potrebujete len rýchlo chytiť súbor a nechcete vôbec pripájať disk, zapnite pripojenie **Prehliadač** v Nastavenia, Zdieľanie, Pripojenia. Everdisk vám potom dá webovú adresu, ktorú môžete otvoriť v akomkoľvek prehliadači na akomkoľvek zariadení na prezeranie a sťahovanie vašich súborov. Je to najrýchlejší spôsob, ako odovzdať súbor Windows PC, Chromebooku alebo telefónu kamaráta.

## Len na čítanie alebo na čítanie a zápis

Toto rozhoduje prepínač **Úprava súborov** v Nastavenia, Zdieľanie, Prístup. Zapnutý znamená, že pripojené počítače môžu nahrávať, premenúvať a mazať. Vypnutý znamená, že disk je len na čítanie, takže ostatní môžu zobrazovať a kopírovať vaše súbory, ale nemôžu ich meniť.

## Ako to ľudia využívajú v bežnom živote

- **Skopírujte súbory do svojho iPhonu z Windows PC** jeho namapovaním ako sieťové umiestnenie a ich pretiahnutím.
- **Presuňte fotky a dokumenty do notebooku** pomocou správcu súborov, ktorý už poznáte, bez kábla a bez iTunes.
- **Upravte dokument na mieste** z Macu, otvorte ho priamo z telefónu a uložte späť.
- **Presuňte priečinok medzi iPhonom a iPadom** pomocou karty Zariadenia aplikácie Everdisk na prijímacom zariadení.

## Zopár tipov

- Nechajte Everdisk otvorený, kým je zariadenie pripojené. Dlhé zamknutie telefónu môže aplikáciu pozastaviť.
- Na Windowse, ak pripojenie zlyhá, spustite službu WebClient a skúste adresu znova.
- WebDAV aj SMB sa pripájajú ako sieťové disky. Použite WebDAV, keď je v hre Windows, a [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), keď chcete rýchlosť Finderu a šifrovanie.
- Pre najrýchlejšie prenosy ponechajte kvalitu fotiek a videa na Original v Nastaveniach.

## Často kladené otázky

{{% details title="Aká je adresa a port WebDAV pre môj iPhone?" closed="true" %}}
Po spustení zdieľania Everdisk zobrazí adresu na obrazovke Zdieľanie. Vyzerá ako http://192.168.1.20:8080. 8080 je port, ktorý Everdisk používa pre WebDAV, a prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vaša bude iná.
{{% /details %}}

{{% details title="Ako sa pripojím k WebDAV svojho iPhonu z Windowsu?" closed="true" %}}
Otvorte File Explorer, kliknite pravým tlačidlom na This PC a zvoľte Add a network location alebo Map network drive. Zadajte adresu WebDAV z aplikácie Everdisk, napríklad http://192.168.1.20:8080, potom zadajte svoje prihlásenie, ak ste ho nastavili. Ak sa Windows nechce pripojiť, uistite sa, že služba WebClient beží (vyhľadajte Services, nájdite WebClient, spustite ju) a skúste znova.
{{% /details %}}

{{% details title="Môžem použiť WebDAV medzi dvoma iPhonmi?" closed="true" %}}
Áno, ale aplikácia Súbory v iOS nemá klienta WebDAV, preto použite Everdisk na druhom zariadení. Otvorte kartu Zariadenia, ťuknite na Nové pripojenie, zvoľte WebDAV a zadajte adresu zobrazenú na prvom telefóne. Funguje aj aplikácia WebDAV ako Documents by Readdle.
{{% /details %}}

{{% details title="Potrebuje WebDAV heslo?" closed="true" %}}
Nie, prihlásenie je voliteľné. Nechajte Prihlasovacie meno a Heslo prázdne v Nastavenia, Zdieľanie, Prístup pre hosťovský prístup, alebo ich nastavte, ak chcete, aby sa pripojenia prihlasovali.
{{% /details %}}

{{% details title="Môžu iní ľudia meniť moje súbory cez WebDAV?" closed="true" %}}
Len ak to povolíte. Prepínač Úprava súborov v Nastavenia, Zdieľanie, Prístup toto ovláda. Zapnutý umožňuje pripojeným zariadeniam nahrávať, premenúvať a mazať. Vypnutý robí disk len na čítanie, takže ostatní môžu zobrazovať a kopírovať, ale nič meniť.
{{% /details %}}

{{% details title="WebDAV alebo SMB, aký je rozdiel?" closed="true" %}}
Obidva pripoja váš iPhone ako sieťový disk. WebDAV beží cez webový protokol a pripája sa čisto z Prieskumníka súborov Windowsu, čo je jeho hlavná prednosť. SMB je natívne zdieľanie súborov na Macu, Linuxe a zariadeniach NAS, na Macu je zvyčajne rýchlejšie a je to jediné pripojenie Everdisk, ktoré dokáže zašifrovať prenosy. Everdisk môže spustiť obidva naraz.
{{% /details %}}

{{% details title="Prečo sa môj disk WebDAV odpája?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikácie, ktoré zostávajú príliš dlho na pozadí. Nechajte Everdisk otvorený na obrazovke, kým je zariadenie pripojené, a počas dlhých prenosov pripojte k napájaniu. Tiež overte, že obe zariadenia sú stále v tej istej Wi-Fi.
{{% /details %}}

{{% details title="Môžem sa pripojiť cez WebDAV bez Wi-Fi?" closed="true" %}}
Áno, ak pripojíte svoj iPhone k Macu káblom. Everdisk potom zobrazí ďalšiu adresu káblového pripojenia, ktorú môže pripojený Mac otvoriť vo Finderi, čo funguje aj bez akejkoľvek Wi-Fi. Cez kábel sa k zariadeniu dostane len ten Mac.
{{% /details %}}

{{% details title="Je Everdisk zadarmo?" closed="true" %}}
Áno, Everdisk je zadarmo na stiahnutie a server WebDAV je súčasťou. Voliteľný jednorazový nákup Premium pridáva extra funkcie ako vlastné porty a prevod fotiek a videí. WebDAV môžete nastaviť a zdieľať súbory bez platenia.
{{% /details %}}

Chcete to vyskúšať? [Stiahnite si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a za pár minút pripojte svoj iPhone ako disk. Otázky alebo spätná väzba? Napíšte nám na **support@everappz.com**.
