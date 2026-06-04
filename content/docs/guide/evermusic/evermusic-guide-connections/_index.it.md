---
title: "Connessioni"
date: 2020-01-01
description: "Scopri come collegare servizi cloud, computer, dispositivi NAS e gestire i tuoi file musicali usando Evermusic. Guida passo dopo passo per Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing e altro ancora."
keywords: [
  "Evermusic", "lettore musicale cloud", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "connettere storage cloud", "trasferimento musica iPhone", "gestore file iOS"
]
tags: ["evermusic", "guida", "connessioni"]
readingTime: 11
---


Nella schermata Connessioni puoi collegare ogni sorgente che contiene la tua musica — servizi cloud popolari, server multimediali self-hosted, il tuo Mac o PC, un NAS personale, Apple Time Capsule, WD My Cloud Home, persino un flash drive USB — e usarli tutti da un'unica interfaccia unificata. Connessioni è anche il luogo in cui configuri l'Accesso Rapido a cartelle cloud profondamente annidate e dove autentichi Last.fm per lo scrobbling.

La schermata è divisa in sezioni chiaramente etichettate, così si scala da un singolo account iCloud Drive a una libreria distribuita su più cloud e dispositivi NAS: Accesso Rapido in alto (le tue cartelle cloud preferite), Archiviazione cloud (gli account che hai aggiunto), Rete locale (dispositivi scoperti da Bonjour), Computer (Wi-Fi Drive, iTunes File Sharing, SMB), Accessori esterni (flash drive USB collegati) e Altri servizi (Last.fm e simili).

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Connessioni di Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Connettiti allo storage cloud

- Apri la scheda Connessioni.
- Seleziona Connetti allo storage cloud dal menu.
- Scegli un servizio di storage cloud dall'elenco.
- Accedi nella pagina di autorizzazione ufficiale del provider (Evermusic non vede mai la tua password).
- Tocca Fine.

{{< cards cols="1">}}
  {{< card title="" subtitle="Selettore Provider di Archiviazione Cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Se riscontri problemi, verifica la tua connessione internet e le credenziali di accesso, e assicurati che l'autenticazione a due fattori sia configurata correttamente per quel servizio.  
Nella versione Premium dell'app puoi aggiungere un numero illimitato di servizi. Gli utenti gratuiti possono connettere un singolo account cloud alla volta.

## Servizi di storage cloud supportati

Evermusic supporta la gamma completa di servizi cloud e self-hosted popolari. Gli utenti gratuiti ottengono lo stesso catalogo di provider ma con il limite di un account; Premium sblocca account illimitati e rimuove la maggior parte degli altri limiti.

- **Account cloud personali:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Server self-hosted e librerie multimediali:** Plex · Jellyfin · Emby · Subsonic (e ogni server compatibile con Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (e Owncloud, tramite l'API condivisa) · Synology Drive · QNAP.
- **NAS e protocolli di condivisione file:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (autenticazione con password o chiave pubblica), NFS e DLNA (sola lettura — riproduzione e download).
- **Object storage compatibile S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage, o qualsiasi endpoint S3-API.
- **Rilevamento della rete locale:** la sezione Dispositivi disponibili elenca automaticamente qualsiasi dispositivo sulla tua Wi-Fi che si pubblicizza tramite Bonjour / mDNS — server Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, router AirPort con unità collegate e così via.

## Sicurezza e privacy

Utilizziamo solo SDK ufficiali e connessioni sicure per interagire con i servizi cloud collegati. Il tuo login e la tua password non sono disponibili per l'applicazione. Tutte le richieste dall'applicazione al servizio cloud sono crittografate.

Quando inserisci login e password, l'applicazione ti mostra la pagina di autorizzazione ufficiale fornita dal provider del servizio cloud e tutto il processo di autorizzazione avviene al di fuori dell'applicazione. Il provider del servizio cloud invia un token di autenticazione all'applicazione dopo l'autorizzazione riuscita e quel token viene utilizzato per effettuare chiamate API.

Il token di autenticazione è una chiave digitale che consente ad applicazioni di terze parti di interagire con lo storage cloud. Il token di autenticazione è memorizzato sul tuo dispositivo in un archivio di sistema sicuro chiamato Keychain. Puoi scaricare i file dal servizio cloud collegato al dispositivo e quei file saranno collocati nella directory "Documents" dell'app. Puoi rimuovere quei file in qualsiasi momento usando il gestore file integrato.

L'applicazione non condivide alcuna informazione dall'account cloud collegato. Puoi revocare l'accesso al tuo account cloud in qualsiasi momento aprendo la pagina delle impostazioni dell'account sul tuo browser web.

## Rifiuta il token di autenticazione

Accedi al tuo account sul browser web e naviga alla pagina delle impostazioni. Lì puoi trovare tutte le app di terze parti che sono collegate al tuo account cloud e rimuovere quelle che non vuoi più utilizzare. Istruzioni dettagliate disponibili [qui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puoi anche disconnettere gli account cloud collegati nell'applicazione e il token di autenticazione verrà rimosso anche dal tuo dispositivo. Se rimuovi l'applicazione dal tuo dispositivo, tutti i dati scaricati e i token di accesso verranno rimossi.

## Disconnetti uno storage cloud o modifica la configurazione

- Accedi alle opzioni di archiviazione cloud: prima, individua l'archiviazione cloud che desideri gestire nell'interfaccia dell'app.
- Tocca il pulsante '...': accanto al titolo del servizio, vedrai un pulsante '...'. Toccalo per accedere alle opzioni aggiuntive.
  - **Rinomina**: se vuoi cambiare il nome del servizio cloud come appare nel tuo elenco, seleziona 'Rinomina.'
  - **Impostazioni**: per modificare la configurazione o i dati di autenticazione del servizio cloud, scegli 'Impostazioni.' A volte potrebbe essere necessario riautorizzare il servizio cloud collegato se il token di autorizzazione è scaduto.
  - **Disconnetti**: se desideri interrompere completamente la connessione tra l'app e il servizio cloud, seleziona 'Disconnetti.' Tieni presente che la scelta di questa opzione rimuoverà tutte le canzoni associate a questo servizio cloud dalla libreria musicale dell'app, ma rimarranno sul server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Altre azioni per Archiviazione Cloud Collegata" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Connetti al Computer o NAS

Puoi anche collegare il tuo computer, NAS personale o altri dispositivi di rete usando il protocollo SMB, DLNA o WebDAV.

## Connetti al computer usando SMB

- Tocca "Connetti allo storage cloud" → SMB.
- Inserisci l'indirizzo IP del computer e il nome della cartella condivisa nel campo URL usando il formato smb://computer-ip-address/shared-folder-name
- Scegli la versione del protocollo: Auto, SMB1, SMB2
- Inserisci login e password (se richiesto)
- Tocca "Fine".

Se la connessione ha successo vedrai lo storage collegato nella sezione "Archiviazione cloud".  
Un tutorial completo su come connettere il tuo MAC o PC usando SMB è disponibile [qui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Impostazioni Connessione SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Connetti al NAS usando WebDAV

Tutti i passaggi sono gli stessi tranne per il campo URL.  
L'URL deve essere nel formato http://server-name, o https://server-name se il server supporta SSL.
Un tutorial completo su come connettere un NAS usando il protocollo WebDAV è disponibile [qui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Impostazioni Connessione WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Connetti al Computer o NAS usando DLNA

Puoi anche condividere una libreria musicale situata sul tuo PC Windows o NAS personale usando il protocollo DLNA e accedere a quella libreria nell'app come descritto [qui](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA è un protocollo popolare e ampiamente usato, ma ti permette solo di riprodurre o scaricare musica. Non puoi caricare file o creare nuove cartelle sul server.

{{< cards cols="1">}}
  {{< card title="" subtitle="Impostazioni Connessione DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dispositivi disponibili

Questa sezione mostra tutti i dispositivi nella tua rete locale a cui puoi connetterti tramite l'applicazione.  
Per stabilire una connessione con un dispositivo, segui questi passaggi:

- Apri l'app e vai alla sezione "Dispositivi disponibili".
- Tocca il dispositivo a cui vuoi connetterti dall'elenco.
- Se necessario, inserisci le tue credenziali di accesso per completare la connessione.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositivi Disponibili sulla Rete Locale" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive è una tecnologia conveniente che consente trasferimenti di file wireless dal tuo computer al tuo dispositivo iOS tramite un browser desktop.  
Per utilizzare questa funzione efficacemente, assicurati che il tuo dispositivo e il computer siano connessi alla stessa rete Wi-Fi.  
Ecco una guida passo dopo passo su come usare Wi-Fi Drive.

## Abilita Wi-Fi Drive

- Apri l'applicazione e vai alla scheda "Connessioni".
- Seleziona "Connetti tramite Wi-Fi" per accedere alla schermata principale di Wi-Fi Drive.
- Tocca "Avvia Wi-Fi Drive" per abilitare Wi-Fi Drive.

## Accedi a Wi-Fi Drive dal tuo Computer

- Sul tuo computer (desktop o laptop), apri un browser web (come Chrome, Firefox o Safari).
- Nella barra degli indirizzi del browser, inserisci l'URL fornito dall'applicazione.

## Trasferisci File in Wireless

Una volta che la pagina web corrispondente al tuo dispositivo iOS si apre nel browser, puoi facilmente trascinare e rilasciare i file dal tuo computer sulla pagina web.  
I file che trascini e rilasci inizieranno a trasferirsi sul tuo dispositivo iOS e saranno accessibili all'interno dell'applicazione.

{{< cards cols="1">}}
  {{< card title="" subtitle="Impostazioni Server Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Istruzioni dettagliate su come trasferire file in modalità wireless usando WiFi-Drive sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing è un'altra tecnologia che ti permette di trasferire file dal computer al dispositivo usando l'app Finder sul Mac e il cavo lightning.  
- Collega semplicemente un dispositivo al computer usando un cavo e avvia l'app Finder sul tuo Mac.
- Apri "Posizioni" → "Il tuo Dispositivo Connesso" → "File" → e trova l'app Evermusic.
- Tocca l'icona dell'app per vedere tutte le cartelle condivise.
- Copia i file dal computer alla cartella condivisa sul dispositivo usando drag-and-drop.

Istruzioni dettagliate su come usare iTunes file sharing disponibili [qui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing su Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Connetti una flash drive USB

Se hai una scheda SD, puoi collegarla usando un lettore di schede lightning. L'app supporta attualmente lettori di schede Apple Certified e iXpand Flash Drive. Se hai un iXpand Flash Drive - inseriscilo nella porta lightning e apri l'applicazione. Vedrai un messaggio 'Dispositivo esterno collegato' e le informazioni sul dispositivo. Basta toccare l'icona del flash drive per accedere alla cartella musicale e toccare qualsiasi file audio per iniziare la riproduzione. Abbiamo istruzioni dettagliate su come collegare una flash drive USB all'iPhone e ascoltare musica o gestire i file presenti disponibili [qui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestore File

Una volta collegato un servizio di storage cloud, tocca la sua icona per visualizzare tutti i file e le cartelle disponibili. Puoi usare il gestore file integrato per lavorare con questi file — scaricare, rinominare, spostare e altro ancora. Quando avvii un download, il file apparirà nella coda di trasferimento. Per visualizzare la coda di trasferimento, vai alla scheda "File locali" e tocca le frecce rotanti nell'angolo in alto a sinistra. Tutti i file e le cartelle scaricati sono disponibili nella sezione "File locali".

## Barra degli strumenti superiore

La barra degli strumenti superiore, convenientemente posizionata sotto la barra di navigazione, offre diverse azioni utili per un accesso facile. Puoi mostrare o nascondere questa barra degli strumenti usando un semplice gesto di scorrimento verso il basso. Ecco le azioni disponibili:

- **Cerca**: questa opzione ti permette di eseguire una ricerca rapida nella directory corrente, rendendo facile individuare file o cartelle specifici.
- **Continua Riproduzione**: se abilitata nelle impostazioni dell'applicazione, questa funzione ripristina la coda del lettore audio e l'ultima posizione media per la cartella corrente. È un modo pratico per riprendere da dove hai lasciato nella tua libreria musicale.
- **Riproduci tutti**: selezionando questa azione, l'app scansionerà la cartella corrente e le sue sottocartelle, aggiungendo tutti i file audio trovati a una nuova coda del lettore. Questo è utile quando vuoi riprodurre tutta la musica all'interno di una particolare directory.
- **Mescola tutti**: simile a "Riproduci tutti," questa azione scansiona la cartella corrente e le sue sottocartelle ma mescola i file prima di aggiungerli alla coda del lettore audio. È un ottimo modo per godere della tua musica in ordine casuale per un po' di varietà.

{{< cards cols="1">}}
  {{< card title="" subtitle="Barra degli Strumenti Superiore in una Cartella Cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opzioni Cartella

Quando apri una cartella all'interno dell'app, troverai un utile set di azioni disponibili toccando il pulsante "..." nell'angolo in alto a destra dello schermo.  
Ecco una descrizione di queste azioni:

- **Seleziona**: attiva la modalità di selezione file. Questa modalità ti permette di scegliere uno o più file all'interno della cartella, rendendo facile eseguire azioni sugli elementi selezionati.
- **Nuova cartella**: crea una nuova cartella all'interno della cartella corrente. Questa funzione ti permette di organizzare i tuoi file e mantenere la tua libreria ben strutturata.
- **Abilita modalità offline**: attiva la modalità offline per la cartella corrente. La modalità offline va oltre il semplice download; monitora attivamente la cartella per rilevare modifiche. Se aggiungi nuovi file alla cartella online, l'app li scaricherà automaticamente sul tuo dispositivo. Questo garantisce che la tua libreria locale rimanga aggiornata con le modifiche sul server.
- **Carica file**: carica file dal tuo dispositivo nella cartella online. Questa azione ti permette di trasferire file sul cloud o server, rendendoli accessibili da qualsiasi luogo.
- **Cerca**: cerca file specifici all'interno della cartella corrente. Questo è particolarmente utile per individuare rapidamente elementi specifici in una grande raccolta.
- **Ordina**: ordina i file all'interno della cartella per criteri come nome, dimensione o data di modifica. La modalità di ordinamento predefinita in genere rispecchia l'ordine di ordinamento sul server, ma puoi cambiarla secondo le tue preferenze.
- **Vista griglia/lista**: passa tra due modalità di visualizzazione: vista tabella e vista miniatura. La vista tabella presenta i file in un elenco, mentre la vista miniatura mostra rappresentazioni visive dei file, rendendo più facile identificare il contenuto a colpo d'occhio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Altre azioni Cartella Corrente" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Modifica File Online

Quando hai bisogno di gestire più file nel tuo storage cloud su Evermusic, puoi usare la modalità di selezione per semplificare le tue azioni. Segui questi passaggi per una gestione efficace dei file:

- **Attiva Modalità Selezione**: apri l'app sul tuo dispositivo e naviga alla sezione contenente il tuo storage cloud. Cerca il pulsante "..." (ellissi) nell'angolo in alto a destra. Toccalo e scegli la voce di menu "Seleziona" per attivare la modalità di selezione.
- **Scegli File**: noterai le caselle di controllo che appaiono accanto a ogni file o cartella elencata. Scegli uno o più file o cartelle semplicemente toccando le caselle di controllo accanto a loro.
- **Esegui Varie Azioni**: una volta selezionati i file o le cartelle che vuoi gestire, avrai accesso a diverse azioni personalizzate per le tue esigenze.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modalità Selezione per File Online" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Azioni sui file

Vicino al titolo del file, noterai un simbolo di ellissi "..." (tre punti) — questo funge da menu delle azioni.  
Toccalo per rivelare un elenco di azioni disponibili:

- **Riproduci successivo**: scegli questa azione per inserire il file selezionato in cima alla coda del lettore, assicurandoti che venga riprodotto immediatamente dopo l'elemento in riproduzione.
- **Riproduci più tardi**: selezionando questa opzione il file viene aggiunto in fondo alla coda del lettore, assicurandosi che venga riprodotto dopo la coda esistente.
- **Aggiungi alla Libreria musicale**: questa azione ti permette di incorporare il file nella tua libreria musicale, rendendolo facilmente accessibile e ordinato per artista, album, genere o compositore.
- **Aggiungi a una Playlist**: usa questa azione per aggiungere il file a una playlist esistente o crearne una nuova.
- **Modificare i tag audio**: selezionando questa opzione, puoi accedere all'editor di tag integrato di Evermusic, permettendoti di modificare i tag audio per il file selezionato. Il file verrà temporaneamente scaricato in una directory temporanea e poi caricato sullo storage dopo che confermi le modifiche.
- **Aggiungi ai Preferiti**: questa azione aggiunge il file al tuo elenco di file preferiti per un accesso rapido e conveniente.
- **Scarica**: scegli questa azione per scaricare il file o la cartella sul tuo dispositivo, rendendolo accessibile per l'uso offline.
- **Rinomina**: questa opzione ti permette di rinominare il file direttamente sullo storage remoto, consentendo la denominazione personalizzata dei file.
- **Sposta**: scegli questa azione per spostare il file in una cartella diversa all'interno del tuo storage cloud, aiutando a mantenere una struttura di file organizzata.
- **Apri con**: usa questa azione per esportare il file in un'altra app compatibile. Il file verrà scaricato sul tuo dispositivo, e poi apparirà il dialogo di Condivisione per ulteriore condivisione o interazione.
- **Elimina**: fai attenzione con questa azione, poiché rimuove permanentemente il file dal tuo storage cloud. Questa eliminazione non può essere annullata.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Altre azioni per un Singolo File" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Se l'elenco delle azioni supera lo spazio disponibile sullo schermo, scorri semplicemente verso il basso all'interno del menu delle azioni per accedere a opzioni aggiuntive.

## Azioni sulle cartelle

Per ogni cartella nel tuo storage cloud, sono disponibili varie azioni. Per accedere a queste opzioni, basta toccare l'icona ellissi "..." situata accanto al titolo della cartella. Se non vedi tutte le azioni, scorri verso il basso per rivelare più scelte. Ecco le azioni disponibili:

- **Riproduci tutti**: sostituisce la coda del lettore corrente con tutti gli elementi della cartella selezionata.
- **Riproduci successivo**: aggiunge l'intera cartella in cima alla coda del lettore, subito dopo l'elemento in riproduzione.
- **Riproduci più tardi**: aggiunge il contenuto della cartella in fondo alla coda del lettore.
- **Aggiungi alla Libreria musicale**: questa azione incorpora perfettamente il contenuto della cartella nella tua libreria musicale, rendendolo facilmente accessibile e ordinato per artista, album, genere o compositore.
- **Aggiungi alla Playlist**: puoi includere l'intera cartella in una playlist. Hai anche la possibilità di creare una nuova playlist, e il nome della cartella verrà assegnato automaticamente.
- **Aggiungi ai Preferiti**: usa questa azione per aggiungere la cartella al tuo elenco di file preferiti per un accesso rapido e conveniente.
- **Abilita modalità offline**: abilitando la modalità offline per una cartella selezionata, l'applicazione va oltre il semplice download. Scansiona continuamente le modifiche, e se nuovi file vengono aggiunti alla cartella online, verranno scaricati automaticamente nell'app.
- **Scarica**: scarica tutti i contenuti della cartella sul tuo dispositivo per l'accesso offline.
- **Rinomina**: rinomina la cartella direttamente sullo storage remoto.
- **Sposta**: sposta la cartella in una posizione diversa all'interno del tuo storage cloud.
- **Elimina**: fai attenzione con questa azione poiché rimuove permanentemente la cartella e il suo contenuto dal tuo storage cloud. Questa azione non può essere annullata.


## Accesso Rapido

La sezione Accesso Rapido si trova in cima alla schermata. Ti dà un accesso rapido ai tuoi file preferiti e aperti di recente dai servizi cloud connessi.
Ogni volta che apri un file o una cartella dal cloud, viene aggiunto all'elenco "Aperti di recente". Per cancellare questo elenco, apri "Recenti," tocca il pulsante "Altre azioni", e scegli "Elimina Elenco." Puoi anche contrassegnare cartelle profondamente annidate come Preferiti per accedervi rapidamente senza dover scavare nella struttura della directory.

## Altri Servizi

Questa sezione mostra funzionalità extra che migliorano la tua esperienza. Attualmente, l'app supporta lo scrobbling di Last.fm. Quando collegata, le tue statistiche di riproduzione vengono inviate automaticamente al tuo account Last.fm. Puoi visitare il tuo profilo Last.fm in seguito per visualizzare le analisi di ascolto e ricevere raccomandazioni musicali personalizzate. Istruzioni di configurazione dettagliate sono disponibili [qui](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
