---
title: "Lettore Media"
date: 2020-02-01
lastmod: 2026-06-01
description: "Scopri come usare il lettore media di Evervideo su iPhone, iPad e Mac. Picture-in-Picture, decodifica hardware H.264 / HEVC, equalizzatori audio e video, sottotitoli primari e secondari, selezione delle tracce audio e video, ridimensionamento e rotazione del video, velocità di riproduzione, sleep timer, AirPlay 2, Google Chromecast, stream RTSP e il lettore compatto sempre visibile sullo schermo."
keywords: [
  "guida lettore Evervideo", "impostazioni lettore video", "equalizzatore Evervideo",
  "Picture-in-Picture iPhone", "video PiP iPad", "video PiP Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "sottotitoli video iPhone", "sottotitoli SRT esterni",
  "lettore sottotitoli ASS SSA", "libass iOS",
  "doppi sottotitoli apprendimento lingue",
  "luminosità contrasto equalizzatore video", "equalizzatore audio lettore video",
  "blocco rotazione lettore video", "modalità ridimensionamento video iOS",
  "decoder H.264 hardware iPhone", "decoder HEVC hardware iPad",
  "velocità riproduzione video", "lettore video FFmpeg iOS",
  "lettore RTSP iPhone", "lettore video compatto",
  "lettore video VR 360 iPhone"
]
tags: ["guida", "evervideo", "lettore", "PiP", "sottotitoli", "equalizzatore video"]
readingTime: 14
---


Il Lettore Media è la schermata principale dell'app dove controlli la riproduzione e la maggior parte delle funzionalità di Evervideo. Riproduce sia file video che audio ed è costruito su un lettore personalizzato basato su FFmpeg con decodifica H.264 e HEVC con accelerazione hardware. Scopriamo come usarlo.

## Accedere al Lettore Media

Puoi arrivare al lettore a schermo intero dalla barra del lettore compatto. Su iPhone, il lettore compatto si trova in cima alla schermata principale. Su iPad e Mac, si trova sul lato sinistro (o in cima al pannello principale). Per chiudere il lettore a schermo intero nella vista compatta, tocca il pulsante di chiusura nell'angolo in basso a destra o scorri verso il basso. Per nascondere completamente il lettore compatto, tocca e scorri verso il basso un'altra volta.

Il lettore compatto rimane visibile mentre sfoglie la libreria, il gestore file o le impostazioni, così non perdi mai il video mentre cerchi il prossimo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lettore Media a Schermo Intero di Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formati Video e Audio Supportati

Evervideo riproduce praticamente ogni contenitore e codec moderno attraverso il motore FFmpeg incluso, con decodifica H.264 e HEVC con accelerazione hardware sui dispositivi supportati.

- **Contenitori video:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — e molti altri.
- **Codec video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — più praticamente ogni altro codec supportato da FFmpeg.
- **Codec audio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — e molti altri.
- **Formati sottotitoli:** SRT, VTT (WebVTT), ASS / SSA e tracce di sottotitoli di testo o immagini incorporate.
- **Protocolli streaming:** HTTP / HTTPS, HLS (m3u8), RTSP (telecamere IP e IPTV) e streaming di file diretto tramite SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Questo copre praticamente ogni file video che potresti incontrare — inclusi i rip MKV, gli stream RTSP delle telecamere di sicurezza e i download web AV1 webm.

## Controlli di Riproduzione

In fondo alla schermata del lettore, vedrai i pulsanti Riproduci, Pausa, Avanti e Indietro. Ci sono anche pulsanti opzionali come Salta Avanti e Salta Indietro (predefiniti 10 secondi) che puoi abilitare nelle impostazioni dell'app. Tieni premuto i pulsanti Avanti / Indietro per avanzare o riavvolgere velocemente. Trascina lo slider di riproduzione per saltare a qualsiasi posizione.

## Ripeti e Casuale

Tocca il pulsante di ripetizione per scorrere le modalità di ripetizione:

- **Ripeti Tutto** — riproduce in loop ogni video nella coda.
- **Ripeti Uno** — ripete solo il video corrente.
- **Ripeti Stop** — mette in pausa quando il video corrente finisce.
- **Nessuna Ripetizione** — riproduce la coda una volta senza ripetere.

Usa il pulsante **Casuale** per randomizzare l'ordine dei video nella coda.

## Picture-in-Picture (PiP)

Su iPhone e iPad, Evervideo supporta pienamente Picture-in-Picture (PiP). Tocca l'icona PiP sulla schermata del lettore o semplicemente porta Evervideo in background — il video continua a essere riprodotto in una finestra fluttuante sopra ogni altra app. Trascina la finestra fluttuante in qualsiasi angolo; avvicina le dita per ridimensionare; tocca una volta per visualizzare i controlli di base riproduzione / pausa / salta; tocca il piccolo pulsante di espansione per tornare all'Evervideo completo.

PiP funziona con ogni formato video riprodotto da Evervideo, inclusi i file in streaming cloud e gli stream RTSP. PiP continua anche quando il telefono è bloccato (a seconda delle impostazioni di Auto-Lock).

## Lettore Compatto

Il lettore compatto è un mini lettore persistente che rimane visibile in cima a ogni schermata dell'app mentre sfoglie la libreria, il gestore file o le impostazioni. Toccalo per espanderlo nel lettore a schermo intero; scorri verso il basso per ridurlo di nuovo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Impostazioni Video Evervideo dalla Vista Lettore Compatto nella Schermata Principale" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Per AirPlay, tocca il pulsante AirPlay sul lettore. Evervideo supporta AirPlay 2, così puoi fare streaming di video su Apple TV, HomePod o qualsiasi speaker o smart TV compatibile con AirPlay 2. Su un impianto con più dispositivi AirPlay, puoi instradare l'audio a più ricevitori contemporaneamente.

## Google Chromecast

Per gli utenti Google Cast, l'icona Cast appare sul lettore. Toccala per scegliere un dispositivo e iniziare il casting. Assicurati che il telefono e il ricevitore Cast siano sulla stessa rete Wi-Fi. Non ogni codec è supportato dall'hardware Chromecast — alcuni file potrebbero necessitare di transcoding.

## Stream RTSP Live

Evervideo può riprodurre sorgenti RTSP direttamente — telecamere IP, telecamere citofoniche, stream IPTV, trasmissioni live e qualsiasi URL `rtsp://`. Aggiungi lo stream come connessione RTSP in File → Link Online → Aggiungi link, poi toccalo per iniziare a guardare. Gli stream RTSP funzionano in Picture-in-Picture, nel lettore compatto e possono essere trasmessi tramite AirPlay 2 e Chromecast come un normale video.

## Selezione della Traccia Audio

Per video con più tracce audio (commento, doppiaggi in lingua alternativa, tracce del regista), tocca il pulsante Altre azioni sul lettore e scegli Traccia Audio — poi seleziona la traccia desiderata. Questo è essenziale per film in lingua straniera, file BDMV / MKV con più doppiaggi e contenuti istruttivi con tracce di commento.

## Selezione della Traccia Video

Alcuni file video includono più flussi video (Blu-ray multi-angolo, tagli alternativi). Scegli Traccia Video dal menu Altre azioni per passare tra di loro durante la riproduzione.

## Sottotitoli — Interni ed Esterni

Evervideo ti offre un controllo granulare sui sottotitoli:

- **Traccia sottotitoli** — scegli dalle tracce incorporate nel file.
- **File di sottotitoli esterni** — carica file `.srt`, `.vtt`, `.ass` o `.ssa` dal dispositivo, iCloud Drive o qualsiasi servizio cloud connesso.
- **Rendering Libass** — la stilizzazione avanzata ASS / SSA (font, colori, posizioni, effetti karaoke) viene renderizzata correttamente grazie alla libass inclusa.
- **Selezione font** — scegli un font personalizzato per i sottotitoli primari e un font separato per i sottotitoli secondari. Sono disponibili font incorporati più qualsiasi font installato sul dispositivo.

Puoi configurare tutto questo in Impostazioni → Sottotitoli prima della riproduzione, oppure usa Altre azioni → Sottotitoli dal lettore per cambiare al volo.

## Equalizzatore Audio

Evervideo include un equalizzatore audio completo per sintonizzare le colonne sonore video per le tue cuffie, altoparlanti o impianto hi-fi. Tocca l'icona dell'equalizzatore sulla vista volume (o l'azione Equalizzatore Audio nel menu Altre azioni del lettore), attiva l'equalizzatore con l'interruttore nell'angolo in alto a destra, e poi scegli un preset o trascina gli slider delle bande per creare il tuo preset. I preset personalizzati possono essere esportati e importati così puoi condividerli tra i dispositivi o fare un backup.

## Equalizzatore Video

Per sintonizzare l'immagine, Evervideo fornisce un equalizzatore video dedicato — regola luminosità, contrasto, saturazione e tonalità in tempo reale durante la riproduzione. Come l'equalizzatore audio, i preset video personalizzati possono essere esportati e importati per la condivisione o il backup. Usalo per illuminare una scena buia in una giornata di sole, aumentare la saturazione su contenuti sbiaditi o riscaldare una tonalità di colore fredda.

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizzatore Video di Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Modalità di Ridimensionamento Video

Scegli come il video riempie lo schermo:

- **Adatta** — conserva il rapporto aspetto originale; barre nere dove necessario.
- **Riempi** — riempi l'intero schermo, ritagliando il video se necessario.
- **Allunga** — allunga il video per riempire lo schermo, distorcendolo se necessario.
- **Originale** — mantieni la risoluzione nativa a 1:1.

## Rotazione Video

Per video registrati con l'orientamento sbagliato, scegli **Altre azioni → Rotazione** e scegli **0°**, **90°**, **180°** o **270°** per ruotare l'immagine senza lasciare il lettore.

## Decodifica Hardware (H.264 e HEVC)

In Impostazioni → Lettore → Video, puoi abilitare / disabilitare Decodifica Hardware H.264 e Decodifica Hardware H.265 (HEVC) indipendentemente. La decodifica hardware è più veloce, usa meno batteria e funziona più fredda — ma in rari casi (file corrotti, profili esotici) potresti dover disabilitare la decodifica hardware e tornare alla decodifica software FFmpeg. Evervideo ti permette di farlo file per file dal menu Altre azioni del lettore.

## Viewport VR 360°

Evervideo include un viewport VR / 360° per file video sferici. Quando si riproduce un video a 360°, puoi trascinare per guardare intorno, avvicinare le dita per zoomare, ed Evervideo deformerà il rendering in tempo reale.

## Velocità di Riproduzione

Tocca il controllo Velocità sulla barra degli strumenti del lettore per cambiare la velocità di riproduzione — rallentala per l'analisi (0,25× o 0,5×) o accelerala per tutorial e lezioni (1,25×, 1,5×, 2× e fino a 3×). Tocca l'icona di configurazione nell'angolo in alto a destra della schermata Velocità per passare alla modalità precisa con regolazioni più fini. La correzione del tono per traccia è anche disponibile.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velocità di Riproduzione Evervideo sulla Barra degli Strumenti Principale" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Coda del Lettore

Per vedere la coda del lettore, tocca il pulsante coda sul lettore. Ogni video nella coda ha più azioni — tocca i tre puntini per visualizzarle. Per riordinare un video nella coda, usa l'indicatore di riordino vicino al titolo e trascinalo in una nuova posizione.

{{< cards cols="1">}}
  {{< card title="" subtitle="Coda di Riproduzione di Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Sleep Timer

Apri Impostazioni → Lettore → Sleep Timer, attivalo e scegli per quanto tempo vuoi che la riproduzione continui prima di fermarsi automaticamente. Puoi anche aggiungere il pulsante Sleep Timer direttamente alla schermata principale del lettore tramite Impostazioni → Lettore → Personalizzazione → Azioni Schermata Principale.

## Segnalibri del Lettore

Salva il tuo posto nei video lunghi — lezioni, audiobook-su-video, tutorial, download YouTube di un'ora — toccando Aggiungi Segnalibro dal menu Altre azioni. I segnalibri appaiono nella lista Altre azioni → Segnalibri del video e persistono tra le sessioni.

## Menu Altre azioni

Tocca il pulsante **Altre azioni "..."** sul lettore per accedere a funzioni aggiuntive.

- **Continua Riproduzione** — riprendi la coda dall'ultima posizione.
- **Cerca** — trova un video specifico nella coda.
- **Segnalibri** — visualizza e salta ai segnalibri.
- **Velocità** — regola la velocità di riproduzione.
- **Recenti** — video riprodotti di recente.
- **Preferiti** — video preferiti.
- **Equalizzatore Audio** — attiva l'equalizzatore audio.
- **Equalizzatore Video** — attiva l'equalizzatore video.
- **Traccia Audio** — scegli il flusso audio.
- **Traccia Video** — scegli il flusso video.
- **Sottotitoli** — traccia primaria / secondaria, file esterno, font.
- **Rotazione** — ruota l'immagine di 0° / 90° / 180° / 270°.
- **Modalità Ridimensionamento** — Adatta / Riempi / Allunga / Originale.
- **Picture-in-Picture** — entra in modalità PiP.
- **AirPlay** / **Chromecast** — invia a un dispositivo.
- **Sleep Timer** — imposta un timer per fermare la riproduzione.
- **Salva Coda in Playlist** — salva la coda corrente come nuova playlist.
- **Elimina Coda** — svuota la coda e ferma la riproduzione.
- **Impostazioni** — vai direttamente alle impostazioni del lettore.
- **Aiuto** — apri la guida.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Altre Azioni del Lettore Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Impostazioni del Lettore

L'albero completo delle impostazioni del Lettore è documentato nella [guida alle Impostazioni](/docs/guide/evervideo/evervideo-guide-settings/). Le sezioni più usate:

- **Generale** — Modalità Ripeti, Modalità Casuale, Salva Stato Lettore, Salva Posizione di Riproduzione, Intervalli di tempo di salto.
- **Video** — Decodifica hardware H.264 / HEVC, equalizzatore video, modalità di ridimensionamento, rotazione, modalità di visualizzazione, FPS preferito, formato pixel preferito, viewport VR.
- **Audio** — Equalizzatore audio, frequenza di campionamento, canali, durata buffer IO, modalità mista.
- **Sottotitoli** — Traccia primaria / secondaria, selezione file esterno, font, font secondario.
- **Dispositivi** (iOS) — AirPlay / Chromecast.
- **Personalizzazione** — Stile layout lettore (Minimale / Inferiore / Antico / Classico), azioni schermata principale, controlli schermata di blocco.
- **Cache di Riproduzione** — cache su disco per uno streaming più fluido.
- **Sleep Timer** — stop automatico.

## Accessibilità

Evervideo è completamente accessibile con VoiceOver. Ogni componente ha un'etichetta e una descrizione ben progettate. Quando VoiceOver è attivo, l'app passa alla Modalità Testo in modo che vengano mostrati solo gli elementi significativi — migliorando la velocità di navigazione e la chiarezza. Puoi anche attivare la Modalità Testo in Impostazioni → Accessibilità → Modalità Testo.

### Regolazione degli Slider con VoiceOver

1. **Seleziona lo slider** — scorri a sinistra o a destra finché VoiceOver non lo annuncia.
2. **Regola il valore** — tocca due volte e tieni premuto lo slider, poi trascina su o giù per cambiare il valore rapidamente. VoiceOver annuncia il nuovo valore man mano che procedi.

Gli altri componenti funzionano come previsto, utilizzando i pattern VoiceOver forniti dal sistema.
