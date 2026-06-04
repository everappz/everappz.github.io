---
title: "Connessioni"
date: 2020-02-01
description: "Scopri come connettere servizi cloud e dispositivi NAS a Flacbox. Fai streaming di musica ad alta risoluzione da iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk e altro. Usa SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing e drive flash USB."
keywords: [
  "configurazione cloud Flacbox", "connettere Google Drive a Flacbox", "streaming musica SMB",
  "lettore iOS WebDAV", "app musica DLNA", "streaming audio NAS", "Wi-Fi Drive iPhone",
  "trasferire file su iPhone", "Flacbox iTunes File Sharing", "connettere NAS a iPhone",
  "app musica Synology Drive", "app musica QNAP", "app musica Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "app musica scrobbling Last.fm",
  "musica iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["guida", "flacbox", "connessioni", "cloud", "NAS"]
readingTime: 12
---


In questa schermata puoi connettere ogni sorgente che contiene la tua musica. Puoi integrare i servizi cloud più diffusi come Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive e molti altri, oltre al tuo Mac, PC o NAS tramite protocolli standard. Che la tua collezione si trovi su un servizio streaming-friendly come Dropbox o su un NAS personale come Synology, QNAP, Buffalo, Apple Time Capsule o WD My Cloud Home, Flacbox si connette a tutto da un'unica schermata.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Connessioni di Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Connessione a Cloud Storage

- Apri la scheda **Connessioni**.
- Seleziona **Connettere a cloud storage** dal menu.
- Scegli un servizio di cloud storage dall'elenco.
- Inserisci le credenziali nella pagina di autorizzazione ufficiale fornita dal provider cloud, poi tocca **Fatto**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Aggiunta di un Servizio Cloud Storage" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Se riscontri problemi, verifica la connessione internet e login / password. Nella versione Premium puoi aggiungere un numero illimitato di servizi; la versione gratuita supporta fino a tre.

## Servizi Cloud Storage, Server Media e Protocolli Supportati

Flacbox supporta una gamma eccezionalmente ampia di sorgenti per la tua musica. Tutto quanto segue funziona da un'unica schermata **Connettere a cloud storage**.

**Cloud storage personale:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Server self-hosted:** Plex · Jellyfin · Emby · Subsonic (e ogni server compatibile — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (e ownCloud tramite l'API condivisa) · Synology Drive · QNAP.

**Protocolli NAS e condivisione file:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, autenticazione con password o chiave pubblica) · NFS · DLNA / UPnP (riproduzione e download).

**Object storage compatibile S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualsiasi altro servizio che espone un endpoint S3-API.

**Scoperta rete locale:** La sezione Dispositivi disponibili elenca automaticamente ogni servizio Bonjour / mDNS sulla tua rete Wi-Fi così puoi toccare per connetterti senza digitare indirizzi IP.

Ogni connessione utilizza l'**SDK ufficiale o il protocollo aperto** del servizio, con autorizzazione basata su OAuth dove supportata. Puoi connettere più account dello stesso servizio (ad esempio due account Google Drive, un Dropbox personale e uno di lavoro, o sia un server Plex che uno Jellyfin) e sfogliarli fianco a fianco nella schermata Connessioni.

## Sicurezza e Privacy

Utilizziamo solo SDK ufficiali e connessioni sicure per interagire con i servizi cloud connessi. Il tuo login e la tua password non sono accessibili all'applicazione — tutti i trasferimenti sono cifrati con TLS.

Quando inserisci login e password, l'applicazione mostra la pagina di autorizzazione ufficiale fornita dal provider del servizio cloud, e l'intero processo di autorizzazione avviene al di fuori dell'applicazione. Il provider del servizio cloud invia poi un auth-token all'applicazione dopo l'autorizzazione riuscita, e quel token viene usato per effettuare chiamate API.

Un auth-token è una chiave digitale che consente ad applicazioni di terze parti di interagire con il cloud storage per tuo conto. Il token è archiviato sul tuo dispositivo nell'archiviazione sicura di sistema di Apple (Keychain), che è cifrata a riposo e protetta dal codice di accesso del dispositivo o dal blocco biometrico. Puoi scaricare file dai servizi cloud connessi sul tuo dispositivo; quei file vengono collocati nella directory Documenti dell'app e possono essere rimossi in qualsiasi momento usando il gestore file integrato.

L'applicazione non condivide alcuna informazione dai tuoi account cloud connessi con Everappz, inserzionisti o terze parti. Puoi revocare l'accesso al tuo account cloud in qualsiasi momento aprendo la pagina delle impostazioni account nel browser web.

## Revocare un Auth-Token

Per revocare un auth-token, accedi al tuo account cloud nel browser web e vai alla pagina sicurezza o app connesse. Lì puoi trovare ogni app di terze parti connessa al tuo account cloud e rimuovere quelle che non vuoi più usare. Le istruzioni dettagliate per gli account Google sono disponibili [qui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puoi anche disconnettere l'account cloud dall'interno dell'applicazione — quando lo fai, l'auth-token viene immediatamente eliminato dal tuo dispositivo. Se disinstalli l'applicazione dal dispositivo, tutti i dati scaricati e i token di accesso vengono rimossi automaticamente.

## Disconnettere un Cloud Storage o Modificare la Configurazione

- **Accedi alle opzioni del cloud storage** — individua il servizio connesso nella schermata **Connessioni**.
- **Tocca il pulsante "..."** accanto al titolo del servizio per aprire le opzioni aggiuntive:
  - **Rinomina** — cambia il nome del servizio cloud come appare nel tuo elenco.
  - **Impostazioni** — modifica la configurazione o i dati di autenticazione. A volte potrebbe essere necessario ri-autorizzare il servizio cloud connesso se il token di autorizzazione è scaduto.
  - **Disconnettere** — interrompe completamente la connessione tra l'app e il servizio cloud. Rimuove tutti i brani associati a quel servizio dalla libreria musicale dell'app, ma li lascia intatti sul server.

## Connessione a un Computer o NAS

Puoi anche connettere il tuo computer, NAS personale o altri dispositivi di rete usando i protocolli SMB, DLNA o WebDAV. Questo è il modo più semplice per portare una libreria musicale domestica esistente — su Mac, Windows PC, Synology, o NAS — in Flacbox senza copiare nulla.

## Connessione a un Computer Tramite SMB

- Tocca **Connettere a cloud storage → SMB**.
- Inserisci l'indirizzo IP del computer e il nome della cartella condivisa nel campo URL usando il formato `smb://computer-ip-address/shared-folder-name`.
- Scegli la versione del protocollo: **Auto**, **SMB1** o **SMB2**.
- Inserisci login e password (se richiesti).
- Tocca **Fatto**.

Se la connessione ha successo, vedrai lo storage connesso nella sezione **Cloud Storage**. Un tutorial completo su come connettere Mac o PC tramite SMB è disponibile [qui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connessione a un NAS Tramite WebDAV

Tutti i passaggi sono gli stessi di SMB, tranne per il campo URL. L'URL deve essere nel formato `http://server-name` o `https://server-name` se il server supporta SSL. WebDAV funziona con **Synology, QNAP, Nextcloud, ownCloud,** e molti altri server — ovunque sia disponibile un endpoint WebDAV.

Un tutorial completo su come connettere un NAS tramite WebDAV è disponibile [qui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Connessione a un Computer o NAS Tramite DLNA

Puoi anche condividere una libreria musicale sul tuo PC Windows o NAS personale usando il protocollo DLNA / UPnP e accedere a quella libreria nell'app come descritto [qui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA è un protocollo popolare e ampiamente supportato, ma consente solo di riprodurre o scaricare musica — non puoi caricare file o creare nuove cartelle su un server DLNA.

## Connessione a un NAS o Server Tramite FTP, FTPS o SFTP

Flacbox supporta anche i classici protocolli di trasferimento file. Per connettere un server via FTP o FTPS, tocca **Connettere a cloud storage → FTP**, inserisci l'URL host nella forma `ftp://server-name` (o `ftps://server-name` per una connessione cifrata), fornisci login e password, poi tocca **Fatto**. Per **SFTP** (SSH File Transfer Protocol), scegli **SFTP** e fornisci una password o una coppia di chiavi SSH. Entrambi funzionano con dispositivi NAS, host Linux e qualsiasi server con un daemon FTP / FTPS / SSH.

## Connessione a una Condivisione NFS

Flacbox include il supporto **NFS** (Network File System) — utile per host Linux, server BSD e dispositivi NAS che preferiscono esporre le librerie musicali via NFS invece di SMB. Scegli **NFS** nel menu **Connettere a cloud storage**, inserisci l'indirizzo del server e il percorso esportato, e tocca **Fatto**.

## Connessione a un Plex Media Server

Flacbox può connettersi direttamente a un Plex Media Server e sfogliare la libreria musicale per Artisti, Album, Generi e Playlist. Tocca **Connettere a cloud storage → Plex**, accedi con il tuo account Plex, scegli un server, e la libreria appare accanto ai tuoi servizi cloud. I server Plex sulla stessa rete locale vengono scoperti automaticamente anche nella sezione **Dispositivi disponibili**.

## Connessione a un Server Jellyfin o Emby

Sia **Jellyfin** (open-source) che **Emby** (commerciale) funzionano nativamente in Flacbox. Tocca **Connettere a cloud storage → Jellyfin** o **Emby**, inserisci l'URL del server (qualcosa come `http://server-ip:8096`) e le credenziali, e la tua libreria musicale è pronta per lo streaming. Come con Plex, le librerie sulla rete locale vengono elencate automaticamente in **Dispositivi disponibili**.

## Connessione a un Server Subsonic o Navidrome

Flacbox utilizza l'API Subsonic, il che significa che funziona con **Subsonic** stesso, **Navidrome** e ogni altro server compatibile con Subsonic — inclusi Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Tocca **Connettere a cloud storage → Subsonic**, inserisci l'URL del server e le credenziali, e la libreria appare nella schermata Connessioni.

## Connessione a Object Storage Compatibile S3

Flacbox include un connettore compatibile con S3. Tocca **Connettere a cloud storage → S3 storage**, quindi inserisci l'URL dell'endpoint, la regione, la chiave di accesso, la chiave segreta e il nome del bucket. Funziona con AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces e qualsiasi altro servizio che espone un endpoint S3-API.

## Dispositivi Disponibili

Questa sezione mostra ogni dispositivo sulla tua rete locale a cui puoi connetterti da Flacbox tramite il rilevamento Bonjour. Per stabilire una connessione, segui questi passaggi:

- Apri l'app e vai alla sezione **Dispositivi disponibili** sotto Connessioni.
- Tocca il dispositivo a cui vuoi connetterti.
- Se necessario, inserisci i tuoi dati di login per completare la connessione.

Questo è il modo più veloce per scoprire una condivisione SMB, WebDAV o DLNA sulla tua rete domestica senza digitare manualmente gli indirizzi IP.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dispositivi Disponibili sulla Rete Locale" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive è una tecnologia comoda che consente trasferimenti di file wireless dal tuo computer al dispositivo iOS tramite qualsiasi browser desktop. Per usare questa funzione in modo efficace, assicurati che il tuo dispositivo e il computer siano connessi alla stessa rete Wi-Fi. Ecco una guida passo-passo su come usare Wi-Fi Drive.

### Abilitare Wi-Fi Drive

- Apri l'applicazione e vai alla scheda **Connessioni**.
- Seleziona **Connettiti tramite Wi-Fi** per accedere alla schermata principale di Wi-Fi Drive.
- (Opzionale) Imposta un nome utente e una password per il server web integrato per proteggere l'accesso.
- Tocca **Avvia Wi-Fi Drive** per abilitare Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Accedere a Wi-Fi Drive dal Computer

- Sul tuo computer (desktop o laptop), apri un browser web (come Chrome, Firefox o Safari).
- Nella barra degli indirizzi del browser, inserisci l'URL fornito dall'applicazione.

### Trasferire File in Modalità Wireless

Una volta che la pagina web corrispondente al tuo dispositivo iOS si apre nel browser, puoi facilmente trascinare e rilasciare file dal computer sulla pagina web. I file rilasciati inizieranno a trasferirsi sul dispositivo iOS e saranno accessibili all'interno di Flacbox.

Puoi anche montare Wi-Fi Drive direttamente nel Finder su macOS (Vai → Connetti al server…) o in Esplora file su Windows (Connetti unità di rete…) e trattare iPhone o iPad come un normale drive di rete.

Le istruzioni dettagliate su come trasferire file in modo wireless usando Wi-Fi Drive sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (ora Finder File Sharing su macOS Catalina e versioni successive) è un altro modo per trasferire file da un computer a un dispositivo usando un cavo Lightning o USB-C.

- Connetti il dispositivo al computer usando un cavo ed esegui **Finder** su Mac (o **iTunes** su Windows).
- Apri **Posizioni → Il tuo dispositivo connesso → File** e trova l'app Flacbox.
- Tocca l'icona dell'app per vedere tutte le cartelle condivise.
- Copia i file dal computer alla cartella condivisa sul dispositivo usando il trascinamento.

Le istruzioni dettagliate su come usare Finder File Sharing sono disponibili [qui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connessione di un Drive Flash USB

Se hai una scheda SD o un drive USB, puoi connetterlo usando un adattatore Lightning-USB / lettore SD o un drive USB-C (su iPad e iPhone 15 / 16 / 17 / Pro). L'app supporta lettori di schede certificati Apple e iXpand Flash Drive. Con un iXpand Flash Drive, inseriscilo nella porta Lightning e apri l'applicazione — vedrai un messaggio di dispositivo esterno connesso e le informazioni sul dispositivo. Tocca l'icona del drive flash per accedere alla cartella musicale e tocca qualsiasi file audio per iniziare la riproduzione.

Le istruzioni dettagliate su come connettere un drive flash USB a iPhone e ascoltare musica o gestire i file sono disponibili [qui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestore File

Una volta connesso un servizio cloud storage, tocca la sua icona per visualizzare tutti i file e le cartelle disponibili. Puoi usare il gestore file integrato per lavorare con questi file — scaricare, rinominare, spostare, caricare, eliminare e altro ancora. Quando avvii un download, il file appare nella coda di trasferimento. Per aprire la coda di trasferimento, vai alla scheda File Locali e tocca l'icona delle frecce rotanti nell'angolo in alto a sinistra. Tutti i file e le cartelle scaricati sono disponibili nella sezione File Locali.

## Barra degli Strumenti Superiore

La barra degli strumenti superiore, situata convenientemente sotto la barra di navigazione, offre diverse azioni utili per un accesso facile. Puoi mostrarla o nasconderla con un semplice gesto di scorrimento verso il basso.

- **Cerca** — esegui una ricerca rapida nella directory corrente, rendendo facile individuare file o cartelle specifici.
- **Continua Riproduzione** — se abilitata nelle impostazioni dell'applicazione, ripristina la coda del lettore audio e l'ultima posizione multimediale per la cartella corrente.
- **Riproduci Tutto** — scansiona la cartella corrente e le sottocartelle, poi aggiunge tutti i file audio trovati a una nuova coda del lettore.
- **Mescola Tutto** — come Riproduci Tutto, ma mescola i file prima di aggiungerli alla coda del lettore audio.

## Opzioni Cartella

Quando apri una cartella, troverai un utile set di azioni disponibili toccando il pulsante **"..."** nell'angolo in alto a destra.

- **Selezionare** — attiva la modalità di selezione file. Ti permette di scegliere uno o più file nella cartella ed eseguire azioni sull'intera selezione.
- **Nuova Cartella** — crea una nuova cartella nella cartella corrente.
- **Abilitare la modalità offline** — attiva la modalità offline per la cartella corrente. La modalità offline va oltre il semplice download: monitora attivamente la cartella per le modifiche.
- **Carica File** — carica file dal dispositivo alla cartella online.
- **Cerca** — cerca file specifici nella cartella corrente.
- **Ordina** — ordina i file per nome, dimensione, data di modifica o per metadati.
- **Vista Griglia / Elenco** — passa dalla vista tabella alla vista miniature.

## Modifica File Online

Quando devi gestire più file nel cloud storage, usa la **Modalità Selezione** per semplificare le azioni:

- **Attiva Modalità Selezione** — tocca il pulsante **"..."** nell'angolo in alto a destra e scegli **Selezionare**.
- **Scegli File** — le caselle di controllo appaiono accanto a ogni file e cartella. Tocca per selezionare uno o più elementi.
- **Esegui Azioni** — una volta selezionati i file o le cartelle, avrai accesso a Riproduci Successivo, Riproduci Dopo, Aggiungi alla Libreria Musicale, Aggiungi a una Playlist, Copia, Carica, Sposta, Rinomina ed Elimina.

Se preferisci trattare il cloud storage connesso come sola lettura (per prevenire eliminazioni accidentali), abilita Impostazioni → Gestore File → Modificare File Online → Disattivato per nascondere tutte le operazioni distruttive dall'interfaccia.

## Azioni File

Tocca l'icona **"..."** vicino al titolo di un file per vedere il suo menu di azioni:

- **Riproduci Successivo** — inserisce il file in cima alla coda del lettore.
- **Riproduci Dopo** — aggiunge il file in fondo alla coda del lettore.
- **Aggiungi alla Libreria Musicale** — incorpora il file nella libreria musicale, organizzato per artista, album, genere o compositore.
- **Aggiungi a una Playlist** — aggiunge il file a una playlist esistente o ne crea una nuova.
- **Modificare i tag audio** — apre l'editor di tag integrato per modificare i metadati.
- **Aggiungi ai Preferiti** — aggiunge il file ai preferiti per un accesso rapido.
- **Scaricare** — scarica il file o la cartella sul dispositivo per uso offline.
- **Rinomina** — rinomina il file direttamente sullo storage remoto.
- **Sposta** — sposta il file in un'altra cartella nel cloud storage.
- **Apri In** — esporta il file in un'altra app compatibile.
- **Eliminare** — rimuove definitivamente il file dal cloud storage. **Questa azione non può essere annullata.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Altre azioni per un File nel Cloud Storage Connesso" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Se l'elenco delle azioni supera lo spazio disponibile sullo schermo, scorri semplicemente verso il basso nel menu azioni per accedere alle opzioni aggiuntive.

## Azioni Cartella

Per ogni cartella nel cloud storage, hai una vasta gamma di azioni disponibili toccando l'icona **"..."** accanto al titolo della cartella.

- **Riproduci Tutto** — sostituisce la coda del lettore corrente con ogni elemento nella cartella selezionata.
- **Riproduci Successivo** — aggiunge l'intera cartella in cima alla coda del lettore.
- **Riproduci Dopo** — aggiunge il contenuto della cartella in fondo alla coda del lettore.
- **Aggiungi alla Libreria Musicale** — incorpora il contenuto della cartella nella libreria musicale.
- **Aggiungi alla Playlist** — aggiunge l'intera cartella a una playlist.
- **Aggiungi ai Preferiti** — aggiunge la cartella ai preferiti per un accesso rapido.
- **Abilitare la modalità offline** — oltre a un semplice download, monitora continuamente la cartella per nuovi file e li scarica automaticamente man mano che appaiono online.
- **Scaricare** — scarica tutto il contenuto della cartella sul dispositivo per l'accesso offline.
- **Rinomina** — rinomina la cartella direttamente sullo storage remoto.
- **Sposta** — sposta la cartella in un'altra posizione nel cloud storage.
- **Archivio (ZIP)** — raggruppa il contenuto della cartella in un singolo file ZIP (funzione Premium).
- **Eliminare** — rimuove definitivamente la cartella e il suo contenuto dal cloud storage. **Questa azione non può essere annullata.**

## Accesso Rapido

La sezione Accesso Rapido è nella parte superiore dello schermo. Ti dà accesso rapido ai file e alle cartelle preferiti e aperti di recente dai servizi cloud connessi. Ogni volta che apri un file o una cartella dal cloud, viene aggiunto all'elenco Aperti di Recente. Per cancellare questo elenco, apri Recenti, tocca il pulsante Altre azioni e scegli Elimina elenco.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Link Online e Accesso Rapido" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Altri Servizi

Questa sezione mostra funzionalità extra che migliorano la tua esperienza. Attualmente, l'app supporta lo scrobbling **Last.fm** — quando connessa, le statistiche di riproduzione vengono inviate automaticamente al tuo account Last.fm. Le istruzioni di configurazione dettagliate sono disponibili [qui](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Connessione Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
