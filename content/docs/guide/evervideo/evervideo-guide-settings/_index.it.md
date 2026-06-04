---
title: "Impostazioni"
date: 2020-02-01
lastmod: 2026-06-01
description: "Esplora ogni impostazione di Evervideo — Lettore Media (Picture-in-Picture, decodifica hardware H.264 / HEVC, equalizzatore video, ridimensionamento, rotazione, viewport VR), Audio (equalizzatore, sample rate, canali, IO buffer, modalità mista), Sottotitoli (primario / secondario, font, file esterno, libass), Libreria Media, Gestore File, Wi-Fi Drive, Widget, Personalizzazione, Lingua, Codice d'Accesso, Backup e Ripristino — per iPhone, iPad e Mac."
keywords: [
  "impostazioni Evervideo", "configurazione lettore video", "upgrade premium Evervideo",
  "impostazioni Picture-in-Picture", "impostazioni equalizzatore video",
  "modalità ridimensionamento video", "rotazione video", "decoder hardware iPhone",
  "impostazioni sottotitoli", "sottotitolo secondario iOS", "impostazioni libass",
  "file sottotitolo esterno", "font sottotitolo",
  "impostazioni equalizzatore audio", "sample rate output audio",
  "canali output audio", "durata IO buffer", "modalità mista audio",
  "WiFi Drive video", "widget Evervideo",
  "backup ripristino Evervideo", "codice accesso Evervideo",
  "lingua Evervideo", "personalizzazione Evervideo"
]
tags: ["guida", "evervideo", "impostazioni"]
readingTime: 16
---


La schermata Impostazioni è il centro di controllo di Evervideo. Da qui puoi eseguire l'upgrade a Premium, configurare i motori video e audio (codec di sistema o FFmpeg), gestire il Picture-in-Picture, impostare i sottotitoli (primario, secondario, libass, file esterni, font), organizzare la libreria media, impostare il gestore file, abilitare i widget della Schermata Home, eseguire il backup dei tuoi dati e accedere alle informazioni di aiuto e legali. Le sezioni sono raggruppate sotto intestazioni: Acquisti e Aggiornamenti, Preferenze app, Aiuto, Legale e Privacy.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Principale Impostazioni Evervideo" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Upgrade a Premium

Aggiorna l'applicazione alla versione Premium per rimuovere tutti i limiti. La versione gratuita dell'applicazione offre un acquisto in-app una tantum a vita e due opzioni di abbonamento (1 mese e 1 anno) per rimuovere tutte le restrizioni e eseguire l'upgrade a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Upgrade a Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Condivisione in Famiglia** è abilitata per tutti gli acquisti e i piani, così puoi condividere la versione Premium con un massimo di cinque membri della tua famiglia senza costi aggiuntivi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Seleziona un Piano Premium" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Condivisione degli Acquisti tra iOS e Mac

Gli acquisti a vita e gli abbonamenti sono condivisi tra iOS e Mac usando **iCloud** per sincronizzare queste informazioni. Se hai Premium sul tuo dispositivo iOS, assicurati di avere l'ultima versione installata e che iCloud sia abilitato. Avvia l'app su iOS e attendi un minuto che le informazioni sull'acquisto vengano caricate su iCloud, poi avvia la versione Mac — Premium dovrebbe attivarsi automaticamente.

Puoi anche toccare il pulsante **Ripristina Acquisti** nelle impostazioni dell'app. Assicurati di avere una connessione internet e di aver effettuato l'accesso allo stesso account iCloud e App Store su entrambi i dispositivi.

## Ripristina Acquisti su un Nuovo Dispositivo

Per ripristinare il tuo acquisto su un nuovo dispositivo, usa il menu **Acquisti → Ripristina Acquisti**. Vedrai l'elenco dei tuoi acquisti. Se non li vedi tutti, conferma che il dispositivo sia connesso allo stesso Apple ID utilizzato per effettuare gli acquisti e assicurati che iCloud sia abilitato.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Acquisti Evervideo nelle Impostazioni" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Prova Premium Gratis

Puoi eseguire l'upgrade alla versione Premium gratuitamente, per un periodo limitato, utilizzando questo menu. Basta guardare una pubblicità o parlare ai tuoi amici dell'app.

## Aggiornamento Software

Tocca **Aggiornamento Software** per verificare se è disponibile una versione più recente di Evervideo sull'App Store.

## Novità

Questo menu è disponibile dopo il rilascio di una nuova versione. Mostra un riepilogo delle modifiche e delle nuove funzionalità nell'aggiornamento più recente.

## Lettore

Tutto ciò che riguarda la riproduzione è qui — audio, video, sottotitoli, dispositivi, personalizzazione, cache e timer di stop.

### Generale

Queste impostazioni coprono gli aspetti fondamentali del lettore.

- **Modalità Ripetizione** — scegli come si comporta il lettore quando un video termina:
  - **Ripeti Tutto** — riproduce ogni video nella tua coda.
  - **Ripeti Uno** — ripete solo il video corrente.
  - **Stop Ripetizione** — mette in pausa quando il video corrente termina.
  - **Nessuna Ripetizione** — riproduce la coda una volta senza ripetere.
- **Modalità Casuale** — randomizza l'ordine dei video nella tua coda (**On** o **Off**).
- **Salva Posizione di Riproduzione** — salva e ripristina la posizione di riproduzione per i video nella tua libreria.
- **Salva Stato Lettore** — preserva lo stato del lettore prima di chiudere l'app, così puoi riprendere da dove hai lasciato.

### Video

Configura come Evervideo decodifica e renderizza il video.

- **Decodifica Hardware H.264** — attiva / disattiva la decodifica AVC con accelerazione hardware. Usa quando le prestazioni della batteria e termiche sono importanti; disattiva per compatibilità con profili esotici.
- **Decodifica Hardware H.265 (HEVC)** — uguale per HEVC. iPhone, iPad e Mac moderni decodificano HEVC in modo efficiente.
- **Formato Pixel Preferito** — scegli il formato pixel che il lettore presenta al renderer (i valori predefiniti sono ottimizzati per il dispositivo).
- **FPS Preferiti** — imposta un FPS di riproduzione target. Utile per abbinare una frequenza di aggiornamento specifica del monitor.
- **Modalità Ridimensionamento Video** — Adatta / Riempi / Allunga / Originale. Determina come l'immagine riempie l'area di visualizzazione.
- **Modalità Visualizzazione Video** (iOS / iPadOS) — come il video viene presentato nella vista lettore.
- **Rotazione Video** — ruota manualmente l'immagine 0° / 90° / 180° / 270° (utile per i video registrati con orientamento errato).
- **Equalizzatore Video** — regola luminosità, contrasto, saturazione e tonalità con anteprima in tempo reale. I preset personalizzati possono essere **esportati e importati**.
- **Viewport VR** (iOS / iPadOS) — per video sferici a 360°. Trascina per guardarsi intorno, pizzica per ingrandire.
- **Picture-in-Picture (PiP)** (iOS / iPadOS) — abilita il supporto PiP; l'app passa a una finestra lettore mobile quando si mette l'app in background o si tocca il pulsante PiP.

### Audio

Configura la riproduzione audio e l'output.

- **Traccia Audio** — scegli lo stream audio quando un video ne ha più di uno (commento, doppiaggio, ecc.).
- **Equalizzatore Audio** — EQ a 10 bande con preset e preamplificatore. I preset personalizzati possono essere esportati / importati.
- **Sample Rate Output Audio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Utile con DAC esterni.
- **Numero di Canali Output Audio** — Mono, Stereo, 5.1, ITU BS.775-1, SDDS e altri.
- **Durata IO Buffer Output Audio Preferita** — il valore tipico per la riproduzione hi-res a bassa latenza è intorno a 5 ms (0,005 s). Regola per il tuo hardware.
- **Modalità Output Audio** (solo iOS) — la modalità mista consente all'audio di Evervideo di mescolarsi con altre app.

### Sottotitoli

Evervideo include un supporto completo per i sottotitoli.

- **Traccia Sottotitoli** — scegli tra le tracce di sottotitoli incorporate nel file.
- **File Sottotitolo Esterno** — carica un file `.srt`, `.vtt`, `.ass` o `.ssa` esterno dal tuo dispositivo o da qualsiasi servizio cloud connesso.
- **Font** — scegli un font per la traccia dei sottotitoli primaria.

### Dispositivi (Solo iOS/iPadOS)

Scegli un dispositivo **AirPlay** o **Google Chromecast** per l'output video.

### Personalizzazione

- **Stile Layout Lettore** — Minimalista (predefinito per Evervideo), Inferiore, Antico, Classico e altri.
- **Azioni Schermata Principale** — scegli quali pulsanti compaiono sulla schermata principale del lettore.
- **Controlli Schermata di Blocco** — Tempo di Salto, Aggiungi Segnalibro, Aggiungi ai Preferiti.
- **Intervalli di Tempo di Salto** — scegli l'intervallo di tempo per i pulsanti di salto (5 s, 10 s, 15 s, 30 s, ecc.).
- **Stile Scorrimento Copertine Album** — stile di scorrimento preferito per le copertine.
- **Elementi Aggiuntivi** — Informazioni Formato Audio, Cursore Volume.

### Caricamento File

Configura come i dati video vengono trasmessi dalla rete.

- **Tipo di Rete** — solo Wi-Fi, o Wi-Fi + Cellulare.
- **Tempo di Precaricamento** — lunghezza del buffer per una riproduzione più fluida su reti lente.
- **Usa URL Diretto** — quando supportato, usa un URL diretto per un caricamento più veloce.

### Cache di Riproduzione

I video nella coda del lettore vengono scaricati automaticamente per garantire una riproduzione fluida. Puoi disabilitare questa opzione o configurare la dimensione della cache qui.

### Timer di Stop

Attiva un timer per fermare automaticamente la riproduzione dopo un periodo specificato. Tocca l'icona di configurazione per la **modalità precisa** con granularità minuto per minuto.

## Libreria Media

Gestisci sincronizzazione automatica, metadati, copertine album, playlist, recenti e preferiti.

### Lettura Metadati

Quando aggiungi video alla libreria, il lettore di metadati li scansiona in background e li organizza per Album e Genere. Puoi regolare la velocità di scansione, disabilitare il lettore, o attivare una riscansione completa con **Ricarica Metadati**. **Normalizza Codifica Metadati** corregge automaticamente le codifiche dei caratteri corrotte (comune con file da PC Windows).

### Sincronizzazione Online

Aggiungi automaticamente video da servizi cloud connessi e server multimediali alla tua libreria. Scegli quali cartelle scansionare, configura la frequenza di sincronizzazione e avvia / interrompi la sincronizzazione manualmente. La sincronizzazione online funziona solo mentre l'app è attiva — per librerie grandi, usa la versione desktop e poi trasferisci la libreria sincronizzata con **Backup e Ripristino**.

### Sincronizzazione Offline

Quando contrassegni una cartella cloud come disponibile offline, appare in **File → Cartelle Offline** e viene scaricata automaticamente. I nuovi file aggiunti online vengono anch'essi scaricati. Configura l'intervallo di tempo e avvia sincronizzazioni manuali da questa schermata.

### Personalizzazione

- **Stile Schermata Libreria Media** — Menu Normale, Menu Raggruppato, Menu a Schede.
- Attiva/disattiva la visualizzazione di grandi copertine album nelle schermate di dettaglio.

### Copertine Album

- **Tipo di Rete** — Wi-Fi o Wi-Fi + Cellulare.
- **Carica Copertine Album per File Online** — recupera le copertine incorporate dai file cloud (usa dati extra).
- **Cerca nella Cartella** — usa immagini JPEG / PNG nella stessa cartella quando un video non ha una copertina incorporata.
- **Qualità Copertina** — regola la risoluzione alla quale le copertine vengono memorizzate nella cache.
- **Mostra nella Cartella** / **Elimina Tutto** — gestisci la cache delle copertine.

### Playlist

Abilita l'aggiunta dello stesso video a una playlist due volte (disabilitato per impostazione predefinita).

### Recenti

Gestisci l'elenco dei video riprodotti di recente — cambia la dimensione, elimina, o esporta come M3U / CSV / TXT.

### Preferiti

- **Modifica Simultanea** — specchia i preferiti tra la libreria media e la sezione file.
- **Elimina Lista** — svuota l'elenco dei preferiti.
- **Esporta Lista Brani** — esporta i preferiti come M3U / CSV / TXT.

### Elimina Libreria Media

Cancella il database della libreria media. I tuoi file video e audio nell'archiviazione rimangono intatti.

## Codice d'Accesso

Proteggi Evervideo con un **codice d'accesso numerico a 4 cifre**. Quando abilitato, ti verrà chiesto di inserire il codice d'accesso ogni volta che l'app viene avviata. Combinalo con iOS Face ID / Touch ID sul dispositivo per una protezione aggiuntiva.

## Gestore File

Controlla come i file vengono trasferiti, archiviati e visualizzati in anteprima.

- **Trasferimenti File** — preferenza di rete (solo Wi-Fi o Wi-Fi + Cellulare).
- **Numero Massimo di Attività Parallele** — imposta il numero di thread di download paralleli.
- **Attività di Trasferimento File** — visualizza upload e download attualmente attivi.
- **Trasferimenti in Background** — consenti i download mentre l'app è in background.
- **Salva File Scaricati In** — directory di download predefinita.
- **Cartelle Offline Sincronizzate** — gestisci le cartelle in modalità offline.
- **Intervallo di Tempo** — con quale frequenza le cartelle offline vengono controllate per le modifiche.
- **Mostra Nomi File Completi** — mostra le estensioni nel gestore file.
- **Modifica File Online** — disabilita per passare alla modalità di sola lettura per i servizi cloud connessi.
- **Copia File all'Apertura** — come gestire i file importati da altre app.
- **Miniature per File** — gestisci le miniature file generate.
- **Elimina File Temporanei** — svuota la cartella cache dell'applicazione.

## Wi-Fi Drive

Attiva Wi-Fi Drive per trasferire file da un computer al tuo dispositivo utilizzando un browser web desktop, Finder o Esplora File. Istruzioni dettagliate disponibili [qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widget

Abilita i widget in modo che l'app aggiorni i dati dei widget durante la riproduzione. Gli aggiornamenti dei widget richiedono energia aggiuntiva, quindi l'interruttore è disattivato per impostazione predefinita — abilitalo solo se usi effettivamente i widget sulla tua Schermata Home o Schermata di Blocco.

Puoi aggiungere widget Evervideo tenendo premuto la tua Schermata Home o Schermata di Blocco, toccando **+**, cercando **Evervideo** e scegliendo una dimensione del widget. I widget mostrano il video in riproduzione e portano direttamente al lettore a schermo intero. I widget funzionano anche su macOS nel Centro Notifiche.

## Personalizzazione

Personalizza l'interfaccia utente secondo le tue preferenze.

- **Icona Applicazione** — icona alternativa della Schermata Home (Premium).
- **Schema Colori** — Scuro, Chiaro o Predefinito (segue l'aspetto del sistema).
- **Stile Sfondo** — Copertina Album Sfocata o colore solido.
- **Aspetto degli Elementi nell'Elenco** — regola automaticamente l'altezza delle righe; mostra miniature più piccole.
- **Limite Caricamento Contenuto** — attiva / disattiva la paginazione.
- **Stile Schermata File** — Menu Normale o Menu Raggruppato.
- **Stile Schermata Libreria Media** — Menu Normale / Raggruppato / a Schede.
- **Stile Schermata Lettore** — Minimalista / Inferiore / Antico / Classico.
- **Stile Menu Contestuale** — menu di sistema o stile pannello inferiore.

## Finestra

Disponibile su Mac e Catalyst. Configura le preferenze relative alla finestra come la dimensione predefinita e il comportamento all'avvio.

## Schermo

Scegli se lo schermo deve rimanere attivo mentre stai usando l'applicazione.

## Accessibilità

Attiva la **Modalità Testo** per nascondere le immagini nell'interfaccia utente. La Modalità Testo viene abilitata automaticamente quando VoiceOver è attivo.

## Lingua

Cambia la lingua dell'applicazione e sostituisci l'impostazione predefinita del sistema. La modifica viene applicata dopo aver completamente chiuso e riaperto Evervideo. Sono supportate oltre 120 lingue.

## Backup e Ripristino

Esegui il backup di tutti i dati dell'applicazione o migrali su un altro dispositivo. Scegli cosa includere:

- **Database** — le voci della libreria media, playlist, valutazioni, preferiti, cronologia visione. I file offline non sono inclusi per mantenere la dimensione del file gestibile.
- **Copertine Album** — le tue copertine nella cache.
- **Impostazioni** — le impostazioni dell'applicazione.

Tocca **Esegui Backup Dati Applicazione** per avviare il backup. Per ripristinare su un nuovo dispositivo, sposta il file di backup tramite iCloud Drive, AirDrop o qualsiasi servizio cloud connesso e aprilo sul nuovo dispositivo.

## Aiuto

Accedi alla guida dell'applicazione per assistenza e indicazioni sull'utilizzo efficace dell'app.

## Domande Frequenti

Trova risposte alle domande comuni nella sezione FAQ.

## Invia Feedback

Invia il tuo feedback al nostro team di supporto direttamente dall'app, con informazioni diagnostiche allegate automaticamente.

## Condividi Questa App

Condividi Evervideo con i tuoi amici per diffondere la notizia.

## Scopri Altre App

Esplora altre app di Everappz.

## Termini e Condizioni

Leggi i termini e le condizioni prima di utilizzare l'applicazione.

## Informativa sulla Privacy

Leggi l'informativa sulla privacy per comprendere le nostre pratiche di gestione dei dati.

## Analisi e Raccolta Dati

Controlla quali servizi sono abilitati per analisi e raccolta dati e disattiva quelli che non desideri.

## Note Legali

Informazioni su ogni libreria utilizzata nell'applicazione insieme al numero di versione dell'app e alle informazioni di build.
