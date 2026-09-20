---
title: "Jak nastavit mediální server DLNA/UPnP na iPhonu a iPadu pro streamování"
description: "Proměňte iPhone nebo iPad v mediální server DLNA/UPnP pomocí Everdisku a streamujte fotky, videa a hudbu do chytré TV, herní konzole, VLC nebo Kodi přes Wi-Fi. Kompletní nastavení a návod, jak se připojit z TV Samsung, LG a Sony, z Windows, Macu, Linuxu, Androidu i z dalšího iPhonu."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "mediální server", "streamování", "chytrá tv", "iphone", "ipad", "wifi"]
keywords: ["DLNA server iPhone", "UPnP server iPad", "jak nastavit DLNA na iPhonu", "streamování do chytré TV z iPhonu", "mediální server DLNA iOS", "streamování videí do TV bez kabelu", "přehrávání fotek z iPhonu na TV", "Samsung TV DLNA iPhone", "LG TV DLNA iPhone", "Sony Bravia DLNA iPhone", "VLC DLNA iPhone", "Kodi DLNA mediální server", "mediální server UPnP AV iOS", "streamování hudby do TV z iPhonu", "aplikace mediální server iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (označované také jako UPnP AV) je tichým tahounem většiny chytrých TV. Je to sdílený jazyk, který umožňuje televizi nebo přehrávači médií najít mediální knihovnu ve stejné Wi-Fi a přehrávat z ní, aniž byste do TV cokoli instalovali. Pokud může vaše zařízení iPhone nebo iPad fungovat jako tato knihovna, vaše fotky, videa a hudba se na velké obrazovce objeví samy.

Tento návod ukazuje, jak proměnit iPhone nebo iPad v mediální server DLNA/UPnP pomocí aplikace [Everdisk](/products/everdisk) a jak tuto knihovnu otevřít z chytré TV, herní konzole, VLC, Kodi, počítače, telefonu s Androidem i z druhého iPhonu. Vše běží přes vaši místní Wi-Fi, takže se nikam nic nenahrává.

## Co budete potřebovat

- iPhone nebo iPad s nainstalovanou aplikací [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8).
- TV, přehrávač nebo počítač ve **stejné síti Wi-Fi** jako vaše zařízení.
- Fotky, videa nebo hudbu, které chcete přehrávat, už uložené v iPhonu (v aplikaci Fotky, v aplikaci Hudba nebo ve složce Dokumenty v Everdisku).

## Nastavení serveru DLNA v Everdisku

### Krok 1: Vyberte, co sdílet

Otevřete Everdisk a přejděte na kartu **Sdílení**. Klepněte na **Co sdílet** a vyberte svůj obsah:

- Zapněte **Povolit přístup k celé knihovně fotek** a nasdílejte každé album, nebo klepněte na **Přidat fotky** a vyberte jen některé.
- Zapněte **Povolit přístup k celé hudební knihovně** a nasdílejte své skladby, nebo klepněte na **Přidat skladby** pro výběr.
- Přidejte libovolné složky nebo soubory pomocí **Přidat složku** a **Přidat soubor**. Vlastní složka Dokumenty aplikace je sdílena ve výchozím nastavení.

Než může sdílení začít, musíte mít vybranou alespoň jednu položku.

### Krok 2: Zapněte Televizi a mediální centrum (DLNA)

Přejděte do **Nastavení**, poté **Sdílení** a poté **Připojení**. Ujistěte se, že je **Televize a mediální centrum** zapnuté. Ve výchozím nastavení je zapnuté a nese značku DLNA. To je server, který TV a přehrávače vyhledávají.

### Krok 3: Spusťte sdílení

Zpět na kartě **Sdílení** klepněte na velké tlačítko **Spustit**. Vaše zařízení je nyní mediálním serverem ve vaší Wi-Fi. Ostatním zařízením se zobrazí pod svým přívětivým názvem, tím, který je v aplikaci uvedený jako název zařízení (něco jako „Speedy-Hare“, dokud jej nezměníte).

Streamování přes DLNA je vždy otevřené, takže na TV nezadáváte žádné heslo. Everdisk mějte během sledování otevřený na obrazovce, protože iOS pozastavuje aplikace, které se úplně přesunou na pozadí.

## Přehrávání na chytré TV

To je nejčastější případ a obvykle to zabere zhruba třicet sekund.

1. Připojte TV ke **stejné Wi-Fi** jako iPhone.
2. Otevřete na TV vestavěný přehrávač médií. Název závisí na značce: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** nebo **SmartThings** (Samsung), **Content Share** nebo **SimplyShare**.
3. Vyhledejte seznam mediálních serverů nebo zdrojů. Vaše zařízení se tam objeví pod svým názvem.
4. Vyberte ho, projděte se do svých fotek, videí nebo hudby a spusťte přehrávání.

Náhledové miniatury se zobrazují automaticky, takže správné album z dovolené nebo film najdete bez hádání.

### Které TV fungují

Většina TV od značek **Samsung, LG, Sony BRAVIA, Panasonic (firmware VIERA), Philips a Hisense** má DLNA vestavěné a funguje hned. **Konzole PlayStation a Xbox a většina AV receiverů** rovněž.

Několik platforem to vynechává: **TV Roku, Amazon Fire TV, Vizio SmartCast a čisté Google TV** bez mediální aplikace výrobce. Pokud je vaše TV jednou z nich a nemůže vaše zařízení najít, obvykle je to právě z tohoto důvodu. Na těchto TV nainstalujte aplikaci pro přehrávání DLNA, například VLC nebo Kodi, nebo se ke svým souborům dostaňte přes webový prohlížeč podle [návodu na nastavení WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Některé značky ponechaly DLNA funkční i po odebrání oficiálního loga DLNA, takže pokud se zdá, že chybí, hledejte jeden z výše uvedených názvů přehrávače médií.

## Přehrávání ve VLC nebo Kodi na Windows, Macu a Linuxu

VLC a Kodi jsou zdarma, běží na každém stolním systému a DLNA umí dobře. Jsou spolehlivým způsobem, jak otevřít svou knihovnu Everdisk na počítači.

**VLC (Windows, Mac, Linux):**

1. Otevřete VLC.
2. Zobrazte seznam skladeb (na Windows a Linuxu stiskněte **Ctrl+L**, na Macu otevřete **Playlist** z nabídky View).
3. V postranním panelu otevřete **Universal Plug'n'Play** v části Local Network.
4. Vaše zařízení se objeví v seznamu. Klikněte na něj a vyberte soubor.

**Kodi (Windows, Mac, Linux):**

1. Přejděte do **Videos**, **Music** nebo **Pictures**, poté **Files** a poté **Add source** (nebo **Browse**).
2. Zvolte **UPnP devices**.
3. Vyberte své zařízení a procházejte svou knihovnu.

Na Windows můžete také otevřít **Windows Media Player**, rozbalit **Other Libraries** v postranním panelu a vaše zařízení se tam objeví.

## Přehrávání na Androidu

Telefony a tablety s Androidem nemají systémový prohlížeč DLNA, proto použijte aplikaci:

- **VLC pro Android**: otevřete boční nabídku, klepněte na **Local Network** a vaše zařízení se objeví pod servery UPnP.
- **BubbleUPnP** nebo podobná aplikace UPnP: vaše zařízení se objeví v seznamu serverů a tyto aplikace umí přehrávání také posílat na TV.

## Přehrávání na dalším iPhonu nebo iPadu

Dvě zařízení, jedna knihovna. Řekněme, že fotky máte na iPhonu a chcete si je prohlédnout na iPadu.

- Nejjednodušší cestou je vlastní karta **Zařízení** v Everdisku na druhém zařízení. Funguje jako klient DLNA i jako server. Otevřete Everdisk na iPadu, přejděte na **Zařízení** a váš iPhone se objeví pod **Dostupná zařízení**. Klepnutím na něj procházejte a přehrávejte.
- Funguje i libovolná aplikace pro přehrávání DLNA pro iOS, například VLC nebo prohlížeč UPnP. Otevřete její zobrazení místní sítě a vyberte svůj iPhone.

## Přehrávání na herní konzoli

- **PlayStation 5 a 4**: otevřete aplikaci **Media** (Media Gallery) a vaše zařízení se objeví jako mediální server, který můžete procházet.
- **Xbox**: použijte aplikaci pro přehrávání médií, která podporuje DLNA, a poté vyberte své zařízení ze seznamu serverů.

## Pokud se vaše zařízení v seznamu neobjeví

Některé přehrávače umožňují přidat mediální server podle adresy, místo aby čekaly na jeho automatické objevení. Na obrazovce **Sdílení** v Everdisku zobrazuje karta DLNA adresu s popisem zařízení, která končí na `/device-desc.xml`. Zadejte tuto adresu do pole pro přidání serveru v přehrávači.

Pokud se stále nezobrazí, zkontrolujte tři věci: obě zařízení jsou ve stejné Wi-Fi (ne v hostovské síti, která blokuje provoz mezi zařízeními), Everdisk je otevřený a sdílení je spuštěné a v Nastavení je zapnuté **Televize a mediální centrum**.

## Pokud se video nechce přehrát

DLNA předá soubor TV tak, jak je, a TV ho musí umět dekódovat. Pokud se klip odmítá přehrát, jeho formát pravděpodobně daná TV nepodporuje. Dvě řešení:

- Otevřete **Nastavení**, poté **Sdílení** a poté **Videa** a snižte **Kvalitu**. Everdisk pak video při streamování převede do kompatibilnějšího formátu. (Převod je funkce Premium.)
- Nebo otevřete stejný soubor ve webovém prohlížeči pomocí odkazu na prohlížeč z Everdisku, který je k formátům shovívavější.

## Jak to lidé používají v praxi

- **Filmový večer s rodinou.** Videa natočená na telefonu se přehrají na TV v obývacím pokoji bez kabelu nebo Apple TV.
- **Fotky z dovolené na velké obrazovce.** Otevřete svou knihovnu Fotky na TV a procházejte výlet s celou místností.
- **Hudba na pozadí na oslavě.** Nasměrujte reproduktor DLNA nebo AV receiver na svou knihovnu Hudba a nechte ji hrát.
- **Sledování na hotelové TV**, která má přehrávač médií, jakmile jsou obě zařízení na Wi-Fi pokoje.

## Několik tipů

- Během streamování mějte Everdisk otevřený. Pokud telefon na dlouho zamknete, iOS může aplikaci pozastavit a přehrávání se zastaví.
- Při dlouhých filmových seancích připojte telefon k napájení.
- Pro nejrychlejší streamování ponechte v Nastavení **Formát** a **Kvalitu** na **Original** a snižujte je jen tehdy, když má konkrétní TV se souborem potíže.
- DLNA slouží jen ke streamování. Nikdo na straně TV nemůže vaše soubory měnit ani mazat. Pro obousměrný přenos souborů použijte místo toho server [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) nebo [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/).

## Často kladené otázky

{{% details title="Jaký je rozdíl mezi DLNA a UPnP?" closed="true" %}}
Jsou úzce příbuzné. UPnP je základní síťový standard a DLNA je mediální profil postavený na něm, který TV a přehrávače používají ke sdílení a přehrávání fotek, videí a hudby. V běžném použití jsou tato slova zaměnitelná. Když v Everdisku zapnete Televizi a mediální centrum, vaše zařízení se stane mediálním serverem DLNA/UPnP, který může procházet jakýkoli klient DLNA.
{{% /details %}}

{{% details title="Musím na TV něco instalovat?" closed="true" %}}
Ne. Pokud vaše TV podporuje DLNA, už má přehrávač médií, který dokáže vaše zařízení najít na Wi-Fi. Everdisk instalujete jen na iPhone nebo iPad, který obsahuje obsah. Pokud vaše TV DLNA nepodporuje, nainstalujte přehrávač jako VLC nebo Kodi na zařízení, které je k ní připojené.
{{% /details %}}

{{% details title="Proč se můj iPhone na TV nezobrazí?" closed="true" %}}
Zkontrolujte, že jsou obě zařízení ve stejné síti Wi-Fi. Hostovské sítě a některé firemní nebo hotelové sítě brání zařízením ve vzájemném vidění, což DLNA zastaví. Poté ověřte, že je Everdisk otevřený se spuštěným sdílením a že je v Nastavení, Sdílení, Připojení zapnuté Televize a mediální centrum. Pokud TV stále nemůže zařízení najít, přidejte server ručně pomocí adresy s popisem zařízení, která končí na /device-desc.xml.
{{% /details %}}

{{% details title="Vyžaduje streamování přes DLNA heslo?" closed="true" %}}
Ne. DLNA je, dokud je zapnuté, vždy otevřené komukoli ve stejné Wi-Fi, a proto na straně TV není žádné přihlášení. To je v pořádku na domácí síti, které důvěřujete. Na síti, které nedůvěřujete, po dokončení Televizi a mediální centrum vypněte, nebo místo toho použijte server SMB se šifrováním.
{{% /details %}}

{{% details title="Můžu streamovat na Chromecast nebo Roku?" closed="true" %}}
Chromecast a Roku ve výchozím stavu jako přehrávače DLNA nefungují, takže vaše zařízení přímo nenajdou. Řešením je nainstalovat aplikaci DLNA, která umí odesílat obraz, například VLC nebo BubbleUPnP na telefonu, a přehrávání na Chromecast nebo Roku posílat odtud. Na většině ostatních chytrých TV DLNA funguje bez čehokoli z toho.
{{% /details %}}

{{% details title="Video se přehrává bez zvuku nebo se neotevře. Co mohu dělat?" closed="true" %}}
To je formát, který TV nedokáže dekódovat. Otevřete v Everdisku Nastavení, Sdílení, Videa a snižte Kvalitu, aby aplikace video při streamování převedla do kompatibilnějšího formátu. Stejný soubor můžete také otevřít přes odkaz na prohlížeč, který zvládá více formátů.
{{% /details %}}

{{% details title="Můžu streamovat hudbu, ne jen video?" closed="true" %}}
Ano. Zapněte Povolit přístup k celé hudební knihovně, nebo přidejte konkrétní skladby, a poté spusťte sdílení. Vaše skladby se objeví na jakémkoli reproduktoru DLNA, AV receiveru nebo TV, s obalem a údaji o skladbě. Hudba se vždy sdílí v původní kvalitě.
{{% /details %}}

{{% details title="Musí aplikace během sledování zůstat otevřená?" closed="true" %}}
Ano. Váš iPhone funguje jako server a iOS pozastavuje aplikace, které se na dlouhou dobu úplně přesunou na pozadí. Během streamování mějte Everdisk na obrazovce a při dlouhých seancích ho připojte k napájení.
{{% /details %}}

{{% details title="Jak streamuji z jednoho iPhonu na druhý iPad?" closed="true" %}}
Spusťte sdílení na iPhonu, poté otevřete Everdisk na iPadu a přejděte na kartu Zařízení. iPhone se objeví pod Dostupná zařízení jako mediální server. Klepnutím na něj procházejte a přehrávejte. Everdisk funguje jako klient DLNA i jako server, takže nepotřebujete další aplikaci.
{{% /details %}}

{{% details title="Je Everdisk zdarma?" closed="true" %}}
Ano, Everdisk je zdarma ke stažení a mediální server DLNA je součástí. Volitelný jednorázový nákup Premium Lifetime přidává doplňky, jako je převod fotek a videí pro starší TV, vlastní porty a další. Streamování přes DLNA můžete nastavit a používat bez placení.
{{% /details %}}

Chcete to vyzkoušet? [Stáhněte si Everdisk z App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) a během pár minut streamujte na TV své první album. Máte dotazy nebo zpětnou vazbu? Napište nám na **support@everappz.com**.
