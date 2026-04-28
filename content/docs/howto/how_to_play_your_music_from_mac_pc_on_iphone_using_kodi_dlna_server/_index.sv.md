---
title: "Hur du spelar din musik från Mac / PC / Linux / NAS på iPhone med Kodi DLNA-server"
date: 2025-07-25
description: "Strömma musik från din dator eller NAS till din iPhone via Wi-Fi med Kodi DLNA och Evermusic-appen."
keywords: ["kodi dlna server", "strömma musik till iphone", "spela musik från nas", "evermusic dlna", "mac till iphone musik", "windows till iphone musik", "kodi dlna iphone", "dlna ljudströmning"]
tags: ["dlna", "kodi", "evermusic", "iphone", "musikströmning", "mac", "nas", "linux", "lokalt nätverk"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Installera Kodi på din Mac, PC, Linux eller NAS, aktivera dess DLNA/UPnP-server och strömma hela ditt musikbibliotek till iPhone eller iPad med den kostnadsfria Evermusic- eller Flacbox-appen via Wi-Fi. Inga prenumerationer krävs.

## Introduktion

Om du har en **Mac, Windows PC, Linux-maskin eller NAS-enhet** kan du enkelt förvandla den till en **personlig musikserver** hemma med [Kodi](https://kodi.tv/), en gratis och öppen mediaplattform. Med Kodis inbyggda **DLNA/UPnP-server** kan du strömma hela ditt musikbibliotek till alla DLNA-kompatibla klienter — inklusive din iPhone eller iPad.

I denna guide visar vi dig steg för steg hur du:

- Installerar Kodi på din Mac eller PC
- Ställer in dina musikmappar för delning
- Aktiverar DLNA-musikservern
- Kommer åt musiken med **Evermusic**- eller **Flacbox**-appen för iOS

Denna installation är 100% gratis — inga prenumerationer, bara din egen musik strömmad via ditt Wi-Fi-nätverk. Oavsett om du försöker organisera din stora MP3-samling, lyssna på FLAC via Wi-Fi, eller bara njuta av din lokala musik utan att synkronisera via iTunes, är denna installation perfekt för dig.

## Ladda ner och installera Kodi på din Mac / PC / Linux / NAS

Besök först Kodis officiella webbplats:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodis huvudsida" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klicka på **Nedladdningar** och scrolla för att hitta versionen för din dator.
Välj ditt operativsystem. I detta exempel använder vi **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodis nedladdningssida" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klicka på **Intel (x86/64)** om du har en Intel Mac eller **Apple Silicon** för M1, M2, M3 Mac för att starta nedladdningen.

{{< cards cols="1">}}
{{< card subtitle="Välj macOS-installationsprogram" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Vänta en stund medan installationsprogrammet laddas ner.

{{< cards cols="1">}}
{{< card subtitle="Kodi nedladdad" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

När nedladdningen är klar, hitta `.dmg`-filen i din **Nedladdningar**-mapp.

{{< cards cols="1">}}
{{< card subtitle="Installera Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dubbelklicka på den nedladdade filen för att starta installationsprogrammet.
Dra Kodi till din **Program**-mapp för att installera.

{{< cards cols="1">}}
{{< card title="" subtitle="Installera Kodi genom att dra till Program" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Starta Kodi. Du kan behöva tillåta den i **Systeminställningar → Säkerhet och integritet → Öppna ändå**.

{{< cards cols="1">}}
{{< card subtitle="Kodis huvudskärm" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Lägg till musik i Kodi-biblioteket

Klicka på **kugghjulsikonen** (Inställningar) från startskärmen.

{{< cards cols="1">}}
{{< card subtitle="Kodi-inställningar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navigera till **Mediainställningar → Bibliotek**. Aktivera **Uppdatera bibliotek vid start** för video- och musikbiblioteket för automatisk indexering.

{{< cards cols="1">}}
{{< card subtitle="Biblioteksinställningar" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Gå sedan till sektionen **Musik** och klicka **Lägg till musik**.

{{< cards cols="1">}}
{{< card subtitle="Lägg till musikmapp" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Bläddra och välj mappen där din musik lagras.

{{< cards cols="1">}}
{{< card subtitle="Välj musikkälla" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Lägg till musikkällan till Kodi.

{{< cards cols="1">}}
{{< card subtitle="Lägg till musikkälla" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Bekräfta och låt Kodi skanna ditt musikbibliotek.

{{< cards cols="1">}}
{{< card subtitle="Bekräfta musikkällor" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Vänta en stund medan ditt bibliotek skannas och byggs upp helt.

{{< cards cols="1">}}
{{< card subtitle="Skannar musikbiblioteket" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Aktivera Kodis DLNA-server

Gå till **Inställningar → Tjänster → UPnP/DLNA**.

Aktivera alternativet: **Dela mina bibliotek**.

Kodi fungerar nu som en DLNA-server på ditt lokala Wi-Fi-nätverk.

{{< cards cols="1">}}
{{< card subtitle="Aktivera DLNA i Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Öppna Kodi-bibliotek

Högerklicka för att stänga inställningsfönstret och öppna Kodis huvudbibliotek.

{{< cards cols="1">}}
{{< card title="" subtitle="Högerklicka för att komma åt Kodi-biblioteket" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Ladda ner musikströmmningsapp för iOS

Skaffa en gratis iOS DLNA-klientapp som låter dig strömma musik från ett brett utbud av molnlagringstjänster och DLNA-servrar.

- Använd **Evermusic** om din samling huvudsakligen är MP3 och andra standardljudformat.
- Välj **Flacbox** om du har ett hi-res musikbibliotek i format som FLAC, ALAC eller DSD.

Båda apparna finns tillgängliga för **iOS** och **macOS**, och är gratis att använda.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Ladda ner Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Ladda ner Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Lägg till DLNA-källa

När du har laddat ner iOS-appen, öppna sektionen **Alla Anslutningar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic-appens huvudsidofält" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Scrolla ner och tryck på **Lokalt nätverk - Tillgängliga enheter** för att upptäcka DLNA-servrar.
I denna sektion ser du alla tillgängliga enheter på ditt lokala nätverk. Din **Kodi DLNA-server** bör visas här. Tryck på Kodi-servern för att ansluta.

{{< cards cols="1">}}
{{< card title="" subtitle="Tillgängliga DLNA-enheter i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic visar biblioteksmapparna som delas via Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi musikbibliotek i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navigera till mappen **Låtar** för att se alla tillgängliga ljudfiler på din DLNA-server.

{{< cards cols="1">}}
{{< card title="" subtitle="Låtar från fjärrmapp" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Tryck på valfri ljudfil för att börja strömma direkt.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3-fil spelas i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Gå tillbaka till sektionen **Anslutningar**. Den tillagda DLNA-servern visas nu här. Tryck på dess ikon för att återansluta när som helst.

Du kan också aktivera **Last.fm-scrobbling** här. Uppspelningsstatistik sparas på ditt Last.fm-konto och ger personliga musikrekommendationer senare.

{{< cards cols="1">}}
{{< card title="" subtitle="Anslutningar i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Bygg musikbibliotek

Både **Evermusic** och **Flacbox** låter dig lägga till musik i ditt bibliotek och organisera det efter **metadatataggar** som artister, album, genrer och kompositörer.

För att börja, öppna sektionen **Musikbibliotek**. Scrolla ner till **Verktyg och inställningar** och tryck **Lägg till musik**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic musikbibliotek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Välj musikkällan — i detta fall välj **Anslutningar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Lägg till ny musik i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Hitta **Kodi DLNA-servern** i Anslutningar och tryck för att se mappar och filer.

{{< cards cols="1">}}
{{< card title="" subtitle="Välj DLNA-server för musikimport" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Välj mapparna eller filerna du vill lägga till och tryck **Färdig**.

{{< cards cols="1">}}
{{< card title="" subtitle="Välj musikmapp att lägga till" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Appen skannar dina valda filer och organiserar dem med metadata i sektioner som Artister, Album, Genrer och Kompositörer.

{{< cards cols="1">}}
{{< card title="" subtitle="Musikbibliotek med kategorier" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Skapa spellistor

Du kan också skapa egna spellistor.

Öppna först fliken **Spellistor**.

{{< cards cols="1">}}
{{< card title="" subtitle="Fliken Spellistor i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Tryck på **plus (+)**-knappen och välj **Ny spellista**.

{{< cards cols="1">}}
{{< card title="" subtitle="Skapa en ny spellista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Ange ett namn för din spellista och tryck **Spara**.

{{< cards cols="1">}}
{{< card title="" subtitle="Ange spellistans namn" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Välj sedan en källa att lägga till låtar från — här väljer vi **Biblioteket**.

{{< cards cols="1">}}
{{< card title="" subtitle="Lägg till låtar i ny spellista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Välj de låtar du vill ha och tryck **Färdig** för att lägga till dem.

{{< cards cols="1">}}
{{< card title="" subtitle="Lägg till musik från biblioteket till spellistan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Dina valda spår visas nu i den skapade spellistan.

{{< cards cols="1">}}
{{< card title="" subtitle="Skapad spellista visad i listan" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Som standard är låtar tillgängliga för strömning. För att lyssna offline, aktivera **Offline-läge** — appen laddar ner alla spellistspår.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline-läge aktiverat för spellista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Tryck på knappen **Fler åtgärder** för att utforska ytterligare alternativ. Du kan:

- Arkivera spellistan
- Ändra albumomslaget
- Ordna om spår
- Och fler användbara funktioner

{{< cards cols="1">}}
{{< card title="" subtitle="Fler spelliståtgärder tillgängliga" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Slutsats

Med **Evermusic** och **Flacbox** är det enkelt att förvandla din iPhone, iPad eller Mac till en kraftfull DLNA-musikspelare.

- Strömma MP3 eller hi-res FLAC direkt från din **Kodi DLNA-server**
- Bygg ett personligt musikbibliotek grupperat efter metadata (album, genrer, kompositörer)
- Skapa och hantera **anpassade spellistor**
- Aktivera **offline-läge** för att lyssna på språng
- Anslut till **flera molntjänster** och **lokala nätverksenheter**
- Spåra dina lyssningsvanor med **Last.fm-integration**

Oavsett om du är en audiofil eller en casual lyssnare, erbjuder Evermusic och Flacbox allt du behöver för sömlös musikströmning och organisation.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Ladda ner Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Ladda ner Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Börja bygga din personliga musikupplevelse idag.

## Vanliga frågor

{{% details title="Är Kodi gratis som DLNA-server?" closed="true" %}}
Ja. Kodi är helt gratis och öppen källkod. Den körs på macOS, Windows, Linux och många NAS-enheter.
{{% /details %}}

{{% details title="Stöder Evermusic och Flacbox FLAC-strömning via DLNA?" closed="true" %}}
Ja. Flacbox är optimerad för hi-res format som FLAC, ALAC och DSD. Evermusic stöder också FLAC-uppspelning tillsammans med MP3 och andra standardformat.
{{% /details %}}

{{% details title="Kan jag lyssna offline efter strömning från Kodi?" closed="true" %}}
Ja. Aktivera Offline-läge på valfri spellista, och appen laddar ner alla spår till din enhet.
{{% /details %}}

{{% details title="Behöver jag en premiumprenumeration för att använda DLNA?" closed="true" %}}
Den kostnadsfria versionen stöder upp till 3 moln- eller nätverksanslutningar. Premium tar bort denna gräns.
{{% /details %}}

{{% details title="Måste min iPhone vara på samma Wi-Fi-nätverk som Kodi?" closed="true" %}}
Ja. DLNA-strömning fungerar via ditt lokala nätverk. Både Kodi-servern och din iOS-enhet måste vara anslutna till samma Wi-Fi-nätverk.
{{% /details %}}

{{% details title="Kan jag använda denna installation med en NAS istället för en Mac eller PC?" closed="true" %}}
Ja. Många NAS-enheter (Synology, QNAP etc.) stöder Kodi eller har sin egen inbyggda DLNA-server. Evermusic och Flacbox kan ansluta till valfri standard DLNA/UPnP-server.
{{% /details %}}
