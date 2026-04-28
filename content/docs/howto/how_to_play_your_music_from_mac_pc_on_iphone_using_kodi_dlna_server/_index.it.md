---
title: "Come riprodurre la musica da Mac / PC / Linux / NAS su iPhone usando il server Kodi DLNA"
date: 2025-07-25
description: "Trasmetti musica dal tuo computer o NAS al tuo iPhone tramite Wi-Fi usando Kodi DLNA e l'app Evermusic."
keywords: ["server kodi dlna", "streaming musica su iphone", "riprodurre musica da nas", "evermusic dlna", "musica da mac a iphone", "musica da windows a iphone", "kodi dlna iphone", "streaming audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "streaming musicale", "mac", "nas", "linux", "rete locale"]
readingTime: 5
---

{{< author-byline >}}


**Riepilogo:** Installa Kodi sul tuo Mac, PC, Linux o NAS, abilita il server DLNA/UPnP e trasmetti l'intera libreria musicale su iPhone o iPad usando l'app gratuita Evermusic o Flacbox tramite Wi-Fi. Nessun abbonamento richiesto.

## Introduzione

Se hai un **Mac, PC Windows, macchina Linux o dispositivo NAS**, puoi facilmente trasformarlo in un **server musicale personale** a casa usando [Kodi](https://kodi.tv/), una piattaforma multimediale gratuita e open-source. Con il server **DLNA/UPnP** integrato di Kodi, puoi trasmettere l'intera libreria musicale a qualsiasi client compatibile DLNA — incluso il tuo iPhone o iPad.

In questa guida, ti mostreremo passo dopo passo come:

- Installare Kodi sul Mac o PC  
- Configurare le cartelle musicali per la condivisione  
- Abilitare il server musicale DLNA  
- Accedere a quella musica usando l'app **Evermusic** o **Flacbox** per iOS

Questa configurazione è gratuita al 100% — nessun abbonamento, solo la tua musica trasmessa sulla tua rete Wi-Fi. Che tu stia cercando di organizzare la tua grande collezione di MP3, ascoltare FLAC tramite Wi-Fi, o semplicemente goderti la tua musica locale senza sincronizzare tramite iTunes, questa configurazione è perfetta per te.

## Scarica e installa Kodi sul tuo Mac / PC / Linux / NAS

Per prima cosa, visita il sito web ufficiale di Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Pagina principale di Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Clicca su **Download** e scorri per trovare la versione per il tuo computer. Scegli il tuo sistema operativo. In questo esempio, useremo **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Pagina download di Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Clicca su **Intel (x86/64)** se hai un Mac Intel o **Apple Silicon** per M1, M2, M3 Mac per avviare il download.

{{< cards cols="1">}}
{{< card subtitle="Scegli il programma di installazione macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Attendi un momento mentre il programma di installazione viene scaricato.

{{< cards cols="1">}}
{{< card subtitle="Kodi scaricato" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Una volta scaricato, individua il file `.dmg` nella cartella **Download**.

{{< cards cols="1">}}
{{< card subtitle="Installa Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Fai doppio clic sul file scaricato per avviare il programma di installazione. Trascina Kodi nella cartella **Applicazioni** per installarlo.

{{< cards cols="1">}}
{{< card title="" subtitle="Installa Kodi trascinandolo in Applicazioni" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Avvia Kodi. Potrebbe essere necessario autorizzarlo in **Preferenze di Sistema → Sicurezza e Privacy → Apri comunque**.

{{< cards cols="1">}}
{{< card subtitle="Schermata principale di Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Aggiungi musica alla libreria di Kodi

Clicca sull'**icona dell'ingranaggio** (Impostazioni) dalla schermata principale.

{{< cards cols="1">}}
{{< card subtitle="Impostazioni di Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Naviga in **Impostazioni media → Libreria**. Abilita **Aggiorna libreria all'avvio** per la libreria video e musicale per l'indicizzazione automatica.

{{< cards cols="1">}}
{{< card subtitle="Impostazioni libreria" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Poi vai alla sezione **Musica** e clicca su **Aggiungi musica**.

{{< cards cols="1">}}
{{< card subtitle="Aggiungi cartella musicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Sfoglia e seleziona la cartella dove è memorizzata la tua musica.

{{< cards cols="1">}}
{{< card subtitle="Scegli sorgente musicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Aggiungi la sorgente musicale a Kodi.

{{< cards cols="1">}}
{{< card subtitle="Aggiungi sorgente musicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Conferma e lascia che Kodi scansioni la tua libreria musicale.

{{< cards cols="1">}}
{{< card subtitle="Conferma sorgenti musicali" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Attendi un momento mentre la libreria viene scansionata e completamente costruita.

{{< cards cols="1">}}
{{< card subtitle="Scansione libreria musicale" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Abilita il server DLNA di Kodi

Vai su **Impostazioni → Servizi → UPnP/DLNA**.

Abilita l'opzione: **Condividi le mie librerie**.

Kodi ora funge da server DLNA sulla tua rete Wi-Fi locale.

{{< cards cols="1">}}
{{< card subtitle="Abilita DLNA in Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Apri la libreria Kodi

Fai clic destro per chiudere la finestra delle impostazioni e aprire la libreria principale di Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Clic destro per accedere alla libreria Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Scarica l'app di streaming musicale per iOS

Ottieni un'app client DLNA gratuita per iOS che ti permette di trasmettere musica da un'ampia gamma di servizi di archiviazione cloud e server DLNA.

- Usa **Evermusic** se la tua collezione è principalmente MP3 e altri formati audio standard.
- Scegli **Flacbox** se hai una libreria musicale hi-res in formati come FLAC, ALAC o DSD.

Entrambe le app sono disponibili per **iOS** e **macOS**, e gratuite da usare.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Scarica Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Scarica Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Aggiungi sorgente DLNA

Dopo aver scaricato l'app iOS, apri la sezione **Tutte le Connessioni**.

{{< cards cols="1">}}
{{< card title="" subtitle="Barra laterale principale dell'app Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Scorri verso il basso e tocca **Rete locale - Dispositivi disponibili** per scoprire i server DLNA. In questa sezione, vedrai tutti i dispositivi disponibili sulla tua rete locale. Il tuo **server Kodi DLNA** dovrebbe apparire qui. Tocca il server Kodi per connetterti.

{{< cards cols="1">}}
{{< card title="" subtitle="Dispositivi DLNA disponibili in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic mostrerà le cartelle della libreria condivise tramite Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Libreria musicale Kodi in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Naviga nella cartella **Brani** per visualizzare tutti i file audio disponibili sul tuo server DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Brani elencati dalla cartella remota" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Tocca qualsiasi file audio per iniziare lo streaming istantaneamente.

{{< cards cols="1">}}
{{< card title="" subtitle="File MP3 in riproduzione in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Torna alla sezione **Connessioni**. Il server DLNA aggiunto apparirà ora qui. Tocca la sua icona per riconnetterti in qualsiasi momento. Puoi anche connettere altri servizi cloud da questa schermata usando gli stessi passaggi.

Puoi anche abilitare lo **scrobbling Last.fm** qui. Le statistiche di riproduzione verranno salvate nel tuo account Last.fm, fornendo raccomandazioni musicali personalizzate in seguito.

{{< cards cols="1">}}
{{< card title="" subtitle="Connessioni in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Costruisci la libreria musicale

Sia **Evermusic** che **Flacbox** ti permettono di aggiungere musica alla tua libreria e organizzarla per **tag dei metadati** come artisti, album, generi e compositori.

Per iniziare, apri la sezione **Libreria musicale**. Scorri verso il basso fino a **Strumenti e preferenze** e tocca **Aggiungi musica**.

{{< cards cols="1">}}
{{< card title="" subtitle="Libreria musicale Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Seleziona la sorgente musicale — in questo caso, scegli **Connessioni**.

{{< cards cols="1">}}
{{< card title="" subtitle="Aggiungi nuova musica in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Trova il **server Kodi DLNA** nelle Connessioni e tocca per visualizzare cartelle e file.

{{< cards cols="1">}}
{{< card title="" subtitle="Scegli server DLNA per importare musica" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Scegli le cartelle o i file che vuoi aggiungere e tocca **Fatto**.

{{< cards cols="1">}}
{{< card title="" subtitle="Seleziona cartella musicale da aggiungere" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

L'app scansionerà i file selezionati e li organizzerà usando i metadati in sezioni come Artisti, Album, Generi e Compositori.

{{< cards cols="1">}}
{{< card title="" subtitle="Libreria musicale con categorie" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Crea Playlist

Puoi anche creare le tue playlist personali.

Per prima cosa, apri la scheda **Playlist**.

{{< cards cols="1">}}
{{< card title="" subtitle="Scheda Playlist in Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Tocca il pulsante **più (+)** e scegli **Nuova playlist**.

{{< cards cols="1">}}
{{< card title="" subtitle="Crea una nuova playlist" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Inserisci un nome per la tua playlist e tocca **Salvare**.

{{< cards cols="1">}}
{{< card title="" subtitle="Inserisci nome playlist" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

Poi, scegli una sorgente da cui aggiungere brani — qui, selezioniamo la **Libreria**.

{{< cards cols="1">}}
{{< card title="" subtitle="Aggiungi brani alla nuova playlist" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Seleziona i brani che desideri e tocca **Fatto** per aggiungerli.

{{< cards cols="1">}}
{{< card title="" subtitle="Aggiungi musica dalla libreria alla playlist" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

I brani selezionati appariranno ora nella playlist creata.

{{< cards cols="1">}}
{{< card title="" subtitle="Playlist creata mostrata nell'elenco" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Per impostazione predefinita, i brani sono disponibili per lo streaming. Per ascoltare offline, abilita la **Modalità offline** — l'app scaricherà tutti i brani della playlist.

{{< cards cols="1">}}
{{< card title="" subtitle="Modalità offline abilitata per la playlist" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Tocca il pulsante **Altre azioni** per esplorare opzioni aggiuntive. Puoi:

- Archiviare la playlist  
- Cambiare la copertina dell'album  
- Riordinare i brani  
- E altre funzionalità utili

{{< cards cols="1">}}
{{< card title="" subtitle="Altre azioni playlist disponibili" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusione

Con **Evermusic** e **Flacbox**, trasformare il tuo iPhone, iPad o Mac in un potente lettore musicale DLNA è facile. Che tu memorizzi la tua musica nel cloud, su un NAS o su un server multimediale domestico come **Kodi**, queste app ti permettono di trasmettere, organizzare e goderti la tua collezione senza limiti.

- Trasmetti MP3 o FLAC hi-res direttamente dal tuo **server Kodi DLNA**  
- Costruisci una libreria musicale personale raggruppata per metadati (album, generi, compositori)  
- Crea e gestisci **playlist personalizzate**  
- Abilita la **modalità offline** per ascoltare in movimento  
- Connettiti a **più servizi cloud** e **dispositivi di rete locale**  
- Traccia le tue abitudini di ascolto con l'**integrazione Last.fm**

Che tu sia un audiofilo o un ascoltatore occasionale, Evermusic e Flacbox offrono tutto ciò di cui hai bisogno per uno streaming e un'organizzazione musicale senza interruzioni.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Scarica Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Scarica Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Inizia a costruire la tua esperienza musicale personale oggi.

## FAQ

{{% details title="Kodi è gratuito come server DLNA?" closed="true" %}}
Sì. Kodi è completamente gratuito e open-source. Funziona su macOS, Windows, Linux e molti dispositivi NAS.
{{% /details %}}

{{% details title="Evermusic e Flacbox supportano lo streaming FLAC tramite DLNA?" closed="true" %}}
Sì. Flacbox è ottimizzato per formati hi-res come FLAC, ALAC e DSD. Evermusic supporta anche la riproduzione FLAC insieme a MP3 e altri formati standard.
{{% /details %}}

{{% details title="Posso ascoltare offline dopo lo streaming da Kodi?" closed="true" %}}
Sì. Abilita la Modalità offline su qualsiasi playlist, e l'app scaricherà tutti i brani sul tuo dispositivo per l'ascolto senza connessione di rete.
{{% /details %}}

{{% details title="Ho bisogno di un abbonamento premium per usare DLNA?" closed="true" %}}
La versione gratuita supporta fino a 3 connessioni cloud o di rete. Premium rimuove questo limite e ti permette di connettere servizi e server DLNA illimitati.
{{% /details %}}

{{% details title="Il mio iPhone deve essere sulla stessa rete Wi-Fi di Kodi?" closed="true" %}}
Sì. Lo streaming DLNA funziona sulla tua rete locale. Sia il server Kodi che il tuo dispositivo iOS devono essere connessi alla stessa rete Wi-Fi.
{{% /details %}}

{{% details title="Posso usare questa configurazione con un NAS invece di un Mac o PC?" closed="true" %}}
Sì. Molti dispositivi NAS (Synology, QNAP, ecc.) supportano Kodi o hanno il proprio server DLNA integrato. Evermusic e Flacbox possono connettersi a qualsiasi server DLNA/UPnP standard.
{{% /details %}}
