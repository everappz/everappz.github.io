---
title: "Ako nastaviť server SMB na iPhone a iPade na zdieľanie súborov"
description: "Premeňte svoj iPhone alebo iPad na súborový server SMB s aplikáciou Everdisk a otvorte ho ako sieťový disk z Macu, ďalšieho iPhonu, Linuxu alebo Androidu cez Wi-Fi. Kompletné nastavenie, adresa a port smb, voliteľné šifrovanie SMB3 a pripojenie krok za krokom pre každé zariadenie."
date: 2026-09-19
tags: ["everdisk", "smb", "zdieľanie súborov", "sieťový disk", "iphone", "ipad", "mac", "finder", "šifrovanie", "wifi"]
keywords: ["SMB server iPhone", "SMB server iPad", "ako nastaviť SMB na iPhone", "SMB zdieľanie iPhone", "pripojiť iPhone SMB Mac Finder", "smb iphone na iphone", "aplikácia Súbory iOS pripojenie k serveru SMB", "zdieľanie súborov iPhone SMB", "iphone sieťový disk Finder", "šifrovanie SMB3 iOS", "smb zdieľanie iPhone Android", "pripojenie k SMB z Linuxu", "iphone ako sieťový disk", "zdieľanie súborov medzi iphonmi wifi", "namapovať iphone ako sieťový disk"]
readingTime: 10
---

{{< author-byline >}}

SMB je zdieľanie súborov zabudované do macOS, Windowsu a Linuxu a takmer do každého sieťového disku (NAS). Keď sa pripojíte k zdieľanému priečinku na inom počítači a otvorí sa ako bežný disk vo Finderi alebo Prieskumníkovi súborov, robí to práve SMB. S aplikáciou [Everdisk](/products/everdisk) môžete umiestniť zdieľanie SMB na svoj iPhone alebo iPad, takže samotný telefón sa zobrazí ako sieťový disk, ktorý iné zariadenia prechádzajú, kopírujú z neho aj naň.

Toto je možnosť, po ktorej siahnuť, keď chcete, aby sa váš iPhone správal ako riadny disk, nie ako webová stránka. Je rýchly, presúva sa oboma smermi a je to jediný typ pripojenia v aplikácii Everdisk, ktorý dokáže zašifrovať každý prenos. Táto príručka pokrýva nastavenie a spôsob pripojenia z Macu, ďalšieho iPhonu alebo iPadu, Linuxu, Androidu a Windowsu.

## Čo potrebujete

- iPhone alebo iPad s nainštalovanou aplikáciou [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Ďalšie zariadenie v **tej istej Wi-Fi sieti**.
- Súbory, ktoré chcete zdieľať, v priečinku Dokumenty aplikácie Everdisk alebo v priečinkoch, ktoré pridáte.

## Nastavenie servera SMB v aplikácii Everdisk

### Krok 1: Vyberte, čo chcete zdieľať a kto môže zapisovať

Otvorte Everdisk, prejdite na kartu **Zdieľanie** a ťuknite na **Čo zdieľať**. Priečinok Dokumenty sa zdieľa štandardne. Pridajte ďalšie pomocou **Pridať priečinok** a **Pridať súbor** a zapnite svoju knižnicu Fotky alebo Hudba, ak chcete, aby boli dostupné aj tie.

Rozhodnite sa, či iné zariadenia môžu vaše súbory len čítať, alebo ich aj meniť. Otvorte **Nastavenia**, potom **Zdieľanie**, potom **Prístup** a nastavte **Úprava súborov**. Keď je zapnutá, pripojené zariadenia môžu kopírovať súbory do vášho telefónu a premenovať alebo mazať ich. Keď je vypnutá, zdieľanie je len na čítanie.

Ak chcete prihlásenie, nastavte na tej istej obrazovke Prístup **Prihlasovacie meno** a **Heslo**. Ak necháte obidve prázdne, povolíte hosťovský prístup.

### Krok 2: Zapnite server SMB

Prejdite do **Nastavenia**, potom **Zdieľanie**, potom **Pripojenia** a zapnite **Počítač (pokročilé)**. To je server SMB (nesie značku SMB).

### Krok 3: Spustite zdieľanie a poznačte si adresu

Vráťte sa na kartu **Zdieľanie** a ťuknite na **Štart**. Sekcia **How to Connect** teraz zobrazuje adresu SMB. Vyzerá takto:

```
smb://192.168.1.20:4455/Share
```

Tri veci, ktoré treba o tejto adrese vedieť:

- Číslo za dvojbodkou je **port**. Everdisk používa štandardne **4455**.
- Zdieľanie sa volá **Share**.
- Prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vo vašej sieti bude iná.

Nechajte Everdisk otvorený, kým sú zariadenia pripojené, pretože iOS pozastavuje aplikácie, ktoré príliš dlho sedia na pozadí.

## Pripojenie z Macu

Toto je najhladší prípad, pretože macOS ovláda SMB natívne.

Najrýchlejší spôsob: otvorte **Finder** a pozrite sa v bočnom paneli pod **Locations** alebo **Network**. Everdisk sa ohlasuje vo Wi-Fi, takže váš iPhone sa tam často zobrazí sám. Kliknite naň, potom kliknite na **Connect As** a zvoľte **Guest** alebo zadajte svoje prihlásenie.

Pripojenie ručne:

1. Vo Finderi zvoľte **Go**, potom **Connect to Server** (alebo stlačte **Command a K**).
2. Napíšte adresu SMB zobrazenú v aplikácii Everdisk, napríklad `smb://192.168.1.20:4455/Share`.
3. Kliknite na **Connect**, potom vyberte **Guest** alebo zadajte svoje **Prihlasovacie meno** a **Heslo**.

Váš iPhone sa otvorí v okne Finderu. Súbory kopírujte dnu alebo von presúvaním, presne ako pri akomkoľvek inom disku (ak je zapnutá Úprava súborov).

## Pripojenie z ďalšieho iPhonu alebo iPadu

iOS a iPadOS dokážu otvoriť zdieľania SMB v zabudovanej aplikácii **Súbory**, čo robí prenosy medzi telefónmi čisté a rýchle.

Na druhom zariadení:

1. Otvorte aplikáciu **Súbory**.
2. Ťuknite na tlačidlo **more** (tri bodky, vpravo hore na iPhone) a zvoľte **Connect to Server**.
3. Zadajte adresu SMB z aplikácie Everdisk, napríklad `smb://192.168.1.20:4455/Share`.
4. Zvoľte **Guest**, alebo **Registered User** a zadajte svoje prihlásenie.
5. Zdieľanie sa zobrazí pod Locations v aplikácii Súbory. Prechádzajte a kopírujte v oboch smeroch.

Na druhom zariadení môžete použiť aj vlastnú kartu **Zariadenia** aplikácie Everdisk, ktorá obsahuje klienta SMB. Otvorte Everdisk, prejdite na **Zariadenia**, ťuknite na **Nové pripojenie**, zvoľte **SMB** a zadajte adresu.

## Pripojenie z Linuxu

1. Otvorte svojho správcu súborov (Files/Nautilus na GNOME, Dolphin na KDE).
2. Zvoľte **Other Locations** alebo **Connect to Server**.
3. Zadajte adresu, napríklad `smb://192.168.1.20:4455/Share`.
4. Pripojte sa ako hosť alebo zadajte svoje prihlásenie.

Z terminálu môžete tiež spustiť `smbclient //192.168.1.20/Share -p 4455` a po vyzvaní zadať svoje prihlásenie.

## Pripojenie z Androidu

Android nemá systémový prehliadač SMB, preto použite správcu súborov, ktorý podporuje SMB:

1. Nainštalujte aplikáciu ako **CX File Explorer**, **Solid Explorer** alebo **X-plore File Manager**.
2. Pridajte nové pripojenie **SMB** alebo **LAN**.
3. Zadajte hostiteľa (adresu vášho iPhonu vo Wi-Fi), nastavte **port na 4455** a názov zdieľania **Share**.
4. Pripojte sa ako hosť alebo so svojím prihlásením, potom prechádzajte a kopírujte.

## Pripojenie z Windowsu

Windows dokáže čítať zdieľania SMB, s jedným háčikom, ktorý sa oplatí vedieť vopred. Zabudovaný Prieskumník súborov komunikuje so SMB len na štandardnom porte a neumožňuje zadať vlastný port v ceste a Everdisk používa port 4455. Takže obyčajná cesta cez **Map network drive** sa k nemu často nedostane.

Vo Windowse máte dve dobré možnosti:

- Použite správcu súborov alebo klienta SMB, ktorý umožňuje nastaviť vlastný port, a nasmerujte ho na adresu vášho iPhonu s portom **4455** a názvom zdieľania **Share**.
- Alebo sa z Windowsu pripojte namiesto toho pomocou iného zo serverov aplikácie Everdisk. [Nastavenie WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) aj [nastavenie FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) fungujú z Prieskumníka súborov Windowsu dobre a odkaz prehliadača funguje v ktoromkoľvek prehliadači.

Ak chcete predsa len skúsiť Map network drive: otvorte **File Explorer**, kliknite pravým tlačidlom na **This PC**, zvoľte **Map network drive** a zadajte hostiteľa a názov zdieľania zobrazený v aplikácii Everdisk. Ak sa nedokáže pripojiť, je to práve to obmedzenie portu vyššie, takže prejdite na WebDAV alebo FTP.

## Zapnite šifrovanie pre nedôveryhodnú Wi-Fi

SMB je jediné pripojenie Everdisk, ktoré dokáže zašifrovať každý prenos, čo je dôležité vo Wi-Fi, ktorú úplne neovládate, napríklad v kaviarni alebo firemnej sieti.

1. V **Nastaveniach**, **Zdieľanie**, **Prístup** nastavte **Prihlasovacie meno** a **Heslo**. Šifrované pripojenia nemôžu byť anonymné, takže tento krok je potrebný.
2. V **Nastaveniach**, **Zdieľanie** zapnite **Vyžadovať šifrovanie SMB**.
3. Zastavte a znova spustite zdieľanie, aby sa zmena prejavila.

Každý prenos cez SMB je potom chránený **šifrovaním SMB3 (AES)**. Pripájajúce sa zariadenie musí podporovať SMB3, čo Finder na modernom Macu aj Windows 10 alebo novší spĺňajú. Šifrovanie SMB je súčasťou jednorazového nákupu Premium.

## Len na čítanie alebo na čítanie a zápis

Prepínač **Úprava súborov** v Nastavenia, Zdieľanie, Prístup toto ovláda pre každý server, vrátane SMB. Zapnite ho a pripojené zariadenia môžu nahrávať, premenúvať a mazať. Vypnite ho a môžu len prechádzať a kopírovať súbory z vášho telefónu. Zvoľte len na čítanie, keď odovzdávate súbory niekomu, komu nechcete dovoliť čokoľvek meniť.

## Ako to ľudia využívajú v bežnom živote

- **Presuňte veľký priečinok do svojho iPhonu z Macu** jeho pretiahnutím do okna Finderu, rýchlejšie ako webové nahrávanie.
- **Stiahnite si celodenné fotky a videá z telefónu** do notebooku bez iTunes alebo kábla.
- **Posielajte súbory medzi dvoma iPhonmi** cez aplikáciu Súbory, bez tretej aplikácie na oboch stranách.
- **Pracujte so súborom na mieste**, otvorte dokument priamo z telefónu v aplikácii na Macu a uložte ho späť.

## Zopár tipov

- Nechajte Everdisk otvorený, kým je zariadenie pripojené. Dlhé zamknutie telefónu môže aplikáciu pozastaviť a prerušiť pripojenie.
- Ak Mac nevidí telefón v bočnom paneli Finderu, pripojte sa ručne cez Connect to Server a plnú adresu smb.
- Pre najlepšiu rýchlosť pri veľkých prenosoch ponechajte kvalitu fotiek a videa na Original v Nastaveniach.
- V nedôveryhodnej sieti zapnite Vyžadovať šifrovanie SMB a počas práce ostatné servery vypnite.

## Často kladené otázky

{{% details title="Aká je adresa a port SMB pre môj iPhone?" closed="true" %}}
Po spustení zdieľania Everdisk zobrazí adresu na obrazovke Zdieľanie. Vyzerá ako smb://192.168.1.20:4455/Share. 4455 je port, ktorý Everdisk používa pre SMB, a Share je názov zdieľaného priečinka. Prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vaša bude iná.
{{% /details %}}

{{% details title="Môžem sa pripojiť k zdieľaniu SMB svojho iPhonu z Windowsu?" closed="true" %}}
Prieskumník súborov Windowsu sa pripája k SMB len na štandardnom porte a neprijíma vlastný port v ceste, zatiaľ čo Everdisk používa port 4455. Takže obyčajná cesta cez Map network drive sa k nemu často nedostane. Použite správcu súborov, ktorý umožňuje nastaviť vlastný port, alebo sa z Windowsu pripojte namiesto toho cez WebDAV, FTP alebo odkaz prehliadača. Všetky tieto fungujú z Windowsu bez problémov s portom.
{{% /details %}}

{{% details title="Ako zdieľam súbory medzi dvoma iPhonmi cez SMB?" closed="true" %}}
Spustite server SMB na prvom iPhone v aplikácii Everdisk. Na druhom iPhone otvorte aplikáciu Súbory, ťuknite na tlačidlo more, zvoľte Connect to Server a zadajte adresu smb zobrazenú v aplikácii Everdisk (napríklad smb://192.168.1.20:4455/Share). Pripojte sa ako Guest alebo so svojím prihlásením a zdieľanie sa zobrazí v aplikácii Súbory. Na druhom telefóne môžete použiť aj vlastnú kartu Zariadenia aplikácie Everdisk.
{{% /details %}}

{{% details title="Zobrazí sa môj iPhone v bočnom paneli Finderu na Macu automaticky?" closed="true" %}}
Zvyčajne áno. Everdisk ohlasuje zdieľanie SMB vo vašej Wi-Fi, takže váš iPhone sa často zobrazí pod Locations alebo Network v bočnom paneli Finderu. Kliknite naň a zvoľte Connect As, potom Guest alebo svoje prihlásenie. Ak sa nezobrazí, pripojte sa ručne cez Go, Connect to Server a plnú adresu smb.
{{% /details %}}

{{% details title="Potrebujem heslo na použitie SMB?" closed="true" %}}
Nie, prihlásenie je voliteľné. Nechajte Prihlasovacie meno a Heslo prázdne v Nastavenia, Zdieľanie, Prístup, aby ste povolili hosťovský prístup. Nastavte ich, ak chcete, aby sa pripojenia prihlasovali. Prihlasovacie meno a heslo sú potrebné len vtedy, ak zapnete Vyžadovať šifrovanie SMB, pretože šifrované pripojenia nemôžu byť anonymné.
{{% /details %}}

{{% details title="Je pripojenie SMB šifrované?" closed="true" %}}
Môže byť. SMB je jediné pripojenie Everdisk, ktoré podporuje šifrovanie. Nastavte prihlasovacie meno a heslo, potom v Nastavenia, Zdieľanie zapnite Vyžadovať šifrovanie SMB. Každý prenos je potom chránený SMB3 (AES). Druhé zariadenie musí podporovať SMB3, čo moderné Macy a Windows 10 alebo novší spĺňajú. Šifrovanie je funkcia Premium.
{{% /details %}}

{{% details title="Môžu ľudia meniť alebo mazať moje súbory cez SMB?" closed="true" %}}
Len ak to povolíte. Prepínač Úprava súborov v Nastavenia, Zdieľanie, Prístup toto ovláda. Keď je zapnutý, pripojené zariadenia môžu nahrávať, premenúvať a mazať. Keď je vypnutý, zdieľanie je len na čítanie a ostatní môžu prechádzať a kopírovať súbory z vášho telefónu, ale nemôžu nič meniť.
{{% /details %}}

{{% details title="Prečo mi vypadlo pripojenie SMB?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikácie, ktoré zostávajú príliš dlho na pozadí. Nechajte Everdisk otvorený na obrazovke, kým je zariadenie pripojené, a počas dlhých prenosov pripojte telefón k napájaniu. Tiež sa uistite, že obe zariadenia zostali v tej istej Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV alebo FTP, ktorý mám použiť?" closed="true" %}}
Použite SMB, keď chcete, aby sa telefón správal ako skutočný sieťový disk na Macu, ďalšom iPhone, Linuxe alebo NAS, a keď chcete šifrovanie. Použite WebDAV, keď chcete sieťový disk, ktorý dobre funguje aj z Windowsu. Použite FTP pre najširšiu kompatibilitu so staršími zariadeniami a aplikáciami. Everdisk môže bežať všetky naraz, takže nie ste viazaní na jeden.
{{% /details %}}

{{% details title="Je Everdisk zadarmo?" closed="true" %}}
Áno, Everdisk je zadarmo na stiahnutie a server SMB je súčasťou. Voliteľný jednorazový nákup Premium pridáva šifrovanie SMB, vlastné porty a niekoľko ďalších extra funkcií. SMB môžete nastaviť a zdieľať súbory bez platenia.
{{% /details %}}

Chcete to vyskúšať? [Stiahnite si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a otvorte svoj iPhone vo Finderi asi za minútu. Otázky alebo spätná väzba? Napíšte nám na **support@everappz.com**.
