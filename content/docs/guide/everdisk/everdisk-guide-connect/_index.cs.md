---
title: "Připojte svá zařízení"
date: 2026-08-20
description: "Pokyny krok za krokem, jak se připojit k bezdrátovému disku Everdisk: sledujte na chytré televizi přes DLNA, otevřete své soubory v jakémkoli webovém prohlížeči, připojte zařízení jako síťový disk ve Finderu, ve Windows nebo v Linuxu přes WebDAV, propojte souborové aplikace přes FTP a přenášejte přes kabel USB do Macu bez Wi-Fi."
keywords: ["připojení k Everdisku", "streamování do TV DLNA", "otevření souborů v prohlížeči", "připojení síťového disku Finder", "WebDAV Windows Linux", "souborová aplikace FTP", "přenos přes kabel USB Mac", "připojení iPhonu k počítači", "síťový disk iPhone"]
tags: ["everdisk", "guide", "connect"]
readingTime: 11
---


Jakmile na obrazovce [Sdílení](/docs/guide/everdisk/everdisk-guide-sharing) klepnete na **Spustit**, mohou se ostatní zařízení k vašim souborům připojit čtyřmi různými způsoby. Vyberte metodu, která odpovídá zařízení, jež chcete použít. V každém případě je přesná **adresa**, kterou potřebujete, zobrazena v sekci **Jak se připojit** na obrazovce Sdílení.

> Obě zařízení musí být ve **stejné síti Wi-Fi** - nebo, v případě Macu, propojená **kabelem USB** (viz poslední sekce).

## Sledování na televizi (DLNA)

Použijte tuto možnost pro zobrazení fotek, videí a hudby na chytré televizi nebo mediálním přehrávači.

1. V **Nastavení → Sdílení → Připojení** se ujistěte, že je **TV a mediální centrum** zapnuté (ve výchozím nastavení je).
2. Na obrazovce Sdílení klepněte na **Spustit**.
3. Na televizi otevřete její vestavěný mediální přehrávač nebo aplikaci mediálního serveru (může se jmenovat Media Player, SmartShare, AllShare a podobně).
4. Vaše zařízení se objeví v seznamu mediálních serverů pod svým názvem (například "Speedy-Hare"). Vyberte je.
5. Procházejte své sdílené fotky, videa a hudbu a spusťte přehrávání. Náhledové miniatury se zobrazí automaticky.

Poznámky:

- DLNA nelze chránit heslem, takže toto připojení je po dobu, kdy je zapnuté, otevřené komukoli ve stejné síti Wi-Fi.
- Pokud se video na starší televizi nepřehrává, snižte kvalitu videa v **Nastavení → Sdílení → Videa**, aby je Everdisk převedl do kompatibilnějšího formátu.

## Otevření ve webovém prohlížeči (HTTP)

Použijte tuto možnost, když chcete předat soubory komukoli s webovým prohlížečem - žádná aplikace k instalaci.

1. V **Nastavení → Sdílení → Připojení** se ujistěte, že je **Prohlížeč** zapnutý.
2. Klepněte na **Spustit**.
3. Na obrazovce Sdílení zkopírujte adresu **Prohlížeč** (nebo zobrazte její QR kód).
4. Na druhém telefonu, tabletu nebo počítači otevřete jakýkoli webový prohlížeč (Safari, Chrome, Edge, Firefox) a zadejte tuto adresu.
5. Otevře se stránka s vašimi sdílenými soubory.

V prohlížeči může druhá osoba:

- Přepínat mezi zobrazením **seznam** a **mřížka** a řadit podle názvu, data nebo velikosti.
- Vidět skutečné **miniatury** pro fotky, videa, PDF a obaly hudby.
- Otevřít fotku do celoobrazovkové **galerie** s posouváním, přiblížením sevřením prstů a prezentací.
- Přehrávat hudbu ve vestavěném **přehrávači** s frontou, náhodným přehráváním a opakováním.
- **Stáhnout** jakýkoli soubor, nebo stáhnout celou složku (či několik vybraných položek) jako jediný **Archive.zip**.
- **Nahrát** soubory zpět do vašeho zařízení - pouze pokud jste zapnuli **Úpravy souborů** (viz [Přístup a soukromí](/docs/guide/everdisk/everdisk-guide-access)).

## Použití jako síťový disk (WebDAV)

Použijte tuto možnost, aby se vaše zařízení zobrazilo jako běžný disk na Macu, na PC s Windows nebo na počítači s Linuxem, takže můžete soubory přetahovat oběma směry.

**Na Macu (Finder)**

1. V **Nastavení → Sdílení → Připojení** se ujistěte, že je **Počítač** zapnutý.
2. Klepněte na **Spustit** a poznamenejte si adresu **Počítač (WebDAV)**.
3. Ve Finderu zvolte **Otevřít → Připojit k serveru** (nebo stiskněte **⌘K**).
4. Zadejte adresu WebDAV přesně tak, jak je zobrazena, a klikněte na **Připojit**.
5. Zadejte přihlašovací jméno a heslo, pokud jste je nastavili, jinak se připojte jako host.
6. Vaše zařízení se otevře jako každý jiný síťový disk. Přetahujte soubory dovnitř nebo ven.

**Ve Windows**

1. Otevřete **Průzkumník souborů**, klikněte pravým tlačítkem na **Tento počítač** a zvolte **Přidat síťové umístění** (nebo namapujte síťovou jednotku).
2. Zadejte adresu WebDAV zobrazenou v Everdisku.
3. Zadejte přihlašovací jméno a heslo, pokud jste je nastavili.

**V Linuxu**

1. Otevřete svého správce souborů a zvolte **Připojit k serveru** (nebo použijte `davs://` / `dav://`).
2. Zadejte adresu WebDAV zobrazenou v Everdisku.

Zda je připojení jen ke čtení, nebo obousměrné, závisí na nastavení **Úpravy souborů**. Při zapnutém nastavení můžete soubory do zařízení kopírovat a přejmenovávat či mazat je; při vypnutém je disk pouze ke čtení.

## Připojení souborové aplikace (FTP)

Použijte tuto možnost pro souborové a přenosové aplikace, které umí FTP (například FileZilla nebo Cyberduck na počítači).

1. V **Nastavení → Sdílení → Připojení** se ujistěte, že jsou **Ostatní aplikace a zařízení** zapnuté.
2. Klepněte na **Spustit** a poznamenejte si adresu **FTP**.
3. Ve své aplikaci FTP přidejte nové připojení s touto adresou.
4. Zadejte přihlašovací jméno a heslo, pokud jste je nastavili, nebo je nechte prázdné pro anonymní přístup.

## Přenos přes kabel USB (Mac, Wi-Fi není potřeba)

Použijte tuto možnost, když není k dispozici Wi-Fi, nebo když chcete nejrychlejší a nejsoukromější přenos. Funguje pouze s **Macem**.

1. Připojte svůj iPhone nebo iPad k Macu běžným nabíjecím kabelem.
2. Pokud budete na zařízení dotázáni, klepněte na **Důvěřovat tomuto počítači**.
3. V Everdisku klepněte na **Spustit**. Objeví se poznámka **Rychlé připojení k dispozici** a obrazovka Sdílení zobrazí další adresu s odznakem **Kabelové připojení**, která končí na `.local`.
4. Na Macu otevřete Finder → **Otevřít → Připojit k serveru** (**⌘K**) a zadejte tuto adresu `.local` (funguje pro připojení Prohlížeč i Počítač).
5. Vaše zařízení se otevře přes kabel - rychleji než přes Wi-Fi a data se nikdy nedostanou na router ani na internet.

Poznámky:

- Používejte **název `.local`**, nikoli IP adresu (IP adresy fungují jen přes Wi-Fi) a nikdy ne `localhost`.
- Cesta přes kabel je **jen pro Mac**. PC s Windows a zařízení s Androidem musí použít Wi-Fi.
- Soubory můžete do složky Everdisk přetáhnout také pomocí Finderu na Macu, nebo pomocí aplikace Apple Devices (či iTunes) ve Windows, a to prostřednictvím standardního sdílení souborů iOS.

## Další kroky

- [Přístup a soukromí](/docs/guide/everdisk/everdisk-guide-access) - přidejte heslo, povolte nahrávání, zablokujte zařízení.
- [Fotky, hudba a video](/docs/guide/everdisk/everdisk-guide-media) - sdílejte celou svou knihovnu a nastavte kvalitu.
- [Připojení k serverům](/docs/guide/everdisk/everdisk-guide-devices) - dostaňte se z Everdisku k dalším zařízením.
