---
title: "Přístup a soukromí"
date: 2026-08-20
description: "Udržte své sdílení v Everdisku v bezpečí: chraňte přístup přihlášením a heslem, řiďte pomocí Úprav souborů, zda mohou připojená zařízení nahrávat, přejmenovávat a mazat, blokujte neznámá zařízení, zvolte koš vs. trvalé smazání a pochopte, proč všechno zůstává ve vaší místní síti."
keywords: ["ochrana Everdisk heslem", "přepínač úprav souborů", "blokovat zařízení", "blokovaná zařízení", "trvalé smazání souborů", "pouze místní síť", "soukromé sdílení souborů", "DLNA bez hesla", "bezpečnost sítě"]
tags: ["everdisk", "guide", "access", "privacy", "security"]
readingTime: 8
---


Everdisk uchovává vaše soubory ve vaší vlastní síti a dává vám jednoduché ovládání toho, kdo se k nim může dostat a co s nimi může dělat. Tyto ovládací prvky najdete v **Nastavení → Sdílení → Přístup** plus několik souvisejících nastavení ve Správci souborů.

## Chraňte přístup přihlášením a heslem

Ve výchozím nastavení může vaše sdílené soubory otevřít kdokoli ve stejné síti, kdo má vaši adresu. Chcete-li vyžadovat přihlášení:

1. Přejděte do **Nastavení → Sdílení → Přístup**.
2. Zadejte **Přihlašovací jméno** a **Heslo**.
3. Nyní si připojení **Prohlížeč (HTTP)**, **Počítač (WebDAV)** a **Ostatní aplikace a zařízení (FTP)** vyžádají tyto údaje, než zobrazí vaše soubory.

Pro otevřený přístup nechte obě pole prázdná. Vaše heslo je bezpečně uloženo v Keychainu zařízení.

> **DLNA je vždy otevřené.** Připojení TV a mediální centrum (DLNA) nelze chránit heslem, takže jakmile je zapnuté, může jakékoli zařízení ve stejné síti Wi-Fi procházet vaše sdílená média. Vypněte je, pokud chcete jen chráněná připojení, a sdílejte pouze v sítích, kterým důvěřujete.

## Povolení nebo zákaz úprav (Úpravy souborů)

Přepínač **Úpravy souborů** řídí, zda si připojená zařízení mohou vaše soubory jen prohlížet, nebo je také měnit.

- **Zapnuto** (výchozí): připojená zařízení mohou vaše sdílené soubory **nahrávat, přejmenovávat a mazat** - takže vaše zařízení funguje jako skutečný obousměrný síťový disk.
- **Vypnuto**: vaše sdílené soubory jsou **pouze ke čtení**. Ostatní si je mohou prohlížet a stahovat, ale nemohou nic přidávat ani měnit.

Zapnutí zobrazí krátké varování, protože umožňuje ostatním lidem měnit vaše soubory. Dokud je zapnuto, nese odznak **Důležité**.

## Blokování zařízení

Pokud uvidíte zařízení, které nepoznáváte:

1. Na obrazovce Sdílení jej najděte pod **Kdo je připojen**.
2. Klepněte na jeho tlačítko dalších akcí a zvolte **Blokovat toto zařízení**.

Blokovaná zařízení jsou uvedena v **Nastavení → Sdílení → Přístup → Blokovaná zařízení**, kde můžete některé **odblokovat** nebo zvolit **Odblokovat vše**. Blokování sleduje zařízení, i když se jeho síťová adresa změní (pro připojení Prohlížeč, Počítač a TV).

## Koš vs. trvalé smazání

Když je soubor smazán - vámi ve správci souborů nebo připojeným zařízením - jde obvykle do obnovitelného **koše**, takže jej můžete získat zpět.

Pokud dáváte přednost tomu, aby se soubory odstranily okamžitě bez možnosti obnovy, zapněte **Trvale mazat soubory** v **Nastavení → Správce souborů → Mazání souborů**. Ve výchozím nastavení je vypnuto. **Týká se to správce souborů v zařízení** a **smazání provedených po síti**; nemění to, jak se s mazáním vypořádá systémová knihovna Fotek nebo knihovna Hudby.

## Všechno zůstává lokálně

Everdisk sdílí pouze přes vaši **místní síť** - nic se nenahrává na internet a žádný cloudový účet není nikde uprostřed. Pár věcí, které stojí za to vědět:

- Everdisk potřebuje oprávnění iOS **Místní síť**, aby jej okolní zařízení mohla najít. Pokud je toto oprávnění vypnuté, poznámka vysvětlí, jak je zapnout zpět v aplikaci Nastavení iOS.
- Pro maximální soukromí sdílejte jen tehdy, když jste v **domácí nebo soukromé síti Wi-Fi**, které důvěřujete, a buďte opatrní na veřejné Wi-Fi. Přihlašovací jméno a heslo pomáhá, ale není náhradou za důvěryhodnou síť.
- **Nejsoukromější možností ze všech je kabel USB do Macu** - data jdou rovnou přes kabel a nikdy se nedostanou na router ani na internet. Viz [Připojte svá zařízení](/docs/guide/everdisk/everdisk-guide-connect).

## Další kroky

- [Sdílení](/docs/guide/everdisk/everdisk-guide-sharing) - vyberte, co sdílet, a spusťte sdílení.
- [Nastavení](/docs/guide/everdisk/everdisk-guide-settings) - všechna nastavení Přístupu a Správce souborů na jednom místě.
