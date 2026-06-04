---
title: "Impostazioni"
date: 2020-01-01
description: "Esplora tutte le impostazioni in Evermusic tra cui la configurazione audio, la sincronizzazione della libreria musicale, le cartelle offline, i metadati, la personalizzazione, l'accessibilità, i widget, CarPlay e le opzioni di backup."
keywords: [
  "Evermusic", "impostazioni", "impostazioni audio", "sincronizzazione libreria musicale",
  "cartelle offline", "equalizzatore", "crossfade", "riproduzione gapless",
  "processore audio", "impostazioni playlist", "aggiornamento premium",
  "ripristina acquisti", "gestore file", "editor tag", "WiFi drive",
  "voiceover", "backup app", "accessibilità", "localizzazione",
  "widget", "CarPlay", "audio spaziale", "intonazione audio"
]
tags: ["evermusic", "guida", "impostazioni"]
readingTime: 16
---


La schermata Impostazioni è il centro di controllo di Evermusic. Da qui puoi passare a Premium, configurare il lettore audio, gestire la tua libreria musicale, impostare il gestore file, personalizzare l'interfaccia, abilitare widget e CarPlay, eseguire il backup dei tuoi dati e accedere all'aiuto e alle informazioni legali. Le sezioni sono raggruppate sotto intestazioni: **Acquisti e aggiornamenti**, preferenze app, **Aiuto**, e **Legale e privacy**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Impostazioni Evermusic" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Acquisti e Aggiornamenti

### Passa a Premium

Aggiorna l'applicazione alla versione Premium per rimuovere tutti i limiti. La versione gratuita offre un acquisto in-app una tantum e due opzioni di abbonamento che sbloccano il set completo di funzionalità.

Il Family Sharing è abilitato per tutti gli acquisti e i piani, in modo da poter condividere la versione Premium con i membri della famiglia.

Puoi leggere di più sugli acquisti e sulla versione Premium qui: [Qual è la differenza tra Evermusic ed Evermusic Premium](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (Icona Blu) vs Evermusic Pro (Icona Rossa)

Evermusic è pubblicato sull'App Store con due icone/colori diversi:

- **Evermusic Free (icona blu)** è suddiviso in **due app App Store separate con bundle ID diversi** — uno per **iOS/iPadOS** e uno dedicato per **macOS** (Binary Universal che funziona su **Apple Silicon e Intel Mac**). Gli acquisti in-app Premium sono **condivisi tra le app blu iOS e Mac tramite iCloud** — acquista Premium su iPhone e si attiva automaticamente su Mac (e viceversa), purché entrambi i dispositivi utilizzino lo stesso Apple ID con iCloud abilitato.
- **Evermusic Pro (icona rossa)** è una **singola app App Store** con un **singolo bundle ID** che funziona su **iPhone, iPad e Apple Silicon Mac (M1 e versioni successive)**. Ha la **stessa funzionalità di Evermusic Free con un piano Premium attivato**. L'app rossa **non supporta Intel Mac**, ecco perché il suo prezzo è leggermente inferiore all'acquisto Premium equivalente nell'app blu. Evermusic Pro **non raccoglie alcuna diagnostica o analitiche utente** — le analitiche sono completamente disabilitate nel build, senza opzione di opt-in.

Poiché i bundle ID differiscono tra blu e rosso, un acquisto in-app Premium attivato nell'app blu non sblocca l'app rossa gratuitamente e viceversa. Se usi già l'app blu con Premium attivato, non è necessario installare l'app rossa — hai già tutto ciò che Pro offre.

### Condivisione degli Acquisti tra iOS e Mac

Gli acquisti a vita e gli abbonamenti sono condivisi tra iOS e Mac usando iCloud. Se hai già Premium su iOS, assicurati di avere la versione più recente installata e che iCloud sia abilitato. Avvia l'app su iOS e attendi un minuto affinché le informazioni sull'acquisto vengano caricate su iCloud.

Puoi anche toccare **Ripristina Acquisti** nelle impostazioni dell'app. Successivamente, installa la versione più recente dell'app dall'App Store sul tuo Mac e avvia l'app. Assicurati di avere una connessione internet e di essere connesso con lo stesso account iCloud e App Store su entrambi i dispositivi. Attendi un minuto affinché l'app scarichi le informazioni sull'acquisto da iCloud. La versione Premium dovrebbe attivarsi automaticamente sul tuo Mac.

### Ripristina Acquisti su un Nuovo Dispositivo

Per ripristinare il tuo acquisto su un nuovo dispositivo, usa **Acquisti → Ripristina Acquisti**. Vedrai l'elenco dei tuoi acquisti. Se manca qualcosa, verifica che il dispositivo sia connesso allo stesso account iTunes utilizzato per effettuare gli acquisti e che iCloud sia abilitato.

### Prova Premium Gratuitamente

Puoi passare alla versione Premium gratuitamente per un periodo limitato usando questo menu. Guarda una breve pubblicità o condividi l'app con gli amici per sbloccare temporaneamente Premium.

### Acquisti

Ripristina gli acquisti precedenti da questo menu. Se riscontri errori di attivazione, prova ad abilitare l'opzione **Ripristina Acquisti all'Avvio dell'App**.

### Aggiornamento Software

Tocca **Aggiornamento Software** per verificare se è disponibile una versione più recente di Evermusic. L'app confronterà la versione installata con la versione più recente sull'App Store e ti farà sapere se è consigliato un aggiornamento.

### Novità

Questo menu diventa disponibile dopo il rilascio di una nuova versione. Mostra un riepilogo delle modifiche e delle nuove funzionalità incluse nell'aggiornamento più recente.

## Impostazioni del Lettore Audio

Tutte le impostazioni del lettore audio sono raggruppate qui: equalizzatore, riproduzione crossfade, cache del lettore audio, caricamento canzoni e altro. Le impostazioni sono organizzate in sotto-sezioni logiche.

### Generale

Questa sotto-sezione contiene le impostazioni generali della coda di riproduzione, dell'uscita audio e del salvataggio dello stato.

#### Modalità di Ripetizione

Specifica il comportamento del lettore audio quando un brano termina la riproduzione:

- **Ripeti Tutto** – riproduce in loop tutti i brani nella tua coda del lettore.
- **Ripeti Uno** – ripete solo il brano corrente.
- **Ferma Ripetizione** – mette in pausa la riproduzione quando il brano corrente finisce.
- **Nessuna Ripetizione** – lascia riprodurre la coda senza ripetere.

#### Modalità Mescola

Riproduce i brani in ordine casuale. Questo mescola effettivamente la coda e riproduce i brani uno per uno nel nuovo ordine. Valori disponibili: **Mescola disattivato** e **Mescola attivato**.

#### Processore Audio

Valori possibili: **AVFoundation** e **CoreAudio**. Per impostazione predefinita, viene usato AVFoundation. A causa di un problema noto con AVFoundation su iOS 17.0–17.6, la riproduzione crossfade e l'equalizzatore audio non possono essere usati contemporaneamente. Per godere di entrambi su queste versioni di iOS, passa al processore audio CoreAudio.

Se riscontri problemi con la riproduzione gapless usando AVFoundation, prova anche CoreAudio. Le uniche limitazioni di CoreAudio sono lo streaming internet di alcune stazioni radio e certi formati audio, poiché non supporta ogni formato audio di sistema (come M4A e altri).

#### Frequenza di Campionamento dell'Uscita Audio

Imposta la frequenza di campionamento dell'uscita audio da 8 KHz a 384 KHz. Questa opzione è disponibile solo quando il processore CoreAudio è selezionato.

#### Numero di Canali di Uscita Audio

Imposta il numero di canali di uscita audio — **MONO** o **STEREO**. Questa opzione è disponibile solo quando il processore CoreAudio è selezionato.

#### Algoritmo di Intonazione Audio

Scegli l'algoritmo usato per la correzione dell'intonazione. I valori disponibili sono **Dominio Temporale**, **Spettrale** e **Varispeed**. Utile se regoli la velocità di riproduzione e vuoi controllare la qualità audio risultante.

#### Audio Spaziale

L'audio spaziale utilizza metodi psicoacustici per creare un'esperienza audio più immersiva su cuffie e disposizioni di altoparlanti supportati. Valori possibili: **Disattivato**, **Mono e Stereo**, **Multicanale**, **Mono Stereo Multicanale**.

#### Modalità di Uscita Audio

Disponibile solo su iOS. Ti permette di abilitare la modalità mista in modo che l'audio di questa applicazione si mescoli con altre applicazioni. Puoi trovare istruzioni su come usare la modalità mista [qui](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Salva Posizione di Riproduzione

Assicura che l'applicazione salvi e ripristini la posizione di riproduzione per i brani nella tua libreria musicale.

#### Salva Stato del Lettore Audio

Salva lo stato del lettore audio prima di chiudere l'applicazione, rendendo facile riprendere da dove ti eri interrotto.

Una volta abilitati entrambe queste funzioni, apri qualsiasi cartella, album, artista o genere. Vedrai un'azione **Continua Riproduzione** nella parte superiore della schermata, insieme all'ultima canzone salvata e alla posizione di riproduzione. Tocca **Continua Riproduzione** per ripristinare. Per riprendere la riproduzione per un singolo file, tocca semplicemente quel file.

### Personalizzazione

Personalizza l'aspetto della schermata del lettore audio, scegli quali controlli sono visibili sul lettore, sulla schermata di blocco e sulla barra di stato, e configura i pulsanti del tempo di salto.

#### Stile Schermata Lettore Audio

Configura il posizionamento delle toolbar e dei controlli principali sul lettore audio.

#### Stile Scorrimento Copertine Album

Scegli lo stile di scorrimento per le copertine degli album nella schermata del lettore audio.

#### Elementi Aggiuntivi

Abilita elementi extra nella schermata del lettore audio. **Info Formato Audio** mostra le informazioni tecniche del brano in riproduzione sopra l'artwork; **Cursore Volume Audio** mostra il cursore dell'uscita audio sotto i controlli di riproduzione.

#### Azioni Schermata Principale

Configura quali pulsanti sono visibili nella schermata principale del lettore audio. Le opzioni disponibili includono Modalità Ripetizione e Mescola, Canzone Successiva e Precedente, Salta Tempo, Timer di Spegnimento, Google Chromecast, AirPlay e Bluetooth, Equalizzatore Audio, Cerca, Segnalibri, Velocità, Aggiungi Segnalibro, Aggiungi ai Preferiti, Commenti e altro.

#### Controlli di Riproduzione nella Schermata di Blocco

Scegli quali controlli extra sono abilitati nella schermata di blocco. Valori possibili: **Salta Tempo**, **Aggiungi Segnalibro** e **Aggiungi ai Preferiti**.

#### Intervalli di Tempo di Salto

Seleziona gli intervalli di tempo usati dai pulsanti Salta Tempo avanti e indietro.

### Caricamento File

Scegli il tipo di rete usato per fare lo streaming delle canzoni. Opzioni disponibili: **Wi-Fi** e **Wi-Fi & Dati Cellulari**.

#### Tempo di Precaricamento

Imposta l'intervallo di buffering. Aumenta questo valore se hai una connessione di rete scadente.

#### Usa URL Diretto

Quando abilitato, viene usato un URL diretto per caricare la canzone se il server lo supporta. Questo può velocizzare il caricamento delle canzoni ma può influire leggermente sulla stabilità della riproduzione.

#### Ottimizza Caricamento File

Quando abilitato, il sistema ottimizza il caricamento delle canzoni per il processore audio AVFoundation, il che può migliorare la stabilità della riproduzione. L'app usa la tecnologia descritta [qui](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Equalizzatore Audio

Configura l'equalizzatore audio. Puoi leggere di più sui preset e le configurazioni EQ [qui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Dispositivi

Connetti a un dispositivo AirPlay o Google Chromecast (solo iOS).

### Velocità di Riproduzione

Regola la velocità di riproduzione del lettore audio. Per un controllo più preciso, abilita il cursore preciso toccando l'icona di configurazione nell'angolo in alto a destra.

### Riproduzione Crossfade

Il crossfade consente ai brani di scorrere senza interruzioni in un mix continuo — il brano successivo inizia a riprodursi alcuni secondi prima che quello corrente finisca. Il crossfade non è disponibile per AirPlay e Google Chromecast. In questa schermata, scegli per quanto tempo il brano corrente e il brano successivo vengono riprodotti contemporaneamente. Se riscontri problemi con crossfade e l'equalizzatore audio contemporaneamente, cambia il processore audio come descritto sopra.

### Riproduzione Gapless

La riproduzione gapless garantisce che i brani vengano riprodotti senza interruzioni o silenzi nel mezzo. È perfetta per la musica classica, le registrazioni dal vivo e gli album concept. Se hai problemi con la riproduzione gapless, cambia il processore audio come descritto sopra.

### Cache di Riproduzione

I brani nella coda del lettore audio vengono scaricati automaticamente per una riproduzione fluida. Se scarichi file audio manualmente, puoi disabilitare questa opzione per evitare duplicati. Puoi anche configurare qui la dimensione della cache del lettore audio. Leggi di più sulla modalità offline e la cache di riproduzione qui: [Riproduci Musica Offline in Evermusic & Flacbox: Scarica e Sincronizza dal Cloud ai File Locali](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Timer di Spegnimento

Abilita un timer per arrestare la riproduzione dopo un timeout specificato. Per un controllo più preciso, abilita la modalità precisa toccando l'icona di configurazione nell'angolo in alto a destra.

## Libreria

Le impostazioni della libreria musicale — sincronizzazione automatica, lettura dei metadati, caricamento delle copertine degli album, playlist, recenti e preferiti — si trovano qui.

### Lettura dei Metadati

Quando aggiungi brani alla libreria, il lettore di metadati li elabora in background e li organizza per Artista, Album, Genere e Compositore. Puoi regolare la velocità di lettura dei metadati per caricare i dati più velocemente (al costo di più batteria). Puoi anche disabilitare completamente il lettore di metadati e mostrare i nomi dei file invece delle informazioni sui tag.

Il lettore di metadati aggiorna solo il database della libreria musicale; non altera i file memorizzati nel tuo account cloud o nell'archiviazione locale. Se hai bisogno di modificare i metadati dei file audio, usa l'editor di tag integrato tramite l'azione corrispondente nel menu opzioni.

Quando **Lettura dei Metadati in Background** è attiva, il lettore continua a lavorare in modalità background. Se l'app usa troppa energia durante la riproduzione, iOS potrebbe sospenderla.

Se hai una grande raccolta musicale, è consigliabile eseguire la sincronizzazione dei metadati sulla versione desktop dell'applicazione. Puoi poi trasferire la libreria musicale sincronizzata su iOS usando la funzione **Backup e Ripristino**.

Quando **Normalizza Codifica Metadati** è abilitato, l'app normalizza automaticamente la codifica dei metadati per tutte le canzoni. Questo risolve i problemi in cui la codifica dei tag audio è danneggiata (ad esempio dopo aver modificato file su un PC Windows) e impedisce che caratteri errati appaiano nelle informazioni sui brani.

**Ricarica Metadati** contrassegna ogni file nella tua libreria musicale come avente metadati mancanti, il che fa sì che il lettore di metadati aggiorni ogni record.

**Avvia Lettura Metadati** avvia manualmente il lettore di metadati. Il progresso viene mostrato sotto l'azione.

### Sincronizzazione Online

La sincronizzazione automatica della musica online aggiunge brani dai servizi cloud connessi alla libreria musicale automaticamente. Per abilitarla, apri le impostazioni della libreria musicale e seleziona le cartelle di sincronizzazione.

Con questa opzione abilitata, l'applicazione scansiona le cartelle selezionate, identifica i file audio supportati e li aggiunge alla tua libreria. Avvia o interrompi la sincronizzazione con la corrispondente azione del menu.

La sincronizzazione online funziona solo quando l'app è in primo piano, quindi sincronizzare una grande libreria può richiedere del tempo. Per accelerare le cose, tieni l'app aperta, connetti a una fonte di alimentazione e abilita **Schermo → Sempre Attivo** nelle impostazioni.

In alternativa, esegui la sincronizzazione online sulla versione desktop dell'app e trasferisci la libreria musicale su iOS usando **Backup e Ripristino**.

Puoi anche scegliere con quale frequenza eseguire la sincronizzazione online. Impostando l'intervallo su **Immediatamente** si avvia una sincronizzazione ogni volta che apri l'applicazione.

### Sincronizzazione Offline

Configura la sincronizzazione della musica offline.

#### Cartelle Offline Sincronizzate

Quando contrassegni una cartella online sul tuo server cloud come disponibile offline (usando il menu Altre Azioni), appare qui. Il contenuto della cartella viene scaricato in **File Locali → Cartelle Offline**. Quando la cartella online cambia (file aggiunti, rimossi o aggiornati), l'app verifica le modifiche e aggiorna la copia locale sul tuo dispositivo.

In questa schermata puoi avviare manualmente la sincronizzazione delle cartelle offline, rivelare la cartella offline nella cartella che la contiene e disabilitare la modalità offline per la cartella. Disabilitare la modalità offline rimuove tutte le copie locali dei file dal tuo dispositivo.

#### Intervallo di Tempo

Scegli con quale frequenza l'app controlla le cartelle offline per le modifiche.

#### Avvia Scansione Cartelle Locali

Esegui la scansione di tutte le cartelle locali nella directory Documents dell'applicazione per i file audio supportati. I file trovati vengono aggiunti automaticamente alla libreria musicale. I file situati sul tuo dispositivo ma fuori dalla directory Documents dell'applicazione devono essere aggiunti manualmente alla libreria musicale, poiché l'app non può accedervi a causa delle restrizioni di sicurezza di iOS/macOS.

**Importante:** È consigliabile avviare periodicamente la sincronizzazione della musica offline per mantenere aggiornata la tua libreria musicale con i tuoi file locali.

### Personalizzazione

Configura lo stile della schermata della libreria musicale. Sono disponibili tre opzioni: **Menu semplice**, **Menu raggruppato** e **Menu a schede**. Puoi anche abilitare o disabilitare le copertine degli album nella schermata dei dettagli dell'album.

### Copertine Album

Scegli come l'applicazione carica e archivia le artwork degli album.

- **Tipo di rete** — scegli **Wi-Fi** o **Wi-Fi & Dati Cellulari** per i download delle copertine.
- **Carica Copertine Album per File Online** — quando abilitato, le copertine degli album incorporate vengono caricate per i file memorizzati nel cloud. Questo può usare dati di rete aggiuntivi.
- **Cerca nella Cartella** — quando abilitato, se un brano non ha una copertina incorporata, l'app cerca immagini JPEG o PNG nella stessa cartella e le usa come artwork dell'album.
- **Qualità Copertina** — seleziona la qualità delle copertine degli album memorizzate sul tuo dispositivo.
- **Mostra nella Cartella** — apri la cartella in cui sono memorizzate nella cache le copertine degli album in modo da poterle gestire o eseguire il backup.
- **Elimina Tutto** — elimina le copertine degli album nella cache per liberare spazio di archiviazione e forzare l'app a ricaricarle su richiesta.

### Playlist

Abilita l'opzione per aggiungere la stessa canzone a una playlist due volte. Per impostazione predefinita, questa opzione è disabilitata.

### Recenti

Gestisci il tuo elenco di canzoni riprodotte di recente.

- **Elimina Elenco** — elimina l'intero elenco delle canzoni riprodotte di recente.
- **Cambia Dimensione Elenco** — imposta il numero di elementi che appaiono nell'elenco.
- **Esporta Elenco Canzoni** — esporta il tuo elenco di canzoni riprodotte di recente come M3U, CSV o TXT. Le istruzioni dettagliate sono disponibili [qui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Preferiti

Gestisci l'elenco delle tue canzoni preferite.

- **Modifica Simultanea** — quando abilitato, aggiungere una canzone ai preferiti la aggiunge sia nella libreria musicale che nella sezione file contemporaneamente.
- **Elimina Elenco** — elimina l'intero elenco delle canzoni preferite.
- **Esporta Elenco Canzoni** — come Recenti, esporta i preferiti come M3U, CSV o TXT.

### Elimina Libreria Musicale

Cancella il database della libreria musicale. I tuoi file musicali nell'archiviazione vengono lasciati intatti.

## Codice di Accesso

Attiva la schermata di protezione con password se vuoi proteggere i dati della tua applicazione.

## Gestore File

La sezione Gestore File controlla come i file vengono trasferiti, archiviati e visualizzati in anteprima.

### Trasferimenti File

Scegli la tua preferenza di rete per scaricare file sul tuo dispositivo.

### Numero Massimo di Attività Parallele

Imposta il numero di thread di download paralleli. Un numero più alto accelera i download ma richiede più batteria.

### Attività di Trasferimento File

Visualizza le attività di caricamento e download attualmente attive.

### Trasferimenti in Background

Consenti i download mentre l'app è in background. Se i trasferimenti in background consumano molta energia, iOS potrebbe sospendere l'app.

### Salva File Scaricati In

Scegli la directory di download predefinita o fai in modo che l'app ti chieda ogni volta.

### Cartelle Offline Sincronizzate

Gestisci la sincronizzazione offline per le cartelle selezionate. Per abilitare la sincronizzazione offline, tocca il pulsante con i tre punti accanto a una cartella e seleziona **Modalità Disponibile Offline**. I nuovi file aggiunti alla cartella cloud vengono scaricati automaticamente sul tuo dispositivo. Leggi di più sulle modalità offline [qui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervallo di Tempo

Scegli con quale frequenza le cartelle offline vengono sincronizzate. **Immediatamente** avvia una sincronizzazione ogni volta che apri l'app.

### Mostra Nomi File Completi

Mostra i nomi file completi, incluse le estensioni, nel gestore file.

### Modifica File Online

Disabilita la modifica dei file online per passare alla modalità di sola lettura per i servizi cloud connessi e prevenire eliminazioni accidentali. Questa azione rimuove le operazioni di modifica file dall'interfaccia utente.

### Copia File all'Apertura

Specifica come l'app gestisce i file importati da altre applicazioni.

### Miniature per File

Gestisci ed elimina le miniature dei file generate per liberare spazio di archiviazione.

### Elimina File Temporanei

Svuota la cartella cache dell'applicazione per recuperare spazio di archiviazione.

## Editor Tag Audio

Configura l'editor di tag audio integrato.

### Ridimensionamento Copertina Album

Scegli il metodo di ridimensionamento usato quando una copertina dell'album viene salvata nei tag audio.

### Aggiorna File Online

Quando abilitato, l'applicazione aggiorna automaticamente i metadati di un file sul server cloud dopo aver terminato la modifica.

### Elimina File Dopo la Modifica Online

Scegli se l'applicazione deve eliminare la copia scaricata dopo aver terminato la modifica di un file online su un server cloud.

### Pulsanti Schermata Principale

Scegli quali pulsanti sono visibili nella schermata principale dell'editor di tag audio.

## Widget

Abilita i widget in modo che l'app aggiorni i dati dei widget durante la riproduzione. Gli aggiornamenti dei widget richiedono energia aggiuntiva, quindi abilita questo solo se usi effettivamente i widget nella tua schermata Home o schermata di blocco.

Puoi leggere di più sui widget Evermusic nella [guida Navigazione](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Modifica le impostazioni CarPlay qui. Questo menu è disponibile anche all'interno dell'interfaccia CarPlay in modo da poter regolare l'esperienza durante la guida.

### Ordina

Configura le opzioni di ordinamento per tutte le schermate CarPlay.

### Limite Caricamento Contenuti

Scegli se l'app usa la paginazione nella schermata CarPlay. La paginazione mantiene i menu reattivi sui dispositivi con memoria limitata e librerie di grandi dimensioni.

### Colore Gradiente Icone Menu

Seleziona la combinazione di colori per la schermata home di CarPlay.

### Mostra Immagini

Disabilita le immagini nella schermata CarPlay per ottimizzare la velocità di caricamento e ridurre l'utilizzo della memoria su librerie di grandi dimensioni.

### Metti in Pausa la Riproduzione Quando Connesso

Abilita questo per evitare audio improvvisamente forte quando colleghi il dispositivo a CarPlay.

## Wi-Fi Drive

Attiva Wi-Fi Drive per trasferire file da un computer al tuo dispositivo usando un browser web desktop. Le istruzioni dettagliate su come usare Wi-Fi Drive sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizzazione

Personalizza l'interfaccia utente secondo le tue preferenze.

### Icona Applicazione

Scegli un'icona alternativa dell'applicazione per la tua schermata Home.

### Schema Colori

Scegli il tema dell'interfaccia utente e abilita la modalità scura. Quando è selezionato **Default**, l'applicazione segue le impostazioni di aspetto a livello di dispositivo.

### Stile Sfondo

Modifica lo stile dello sfondo dell'applicazione. Attualmente l'unica opzione è **Copertina Album Sfocata**, che usa l'artwork del brano attualmente in riproduzione come sfondo dell'app sfocato.

### Aspetto degli Elementi nell'Elenco

Regola come gli elementi sono visualizzati negli elenchi. Utile su schermi piccoli — puoi lasciare che l'app regoli automaticamente l'altezza delle righe in base al contenuto, o mostrare icone più piccole nelle celle dell'elenco per dare più spazio al testo.

### Limite Caricamento Contenuti

Per impostazione predefinita l'applicazione usa la paginazione per velocizzare il caricamento dei contenuti. Puoi disabilitare la paginazione per caricare tutto in una volta.

### Stile Schermata File Locali

Cambia lo stile di presentazione della sezione **File Locali**.

### Stile Schermata Libreria Musicale

Personalizza l'aspetto della schermata **Libreria Musicale**.

### Stile Schermata Lettore Audio

Configura l'aspetto della schermata **Lettore Audio**.

### Stile Menu Contestuale

Scegli lo stile del menu contestuale mostrato quando tocchi il pulsante Altre Azioni.

## Finestra

Disponibile su Mac e Catalyst. Configura le preferenze relative alla finestra come la dimensione predefinita e il comportamento all'avvio.

## Schermo

Scegli se lo schermo deve rimanere attivo mentre usi l'applicazione. Utile quando si scansionano grandi librerie o si eseguono lavori di modifica tag prolungati.

## Accessibilità

Attiva la **Modalità Testo** per nascondere tutte le immagini nell'interfaccia utente. La modalità Testo viene abilitata automaticamente quando VoiceOver è attivo ed è utile anche per configurazioni molto piccole o solo testo.

## Lingua

Cambia la lingua dell'applicazione e sovrascrivi il predefinito del sistema. Attualmente l'app supporta le seguenti localizzazioni: Afrikaans, Akan, Albanese, Amarico, Arabo, Armeno, Assamese, Aymara, Azerbaigiano, Bambara, Bangla, Basco, Bielorusso, Bosniaco, Bulgaro, Birmano, Catalano, Cebuano, Cinese Semplificato, Cinese Tradizionale, Corso, Croato, Ceco, Danese, Divehi, Dogri, Olandese, Inglese, Esperanto, Estone, Ewe, Filipino, Finlandese, Francese, Galiziano, Ganda, Georgiano, Tedesco, Greco, Guaraní, Gujarati, Creolo Haitiano, Hausa, Hawaiano, Ebraico, Hindi, Hmong, Ungherese, Islandese, Igbo, Iloko, Indonesiano, Irlandese, Italiano, Giapponese, Giavanese, Kannada, Kazako, Khmer, Kinyarwanda, Coreano, Krio, Curdo, Curdo Sorani, Kirghiso, Laotiano, Latino, Lettone, Lingala, Lituano, Lussemburghese, Macedone, Maithili, Malgascio, Malese, Malayalam, Maltese, Māori, Marathi, Mizo, Mongolo, Nepalese, Sotho del Nord, Norvegese Bokmål, Nyanja, Odia, Oromo, Pashtu, Persiano, Polacco, Portoghese, Punjabi, Rumeno, Russo, Samoano, Sanscrito, Gaelico Scozzese, Serbo, Shona, Sindhi, Singalese, Slovacco, Sloveno, Somalo, Sotho Meridionale, Spagnolo, Sundanese, Swahili, Svedese, Tagico, Tamil, Tataro, Telugu, Thai, Tsonga, Turco, Turcmeno, Ucraino, Urdu, Uiguro, Uzbeko, Vietnamita, Gallese, Xhosa, Yiddish, Yoruba, Zulu.

## Backup e Ripristino

Esegui il backup di tutti i dati dell'applicazione o eseguine la migrazione a un altro dispositivo. Puoi scegliere cosa includere:

- **Database** — tutti i brani e le playlist della tua libreria musicale. I brani offline non sono inclusi per mantenere la dimensione del backup gestibile.
- **Copertine Album** — tutte le copertine degli album nella cache.
- **Impostazioni** — tutte le impostazioni dell'applicazione.

Tocca **Backup Dati Applicazione** per avviare l'operazione di backup. I dati dell'applicazione vengono scritti in un singolo file che puoi usare in seguito per ripristinare lo stato dell'applicazione su un nuovo dispositivo o dopo aver reinstallato l'app.

Per ripristinare i dati dell'applicazione su un nuovo dispositivo, sposta il file di backup sul nuovo dispositivo usando un servizio cloud connesso o iCloud e aprilo sul nuovo dispositivo.

Abbiamo una guida dettagliata passo per passo qui: [Come Trasferire la Tua Libreria Musicale tra Dispositivi in Evermusic: Guida Passo per Passo](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Aiuto

Apri la guida dell'applicazione per assistenza e guida sull'utilizzo efficace dell'app.

## Domande Frequenti

Trova le risposte alle domande comuni nella sezione FAQ.

## Invia Feedback

Hai feedback o hai bisogno di assistenza? Invia il tuo feedback al nostro team di supporto direttamente dall'app.

## Condividi Questa App

Condividi l'applicazione con i tuoi amici per aiutare a diffondere la parola.

## Scopri Altre App

Esplora altre app di Everappz.

## Termini e Condizioni

Descrive i termini e le condizioni per l'utilizzo dell'applicazione. Si prega di leggerlo prima di usare l'applicazione.

## Informativa sulla Privacy

Visita la pagina dell'informativa sulla privacy per comprendere le nostre pratiche di gestione dei dati. Si prega di leggerlo prima di usare l'applicazione.

## Analitiche e Raccolta Dati

Controlla quali servizi sono abilitati per le analitiche e la raccolta dei dati e disattiva quelli che non vuoi.

In **Evermusic Free (icona blu)**, le analitiche e la diagnostica sono abilitate per impostazione predefinita per aiutarci a migliorare l'app — puoi disattivarle qui in qualsiasi momento. **Evermusic Pro (icona rossa) non include alcuna analitiche o diagnostica** — la sezione è vuota (o nascosta) perché non viene raccolto nulla, e non c'è opzione di opt-in.

## Note Legali

Contiene informazioni su ogni libreria usata nell'applicazione insieme al numero di versione dell'app e alle informazioni di build.
