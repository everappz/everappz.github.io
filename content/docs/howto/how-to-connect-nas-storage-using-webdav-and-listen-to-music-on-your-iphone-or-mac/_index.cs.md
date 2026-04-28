---
title: "Jak připojit úložiště NAS pomocí WebDAV a poslouchat hudbu na iPhone nebo Mac"
date: 2024-07-28
description: "Naučte se, jak nakonfigurovat WebDAV na vašem Synology NAS a streamovat hudbu na iPhone nebo Mac pomocí Evermusic nebo Flacbox. Postupujte podle našeho podrobného průvodce."
keywords: ["připojit nas", "webdav synology", "streamovat hudbu nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["hudba", "streaming", "úložiště", "nas", "připojení", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Shrnutí:** Nainstalujte a povolte WebDAV na vašem Synology NAS, nakonfigurujte oprávnění sdílené složky a poté se připojte z Evermusic nebo Flacbox pomocí IP adresy NAS a portu WebDAV (výchozí 5005/5006). Můžete streamovat a spravovat celou svou hudební knihovnu bez kopírování souborů do zařízení.

Zjistěte, jak připojit úložiště NAS pomocí WebDAV a snadno streamovat hudební knihovnu na iPhone nebo Mac. WebDAV (Web-based Distributed Authoring and Versioning) je protokol, který vám umožňuje spravovat a sdílet soubory přes internet. Nastavením WebDAV na vašem NAS můžete přistupovat ke své hudební sbírce a streamovat ji, takže budete mít své oblíbené skladby vždy na dosah.

V tomto průvodci vám ukážeme, jak nastavit připojení WebDAV na jednom z nejpopulárnějších serverů NAS, Synology NAS. Postupujte podle našich jednoduchých kroků pro konfiguraci WebDAV na vašem Synology NAS a budete moci procházet, streamovat a spravovat svou hudební knihovnu přímo z iPhone nebo Mac.

## Krok 1: Instalace WebDAV na Synology NAS

1. Přihlaste se do svého Synology NAS a otevřete **Centrum balíčků**.
2. Vyhledejte "webdav" a nainstalujte balíček WebDAV, pokud ještě není nainstalován. Otevřete server WebDAV pro jeho konfiguraci.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instalace WebDAV na Synology" width="600" >}}

## Krok 2: Konfigurace serveru WebDAV

1. Na stránce nastavení WebDAV zaškrtněte políčka **Povolit HTTP**, **Povolit HTTPS**, **Povolit anonymní WebDAV** a **Povolit DavDepthInfinity**.
2. Klikněte na **Použít** pro uložení změn. Poznamenejte si čísla portů pro připojení HTTP a HTTPS, která jsou ve výchozím nastavení 5005 a 5006.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Konfigurace nastavení WebDAV" width="600" >}}

## Krok 3: Konfigurace oprávnění sdílené složky

1. Otevřete **Ovládací panel** a přejděte do sekce **Sdílená složka**.
2. Vyberte složku **Hudba** a klikněte na **Upravit**.
3. Na kartě **Oprávnění** nakonfigurujte oprávnění. Povolte přístup hosta s oprávněním Pouze pro čtení, pokud potřebujete pouze poslouchat hudbu, nebo Čtení/Zápis, pokud potřebujete upravovat soubory. Uložte změny.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Oprávnění sdílené složky" width="600" >}}

## Krok 4: Zjištění IP adresy Synology NAS

1. Otevřete **Ovládací panel** a přejděte na kartu **Síťové rozhraní**, nebo použijte webový prohlížeč k návštěvě [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Zjištění IP adresy NAS" width="600" >}}

2. Poznamenejte si IP adresu vašeho Synology NAS (např. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="IP adresa Synology NAS" width="600" >}}

## Krok 5: Připojení k Synology NAS pomocí Evermusic/Flacbox

1. Otevřete aplikaci Evermusic nebo Flacbox a přejděte na kartu **Připojení**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Karta Připojení v Evermusic" width="600" >}}

2. Pro automatické připojení najděte svůj Synology NAS v sekci **Dostupná zařízení** a klepnutím se připojte.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Seznam dostupných zařízení" width="600" >}}

3. Pro ruční připojení vyberte **Připojit cloudovou službu** a zvolte **WebDAV**. Zadejte adresu serveru ve formátu: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (např. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Ruční konfigurace WebDAV" width="600" >}}

4. Pro přístup hosta ponechte pole pro přihlášení a heslo prázdná, nebo zadejte své přihlašovací údaje Synology. Klepněte na **Přihlásit se**.

## Krok 6: Procházení a přehrávání hudby

1. Po připojení se zařízení zobrazí v seznamu **Připojené příslušenství**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Připojená zařízení v Evermusic" width="600" >}}

2. Přejděte do složky **Hudba** a klepněte na libovolný zvukový soubor pro spuštění přehrávání.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Procházení složky s hudbou" width="600" >}}

## Krok 7: Přidání připojené cloudové složky do hudební knihovny

1. Otevřete sekci **Hudební knihovna** v aplikaci.
2. Vyberte **Přidat hudbu** a zvolte **Připojení**.
3. Vyberte připojený server NAS a zvolte složku **Hudba**. Klepněte na **Hotovo**.
4. Aplikace prohledá hudební složku a přidá podporované zvukové soubory do hudební knihovny. Načtou se metadata a vaše skladby budou seskupeny podle alba, interpreta a žánru.

## Závěr

Podle těchto kroků můžete snadno nastavit připojení WebDAV na vašem Synology NAS a streamovat hudební knihovnu na iPhone nebo Mac pomocí Evermusic nebo Flacbox. Užijte si bezproblémový přístup ke svým oblíbeným skladbám kdykoli.

## Často kladené otázky

{{% details title="Která zařízení NAS podporují WebDAV?" closed="true" %}}
Většina populárních značek NAS podporuje WebDAV, včetně Synology, QNAP, TrueNAS a Western Digital. Zkontrolujte dokumentaci výrobce vašeho NAS pro pokyny k nastavení WebDAV.
{{% /details %}}

{{% details title="Jaký je rozdíl mezi WebDAV a SMB pro streamování hudby z NAS?" closed="true" %}}
WebDAV funguje přes HTTP/HTTPS a je vhodnější pro vzdálený přístup přes internet. SMB je obvykle rychlejší v lokálních sítích. Evermusic a Flacbox podporují oba protokoly, takže si vyberte podle toho, zda potřebujete lokální nebo vzdálený přístup.
{{% /details %}}

{{% details title="Potřebuji uživatelské jméno a heslo pro WebDAV na Synology?" closed="true" %}}
Ne, pokud povolíte anonymní přístup WebDAV a nakonfigurujete oprávnění hosta pro sdílenou složku. Pro lepší zabezpečení můžete místo toho použít své přihlašovací údaje Synology.
{{% /details %}}

{{% details title="Mohu streamovat FLAC a další formáty ve vysokém rozlišení z NAS přes WebDAV?" closed="true" %}}
Ano. Evermusic i Flacbox podporují FLAC, ALAC, WAV, DSD a další formáty ve vysokém rozlišení při streamování z úložiště NAS přes WebDAV.
{{% /details %}}

{{% details title="Proč aplikace nemůže najít můj NAS v Dostupných zařízeních?" closed="true" %}}
Ujistěte se, že váš iPhone/Mac a NAS jsou na stejné síti Wi-Fi. Pokud automatické vyhledávání nefunguje, použijte možnost ručního připojení a zadejte IP adresu NAS a port WebDAV přímo.
{{% /details %}}
