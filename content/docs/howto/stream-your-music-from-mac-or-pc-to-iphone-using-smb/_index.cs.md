---
title: "Streamujte hudbu z Macu nebo PC na iPhone pomocí SMB"
description: "Naučte se, jak streamovat svou hudební sbírku z Macu nebo Windows PC na iPhone nebo iPad pomocí Evermusic a protokolu SMB. Jednoduchý průvodce krok za krokem pro připojení a poslech zvuku bez synchronizace."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streamování hudby z Mac na iPhone", "SMB audio streaming iOS", "nastavení Evermusic SMB", "připojení hudby z PC na iPhone", "sdílení hudby Mac iOS", "SMB Windows streamování souborů", "přístup Evermusic ke složkám PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Shrnutí:** Použijte aplikaci Evermusic pro iPhone nebo iPad ke streamování hudby z Macu nebo Windows PC přes vaši lokální síť pomocí SMB. Žádná synchronizace, žádné kopírování -- stačí povolit sdílení souborů na počítači, připojit se v aplikaci a přehrávat. Nastavení trvá méně než 5 minut.

Topíte se v moři hudby na svém MAC nebo PC a chcete si ji bez starostí užívat na iPhonu nebo iPadu? Nehledejte dál než Evermusic. S Evermusic je neuvěřitelně jednoduché připojit svůj počítač pomocí protokolu SMB a streamovat své oblíbené melodie bez starostí o zabírání místa na zařízení nebo řešení problémů se synchronizací. Zde je průvodce krok za krokem:

## Krok 1: Povolte protokol SMB na vašem počítači

![Evermusic - Podpora SMB - Obrazovka sdílení na Macu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Pokud používáte MAC

- Otevřete Předvolby systému -> Sdílení.
- Povolte službu Sdílení souborů.
- V sekci "Sdílené složky" přidejte svou složku s hudbou, vyberte uživatele a nastavte úrovně oprávnění (Čtení a zápis nebo Pouze čtení).
- Pro větší pohodlí můžete vybrat "Všichni: Pouze čtení" pro složku s hudbou, čímž ji snadno zpřístupníte v Evermusic.
- Nezapomeňte si zapamatovat URL vašeho počítače (smb://192.168.xx.xx) pro další kroky.

![Evermusic - Podpora SMB - Obrazovka sdílení souborů](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Klepněte na "Možnosti" a povolte "Sdílet soubory a složky pomocí SMB."
- Povolte "Sdílení souborů Windows" pro dostupné účty.

![Evermusic - Podpora SMB - Obrazovka sdílení souborů a složek](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Pokud používáte Windows PC

![Evermusic - Podpora SMB - Sdílení souborů ve Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Klikněte pravým tlačítkem na složku s hudbou.
- Vyberte "Vlastnosti."
- Otevřete záložku "Sdílení."
- Klikněte na "Sdílet..."
- Vyberte lidi, se kterými chcete sdílet, a nastavte jejich úrovně oprávnění.
- Stejně jako u MAC můžete zvolit "Všichni: Čtení" pro vybranou složku s hudbou.
- Klikněte na "Hotovo" pro uložení nastavení.

![Evermusic - Podpora SMB - Sdílená složka ve Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Krok 2: Přidejte svůj počítač automaticky

- Nyní otevřete Evermusic a přejděte na záložku "Připojení" ("Síť" pokud používáte starší verzi aplikace).
- Pokud vidíte svůj počítač v sekci "Dostupná zařízení" ("Dostupná sdílení" pokud používáte starší verzi aplikace) a v předchozím kroku jste vybrali "Všichni: Pouze čtení", stačí klepnout na svůj počítač a připojí se automaticky.
- Pokud se to nestane, můžete svůj počítač přidat ručně.

![Evermusic - Podpora SMB - Obrazovka připojení účtu](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Krok 3: Přidejte svůj počítač ručně

- Klepněte na "Připojit cloudovou službu" ("Přidat účet" pokud používáte starší verzi aplikace)
- Na další obrazovce vyberte "SMB" ze seznamu dostupných serverů.
- Na obrazovce nastavení "SMB":
  - Zadejte URL serveru s cestou ke sdílené složce. Můžete zadat název serveru nebo IP serveru. Například:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Zadejte své přihlašovací jméno a heslo nebo ponechte tato pole prázdná, pokud jste v předchozím kroku vybrali "Všichni: Pouze čtení".
  - Pole "WORKGROUP" je volitelné a mělo by se použít, pokud máte doménu Active Directory.

![Evermusic - Podpora SMB - Obrazovka zadání přihlašovacích údajů](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Po připojení vašeho účtu SMB se zobrazí v sekci "Cloudové služby" ("Účty"). Otevřete připojený účet klepnutím na něj, přejděte do složky s hudbou a klepněte na libovolný audio soubor pro spuštění přehrávače.

![Evermusic - Podpora SMB - Obrazovka otevření připojené složky](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Užívejte si svou hudební sbírku plynule na iPhonu nebo iPadu s Evermusic.

![Evermusic - Podpora SMB - Obrazovka audio přehrávače](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Krok 4: Řešení pro SMB2

Pokud narazíte na problémy s procházením složek nebo přehráváním souborů obsahujících speciální znaky (jako ü, ö, é), může to souviset s protokolem SMB2. Na řešení tohoto problému aktivně pracujeme.

Jako dočasné řešení zkuste povolit SMB 1 na vašem serveru a v nastavení aplikace. Alternativně se můžete připojit k serveru SMB pomocí systémové nabídky otevření souborů. Postupujte takto:

1. Přejděte na "Lokální soubory."
2. Posuňte se dolů k sekci "Soubory na tomto zařízení" a klepněte na "Otevřít soubory..." nebo "Otevřít složky..."
3. Najděte svůj server a vyberte potřebné soubory nebo složky.
4. Klepněte na "Otevřít" pro potvrzení výběru.

## Krok 5: Řešení s WebDAV

Kromě toho můžete zkusit připojení k vašemu NAS pomocí protokolů WebDAV nebo DLNA, pokud jsou podporovány.

Dodržením těchto kroků můžete obejít problémy související se speciálními znaky v názvech souborů a pokračovat v užívání svých mediálních souborů.

P.S. Můžete také přenést audio soubory z MAC/PC na iPhone pomocí sdílení souborů iTunes a přehrávat lokální audio soubory. Více o této funkci se dozvíte v našem průvodci: [Jak přehrávat soubory iTunes na iPhonu](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Často kladené dotazy

{{% details title="Mohu streamovat hudbu z PC na iPhone bez iTunes?" closed="true" %}}
Ano. Evermusic se připojuje k vašemu PC přes SMB na vaší lokální Wi-Fi síti. iTunes není potřeba. Stačí povolit sdílení souborů na PC a připojit se v aplikaci.
{{% /details %}}

{{% details title="Používá SMB streaming mobilní data?" closed="true" %}}
Ne. SMB funguje přes vaši lokální Wi-Fi síť. Není potřeba připojení k internetu ani mobilní data.
{{% /details %}}

{{% details title="Jaké audio formáty Evermusic podporuje přes SMB?" closed="true" %}}
Evermusic podporuje MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC a další běžné audio formáty. Soubory se přehrávají přímo ze sdílení SMB.
{{% /details %}}

{{% details title="Mohu streamovat hudbu z NAS na iPhone?" closed="true" %}}
Ano. Pokud váš NAS podporuje SMB (většina ano, včetně Synology, QNAP a WD My Cloud), můžete se k němu připojit pomocí stejných kroků v tomto průvodci.
{{% /details %}}

{{% details title="Musím mít počítač zapnutý při streamování?" closed="true" %}}
Ano. Protože Evermusic streamuje soubory přímo z vašeho počítače, musí být zapnutý a připojený ke stejné síti jako váš iPhone.
{{% /details %}}

{{% details title="Existuje limit velikosti souboru pro SMB streaming?" closed="true" %}}
Ne. Evermusic streamuje soubory libovolné velikosti přes SMB. Velké bezztrátové soubory (FLAC, WAV) fungují bez problémů.
{{% /details %}}
