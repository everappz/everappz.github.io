---
title: "Sådan afspiller du din musik fra Mac / PC / Linux / NAS på iPhone med Kodi DLNA-server"
date: 2025-07-25
description: "Stream musik fra din computer eller NAS til din iPhone via Wi-Fi med Kodi DLNA og Evermusic-appen."
keywords: ["kodi dlna server", "stream musik til iphone", "afspil musik fra nas", "evermusic dlna", "mac til iphone musik", "windows til iphone musik", "kodi dlna iphone", "dlna audio streaming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "musikstreaming", "mac", "nas", "linux", "lokalt netværk"]
readingTime: 5
---

{{< author-byline >}}


**Resumé:** Installer Kodi på din Mac, PC, Linux eller NAS, aktiver dens DLNA/UPnP-server, og stream hele dit musikbibliotek til iPhone eller iPad med den gratis Evermusic- eller Flacbox-app via Wi-Fi. Ingen abonnementer nødvendige.

## Introduktion

Hvis du har en **Mac, Windows PC, Linux-maskine eller NAS-enhed**, kan du nemt forvandle den til en **personlig musikserver** derhjemme med [Kodi](https://kodi.tv/), en gratis og open source-medieplatform. Med Kodis indbyggede **DLNA/UPnP-server** kan du streame hele dit musikbibliotek til enhver DLNA-kompatibel klient — inklusive din iPhone eller iPad.

I denne guide viser vi dig trin for trin, hvordan du:

- Installerer Kodi på din Mac eller PC  
- Opsætter dine musikmapper til deling  
- Aktiverer DLNA-musikserveren  
- Tilgår musikken med **Evermusic**- eller **Flacbox**-appen til iOS

Denne opsætning er 100% gratis — ingen abonnementer, bare din egen musik streamet over dit Wi-Fi-netværk. Uanset om du prøver at organisere din store MP3-samling, lytte til FLAC over Wi-Fi, eller bare nyde din lokale musik uden at synkronisere via iTunes, er denne opsætning perfekt for dig.

## Download og installer Kodi på din Mac / PC / Linux / NAS

Først skal du besøge Kodis officielle hjemmeside:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodis hovedside" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klik på **Downloads** og rul ned for at finde versionen til din computer.
Vælg dit operativsystem. I dette eksempel bruger vi **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodi downloadside" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klik på **Intel (x86/64)** hvis du har en Intel Mac eller **Apple Silicon** til M1, M2, M3 Mac for at starte download.

{{< cards cols="1">}}
{{< card subtitle="Vælg macOS-installationsprogram" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Vent venligst et øjeblik mens installationsprogrammet downloades.

{{< cards cols="1">}}
{{< card subtitle="Kodi downloadet" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Når den er downloadet, find `.dmg`-filen i din **Downloads**-mappe.

{{< cards cols="1">}}
{{< card subtitle="Installer Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dobbeltklik på den downloadede fil for at starte installationsprogrammet.
Træk Kodi til din **Programmer**-mappe for at installere.

{{< cards cols="1">}}
{{< card title="" subtitle="Installer Kodi ved at trække den til Programmer" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Start Kodi. Du skal muligvis tillade den i **Systemindstillinger → Sikkerhed og privatliv → Åbn alligevel**.

{{< cards cols="1">}}
{{< card subtitle="Kodis hovedskærm" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Tilføj musik til Kodi-biblioteket

Klik på **tandhjulsikonet** (Indstillinger) fra startskærmen.

{{< cards cols="1">}}
{{< card subtitle="Kodi-indstillinger" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Naviger til **Medieindstillinger → Bibliotek**. Aktiver **Opdater bibliotek ved opstart** for videobibliotek og musikbibliotek til automatisk indeksering.

{{< cards cols="1">}}
{{< card subtitle="Biblioteksindstillinger" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Gå derefter til sektionen **Musik** og klik på **Tilføj musik**.

{{< cards cols="1">}}
{{< card subtitle="Tilføj musikmappe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Gennemse og vælg mappen, hvor din musik er gemt.

{{< cards cols="1">}}
{{< card subtitle="Vælg musikkilde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Tilføj musikkilde til Kodi.

{{< cards cols="1">}}
{{< card subtitle="Tilføj musikkilde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Bekræft og lad Kodi scanne dit musikbibliotek.

{{< cards cols="1">}}
{{< card subtitle="Bekræft musikkilder" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Vent et øjeblik mens dit bibliotek scannes og opbygges fuldstændigt.

{{< cards cols="1">}}
{{< card subtitle="Scanner musikbibliotek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Aktiver Kodis DLNA-server

Gå til **Indstillinger → Tjenester → UPnP/DLNA**.

Aktiver indstillingen: **Del mine biblioteker**.

Kodi fungerer nu som en DLNA-server på dit lokale Wi-Fi-netværk.

{{< cards cols="1">}}
{{< card subtitle="Aktiver DLNA i Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Åbn Kodi-bibliotek

Højreklik for at lukke indstillingsvinduet og åbne Kodis hovedbibliotek.

{{< cards cols="1">}}
{{< card title="" subtitle="Højreklik for at tilgå Kodi-biblioteket" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Download musikstreaming-app til iOS

Få en gratis iOS DLNA-klientapp, der lader dig streame musik fra en bred vifte af cloud-lagringstjenester og DLNA-servere.

- Brug **Evermusic** hvis din samling hovedsageligt er MP3 og andre standard lydformater.
- Vælg **Flacbox** hvis du har et hi-res musikbibliotek i formater som FLAC, ALAC eller DSD.

Begge apps er tilgængelige for **iOS** og **macOS**, og er gratis at bruge.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Download Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Download Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Tilføj DLNA-kilde

Når du har downloadet iOS-appen, åbn sektionen **Alle Forbindelser**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic-appens hovedmenu" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Rul ned og tryk på **Lokalt netværk - Tilgængelige enheder** for at opdage DLNA-servere.
I denne sektion kan du se alle tilgængelige enheder på dit lokale netværk. Din **Kodi DLNA-server** bør vises her. Tryk på Kodi-serveren for at oprette forbindelse.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilgængelige DLNA-enheder i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic viser biblioteksmapperne delt gennem Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi-musikbibliotek i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Naviger til mappen **Sange** for at se alle tilgængelige lydfiler på din DLNA-server.

{{< cards cols="1">}}
{{< card title="" subtitle="Sange oplistet fra fjernmappe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Tryk på en lydfil for at starte streaming med det samme.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3-fil afspilles i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Vend tilbage til sektionen **Forbindelser**. Den tilføjede DLNA-server vises nu her. Tryk på dens ikon for at genoprette forbindelsen når som helst. Du kan også forbinde andre cloud-tjenester fra denne skærm med de samme trin.

Du kan også aktivere **Last.fm-scrobbling** her. Afspilningsstatistikker gemmes på din Last.fm-konto og giver personlige musikanbefalinger senere.

{{< cards cols="1">}}
{{< card title="" subtitle="Forbindelser i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Opbyg musikbibliotek

Både **Evermusic** og **Flacbox** lader dig tilføje musik til dit bibliotek og organisere det efter **metadata-tags** som kunstnere, albums, genrer og komponister.

For at starte, åbn sektionen **Musikbibliotek**. Rul ned til **Værktøjer og præferencer** og tryk på **Tilføj musik**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic-musikbibliotek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Vælg musikkilden — i dette tilfælde vælg **Forbindelser**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilføj ny musik i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Find **Kodi DLNA-serveren** i Forbindelser og tryk for at se mapper og filer.

{{< cards cols="1">}}
{{< card title="" subtitle="Vælg DLNA-server til musikimport" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Vælg de mapper eller filer, du vil tilføje, og tryk på **Færdig**.

{{< cards cols="1">}}
{{< card title="" subtitle="Vælg musikmappe at tilføje" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Appen scanner dine valgte filer og organiserer dem ved hjælp af metadata i sektioner som Kunstnere, Albums, Genrer og Komponister.

{{< cards cols="1">}}
{{< card title="" subtitle="Musikbibliotek med kategorier" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Opret afspilningslister

Du kan også oprette dine egne afspilningslister.

Først skal du åbne fanen **Afspilningslister**.

{{< cards cols="1">}}
{{< card title="" subtitle="Fanen Afspilningslister i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Tryk på **plus (+)**-knappen og vælg **Ny afspilningsliste**.

{{< cards cols="1">}}
{{< card title="" subtitle="Opret en ny afspilningsliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Indtast et navn til din afspilningsliste og tryk på **Gem**.

{{< cards cols="1">}}
{{< card title="" subtitle="Indtast afspilningslistenavn" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Vælg derefter en kilde at tilføje sange fra — her vælger vi **Biblioteket**.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilføj sange til ny afspilningsliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Vælg de sange, du ønsker, og tryk på **Færdig** for at tilføje dem.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilføj musik fra bibliotek til afspilningsliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Dine valgte numre vises nu i den oprettede afspilningsliste.

{{< cards cols="1">}}
{{< card title="" subtitle="Oprettet afspilningsliste vist i listen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Som standard er sange tilgængelige for streaming. For at lytte offline, aktiver **Offline-tilstand** — appen downloader alle afspilningslistens numre.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline-tilstand aktiveret for afspilningsliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Tryk på knappen **Flere handlinger** for at udforske yderligere muligheder. Du kan:

- Arkivere afspilningslisten  
- Ændre albumcoveret  
- Omarrangere numre  
- Og flere nyttige funktioner

{{< cards cols="1">}}
{{< card title="" subtitle="Flere afspilningslistehandlinger tilgængelige" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Konklusion

Med **Evermusic** og **Flacbox** er det nemt at forvandle din iPhone, iPad eller Mac til en kraftfuld DLNA-musikafspiller. Uanset om du gemmer din musik i skyen, på en NAS eller på en hjemmemedieserver som **Kodi**, lader disse apps dig streame, organisere og nyde din samling uden begrænsninger.

- Stream MP3 eller hi-res FLAC direkte fra din **Kodi DLNA-server**  
- Opbyg et personligt musikbibliotek grupperet efter metadata (albums, genrer, komponister)  
- Opret og administrer **brugerdefinerede afspilningslister**  
- Aktiver **offline-tilstand** til lytning på farten  
- Forbind til **flere cloud-tjenester** og **lokale netværksenheder**  
- Spor dine lyttevaner med **Last.fm-integration**

Uanset om du er en audiofile eller en afslappet lytter, tilbyder Evermusic og Flacbox alt, hvad du har brug for til problemfri musikstreaming og organisering.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Download Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Download Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Begynd at opbygge din personlige musikoplevelse i dag.

## FAQ

{{% details title="Er Kodi gratis at bruge som DLNA-server?" closed="true" %}}
Ja. Kodi er helt gratis og open source. Det kører på macOS, Windows, Linux og mange NAS-enheder.
{{% /details %}}

{{% details title="Understøtter Evermusic og Flacbox FLAC-streaming over DLNA?" closed="true" %}}
Ja. Flacbox er optimeret til hi-res formater som FLAC, ALAC og DSD. Evermusic understøtter også FLAC-afspilning sammen med MP3 og andre standardformater.
{{% /details %}}

{{% details title="Kan jeg lytte offline efter streaming fra Kodi?" closed="true" %}}
Ja. Aktiver Offline-tilstand på enhver afspilningsliste, og appen downloader alle numre til din enhed til lytning uden netværksforbindelse.
{{% /details %}}

{{% details title="Har jeg brug for et premium-abonnement for at bruge DLNA?" closed="true" %}}
Den gratis version understøtter op til 3 cloud- eller netværksforbindelser. Premium fjerner denne grænse og lader dig forbinde ubegrænsede tjenester og DLNA-servere.
{{% /details %}}

{{% details title="Skal min iPhone være på det samme Wi-Fi-netværk som Kodi?" closed="true" %}}
Ja. DLNA-streaming fungerer over dit lokale netværk. Både Kodi-serveren og din iOS-enhed skal være forbundet til det samme Wi-Fi-netværk.
{{% /details %}}

{{% details title="Kan jeg bruge denne opsætning med en NAS i stedet for en Mac eller PC?" closed="true" %}}
Ja. Mange NAS-enheder (Synology, QNAP osv.) understøtter Kodi eller har deres egen indbyggede DLNA-server. Evermusic og Flacbox kan forbinde til enhver standard DLNA/UPnP-server.
{{% /details %}}
