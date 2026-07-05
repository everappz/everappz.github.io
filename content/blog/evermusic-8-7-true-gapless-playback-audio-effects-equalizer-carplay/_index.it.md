---
title: "Evermusic 8.7: vera riproduzione gapless, effetti audio, normalizzazione del volume, equalizzatore ridisegnato"
date: 2026-07-05
description: "Evermusic 8.7 per iPhone, iPad e Mac aggiunge la vera riproduzione gapless, cinque effetti audio da studio (Riverbero, Delay, Distorsione, Compressore, Crossfeed), la normalizzazione del volume EBU R128, un equalizzatore a 10 bande ridisegnato con import/export dei preset, un motore di streaming AVAudioEngine ricostruito con supporto FLAC e Ogg Vorbis, e CarPlay e In riproduzione più veloci e accurati."
keywords: ["Evermusic 8.7", "aggiornamento Evermusic", "vera riproduzione gapless iPhone", "lettore musicale gapless iOS", "riproduzione gapless CarPlay", "effetti audio lettore musicale iPhone", "riverbero delay distorsione compressore crossfeed iOS", "crossfeed cuffie iOS", "normalizzazione del volume iPhone", "normalizzazione loudness lettore musicale", "normalizzazione EBU R128 iOS", "alternativa a replay gain iPhone", "equalizzatore a 10 bande iPhone", "equalizzatore grafico app iOS", "import export preset equalizzatore", "lettore FLAC iPhone", "lettore Ogg Vorbis iOS", "lettore musicale lossless iPhone 2026", "lettore musicale AVAudioEngine", "lettore musicale CarPlay iPhone", "accuratezza In riproduzione schermata di blocco", "lettore musicale cloud iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Riproduzione gapless", "Effetti audio", "Riverbero", "Delay", "Distorsione", "Compressore", "Crossfeed", "Normalizzazione del volume", "EBU R128", "Equalizzatore", "FLAC", "Ogg Vorbis", "CarPlay", "In riproduzione", "Liquid Glass", "Novità"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**In breve:** [Evermusic 8.7](/products/evermusic) è un aggiornamento dedicato alla qualità del suono per iPhone, iPad e Mac. Porta la **vera riproduzione gapless** (nessuna pausa, click o scatto tra i brani), un set completo di **effetti audio da studio** — Riverbero, Delay, Distorsione, Compressore e Crossfeed — e la **normalizzazione del volume EBU R128** che mantiene l'intensità costante da una canzone all'altra senza tag ReplayGain. L'**equalizzatore a 10 bande** è ridisegnato con nuovi cursori, cambio dei preset più rapido, preset personalizzati che puoi importare ed esportare e un layout migliore in orizzontale e su iPad. Sotto il cofano, un **motore di streaming AVAudioEngine ricostruito** migliora l'affidabilità e il supporto dei formati, inclusi **FLAC** e **Ogg Vorbis**. **CarPlay** e **In riproduzione** sono più veloci e accurati sulla schermata di blocco, in auto e dai comandi remoti delle cuffie.

---

## Ciao a tutti!

Evermusic 8.7 è disponibile per il download. Questo aggiornamento riguarda tutto il modo in cui la tua musica *suona*. Abbiamo ricostruito il motore di riproduzione per la vera riproduzione gapless, aggiunto una suite di effetti audio di livello studio, introdotto la normalizzazione del volume e ridisegnato l'equalizzatore fin dai cursori. Tutto è avvolto nel nuovo design **Liquid Glass** di Apple.

[Scarica Evermusic 8.7 dall'App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o aggiorna dalla tua versione esistente. Evermusic è un download gratuito con aggiornamenti in-app opzionali.

## Vera riproduzione gapless

La riproduzione gapless significa che il silenzio tra due brani è scomparso. Nessuna pausa, nessun click, nessuno scatto: la canzone corrente scorre direttamente nella successiva. Conta soprattutto per la musica progettata per essere ascoltata come un tutt'uno: **registrazioni dal vivo, DJ mix, opere classiche e concept album** dove un brano sfuma direttamente in un altro.

Ecco cosa è cambiato tecnicamente. Il motore audio di Evermusic tiene due brani in riproduzione contemporaneamente: quello che stai ascoltando e il successivo in coda. Mentre il brano corrente è in riproduzione, il successivo viene già **recuperato, decodificato e pre-caricato** in background. Quando il brano corrente raggiunge la fine, il motore effettua il passaggio al brano successivo **all'interno del lettore, non all'interno del flusso audio**. Il ciclo di rendering dell'uscita continua a prelevare campioni audio da un ring buffer continuo senza mai fermarsi, così l'ascoltatore non sente mai un confine. Il cambio avviene tra i campioni, ed è esattamente per questo che non c'è alcuna pausa udibile.

Questo funziona allo stesso modo sia che il file sia sul tuo dispositivo, nel cloud o su un media server: il pre-caricamento inizia solo un po' prima per le sorgenti remote.

## Effetti audio da studio

Evermusic 8.7 aggiunge cinque effetti audio in tempo reale che puoi sovrapporre alla tua musica. Ognuno funziona come nodo nativo di elaborazione audio nel motore di riproduzione, quindi si applica a tutto ciò che riproduci — file locali, streaming dal cloud e radio internet allo stesso modo — senza ricodifica.

Ogni effetto include una **libreria curata di preset** per ottenere un ottimo suono con un tocco, ed Evermusic **ricorda le tue impostazioni esatte** tra le sessioni. Regola qualsiasi controllo e l'effetto passa a uno stato **Manuale** così sai sempre quando ti sei allontanato da un preset.

### Riverbero

Aggiunge un senso di spazio, da una stanza raccolta a una cattedrale. Costruito sull'`AVAudioUnitReverb` di Apple, offre **13 preset di ambiente** (Stanza piccola, Sala media, Plate, Cattedrale e altri) più un controllo **mix wet/dry** da 0 a 100% così decidi quanto spazio aggiungere.

### Delay (Eco)

Un'eco classica con **10 preset** — Slapback, Tape Echo, Dub, Ambient e altri. Puoi regolare il **tempo di delay** (fino a 2 secondi), il **feedback** (quante ripetizioni), un **cutoff passa-basso** per scaldare le ripetizioni e il **mix wet/dry**.

### Distorsione

Da una grinta sottile alla piena distruzione lo-fi, guidata da `AVAudioUnitDistortion` con **22 preset di carattere** (Bit Brush, Cellphone Concert, Radio Tower e altri), un controllo drive di **pre-gain** e un mix wet/dry così puoi rimescolare l'effetto nel segnale pulito.

### Compressore

Un processore di dinamica (l'`AUDynamicsProcessor` di Apple) che livella i passaggi forti e deboli. Espone il set di controlli professionali completo — **soglia, ratio/headroom, attacco, rilascio, espansione e guadagno di compensazione** — con **10 preset** calibrati per situazioni reali: tra cui Voce / Podcast, A tarda notte, Dialoghi di film, Adatta streaming e Massima intensità.

### Crossfeed

Il Crossfeed rende l'ascolto in cuffia più naturale mescolando un po' del canale sinistro nel destro e viceversa, nel modo in cui le tue orecchie sentono veri altoparlanti. È costruito sul noto algoritmo **Bauer stereophonic-to-binaural (bs2b)**, con controllo del **livello di crossfeed** e della **frequenza di cutoff**, e **6 preset** tra cui le impostazioni predilette dagli audiofili *Chu Moy* e *Jan Meier*. È particolarmente efficace sui vecchi mix stereo con panning estremo degli anni '60 e '70.

## Normalizzazione del volume

Ti è mai capitato di creare una playlist dove un brano esplode e il successivo è un sussurro? La normalizzazione del volume risolve questo. Evermusic 8.7 usa la **misurazione del loudness EBU R128** (lo stesso standard ITU-R BS.1770 usato nel broadcast e dai servizi di streaming) per misurare l'intensità percepita reale di ogni brano e guidarla dolcemente verso un target costante.

A differenza di ReplayGain, **non** richiede alcun tag nei tuoi file e **non** modifica il tuo audio. Funziona in tempo reale su qualsiasi cosa riproduci, inclusi streaming dal cloud e radio live, e si reimposta in modo pulito quando cerchi o cambi brano.

Quattro preset coprono i casi comuni:

- **Leggero** — livellamento delicato (target −20 LUFS).
- **Standard** — il predefinito, intensità in stile streaming (target −16 LUFS, fino a +12 dB di lift per i brani deboli).
- **Forte** — adattamento aggressivo per librerie molto miste (target −14 LUFS).
- **Notte** — più tranquillo e costante per l'ascolto serale a basso volume (target −23 LUFS).

Non devi più regolare il volume tra una canzone e l'altra.

## Equalizzatore ridisegnato

L'**equalizzatore grafico a 10 bande** di Evermusic ha ricevuto un completo restyling. Le bande coprono da **32 Hz a 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), ognuna regolabile da **−12 dB a +12 dB** con passi fini di 0,1 dB, con un **preamplificatore** da −24 dB a +24 dB per prevenire il clipping quando aumenti i livelli.

Cosa c'è di nuovo in 8.7:

- **Nuovi cursori** — controlli precisi e reattivi che adottano l'aspetto del cursore di sistema nativo di iOS 26 e il materiale **Liquid Glass**.
- **Cambio dei preset più veloce e fluido** — passa tra i preset all'istante, con una barra dei preset orizzontale ridisegnata in verticale e una colonna di preset verticale in orizzontale.
- **Layout migliore in orizzontale e su iPad** — i cursori e il selettore dei preset si riorganizzano per usare la larghezza extra invece di stiparsi in una colonna delle dimensioni di un telefono.
- **Preset personalizzati** — crea e salva le tue curve, riordinale e **importa ed esporta** i preset come file `.eqp` per spostarli tra i dispositivi o condividerli.

L'equalizzatore funziona nativamente nel motore (`AVAudioUnitEQ`), quindi si applica a ogni sorgente, e funziona anche tramite AirPlay, Chromecast e CarPlay dove supportato.

## Motore di riproduzione ricostruito

Sotto il cofano, Evermusic 8.7 gira su un **motore di streaming ricostruito** basato sull'`AVAudioEngine` di Apple con una pipeline di rendering personalizzata. È questo che rende possibili il passaggio gapless, la catena di effetti e l'equalizzatore, e rende anche la riproduzione quotidiana più affidabile.

- **Supporto dei formati migliorato** — inclusi **FLAC** (tramite Core Audio) e **Ogg Vorbis** (tramite `libvorbisfile`), insieme a MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF e altri.
- **Buffering più intelligente** — un pre-buffer adattivo si adatta alla tua connessione, con un ring buffer continuo che alimenta l'uscita così i brevi intoppi di rete non si trasformano in interruzioni.
- **Recupero automatico** — una macchina a stati di rebuffering e una logica di retry con backoff riprendono la riproduzione in modo pulito dopo un momento di segnale debole invece di fermare il brano.
- **Meno interruzioni** — lo stesso motore gestisce file locali, streaming dal cloud, media server e radio internet, così il comportamento è coerente ovunque.

## In riproduzione e CarPlay

Le schermate che guardi davvero mentre ascolti — la **schermata di blocco**, **CarPlay** e i pulsanti dei comandi remoti dell'auto o delle cuffie — sono più accurate e veloci in 8.7.

- **Informazioni In riproduzione più accurate.** Evermusic cattura lo stato del lettore sotto un lock prima di pubblicarlo, così il titolo, il tempo trascorso, la durata e lo stato play/pause non possono mai contraddirsi tra loro sulla schermata di blocco o in auto. Gli stati di buffering e caricamento ora vengono riportati correttamente invece di mostrare "in riproduzione" mentre un brano è ancora in fase di recupero.
- **Comandi remoti affidabili.** Play, pausa, avanti, indietro, ricerca, salta, riproduzione casuale, ripeti e velocità di riproduzione rispondono tutti in modo coerente dai pulsanti delle cuffie, dai comandi dell'auto e dalla schermata di blocco, guidati da `MPRemoteCommandCenter`.
- **Copertine CarPlay più veloci.** Le copertine degli album ora si caricano diverse volte più velocemente su liste lunghe (ritmo dei batch ridotto da 1,0 s a 0,25 s, con la prima schermata visibile che si carica immediatamente), e ora compaiono nelle righe compatte delle liste CarPlay di iOS 26 che prima non mostravano copertine.
- **Correzioni di ordinamento e stabilità di CarPlay.** Ordinamento più veloce su librerie grandi e maggiore robustezza contro i crash in casi limite durante lo scorrimento di liste lunghe.
- **Aggiornamenti dei metadati limitati.** Gli aggiornamenti di In riproduzione e dei comandi remoti sono limitati così i cambiamenti rapidi non inondano più il sistema, mantenendo reattivi i comandi della schermata di blocco e di CarPlay.

## Altri miglioramenti

- **Perfezionamenti del design Liquid Glass** in tutta l'app — superfici traslucide, animazioni più fluide e controlli raffinati su iOS, iPadOS e macOS.
- **Nuovi widget per la schermata Home** con una logica di aggiornamento migliorata che li mantiene sincronizzati senza consumare batteria extra.
- Correzioni per le recenti versioni di iOS.
- Correzioni di localizzazione in più lingue.
- Molti miglioramenti minori basati sulle tue email e recensioni sull'App Store.

## Perché questo aggiornamento è importante

Evermusic 8.7 è costruito attorno a un'unica idea: **la tua musica dovrebbe suonare al meglio, su qualsiasi sorgente.**

1. **Album interi, come previsto.** La vera riproduzione gapless significa che i set dal vivo, i DJ mix e i concept album vengono finalmente riprodotti nel modo in cui l'artista li ha masterizzati.
2. **Uno studio in tasca.** Riverbero, Delay, Distorsione, Compressore, Crossfeed, un equalizzatore ridisegnato e la normalizzazione del volume ti danno un vero controllo sul tuo suono, non solo un interruttore on/off.
3. **La stessa esperienza ovunque.** File locali, unità cloud, media server e radio internet passano tutti attraverso lo stesso motore ricostruito, con un In riproduzione accurato e un CarPlay più veloce in cima.

## Ottieni Evermusic 8.7

[**Scarica Evermusic dall'App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o aggiorna dall'interno dell'App Store. Evermusic è un download gratuito con aggiornamenti in-app opzionali per le funzioni avanzate.

Se ti piace l'app, lascia una valutazione sull'App Store: aiuta davvero. Hai feedback o hai riscontrato un problema? Scrivici a **support@everappz.com**. Leggiamo ogni messaggio.

## Domande frequenti

{{% details title="Cosa c'è di nuovo in Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 aggiunge la vera riproduzione gapless, cinque effetti audio da studio (Riverbero, Delay, Distorsione, Compressore e Crossfeed), la normalizzazione del volume EBU R128, un equalizzatore a 10 bande ridisegnato con preset personalizzati e import/export, un motore di streaming AVAudioEngine ricostruito con supporto dei formati migliorato (inclusi FLAC e Ogg Vorbis), CarPlay e In riproduzione più veloci e accurati, aggiornamenti del design Liquid Glass, widget per la schermata Home rinnovati, e correzioni di bug e localizzazione.
{{% /details %}}

{{% details title="Evermusic ha la vera riproduzione gapless?" closed="true" %}}
Sì. A partire da Evermusic 8.7, la riproduzione è veramente gapless: non c'è alcuna pausa, click o scatto tra i brani. Il motore pre-carica e decodifica il brano successivo mentre quello corrente è in riproduzione ed effettua il passaggio tra i campioni audio su un ring buffer continuo, così la transizione è impercettibile. Funziona con file locali, streaming dal cloud e media server, ed è ideale per album live, DJ mix e concept album.
{{% /details %}}

{{% details title="Quali effetti audio include Evermusic 8.7?" closed="true" %}}
Cinque effetti in tempo reale: **Riverbero** (13 preset di ambiente, mix wet/dry), **Delay/Eco** (10 preset con tempo di delay, feedback, passa-basso e mix), **Distorsione** (22 preset di carattere con pre-gain e mix), **Compressore** (un processore di dinamica completo con soglia, ratio, attacco, rilascio, espansione e guadagno di compensazione, più 10 preset), e **Crossfeed** (crossfeed per cuffie Bauer bs2b con controlli di livello e cutoff e 6 preset). Ogni effetto include preset curati, e le tue impostazioni personalizzate vengono ricordate tra le sessioni.
{{% /details %}}

{{% details title="Cos'è il Crossfeed e perché dovrei usarlo?" closed="true" %}}
Il Crossfeed mescola una piccola quantità filtrata di ciascun canale stereo nell'altro, nel modo in cui le tue orecchie sentono naturalmente veri altoparlanti in una stanza. In cuffia questo riduce la separazione esagerata e "dentro la testa" delle registrazioni con panning estremo e rende più comodo l'ascolto prolungato. Evermusic usa il noto algoritmo Bauer stereophonic-to-binaural (bs2b) e include preset come Chu Moy e Jan Meier. È particolarmente efficace sui vecchi mix stereo degli anni '60 e '70.
{{% /details %}}

{{% details title="Come funziona la normalizzazione del volume in Evermusic?" closed="true" %}}
Evermusic 8.7 misura l'intensità percepita di ogni brano usando lo standard EBU R128 (ITU-R BS.1770) in tempo reale e regola dolcemente il livello verso un target costante così i brani non saltano di volume. Non richiede tag ReplayGain e non altera i tuoi file. Sono disponibili quattro preset — Leggero (−20 LUFS), Standard (−16 LUFS), Forte (−14 LUFS) e Notte (−23 LUFS) — e la normalizzazione si reimposta in modo pulito quando cerchi o cambi brano.
{{% /details %}}

{{% details title="La normalizzazione del volume di Evermusic è la stessa cosa di ReplayGain?" closed="true" %}}
Raggiunge lo stesso obiettivo — intensità costante tra i brani — ma funziona in modo diverso. ReplayGain si basa su tag di loudness memorizzati all'interno dei tuoi file. Il normalizzatore di Evermusic misura l'intensità dal vivo usando EBU R128, quindi funziona su qualsiasi sorgente, inclusi streaming dal cloud e radio internet, anche quando i file non hanno alcun tag.
{{% /details %}}

{{% details title="Quante bande ha l'equalizzatore di Evermusic e posso creare i miei preset?" closed="true" %}}
L'equalizzatore di Evermusic è un equalizzatore grafico a 10 bande che copre da 32 Hz a 16 kHz, con ogni banda regolabile da −12 dB a +12 dB con passi di 0,1 dB e un preamplificatore da −24 dB a +24 dB. Include preset integrati, ti permette di creare e salvare preset personalizzati e supporta l'importazione e l'esportazione dei preset come file .eqp così puoi spostarli o condividerli tra i dispositivi.
{{% /details %}}

{{% details title="Cosa è cambiato nell'equalizzatore di Evermusic 8.7?" closed="true" %}}
L'equalizzatore è stato ridisegnato con nuovi cursori più precisi che adottano l'aspetto del cursore di sistema di iOS 26 e di Liquid Glass, un cambio dei preset più veloce e fluido, e un layout migliore in orizzontale e su iPad (una barra dei preset orizzontale in verticale e una colonna di preset verticale in orizzontale). Sono supportati i preset personalizzati e l'import/export .eqp.
{{% /details %}}

{{% details title="Evermusic 8.7 supporta FLAC e Ogg Vorbis?" closed="true" %}}
Sì. Il motore ricostruito riproduce FLAC (tramite Core Audio) e Ogg Vorbis (tramite libvorbisfile), insieme a MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF e altri, da file locali, unità cloud e media server.
{{% /details %}}

{{% details title="Cosa è migliorato in CarPlay e sulla schermata di blocco?" closed="true" %}}
Le copertine degli album in CarPlay si caricano diverse volte più velocemente su liste lunghe e ora compaiono nelle righe compatte delle liste di iOS 26 che prima non ne mostravano. Le informazioni In riproduzione sulla schermata di blocco e in CarPlay sono più accurate: il titolo, il tempo trascorso, la durata e lo stato play/pause vengono catturati insieme così non possono contraddirsi, e gli stati di buffering vengono riportati correttamente. I comandi remoti (play, pausa, avanti, indietro, ricerca, riproduzione casuale, ripeti, velocità) rispondono in modo affidabile dalle cuffie e dall'auto, e l'ordinamento di CarPlay su librerie grandi è più veloce.
{{% /details %}}

{{% details title="Gli effetti audio e l'equalizzatore funzionano con lo streaming dal cloud e CarPlay?" closed="true" %}}
Sì. Gli effetti, l'equalizzatore e la normalizzazione del volume funzionano nativamente all'interno del motore di riproduzione, quindi si applicano a tutto ciò che Evermusic riproduce — file locali, unità cloud, media server e radio internet — e continuano a funzionare durante la riproduzione con CarPlay e, dove supportato, tramite AirPlay e Chromecast.
{{% /details %}}

{{% details title="Evermusic 8.7 è gratuito da aggiornare e quali dispositivi supporta?" closed="true" %}}
Sì. Evermusic è un download gratuito dall'App Store, e 8.7 è un aggiornamento gratuito per gli utenti esistenti, con aggiornamenti in-app opzionali per le funzioni avanzate. Funziona su iPhone, iPad e Mac. CarPlay richiede un veicolo o un'unità head compatibile con CarPlay.
{{% /details %}}
