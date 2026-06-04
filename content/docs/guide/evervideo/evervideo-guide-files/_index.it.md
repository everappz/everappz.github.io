---
title: "File"
date: 2020-02-01
lastmod: 2026-06-01
description: "Scopri come usare la scheda File in Evervideo su iPhone, iPad e Mac. Connetti servizi cloud, dispositivi NAS, server multimediali e stream RTSP in un unico posto. Gestisci video offline, la coda di trasferimento, i download, Wi-Fi Drive, la condivisione file iTunes / Finder e drive USB. Include iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA e archiviazione compatibile S3."
keywords: [
  "file Evervideo", "connessioni Evervideo", "file locali Evervideo",
  "configurazione video cloud iPhone", "connetti Google Drive video", "streaming video SMB",
  "lettore video WebDAV iOS", "video DLNA iPhone", "streaming video NAS",
  "trasferimento video Wi-Fi Drive", "iTunes File Sharing Evervideo", "RTSP iPhone",
  "Plex Evervideo", "Jellyfin Evervideo", "Emby Evervideo",
  "Subsonic Evervideo", "Navidrome Evervideo",
  "modalità offline video Evervideo", "coda trasferimento Evervideo",
  "gestore file Evervideo", "cartella Documenti Evervideo",
  "lettore video Synology", "lettore video QNAP",
  "lettore video Apple Time Capsule", "USB DAC video",
  "lettore video iXpand", "lettore video S3"
]
tags: ["guida", "evervideo", "file", "connessioni", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

La scheda File è il gestore file all-in-one di Evervideo. A differenza della maggior parte delle app video che separano l'archiviazione cloud dai file locali in schede diverse, Evervideo unisce entrambi in un'unica schermata scorrevole in modo da poter passare da un server Plex a una cartella cloud alla cartella Documenti dell'iPhone senza cambiare scheda.

La scheda File è divisa in sezioni chiare che appaiono in questo ordine sullo schermo:

- **Accesso Rapido** — recenti e preferiti per i file e le cartelle aperti più di recente.
- **File in Questa Applicazione** — ciò che si trova nella cartella Documenti in sandbox di Evervideo.
- **File su Questo iPhone / iPad / Mac** — video altrove sul dispositivo, esposti attraverso il selettore di file di sistema.
- **Archiviazione Cloud** — ogni account cloud, NAS e server multimediale che hai collegato.
- **Dispositivi Disponibili** — server e drive scoperto automaticamente da Bonjour / mDNS sulla rete locale.

Nell'angolo in alto a destra della schermata File c'è un pulsante Transfer (un'icona con frecce rotanti). Toccalo per aprire la Coda di Trasferimento dove puoi monitorare ogni download e caricamento da tutte le tue sorgenti.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Evervideo su Tutte le Archiviazioni Connesse" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Connetti all'Archiviazione Cloud

La sezione Archiviazione Cloud della scheda File è dove vivono ogni account connesso, NAS, server multimediale e stream — fianco a fianco, in un unico elenco scorrevole.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sezione Archiviazione Cloud Evervideo nella Scheda File" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Apri la scheda **File**.
- Scorri alla sezione **Archiviazione Cloud**.
- Tocca **Connetti all'archiviazione cloud** dal menu.
- Scegli un servizio di archiviazione cloud dall'elenco.
- Inserisci le tue credenziali nella pagina di autorizzazione ufficiale fornita dal provider cloud, quindi tocca **Fatto**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Connette un Servizio di Archiviazione Cloud" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Se incontri problemi, controlla la connessione internet e login / password. Nella versione Premium dell'app, puoi aggiungere un numero illimitato di servizi; la versione gratuita supporta fino a tre.

## Servizi di Archiviazione Cloud, Server Multimediali e Protocolli Supportati

Evervideo supporta una gamma eccezionalmente ampia di sorgenti per i tuoi video. Tutto qui sotto funziona da un unico flusso Connetti all'archiviazione cloud.

**Archiviazione cloud personale:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Server multimediali self-hosted:** Plex · Jellyfin · Emby · Subsonic (e ogni server compatibile Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (e ownCloud tramite API condivisa) · Synology Drive · QNAP.

**Protocolli NAS e condivisione file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, autenticazione con password o chiave pubblica) · NFS · DLNA / UPnP (riproduzione e download).

**Stream live e telecamere IP:** RTSP — punta Evervideo su qualsiasi URL `rtsp://` e riproduce subito. Ottimo per telecamere di sicurezza, stream IPTV, telecamere citofoniche, baby monitor e simili sorgenti live.

**Archiviazione oggetti compatibile S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualsiasi altro endpoint S3-API.

**Librerie sul dispositivo:** la libreria Foto (tutti i video, registrazioni schermo, album foto) e la libreria app Music (Album, Generi, Playlist) — entrambe appaiono nella Libreria Media così non devi copiare nulla.

**Scoperta rete locale:** la sezione Dispositivi Disponibili elenca automaticamente ogni servizio Bonjour / mDNS sulla rete Wi-Fi — server Plex, Jellyfin, Emby, Synology, QNAP, router AirPort con drive collegati, Apple Time Capsule — così puoi toccare per connetterti senza digitare un indirizzo IP.

Ogni connessione usa l'SDK ufficiale o il protocollo aperto del servizio, con autorizzazione basata su OAuth dove supportato. Puoi connettere più account dello stesso servizio (ad esempio, due account Google Drive, o sia un Plex che un server Jellyfin) e sfogliarli fianco a fianco nella sezione Archiviazione Cloud.

## Sicurezza e Privacy

Evervideo usa solo SDK ufficiali e connessioni sicure per interagire con i servizi cloud connessi. Il tuo login e password non sono accessibili all'applicazione — tutti i trasferimenti sono crittografati TLS.

Quando inserisci il login e la password, l'applicazione ti mostra la pagina di autorizzazione ufficiale fornita dal provider del servizio cloud, e l'intero processo di autorizzazione avviene fuori dall'applicazione. Il provider del servizio cloud invia quindi un token di autenticazione all'applicazione dopo l'autorizzazione avvenuta con successo, e quel token viene usato per fare chiamate API.

Un token di autenticazione è una chiave digitale che consente alle applicazioni di terze parti di interagire con l'archiviazione cloud a tuo nome. Il token è memorizzato sul dispositivo nell'archivio di sistema sicuro di Apple (Keychain), che è crittografato a riposo e protetto dal codice di accesso del dispositivo o dal blocco biometrico. Puoi scaricare file dai servizi cloud connessi al dispositivo; quei file vengono inseriti nella directory Documenti dell'app e possono essere rimossi in qualsiasi momento usando il gestore file integrato.

L'applicazione non condivide alcuna informazione dai tuoi account cloud connessi con Everappz, inserzionisti o terze parti. Puoi revocare l'accesso al tuo account cloud in qualsiasi momento aprendo la pagina delle impostazioni dell'account nel browser web.

## Rifiuta il Token di Autenticazione

Per revocare un token di autenticazione, accedi al tuo account cloud in un browser web e naviga alla pagina di sicurezza o delle app connesse. Lì puoi trovare ogni app di terze parti connessa al tuo account cloud e rimuovere qualsiasi di esse se non vuoi più usarla. Le istruzioni dettagliate per gli account Google sono disponibili [qui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puoi anche disconnettere l'account cloud all'interno dell'applicazione stessa — quando lo fai, il token di autenticazione viene immediatamente eliminato dal dispositivo. Se disinstalli l'applicazione dal dispositivo, tutti i dati scaricati e i token di accesso vengono rimossi automaticamente.

## Disconnetti un'Archiviazione Cloud o Cambia Configurazione

- **Accedi alle opzioni di archiviazione cloud** — individua il servizio connesso nella sezione **Archiviazione Cloud** della scheda File.
- **Tocca il pulsante "..."** accanto al titolo del servizio per aprire opzioni aggiuntive:
  - **Rinomina** — cambia il nome del servizio cloud come appare nell'elenco.
  - **Impostazioni** — modifica la configurazione o i dati di autenticazione. A volte potresti dover ri-autorizzare il servizio cloud connesso se il token di autorizzazione è scaduto.
  - **Disconnetti** — interrompe completamente la connessione tra l'app e il servizio cloud. Questo rimuove tutti i video associati a quel servizio dalla tua libreria media, ma li lascia intatti sul server.

## Connetti a un Computer o NAS

Puoi connettere il tuo computer, NAS personale o altro dispositivo di rete usando il protocollo SMB, WebDAV, FTP / FTPS, SFTP, NFS o DLNA. Questo è il modo più semplice per portare una libreria media domestica esistente — che si trovi su un Mac, Windows PC, Synology, QNAP, Apple Time Capsule o WD My Cloud Home — in Evervideo senza copiare nulla.

### Connetti a un Computer Usando SMB

- Tocca **Connetti all'archiviazione cloud → SMB**.
- Inserisci l'indirizzo IP del computer e il nome della cartella condivisa usando il formato `smb://computer-ip-address/shared-folder-name`.
- Scegli la versione del protocollo: **Auto**, **SMB1** o **SMB2**.
- Inserisci il login e la password (se richiesto).
- Tocca **Fatto**.

Se la connessione va a buon fine, la condivisione appare nella sezione Archiviazione Cloud. Un tutorial completo su come connettere il tuo Mac o PC usando SMB è disponibile [qui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Connetti a un NAS Usando WebDAV

Tutti i passaggi sono gli stessi di SMB, tranne per il campo URL. Usa `http://server-name` o `https://server-name` se il server supporta SSL. WebDAV funziona con Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home e qualsiasi altro server con un endpoint WebDAV.

Un tutorial completo su WebDAV è disponibile [qui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Connetti tramite DLNA / UPnP

Condividi una libreria media sul tuo Windows PC o NAS usando il protocollo DLNA / UPnP e accedivi all'interno di Evervideo come descritto [qui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA è ampiamente supportato, ma ti consente solo di riprodurre o scaricare video — non puoi caricare file o creare nuove cartelle su un server DLNA.

### Connetti Usando FTP, FTPS o SFTP

Evervideo supporta anche i protocolli classici di trasferimento file. Per connettere un server via FTP o FTPS, tocca Connetti all'archiviazione cloud → FTP, inserisci l'URL host nella forma `ftp://server-name` (o `ftps://server-name` per una connessione crittografata), fornisci il login e la password, poi tocca Fatto. Per SFTP (SSH File Transfer Protocol), scegli SFTP e fornisci una password o una coppia di chiavi SSH.

### Connetti a una Condivisione NFS

Evervideo include il supporto NFS (Network File System) — utile per host Linux, server BSD e dispositivi NAS che preferiscono esporre le librerie video via NFS invece di SMB. Scegli NFS nel menu Connetti all'archiviazione cloud, inserisci l'indirizzo del server e il percorso esportato, e tocca Fatto.

## Connetti un Plex Media Server

Evervideo può connettersi direttamente a un Plex Media Server e sfogliare le tue librerie di Film, Serie TV e Video Domestici. Tocca Connetti all'archiviazione cloud → Plex, accedi con il tuo account Plex, scegli un server, e la libreria appare accanto ai tuoi servizi cloud. I server Plex sulla stessa rete locale vengono scoperti automaticamente anche nella sezione Dispositivi Disponibili.

## Connetti un Server Jellyfin o Emby

Sia Jellyfin (open-source) che Emby (commerciale) server multimediali funzionano nativamente in Evervideo. Tocca Connetti all'archiviazione cloud → Jellyfin o Emby, inserisci l'URL del server (tipicamente qualcosa come `http://server-ip:8096`) e le credenziali, e la tua libreria è pronta per lo streaming.

## Connetti un Server Subsonic o Navidrome

Evervideo parla l'API Subsonic, il che significa che funziona con Subsonic stesso, Navidrome e ogni altro server compatibile Subsonic — inclusi Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) e Ampache. Tocca Connetti all'archiviazione cloud → Subsonic, inserisci l'URL del server e le credenziali, e la libreria appare nella sezione Archiviazione Cloud.

## Connetti uno Stream RTSP (Telecamere IP, TV Live, IPTV)

Evervideo ha supporto RTSP nativo, così puoi puntarlo su qualsiasi sorgente RTSP — telecamere di sicurezza, telecamere citofoniche, provider IPTV, baby monitor, trasmissioni live — ed Evervideo tirerà e decodificherà lo stream dal vivo. Tocca Link Online → Aggiungi link, incolla l'URL completo (`rtsp://camera-ip:port/stream-path`), fornisci login e password se richiesti, e tocca Fatto.

## Connetti all'Archiviazione Oggetti Compatibile S3

Per i self-hoster e gli utenti avanzati che usano l'archiviazione oggetti cloud, Evervideo include un connettore compatibile S3. Tocca Connetti all'archiviazione cloud → Archiviazione S3, poi inserisci l'URL dell'endpoint, la regione, la chiave di accesso, la chiave segreta e il nome del bucket. Funziona con AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualsiasi altro endpoint S3-API.

## Dispositivi Disponibili

Questa sezione mostra ogni dispositivo sulla rete locale a cui puoi connetterti da Evervideo tramite scoperta Bonjour / mDNS — server Plex, Jellyfin, Emby, Synology, QNAP, router AirPort con drive collegati, Apple Time Capsule e così via. Per stabilire una connessione:

- Scorri alla sezione Dispositivi Disponibili nella scheda File.
- Tocca il dispositivo a cui vuoi connetterti.
- Se necessario, inserisci i tuoi dati di accesso per completare la connessione.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositivi Disponibili Evervideo sulla Rete Locale" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive ti consente di trasferire file in modalità wireless dal computer al dispositivo iOS tramite qualsiasi browser desktop, Finder o File Explorer. Il dispositivo e il computer devono essere sulla stessa rete Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive di Evervideo" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Abilita Wi-Fi Drive

- Nella scheda File, scorri a Archiviazione Cloud → Connetti tramite Wi-Fi per aprire la schermata principale di Wi-Fi Drive.
- (Facoltativo) Imposta un nome utente e una password per il server web integrato.
- Tocca Avvia Wi-Fi Drive.

### Accedi a Wi-Fi Drive dal Computer

- Apri un browser web sul computer (Chrome, Firefox, Safari, ecc.).
- Inserisci l'URL mostrato dall'applicazione.
- Trascina e rilascia file dal computer sulla pagina web — inizieranno il trasferimento al dispositivo iOS.

Puoi anche montare Wi-Fi Drive direttamente in **Finder** su macOS (Vai → Connetti al server…) o File Explorer su Windows (Mappa unità di rete…) e trattare iPhone o iPad come un normale drive di rete.

Le istruzioni dettagliate sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (ora Finder File Sharing su macOS Catalina e versioni successive) ti consente di trasferire file usando un cavo Lightning o USB-C. Connetti il dispositivo, apri Finder su Mac (o iTunes su Windows), trova Evervideo nell'elenco delle app e copia i file nella sua cartella condivisa.

## Connetti un Flash Drive USB o Scheda SD

Collega un drive USB o una scheda SD al tuo iPhone, iPad o Mac tramite l'adattatore da Lightning a USB / USB-C o un lettore di schede. Apri File → File su Questo iPhone → Apri Cartella, naviga fino al drive e seleziona un file video o una cartella. Evervideo riproduce i file direttamente dal drive senza copiarli nell'archiviazione interna — utile per librerie 4K molto grandi.

## Navigazione delle Cartelle nei Depositi Connessi

Tocca qualsiasi servizio cloud connesso per aprire il suo browser di file. Le cartelle mostrano miniature video quando disponibili, e toccare un video avvia immediatamente la riproduzione continuando a fare streaming del resto del file in background.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Naviga Cartelle nei Depositi Connessi" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Accesso Rapido

La sezione Accesso Rapido si trova in cima alla scheda File. Ti offre accesso rapido ai tuoi file e cartelle preferiti e aperti di recente — sia dai servizi cloud che dall'archiviazione sul dispositivo. Ogni volta che apri un file o una cartella dal cloud, viene aggiunto all'elenco Aperti di Recente. Puoi contrassegnare le cartelle profondamente annidate come Preferiti per accedervi rapidamente senza scavare nella struttura delle directory.

{{< cards cols="1">}}
  {{< card title="" subtitle="Link Online Evervideo e Accesso Rapido" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## File in Questa Applicazione

Questa sezione mostra file e cartelle memorizzati nella directory Documenti in sandbox di Evervideo — tutto ciò che hai scaricato dal cloud, trasferito tramite Wi-Fi Drive, copiato tramite Finder File Sharing o importato da un'altra app.

{{< cards cols="1">}}
  {{< card title="" subtitle="File in Questa Applicazione di Evervideo" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Cartella Documenti

La cartella Documenti è la radice di tutto all'interno di File in Questa Applicazione. Puoi creare sottocartelle, rinominare file, spostarli e raggrupparli come preferisci.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Locali Evervideo — Cartella Documenti" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## File su Questo iPhone / iPad / Mac

Questa sezione mostra i video che si trovano sul dispositivo ma in applicazioni diverse. Puoi importarli in Evervideo usando il selettore file di sistema:

- Tocca Apri File… per selezionare file specifici.
- Tocca Apri Cartella… per selezionare un'intera cartella.

Puoi anche usare Connetti una Cartella per creare un collegamento a una cartella sul dispositivo con accesso in lettura / scrittura — perfetto per lavorare con una cartella su iCloud Drive o un drive USB collegato senza copiare nulla.

{{< cards cols="1">}}
  {{< card title="" subtitle="File Evervideo su Questo Dispositivo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Cartelle Speciali

All'interno della scheda File vedrai diverse cartelle speciali che Evervideo crea e usa automaticamente:

- **Download** — ogni file scaricato dal cloud appare qui per impostazione predefinita. Personalizza in Impostazioni → Gestore File → Salva i File Scaricati In.
- **Cache Lettore** — la cache del lettore media. Per impostazione predefinita il lettore scarica i video successivi per una riproduzione fluida. Puoi disabilitare la cache nelle impostazioni dell'app o semplicemente eliminare questa cartella.
- **iCloud** — i file in questa cartella si sincronizzano su tutti i tuoi dispositivi connessi allo stesso account iCloud.
- **Cartelle Offline** — quando contrassegni una cartella, playlist, album o genere come disponibile offline, i file vengono scaricati in questa cartella.

## Barra degli Strumenti Superiore

La barra degli strumenti superiore, situata sotto la barra di navigazione, offre diverse azioni che puoi mostrare o nascondere con un gesto di scorrimento verso il basso:

- **Cerca** — esegui una ricerca nella cartella o nella sezione corrente.
- **Continua Riproduzione** — se abilitato nelle impostazioni, ripristina la coda del lettore e l'ultima posizione video per la cartella corrente.
- **Riproduci Tutto** — scansiona la cartella corrente e le sue sottocartelle e aggiunge file alla coda del lettore.
- **Riproduci in Ordine Casuale** — come Riproduci Tutto, ma mescola prima di aggiungere.

## Opzioni Cartella

Quando apri una cartella, tocca il pulsante **"..."** nell'angolo in alto a destra per queste azioni:

- **Seleziona** — attiva la modalità di selezione file.
- **Nuova Cartella** — crea una nuova cartella all'interno della cartella corrente.
- **Abilita Modalità Offline** — attiva la sincronizzazione offline per la cartella corrente. I nuovi file aggiunti online vengono scaricati automaticamente.
- **Carica File** — carica file dal dispositivo nella cartella online.
- **Cerca** — cerca all'interno della cartella.
- **Ordina** — ordina i file per nome, dimensione, data di modifica o metadati.
- **Vista Griglia / Lista** — passa tra la vista tabella e la vista miniatura. La vista miniatura mostra grandi anteprime dei poster video.

## Modalità Selezione

Tocca **"..."** nell'angolo in alto a destra e scegli **Seleziona** per entrare in modalità selezione. Le caselle di controllo appaiono accanto a ogni file e cartella. Tocca per selezionare uno o più elementi, poi esegui azioni batch: Riproduci Dopo, Riproduci Più Tardi, Aggiungi alla Libreria Media, Aggiungi a una Playlist, Copia, Carica, Sposta, Rinomina o Elimina.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modalità Selezione Evervideo nel Gestore File" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Se preferisci trattare l'archiviazione cloud connessa come di sola lettura (per prevenire eliminazioni accidentali), abilita Impostazioni → Gestore File → Modifica File Online → Disattivato per nascondere tutte le operazioni distruttive dall'interfaccia.

## Azioni sui File

Tocca l'icona **"..."** vicino al titolo di un file per rivelare il menu delle azioni:

- **Riproduci Dopo** — inserisci il file in cima alla coda del lettore.
- **Riproduci Più Tardi** — aggiungi il file in fondo alla coda del lettore.
- **Aggiungi alla Libreria Media** — incorpora il file nella libreria media, organizzata per Album e Genere.
- **Aggiungi a una Playlist** — aggiungi il file a una playlist esistente o creane una nuova.
- **Modifica Tag** — apri l'editor di tag integrato per modificare i metadati. Per i file online, il file viene temporaneamente scaricato, modificato e poi ricaricato dopo la conferma.
- **Aggiungi ai Preferiti** — aggiungi il file all'elenco dei preferiti per un accesso rapido.
- **Scarica** — scarica il file o la cartella sul dispositivo per uso offline.
- **Rinomina** — rinomina il file direttamente sull'archiviazione remota.
- **Sposta** — sposta il file in una cartella diversa all'interno della tua archiviazione cloud.
- **Aggiungi all'Archivio** — raggruppa il file in un singolo file ZIP (funzione Premium).
- **Apri in** — esporta il file in un'altra app compatibile tramite il foglio di condivisione di sistema.
- **Elimina** — rimuovi permanentemente il file. **Questa azione non può essere annullata.**

## Azioni sulle Cartelle

Per ogni cartella nella tua archiviazione cloud, sono disponibili molte azioni toccando l'icona **"..."** accanto al titolo della cartella.

- **Riproduci Tutto** — sostituisce la coda del lettore corrente con ogni video nella cartella.
- **Riproduci Dopo / Riproduci Più Tardi** — aggiungi l'intera cartella alla coda.
- **Aggiungi alla Libreria Media** — incorpora il contenuto della cartella nella libreria media.
- **Aggiungi alla Playlist** — aggiungi l'intera cartella a una playlist.
- **Aggiungi ai Preferiti** — aggiungi la cartella ai tuoi preferiti.
- **Abilita Modalità Offline** — oltre a un semplice download, questo monitora continuamente la cartella per nuovi file e li scarica automaticamente man mano che appaiono online.
- **Scarica** — scarica tutto il contenuto della cartella sul dispositivo per l'accesso offline.
- **Rinomina / Sposta** — rinomina o sposta la cartella sull'archiviazione remota.
- **Aggiungi all'Archivio** — raggruppa il contenuto della cartella in un file ZIP (funzione Premium).
- **Elimina** — rimuovi permanentemente la cartella e il suo contenuto. **Questa azione non può essere annullata.**

## Coda di Trasferimento

Nell'angolo in alto a destra della scheda File c'è un pulsante **Transfer** (un'icona con frecce rotanti). Toccalo per aprire la Coda di Trasferimento — un elenco di ogni download e caricamento attivo da tutte le tue sorgenti, con avanzamento in tempo reale, velocità e ETA per file.

{{< cards cols="1">}}
  {{< card title="" subtitle="Coda di Trasferimento File Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Puoi mettere in pausa, riprendere, riprovare i trasferimenti falliti, riorganizzare gli elementi per dare priorità a download specifici o cancellarli singolarmente. Puoi anche regolare la velocità della coda di trasferimento (numero massimo di attività parallele), il tipo di rete (solo Wi-Fi o Wi-Fi + Cellulare) e i trasferimenti in background in Impostazioni → Gestore File.

{{< cards cols="1">}}
  {{< card title="" subtitle="Azioni Evervideo sulla Coda di Trasferimento File" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Modalità Offline e Cartelle Offline Sincronizzate

La modalità offline è una funzione utile che ti consente di guardare i tuoi video preferiti anche quando non sei connesso a Internet. Quando abiliti la modalità offline per qualsiasi cartella, playlist, album o genere, tutti i file all'interno di quella raccolta vengono scaricati automaticamente sul dispositivo per la riproduzione offline. Appaiono nella sezione Cartelle Offline.

Quando aggiungi nuovi file al server remoto, vengono scaricati automaticamente anche loro — così la tua raccolta offline rimane aggiornata senza che tu faccia nulla. Per sincronizzare manualmente, tocca i tre puntini nell'angolo in alto a destra di una cartella offline e seleziona Sincronizza.

Puoi regolare il timeout di sincronizzazione in Impostazioni → Gestore File → Cartelle Offline Sincronizzate → Intervallo di Tempo.

Le istruzioni dettagliate sono disponibili [qui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalizzazione

In Impostazioni → Personalizzazione puoi configurare come viene presentata la scheda File:

- **Stile Schermata File** — Menu Semplice (mostra direttamente l'elenco delle cartelle) o Menu Raggruppato (raggruppa il contenuto per categoria — Accesso Rapido, Cartelle Speciali, Archiviazione Cloud, ecc.).
