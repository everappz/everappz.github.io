---
title: "Jak nastavit server SMB na iPhonu a iPadu pro sdílení souborů"
description: "Proměňte iPhone nebo iPad v souborový server SMB pomocí Everdisku a otevřete jej jako síťový disk z Macu, dalšího iPhonu, Linuxu nebo Androidu přes Wi-Fi. Kompletní nastavení, adresa a port smb, volitelné šifrování SMB3 a krok za krokem připojení pro každé zařízení."
date: 2026-09-19
tags: ["everdisk", "smb", "sdílení souborů", "síťový disk", "iphone", "ipad", "mac", "finder", "šifrování", "wifi"]
keywords: ["SMB server iPhone", "SMB server iPad", "jak nastavit SMB na iPhonu", "sdílení SMB z iPhonu", "připojit iPhone SMB Mac Finder", "smb iphone na iphone", "aplikace Soubory iOS připojit k serveru SMB", "sdílení souborů iPhone SMB", "iphone jako síťový disk Finder", "šifrování SMB3 iOS", "sdílení smb iPhone Android", "připojit k SMB z Linuxu", "iphone jako síťový disk", "sdílení souborů mezi iphony wifi", "namapovat iphone jako síťový disk"]
readingTime: 10
---

{{< author-byline >}}

SMB je sdílení souborů vestavěné do macOS, Windows a Linuxu a do téměř každého síťového disku (NAS). Když se připojíte ke sdílené složce na jiném počítači a ta se otevře jako běžný disk ve Finderu nebo Průzkumníku souborů, je to právě SMB, které tu práci odvádí. S aplikací [Everdisk](/products/everdisk) můžete sdílení SMB umístit na iPhone nebo iPad, takže se sám telefon zobrazí jako síťový disk, který ostatní zařízení procházejí, kopírují z něj i na něj.

To je volba, po které sáhnete, když chcete, aby se váš iPhone choval jako opravdový disk, ne jako webová stránka. Je rychlá, přetahuje soubory oběma směry a je to jediný typ připojení v Everdisku, který dokáže šifrovat každý přenos. Tento návod popisuje nastavení a jak se připojit z Macu, dalšího iPhonu nebo iPadu, Linuxu, Androidu a Windows.

## Co budete potřebovat

- iPhone nebo iPad s nainstalovanou aplikací [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Další zařízení ve **stejné síti Wi-Fi**.
- Soubory, které chcete sdílet, ve složce Dokumenty v Everdisku nebo ve složkách, které přidáte.

## Nastavení serveru SMB v Everdisku

### Krok 1: Vyberte, co sdílet a kdo může zapisovat

Otevřete Everdisk, přejděte na kartu **Sdílení** a klepněte na **Co sdílet**. Složka Dokumenty je sdílena ve výchozím nastavení. Přidejte další pomocí **Přidat složku** a **Přidat soubor** a zapněte svou knihovnu Fotky nebo Hudba, pokud chcete, aby byly dostupné také.

Rozhodněte, zda ostatní zařízení mohou vaše soubory jen číst, nebo je také měnit. Otevřete **Nastavení**, poté **Sdílení** a poté **Přístup** a nastavte **Úpravy souborů**. Když je zapnuté, připojená zařízení mohou kopírovat soubory do vašeho telefonu a přejmenovávat je nebo mazat. Když je vypnuté, je sdílení jen ke čtení.

Pokud chcete přihlášení, nastavte **Přihlašovací jméno** a **Heslo** na téže obrazovce Přístup. Ponechte obojí prázdné, chcete-li povolit hostovský přístup.

### Krok 2: Zapněte server SMB

Přejděte do **Nastavení**, poté **Sdílení** a poté **Připojení** a zapněte **Počítač (pokročilé)**. To je server SMB (nese značku SMB).

### Krok 3: Spusťte sdílení a poznamenejte si adresu

Vraťte se na kartu **Sdílení** a klepněte na **Spustit**. Sekce **Jak se připojit** nyní zobrazuje adresu SMB. Vypadá takto:

```
smb://192.168.1.20:4455/Share
```

O této adrese je třeba vědět tři věci:

- Číslo za dvojtečkou je **port**. Everdisk používá ve výchozím nastavení **4455**.
- Sdílení se jmenuje **Share**.
- První část je adresa vašeho iPhonu ve Wi-Fi, takže na vaší síti bude jiná.

Během připojení zařízení mějte Everdisk otevřený, protože iOS pozastavuje aplikace, které jsou příliš dlouho na pozadí.

## Připojení z Macu

To je nejplynulejší případ, protože macOS mluví SMB nativně.

Nejrychlejší způsob: otevřete **Finder** a podívejte se do postranního panelu do části **Locations** nebo **Network**. Everdisk se na Wi-Fi ohlašuje, takže se váš iPhone tam často objeví sám. Klikněte na něj, poté klikněte na **Connect As** a zvolte **Guest**, nebo zadejte své přihlašovací jméno.

Připojení ručně:

1. Ve Finderu zvolte **Go**, poté **Connect to Server** (nebo stiskněte **Command a K**).
2. Zadejte adresu SMB zobrazenou v Everdisku, například `smb://192.168.1.20:4455/Share`.
3. Klikněte na **Connect**, poté vyberte **Guest** nebo zadejte své **Přihlašovací jméno** a **Heslo**.

Váš iPhone se otevře v okně Finderu. Soubory kopírujte dovnitř nebo ven přetažením, přesně jako u jakéhokoli jiného disku (pokud jsou Úpravy souborů zapnuté).

## Připojení z dalšího iPhonu nebo iPadu

iOS a iPadOS umí otevřít sdílení SMB ve vestavěné aplikaci **Files**, což činí přenosy mezi telefony přehledné a rychlé.

Na druhém zařízení:

1. Otevřete aplikaci **Files**.
2. Klepněte na tlačítko **more** (tři tečky, vpravo nahoře na iPhonu) a zvolte **Connect to Server**.
3. Zadejte adresu SMB z Everdisku, například `smb://192.168.1.20:4455/Share`.
4. Zvolte **Guest**, nebo **Registered User** a zadejte své přihlašovací jméno.
5. Sdílení se objeví pod Locations v aplikaci Files. Procházejte a kopírujte v obou směrech.

Na druhém zařízení můžete také použít vlastní kartu **Zařízení** v Everdisku, která obsahuje klienta SMB. Otevřete Everdisk, přejděte na **Zařízení**, klepněte na **Nové připojení**, zvolte **SMB** a zadejte adresu.

## Připojení z Linuxu

1. Otevřete svého správce souborů (Files/Nautilus na GNOME, Dolphin na KDE).
2. Zvolte **Other Locations** nebo **Connect to Server**.
3. Zadejte adresu, například `smb://192.168.1.20:4455/Share`.
4. Připojte se jako host, nebo zadejte své přihlašovací jméno.

Z terminálu můžete také spustit `smbclient //192.168.1.20/Share -p 4455` a na výzvu zadat své přihlašovací jméno.

## Připojení z Androidu

Android nemá systémový prohlížeč SMB, proto použijte správce souborů, který SMB podporuje:

1. Nainstalujte aplikaci jako **CX File Explorer**, **Solid Explorer** nebo **X-plore File Manager**.
2. Přidejte nové připojení **SMB** nebo **LAN**.
3. Zadejte hostitele (adresu iPhonu ve Wi-Fi), nastavte **port na 4455** a název sdílení **Share**.
4. Připojte se jako host nebo se svým přihlašovacím jménem, poté procházejte a kopírujte.

## Připojení z Windows

Windows umí číst sdílení SMB, s jednou výhradou, o které je dobré vědět předem. Vestavěný Průzkumník souborů komunikuje se SMB pouze na standardním portu a neumožňuje zadat vlastní port v cestě, a Everdisk používá port 4455. Takže obyčejná cesta přes **Mapovat síťovou jednotku** ho často nedosáhne.

Na Windows máte dvě dobré možnosti:

- Použijte správce souborů nebo klienta SMB, který umožňuje nastavit vlastní port, a nasměrujte ho na adresu iPhonu s portem **4455** a názvem sdílení **Share**.
- Nebo se z Windows připojte pomocí jiného z serverů Everdisku. [Nastavení WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) i [nastavení FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) fungují z Průzkumníka souborů Windows dobře a odkaz na prohlížeč funguje v jakémkoli prohlížeči.

Pokud chcete Mapovat síťovou jednotku vyzkoušet: otevřete **File Explorer**, klikněte pravým tlačítkem na **This PC**, zvolte **Map network drive** a zadejte hostitele a název sdílení zobrazené v Everdisku. Pokud se nemůže připojit, jde o výše uvedené omezení portu, takže přejděte na WebDAV nebo FTP.

## Zapnutí šifrování pro nedůvěryhodnou Wi-Fi

SMB je jediné připojení Everdisku, které dokáže šifrovat každý přenos, což je důležité na Wi-Fi, kterou plně neovládáte, jako v kavárně nebo firemní síti.

1. V **Nastavení**, **Sdílení**, **Přístup** nastavte **Přihlašovací jméno** a **Heslo**. Šifrovaná připojení nemohou být anonymní, takže tento krok je nutný.
2. V **Nastavení**, **Sdílení** zapněte **Vyžadovat šifrování SMB**.
3. Zastavte a znovu spusťte sdílení, aby se změna projevila.

Každý přenos SMB je pak chráněn **šifrováním SMB3 (AES)**. Připojující se zařízení musí podporovat SMB3, což Finder na moderním Macu i Windows 10 nebo novější splňují. Šifrování SMB je součástí jednorázového nákupu Premium.

## Jen ke čtení, nebo pro čtení i zápis

Přepínač **Úpravy souborů** v Nastavení, Sdílení, Přístup toto řídí pro každý server, včetně SMB. Zapněte ho a připojená zařízení mohou nahrávat, přejmenovávat a mazat. Vypněte ho a mohou pouze procházet a kopírovat soubory z vašeho telefonu. Zvolte jen ke čtení, když předáváte soubory někomu, u koho nechcete, aby cokoli měnil.

## Jak to lidé používají v praxi

- **Přesuňte velkou složku do iPhonu z Macu** jejím přetažením do okna Finderu, rychleji než nahrávání přes web.
- **Stáhněte z telefonu celý den fotek a videí** do notebooku bez iTunes nebo kabelu.
- **Posílejte soubory mezi dvěma iPhony** přes aplikaci Files, bez třetí aplikace na kterékoli straně.
- **Pracujte se souborem na místě**, otevřete dokument přímo z telefonu v aplikaci na Macu a uložte ho zpět.

## Několik tipů

- Během připojení zařízení mějte Everdisk otevřený. Dlouhé zamknutí telefonu může aplikaci pozastavit a připojení přerušit.
- Pokud Mac telefon v postranním panelu Finderu nevidí, připojte se ručně přes Connect to Server a celou adresu smb.
- Pro nejlepší rychlost u velkých přenosů ponechte kvalitu fotek a videí na Original v Nastavení.
- Na nedůvěryhodné síti zapněte Vyžadovat šifrování SMB a ostatní servery během práce vypněte.

## Často kladené otázky

{{% details title="Jaká je adresa a port SMB pro můj iPhone?" closed="true" %}}
Po spuštění sdílení Everdisk zobrazí adresu na obrazovce Sdílení. Vypadá jako smb://192.168.1.20:4455/Share. Číslo 4455 je port, který Everdisk používá pro SMB, a Share je název sdílené složky. První část je adresa vašeho iPhonu ve Wi-Fi, takže ta vaše bude jiná.
{{% /details %}}

{{% details title="Můžu se ke sdílení SMB na svém iPhonu připojit z Windows?" closed="true" %}}
Průzkumník souborů Windows se připojuje k SMB pouze na standardním portu a nepřijímá vlastní port v cestě, zatímco Everdisk používá port 4455. Takže obyčejná cesta přes Mapovat síťovou jednotku ho často nedosáhne. Použijte správce souborů, který umožňuje nastavit vlastní port, nebo se z Windows připojte přes WebDAV, FTP nebo odkaz na prohlížeč. Všechny tyto fungují z Windows bez potíží s portem.
{{% /details %}}

{{% details title="Jak sdílím soubory mezi dvěma iPhony přes SMB?" closed="true" %}}
Spusťte server SMB na prvním iPhonu v Everdisku. Na druhém iPhonu otevřete aplikaci Files, klepněte na tlačítko more, zvolte Connect to Server a zadejte adresu smb zobrazenou v Everdisku (například smb://192.168.1.20:4455/Share). Připojte se jako Guest nebo se svým přihlašovacím jménem a sdílení se objeví v aplikaci Files. Na druhém telefonu můžete také použít vlastní kartu Zařízení v Everdisku.
{{% /details %}}

{{% details title="Objeví se můj iPhone v postranním panelu Finderu na Macu automaticky?" closed="true" %}}
Obvykle ano. Everdisk ohlašuje sdílení SMB na vaší Wi-Fi, takže se váš iPhone často objeví pod Locations nebo Network v postranním panelu Finderu. Klikněte na něj a zvolte Connect As, poté Guest nebo své přihlašovací jméno. Pokud se neobjeví, připojte se ručně přes Go, Connect to Server a celou adresu smb.
{{% /details %}}

{{% details title="Potřebuji k použití SMB heslo?" closed="true" %}}
Ne, přihlášení je volitelné. Ponechte Přihlašovací jméno a Heslo prázdné v Nastavení, Sdílení, Přístup a povolíte hostovský přístup. Nastavte je, pokud chcete, aby se připojení přihlašovalo. Přihlašovací jméno a heslo jsou nutné jen tehdy, když zapnete Vyžadovat šifrování SMB, protože šifrovaná připojení nemohou být anonymní.
{{% /details %}}

{{% details title="Je připojení SMB šifrované?" closed="true" %}}
Může být. SMB je jediné připojení Everdisku, které podporuje šifrování. Nastavte přihlašovací jméno a heslo, poté zapněte Vyžadovat šifrování SMB v Nastavení, Sdílení. Každý přenos je pak chráněn SMB3 (AES). Druhé zařízení musí podporovat SMB3, což moderní Macy a Windows 10 nebo novější splňují. Šifrování je funkce Premium.
{{% /details %}}

{{% details title="Můžou lidé měnit nebo mazat moje soubory přes SMB?" closed="true" %}}
Jen pokud to povolíte. Řídí to přepínač Úpravy souborů v Nastavení, Sdílení, Přístup. Když je zapnutý, připojená zařízení mohou nahrávat, přejmenovávat a mazat. Když je vypnutý, je sdílení jen ke čtení a ostatní mohou procházet a kopírovat soubory z vašeho telefonu, ale nemohou nic měnit.
{{% /details %}}

{{% details title="Proč se moje připojení SMB přerušilo?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikace, které zůstávají příliš dlouho na pozadí. Během připojení zařízení mějte Everdisk otevřený na obrazovce a při dlouhých přenosech telefon připojte k napájení. Také se ujistěte, že obě zařízení zůstala na stejné Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV nebo FTP, které mám použít?" closed="true" %}}
Použijte SMB, když chcete, aby se telefon choval jako opravdový síťový disk na Macu, dalším iPhonu, Linuxu nebo NAS, a když chcete šifrování. Použijte WebDAV, když chcete síťový disk, který dobře funguje i z Windows. Použijte FTP pro nejširší kompatibilitu se staršími zařízeními a aplikacemi. Everdisk umí všechny běžet najednou, takže nejste uzamčeni jen v jednom.
{{% /details %}}

{{% details title="Je Everdisk zdarma?" closed="true" %}}
Ano, Everdisk je zdarma ke stažení a server SMB je součástí. Volitelný jednorázový nákup Premium přidává šifrování SMB, vlastní porty a několik dalších doplňků. SMB můžete nastavit a sdílet soubory bez placení.
{{% /details %}}

Chcete to vyzkoušet? [Stáhněte si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a asi za minutu otevřete svůj iPhone ve Finderu. Máte dotazy nebo zpětnou vazbu? Napište nám na **support@everappz.com**.
