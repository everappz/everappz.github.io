---
title: "Jak přehrávat hudbu z Mac / PC / Linux / NAS na iPhone pomocí serveru Kodi DLNA"
date: 2025-07-25
description: "Streamujte hudbu z počítače nebo NAS do iPhone přes Wi-Fi pomocí Kodi DLNA a aplikace Evermusic."
keywords: ["kodi dlna server", "streamování hudby na iphone", "přehrávání hudby z nas", "evermusic dlna", "hudba z mac na iphone", "hudba z windows na iphone", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streamování hudby", "mac", "nas", "linux", "lokální síť"]
readingTime: 5
---

{{< author-byline >}}


**Shrnutí:** Nainstalujte Kodi na Mac, PC, Linux nebo NAS, povolte jeho DLNA/UPnP server a streamujte celou svou hudební knihovnu na iPhone nebo iPad pomocí bezplatné aplikace Evermusic nebo Flacbox přes Wi-Fi. Žádné předplatné není potřeba.

## Úvod

Pokud máte **Mac, PC s Windows, Linux nebo NAS zařízení**, můžete ho snadno proměnit v **osobní hudební server** doma pomocí [Kodi](https://kodi.tv/), bezplatné a open-source mediální platformy. S vestavěným **DLNA/UPnP serverem** Kodi můžete streamovat celou svou hudební knihovnu na jakéhokoli klienta kompatibilního s DLNA — včetně vašeho iPhone nebo iPad.

V tomto průvodci vám ukážeme krok za krokem, jak:

- Nainstalovat Kodi na Mac nebo PC  
- Nastavit hudební složky pro sdílení  
- Povolit DLNA hudební server  
- Přistupovat k hudbě pomocí aplikace **Evermusic** nebo **Flacbox** pro iOS

Toto nastavení je 100% zdarma — žádné předplatné, jen vaše vlastní hudba streamovaná přes vaši Wi-Fi síť. Ať už se snažíte organizovat svou velkou sbírku MP3, poslouchat FLAC přes Wi-Fi, nebo si jednoduše užívat lokální hudbu bez synchronizace přes iTunes, toto nastavení je pro vás ideální.

## Stažení a instalace Kodi na Mac / PC / Linux / NAS

Nejprve navštivte oficiální webové stránky Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Hlavní stránka Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klikněte na **Stáhnout** a přejděte dolů k nalezení verze pro váš počítač.
Vyberte svůj operační systém. V tomto příkladu použijeme **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Stránka stahování Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klikněte na **Intel (x86/64)**, pokud máte Intel Mac, nebo **Apple Silicon** pro M1, M2, M3 Mac pro zahájení stahování.

{{< cards cols="1">}}
{{< card subtitle="Vyberte instalátor macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Počkejte chvíli, než se instalátor stáhne.

{{< cards cols="1">}}
{{< card subtitle="Kodi staženo" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Po stažení najděte soubor `.dmg` ve složce **Stažené soubory**.

{{< cards cols="1">}}
{{< card subtitle="Instalace Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Poklepejte na stažený soubor pro spuštění instalátoru.
Přetáhněte Kodi do složky **Aplikace** pro instalaci.

{{< cards cols="1">}}
{{< card title="" subtitle="Nainstalujte Kodi přetažením do Aplikací" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Spusťte Kodi. Možná budete muset povolit aplikaci v **Předvolby systému → Zabezpečení a soukromí → Přesto otevřít**.

{{< cards cols="1">}}
{{< card subtitle="Hlavní obrazovka Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Přidání hudby do knihovny Kodi

Klikněte na **ikonu ozubeného kola** (Nastavení) z domovské obrazovky.

{{< cards cols="1">}}
{{< card subtitle="Nastavení Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Přejděte do **Nastavení médií → Knihovna**. Povolte **Aktualizovat knihovnu při spuštění** pro video knihovnu a hudební knihovnu pro automatickou indexaci.

{{< cards cols="1">}}
{{< card subtitle="Nastavení knihovny" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Poté přejděte do sekce **Hudba** a klikněte na **Přidat hudbu**.

{{< cards cols="1">}}
{{< card subtitle="Přidat hudební složku" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Procházejte a vyberte složku, kde je uložena vaše hudba.

{{< cards cols="1">}}
{{< card subtitle="Vybrat zdroj hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Přidejte zdroj hudby do Kodi.

{{< cards cols="1">}}
{{< card subtitle="Přidat zdroj hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Potvrďte a nechte Kodi prohledat vaši hudební knihovnu.

{{< cards cols="1">}}
{{< card subtitle="Potvrdit zdroje hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Počkejte chvíli, než bude knihovna prohledána a plně vytvořena.

{{< cards cols="1">}}
{{< card subtitle="Prohledávání hudební knihovny" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Povolení DLNA serveru Kodi

Přejděte do **Nastavení → Služby → UPnP/DLNA**.

Povolte možnost: **Sdílet mé knihovny**.

Kodi nyní funguje jako DLNA server na vaší lokální Wi-Fi síti.

{{< cards cols="1">}}
{{< card subtitle="Povolení DLNA v Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Otevření knihovny Kodi

Klikněte pravým tlačítkem pro zavření okna nastavení a otevření hlavní knihovny Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Klikněte pravým tlačítkem pro přístup ke knihovně Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Stažení aplikace pro streamování hudby pro iOS

Získejte bezplatnou iOS DLNA klientskou aplikaci, která vám umožní streamovat hudbu z široké škály cloudových úložišť a DLNA serverů.

- Použijte **Evermusic**, pokud je vaše sbírka převážně MP3 a jiné standardní audio formáty.
- Zvolte **Flacbox**, pokud máte hi-res hudební knihovnu ve formátech jako FLAC, ALAC nebo DSD.

Obě aplikace jsou dostupné pro **iOS** a **macOS** a jsou zdarma k použití.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Stáhnout Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Stáhnout Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Přidání zdroje DLNA

Po stažení iOS aplikace otevřete sekci **Všechna Připojení**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hlavní postranní panel aplikace Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Přejděte dolů a klepněte na **Lokální síť - Dostupná zařízení** pro objevení DLNA serverů.
V této sekci uvidíte všechna dostupná zařízení ve vaší lokální síti. Váš **Kodi DLNA server** by se zde měl objevit. Klepněte na server Kodi pro připojení.

{{< cards cols="1">}}
{{< card title="" subtitle="Dostupná DLNA zařízení v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic zobrazí složky knihovny sdílené prostřednictvím Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudební knihovna Kodi v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Přejděte do složky **Skladby** pro zobrazení všech dostupných audio souborů na vašem DLNA serveru.

{{< cards cols="1">}}
{{< card title="" subtitle="Skladby ze vzdálené složky" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Klepněte na jakýkoli audio soubor pro okamžité zahájení streamování.

{{< cards cols="1">}}
{{< card title="" subtitle="Přehrávání MP3 souboru v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Vraťte se do sekce **Připojení**. Přidaný DLNA server se zde nyní objeví. Klepněte na jeho ikonu pro opětovné připojení kdykoli. Z této obrazovky můžete také připojit další cloudové služby pomocí stejných kroků.

Zde můžete také povolit **sledování Last.fm**. Statistiky přehrávání se uloží do vašeho účtu Last.fm a poskytnou vám personalizovaná hudební doporučení.

{{< cards cols="1">}}
{{< card title="" subtitle="Připojení v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Vytvoření hudební knihovny

**Evermusic** i **Flacbox** vám umožňují přidat hudbu do knihovny a organizovat ji podle **metadatových tagů**, jako jsou interpreti, alba, žánry a skladatelé.

Pro začátek otevřete sekci **Hudební knihovna**. Přejděte dolů k **Nástroje a předvolby** a klepněte na **Přidat hudbu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudební knihovna Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Vyberte zdroj hudby — v tomto případě zvolte **Připojení**.

{{< cards cols="1">}}
{{< card title="" subtitle="Přidat novou hudbu v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Najděte **Kodi DLNA server** v Připojeních a klepněte pro zobrazení složek a souborů.

{{< cards cols="1">}}
{{< card title="" subtitle="Vybrat DLNA server pro import hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Vyberte složky nebo soubory, které chcete přidat, a klepněte na **Hotovo**.

{{< cards cols="1">}}
{{< card title="" subtitle="Vybrat hudební složku k přidání" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplikace prohledá vybrané soubory a uspořádá je pomocí metadat do sekcí jako Interpreti, Alba, Žánry a Skladatelé.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudební knihovna s kategoriemi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Vytvoření seznamů skladeb

Můžete si také vytvořit vlastní seznamy skladeb.

Nejprve otevřete kartu **Seznamy skladeb**.

{{< cards cols="1">}}
{{< card title="" subtitle="Karta seznamů skladeb v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Klepněte na tlačítko **plus (+)** a zvolte **Nový seznam skladeb**.

{{< cards cols="1">}}
{{< card title="" subtitle="Vytvořit nový seznam skladeb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Zadejte název seznamu skladeb a klepněte na **Uložit**.

{{< cards cols="1">}}
{{< card title="" subtitle="Zadejte název seznamu skladeb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Dále zvolte zdroj pro přidání skladeb — zde vybereme **Knihovnu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Přidat skladby do nového seznamu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Vyberte požadované skladby a klepněte na **Hotovo** pro jejich přidání.

{{< cards cols="1">}}
{{< card title="" subtitle="Přidat hudbu z knihovny do seznamu skladeb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Vybrané skladby se nyní zobrazí ve vytvořeném seznamu skladeb.

{{< cards cols="1">}}
{{< card title="" subtitle="Vytvořený seznam skladeb zobrazený v seznamu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Ve výchozím nastavení jsou skladby dostupné pro streamování. Pro poslech offline povolte **Offline režim** — aplikace stáhne všechny skladby seznamu.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline režim povolen pro seznam skladeb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Klepněte na tlačítko **Další akce** pro prozkoumání dalších možností. Můžete:

- Archivovat seznam skladeb  
- Změnit obal alba  
- Přeuspořádat skladby  
- A další užitečné funkce

{{< cards cols="1">}}
{{< card title="" subtitle="Další akce seznamu skladeb k dispozici" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Závěr

S **Evermusic** a **Flacbox** je proměna vašeho iPhone, iPad nebo Mac v výkonný DLNA hudební přehrávač snadná. Ať už ukládáte hudbu v cloudu, na NAS nebo na domácím mediálním serveru jako **Kodi**, tyto aplikace vám umožní streamovat, organizovat a užívat si svou sbírku bez omezení.

- Streamujte MP3 nebo hi-res FLAC přímo z vašeho **Kodi DLNA serveru**  
- Vytvořte si osobní hudební knihovnu seskupenou podle metadat (alba, žánry, skladatelé)  
- Vytvářejte a spravujte **vlastní seznamy skladeb**  
- Povolte **offline režim** pro poslech na cestách  
- Připojte se k **více cloudovým službám** a **zařízením lokální sítě**  
- Sledujte své poslechové návyky s **integrací Last.fm**

Ať už jste audiofil nebo příležitostný posluchač, Evermusic a Flacbox nabízejí vše, co potřebujete pro bezproblémové streamování a organizaci hudby.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Stáhnout Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Stáhnout Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Začněte budovat svůj osobní hudební zážitek ještě dnes.

## Často kladené otázky

{{% details title="Je Kodi zdarma jako DLNA server?" closed="true" %}}
Ano. Kodi je zcela zdarma a open-source. Běží na macOS, Windows, Linux a mnoha NAS zařízeních.
{{% /details %}}

{{% details title="Podporují Evermusic a Flacbox streamování FLAC přes DLNA?" closed="true" %}}
Ano. Flacbox je optimalizován pro hi-res formáty jako FLAC, ALAC a DSD. Evermusic také podporuje přehrávání FLAC spolu s MP3 a dalšími standardními formáty.
{{% /details %}}

{{% details title="Mohu poslouchat offline po streamování z Kodi?" closed="true" %}}
Ano. Povolte Offline režim na jakémkoli seznamu skladeb a aplikace stáhne všechny skladby do vašeho zařízení pro poslech bez síťového připojení.
{{% /details %}}

{{% details title="Potřebuji prémiové předplatné pro použití DLNA?" closed="true" %}}
Bezplatná verze podporuje až 3 cloudová nebo síťová připojení. Premium odstraňuje tento limit a umožňuje připojit neomezené služby a DLNA servery.
{{% /details %}}

{{% details title="Musí být můj iPhone na stejné Wi-Fi síti jako Kodi?" closed="true" %}}
Ano. DLNA streamování funguje přes vaši lokální síť. Server Kodi i vaše iOS zařízení musí být připojeny ke stejné Wi-Fi síti.
{{% /details %}}

{{% details title="Mohu toto nastavení použít s NAS místo Mac nebo PC?" closed="true" %}}
Ano. Mnoho NAS zařízení (Synology, QNAP atd.) podporuje Kodi nebo má vlastní vestavěný DLNA server. Evermusic a Flacbox se mohou připojit k jakémukoli standardnímu DLNA/UPnP serveru.
{{% /details %}}
