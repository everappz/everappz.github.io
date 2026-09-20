---
title: "Ako nastaviť server FTP na iPhone a iPade na prenos súborov"
description: "Premeňte svoj iPhone alebo iPad na server FTP s aplikáciou Everdisk a prenášajte súbory z Macu, Windows PC, Linuxu, Androidu, FTP aplikácie ako FileZilla alebo z ďalšieho iPhonu cez Wi-Fi. Kompletné nastavenie, adresa a port ftp, hosťovský prístup a pripojenie krok za krokom pre každé zariadenie."
date: 2026-09-19
tags: ["everdisk", "ftp", "prenos súborov", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP server iPhone", "FTP server iPad", "ako nastaviť FTP na iPhone", "aplikácia ftp server iphone", "pripojiť FileZilla k iPhone", "Cyberduck iPhone FTP", "prenos súborov iPhone FTP", "ftp iphone do počítača", "ftp iphone na iphone", "pripojenie k FTP iPhonu z Windowsu", "adresa port ftp iphone", "anonymné ftp iphone", "zdieľanie súborov iphone ftp", "iphone ftp pre kameru nas"]
readingTime: 9
---

{{< author-byline >}}

FTP je stará spoľahlivá klasika prenosu súborov. Je tu desaťročia, a práve preto je taký užitočný: rozumie mu takmer čokoľvek, čo dokáže komunikovať so serverom. Fotoaparáty, smart TV, smerovače, sieťové disky, automatizačné nástroje a každá stolná FTP aplikácia ovládajú FTP. S aplikáciou [Everdisk](/products/everdisk) môžete spustiť server FTP na svojom iPhone alebo iPade, takže telefón sa stane miestom, ku ktorému sa tieto zariadenia a aplikácie môžu pripojiť a presúvať súbory.

Po FTP siahnite, keď ostatné možnosti nevyhovujú, napríklad pri staršom zariadení alebo aplikácii, ktorá sa vie pripojiť len cez FTP. Táto príručka pokrýva nastavenie a spôsob pripojenia z Macu, Windowsu, FTP aplikácie, Linuxu, Androidu a druhého iPhonu.

## Čo potrebujete

- iPhone alebo iPad s nainštalovanou aplikáciou [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Počítač, aplikáciu alebo zariadenie v **tej istej Wi-Fi sieti**.
- Súbory, ktoré chcete zdieľať, v priečinku Dokumenty aplikácie Everdisk alebo v priečinkoch, ktoré pridáte.

## Nastavenie servera FTP v aplikácii Everdisk

### Krok 1: Vyberte, čo chcete zdieľať a nastavte prístup

Otvorte Everdisk, prejdite na kartu **Zdieľanie** a ťuknite na **Čo zdieľať**. Priečinok Dokumenty sa zdieľa štandardne. Pridajte ďalšie pomocou **Pridať priečinok** a **Pridať súbor**.

Otvorte **Nastavenia**, potom **Zdieľanie**, potom **Prístup**. Zapnite **Úprava súborov**, ak chcete, aby ľudia mohli nahrávať, premenúvať a mazať, alebo ju vypnite, aby ste povolili len sťahovanie. Nastavte **Prihlasovacie meno** a **Heslo**, ak chcete prihlásenie, alebo ich nechajte prázdne, aby sa ktokoľvek mohol pripojiť ako hosť.

### Krok 2: Zapnite server FTP

Prejdite do **Nastavenia**, potom **Zdieľanie**, potom **Pripojenia** a zapnite **Ostatné aplikácie a zariadenia**. To je server FTP (nesie značku FTP).

### Krok 3: Spustite zdieľanie a poznačte si adresu

Vráťte sa na kartu **Zdieľanie** a ťuknite na **Štart**. Sekcia **How to Connect** zobrazuje adresu FTP. Vyzerá takto:

```
ftp://192.168.1.20:2121
```

Číslo za dvojbodkou je **port**, ktorý je štandardne **2121**. Prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vaša bude iná. Nechajte Everdisk otvorený na obrazovke, kým je zariadenie pripojené.

## Pripojenie z Macu

1. Otvorte **Finder**, zvoľte **Go**, potom **Connect to Server** (alebo stlačte **Command a K**).
2. Napíšte adresu FTP zobrazenú v aplikácii Everdisk, napríklad `ftp://192.168.1.20:2121`.
3. Kliknite na **Connect**, potom zvoľte **Guest** alebo zadajte svoje **Prihlasovacie meno** a **Heslo**.

Finder pripojí zdieľanie FTP, takže môžete prechádzať a kopírovať súbory do svojho Macu. Vezmite na vedomie, že Finder otvára FTP len na čítanie. Keď chcete nahrávať z Macu, použite FTP aplikáciu, ako je popísané nižšie.

## Pripojenie z Windowsu

1. Otvorte **File Explorer** a kliknite na panel s adresou navrchu.
2. Napíšte adresu FTP z aplikácie Everdisk, napríklad `ftp://192.168.1.20:2121`, a stlačte **Enter**.
3. Zadajte svoje **Prihlasovacie meno** a **Heslo**, ak ste ich nastavili, alebo pokračujte ako hosť.

Zdieľané súbory sa zobrazia v okne a môžete ich kopírovať do svojho PC.

## Pripojenie cez FTP aplikáciu (FileZilla, Cyberduck)

Na nahrávanie a plnú kontrolu je najlepším nástrojom FTP aplikácia. **FileZilla** a **Cyberduck** sú zadarmo a bežia na Windowse, Macu a Linuxe.

1. Otvorte aplikáciu a vytvorte nové pripojenie.
2. Nastavte **Host** na adresu vášho iPhonu vo Wi-Fi a **Port** na **2121**.
3. Pre prihlásenie zadajte svoje **Prihlasovacie meno** a **Heslo**, alebo zvoľte **Anonymous**, ak ste žiadne nenastavili.
4. Pripojte sa a presúvajte súbory oboma smermi (nahrávanie vyžaduje zapnutú Úprava súborov).

## Pripojenie z Linuxu

1. Otvorte svojho správcu súborov a zvoľte **Connect to Server** alebo **Other Locations**.
2. Zadajte adresu, napríklad `ftp://192.168.1.20:2121`.
3. Pripojte sa ako hosť alebo so svojím prihlásením.

Môžete tiež použiť ktoréhokoľvek FTP klienta pre Linux z terminálu a nasmerovať ho na toho istého hostiteľa a port 2121.

## Pripojenie z Androidu

Android nemá systémový prehliadač FTP, preto použite aplikáciu:

1. Nainštalujte FTP klienta ako **AndFTP**, **FTPCafe** alebo správcu súborov s podporou FTP ako **Solid Explorer**.
2. Pridajte pripojenie s hostiteľom, **portom 2121** a svojím prihlásením alebo Anonymous.
3. Prechádzajte a prenášajte.

## Pripojenie z ďalšieho iPhonu alebo iPadu

Aplikácia Súbory v iOS neobsahuje klienta FTP, preto na druhom zariadení použite jednu z týchto možností:

- **Vlastná karta Zariadenia aplikácie Everdisk.** Otvorte Everdisk, prejdite na **Zariadenia**, ťuknite na **Nové pripojenie**, zvoľte **FTP** a zadajte adresu, napríklad `ftp://192.168.1.20:2121`. Toto je najjednoduchšia cesta.
- **Špecializovaná FTP aplikácia** pre iOS s tým istým hostiteľom, portom 2121 a prihlásením.

## Pripojenie ďalšieho vybavenia: fotoaparáty, TV, smerovače a NAS

Práve tu FTP vyniká. Mnohé zariadenia majú zabudovaného FTP klienta, ktorý dokáže posielať alebo sťahovať súbory:

- **Fotoaparáty**, ktoré nahrávajú fotky cez FTP, ich môžu posielať priamo do vášho iPhonu.
- **Smart TV, smerovače, boxy NAS a automatizačné nástroje**, ktoré podporujú FTP, sa môžu pripojiť rovnako.

Nasmerujte ich na adresu vášho iPhonu vo Wi-Fi, port **2121** a svoje prihlásenie (alebo Anonymous), pomocou adresy zobrazenej v aplikácii Everdisk.

## Len na čítanie alebo na čítanie a zápis

Toto ovláda prepínač **Úprava súborov** v Nastavenia, Zdieľanie, Prístup. Zapnutý umožňuje ľuďom nahrávať, premenúvať a mazať. Vypnutý znamená, že môžu len sťahovať. Zvoľte len na čítanie, keď súbory rozdávate a nechcete, aby sa vo vašom telefóne čokoľvek zmenilo.

## Ako to ľudia využívajú v bežnom živote

- **Pripojte FileZilla k svojmu iPhonu** a nahrajte dávku súborov do telefónu naraz.
- **Nechajte starú aplikáciu alebo zariadenie, ktoré ovláda len FTP**, dostať sa k vašim súborom, keď sa nič iné nedokáže pripojiť.
- **Prijímajte fotky z fotoaparátu**, ktorý nahráva cez FTP.
- **Presúvajte súbory medzi iPhonom a iPadom** pomocou karty Zariadenia aplikácie Everdisk na prijímacom zariadení.

## Zopár tipov

- Nechajte Everdisk otvorený, kým je zariadenie pripojené, keďže iOS po chvíli pozastavuje aplikácie na pozadí.
- Na nahrávanie z Macu použite FileZilla alebo Cyberduck namiesto Finderu, pretože Finder otvára FTP len na čítanie.
- Pre najširšiu kompatibilitu nechajte prihlásenie prázdne a potom sa pripojte ako Anonymous, čo väčšina FTP klientov ponúka.
- FTP nešifruje svoju komunikáciu. V sieti, ktorej nedôverujete, použite namiesto toho [server SMB so šifrovaním](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Často kladené otázky

{{% details title="Aká je adresa a port FTP pre môj iPhone?" closed="true" %}}
Po spustení zdieľania Everdisk zobrazí adresu na obrazovke Zdieľanie. Vyzerá ako ftp://192.168.1.20:2121. 2121 je port, ktorý Everdisk používa pre FTP, a prvá časť je adresa vášho iPhonu vo Wi-Fi, takže vaša bude iná.
{{% /details %}}

{{% details title="Ako pripojím FileZilla alebo Cyberduck k svojmu iPhonu?" closed="true" %}}
Otvorte aplikáciu a vytvorte nové pripojenie. Nastavte Host na adresu vášho iPhonu vo Wi-Fi a Port na 2121. Zadajte svoje Prihlasovacie meno a Heslo, alebo zvoľte Anonymous, ak ste v aplikácii Everdisk žiadne nenastavili. Pripojte sa a môžete presúvať súbory oboma smermi, keď je zapnutá Úprava súborov.
{{% /details %}}

{{% details title="Môžem sa pripojiť k FTP svojho iPhonu z Windowsu?" closed="true" %}}
Áno. Otvorte File Explorer, kliknite na panel s adresou, napíšte adresu FTP z aplikácie Everdisk (napríklad ftp://192.168.1.20:2121) a stlačte Enter. Zadajte svoje prihlásenie, ak ste ho nastavili, alebo pokračujte ako hosť. Na nahrávanie a väčšiu kontrolu použite namiesto toho FTP aplikáciu ako FileZilla.
{{% /details %}}

{{% details title="Potrebujem prihlásenie pre FTP?" closed="true" %}}
Nie, prihlásenie je voliteľné. Nechajte Prihlasovacie meno a Heslo prázdne v Nastavenia, Zdieľanie, Prístup a pripojte sa ako Anonymous, čo väčšina FTP klientov ponúka. Nastavte prihlásenie, ak chcete, aby sa pripojenia najprv prihlásili.
{{% /details %}}

{{% details title="Prečo môžem len sťahovať a nie nahrávať cez FTP?" closed="true" %}}
Bežné sú dva dôvody. Po prvé, prepínač Úprava súborov v Nastavenia, Zdieľanie, Prístup musí byť zapnutý, aby povolil nahrávanie, premenovanie a mazanie. Po druhé, Finder na Macu otvára FTP len na čítanie, preto na nahrávanie použite FTP aplikáciu ako FileZilla alebo Cyberduck.
{{% /details %}}

{{% details title="Môžem použiť FTP medzi dvoma iPhonmi?" closed="true" %}}
Áno. Spustite server FTP na prvom iPhone. Na druhom otvorte Everdisk, prejdite na kartu Zariadenia, ťuknite na Nové pripojenie, zvoľte FTP a zadajte adresu zobrazenú na prvom telefóne. Funguje aj špecializovaná FTP aplikácia pre iOS, keďže aplikácia Súbory v iOS neobsahuje klienta FTP.
{{% /details %}}

{{% details title="Je FTP bezpečné?" closed="true" %}}
Obyčajné FTP nešifruje svoju komunikáciu, preto ho berte ako nástroj pre siete, ktorým dôverujete, ako je vaša domáca Wi-Fi. V sieti, ktorú neovládate, použite server SMB so zapnutým Vyžadovať šifrovanie SMB, ktorý chráni každý prenos.
{{% /details %}}

{{% details title="Ktoré zariadenia sa môžu pripojiť cez FTP?" closed="true" %}}
Takmer čokoľvek s FTP klientom. To zahŕňa počítače Mac, Windows a Linux, FTP aplikácie ako FileZilla a Cyberduck, správcov súborov pre Android a hardvér ako fotoaparáty, smart TV, smerovače, boxy NAS a automatizačné nástroje. Práve tento široký dosah je hlavným dôvodom voľby FTP.
{{% /details %}}

{{% details title="Prečo mi vypadlo pripojenie FTP?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikácie, ktoré zostávajú príliš dlho na pozadí. Nechajte Everdisk otvorený na obrazovke, kým je zariadenie pripojené, a počas dlhých prenosov pripojte k napájaniu. Tiež sa uistite, že obe zariadenia sú stále v tej istej Wi-Fi.
{{% /details %}}

{{% details title="Je Everdisk zadarmo?" closed="true" %}}
Áno, Everdisk je zadarmo na stiahnutie a server FTP je súčasťou. Voliteľný jednorazový nákup Premium pridáva extra funkcie ako vlastné porty a prevod fotiek a videí. FTP môžete nastaviť a prenášať súbory bez platenia.
{{% /details %}}

Chcete to vyskúšať? [Stiahnite si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a za pár minút pripojte svojho prvého FTP klienta. Otázky alebo spätná väzba? Napíšte nám na **support@everappz.com**.
