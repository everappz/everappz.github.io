---
title: "Lettore Audio"
date: 2020-02-01
description: "Scopri come usare il lettore audio Flacbox su iPhone, iPad e Mac. Controlla la riproduzione, gestisci le code, configura il motore audio FFmpeg / sistema, cambia sample rate, correzione tonalità, durata buffer IO, equalizzatore, segnalibri audio, AirPlay 2, Google Cast, CarPlay, widget e scorciatoie da tastiera Mac."
keywords: [
  "guida lettore Flacbox", "impostazioni lettore audio", "equalizzatore Flacbox",
  "streaming musica AirPlay", "musica Google Cast", "segnalibri audio",
  "coda riproduzione Flacbox", "ripetizione shuffle Flacbox", "controllo volume Flacbox",
  "mini player macOS", "app musicale voiceover",
  "Flacbox FFmpeg", "correzione tonalità Flacbox", "sample rate Flacbox",
  "DAC esterno Flacbox", "surround sound Flacbox", "buffer IO Flacbox",
  "velocità riproduzione Flacbox", "sleep timer Flacbox"
]
tags: ["guida", "flacbox", "lettore"]
readingTime: 14
---


Il Lettore Audio è la schermata principale dell'app dove controlli la musica e la maggior parte delle funzionalità di riproduzione. È anche qui che il motore audio hi-res di Flacbox — costruito sui codec di sistema più la libreria **FFmpeg** inclusa — fa il lavoro pesante. Esploriamo come usarlo.

## Accedere al Lettore Audio

Puoi accedere al lettore a schermo intero dalla barra del mini player. Su iPhone, il mini player si trova nella parte inferiore della schermata principale. Su iPad e Mac, è sul lato sinistro. Per nascondere il mini player su iPhone, toccalo una volta e scorri verso il basso. Per chiudere completamente il lettore a schermo intero, tocca il pulsante di chiusura nell'angolo in basso a destra.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Principale del Lettore Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formati Audio Supportati

Flacbox riproduce i formati audio più popolari — sia i codec di sistema di Apple che molti formati aggiuntivi gestiti dal motore FFmpeg incluso:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

## Controlli di Riproduzione

Nella parte inferiore della schermata del lettore troverai i pulsanti per Riproduci, Pausa, Traccia Successiva e Traccia Precedente. Ci sono anche pulsanti opzionali come Avanti 30 sec e Indietro 30 sec che puoi abilitare nelle impostazioni. Puoi andare avanti o indietro velocemente tenendo premuti i pulsanti Avanti / Indietro. Per saltare a una parte specifica di una traccia, trascina lo slider di riproduzione.

## Ripeti e Mescola

Tocca il pulsante di ripetizione per passare tra le modalità di ripetizione:

- **Ripeti Tutto** — riproduce in loop tutte le tracce nella coda.
- **Ripeti Uno** — ripete solo la traccia corrente.
- **Ferma Ripetizione** — mette in pausa quando la traccia corrente finisce.
- **Nessuna Ripetizione** — riproduce la coda una volta senza ripetere.

Usa il pulsante **Mescola** per randomizzare l'ordine delle tracce nella coda.

## Controllo Volume

Apri la schermata Impostazioni Audio toccando l'icona del suono sotto i controlli di riproduzione per accedere allo slider del volume. Troverai anche pulsanti per **Google Cast** e **AirPlay** qui.

## Google Cast (Chromecast)

Per gli utenti Google Cast, l'icona **Cast** appare nella parte inferiore del lettore. Toccala per scegliere un dispositivo e iniziare lo streaming. Assicurati che il tuo dispositivo e il ricevitore Google Cast siano sulla stessa rete Wi-Fi.

## AirPlay

Per AirPlay, cerca il pulsante **AirPlay** nella parte inferiore del lettore. Toccalo e seleziona un dispositivo per lo streaming. Flacbox supporta **AirPlay 2**, così puoi riprodurre su più HomePod, Apple TV o speaker compatibili con AirPlay 2 contemporaneamente.

## Equalizzatore Audio

Flacbox include un **equalizzatore a 10 bande** con preset in stile iPod. Tocca Equalizzatore sulla vista del volume, poi attivalo nell'angolo in alto a destra. Puoi usare preset come Acustico e Potenziatore di bassi, o regolare ogni banda di frequenza con gli slider. Istruzioni più dettagliate su come usare l'equalizzatore sono disponibili [qui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalizzatore del Lettore Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Barra degli Strumenti Modalità Lettore

Per alcuni stili di lettore, c'è una barra degli strumenti dedicata nella parte superiore del lettore a schermo intero:

- **Cerca** — trova rapidamente una traccia specifica nella coda del lettore.
- **Controllo Velocità di Riproduzione** — regola la velocità di riproduzione da 0,02× a 3,00×.
- **Segnalibri Audio** — crea più segnalibri per traccia.

## Coda del Lettore

Per vedere la coda del lettore, tocca il pulsante della coda sul lato destro della canzone corrente. Ogni canzone nella coda ha più azioni — tocca i tre punti per visualizzarle.

{{< cards cols="1">}}
  {{< card title="" subtitle="Coda di Riproduzione Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Commenti / Testi

Per visualizzare i commenti delle tracce e i testi incorporati, nonché i file LRC, segui questi passaggi:

1. Apri **Impostazioni**.
2. Vai a **Lettore Audio**.
3. Seleziona **Personalizzazione**.
4. Tocca **Pulsanti nella schermata principale**.
5. Abilita **Commenti**.

Dopo di ciò, tocca il pulsante della coda del lettore nella parte inferiore dello schermo più volte per passare dalla vista artwork / coda alla vista commenti. Le istruzioni complete sono disponibili [qui](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Testi e Commenti Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menu Opzioni

Ogni canzone nella coda del lettore audio ha un menu con più azioni, accessibile toccando il pulsante a tre punti vicino al titolo della canzone.

- **Riproduci Successivo** — aggiunge la canzone in cima alla coda del lettore.
- **Aggiungi alla Playlist** — include la canzone in una playlist.
- **Aggiungi ai Preferiti** — contrassegna la canzone come preferita.
- **Scaricare** — salva la canzone nei file locali.
- **Modificare i tag audio** — apre l'editor di tag audio integrato.
- **Mostra nella Cartella** — rivela la cartella dove è archiviato il file audio.
- **Mostra nel Finder** — per i file importati dal Mac.
- **Apri In** — esporta il file audio in un'altra app.
- **Elimina dalla Coda** — rimuove la canzone selezionata dalla coda del lettore audio.
- **Elimina dal Servizio Cloud** — elimina la canzone dalla libreria musicale e dal cloud storage. **Questa azione è irreversibile.**
- **Elimina dai File Locali** — elimina la canzone dalla libreria musicale e dallo storage locale. **Questa azione è irreversibile.**
- **Elimina dalla Libreria Musicale** — elimina la canzone dalla libreria musicale, mantenendo il file nello storage.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Opzioni per un Elemento nella Coda di Riproduzione" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Azioni Aggiuntive del Lettore

Tocca il pulsante **Altre azioni** "..." sul lato sinistro del titolo della canzone attualmente in riproduzione per vedere azioni aggiuntive.

- **Continua Riproduzione** — riprendi da dove ti eri fermato.
- **Cerca** — trova rapidamente una traccia specifica nella coda del lettore audio.
- **Segnalibri** — visualizza l'elenco dei segnalibri audio creati.
- **Commenti** — visualizza i commenti delle tracce e i testi incorporati.
- **Velocità** — regola la velocità di riproduzione a tuo piacimento.
- **Recenti** — accedi a un elenco di canzoni riprodotte di recente.
- **Preferiti** — visualizza la collezione di canzoni preferite.
- **Equalizzatore Audio** — attiva l'equalizzatore audio.
- **Sleep Timer** — imposta un timer per interrompere la riproduzione dopo un intervallo specificato.
- **Salva Coda come Playlist** — salva la coda del lettore audio corrente come nuova playlist.
- **Elimina Coda** — svuota la coda del lettore e arresta la riproduzione.
- **Impostazioni** — accedi alle impostazioni del lettore audio.
- **Aiuto** — trova assistenza e guida.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Altre azioni del Lettore Audio Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Segnalibri Audio

Questa funzione ti permette di creare più segnalibri per le tracce nella libreria musicale — perfetto per audiolibri, lezioni, lunghi mix DJ o per segnare il ritornello di una traccia preferita.

Per creare un nuovo segnalibro:

- Inizia a riprodurre la canzone desiderata.
- Apri la schermata del lettore.
- Tocca il pulsante **Segnalibri** sulla barra degli strumenti della modalità lettore.
- Seleziona **Aggiungi Segnalibro**.
- Scegli il momento del segnalibro e tocca **Fatto** nell'angolo in alto a destra.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Segnalibri Audio Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recenti e Preferiti

Nella schermata del lettore, tocca i tre punti per accedere a Recenti e Preferiti. Le istruzioni dettagliate su come esportare elenchi di brani sono disponibili [qui](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Connetti iPhone all'auto tramite USB o Apple CarPlay wireless. L'interfaccia CarPlay include tab dedicate per Libreria, Connessioni, File Locali e Impostazioni.

[Leggi la guida completa CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox su Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widget della Schermata Home (iPhone & iPad)

Flacbox supporta i widget della schermata Home e della schermata di blocco iOS. Assicurati che i Widget siano abilitati in Impostazioni → Widget → Abilita Widget, poi tieni premuto la Schermata Home o la Schermata di Blocco, tocca **+**, cerca **Flacbox** e aggiungi un widget.

## Finestra Mini Player (Solo Mac)

Gli utenti Mac possono usare un mini player compatto sempre in primo piano. Sposta il cursore sul bordo in basso a destra della finestra Flacbox, ridimensionala alla dimensione minima e tocca il pulsante di riduzione.

## Scorciatoie da Tastiera (Solo Mac)

Per gli utenti Mac, premi la barra spaziatrice per Riproduci / Pausa. Sono disponibili anche scorciatoie per Stop, Canzone Successiva, Canzone Precedente, Salta Tempo, Ripeti, Mescola e Velocità di Riproduzione.

## Impostazioni del Lettore Audio

Per accedere alle impostazioni, tocca il pulsante Altro nella schermata del lettore e scegli Impostazioni.

### Generale

- **Modalità di Ripetizione** — scegli come si comporta il lettore audio quando una traccia finisce.
- **Modalità Mescola** — randomizza l'ordine delle tracce nella coda.
- **Codec Audio** — scegli il motore audio usato per la riproduzione (System Codec + FFmpeg o FFmpeg).
- **Sample Rate Output Audio** — valori disponibili: 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz e 96 kHz.
- **Numero di Canali Output Audio** — Mono, Stereo, ecc.
- **Durata Buffer IO Output Audio Preferita** — configura la durata del buffer.
- **Modalità Output Audio (solo iOS)** — configura la modalità output audio misto.
- **Salva Posizione di Riproduzione** — salva e ripristina la posizione di riproduzione.
- **Salva Stato Lettore Audio** — preserva lo stato del lettore audio prima di chiudere.

### Personalizzazione

- **Stile Schermata Lettore Audio** — configura il posizionamento degli elementi.
- **Stile Scorrimento Copertine Album** — configura lo stile di scorrimento preferito.
- **Elementi Aggiuntivi** — abilita elementi extra nella schermata del lettore.
- **Azioni Schermata Principale** — configura quali pulsanti devono essere visibili.
- **Controlli Riproduzione sulla Schermata di Blocco** — scegli quali controlli appaiono.
- **Pulsanti Salta Tempo** — scegli l'intervallo di tempo.

### Caricamento File

- **Tempo di Pre-caricamento** — imposta l'intervallo di tempo di buffering.
- **Usa URL Diretto** — quando abilitato, usa un URL diretto per caricare la canzone.

### Equalizzatore Audio

Configura l'equalizzatore audio a 10 bande. Leggi di più [qui](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocità di Riproduzione

Regola la velocità di riproduzione del lettore audio da **0,02× a 3,00×**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Velocità di Riproduzione Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Correzione Tonalità

Cambia le impostazioni di correzione della tonalità. L'intervallo va da **-1000 a +1000**.

### Cache di Riproduzione

Le canzoni nella coda del lettore audio vengono scaricate automaticamente per garantire una riproduzione fluida. Puoi anche configurare la dimensione della cache del lettore audio qui.

### Sleep Timer

Attiva un timer per interrompere automaticamente la riproduzione dopo un periodo specificato.

## Accessibilità

Flacbox è completamente accessibile con **VoiceOver**. Ogni componente ha un'etichetta e una descrizione ben progettate. Quando VoiceOver è attivo, l'app passa alla **Modalità Testo**.

### Regolare i Cursori con VoiceOver

1. **Seleziona il cursore** — scorri a sinistra o a destra finché VoiceOver non lo annuncia.
2. **Regola il valore** — tocca due volte e tieni il cursore, poi trascina su o giù.

### Regolare la Posizione di un Brano in un Elenco con VoiceOver

1. Tocca l'icona dell'indicatore di riordino vicino al titolo del brano.
2. Tocca rapidamente due volte l'indicatore di riordino. Al secondo tocco, non rilasciare il dito.
3. Sposta la cella nella sua nuova posizione.
