---
title: "Jak nastavit server FTP na iPhonu a iPadu pro přenos souborů"
description: "Proměňte iPhone nebo iPad v server FTP pomocí Everdisku a přenášejte soubory z Macu, PC s Windows, Linuxu, Androidu, aplikace FTP jako FileZilla nebo z dalšího iPhonu přes Wi-Fi. Kompletní nastavení, adresa a port ftp, hostovský přístup a krok za krokem připojení pro každé zařízení."
date: 2026-09-19
tags: ["everdisk", "ftp", "přenos souborů", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["FTP server iPhone", "FTP server iPad", "jak nastavit FTP na iPhonu", "aplikace ftp server iphone", "připojit FileZilla k iPhonu", "Cyberduck iPhone FTP", "přenos souborů iPhone FTP", "ftp iphone do počítače", "ftp iphone na iphone", "připojit k FTP na iPhonu z Windows", "adresa port ftp iphone", "anonymní ftp iphone", "sdílení souborů iphone ftp", "iphone ftp pro fotoaparát nas"]
readingTime: 9
---

{{< author-byline >}}

FTP je stará jistota přenosu souborů. Je tu už desítky let, což je přesně důvod, proč je tak užitečné: téměř cokoli, co umí komunikovat se serverem, mu rozumí. Fotoaparáty, chytré TV, routery, síťové disky, automatizační nástroje i každá stolní aplikace FTP mluví FTP. S aplikací [Everdisk](/products/everdisk) můžete na iPhonu nebo iPadu provozovat server FTP, takže se telefon stane místem, ke kterému se tato zařízení a aplikace mohou připojit a přesouvat soubory.

Po FTP sáhněte, když ostatní možnosti nevyhovují, například u staršího zařízení nebo aplikace, která se umí připojit jen přes FTP. Tento návod popisuje nastavení a jak se připojit z Macu, Windows, aplikace FTP, Linuxu, Androidu a druhého iPhonu.

## Co budete potřebovat

- iPhone nebo iPad s nainstalovanou aplikací [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- Počítač, aplikaci nebo zařízení ve **stejné síti Wi-Fi**.
- Soubory, které chcete sdílet, ve složce Dokumenty v Everdisku nebo ve složkách, které přidáte.

## Nastavení serveru FTP v Everdisku

### Krok 1: Vyberte, co sdílet a nastavte přístup

Otevřete Everdisk, přejděte na kartu **Sdílení** a klepněte na **Co sdílet**. Složka Dokumenty je sdílena ve výchozím nastavení. Přidejte další pomocí **Přidat složku** a **Přidat soubor**.

Otevřete **Nastavení**, poté **Sdílení** a poté **Přístup**. Zapněte **Úpravy souborů**, pokud chcete, aby lidé mohli nahrávat, přejmenovávat a mazat, nebo je vypněte a povolte pouze stahování. Nastavte **Přihlašovací jméno** a **Heslo**, pokud chcete přihlášení, nebo je ponechte prázdné, aby se kdokoli mohl připojit jako host.

### Krok 2: Zapněte server FTP

Přejděte do **Nastavení**, poté **Sdílení** a poté **Připojení** a zapněte **Ostatní aplikace a zařízení**. To je server FTP (nese značku FTP).

### Krok 3: Spusťte sdílení a poznamenejte si adresu

Vraťte se na kartu **Sdílení** a klepněte na **Spustit**. Sekce **Jak se připojit** zobrazí adresu FTP. Vypadá takto:

```
ftp://192.168.1.20:2121
```

Číslo za dvojtečkou je **port**, což je ve výchozím nastavení **2121**. První část je adresa vašeho iPhonu ve Wi-Fi, takže ta vaše bude jiná. Během připojení zařízení mějte Everdisk otevřený na obrazovce.

## Připojení z Macu

1. Otevřete **Finder**, zvolte **Go**, poté **Connect to Server** (nebo stiskněte **Command a K**).
2. Zadejte adresu FTP zobrazenou v Everdisku, například `ftp://192.168.1.20:2121`.
3. Klikněte na **Connect**, poté zvolte **Guest** nebo zadejte své **Přihlašovací jméno** a **Heslo**.

Finder připojí sdílení FTP, takže můžete procházet a kopírovat soubory do Macu. Vezměte na vědomí, že Finder otevírá FTP jen ke čtení. Když chcete nahrávat z Macu, použijte aplikaci FTP, jak je popsáno níže.

## Připojení z Windows

1. Otevřete **File Explorer** a klikněte na adresní řádek nahoře.
2. Zadejte adresu FTP z Everdisku, například `ftp://192.168.1.20:2121`, a stiskněte **Enter**.
3. Zadejte své **Přihlašovací jméno** a **Heslo**, pokud jste je nastavili, nebo pokračujte jako host.

Sdílené soubory se objeví v okně a můžete je zkopírovat do PC.

## Připojení pomocí aplikace FTP (FileZilla, Cyberduck)

Pro nahrávání a plnou kontrolu je aplikace FTP nejlepším nástrojem. **FileZilla** a **Cyberduck** jsou zdarma a běží na Windows, Macu i Linuxu.

1. Otevřete aplikaci a vytvořte nové připojení.
2. Nastavte **Host** na adresu iPhonu ve Wi-Fi a **Port** na **2121**.
3. Pro přihlášení zadejte své **Přihlašovací jméno** a **Heslo**, nebo zvolte **Anonymous**, pokud jste žádné nenastavili.
4. Připojte se a přetahujte soubory oběma směry (nahrávání vyžaduje zapnuté Úpravy souborů).

## Připojení z Linuxu

1. Otevřete svého správce souborů a zvolte **Connect to Server** nebo **Other Locations**.
2. Zadejte adresu, například `ftp://192.168.1.20:2121`.
3. Připojte se jako host nebo se svým přihlašovacím jménem.

Můžete také použít libovolného klienta FTP na Linuxu z terminálu a nasměrovat ho na stejného hostitele a port 2121.

## Připojení z Androidu

Android nemá systémový prohlížeč FTP, proto použijte aplikaci:

1. Nainstalujte klienta FTP jako **AndFTP**, **FTPCafe** nebo správce souborů s podporou FTP jako **Solid Explorer**.
2. Přidejte připojení s hostitelem, **portem 2121** a svým přihlašovacím jménem nebo Anonymous.
3. Procházejte a přenášejte.

## Připojení z dalšího iPhonu nebo iPadu

Aplikace Files v iOS neobsahuje klienta FTP, proto na druhém zařízení použijte jednu z těchto možností:

- **Vlastní karta Zařízení v Everdisku.** Otevřete Everdisk, přejděte na **Zařízení**, klepněte na **Nové připojení**, zvolte **FTP** a zadejte adresu, například `ftp://192.168.1.20:2121`. To je nejjednodušší cesta.
- **Vyhrazená aplikace FTP** pro iOS, se stejným hostitelem, portem 2121 a přihlašovacím jménem.

## Připojení dalšího vybavení: fotoaparátů, TV, routerů a NAS

Tady FTP září. Mnoho zařízení má vestavěného klienta FTP, který dokáže soubory posílat nebo stahovat:

- **Fotoaparáty**, které nahrávají fotky přes FTP, je mohou posílat přímo do vašeho iPhonu.
- **Chytré TV, routery, boxy NAS a automatizační nástroje**, které FTP podporují, se mohou připojit stejným způsobem.

Nasměrujte je na adresu iPhonu ve Wi-Fi, port **2121** a své přihlašovací jméno (nebo Anonymous), pomocí adresy zobrazené v Everdisku.

## Jen ke čtení, nebo pro čtení i zápis

Řídí to přepínač **Úpravy souborů** v Nastavení, Sdílení, Přístup. Zapnutý umožňuje lidem nahrávat, přejmenovávat a mazat. Vypnutý znamená, že mohou pouze stahovat. Zvolte jen ke čtení, když soubory předáváte a nechcete, aby se ve vašem telefonu cokoli měnilo.

## Jak to lidé používají v praxi

- **Připojte FileZilla k iPhonu** a přesuňte dávku souborů do telefonu najednou.
- **Nechte starou aplikaci nebo zařízení, které mluví jen FTP**, dosáhnout na vaše soubory, když se nic jiného nepřipojí.
- **Přijímejte fotky z fotoaparátu**, který nahrává přes FTP.
- **Přesouvejte soubory mezi iPhonem a iPadem** pomocí karty Zařízení v Everdisku na přijímajícím zařízení.

## Několik tipů

- Během připojení zařízení mějte Everdisk otevřený, protože iOS po chvíli pozastavuje aplikace na pozadí.
- Pro nahrávání z Macu použijte FileZillu nebo Cyberduck spíše než Finder, protože Finder otevírá FTP jen ke čtení.
- Ponechte přihlašovací jméno prázdné pro nejširší kompatibilitu, poté se připojte jako Anonymous, což většina klientů FTP nabízí.
- FTP svůj provoz nešifruje. Na síti, které nedůvěřujete, použijte místo toho [server SMB se šifrováním](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Často kladené otázky

{{% details title="Jaká je adresa a port FTP pro můj iPhone?" closed="true" %}}
Po spuštění sdílení Everdisk zobrazí adresu na obrazovce Sdílení. Vypadá jako ftp://192.168.1.20:2121. Číslo 2121 je port, který Everdisk používá pro FTP, a první část je adresa vašeho iPhonu ve Wi-Fi, takže ta vaše bude jiná.
{{% /details %}}

{{% details title="Jak připojím FileZillu nebo Cyberduck k iPhonu?" closed="true" %}}
Otevřete aplikaci a vytvořte nové připojení. Nastavte Host na adresu iPhonu ve Wi-Fi a Port na 2121. Zadejte své Přihlašovací jméno a Heslo, nebo zvolte Anonymous, pokud jste v Everdisku žádné nenastavili. Připojte se a můžete přetahovat soubory oběma směry, když jsou zapnuté Úpravy souborů.
{{% /details %}}

{{% details title="Můžu se k FTP na svém iPhonu připojit z Windows?" closed="true" %}}
Ano. Otevřete File Explorer, klikněte na adresní řádek, zadejte adresu FTP z Everdisku (například ftp://192.168.1.20:2121) a stiskněte Enter. Zadejte své přihlašovací jméno, pokud jste je nastavili, nebo pokračujte jako host. Pro nahrávání a větší kontrolu použijte místo toho aplikaci FTP jako FileZilla.
{{% /details %}}

{{% details title="Potřebuji přihlášení pro FTP?" closed="true" %}}
Ne, přihlášení je volitelné. Ponechte Přihlašovací jméno a Heslo prázdné v Nastavení, Sdílení, Přístup a připojte se jako Anonymous, což většina klientů FTP nabízí. Nastavte přihlášení, pokud chcete, aby se připojení nejprve přihlásilo.
{{% /details %}}

{{% details title="Proč mohu jen stahovat a ne nahrávat přes FTP?" closed="true" %}}
Časté jsou dva důvody. Zaprvé musí být přepínač Úpravy souborů v Nastavení, Sdílení, Přístup zapnutý, aby umožnil nahrávání, přejmenovávání a mazání. Zadruhé Finder na Macu otevírá FTP jen ke čtení, proto při nahrávání použijte aplikaci FTP jako FileZilla nebo Cyberduck.
{{% /details %}}

{{% details title="Můžu použít FTP mezi dvěma iPhony?" closed="true" %}}
Ano. Spusťte server FTP na prvním iPhonu. Na druhém otevřete Everdisk, přejděte na kartu Zařízení, klepněte na Nové připojení, zvolte FTP a zadejte adresu zobrazenou na prvním telefonu. Funguje i vyhrazená aplikace FTP pro iOS, protože aplikace Files v iOS klienta FTP neobsahuje.
{{% /details %}}

{{% details title="Je FTP bezpečné?" closed="true" %}}
Prosté FTP svůj provoz nešifruje, proto s ním zacházejte jako s nástrojem pro sítě, kterým důvěřujete, jako je vaše domácí Wi-Fi. Na síti, kterou neovládáte, použijte server SMB se zapnutým Vyžadovat šifrování SMB, který chrání každý přenos.
{{% /details %}}

{{% details title="Která zařízení se mohou připojit přes FTP?" closed="true" %}}
Téměř cokoli s klientem FTP. To zahrnuje počítače s Macem, Windows a Linuxem, aplikace FTP jako FileZilla a Cyberduck, správce souborů pro Android a hardware jako fotoaparáty, chytré TV, routery, boxy NAS a automatizační nástroje. Tento široký dosah je hlavním důvodem, proč zvolit FTP.
{{% /details %}}

{{% details title="Proč se moje připojení FTP přerušilo?" closed="true" %}}
Váš iPhone je server a iOS pozastavuje aplikace, které zůstávají příliš dlouho na pozadí. Během připojení zařízení mějte Everdisk otevřený na obrazovce a při dlouhých přenosech ho připojte k napájení. Také se ujistěte, že jsou obě zařízení stále na stejné Wi-Fi.
{{% /details %}}

{{% details title="Je Everdisk zdarma?" closed="true" %}}
Ano, Everdisk je zdarma ke stažení a server FTP je součástí. Volitelný jednorázový nákup Premium přidává doplňky, jako jsou vlastní porty a převod fotek a videí. FTP můžete nastavit a přenášet soubory bez placení.
{{% /details %}}

Chcete to vyzkoušet? [Stáhněte si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a během pár minut připojte svého prvního klienta FTP. Máte dotazy nebo zpětnou vazbu? Napište nám na **support@everappz.com**.
