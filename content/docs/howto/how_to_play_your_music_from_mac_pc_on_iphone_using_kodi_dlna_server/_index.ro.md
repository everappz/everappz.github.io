---
title: "Cum să redai muzica de pe Mac / PC / Linux / NAS pe iPhone folosind serverul Kodi DLNA"
date: 2025-07-25
description: "Transmite muzică de pe computer sau NAS pe iPhone prin Wi-Fi folosind Kodi DLNA și aplicația Evermusic."
keywords: ["server kodi dlna", "streaming muzică pe iphone", "redare muzică de pe nas", "evermusic dlna", "muzică de pe mac pe iphone", "muzică de pe windows pe iphone", "kodi dlna iphone", "streaming audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streaming muzică", "mac", "nas", "linux", "rețea locală"]
readingTime: 5
---

{{< author-byline >}}

**TL;DR:** Instalează Kodi pe Mac, PC, Linux sau NAS, activează serverul DLNA/UPnP și transmite întreaga bibliotecă muzicală pe iPhone sau iPad folosind aplicația gratuită Evermusic sau Flacbox prin Wi-Fi. Fără abonamente.

## Introducere

Dacă ai un **Mac, PC cu Windows, mașină Linux sau dispozitiv NAS**, îl poți transforma ușor într-un **server de muzică personal** acasă folosind [Kodi](https://kodi.tv/), o platformă media gratuită și open-source. Cu serverul **DLNA/UPnP** integrat al Kodi, poți transmite întreaga bibliotecă muzicală către orice client compatibil DLNA — inclusiv iPhone-ul sau iPad-ul tău.

În acest ghid, îți vom arăta pas cu pas cum să:

- Instalezi Kodi pe Mac sau PC
- Configurezi folderele de muzică pentru partajare
- Activezi serverul de muzică DLNA
- Accesezi muzica folosind aplicația **Evermusic** sau **Flacbox** pentru iOS

Această configurare este 100% gratuită — fără abonamente, doar muzica ta transmisă prin rețeaua Wi-Fi. Fie că încerci să organizezi o colecție mare de MP3, să asculți FLAC prin Wi-Fi sau pur și simplu să te bucuri de muzica locală fără sincronizare prin iTunes, această configurare este perfectă pentru tine.

## Descarcă și instalează Kodi pe Mac / PC / Linux / NAS

Mai întâi, vizitează site-ul oficial Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Pagina principală Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Apasă pe **Descărcări** și derulează pentru a găsi versiunea pentru computerul tău.
Alege sistemul de operare. În acest exemplu, vom folosi **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Pagina de descărcări Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Apasă **Intel (x86/64)** dacă ai un Mac Intel sau **Apple Silicon** pentru M1, M2, M3 Mac pentru a începe descărcarea.

{{< cards cols="1">}}
{{< card subtitle="Alege instalatorul macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Te rugăm să aștepți un moment cât se descarcă instalatorul.

{{< cards cols="1">}}
{{< card subtitle="Kodi descărcat" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

După descărcare, localizează fișierul `.dmg` în folderul **Descărcări**.

{{< cards cols="1">}}
{{< card subtitle="Instalează Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Dublu-clic pe fișierul descărcat pentru a lansa instalatorul.
Trage Kodi în folderul **Aplicații** pentru a instala.

{{< cards cols="1">}}
{{< card title="" subtitle="Instalează Kodi trăgându-l în Aplicații" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Lansează Kodi. S-ar putea să fie nevoie să-l permiți în **Preferințe Sistem → Securitate și Confidențialitate → Deschide oricum**.

{{< cards cols="1">}}
{{< card subtitle="Ecranul principal Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Adaugă muzică în biblioteca Kodi

Apasă pe **pictograma roată dințată** (Setări) din ecranul principal.

{{< cards cols="1">}}
{{< card subtitle="Setări Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navighează la **Setări Media → Bibliotecă**. Activează **Actualizează biblioteca la pornire** pentru biblioteca video și muzicală pentru indexare automată.

{{< cards cols="1">}}
{{< card subtitle="Setări bibliotecă" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Apoi mergi la secțiunea **Muzică** și apasă **Adaugă muzică**.

{{< cards cols="1">}}
{{< card subtitle="Adaugă folder de muzică" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Navighează și selectează folderul unde este stocată muzica ta.

{{< cards cols="1">}}
{{< card subtitle="Alege sursa de muzică" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Adaugă sursa de muzică în Kodi.

{{< cards cols="1">}}
{{< card subtitle="Adaugă sursă de muzică" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirmă și lasă Kodi să scaneze biblioteca muzicală.

{{< cards cols="1">}}
{{< card subtitle="Confirmă sursele de muzică" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Așteaptă un moment cât biblioteca este scanată și complet construită.

{{< cards cols="1">}}
{{< card subtitle="Scanarea bibliotecii muzicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Activează serverul DLNA al Kodi

Mergi la **Setări → Servicii → UPnP/DLNA**.

Activează opțiunea: **Partajează bibliotecile mele**.

Kodi funcționează acum ca server DLNA în rețeaua ta Wi-Fi locală.

{{< cards cols="1">}}
{{< card subtitle="Activează DLNA în Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Deschide biblioteca Kodi

Clic dreapta pentru a închide fereastra de setări și a deschide biblioteca principală Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Clic dreapta pentru a accesa biblioteca Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Descarcă aplicația de streaming muzical pentru iOS

Obține o aplicație client DLNA gratuită pentru iOS care îți permite să transmiți muzică din diverse servicii de stocare cloud și servere DLNA.

- Folosește **Evermusic** dacă colecția ta este în principal MP3 și alte formate audio standard.
- Alege **Flacbox** dacă ai o bibliotecă muzicală hi-res în formate precum FLAC, ALAC sau DSD.

Ambele aplicații sunt disponibile pentru **iOS** și **macOS**, și sunt gratuite.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descarcă Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descarcă Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Adaugă sursă DLNA

După ce ai descărcat aplicația iOS, deschide secțiunea **Toate Conexiunile**.

{{< cards cols="1">}}
{{< card title="" subtitle="Bara laterală principală a aplicației Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Derulează în jos și apasă **Rețea locală - Dispozitive disponibile** pentru a descoperi serverele DLNA.
În această secțiune, vei vedea toate dispozitivele disponibile din rețeaua ta locală. **Serverul Kodi DLNA** ar trebui să apară aici. Apasă pe serverul Kodi pentru a te conecta.

{{< cards cols="1">}}
{{< card title="" subtitle="Dispozitive DLNA disponibile în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic va afișa folderele bibliotecii partajate prin Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca muzicală Kodi în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navighează la folderul **Melodii** pentru a vedea toate fișierele audio disponibile pe serverul DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Melodii listate din folderul la distanță" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Apasă pe orice fișier audio pentru a începe streaming-ul instantaneu.

{{< cards cols="1">}}
{{< card title="" subtitle="Fișier MP3 redând în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Revino la secțiunea **Conexiuni**. Serverul DLNA adăugat va apărea acum aici. Apasă pe pictograma sa pentru a te reconecta oricând. Poți conecta și alte servicii cloud din acest ecran folosind aceiași pași.

Poți activa și **scrobbling-ul Last.fm** aici. Statisticile de redare vor fi salvate în contul tău Last.fm, oferind recomandări muzicale personalizate ulterior.

{{< cards cols="1">}}
{{< card title="" subtitle="Conexiuni în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Construiește biblioteca muzicală

Atât **Evermusic** cât și **Flacbox** îți permit să adaugi muzică în bibliotecă și să o organizezi după **etichete de metadate** precum artiști, albume, genuri și compozitori.

Pentru a începe, deschide secțiunea **Bibliotecă Muzicală**. Derulează în jos la **Instrumente și preferințe** și apasă **Adaugă muzică**.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca muzicală Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Selectează sursa de muzică — în acest caz, alege **Conexiuni**.

{{< cards cols="1">}}
{{< card title="" subtitle="Adaugă muzică nouă în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Găsește **serverul Kodi DLNA** în Conexiuni și apasă pentru a vedea foldere și fișiere.

{{< cards cols="1">}}
{{< card title="" subtitle="Alege serverul DLNA pentru import muzică" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Alege folderele sau fișierele pe care vrei să le adaugi și apasă **Finalizat**.

{{< cards cols="1">}}
{{< card title="" subtitle="Selectează folderul de muzică de adăugat" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

Aplicația va scana fișierele selectate și le va organiza folosind metadate în secțiuni precum Artiști, Albume, Genuri și Compozitori.

{{< cards cols="1">}}
{{< card title="" subtitle="Bibliotecă muzicală cu categorii" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Creează liste de redare

Poți crea și propriile liste de redare.

Mai întâi, deschide fila **Liste de redare**.

{{< cards cols="1">}}
{{< card title="" subtitle="Fila Liste de redare în Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Apasă butonul **plus (+)** și alege **Listă de redare nouă**.

{{< cards cols="1">}}
{{< card title="" subtitle="Creează o nouă listă de redare" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Introdu un nume pentru lista de redare și apasă **Salvați**.

{{< cards cols="1">}}
{{< card title="" subtitle="Introdu numele listei de redare" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Apoi, alege o sursă pentru a adăuga melodii — aici, selectăm **Biblioteca**.

{{< cards cols="1">}}
{{< card title="" subtitle="Adaugă melodii la noua listă de redare" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Selectează melodiile dorite și apasă **Finalizat** pentru a le adăuga.

{{< cards cols="1">}}
{{< card title="" subtitle="Adaugă muzică din bibliotecă în lista de redare" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Piesele selectate vor apărea acum în lista de redare creată.

{{< cards cols="1">}}
{{< card title="" subtitle="Lista de redare creată afișată în listă" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Implicit, melodiile sunt disponibile pentru streaming. Pentru a asculta offline, activează **Modul offline** — aplicația va descărca toate piesele listei.

{{< cards cols="1">}}
{{< card title="" subtitle="Modul offline activat pentru lista de redare" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Apasă butonul **Mai multe acțiuni** pentru a explora opțiuni suplimentare. Poți:

- Arhiva lista de redare
- Schimba coperta albumului
- Reordona piesele
- Și mai multe funcții utile

{{< cards cols="1">}}
{{< card title="" subtitle="Mai multe acțiuni pentru lista de redare disponibile" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Concluzie

Cu **Evermusic** și **Flacbox**, transformarea iPhone-ului, iPad-ului sau Mac-ului într-un player de muzică DLNA puternic este ușoară. Fie că stochezi muzica în cloud, pe un NAS sau pe un server media de acasă precum **Kodi**, aceste aplicații îți permit să transmiți, să organizezi și să te bucuri de colecția ta fără limite.

- Transmite MP3 sau FLAC hi-res direct de pe **serverul Kodi DLNA**
- Construiește o bibliotecă muzicală personală grupată după metadate (albume, genuri, compozitori)
- Creează și gestionează **liste de redare personalizate**
- Activează **modul offline** pentru a asculta în mișcare
- Conectează-te la **mai multe servicii cloud** și **dispozitive de rețea locală**
- Urmărește obiceiurile de ascultare cu **integrarea Last.fm**

Fie că ești un audiofil sau un ascultător ocazional, Evermusic și Flacbox oferă tot ce ai nevoie pentru streaming și organizare muzicală fără întreruperi.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descarcă Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descarcă Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Începe să construiești experiența ta muzicală personală astăzi.

## Întrebări frecvente

{{% details title="Este Kodi gratuit ca server DLNA?" closed="true" %}}
Da. Kodi este complet gratuit și open-source. Rulează pe macOS, Windows, Linux și multe dispozitive NAS.
{{% /details %}}

{{% details title="Suportă Evermusic și Flacbox streaming-ul FLAC prin DLNA?" closed="true" %}}
Da. Flacbox este optimizat pentru formate hi-res precum FLAC, ALAC și DSD. Evermusic suportă și redarea FLAC alături de MP3 și alte formate standard.
{{% /details %}}

{{% details title="Pot asculta offline după streaming de pe Kodi?" closed="true" %}}
Da. Activează Modul offline pe orice listă de redare și aplicația va descărca toate piesele pe dispozitiv pentru ascultare fără conexiune de rețea.
{{% /details %}}

{{% details title="Am nevoie de un abonament premium pentru a folosi DLNA?" closed="true" %}}
Versiunea gratuită suportă până la 3 conexiuni cloud sau de rețea. Premium elimină această limită și permite conectarea la servicii și servere DLNA nelimitate.
{{% /details %}}

{{% details title="iPhone-ul meu trebuie să fie pe aceeași rețea Wi-Fi ca Kodi?" closed="true" %}}
Da. Streaming-ul DLNA funcționează prin rețeaua ta locală. Atât serverul Kodi cât și dispozitivul iOS trebuie să fie conectate la aceeași rețea Wi-Fi.
{{% /details %}}

{{% details title="Pot folosi această configurare cu un NAS în loc de Mac sau PC?" closed="true" %}}
Da. Multe dispozitive NAS (Synology, QNAP etc.) suportă Kodi sau au propriul server DLNA integrat. Evermusic și Flacbox se pot conecta la orice server DLNA/UPnP standard.
{{% /details %}}
