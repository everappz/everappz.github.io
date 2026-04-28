---
title: "Jak připojit Synology NAS a poslouchat hudbu na iPhone nebo Mac"
date: 2024-09-19
description: "Naučte se, jak připojit Synology NAS pomocí nativního API nebo QuickConnect a streamovat vysoce kvalitní hudbu na iPhone nebo Mac s Evermusic a Flacbox."
keywords: ["synology nas", "streamování hudby", "quickconnect", "evermusic synology", "flacbox synology", "hudební přehrávač nas", "hudba iphone nas"]
tags: ["hudba", "streamování", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Shrnutí:** Připojte svůj Synology NAS k Evermusic nebo Flacbox pomocí nativního API Synology -- buď ručně přes IP adresu, nebo automaticky přes QuickConnect ID. QuickConnect vám umožňuje streamovat hudbu vzdáleně bez přesměrování portů. Obě aplikace podporují FLAC, MP3, WAV a další hi-res formáty.

Pokud hledáte bezproblémový způsob, jak připojit svůj Synology NAS a užívat si svou hudební knihovnu na iPhone nebo Mac, aplikace Evermusic a Flacbox jsou perfektním řešením. Tyto aplikace podporují širokou škálu audio formátů, včetně FLAC, MP3 a WAV, což usnadňuje streamování a poslech vysoce kvalitní hudby přímo z vašeho Synology NAS.

V tomto průvodci vám ukážeme, jak připojit Synology NAS k aplikaci Evermusic nebo Flacbox pomocí nativního API Synology a funkce QuickConnect. Využitím přímého API Synology můžete bezpečně přistupovat ke své hudební knihovně mimo domácí síť bez nutnosti složitých konfigurací jako WebDAV, SMB, DLNA. S QuickConnect budete moci streamovat a spravovat svou hudbu odkudkoli pomocí iPhone nebo Mac.

## Krok 1: Konfigurace oprávnění sdílené složky (volitelné)

1. Otevřete **Ovládací panel** a přejděte do sekce **Sdílená složka**.

![Sdílená složka](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Vyberte složku **Hudba** a klikněte na **Upravit**.

3. Na kartě **Oprávnění** nakonfigurujte oprávnění. Povolte přístup pro hosty s oprávněním pouze ke čtení, pokud potřebujete pouze poslouchat hudbu, nebo čtení/zápis, pokud potřebujete upravovat soubory. Uložte změny.

![Oprávnění](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Krok 2: Zjištění IP adresy Synology NAS

1. Otevřete **Ovládací panel** a přejděte na kartu **Síťové rozhraní**.

![Síťové rozhraní](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Nebo použijte webový prohlížeč k návštěvě [find.synology.com](http://find.synology.com).

![Najít Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Poznamenejte si IP adresu vašeho Synology NAS (např. 192.168.18.137).

## Krok 3: Zjištění síťových portů Synology NAS

Oficiální dokumentaci Synology pro výchozí síťové porty DSM najdete v tomto [článku znalostní báze Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM používá následující výchozí porty:
- **HTTP (Webový přístup):** Port **5000**
- **HTTPS (Zabezpečený webový přístup):** Port **5001**

Toto jsou výchozí porty pro přístup k rozhraní DSM.

![Síťové porty](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Krok 4: Povolení funkce QuickConnect ID

QuickConnect ID od Synology je jedinečný identifikátor, který vám umožňuje vzdáleně přistupovat k Synology NAS přes internet bez nutnosti konfigurovat složitá síťová nastavení, jako je přesměrování portů. QuickConnect zjednodušuje vzdálený přístup využitím serverů Synology k navázání spojení mezi vaším NAS a vaším zařízením, jako je smartphone nebo počítač, prostřednictvím QuickConnect ID.

**Jak najít nebo nastavit QuickConnect ID:**

1. **Přihlaste se do DSM.**
2. Přejděte na **Ovládací panel > Externí přístup > QuickConnect**.
3. **Povolte QuickConnect** a vytvořte nebo zobrazte svůj jedinečný QuickConnect ID.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Krok 5: Připojení k Synology NAS na iPhone/Mac pomocí Evermusic nebo Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) a [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) jsou hudební přehrávače navržené pro zařízení iOS a macOS, z nichž každý nabízí jedinečné funkce a možnosti pro správu a užívání vaší hudební knihovny.

1. Otevřete aplikaci Evermusic nebo Flacbox a přejděte na kartu **Připojení**.

![Připojení](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Vyberte **Připojit cloudovou službu** a zvolte **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Máte dvě možnosti připojení: **ruční** pomocí IP adresy serveru a portu, nebo **automatické** přes QuickConnect ID.

### Ruční připojení

Pro ruční metodu budete potřebovat přímou IP adresu a číslo portu, které jste získali v předchozích krocích.

1. Zadejte URL serveru, kterou jste získali v kroku 2, v následujícím formátu: PROTOKOL://IP_ADRESA:ČÍSLO_PORTU
   - Použijte **port 5000** pro HTTP a **port 5001** pro připojení HTTPS.

   Například:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Skutečné číslo portu lze ověřit v kroku 3 vašeho nastavení.
3. Zadejte své **přihlašovací jméno** a **heslo** pro Synology NAS.
4. Klepněte na **Přihlásit se** pro navázání připojení.

![Ruční připojení](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Automatické připojení

Pro automatické připojení použijete **QuickConnect ID** z kroku 4. Místo ručního zadávání IP adresy a čísla portu vašeho Synology NAS jednoduše zadejte **QuickConnect ID**. Aplikace automaticky načte potřebné informace o připojení.

Tato metoda vám umožňuje přistupovat k NAS vzdáleně, i mimo domácí síť, takže můžete spravovat své soubory z internetu bez nutnosti konfigurace přesměrování portů nebo statických IP adres.

![Automatické připojení](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Dvoufaktorové ověřování

Počínaje DSM 4.2 zavedla Synology **dvoufázové ověřování** pro zvýšení bezpečnosti. Tato funkce vyžaduje kód **jednorázového hesla (OTP)**, generovaný autentizační aplikací, kromě vašich běžných přihlašovacích údajů. Pokud jste povolili dvoufázové ověřování, po zadání uživatelského jména a hesla budete muset zadat také OTP pro přihlášení do relace DSM.

Upozorňujeme, že po vypršení relace bude nutné aplikaci znovu autorizovat ručně. Pro opětovnou autorizaci:

1. Přejděte na kartu **Připojení** v aplikaci.
2. Klepněte na tlačítko **Další akce** vedle názvu serveru.
3. Vyberte **Nastavení** z nabídky pro zadání nového autentizačního kódu a dokončení procesu opětovné autorizace.

Tím je zajištěno, že i když přistupujete k NAS z nedůvěryhodné sítě, vaše data zůstanou v bezpečí.

## Krok 6: Procházení a přehrávání hudby

1. Po připojení se zařízení zobrazí v seznamu **Připojená zařízení**.

![Připojená zařízení](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Přejděte do složky **Hudba** a klepnutím na libovolný audio soubor spusťte přehrávání.

![Přehrát hudbu](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Krok 7: Přidání připojené cloudové složky do hudební knihovny

1. Otevřete sekci **Hudební knihovna** v aplikaci.
2. Vyberte **Přidat hudbu** a zvolte **Připojení**.
3. Vyberte připojený server NAS a zvolte složku **Hudba**. Klepněte na **Hotovo**.
4. Aplikace prohledá hudební složku a přidá podporované audio soubory do hudební knihovny. Metadata budou načtena a vaše skladby budou seskupeny podle alba, interpreta a žánru.

## Závěr

Dodržením těchto kroků můžete snadno nastavit připojení na Synology NAS a streamovat celou hudební knihovnu na iPhone nebo Mac pomocí Evermusic nebo Flacbox. Ať už jste doma nebo na cestách, užívejte si bezproblémový, vysoce kvalitní přístup ke svým oblíbeným skladbám odkudkoli pomocí QuickConnect. Využijte flexibility a pohodlí, které tyto aplikace nabízejí, a začněte spravovat svou hudební sbírku s lehkostí na všech svých zařízeních.

S bezpečným vzdáleným přístupem přes QuickConnect a podporou široké škály audio formátů nebudete nikdy daleko od své hudby. Nyní jsou vaše soubory uložené na NAS na dosah jediného klepnutí!

## Často kladené otázky

{{% details title="Jaký je rozdíl mezi ručním připojením a QuickConnect?" closed="true" %}}
Ruční připojení používá IP adresu NAS a port, což funguje na vaší lokální síti. QuickConnect využívá přenosovou službu Synology k navázání připojení odkudkoli přes internet, bez přesměrování portů.
{{% /details %}}

{{% details title="Mohu streamovat hudbu ze Synology NAS mimo domácí síť?" closed="true" %}}
Ano. Povolte QuickConnect na Synology NAS a použijte QuickConnect ID v Evermusic nebo Flacbox pro streamování hudby odkudkoli s připojením k internetu.
{{% /details %}}

{{% details title="Které audio formáty jsou podporovány při streamování ze Synology NAS?" closed="true" %}}
Evermusic a Flacbox podporují FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD a mnoho dalších formátů. Všechny podporované formáty fungují při streamování ze Synology NAS.
{{% /details %}}

{{% details title="Potřebuji dvoufaktorové ověřování pro připojení?" closed="true" %}}
Ne, dvoufaktorové ověřování je volitelné. Pokud jste však povolili dvoufázové ověřování na Synology DSM, aplikace vás požádá o jednorázové heslo během přihlašování. Budete muset provést opětovnou autorizaci po vypršení relace.
{{% /details %}}

{{% details title="Mám použít nativní API Synology, WebDAV nebo SMB pro připojení?" closed="true" %}}
Nativní API Synology s QuickConnect je nejlepší volbou pro vzdálený přístup. Pro použití v lokální síti je SMB obvykle nejrychlejší možností. WebDAV funguje dobře pro lokální i vzdálený přístup. Evermusic a Flacbox podporují všechny tři protokoly.
{{% /details %}}
