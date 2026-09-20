---
title: "Jak nastavit server WebDAV na iPhonu a iPadu pro přístup k souborům a sdílení"
description: "Proměňte iPhone nebo iPad v server WebDAV pomocí Everdisku a připojte jej jako síťový disk ve Finderu na Macu, v Průzkumníku souborů Windows, na Linuxu, Androidu nebo dalším iPhonu přes Wi-Fi. Kompletní nastavení, adresa a port WebDAV a krok za krokem připojení pro každé zařízení."
date: 2026-09-19
tags: ["everdisk", "webdav", "síťový disk", "sdílení souborů", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["WebDAV server iPhone", "WebDAV server iPad", "jak nastavit WebDAV na iPhonu", "připojit iPhone jako síťový disk", "připojit iPhone WebDAV Mac Finder", "WebDAV Průzkumník souborů Windows iPhone", "iphone síťový disk Windows", "WebDAV Linux iPhone", "přístup k souborům iPhonu z počítače", "webdav iphone na iphone", "sdílení souborů iPhone WebDAV", "namapovat síťový disk iphone", "přenos souborů iphone webdav", "adresa port webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV promění složku v síťový disk, který počítač otevře ve svém běžném správci souborů. Běží přes stejný webový protokol, jaký používá váš prohlížeč, a proto putuje dobře napříč Macem, Windows a Linuxem bez speciálních ovladačů. S aplikací [Everdisk](/products/everdisk) můžete na iPhonu nebo iPadu provozovat server WebDAV, takže se telefon zobrazí jako disk, který můžete procházet, kopírovat z něj i na něj z téměř jakéhokoli počítače.

WebDAV je nejlepší volbou, když je ve hře Windows, protože Průzkumník souborů Windows se k němu připojuje čistě. Tento návod popisuje nastavení a jak se připojit z Macu, Windows, Linuxu, Androidu a druhého iPhonu.

## Co budete potřebovat

- iPhone nebo iPad s nainstalovanou aplikací [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Počítač nebo jiné zařízení ve **stejné síti Wi-Fi**.
- Soubory, které chcete sdílet, ve složce Dokumenty v Everdisku nebo ve složkách, které přidáte.

## Nastavení serveru WebDAV v Everdisku

### Krok 1: Vyberte, co sdílet a nastavte přístup

Otevřete Everdisk, přejděte na kartu **Sdílení** a klepněte na **Co sdílet**. Složka Dokumenty je sdílena ve výchozím nastavení. Přidejte další pomocí **Přidat složku** a **Přidat soubor**.

Otevřete **Nastavení**, poté **Sdílení** a poté **Přístup**. Zapněte **Úpravy souborů**, pokud chcete, aby připojené počítače mohly kopírovat soubory do vašeho telefonu a přejmenovávat je nebo mazat, nebo je vypněte pro disk jen ke čtení. Nastavte zde **Přihlašovací jméno** a **Heslo**, pokud chcete přihlášení, nebo je ponechte prázdné pro hostovský přístup.

### Krok 2: Zapněte server WebDAV

Přejděte do **Nastavení**, poté **Sdílení** a poté **Připojení** a zapněte **Počítač**. To je server WebDAV (nese značku WebDAV).

### Krok 3: Spusťte sdílení a poznamenejte si adresu

Vraťte se na kartu **Sdílení** a klepněte na **Spustit**. Sekce **Jak se připojit** zobrazí adresu WebDAV. Vypadá takto:

```
http://192.168.1.20:8080
```

Číslo za dvojtečkou je **port**, což je ve výchozím nastavení **8080**. První část je adresa vašeho iPhonu ve Wi-Fi, takže ta vaše bude jiná. Během připojení zařízení mějte Everdisk otevřený na obrazovce.

## Připojení z Macu

1. Otevřete **Finder**, zvolte **Go**, poté **Connect to Server** (nebo stiskněte **Command a K**).
2. Zadejte adresu WebDAV zobrazenou v Everdisku, například `http://192.168.1.20:8080`.
3. Klikněte na **Connect**, poté zvolte **Guest** nebo zadejte své **Přihlašovací jméno** a **Heslo**.

Váš iPhone se otevře v okně Finderu a chová se jako běžná složka. Kopírujte soubory v obou směrech, pokud jsou Úpravy souborů zapnuté.

## Připojení z Windows

Windows má vestavěného klienta WebDAV, takže to funguje z Průzkumníka souborů.

1. Otevřete **File Explorer**, klikněte pravým tlačítkem na **This PC** v postranním panelu a zvolte **Add a network location** (můžete použít i **Map network drive**).
2. Až budete dotázáni na adresu, zadejte stejnou adresu WebDAV z Everdisku, například `http://192.168.1.20:8080`, poté klikněte na **Next**.
3. Zadejte své **Přihlašovací jméno** a **Heslo**, pokud jste je nastavili.

Zařízení se poté objeví pod This PC jako síťové umístění, které můžete otevřít a kopírovat z něj soubory. Pokud Windows odmítne připojení napoprvé, ujistěte se, že běží služba **WebClient** (v nabídce Start vyhledejte Services, najděte WebClient a nastavte jej ke spuštění), poté to zkuste znovu.

## Připojení z Linuxu

1. Otevřete svého správce souborů a zvolte **Connect to Server** nebo **Other Locations**.
2. Zadejte adresu s předponou WebDAV, například `dav://192.168.1.20:8080` (`davs://` použijte jen tehdy, pokud jste nastavili TLS).
3. Připojte se jako host nebo zadejte své přihlašovací jméno.

## Připojení z Androidu

Android nemá systémový prohlížeč WebDAV, proto použijte správce souborů, který jej podporuje:

1. Nainstalujte aplikaci jako **Solid Explorer** nebo **CX File Explorer**.
2. Přidejte nové připojení **WebDAV**.
3. Zadejte hostitele a **port 8080**, zvolte schéma `http` a přidejte své přihlašovací jméno, pokud jste je nastavili.

## Připojení z dalšího iPhonu nebo iPadu

Aplikace Files v iOS neobsahuje klienta WebDAV, proto použijte jednu z těchto možností:

- **Vlastní karta Zařízení v Everdisku.** Na druhém zařízení otevřete Everdisk, přejděte na **Zařízení**, klepněte na **Nové připojení**, zvolte **WebDAV** a zadejte adresu, například `http://192.168.1.20:8080`. To je nejjednodušší cesta a nepotřebuje nic navíc.
- **Aplikace WebDAV** jako Documents od Readdle, která umí přidat připojení WebDAV se stejnou adresou a přihlašovacím jménem.

## Chcete raději rychlý odkaz než disk?

Pokud potřebujete jen rychle chytnout soubor a nechcete disk vůbec připojovat, zapněte připojení **Prohlížeč** v Nastavení, Sdílení, Připojení. Everdisk vám pak dá webovou adresu, kterou můžete otevřít v libovolném prohlížeči na jakémkoli zařízení a procházet a stahovat své soubory. Je to nejrychlejší způsob, jak předat soubor PC s Windows, Chromebooku nebo telefonu kamaráda.

## Jen ke čtení, nebo pro čtení i zápis

Rozhoduje o tom přepínač **Úpravy souborů** v Nastavení, Sdílení, Přístup. Zapnutý znamená, že připojené počítače mohou nahrávat, přejmenovávat a mazat. Vypnutý znamená, že je disk jen ke čtení, takže ostatní mohou vaše soubory prohlížet a kopírovat, ale nemohou je měnit.

## Jak to lidé používají v praxi

- **Zkopírujte soubory do iPhonu z PC s Windows** jeho namapováním jako síťového umístění a přetažením přes něj.
- **Přesuňte fotky a dokumenty do notebooku** pomocí správce souborů, který už znáte, bez kabelu a bez iTunes.
- **Upravte dokument na místě** z Macu, otevřete ho přímo z telefonu a uložte zpět.
- **Přesuňte složku mezi iPhonem a iPadem** pomocí karty Zařízení v Everdisku na přijímajícím zařízení.

## Několik tipů

- Během připojení zařízení mějte Everdisk otevřený. Dlouhé zamknutí telefonu může aplikaci pozastavit.
- Na Windows, pokud připojení selže, spusťte službu WebClient a zkuste adresu znovu.
- WebDAV i SMB se připojují jako síťové disky. Použijte WebDAV, když je ve hře Windows, a [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), když chcete rychlost Finderu a šifrování.
- Pro nejrychlejší přenosy ponechte kvalitu fotek a videí na Original v Nastavení.

## Často kladené otázky

{{% details title="Jaká je adresa a port WebDAV pro můj iPhone?" closed="true" %}}
Po spuštění sdílení Everdisk zobrazí adresu na obrazovce Sdílení. Vypadá jako http://192.168.1.20:8080. Číslo 8080 je port, který Everdisk používá pro WebDAV, a první část je adresa vašeho iPhonu ve Wi-Fi, takže ta vaše bude jiná.
{{% /details %}}

{{% details title="Jak se připojím k WebDAV na svém iPhonu z Windows?" closed="true" %}}
Otevřete File Explorer, klikněte pravým tlačítkem na This PC a zvolte Add a network location nebo Map network drive. Zadejte adresu WebDAV z Everdisku, například http://192.168.1.20:8080, poté zadejte své přihlašovací jméno, pokud jste je nastavili. Pokud se Windows nechce připojit, ujistěte se, že běží služba WebClient (vyhledejte Services, najděte WebClient, spusťte ji) a zkuste to znovu.
{{% /details %}}

{{% details title="Můžu použít WebDAV mezi dvěma iPhony?" closed="true" %}}
Ano, ale aplikace Files v iOS nemá klienta WebDAV, proto na druhém zařízení použijte Everdisk. Otevřete kartu Zařízení, klepněte na Nové připojení, zvolte WebDAV a zadejte adresu zobrazenou na prvním telefonu. Funguje i aplikace WebDAV jako Documents od Readdle.
{{% /details %}}

{{% details title="Vyžaduje WebDAV heslo?" closed="true" %}}
Ne, přihlášení je volitelné. Ponechte Přihlašovací jméno a Heslo prázdné v Nastavení, Sdílení, Přístup pro hostovský přístup, nebo je nastavte, pokud chcete, aby se připojení přihlašovalo.
{{% /details %}}

{{% details title="Můžou ostatní lidé měnit moje soubory přes WebDAV?" closed="true" %}}
Jen pokud to povolíte. Řídí to přepínač Úpravy souborů v Nastavení, Sdílení, Přístup. Zapnutý umožňuje připojeným zařízením nahrávat, přejmenovávat a mazat. Vypnutý činí disk jen ke čtení, takže ostatní mohou prohlížet a kopírovat, ale nic měnit.
{{% /details %}}

{{% details title="WebDAV, nebo SMB, jaký je rozdíl?" closed="true" %}}
Oba připojí váš iPhone jako síťový disk. WebDAV běží přes webový protokol a připojuje se čistě z Průzkumníka souborů Windows, což je jeho hlavní síla. SMB je nativní sdílení souborů na Macu, Linuxu a zařízeních NAS, je obvykle rychlejší na Macu a je to jediné připojení Everdisku, které dokáže šifrovat přenosy. Everdisk umí oba běžet najednou.
{{% /details %}}

{{% details title="Proč se můj disk WebDAV odpojuje?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikace, které zůstávají příliš dlouho na pozadí. Během připojení zařízení mějte Everdisk otevřený na obrazovce a při dlouhých přenosech ho připojte k napájení. Také ověřte, že jsou obě zařízení stále na stejné Wi-Fi.
{{% /details %}}

{{% details title="Můžu se připojit přes WebDAV bez Wi-Fi?" closed="true" %}}
Ano, pokud iPhone připojíte k Macu kabelem. Everdisk pak zobrazí další adresu připojení kabelem, kterou může připojený Mac otevřít ve Finderu a která funguje i úplně bez Wi-Fi. Přes kabel se k zařízení dostane jen tento Mac.
{{% /details %}}

{{% details title="Je Everdisk zdarma?" closed="true" %}}
Ano, Everdisk je zdarma ke stažení a server WebDAV je součástí. Volitelný jednorázový nákup Premium přidává doplňky, jako jsou vlastní porty a převod fotek a videí. WebDAV můžete nastavit a sdílet soubory bez placení.
{{% /details %}}

Chcete to vyzkoušet? [Stáhněte si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a během pár minut připojte svůj iPhone jako disk. Máte dotazy nebo zpětnou vazbu? Napište nám na **support@everappz.com**.
