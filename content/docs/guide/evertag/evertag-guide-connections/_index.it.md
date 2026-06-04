---
title: "Connessioni"
date: 2020-02-01
description: "Scopri come connettere archiviazione cloud, NAS e il tuo computer a Evertag. Accedi e modifica i file audio direttamente dall'archiviazione cloud, dal NAS personale o da Mac/PC."
keywords: [
  "configurazione cloud Evertag", "connettere iCloud a Evertag", "accesso file SMB iOS",
  "editor tag audio WebDAV", "modifica metadati NAS", "Wi-Fi Drive Evertag",
  "trasferire file audio su iPhone", "Evertag iTunes File Sharing", "modifica tag FLAC dal cloud"
]
tags: ["guida", "evertag", "connessioni"]
readingTime: 11
---


In questa schermata puoi connettere varie sorgenti contenenti i tuoi file audio. Puoi integrare servizi cloud popolari come Google Drive, Dropbox, OneDrive, iCloud e altri, nonché connettere il tuo Mac o PC. Inoltre, hai la possibilità di modificare i file audio situati su Apple Time Capsule, WD Cloud Home, o qualsiasi NAS che supporti SMB o WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Connessioni di Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Accesso rapido

In cima alla schermata Connessioni troverai un elenco **Accesso rapido**. Qualsiasi cartella cloud che aggiungi ai preferiti — anche una sepolta a diversi livelli di profondità — appare qui così puoi raggiungerla senza dover navigare tra le cartelle padre ogni volta.

## Connetti a un'archiviazione cloud

- Apri la scheda 'Connessioni'  
- Seleziona 'Connetti a un'archiviazione cloud' dal menu  
- Scegli un servizio di archiviazione cloud dall'elenco  
- Inserisci le credenziali e tocca 'Fatto.'

Se riscontri problemi, assicurati di controllare la connessione Internet e il login/password.  
Nella versione Premium dell'app, puoi aggiungere un numero illimitato di servizi.

## Servizi di archiviazione cloud supportati

Attualmente, l'applicazione supporta i servizi di archiviazione cloud più popolari: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), nonché qualsiasi server SMB o WebDAV.

## Sicurezza e privacy

Utilizziamo solo SDK ufficiali e connessioni sicure per interagire con i servizi cloud connessi. Il tuo login e la tua password non sono accessibili all'applicazione. Tutte le richieste dall'applicazione al servizio cloud sono crittografate.

Quando inserisci il tuo login e la tua password, l'applicazione ti mostra la pagina di autorizzazione ufficiale fornita dal provider del servizio cloud, e l'intero processo di autorizzazione avviene al di fuori dell'applicazione. Il provider del servizio cloud invia un token di autenticazione all'applicazione dopo l'autorizzazione riuscita, e quel token viene utilizzato per effettuare chiamate API.

Un token di autenticazione è una chiave digitale che consente alle applicazioni di terze parti di interagire con l'archiviazione cloud. Il token di autenticazione è archiviato sul tuo dispositivo in un'archiviazione di sistema sicura chiamata Keychain. Puoi scaricare i tuoi file dal servizio cloud connesso al dispositivo, e quei file saranno collocati nella directory "Documents" dell'app. Puoi rimuovere quei file in qualsiasi momento usando il gestore file integrato.

L'applicazione non condivide alcuna informazione dall'account cloud connesso. Puoi revocare l'accesso al tuo account cloud in qualsiasi momento aprendo la pagina delle impostazioni dell'account nel tuo browser web.

## Rifiuta il token di autenticazione

Accedi al tuo account in un browser web e vai alla pagina delle impostazioni. Lì puoi trovare tutte le app di terze parti connesse al tuo account cloud e rimuovere quelle che non vuoi più usare. Istruzioni dettagliate sono disponibili [qui](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Puoi anche disconnettere gli account cloud connessi nell'applicazione, e il token di autenticazione verrà rimosso anche dal tuo dispositivo. Se rimuovi l'applicazione dal dispositivo, tutti i dati scaricati e i token di accesso verranno rimossi.

## Disconnetti un'archiviazione cloud o modifica la configurazione

- Accedi alle opzioni di archiviazione cloud: prima individua l'archiviazione cloud che desideri gestire nell'interfaccia dell'app.  
- Tocca il pulsante '...': accanto al titolo del servizio vedrai un pulsante '...'. Toccalo per accedere alle opzioni aggiuntive.  
  - **Rinomina**: se vuoi cambiare il nome del servizio cloud come appare nel tuo elenco, seleziona 'Rinomina.'  
  - **Impostazioni**: per modificare la configurazione o i dati di autenticazione del servizio cloud, scegli 'Impostazioni.' A volte, potrebbe essere necessario riautorizzare il servizio cloud connesso se il token di autorizzazione è scaduto.  
  - **Disconnettere**: se desideri interrompere completamente la connessione tra l'app e il servizio cloud, seleziona 'Disconnettere.' Tieni presente che scegliendo questa opzione verranno rimossi tutti i brani associati a questo servizio cloud dalla libreria musicale dell'app, ma rimarranno sul server.

## Connetti a un computer o NAS

Puoi anche connettere il tuo computer, NAS personale o altri dispositivi di rete utilizzando il protocollo SMB, DLNA o WebDAV.

## Connetti al computer tramite SMB

- Tocca "Connetti a un'archiviazione cloud" → SMB.  
- Inserisci l'indirizzo IP del computer e il nome della cartella condivisa nel campo URL usando il formato smb://computer-ip-address/shared-folder-name  
- Scegli la versione del protocollo: Auto, SMB1, SMB2  
- Inserisci login e password (se richiesti)  
- Tocca "Fatto."

Se la connessione ha successo, vedrai l'archiviazione connessa nella sezione "Archiviazione cloud."  
Un tutorial completo su come connettere il tuo Mac o PC tramite SMB è disponibile [qui](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connetti al NAS tramite WebDAV

Tutti i passaggi sono gli stessi tranne per il campo URL.  
L'URL deve essere nel formato http://server-name, o https://server-name se il server supporta SSL.  
Un tutorial completo su come connettere il NAS usando il protocollo WebDAV è disponibile [qui](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dispositivi disponibili

Questa sezione mostra tutti i dispositivi nella tua rete locale a cui puoi connetterti tramite l'applicazione.  
Per stabilire una connessione con un dispositivo, segui questi passaggi:

- Apri l'app e vai alla sezione "Dispositivi disponibili".  
- Tocca il dispositivo a cui vuoi connetterti dall'elenco.  
- Se necessario, inserisci i tuoi dati di accesso per completare la connessione.

## Wi-Fi Drive 

Wi-Fi Drive è una tecnologia conveniente che consente trasferimenti di file wireless dal computer al dispositivo iOS tramite un browser desktop.  
Per usare questa funzionalità in modo efficace, assicurati che il tuo dispositivo e il computer siano connessi alla stessa rete Wi-Fi.  
Ecco una guida passo dopo passo su come usare Wi-Fi Drive.

## Abilita Wi-Fi Drive

- Apri l'applicazione e vai alla scheda "Connessioni".  
- Seleziona "Connetti tramite Wi-Fi" per accedere alla schermata principale di Wi-Fi Drive.  
- Tocca "Avvia Wi-Fi Drive" per abilitare Wi-Fi Drive.

## Accedi a Wi-Fi Drive dal computer

- Sul tuo computer (desktop o laptop), apri un browser web (come Chrome, Firefox o Safari).  
- Nella barra degli indirizzi del browser, inserisci l'URL fornito dall'applicazione.

## Trasferisci file in modalità wireless

Una volta che la pagina web corrispondente al tuo dispositivo iOS si apre nel browser, puoi facilmente trascinare e rilasciare file dal computer alla pagina web.  
I file che trascini e rilasci inizieranno a trasferirsi sul tuo dispositivo iOS e saranno accessibili nell'applicazione.

Istruzioni dettagliate su come trasferire file in modalità wireless usando Wi-Fi Drive sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing è un'altra tecnologia che ti consente di trasferire file da un computer a un dispositivo usando l'app Finder su Mac e un cavo Lightning.  
- Basta connettere il dispositivo al computer usando un cavo e avviare l'app Finder sul Mac.  
- Apri "Posizioni" → "Il tuo dispositivo connesso" → "File" → e trova l'app corrente.  
- Tocca l'icona dell'app per vedere tutte le cartelle condivise.  
- Copia i file dal computer alla cartella condivisa sul dispositivo usando il trascinamento.

Istruzioni dettagliate su come usare iTunes File Sharing sono disponibili [qui](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connetti una chiavetta USB

Se hai una scheda SD o una chiavetta USB, puoi connetterla usando un lettore di schede Lightning o USB-C su iPhone/iPad, o inserirla direttamente in un Mac. L'app supporta attualmente i lettori di schede certificati Apple. Abbiamo istruzioni dettagliate su come connettere una chiavetta USB all'iPhone o iPad e gestire i file su di essa, disponibili [qui](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). I drive connessi appaiono nella sezione **Accessori connessi** della schermata Connessioni.

## Gestore file

Dopo aver connesso un servizio di archiviazione cloud, tocca la sua icona per visualizzare tutti i file e le cartelle disponibili. Puoi usare il gestore file integrato per lavorare con questi file — scaricare, rinominare, spostare e altro ancora. Quando avvii un download, il file apparirà nella coda di trasferimento. Per visualizzare la coda di trasferimento, vai alla scheda "File locali" e tocca le frecce rotanti nell'angolo in alto a sinistra. Tutti i file e le cartelle scaricati sono disponibili nella sezione "File locali".

## Barra degli strumenti superiore

La barra degli strumenti superiore, comodamente posizionata sotto la barra di navigazione, offre diverse azioni utili per un facile accesso. Puoi mostrare o nascondere questa barra strumenti usando un semplice gesto di scorrimento verso il basso. Ecco le azioni disponibili:

- **Cerca**: questa opzione ti permette di eseguire una ricerca rapida nella directory corrente, rendendo semplice trovare file o cartelle specifici.  

## Opzioni cartella

Quando apri una cartella nell'app, troverai una serie di azioni disponibili toccando il pulsante "..." nell'angolo in alto a destra dello schermo.  
Ecco le azioni disponibili:

- **Selezionare**: attiva la modalità di selezione file. Questa modalità ti consente di scegliere uno o più file all'interno della cartella.  
- **Nuova cartella**: crea una nuova cartella all'interno della cartella corrente. Questa funzione ti permette di organizzare i file e mantenere la libreria ben strutturata.  
- **Carica file**: carica file dal dispositivo nella cartella online. Questa azione ti consente di trasferire file nel cloud o sul server.  
- **Cerca**: cerca file specifici all'interno della cartella corrente.  
- **Ordina**: ordina i file nella cartella per criteri come nome, dimensione o data di modifica.  
- **Vista griglia/elenco**: passa tra due modalità di visualizzazione: vista a tabella e vista a miniature.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ordinamento cartella cloud Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Modifica file online

Quando devi gestire più file nell'archiviazione cloud su questa app, puoi usare la modalità di selezione per semplificare le tue azioni. Segui questi passaggi per una gestione efficace dei file:

- **Attiva la modalità di selezione**: apri l'app sul dispositivo e naviga nella sezione contenente la tua archiviazione cloud. Cerca il pulsante "..." (puntini di sospensione) nell'angolo in alto a destra. Toccalo e scegli la voce di menu "Selezionare" per attivare la modalità di selezione.  
- **Scegli file**: vedrai comparire caselle di controllo accanto a ogni file o cartella elencato. Scegli uno o più file o cartelle semplicemente toccando le caselle di controllo accanto ad essi.  
- **Esegui varie azioni**: dopo aver selezionato i file o le cartelle da gestire, avrai accesso a diverse azioni:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selezione file Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Azioni file

Vicino al titolo del file, vedrai un simbolo di puntini di sospensione "..." (tre punti) — questo funge da menu delle azioni.  
Toccalo per rivelare un elenco di azioni disponibili:

- **Modificare i tag audio**: selezionando questa opzione puoi accedere all'editor di tag integrato, che ti consente di modificare i tag audio per il file scelto. Il file verrà temporaneamente scaricato in una directory temporanea e poi caricato sull'archiviazione dopo che avrai confermato le modifiche.  
- **Aggiungi ai preferiti**: questa azione aggiunge il file al tuo elenco di file preferiti per un accesso rapido e comodo.  
- **Scaricare**: scegli questa azione per scaricare il file o la cartella sul dispositivo, rendendolo accessibile offline.  
- **Rinomina**: questa opzione ti permette di rinominare il file direttamente sull'archiviazione remota.  
- **Sposta**: scegli questa azione per spostare il file in un'altra cartella all'interno della tua archiviazione cloud.  
- **Apri in**: usa questa azione per esportare il file in un'altra app compatibile. Il file verrà scaricato sul dispositivo, e poi apparirà la finestra di dialogo di condivisione.  
- **Eliminare**: usa questa azione con cautela, poiché rimuove permanentemente il file dalla tua archiviazione cloud. **Questa eliminazione non può essere annullata**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opzioni file Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Se l'elenco delle azioni supera lo spazio disponibile sullo schermo, scorri semplicemente verso il basso nel menu delle azioni per accedere alle opzioni aggiuntive.

## Azioni cartella

Per ogni cartella nella tua archiviazione cloud, sono disponibili varie azioni. Per accedere a queste opzioni, tocca semplicemente l'icona dei puntini di sospensione "..." situata accanto al titolo della cartella. Se non vedi tutte le azioni, scorri verso il basso per rivelare più scelte. Ecco le azioni disponibili:

- **Aggiungi ai preferiti**: usa questa azione per aggiungere la cartella al tuo elenco di file preferiti per un accesso rapido e comodo.  
- **Scaricare**: scarica tutto il contenuto della cartella sul dispositivo per l'accesso offline.  
- **Rinomina**: rinomina la cartella direttamente sull'archiviazione remota.  
- **Sposta**: sposta la cartella in un'altra posizione all'interno della tua archiviazione cloud.  
- **Eliminare**: usa questa azione con cautela, poiché rimuove permanentemente la cartella e i suoi contenuti dalla tua archiviazione cloud. **Questa azione non può essere annullata**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opzioni cartella Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
