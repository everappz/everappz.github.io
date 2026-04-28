---
title: "Slik spiller du musikk fra Mac / PC / Linux / NAS på iPhone med Kodi DLNA-server"
date: 2025-07-25
description: "Strøm musikk fra datamaskinen eller NAS til iPhone via Wi-Fi med Kodi DLNA og Evermusic-appen."
keywords: ["kodi dlna server", "strøm musikk til iphone", "spill musikk fra nas", "evermusic dlna", "mac til iphone musikk", "windows til iphone musikk", "kodi dlna iphone", "dlna lydstrømming"]
tags: ["dlna", "kodi", "evermusic", "iphone", "musikkstrømming", "mac", "nas", "linux", "lokalt nettverk"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Installer Kodi på din Mac, PC, Linux eller NAS, aktiver DLNA/UPnP-serveren og strøm hele musikkbiblioteket til iPhone eller iPad med den gratis Evermusic- eller Flacbox-appen via Wi-Fi. Ingen abonnementer nødvendig.

## Introduksjon

Hvis du har en **Mac, Windows PC, Linux-maskin eller NAS-enhet**, kan du enkelt gjøre den om til en **personlig musikkserver** hjemme med [Kodi](https://kodi.tv/), en gratis og åpen kildekode-medieplattform. Med Kodis innebygde **DLNA/UPnP-server** kan du strømme hele musikkbiblioteket til enhver DLNA-kompatibel klient — inkludert iPhone eller iPad.

I denne guiden viser vi deg trinn for trinn hvordan du:

- Installerer Kodi på Mac eller PC
- Setter opp musikkmappene for deling
- Aktiverer DLNA-musikkserveren
- Får tilgang til musikken med **Evermusic**- eller **Flacbox**-appen for iOS

Dette oppsettet er 100% gratis — ingen abonnementer, bare din egen musikk strømmet over Wi-Fi-nettverket. Enten du prøver å organisere en stor MP3-samling, lytte til FLAC over Wi-Fi, eller bare nyte lokal musikk uten synkronisering via iTunes, er dette oppsettet perfekt for deg.

## Last ned og installer Kodi på Mac / PC / Linux / NAS

Først, besøk Kodis offisielle nettsted:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Kodi hovedside" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Klikk på **Nedlastinger** og bla for å finne versjonen for datamaskinen din.
Velg operativsystemet ditt. I dette eksempelet bruker vi **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Kodi nedlastingsside" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Klikk **Intel (x86/64)** hvis du har en Intel Mac eller **Apple Silicon** for M1, M2, M3 Mac for å starte nedlastingen.

{{< cards cols="1">}}
{{< card subtitle="Velg macOS-installasjonsprogram" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Vennligst vent et øyeblikk mens installasjonsprogrammet lastes ned.

{{< cards cols="1">}}
{{< card subtitle="Kodi lastet ned" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Etter nedlasting, finn `.dmg`-filen i **Nedlastinger**-mappen.

{{< cards cols="1">}}
{{< card subtitle="Installer Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dobbeltklikk på den nedlastede filen for å starte installasjonsprogrammet.
Dra Kodi til **Programmer**-mappen for å installere.

{{< cards cols="1">}}
{{< card title="" subtitle="Installer Kodi ved å dra den til Programmer" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Start Kodi. Du må kanskje tillate den i **Systeminnstillinger → Sikkerhet og personvern → Åpne likevel**.

{{< cards cols="1">}}
{{< card subtitle="Kodi hovedskjerm" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Legg til musikk i Kodi-biblioteket

Klikk på **tannhjulikonet** (Innstillinger) fra startskjermen.

{{< cards cols="1">}}
{{< card subtitle="Kodi-innstillinger" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Naviger til **Medieinnstillinger → Bibliotek**. Aktiver **Oppdater bibliotek ved oppstart** for video- og musikkbiblioteket for automatisk indeksering.

{{< cards cols="1">}}
{{< card subtitle="Bibliotekinnstillinger" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Gå deretter til **Musikk**-seksjonen og klikk **Legg til musikk**.

{{< cards cols="1">}}
{{< card subtitle="Legg til musikkmappe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Bla og velg mappen der musikken din er lagret.

{{< cards cols="1">}}
{{< card subtitle="Velg musikkilde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Legg til musikkilde i Kodi.

{{< cards cols="1">}}
{{< card subtitle="Legg til musikkilde" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Bekreft og la Kodi skanne musikkbiblioteket.

{{< cards cols="1">}}
{{< card subtitle="Bekreft musikkkilder" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Vent et øyeblikk mens biblioteket skannes og bygges fullt ut.

{{< cards cols="1">}}
{{< card subtitle="Skanner musikkbiblioteket" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Aktiver Kodis DLNA-server

Gå til **Innstillinger → Tjenester → UPnP/DLNA**.

Aktiver alternativet: **Del mine biblioteker**.

Kodi fungerer nå som en DLNA-server på ditt lokale Wi-Fi-nettverk.

{{< cards cols="1">}}
{{< card subtitle="Aktiver DLNA i Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Åpne Kodi-bibliotek

Høyreklikk for å lukke innstillingsvinduet og åpne Kodi-hovedbiblioteket.

{{< cards cols="1">}}
{{< card title="" subtitle="Høyreklikk for å få tilgang til Kodi-biblioteket" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Last ned musikkstrømming-app for iOS

Få en gratis iOS DLNA-klientapp som lar deg strømme musikk fra et bredt spekter av skylagringstjenester og DLNA-servere.

- Bruk **Evermusic** hvis samlingen din hovedsakelig er MP3 og andre standard lydformater.
- Velg **Flacbox** hvis du har et hi-res musikkbibliotek i formater som FLAC, ALAC eller DSD.

Begge appene er tilgjengelige for **iOS** og **macOS**, og er gratis å bruke.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Last ned Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Last ned Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Legg til DLNA-kilde

Etter at du har lastet ned iOS-appen, åpne seksjonen **Alle Tilkoblinger**.

{{< cards cols="1">}}
{{< card title="" subtitle="Hovedsidefelt i Evermusic-appen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Bla ned og trykk på **Lokalt nettverk - Tilgjengelige enheter** for å oppdage DLNA-servere.
I denne seksjonen vil du se alle tilgjengelige enheter på det lokale nettverket. Din **Kodi DLNA-server** bør vises her. Trykk på Kodi-serveren for å koble til.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilgjengelige DLNA-enheter i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic viser bibliotekmappene som deles gjennom Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Kodi musikkbibliotek i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Naviger til **Sanger**-mappen for å se alle tilgjengelige lydfiler på DLNA-serveren.

{{< cards cols="1">}}
{{< card title="" subtitle="Sanger fra ekstern mappe" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Trykk på en lydfil for å starte strømming umiddelbart.

{{< cards cols="1">}}
{{< card title="" subtitle="MP3-fil spilles i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Gå tilbake til **Tilkoblinger**-seksjonen. Den tilføyde DLNA-serveren vises nå her. Trykk på ikonet for å koble til igjen når som helst. Du kan også koble til andre skytjenester fra denne skjermen med de samme trinnene.

Du kan også aktivere **Last.fm-scrobbling** her. Avspillingsstatistikk lagres i Last.fm-kontoen din og gir personlige musikkanbefaling senere.

{{< cards cols="1">}}
{{< card title="" subtitle="Tilkoblinger i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Bygg musikkbibliotek

Både **Evermusic** og **Flacbox** lar deg legge til musikk i biblioteket og organisere det etter **metadata-tagger** som artister, album, sjangre og komponister.

For å starte, åpne **Musikkbibliotek**-seksjonen. Bla ned til **Verktøy og innstillinger** og trykk **Legg til musikk**.

{{< cards cols="1">}}
{{< card title="" subtitle="Evermusic musikkbibliotek" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Velg musikkilden — i dette tilfellet velger du **Tilkoblinger**.

{{< cards cols="1">}}
{{< card title="" subtitle="Legg til ny musikk i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Finn **Kodi DLNA-serveren** i Tilkoblinger og trykk for å se mapper og filer.

{{< cards cols="1">}}
{{< card title="" subtitle="Velg DLNA-server for musikkimport" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Velg mappene eller filene du vil legge til og trykk **Ferdig**.

{{< cards cols="1">}}
{{< card title="" subtitle="Velg musikkmappe å legge til" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Appen skanner de valgte filene og organiserer dem ved hjelp av metadata i seksjoner som Artister, Album, Sjangre og Komponister.

{{< cards cols="1">}}
{{< card title="" subtitle="Musikkbibliotek med kategorier" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Opprett spillelister

Du kan også opprette dine egne spillelister.

Først, åpne **Spillelister**-fanen.

{{< cards cols="1">}}
{{< card title="" subtitle="Spillelister-fanen i Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Trykk på **pluss (+)**-knappen og velg **Ny spilleliste**.

{{< cards cols="1">}}
{{< card title="" subtitle="Opprett en ny spilleliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Skriv inn et navn for spillelisten og trykk **Lagre**.

{{< cards cols="1">}}
{{< card title="" subtitle="Skriv inn spillelistenavn" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Velg deretter en kilde å legge til sanger fra — her velger vi **Biblioteket**.

{{< cards cols="1">}}
{{< card title="" subtitle="Legg til sanger i ny spilleliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Velg sangene du ønsker og trykk **Ferdig** for å legge dem til.

{{< cards cols="1">}}
{{< card title="" subtitle="Legg til musikk fra biblioteket i spillelisten" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

De valgte sporene vises nå i den opprettede spillelisten.

{{< cards cols="1">}}
{{< card title="" subtitle="Opprettet spilleliste vist i listen" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Som standard er sanger tilgjengelige for strømming. For å lytte offline, aktiver **Offline-modus** — appen laster ned alle spillelistespor.

{{< cards cols="1">}}
{{< card title="" subtitle="Offline-modus aktivert for spilleliste" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Trykk på **Flere handlinger**-knappen for å utforske flere alternativer. Du kan:

- Arkivere spillelisten
- Endre albumomslaget
- Omorganisere spor
- Og flere nyttige funksjoner

{{< cards cols="1">}}
{{< card title="" subtitle="Flere spillelistehandlinger tilgjengelig" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Konklusjon

Med **Evermusic** og **Flacbox** er det enkelt å gjøre iPhone, iPad eller Mac til en kraftig DLNA-musikkspiller. Enten du lagrer musikken i skyen, på en NAS eller på en hjemmemedieserver som **Kodi**, lar disse appene deg strømme, organisere og nyte samlingen din uten begrensninger.

- Strøm MP3 eller hi-res FLAC direkte fra **Kodi DLNA-serveren** din
- Bygg et personlig musikkbibliotek gruppert etter metadata (album, sjangre, komponister)
- Opprett og administrer **egne spillelister**
- Aktiver **offline-modus** for lytting på farten
- Koble til **flere skytjenester** og **lokale nettverksenheter**
- Spor lyttevanene dine med **Last.fm-integrering**

Enten du er en audiofil eller en tilfeldig lytter, tilbyr Evermusic og Flacbox alt du trenger for sømløs musikkstrømming og organisering.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Last ned Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Last ned Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Begynn å bygge din personlige musikkopplevelse i dag.

## Vanlige spørsmål

{{% details title="Er Kodi gratis å bruke som DLNA-server?" closed="true" %}}
Ja. Kodi er helt gratis og åpen kildekode. Den kjører på macOS, Windows, Linux og mange NAS-enheter.
{{% /details %}}

{{% details title="Støtter Evermusic og Flacbox FLAC-strømming over DLNA?" closed="true" %}}
Ja. Flacbox er optimalisert for hi-res formater som FLAC, ALAC og DSD. Evermusic støtter også FLAC-avspilling sammen med MP3 og andre standardformater.
{{% /details %}}

{{% details title="Kan jeg lytte offline etter strømming fra Kodi?" closed="true" %}}
Ja. Aktiver Offline-modus på en spilleliste, og appen laster ned alle spor til enheten for lytting uten nettverkstilkobling.
{{% /details %}}

{{% details title="Trenger jeg et premium-abonnement for å bruke DLNA?" closed="true" %}}
Gratisversjonen støtter opptil 3 sky- eller nettverkstilkoblinger. Premium fjerner denne grensen og lar deg koble til ubegrensede tjenester og DLNA-servere.
{{% /details %}}

{{% details title="Må iPhonen min være på samme Wi-Fi-nettverk som Kodi?" closed="true" %}}
Ja. DLNA-strømming fungerer over det lokale nettverket. Både Kodi-serveren og iOS-enheten må være koblet til det samme Wi-Fi-nettverket.
{{% /details %}}

{{% details title="Kan jeg bruke dette oppsettet med en NAS i stedet for en Mac eller PC?" closed="true" %}}
Ja. Mange NAS-enheter (Synology, QNAP osv.) støtter Kodi eller har sin egen innebygde DLNA-server. Evermusic og Flacbox kan koble til enhver standard DLNA/UPnP-server.
{{% /details %}}
