---
title: "Com reproduir la teva música des de Mac / PC / Linux / NAS a l'iPhone utilitzant el servidor Kodi DLNA"
date: 2025-07-25
description: "Transmet música des del teu ordinador o NAS al teu iPhone per Wi-Fi utilitzant Kodi DLNA i l'aplicació Evermusic."
keywords: ["servidor kodi dlna", "transmetre música a iphone", "reproduir música des de nas", "evermusic dlna", "música de mac a iphone", "música de windows a iphone", "kodi dlna iphone", "transmissió d'àudio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "transmissió de música", "mac", "nas", "linux", "xarxa local"]
readingTime: 5
---

{{< author-byline >}}


**Resum:** Instal·la Kodi al teu Mac, PC, Linux o NAS, activa el seu servidor DLNA/UPnP i transmet tota la teva biblioteca musical a l'iPhone o iPad utilitzant l'aplicació gratuïta Evermusic o Flacbox per Wi-Fi. Sense subscripcions.

## Introducció

Si tens un **Mac, PC amb Windows, màquina Linux o dispositiu NAS**, pots transformar-lo fàcilment en un **servidor de música personal** a casa utilitzant [Kodi](https://kodi.tv/), una plataforma multimèdia gratuïta i de codi obert. Amb el servidor **DLNA/UPnP** integrat de Kodi, pots transmetre tota la teva biblioteca musical a qualsevol client compatible amb DLNA — incloent el teu iPhone o iPad.

En aquesta guia, et mostrarem pas a pas com:

- Instal·lar Kodi al teu Mac o PC  
- Configurar les carpetes de música per compartir  
- Activar el servidor de música DLNA  
- Accedir a aquesta música utilitzant l'aplicació **Evermusic** o **Flacbox** per a iOS

Aquesta configuració és 100% gratuïta — sense subscripcions, només la teva pròpia música transmesa per la teva xarxa Wi-Fi. Tant si intentes organitzar la teva gran col·lecció de MP3, escoltar FLAC per Wi-Fi, o simplement gaudir de la teva música local sense sincronitzar via iTunes, aquesta configuració és perfecta per a tu.

## Descarregar i instal·lar Kodi al teu Mac / PC / Linux / NAS

Primer, visita el lloc web oficial de Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Pàgina principal de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Fes clic a **Descàrregues** i desplaça't per trobar la versió per al teu ordinador.
Tria el teu sistema operatiu. En aquest exemple, utilitzarem **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Pàgina de descàrregues de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Fes clic a **Intel (x86/64)** si tens un Mac amb Intel o **Apple Silicon** per a M1, M2, M3 Mac per iniciar la descàrrega.

{{< cards cols="1">}}
{{< card subtitle="Tria l'instal·lador de macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Espera un moment mentre es descarrega l'instal·lador.

{{< cards cols="1">}}
{{< card subtitle="Kodi descarregat" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Un cop descarregat, localitza el fitxer `.dmg` a la teva carpeta de **Descàrregues**.

{{< cards cols="1">}}
{{< card subtitle="Instal·lar Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Fes doble clic al fitxer descarregat per llançar l'instal·lador.
Arrossega Kodi a la teva carpeta d'**Aplicacions** per instal·lar-lo.

{{< cards cols="1">}}
{{< card title="" subtitle="Instal·la Kodi arrossegant-lo a Aplicacions" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Obre Kodi. Potser necessitaràs permetre'l a **Preferències del Sistema → Seguretat i Privacitat → Obrir de totes maneres**.

{{< cards cols="1">}}
{{< card subtitle="Pantalla principal de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Afegir música a la biblioteca de Kodi

Fes clic a la **icona d'engranatge** (Configuració) des de la pantalla d'inici.

{{< cards cols="1">}}
{{< card subtitle="Configuració de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navega a **Configuració de Mitjans → Biblioteca**. Activa **Actualitzar biblioteca a l'inici** per a la biblioteca de vídeo i música per a la indexació automàtica.

{{< cards cols="1">}}
{{< card subtitle="Configuració de la biblioteca" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Després ves a la secció **Música** i fes clic a **Afegir música**.

{{< cards cols="1">}}
{{< card subtitle="Afegir carpeta de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Navega i selecciona la carpeta on s'emmagatzema la teva música.

{{< cards cols="1">}}
{{< card subtitle="Triar font de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Afegeix la font de música a Kodi.

{{< cards cols="1">}}
{{< card subtitle="Afegir font de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirma i deixa que Kodi escanegi la teva biblioteca musical.

{{< cards cols="1">}}
{{< card subtitle="Confirmar fonts de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Espera un moment mentre la biblioteca s'escaneja i es construeix completament.

{{< cards cols="1">}}
{{< card subtitle="Escanejant la biblioteca musical" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Activar el servidor DLNA de Kodi

Ves a **Configuració → Serveis → UPnP/DLNA**.

Activa l'opció: **Compartir les meves biblioteques**.

Kodi ara actua com a servidor DLNA a la teva xarxa Wi-Fi local.

{{< cards cols="1">}}
{{< card subtitle="Activar DLNA a Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Obrir la biblioteca de Kodi

Fes clic dret per tancar la finestra de configuració i obrir la biblioteca principal de Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Fes clic dret per accedir a la biblioteca de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Descarregar l'aplicació de transmissió de música per a iOS

Obtén una aplicació client DLNA gratuïta per a iOS que et permet transmetre música des d'una àmplia gamma de serveis d'emmagatzematge al núvol i servidors DLNA.

- Utilitza **Evermusic** si la teva col·lecció és principalment MP3 i altres formats d'àudio estàndard.
- Tria **Flacbox** si tens una biblioteca de música d'alta resolució en formats com FLAC, ALAC o DSD.

Ambdues aplicacions estan disponibles per a **iOS** i **macOS**, i són gratuïtes.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descarregar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descarregar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Afegir font DLNA

Un cop descarregada l'aplicació iOS, obre la secció **Totes les Connexions**.

{{< cards cols="1">}}
{{< card title="" subtitle="Barra lateral principal de l'aplicació Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Desplaça't cap avall i toca **Xarxa local - Dispositius disponibles** per descobrir servidors DLNA.
En aquesta secció, veuràs tots els dispositius disponibles a la teva xarxa local. El teu **servidor Kodi DLNA** hauria d'aparèixer aquí. Toca el servidor Kodi per connectar-te.

{{< cards cols="1">}}
{{< card title="" subtitle="Dispositius DLNA disponibles a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic mostrarà les carpetes de la biblioteca compartides a través de Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical de Kodi a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navega a la carpeta **Cançons** per veure tots els fitxers d'àudio disponibles al teu servidor DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Cançons llistades des de la carpeta remota" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Toca qualsevol fitxer d'àudio per començar a transmetre instantàniament.

{{< cards cols="1">}}
{{< card title="" subtitle="Fitxer MP3 reproduint-se a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Torna a la secció **Connexions**. El servidor DLNA afegit apareixerà aquí. Toca la seva icona per reconnectar en qualsevol moment. També pots connectar altres serveis al núvol des d'aquesta pantalla seguint els mateixos passos.

També pots activar el **seguiment de Last.fm** aquí. Les estadístiques de reproducció es desaran al teu compte de Last.fm, proporcionant recomanacions musicals personalitzades més endavant.

{{< cards cols="1">}}
{{< card title="" subtitle="Connexions a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Construir la biblioteca musical

Tant **Evermusic** com **Flacbox** et permeten afegir música a la teva biblioteca i organitzar-la per **etiquetes de metadades** com artistes, àlbums, gèneres i compositors.

Per començar, obre la secció **Biblioteca Musical**. Desplaça't cap avall fins a **Eines i preferències** i toca **Afegir música**.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical d'Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Selecciona la font de música — en aquest cas, tria **Connexions**.

{{< cards cols="1">}}
{{< card title="" subtitle="Afegir música nova a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Troba el **servidor Kodi DLNA** a les Connexions i toca per veure carpetes i fitxers.

{{< cards cols="1">}}
{{< card title="" subtitle="Triar servidor DLNA per importar música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Tria les carpetes o fitxers que vols afegir i toca **Fet**.

{{< cards cols="1">}}
{{< card title="" subtitle="Seleccionar carpeta de música per afegir" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

L'aplicació escanejarà els fitxers seleccionats i els organitzarà utilitzant metadades en seccions com Artistes, Àlbums, Gèneres i Compositors.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical amb categories" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Crear llistes de reproducció

També pots crear les teves pròpies llistes de reproducció.

Primer, obre la pestanya **Llistes de reproducció**.

{{< cards cols="1">}}
{{< card title="" subtitle="Pestanya de llistes de reproducció a Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Toca el botó **més (+)** i tria **Nova llista de reproducció**.

{{< cards cols="1">}}
{{< card title="" subtitle="Crear una nova llista de reproducció" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Introdueix un nom per a la teva llista de reproducció i toca **Desar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Introduir nom de la llista de reproducció" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

A continuació, tria una font per afegir cançons — aquí, seleccionem la **Biblioteca**.

{{< cards cols="1">}}
{{< card title="" subtitle="Afegir cançons a la nova llista de reproducció" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Selecciona les cançons que vols i toca **Fet** per afegir-les.

{{< cards cols="1">}}
{{< card title="" subtitle="Afegir música de la biblioteca a la llista de reproducció" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Les pistes seleccionades apareixeran ara a la llista de reproducció creada.

{{< cards cols="1">}}
{{< card title="" subtitle="Llista de reproducció creada mostrada a la llista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Per defecte, les cançons estan disponibles per a la transmissió. Per escoltar fora de línia, activa el **Mode fora de línia** — l'aplicació descarregarà totes les pistes de la llista de reproducció.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode fora de línia activat per a la llista de reproducció" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Toca el botó **Més accions** per explorar opcions addicionals. Pots:

- Arxivar la llista de reproducció  
- Canviar la portada de l'àlbum  
- Reordenar les pistes  
- I més funcions útils

{{< cards cols="1">}}
{{< card title="" subtitle="Més accions de llista de reproducció disponibles" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusió

Amb **Evermusic** i **Flacbox**, convertir el teu iPhone, iPad o Mac en un potent reproductor de música DLNA és fàcil. Tant si emmagatzemes la teva música al núvol, en un NAS o en un servidor multimèdia domèstic com **Kodi**, aquestes aplicacions et permeten transmetre, organitzar i gaudir de la teva col·lecció sense límits.

- Transmet MP3 o FLAC d'alta resolució directament des del teu **servidor Kodi DLNA**  
- Construeix una biblioteca musical personal agrupada per metadades (àlbums, gèneres, compositors)  
- Crea i gestiona **llistes de reproducció personalitzades**  
- Activa el **mode fora de línia** per escoltar en moviment  
- Connecta't a **múltiples serveis al núvol** i **dispositius de xarxa local**  
- Segueix els teus hàbits d'escolta amb la **integració de Last.fm**

Tant si ets un audiòfil com un oient casual, Evermusic i Flacbox ofereixen tot el que necessites per a una transmissió i organització musical sense interrupcions.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descarregar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descarregar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Comença a construir la teva experiència musical personal avui.

## Preguntes freqüents

{{% details title="Kodi és gratuït per utilitzar com a servidor DLNA?" closed="true" %}}
Sí. Kodi és completament gratuït i de codi obert. Funciona en macOS, Windows, Linux i molts dispositius NAS.
{{% /details %}}

{{% details title="Evermusic i Flacbox suporten la transmissió de FLAC per DLNA?" closed="true" %}}
Sí. Flacbox està optimitzat per a formats d'alta resolució com FLAC, ALAC i DSD. Evermusic també suporta la reproducció de FLAC juntament amb MP3 i altres formats estàndard.
{{% /details %}}

{{% details title="Puc escoltar fora de línia després de transmetre des de Kodi?" closed="true" %}}
Sí. Activa el Mode fora de línia en qualsevol llista de reproducció, i l'aplicació descarregarà totes les pistes al teu dispositiu per escoltar sense connexió de xarxa.
{{% /details %}}

{{% details title="Necessito una subscripció premium per utilitzar DLNA?" closed="true" %}}
La versió gratuïta suporta fins a 3 connexions al núvol o de xarxa. La versió Premium elimina aquest límit i et permet connectar serveis i servidors DLNA il·limitats.
{{% /details %}}

{{% details title="El meu iPhone ha d'estar a la mateixa xarxa Wi-Fi que Kodi?" closed="true" %}}
Sí. La transmissió DLNA funciona a través de la teva xarxa local. Tant el servidor Kodi com el teu dispositiu iOS han d'estar connectats a la mateixa xarxa Wi-Fi.
{{% /details %}}

{{% details title="Puc utilitzar aquesta configuració amb un NAS en lloc d'un Mac o PC?" closed="true" %}}
Sí. Molts dispositius NAS (Synology, QNAP, etc.) suporten Kodi o tenen el seu propi servidor DLNA integrat. Evermusic i Flacbox poden connectar-se a qualsevol servidor DLNA/UPnP estàndard.
{{% /details %}}
