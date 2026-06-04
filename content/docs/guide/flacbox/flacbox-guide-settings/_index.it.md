---
title: "Impostazioni"
date: 2020-02-01
description: "Esplora ogni impostazione in Flacbox — dalle preferenze di riproduzione, il motore audio FFmpeg / sistema, output audio Hi-Res, regolazioni dell'equalizzatore, correzione intonazione, durata buffer IO, sincronizzazione metadata, controllo playlist, trasferimenti file, widget Schermata Home, Apple CarPlay, personalizzazione UI, lingua, codice d'accesso, backup e ripristino, e aggiornamento Premium."
keywords: [
  "impostazioni Flacbox", "configurazione lettore audio", "aggiornamento premium Flacbox",
  "WiFi Drive", "sincronizzazione metadati", "equalizzatore", "velocità di riproduzione",
  "duplicati playlist", "impostazioni gestore file", "sincronizzazione musica offline",
  "editor tag audio", "modalità scura", "ripristina acquisti", "impostazioni backup",
  "impostazioni widget Flacbox", "impostazioni CarPlay Flacbox",
  "impostazioni FFmpeg Flacbox", "impostazioni sample rate Flacbox",
  "impostazioni correzione intonazione Flacbox", "IO buffer Flacbox",
  "codice accesso Flacbox", "lingua Flacbox", "personalizzazione Flacbox",
  "analitiche Flacbox"
]
tags: ["guida", "flacbox", "impostazioni"]
readingTime: 16
---


La schermata Impostazioni è il centro di controllo di Flacbox. Da qui puoi passare a Premium, configurare il motore audio (codec di sistema o FFmpeg), gestire la tua libreria musicale, configurare il gestore file, personalizzare l'editor tag audio, abilitare i widget della Schermata Home e Apple CarPlay, eseguire il backup dei tuoi dati e accedere a guida e informazioni legali.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Principale Impostazioni Flacbox" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Aggiorna a Premium

Aggiorna l'applicazione alla versione Premium per rimuovere tutti i limiti. La versione gratuita dell'applicazione offre un acquisto in-app una tantum a vita e due opzioni di abbonamento (1 mese e 1 anno) per rimuovere tutte le restrizioni e passare a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Aggiorna a Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**La Condivisione in Famiglia** è abilitata per tutti gli acquisti e i piani, quindi puoi condividere la versione Premium con fino a cinque membri della tua famiglia senza costi aggiuntivi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Seleziona un Piano Premium" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Puoi leggere di più sugli acquisti e sulla versione Premium qui: [Qual è la differenza tra Flacbox e Flacbox Premium](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/).

## Condivisione degli Acquisti tra iOS e Mac

Gli acquisti a vita e gli abbonamenti sono condivisi tra iOS e Mac, usando iCloud per sincronizzare queste informazioni. Se hai la versione Premium sul tuo dispositivo iOS, assicurati di avere installata l'ultima versione e che iCloud sia abilitato. Avvia l'app su iOS e aspetta un minuto affinché le informazioni sul tuo acquisto vengano caricate su iCloud.

Puoi anche provare a toccare il pulsante Ripristina Acquisti nelle impostazioni dell'app. Successivamente, installa l'ultima versione dell'app dall'App Store sul tuo Mac e avvia l'app.

## Ripristinare gli Acquisti su un Nuovo Dispositivo

Per ripristinare il tuo acquisto su un nuovo dispositivo, usa il menu Acquisti → Ripristina Acquisti. Vedrai l'elenco dei tuoi acquisti. Se non li vedi tutti, conferma che il dispositivo sia connesso allo stesso Apple ID utilizzato per effettuare gli acquisti e assicurati che iCloud sia abilitato.

## Prova Premium Gratis

Puoi passare alla versione Premium gratuitamente, per un periodo limitato, usando questo menu.

## Acquisti

Puoi ripristinare gli acquisti precedenti da questo menu. Se riscontri errori di attivazione, prova ad abilitare l'opzione Ripristina Acquisti all'Avvio dell'App.

## Aggiornamento Software

Tocca Aggiornamento Software per verificare se è disponibile una versione più recente di Flacbox.

## Novità

Questo menu è disponibile dopo il rilascio di una nuova versione. Mostra un riepilogo delle modifiche e delle nuove funzionalità nell'aggiornamento più recente.

## Lettore Audio

Questa sezione configura il lettore audio e il motore audio sottostante, inclusa la scelta FFmpeg / codec di sistema e le opzioni di output audio Hi-Res.

### Generale

- **Modalità Ripetizione** — scegli come si comporta il lettore audio quando una traccia finisce:
  - **Ripeti Tutto** — riproduce di nuovo tutte le tracce nella coda.
  - **Ripeti Uno** — ripete solo la traccia corrente.
  - **Ferma Ripetizione** — mette in pausa la riproduzione quando la traccia corrente finisce.
  - **Nessuna Ripetizione** — lascia che la coda venga riprodotta senza ripetere.
- **Modalità Casuale** — randomizza l'ordine delle tracce nella coda. Puoi impostarlo su **Casuale Disattivato** o **Casuale Attivato**.
- **Codec Audio** — scegli il motore audio usato per la riproduzione:
  - **System Codec + FFmpeg** — prioritizza il codec audio di sistema dove possibile, migliorando compatibilità e stabilità.
  - **FFmpeg** — forza il codec FFmpeg per tutti i file audio, abilitando la correzione intonazione e il sample rate di output audio.
- **Sample Rate Output Audio** — regola il sample rate di output audio per ottimizzare la qualità del suono, specialmente utile con un DAC esterno. Valori disponibili: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** e **96 kHz**.
- **Numero di Canali Output Audio** — per sistemi audio multicanale con DAC esterno, specifica il numero di canali: Mono, Stereo, Center / Left / Right, ecc.
- **Durata IO Buffer Output Audio Preferita** — configura la durata del buffer. Un valore tipico per minimizzare la latenza è circa **5 millisecondi (0,005 secondi)**.
- **Modalità Output Audio (solo iOS)** — configura la modalità di output audio misto. Istruzioni dettagliate [qui](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Salva Posizione di Riproduzione** — salva e ripristina la posizione di riproduzione.
- **Salva Stato Lettore Audio** — preserva lo stato del lettore audio prima di chiudere l'app.

### Personalizzazione

- **Stile Schermata Lettore Audio** — configura il posizionamento degli elementi.
- **Stile Scorrimento Copertine Album** — configura lo stile di scorrimento preferito.
- **Elementi Aggiuntivi** — abilita elementi extra sulla schermata del lettore audio.
- **Azioni Schermata Principale** — configura quali pulsanti devono essere visibili per impostazione predefinita.
- **Controlli Riproduzione sulla Schermata di Blocco** — scegli quali controlli appaiono sulla schermata di blocco.
- **Pulsanti Salta Tempo** — scegli l'intervallo di tempo per i pulsanti Salta Tempo.

### Caricamento File

- **Tempo di Precaricamento** — imposta l'intervallo di tempo del buffering. Aumentalo se hai una connessione di rete scarsa.
- **Usa URL Diretto** — se abilitato, viene usato un URL diretto per caricare il brano se il server lo supporta.

### Equalizzatore Audio

Configura l'equalizzatore audio a 10 bande. Puoi leggere di più [qui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocità di Riproduzione

Regola la velocità di riproduzione del lettore audio da **0,02× a 3,00×**.

### Correzione Intonazione

Cambia le impostazioni di correzione intonazione. Disponibile nel percorso del codec FFmpeg, con un intervallo da **-1000 a +1000**.

### Cache di Riproduzione

I brani nella coda del lettore audio vengono scaricati automaticamente per garantire una riproduzione fluida. Puoi anche configurare la dimensione della cache del lettore audio qui.

### Timer Sonno

Attiva un timer per fermare automaticamente la riproduzione dopo un periodo specificato.

## Libreria

Le impostazioni della tua libreria musicale — sincronizzazione automatica, lettura metadati, caricamento copertine album, playlist, recenti e preferiti — si trovano qui.

### Lettura Metadati

Quando aggiungi tracce alla libreria, il **lettore di metadati** entra in azione. Questo processo in background legge tutti i metadati dalle tue tracce e li organizza per Artista, Album, Genere e Compositore. Puoi disabilitare il lettore di metadati e visualizzare i nomi dei file al posto delle informazioni sui tag.

**Normalizza Codifica Metadati** normalizza automaticamente la codifica dei metadati per tutti i brani.

### Sincronizzazione Online

La sincronizzazione automatica della musica online aggiunge tracce dai servizi cloud connessi alla libreria musicale automaticamente. Per abilitarla, apri le impostazioni della libreria musicale e seleziona le cartelle di sincronizzazione.

### Sincronizzazione Offline

Configura la sincronizzazione della musica offline. Se contrassegni una cartella online come disponibile offline, appare qui. Il contenuto viene scaricato in **File Locali → Cartelle Offline**.

### Personalizzazione

Configura lo stile della schermata della libreria musicale. Sono disponibili tre opzioni: **Menu Semplice, Menu Raggruppato, Menu a Schede**.

### Copertine Album

- **Tipo di Rete** — scegli Wi-Fi o Wi-Fi e Dati Mobili.
- **Carica Copertine Album per File Online** — carica le copertine album incorporate per i file nel cloud storage.
- **Cerca nella Cartella** — se una traccia non ha copertina incorporata, cerca immagini JPEG o PNG nella stessa cartella.
- **Qualità Copertina** — seleziona la qualità delle copertine album.
- **Mostra nella Cartella** — apri la cartella dove sono memorizzate le copertine album.
- **Elimina Tutto** — elimina le copertine album memorizzate nella cache.

### Playlist

Abilita l'opzione per aggiungere lo stesso brano a una playlist due volte.

### Recenti

- **Elimina Lista** — elimina l'intero elenco dei brani riprodotti di recente.
- **Cambia Dimensione Lista** — imposta il numero di elementi che appaiono nell'elenco.
- **Esporta Lista Brani** — esporta l'elenco dei brani riprodotti di recente.

### Preferiti

- **Modifica Simultanea** — quando abilitato, aggiungere un brano ai preferiti lo aggiunge sia nella libreria musicale che nella sezione file contemporaneamente.
- **Elimina Lista** — elimina l'intero elenco dei brani preferiti.
- **Esporta Lista Brani** — esporta i preferiti.

### Elimina Libreria Musicale

Cancella il database della libreria musicale. I tuoi file musicali nello storage rimangono intatti.

## Codice d'Accesso

Attiva la schermata del codice d'accesso per proteggere i dati della tua applicazione con un codice numerico a 4 cifre.

## Gestore File

La sezione Gestore File controlla come i file vengono trasferiti, archiviati e visualizzati in anteprima.

### Trasferimenti File

Scegli la tua preferenza di rete per scaricare file sul tuo dispositivo.

### Numero Massimo di Attività Parallele

Imposta il numero di thread di download paralleli.

### Attività di Trasferimento File

Mostra le attività di caricamento e download attualmente attive.

### Trasferimenti in Background

Permetti i download mentre l'app è in background.

### Salva File Scaricati In

Scegli la directory di download predefinita.

### Cartelle Offline Sincronizzate

Gestisci la sincronizzazione offline per le cartelle selezionate. Leggi di più sulle modalità offline [qui](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervallo di Tempo

Scegli con quale frequenza vengono sincronizzate le cartelle offline.

### Mostra Nomi File Completi

Mostra i nomi file completi, incluse le estensioni.

### Modifica File Online

Disabilita la modifica online dei file per passare alla modalità sola lettura.

### Copia File all'Apertura

Specifica come l'app gestisce i file importati da altre applicazioni.

### Miniature per File

Gestisci ed elimina le miniature di file generate.

### Elimina File Temporanei

Svuota la cartella cache dell'applicazione.

## Editor Tag Audio

Configura l'editor tag audio integrato.

### Ridimensionamento Copertina Album

Scegli il metodo di ridimensionamento usato quando una copertina album viene salvata nei tag audio.

### Aggiorna File Online

Quando abilitato, l'applicazione aggiorna automaticamente i metadati di un file sul server cloud dopo aver finito di modificarlo.

### Elimina File Dopo la Modifica Online

Scegli se l'applicazione deve eliminare la copia scaricata dopo aver finito la modifica di un file online.

### Pulsanti Schermata Principale

Scegli quali pulsanti sono visibili nella schermata principale dell'editor tag audio.

## Widget

Abilita i widget in modo che l'app aggiorni i dati dei widget durante la riproduzione. Gli aggiornamenti dei widget richiedono energia aggiuntiva, quindi il toggle è disattivato per impostazione predefinita.

## CarPlay

Modifica le impostazioni CarPlay qui.

### Ordina

Configura le opzioni di ordinamento per tutte le schermate CarPlay.

### Limite Caricamento Contenuto

Scegli se l'app usa la paginazione sulla schermata CarPlay.

### Colore Gradiente Icone Menu

Seleziona lo schema colori per la schermata Home CarPlay.

### Mostra Immagini

Disabilita le immagini sulla schermata CarPlay per ottimizzare la velocità di caricamento.

### Metti in Pausa la Riproduzione alla Connessione

Abilita questo per evitare audio improvvisamente alto quando connetti il tuo dispositivo a CarPlay.

## Wi-Fi Drive

Attiva **Wi-Fi Drive** per trasferire file da un computer al tuo dispositivo usando un browser web desktop, Finder o File Explorer. Istruzioni dettagliate su come usare Wi-Fi Drive sono disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalizzazione

Personalizza l'interfaccia utente secondo le tue preferenze.

### Icona Applicazione

Scegli un'icona applicazione alternativa per la tua Schermata Home (Premium).

### Schema Colori

Scegli il tema dell'interfaccia utente e abilita la modalità scura.

### Stile Sfondo

Modifica lo stile dello sfondo dell'applicazione. Attualmente l'unica opzione è **Copertina Album Sfocata**.

### Aspetto degli Elementi nella Lista

Regola come gli elementi vengono visualizzati nelle liste.

### Limite Caricamento Contenuto

Per impostazione predefinita l'applicazione usa la paginazione per velocizzare il caricamento dei contenuti.

### Stile Schermata File Locali

Cambia lo stile di presentazione della sezione **File Locali**.

### Stile Schermata Libreria Musicale

Personalizza l'aspetto della schermata **Libreria Musicale**.

### Stile Schermata Lettore Audio

Configura l'aspetto della schermata **Lettore Audio**.

### Stile Menu Contestuale

Scegli lo stile del menu contestuale mostrato quando tocchi il pulsante **Altre Azioni**.

## Finestra

Disponibile su Mac. Configura le preferenze relative alla finestra.

## Schermo

Scegli se lo schermo deve rimanere attivo mentre usi l'applicazione.

## Accessibilità

Attiva la **Modalità Testo** per nascondere tutte le immagini nell'interfaccia utente. La Modalità Testo viene abilitata automaticamente quando VoiceOver è attivo.

## Lingua

Cambia la lingua dell'applicazione e sovrascrive il default del sistema. La modifica si applica dopo aver completamente chiuso e riaperto Flacbox.

## Backup & Ripristino

Usa questa funzione per eseguire il backup di tutti i dati dell'applicazione o per migrarli su un altro dispositivo. Puoi scegliere cosa includere:

- **Database** — tutte le tue tracce nella libreria musicale, incluse le playlist.
- **Copertine Album** — tutte le copertine album memorizzate nella cache.
- **Impostazioni** — tutte le impostazioni dell'applicazione.

Tocca **Backup Dati Applicazione** per avviare il backup.

Istruzioni dettagliate passo dopo passo: [Come trasferire la tua Libreria Musicale tra dispositivi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Guida

Accedi alla guida dell'applicazione per assistenza e orientamento.

## Domande Frequenti

Trova risposte alle domande comuni nella sezione FAQ.

## Invia Feedback

Hai feedback o hai bisogno di assistenza? Invia il tuo feedback al nostro team di supporto direttamente dall'app.

## Condividi Questa App

Condividi l'applicazione con i tuoi amici.

## Scopri Altre App

Esplora altre app di Everappz.

## Termini e Condizioni

Delinea i termini e le condizioni per l'utilizzo dell'applicazione.

## Informativa sulla Privacy

Visita la pagina dell'informativa sulla privacy per capire le nostre pratiche di gestione dei dati.

## Analitiche e Raccolta Dati

Controlla quali servizi sono abilitati per analitiche e raccolta dati e disattiva quelli che non vuoi.

## Note Legali

Contiene informazioni su ogni libreria utilizzata nell'applicazione insieme al numero di versione dell'app e alle informazioni di build.
