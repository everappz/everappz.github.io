---
title: "Ako prehrávať hudbu z Mac / PC / Linux / NAS na iPhone pomocou servera Kodi DLNA"
date: 2025-07-25
description: "Streamujte hudbu z počítača alebo NAS do iPhone cez Wi-Fi pomocou Kodi DLNA a aplikácie Evermusic."
keywords: ["kodi dlna server", "streamovanie hudby na iphone", "prehrávanie hudby z nas", "evermusic dlna", "hudba z mac na iphone", "hudba z windows na iphone", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streamovanie hudby", "mac", "nas", "linux", "lokálna sieť"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Nainštalujte Kodi na Mac, PC, Linux alebo NAS, povoľte server DLNA/UPnP a streamujte celú hudobnú knižnicu na iPhone alebo iPad pomocou bezplatnej aplikácie Evermusic alebo Flacbox cez Wi-Fi. Žiadne predplatné.

## Úvod

Ak máte **Mac, PC s Windows, Linux alebo NAS zariadenie**, môžete ho jednoducho premeniť na **osobný hudobný server** doma pomocou [Kodi](https://kodi.tv/), bezplatnej a open-source mediálnej platformy. So vstavaným serverom **DLNA/UPnP** Kodi môžete streamovať celú hudobnú knižnicu na akéhokoľvek klienta kompatibilného s DLNA — vrátane vášho iPhone alebo iPad.

V tomto sprievodcovi vám ukážeme krok za krokom, ako:

- Nainštalovať Kodi na Mac alebo PC
- Nastaviť hudobné priečinky na zdieľanie
- Povoliť hudobný server DLNA
- Pristupovať k hudbe pomocou aplikácie **Evermusic** alebo **Flacbox** pre iOS

Toto nastavenie je 100% zadarmo — žiadne predplatné, len vaša vlastná hudba streamovaná cez Wi-Fi sieť.

## Stiahnite a nainštalujte Kodi na Mac / PC / Linux / NAS

Najprv navštívte oficiálnu webovú stránku Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Hlavná stránka Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Kliknite na **Stiahnuť** a prejdite nadol, aby ste našli verziu pre váš počítač.
Vyberte si operačný systém. V tomto príklade použijeme **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Stránka stiahnutí Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Kliknite na **Intel (x86/64)**, ak máte Intel Mac, alebo **Apple Silicon** pre M1, M2, M3 Mac na spustenie sťahovania.

{{< cards cols="1">}}
{{< card subtitle="Vyberte inštalačný program macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Počkajte chvíľu, kým sa inštalačný program stiahne.

{{< cards cols="1">}}
{{< card subtitle="Kodi stiahnuté" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Po stiahnutí nájdite súbor `.dmg` v priečinku **Stiahnuté**.

{{< cards cols="1">}}
{{< card subtitle="Inštalácia Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dvakrát kliknite na stiahnutý súbor na spustenie inštalátora.
Presuňte Kodi do priečinka **Aplikácie** na inštaláciu.

{{< cards cols="1">}}
{{< card title="" subtitle="Nainštalujte Kodi presunutím do Aplikácií" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Spustite Kodi. Možno ho budete musieť povoliť v **Systémové nastavenia → Bezpečnosť a súkromie → Otvoriť napriek tomu**.

{{< cards cols="1">}}
{{< card subtitle="Hlavná obrazovka Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Pridajte hudbu do knižnice Kodi

Kliknite na **ikonu ozubeného kolesa** (Nastavenia) z domovskej obrazovky.

{{< cards cols="1">}}
{{< card subtitle="Nastavenia Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Prejdite na **Nastavenia médií → Knižnica**. Povoľte **Aktualizovať knižnicu pri spustení** pre video a hudobnú knižnicu na automatickú indexáciu.

{{< cards cols="1">}}
{{< card subtitle="Nastavenia knižnice" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Potom prejdite do sekcie **Hudba** a kliknite **Pridať hudbu**.

{{< cards cols="1">}}
{{< card subtitle="Pridať hudobný priečinok" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Prehľadajte a vyberte priečinok, kde je uložená vaša hudba.

{{< cards cols="1">}}
{{< card subtitle="Vyberte zdroj hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Pridajte zdroj hudby do Kodi.

{{< cards cols="1">}}
{{< card subtitle="Pridať zdroj hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Potvrďte a nechajte Kodi prehľadať hudobnú knižnicu.

{{< cards cols="1">}}
{{< card subtitle="Potvrďte zdroje hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Počkajte chvíľu, kým sa knižnica prehľadá a úplne vytvorí.

{{< cards cols="1">}}
{{< card subtitle="Prehľadávanie hudobnej knižnice" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Povoľte server DLNA Kodi

Prejdite na **Nastavenia → Služby → UPnP/DLNA**.

Povoľte možnosť: **Zdieľať moje knižnice**.

Kodi teraz funguje ako DLNA server vo vašej lokálnej Wi-Fi sieti.

{{< cards cols="1">}}
{{< card subtitle="Povolenie DLNA v Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Otvorte knižnicu Kodi

Kliknite pravým tlačidlom na zatvorenie okna nastavení a otvorenie hlavnej knižnice Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Pravý klik na prístup ku knižnici Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Stiahnite aplikáciu na streamovanie hudby pre iOS

Získajte bezplatnú iOS DLNA klientsku aplikáciu, ktorá vám umožní streamovať hudbu z rôznych cloudových úložísk a DLNA serverov.

- Použite **Evermusic**, ak je vaša zbierka prevažne MP3 a iné štandardné audio formáty.
- Zvoľte **Flacbox**, ak máte hi-res hudobnú knižnicu vo formátoch ako FLAC, ALAC alebo DSD.

Obe aplikácie sú dostupné pre **iOS** a **macOS** a sú zadarmo.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Stiahnuť Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Stiahnuť Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Pridajte zdroj DLNA

Po stiahnutí iOS aplikácie otvorte sekciu **Všetky Pripojenia**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hlavný bočný panel aplikácie Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Prejdite nadol a ťuknite na **Lokálna sieť - Dostupné zariadenia** na objavenie DLNA serverov.
V tejto sekcii uvidíte všetky dostupné zariadenia vo vašej lokálnej sieti. Váš **Kodi DLNA server** by sa tu mal objaviť. Ťuknite na server Kodi na pripojenie.

{{< cards cols="1">}}
{{< card title="" subtitle="Dostupné DLNA zariadenia v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic zobrazí priečinky knižnice zdieľané cez Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudobná knižnica Kodi v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Prejdite do priečinka **Skladby** na zobrazenie všetkých dostupných audio súborov na DLNA serveri.

{{< cards cols="1">}}
{{< card title="" subtitle="Skladby zo vzdialeného priečinka" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Ťuknite na akýkoľvek audio súbor na okamžité spustenie streamovania.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3 súbor sa prehráva v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Vráťte sa do sekcie **Pripojenia**. Pridaný DLNA server sa tu teraz zobrazí. Ťuknite na jeho ikonu na opätovné pripojenie kedykoľvek.

Tu môžete tiež povoliť **sledovanie Last.fm**. Štatistiky prehrávania sa uložia do vášho účtu Last.fm a poskytnú personalizované hudobné odporúčania neskôr.

{{< cards cols="1">}}
{{< card title="" subtitle="Pripojenia v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Vytvorte hudobnú knižnicu

**Evermusic** aj **Flacbox** vám umožňujú pridať hudbu do knižnice a organizovať ju podľa **metadátových značiek** ako interpreti, albumy, žánre a skladatelia.

Na začiatok otvorte sekciu **Hudobná knižnica**. Prejdite nadol k **Nástroje a nastavenia** a ťuknite na **Pridať hudbu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudobná knižnica Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Vyberte zdroj hudby — v tomto prípade zvoľte **Pripojenia**.

{{< cards cols="1">}}
{{< card title="" subtitle="Pridať novú hudbu v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Nájdite **Kodi DLNA server** v Pripojeniach a ťuknite na zobrazenie priečinkov a súborov.

{{< cards cols="1">}}
{{< card title="" subtitle="Vyberte DLNA server na import hudby" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Vyberte priečinky alebo súbory, ktoré chcete pridať, a ťuknite na **Hotovo**.

{{< cards cols="1">}}
{{< card title="" subtitle="Vyberte hudobný priečinok na pridanie" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplikácia prehľadá vybrané súbory a usporiada ich pomocou metadát do sekcií ako Interpreti, Albumy, Žánre a Skladatelia.

{{< cards cols="1">}}
{{< card title="" subtitle="Hudobná knižnica s kategóriami" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Vytvorenie zoznamov skladieb

Môžete si tiež vytvoriť vlastné zoznamy skladieb.

Najprv otvorte kartu **Prehrávače**.

{{< cards cols="1">}}
{{< card title="" subtitle="Karta zoznamov skladieb v Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Ťuknite na tlačidlo **plus (+)** a zvoľte **Nový zoznam skladieb**.

{{< cards cols="1">}}
{{< card title="" subtitle="Vytvoriť nový zoznam skladieb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Zadajte názov zoznamu skladieb a ťuknite na **Uložiť**.

{{< cards cols="1">}}
{{< card title="" subtitle="Zadajte názov zoznamu skladieb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Ďalej zvoľte zdroj na pridanie skladieb — tu vyberáme **Knižnicu**.

{{< cards cols="1">}}
{{< card title="" subtitle="Pridať skladby do nového zoznamu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Vyberte požadované skladby a ťuknite na **Hotovo** na ich pridanie.

{{< cards cols="1">}}
{{< card title="" subtitle="Pridať hudbu z knižnice do zoznamu skladieb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Vybrané skladby sa teraz zobrazia vo vytvorenom zozname skladieb.

{{< cards cols="1">}}
{{< card title="" subtitle="Vytvorený zoznam skladieb zobrazený v zozname" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

V predvolenom nastavení sú skladby dostupné na streamovanie. Na počúvanie offline povoľte **Offline režim** — aplikácia stiahne všetky skladby zoznamu.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline režim povolený pre zoznam skladieb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Ťuknite na tlačidlo **Viac akcií** na preskúmanie ďalších možností. Môžete:

- Archivovať zoznam skladieb
- Zmeniť obal albumu
- Preusporiadať skladby
- A ďalšie užitočné funkcie

{{< cards cols="1">}}
{{< card title="" subtitle="Ďalšie akcie zoznamu skladieb" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Záver

S **Evermusic** a **Flacbox** je premena vášho iPhone, iPad alebo Mac na výkonný DLNA hudobný prehrávač jednoduchá.

- Streamujte MP3 alebo hi-res FLAC priamo z vášho **Kodi DLNA servera**
- Vytvorte si osobnú hudobnú knižnicu zoskupenú podľa metadát (albumy, žánre, skladatelia)
- Vytvárajte a spravujte **vlastné zoznamy skladieb**
- Povoľte **offline režim** na počúvanie na cestách
- Pripojte sa k **viacerým cloudovým službám** a **zariadeniam lokálnej siete**
- Sledujte svoje počúvacie návyky s **integráciou Last.fm**

Či ste audiofil alebo príležitostný poslucháč, Evermusic a Flacbox ponúkajú všetko pre bezproblémové streamovanie a organizáciu hudby.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Stiahnuť Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Stiahnuť Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Začnite budovať svoj osobný hudobný zážitok ešte dnes.

## Často kladené otázky

{{% details title="Je Kodi zadarmo ako DLNA server?" closed="true" %}}
Áno. Kodi je úplne zadarmo a open-source. Beží na macOS, Windows, Linux a mnohých NAS zariadeniach.
{{% /details %}}

{{% details title="Podporujú Evermusic a Flacbox streamovanie FLAC cez DLNA?" closed="true" %}}
Áno. Flacbox je optimalizovaný pre hi-res formáty ako FLAC, ALAC a DSD. Evermusic tiež podporuje prehrávanie FLAC spolu s MP3 a inými štandardnými formátmi.
{{% /details %}}

{{% details title="Môžem počúvať offline po streamovaní z Kodi?" closed="true" %}}
Áno. Povoľte Offline režim na ľubovoľnom zozname skladieb a aplikácia stiahne všetky skladby na vaše zariadenie.
{{% /details %}}

{{% details title="Potrebujem prémiové predplatné na používanie DLNA?" closed="true" %}}
Bezplatná verzia podporuje až 3 cloudové alebo sieťové pripojenia. Premium odstraňuje tento limit.
{{% /details %}}

{{% details title="Musí byť môj iPhone na rovnakej Wi-Fi sieti ako Kodi?" closed="true" %}}
Áno. DLNA streamovanie funguje cez vašu lokálnu sieť. Server Kodi aj vaše iOS zariadenie musia byť pripojené k rovnakej Wi-Fi sieti.
{{% /details %}}

{{% details title="Môžem toto nastavenie použiť s NAS namiesto Mac alebo PC?" closed="true" %}}
Áno. Mnohé NAS zariadenia (Synology, QNAP atď.) podporujú Kodi alebo majú vlastný vstavaný DLNA server. Evermusic a Flacbox sa môžu pripojiť k akémukoľvek štandardnému DLNA/UPnP serveru.
{{% /details %}}
