---
title: "Streamujte hudbu z Macu alebo PC na iPhone pomocou SMB"
description: "Naučte sa, ako streamovať svoju hudobnú zbierku z Macu alebo Windows PC na iPhone alebo iPad pomocou Evermusic a protokolu SMB. Jednoduchý sprievodca krok za krokom na pripojenie a počúvanie zvuku bez synchronizácie."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streamovanie hudby z Mac na iPhone", "SMB audio streaming iOS", "nastavenie Evermusic SMB", "pripojenie hudby z PC na iPhone", "zdieľanie hudby Mac iOS", "SMB Windows streamovanie súborov", "prístup Evermusic k priečinkom PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Zhrnutie:** Použite aplikáciu Evermusic pre iPhone alebo iPad na streamovanie hudby z vášho Macu alebo Windows PC cez lokálnu sieť pomocou SMB. Žiadna synchronizácia, žiadne kopírovanie -- stačí povoliť zdieľanie súborov na počítači, pripojiť sa v aplikácii a prehrávať. Nastavenie trvá menej ako 5 minút.

Topíte sa v mori hudby na svojom MAC alebo PC a chcete si ju bezstarostne užívať na iPhone alebo iPade? Nehľadajte ďalej ako Evermusic. S Evermusic je neuveriteľne jednoduché pripojiť váš počítač pomocou protokolu SMB a streamovať vaše obľúbené melódie bez starostí o zaberanie miesta na zariadení alebo riešenie problémov so synchronizáciou. Tu je sprievodca krok za krokom:

## Krok 1: Povoľte protokol SMB na vašom počítači

![Evermusic - Podpora SMB - Obrazovka zdieľania na Macu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Ak používate MAC

- Otvorte Predvoľby systému -> Zdieľanie.
- Povoľte službu Zdieľanie súborov.
- V sekcii "Zdieľané priečinky" pridajte svoj hudobný priečinok, vyberte používateľa a nastavte úrovne oprávnení (Čítanie a zápis alebo Len čítanie).
- Pre väčšie pohodlie môžete vybrať "Všetci: Len čítanie" pre hudobný priečinok, čím ho sprístupníte v Evermusic.
- Nezabudnite si zapamätať URL vášho počítača (smb://192.168.xx.xx) pre ďalšie kroky.

![Evermusic - Podpora SMB - Obrazovka zdieľania súborov](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Klepnite na "Možnosti" a povoľte "Zdieľať súbory a priečinky pomocou SMB."
- Povoľte "Zdieľanie súborov Windows" pre dostupné účty.

![Evermusic - Podpora SMB - Obrazovka zdieľania súborov a priečinkov](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Ak používate Windows PC

![Evermusic - Podpora SMB - Zdieľanie súborov vo Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Kliknite pravým tlačidlom na hudobný priečinok.
- Vyberte "Vlastnosti."
- Otvorte záložku "Zdieľanie."
- Kliknite na "Zdieľať..."
- Vyberte ľudí, s ktorými chcete zdieľať, a nastavte ich úrovne oprávnení.
- Rovnako ako na MAC môžete zvoliť "Všetci: Čítanie" pre vybraný hudobný priečinok.
- Kliknite na "Hotovo" pre uloženie nastavení.

![Evermusic - Podpora SMB - Zdieľaný priečinok vo Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Pridajte počítač automaticky

- Teraz otvorte Evermusic a prejdite na záložku "Pripojenia" ("Sieť" ak používate staršiu verziu aplikácie).
- Ak vidíte svoj počítač v sekcii "Dostupné zariadenia" ("Dostupné zdieľania" ak používate staršiu verziu aplikácie) a v predchádzajúcom kroku ste vybrali "Všetci: Len čítanie", stačí klepnúť na počítač a pripojí sa automaticky.
- Ak sa to nestane, môžete počítač pridať ručne.

![Evermusic - Podpora SMB - Obrazovka pripojenia účtu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Krok 3: Pridajte počítač ručne

- Klepnite na "Pripojiť cloudovú službu" ("Pridať účet" ak používate staršiu verziu aplikácie)
- Na ďalšej obrazovke vyberte "SMB" zo zoznamu dostupných serverov.
- Na obrazovke nastavení "SMB":
  - Zadajte URL servera s cestou k zdieľanému priečinku. Môžete zadať názov servera alebo IP servera. Napríklad:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Zadajte prihlasovacie meno a heslo alebo nechajte tieto polia prázdne, ak ste v predchádzajúcom kroku vybrali "Všetci: Len čítanie".
  - Pole "WORKGROUP" je voliteľné a malo by sa použiť, ak máte doménu Active Directory.

![Evermusic - Podpora SMB - Obrazovka zadania prihlasovacích údajov](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Po pripojení účtu SMB sa zobrazí v sekcii "Cloudové služby" ("Účty"). Otvorte pripojený účet klepnutím naň, prejdite do hudobného priečinka a klepnite na ľubovoľný audio súbor pre spustenie prehrávača.

![Evermusic - Podpora SMB - Obrazovka otvorenia pripojeného priečinka](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Užívajte si svoju hudobnú zbierku plynulo na iPhone alebo iPade s Evermusic.

![Evermusic - Podpora SMB - Obrazovka audio prehrávača](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Krok 4: Riešenie pre SMB2

Ak narazíte na problémy s prehliadaním priečinkov alebo prehrávaním súborov obsahujúcich špeciálne znaky (ako ü, ö, é), môže to súvisieť s protokolom SMB2. Na riešení tohto problému aktívne pracujeme.

Ako dočasné riešenie skúste povoliť SMB 1 na vašom serveri a v nastaveniach aplikácie. Alternatívne sa môžete pripojiť k serveru SMB pomocou systémovej ponuky otvorenia súborov. Postupujte takto:

1. Prejdite na "Lokálne súbory."
2. Posuňte sa nadol k sekcii "Súbory na tomto zariadení" a klepnite na "Otvoriť súbory..." alebo "Otvoriť priečinky..."
3. Nájdite svoj server a vyberte potrebné súbory alebo priečinky.
4. Klepnite na "Otvoriť" pre potvrdenie výberu.

## Krok 5: Riešenie s WebDAV

Okrem toho môžete skúsiť pripojenie k vášmu NAS pomocou protokolov WebDAV alebo DLNA, ak sú podporované.

Dodržaním týchto krokov môžete obísť problémy súvisiace so špeciálnymi znakmi v názvoch súborov a pokračovať v užívaní si mediálnych súborov.

P.S. Môžete tiež preniesť audio súbory z MAC/PC na iPhone pomocou zdieľania súborov iTunes a prehrávať lokálne audio súbory. Viac o tejto funkcii sa dozviete v našom sprievodcovi: [Ako prehrávať súbory iTunes na iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Často kladené otázky

{{% details title="Môžem streamovať hudbu z PC na iPhone bez iTunes?" closed="true" %}}
Áno. Evermusic sa pripojí k vášmu PC cez SMB vo vašej lokálnej Wi-Fi sieti. iTunes nie je potrebný. Stačí povoliť zdieľanie súborov na PC a pripojiť sa v aplikácii.
{{% /details %}}

{{% details title="Používa SMB streaming mobilné dáta?" closed="true" %}}
Nie. SMB funguje cez vašu lokálnu Wi-Fi sieť. Nie je potrebné internetové pripojenie ani mobilné dáta.
{{% /details %}}

{{% details title="Aké audio formáty Evermusic podporuje cez SMB?" closed="true" %}}
Evermusic podporuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC a ďalšie bežné audio formáty. Súbory sa prehrávajú priamo zo zdieľania SMB.
{{% /details %}}

{{% details title="Môžem streamovať hudbu z NAS na iPhone?" closed="true" %}}
Áno. Ak váš NAS podporuje SMB (väčšina áno, vrátane Synology, QNAP a WD My Cloud), môžete sa k nemu pripojiť pomocou rovnakých krokov v tomto sprievodcovi.
{{% /details %}}

{{% details title="Musím mať počítač zapnutý počas streamovania?" closed="true" %}}
Áno. Keďže Evermusic streamuje súbory priamo z vášho počítača, musí byť zapnutý a pripojený k rovnakej sieti ako váš iPhone.
{{% /details %}}

{{% details title="Existuje limit veľkosti súboru pre SMB streaming?" closed="true" %}}
Nie. Evermusic streamuje súbory akejkoľvek veľkosti cez SMB. Veľké bezstratové súbory (FLAC, WAV) fungujú bez problémov.
{{% /details %}}
