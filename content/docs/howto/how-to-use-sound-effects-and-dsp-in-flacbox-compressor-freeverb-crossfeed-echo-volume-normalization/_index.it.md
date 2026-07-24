---
title: "Come usare gli effetti sonori e il DSP in Flacbox: Compressore, Freeverb, Crossfeed, Echo, Normalizzazione del volume e altro"
date: 2026-07-24
description: "La guida completa all'audio di Flacbox su iPhone, iPad e Mac. Scopri come funziona il motore BASS, quali formati extra riproduce (inclusa la musica MOD e tracker e il DSD), ed esattamente cosa fa ogni effetto, ogni cursore e ogni preset al tuo suono, oltre all'equalizzatore a 10 bande e alla catena DSP personalizzata."
keywords: ["effetti audio Flacbox", "preset Flacbox spiegati", "motore BASS Flacbox", "libreria audio BASS iOS", "lettore musica MOD iPhone", "lettore musica tracker iOS", "riprodurre MOD XM IT S3M iPhone", "lettore DSD iOS", "lettore FLAC iPhone", "lettore musica lossless iOS", "preset equalizzatore Flacbox", "equalizzatore a 10 bande iPhone", "normalizzazione del volume iPhone", "EBU R128 iOS", "normalizzazione del loudness lettore musica", "crossfeed cuffie iOS", "crossfeed bs2b", "preset compressore lettore musica", "riverbero freeverb iOS", "echo delay lettore musica", "catena DSP lettore musica", "aumento dei bassi iPhone", "come aggiungere effetti alla musica Flacbox", "migliori impostazioni equalizzatore iPhone"]
tags: ["Flacbox", "Effetti audio", "Come fare", "BASS", "Equalizzatore", "Aumento dei bassi", "Compressore", "Freeverb", "Crossfeed", "Echo", "Normalizzazione del volume", "EBU R128", "Musica MOD", "Musica tracker", "DSD", "FLAC", "DSP", "Cuffie", "Preset"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Risposta breve:** in Flacbox scegli un unico **Motore di riproduzione** in **Impostazioni > Lettore audio**: **Standard** (il motore di sistema di Apple), **Universal** (il motore FFmpeg) o **Sound FX** (il **motore BASS™**). Il motore che scegli decide quali formati di file vengono riprodotti, quindi la scelta conta. Il motore **Sound FX** riproduce formati extra che la maggior parte delle app iPhone ignora (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e la vecchia **musica MOD e tracker** come MOD, XM, IT e S3M), ed è l'unico motore che alimenta gli strumenti sonori: un **equalizzatore a 10 bande**, la **Normalizzazione del volume**, il **Compressore**, il **Freeverb**, l'**Auto Wah**, il **Phaser**, il **Flanger**, l'**Echo**, il **Chorus**, la **Distorsione**, il **Rotate**, il **Crossfeed** e una **catena DSP** costruita da te. Quindi, per usare gli effetti di questa guida, imposta prima il tuo Motore di riproduzione su **Sound FX**. Ogni strumento ha **preset** già pronti. Aprili in **Impostazioni > Lettore audio** (Effetti audio, Equalizzatore audio, Elaborazione del segnale), oppure tocca il pulsante **⋯ (Altre azioni)** sul lettore e scegli **Effetti audio**. Nulla di ciò che fai qui modifica mai i tuoi file.

> Le spiegazioni dei cursori e dei preset qui sotto sono le stesse brevi descrizioni che Flacbox ti mostra dentro l'app, arricchite con un po' di contesto in più così da avere il quadro completo prima di toccare.

## Come leggere questa guida

Ogni strumento funziona allo stesso modo:

1. **Attivalo.** Ogni effetto ha il proprio interruttore on/off. All'inizio sono tutti spenti. Puoi attivarne quanti vuoi contemporaneamente.
2. **Scegli un preset.** Un preset è un'impostazione già pronta. Toccane uno e il suono cambia subito. Questa guida elenca cosa fa **ogni** preset.
3. **Regola con precisione (facoltativo).** Apri i cursori per regolare a mano. Nel momento in cui muovi un cursore, l'effetto mostra **Manuale**, così sai di aver lasciato il preset. Ogni cursore ha un pulsante di ripristino.

Nulla viene salvato nei tuoi file. Questi sono effetti in tempo reale. Spegni un effetto e il tuo suono originale ritorna all'istante.

## Scegli il tuo Motore di riproduzione (Sound FX ha gli effetti)

Flacbox non mescola i motori tra loro. Ne scegli **uno** in **Impostazioni > Lettore audio > Motore di riproduzione**, e il motore che scegli decide quali formati di file puoi riprodurre e se gli effetti sono disponibili. Ci sono tre scelte, mostrate nell'app con questi nomi esatti:

1. **Standard.** Il motore di sistema integrato di Apple. Usa la decodifica hardware per un minor consumo della batteria.
2. **Universal.** Il motore FFmpeg, che apre una gamma molto ampia di formati.
3. **Sound FX.** Il **motore BASS™**. Riproduce file lossless e ad alta risoluzione con piena accuratezza, aggiunge la musica a moduli (tracker) e alimenta ogni effetto, l'equalizzatore a 10 bande e la catena DSP di questa guida.

Poiché ogni motore supporta il proprio set di formati, i file che puoi riprodurre cambiano con il motore che selezioni. Ancora più importante, gli effetti, l'equalizzatore e la catena DSP funzionano **solo** con il motore **Sound FX**, quindi scegli quello per primo se vuoi usarli.

Sound FX è costruito su **BASS™**, una libreria audio professionale di Un4seen Developments. Puoi saperne di più nella sua home page su [un4seen.com](https://www.un4seen.com/).

## Formati musicali: cosa aggiunge il motore Sound FX (BASS™) (inclusa la musica MOD e tracker)

Con il motore **Sound FX (BASS™)** selezionato, Flacbox riproduce i formati specialistici qui sotto, oltre a quelli di tutti i giorni. Il più speciale è la **musica a moduli**, chiamata anche **musica tracker**. Un file a moduli non è una normale registrazione. Contiene piccoli suoni di strumenti più uno «spartito» che dice come suonarli, e Flacbox ricostruisce la canzone dal vivo a partire da quello spartito, nel modo in cui questi file erano pensati per essere riprodotti. I lettori normali non possono farlo.

| Tipo di musica | Formati | Buono a sapersi |
|---|---|---|
| **Musica a moduli / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Ricostruita dal vivo dal lettore a moduli BASS™. Ottima per chiptune e vecchie canzoni demoscene o Amiga. |
| **Lossless moderno** | FLAC | Piena qualità, più piccolo del WAV. |
| **Altro lossless** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Tipi lossless meno comuni, tutti supportati. |
| **DSD ad alta risoluzione** | DSF, DFF | Riproduce su hardware normale usando DSD over PCM. |
| **Lossy moderno** | Opus, Ogg Vorbis, MP3 | I soliti tipi per streaming e download. |

Il motore Sound FX riproduce anche i formati Apple più diffusi (AAC, ALAC, M4A, WAV, AIFF) e le trasmissioni live, quindi gli effetti e l'equalizzatore funzionano anche su quelli.

**Perché ti è utile:** se hai un mix di album FLAC, file DSD ad alta risoluzione e una cartella di vecchie canzoni tracker MOD o XM, Flacbox le riproduce tutte, e l'equalizzatore e gli effetti funzionano su ognuna di esse.

## I tre menu che userai

Flacbox tiene i suoi strumenti sonori in tre posti, tutti dentro le impostazioni del lettore audio. Prima assicurati che il tuo **Motore di riproduzione** sia impostato su **Sound FX** (Impostazioni > Lettore audio > Motore di riproduzione), perché gli effetti, l'equalizzatore e la catena DSP sono disponibili solo con quel motore.

- **Effetti audio** (il rack degli effetti): apri il lettore, tocca **⋯ (Altre azioni)**, tocca **Effetti audio**. Oppure vai su **Impostazioni > Lettore audio > Effetti audio**.
- **Equalizzatore audio** (10 bande e preset): **Impostazioni > Lettore audio > Equalizzatore audio**.
- **Elaborazione del segnale** (la tua catena DSP): **Impostazioni > Lettore audio > Elaborazione del segnale**.

Puoi anche impostare la **frequenza di campionamento in uscita**, i **canali** e la **dimensione del buffer** in **Impostazioni > Lettore audio**.

## L'equalizzatore a 10 bande

**Cosa fa:** cambia il timbro della musica, dai bassi profondi agli alti brillanti. È lo strumento migliore per un **aumento dei bassi** pulito o per un top più brillante e chiaro. Pensalo come dieci manopole del volume, ciascuna per una fetta diversa del suono. Alza una banda per portare avanti quella parte, abbassala per tirarla indietro. Piccole variazioni di pochi dB di solito suonano meglio, e funziona su tutto ciò che riproduci.

**Come funziona:** dieci cursori a **32, 64, 125, 250, 500 Hz e 1, 2, 4, 8, 16 kHz**. Ciascuno va da **-12 dB (taglio)** a **+12 dB (aumento)**. C'è anche un **Preamplificatore** da **-24 a +24 dB** per il livello complessivo. Puoi salvare i tuoi preset ed **esportarli o importarli** tra i dispositivi.

**Cosa fa ogni preset integrato (22 preset):**

| Preset | Cosa fa al tuo suono |
|---|---|
| **Flat** | Nessun cambiamento. Tutte le bande a zero. Un punto di partenza pulito. |
| **Acoustic** | Bassi caldi e alti nitidi e presenti. Rende le chitarre acustiche e le voci naturali e vivaci. |
| **Bass Booster** | Forte spinta sulle basse frequenze, medi e alti intatti. Più punch e peso. |
| **Bass Reducer** | Taglia le basse frequenze. Comodo per stanze rimbombanti, auricolari economici o brani pesanti. |
| **Treble Booster** | Alza solo gli alti. Aggiunge brillantezza e aria, più dettaglio. |
| **Treble Reducer** | Ammorbidisce gli alti. Doma registrazioni aspre o taglienti. |
| **Classical** | Bassi pieni e alti delicati con un leggero calo nei medi. Morbido e spazioso per la musica orchestrale. |
| **Dance** | Bassi grandi e alti brillanti con medi scavati. Deciso ed energico per i brani da club. |
| **Deep** | Bassi caldi e corposi con alti più morbidi. Un suono accogliente e rilassato. |
| **Electronic** | Bassi forti e alti brillanti per synth e ritmi. Ampio e moderno. |
| **Hip-Hop** | Bassi pesanti e alti chiari con medi controllati. Corposo e deciso. |
| **Jazz** | Caldo e morbido, con un piccolo calo nei medi. Facile e naturale per il jazz acustico. |
| **Latin** | Bassi e alti potenziati con medi puliti. Brillante e vivace. |
| **Loudness** | Aumenta fortemente bassi e alti (una curva a «sorriso»). Suona più pieno a basso volume. |
| **Lounge** | Medi in avanti con bordi morbidi. Rilassato e adatto alle voci. |
| **Piano** | Medi e alti chiari così le note del piano risuonano pulite. |
| **Pop** | Medi alzati per le voci, con bassi e alti tirati indietro. Le voci stanno in primo piano. |
| **R&B** | Calore molto forte nei bassi-medi e alti chiari. Morbido e ricco. |
| **Rock** | Bassi e alti potenziati per chitarre e batteria. Energico e pieno. |
| **Small Speakers** | Aumenta i bassi e taglia gli alti per aiutare i piccoli altoparlanti a suonare più pieni. |
| **Spoken Word** | Alza la gamma della voce e taglia i bassi profondi. Rende il parlato chiaro. |
| **Vocal Booster** | Spinge la parte centrale dove vivono le voci, taglia intorno. Le voci risaltano. |

**Consiglio per i bassi:** parti da **Bass Booster**, poi, se suona impastato, abbassa il Preamplificatore di 1 o 2 dB così nulla distorce.

## Normalizzazione del volume (volume uniforme)

**Cosa fa:** alcune canzoni suonano più forte di altre, quindi cambi continuamente il volume. Questo fa suonare ogni canzone circa allo stesso volume da sola, così non devi farlo tu. È perfetto per le playlist in riproduzione casuale che mescolano registrazioni vecchie e nuove, album diversi o sorgenti diverse, dove un brano può essere molto più forte del successivo.

**Come funziona:** ascolta il vero loudness di ogni brano usando lo standard **EBU R128** (misurato in **LUFS**, la stessa idea che usano i servizi di streaming), poi regola ogni brano verso il tuo obiettivo. Non ha bisogno di tag nei tuoi file e non cambia mai l'audio. EBU R128 misura il loudness che le tue orecchie percepiscono davvero lungo tutta la canzone, non solo il picco più alto, ed è per questo che corrisponde a quanto forte i brani sembrano davvero a te. Flacbox calcola questo dal vivo mentre la musica suona (e controlla il loudness in anticipo quando può), poi applica un'unica variazione di volume costante al brano. Il limite di **Boost massimo** impedisce che registrazioni molto silenziose vengano spinte così tanto da distorcere. Poiché legge il suono stesso, funziona su qualsiasi sorgente, inclusi file su cloud, trasmissioni live e musica a moduli, anche quando i file non hanno alcun tag di loudness.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Loudness obiettivo** | Imposta il loudness verso cui ogni brano viene livellato. Valori più alti fanno suonare tutto più forte in generale. | -30 a -6 LUFS (-16) |
| **Boost massimo** | Limita quanto i brani silenziosi possono essere amplificati. Valori più alti avvicinano le registrazioni deboli all'obiettivo. | 0 a 24 dB (12) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Light** | Livellamento delicato per un ascolto casuale. Uniforma i salti di volume evidenti senza spingere troppo i brani silenziosi. |
| **Standard** | Il predefinito tuttofare. Un obiettivo di loudness in stile streaming adatto alla maggior parte della musica. Parti da qui. |
| **Strong** | Uniformazione aggressiva che spinge decisamente in alto i brani silenziosi. Ideale per librerie miste con grandi differenze di livello. |
| **Night** | Un obiettivo complessivo più silenzioso che comunque solleva i passaggi deboli, così l'ascolto a tarda notte resta costante e basso. |

## Compressore (uniforma le parti forti e deboli)

**Cosa fa:** in una stessa canzone, le parti silenziose possono essere troppo deboli e quelle forti troppo forti. Questo le avvicina, così l'intera canzone è facile da sentire, anche in auto o in un posto rumoroso. Abbassa dolcemente i momenti più forti e solleva quelli più deboli, così smetti di cercare il volume durante un singolo brano. È diverso dalla Normalizzazione del volume: il Compressore uniforma le cose **all'interno** di una canzone, mentre la Normalizzazione del volume abbina il loudness **tra** le canzoni. I due lavorano bene insieme. Parti da un preset e apri i cursori solo se vuoi più controllo.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Soglia** | Il livello a cui inizia la compressione. Valori più bassi schiacciano più suono, tenendo parti silenziose e forti più vicine. | -60 a 0 dB (-20) |
| **Rapporto** | Quanto fortemente le parti forti vengono trattenute una volta superata la soglia. Valori più alti comprimono più duramente, mantenendo il suono più uniforme. | 1:1 a 30:1 (4:1) |
| **Attacco** | Quanto velocemente l'effetto risponde a un picco forte improvviso. Valori brevi catturano i transienti; quelli più lunghi li lasciano passare. | 0,1 a 1000 ms (10 ms) |
| **Rilascio** | Quanto velocemente l'effetto lascia andare dopo che la parte forte passa. Valori brevi possono pompare; quelli più lunghi suonano più morbidi. | 10 ms a 5 s (100 ms) |
| **Guadagno master** | Aumento finale in uscita applicato dopo l'elaborazione. Alzalo per sollevare il loudness complessivo una volta uniformata la dinamica. | -30 a +30 dB (0) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Transparent** | Rete di sicurezza appena percettibile. Preserva quasi interamente la dinamica e cattura solo i picchi più forti. |
| **Soft** | Livellamento leggero per l'ascolto hi-fi a casa. Ammorbidimento sottile senza schiacciare la musica. |
| **Standard** | Predefinito sensato per la riproduzione musicale di tutti i giorni. Il primo preset da provare. |
| **Heavy** | Uniformazione aggressiva per ambienti rumorosi. Auto, stanza affollata, ascolto a basso volume. |
| **Voice / Podcast** | Ottimizzato per il parlato. Un attacco più lento lascia passare le sibilanti, un generoso guadagno di makeup solleva le voci. |
| **Old Recordings** | Album d'epoca e vinili restaurati, dove il livello medio è inferiore alle uscite moderne. |
| **Late Night** | Compressione pesante più grande boost per l'ascolto silenzioso quando i vicini o la famiglia che dorme contano. |
| **Movie Dialog** | Porta il parlato in evidenza rispetto a musica ed effetti sonori in una colonna sonora variegata. |
| **Streaming Match** | Punta approssimativamente alla normalizzazione del loudness dei moderni servizi di streaming intorno a -14 LUFS. |
| **Maximum Loudness** | Tutto al massimo. Colpisce il limiter; aspettati un segnale schiacciato e molto livellato. Il preset letterale del volume massimo. |

## Freeverb (riverbero, un senso di spazio)

**Cosa fa:** aggiunge un senso di spazio alla musica, da una piccola stanza fino a una grande sala. Scegli un preset, oppure regola tu stesso il mix dry e wet, la dimensione della stanza, lo smorzamento e la larghezza. Il riverbero è l'eco naturale che senti in qualsiasi spazio reale, e Freeverb lo ricrea via software. Un po' rende le registrazioni piatte o ravvicinate più aperte e vive. Molto colloca la musica in uno spazio grande e distante. È un effetto creativo, quindi mantieni il mix wet moderato per risultati naturali.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Mix dry** | Quanto del suono originale, intatto, viene mantenuto. Valori più alti lasciano più segnale dry nel mix. | 0 a 1 (0.0) |
| **Mix wet** | Quanto del suono riverberato viene aggiunto. Valori più alti rendono il riverbero più forte e più evidente. | 0 a 3 (1.0) |
| **Dimensione stanza** | La dimensione dello spazio immaginato. Valori più alti danno una coda di riverbero più lunga e grande, da una piccola stanza fino a una cattedrale. | 0 a 1 (0.5) |
| **Smorzamento** | Quanto velocemente le alte frequenze svaniscono nella coda. Valori più alti rendono il riverbero più scuro e caldo. | 0 a 1 (0.5) |
| **Larghezza** | La diffusione stereo del riverbero. Valori più alti fanno sembrare lo spazio più ampio tra i canali sinistro e destro. | 0 a 1 (1.0) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Room** | Uno spazio piccolo e serrato. Ambienza sottile che aggiunge un senso di luogo senza annacquare il suono. |
| **Studio** | Una sala di registrazione dry e controllata. Giusto quel tanto di riflessione da suonare naturale. |
| **Hall** | Una grande sala da concerto. Una coda lunga e rigogliosa che si addice alla musica orchestrale e acustica. |
| **Cathedral** | Un enorme spazio di pietra riecheggiante. La coda di riverbero più lunga e drammatica. |
| **Plate** | Un riverbero a piastra da studio brillante e denso. Un classico per voci e batteria. |
| **Ambience** | Un'ambienza breve e ariosa. Aggiunge un leggero senso di spazio restando per lo più dry. |

## Auto Wah (spazzata di filtro funky)

**Cosa fa:** un filtro che spazza su e giù da solo per un suono wah funky, simile alla voce. Scegli un preset, oppure imposta tu stesso il mix wet, il feedback, la velocità, la gamma e la frequenza. È la stessa spazzata «wah» che fa un pedale wah per chitarra, ma qui si muove da solo a tempo con la musica. Suona benissimo su funk, disco e brani elettronici. È un effetto deciso ed evidente, quindi un po' basta e avanza nell'ascolto di tutti i giorni.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Mix wet** | Quanto è forte l'effetto wah nel mix. Valori più alti rendono più evidente il filtro spazzante. | -2 a +2 (1.5) |
| **Feedback** | Quanto dell'uscita viene reimmesso nell'effetto. Valori più alti rendono il wah più risonante e pronunciato. | -1 a +1 (0.5) |
| **Velocità** | Quanto velocemente il filtro spazza su e giù. Valori più alti danno un wah più veloce e ritmico. | 0,1 a 9 Hz (2.0) |
| **Gamma** | Quanto lontano spazza il filtro, in ottave. Valori più alti danno una spazzata più ampia e drammatica. | 0,1 a 9 ottave (4.3) |
| **Frequenza** | La frequenza di base intorno a cui spazza il filtro. Valori più bassi suonano più profondi; quelli più alti più brillanti. | 1 a 1000 Hz (50) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Classic** | Una spazzata wah bilanciata e classica. Un buon punto di partenza per funk e rock. |
| **Slow** | Una spazzata lenta e ampia che deriva dolcemente su e giù. Ottima per pad e note lunghe. |
| **Funky** | Una spazzata veloce e decisa con tanto movimento. Aggiunge mordente ritmico a chitarre e synth. |
| **Deep** | Una spazzata profonda e ampia che parte da una bassa frequenza. Grande e drammatica. |
| **Subtle** | Un movimento delicato e sobrio. Aggiunge carattere senza dominare il suono. |
| **Resonant** | Un wah netto e risonante con alto feedback. Simile alla voce ed espressivo. |

## Phaser (whoosh vorticoso)

**Cosa fa:** un filtro spazzante che aggiunge al suono un movimento vorticoso, tipo whoosh. Scegli un preset, oppure imposta tu stesso il feedback, la velocità, la gamma e la frequenza. Aggiunge movimento delicato e scintillio senza cambiare le note. È sottile su voci e pad, e drammatico su synth e chitarre. Prova Slow per un'atmosfera sognante o Jet per un vortice deciso.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Feedback** | Quanto dell'uscita viene reimmesso nell'effetto. Valori più alti rendono il phaser più risonante e pronunciato. | -1 a +1 (0.0) |
| **Velocità** | Quanto velocemente il filtro spazza su e giù. Valori più alti danno un phasing più veloce e ritmico. | 0,1 a 9 Hz (1.0) |
| **Gamma** | Quanto lontano spazza il filtro, in ottave. Valori più alti danno una spazzata più ampia e drammatica. | 0,1 a 9 ottave (4.0) |
| **Frequenza** | La frequenza di base intorno a cui spazza il filtro. Valori più bassi suonano più profondi; quelli più alti più brillanti. | 1 a 1000 Hz (100) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Classic** | Una spazzata phaser bilanciata e classica. Un buon punto di partenza per chitarre e tastiere. |
| **Slow** | Una spazzata lenta e ampia che deriva dolcemente su e giù. Ottima per pad e note lunghe. |
| **Fast** | Una spazzata veloce e scintillante con tanto movimento. Aggiunge moto ed energia. |
| **Deep** | Una spazzata profonda e ampia che parte da una bassa frequenza. Grande e drammatica. |
| **Subtle** | Un movimento delicato e sobrio. Aggiunge carattere senza dominare il suono. |
| **Jet** | Una spazzata intensa e risonante con alto feedback, il classico whoosh dell'aereo a reazione. |

## Flanger (spazzata dell'aereo a reazione)

**Cosa fa:** un breve delay in movimento che dà al suono un whoosh spazzante, simile a un jet. Scegli un preset, oppure imposta tu stesso la profondità, il feedback, la velocità e il delay. È un cugino più forte e più metallico del phaser, famoso per la spazzata sibilante del rock classico e della musica elettronica. Impostazioni sottili aggiungono movimento delicato, mentre impostazioni profonde sono drammatiche ed evidenti. Meglio usarlo con parsimonia, per effetto.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Profondità** | Quanto è forte l'effetto di spazzata. Valori più alti rendono il flanging più evidente. | 0 a 100% (25) |
| **Feedback** | Quanto dell'uscita viene reimmesso nell'effetto. Valori più alti rendono il flanger più risonante e metallico. | -99 a +99% (-50) |
| **Velocità** | Quanto velocemente la spazzata si muove su e giù. Valori più alti danno un movimento più veloce e scintillante. | 0 a 10 Hz (0.25) |
| **Delay** | Il tempo di delay di base su cui è costruita la spazzata. Valori più alti danno un carattere più profondo e cavo. | 0 a 4 ms (2.0) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Classic** | Un flanger bilanciato e classico. Un buon punto di partenza per chitarre e tastiere. |
| **Subtle** | Una spazzata delicata e sobria. Aggiunge movimento senza dominare il suono. |
| **Deep** | Una spazzata profonda e pesante con forte feedback. Grande e drammatica. |
| **Jet** | Una spazzata intensa con feedback positivo, il classico whoosh dell'aereo a reazione. |
| **Fast** | Una spazzata veloce e scintillante con tanto movimento ed energia. |
| **Wide** | Una spazzata lenta e ampia con un lungo delay. Rigogliosa e spaziosa. |

## Echo (ripetizioni)

**Cosa fa:** ripete il suono come echi che svaniscono per un senso di spazio e profondità. Scegli un preset, oppure imposta tu stesso il mix wet, il feedback e il delay. È come gridare in un canyon: il suono ritorna una o più volte dopo una breve pausa. Una singola ripetizione breve aggiunge corpo e un tocco retrò, mentre ripetizioni più lunghe con più feedback creano code spaziose e trascinate. Il preset Ping Pong fa rimbalzare le ripetizioni tra l'orecchio sinistro e destro, il che è divertente in cuffia. Mantieni il mix wet moderato così gli echi sostengono la musica invece di coprirla.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Mix wet** | Quanto sono forti gli echi rispetto al suono originale. Valori più alti fanno risaltare di più le ripetizioni. | -2 a +2 (0.6) |
| **Feedback** | Quante volte l'eco si ripete. Valori più alti danno più ripetizioni che impiegano più tempo a svanire. | -1 a +1 (0.5) |
| **Delay** | Il tempo tra gli echi. Valori più brevi danno uno slap-back serrato; valori più lunghi danno ripetizioni distanziate. | 0,01 a 2 s (0.4) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Slapback** | Una singola ripetizione serrata subito dietro il suono. Il classico slap-back rockabilly. |
| **Room** | Un eco breve e naturale, come una piccola stanza. Aggiunge spazio senza sbavare il suono. |
| **Tape** | Ripetizioni calde e medie che svaniscono gradualmente, come un vecchio delay a nastro. |
| **Dub** | Ripetizioni lunghe e pesanti con forte feedback. Grande, dubby e spazioso. |
| **Ping Pong** | Gli echi rimbalzano tra gli altoparlanti sinistro e destro per un ampio effetto stereo. |
| **Long** | Ripetizioni lente e molto distanziate che si trascinano lontano dietro il suono. |

## Chorus (suono più corposo e ampio)

**Cosa fa:** ispessisce e allarga il suono sovrapponendo una copia mutevole all'originale. Scegli un preset, oppure imposta tu stesso il mix wet/dry, la profondità, la velocità e il feedback. Fa suonare un singolo strumento o una voce come se ne suonassero diversi insieme, aggiungendo copie leggermente scordate e in movimento. Questo aggiunge ricchezza e un delicato scintillio. Impostazioni sottili scaldano le cose, mentre impostazioni forti suonano rigogliose e sognanti. È popolare su chitarre, tastiere e voci.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Wet/Dry** | Quanto del chorus senti rispetto al suono originale. Valori più alti rendono l'effetto più evidente. | 0 a 100% (50) |
| **Profondità** | Quanto oscilla l'intonazione su e giù. Valori più alti danno un suono più corposo e scintillante. | 0 a 100% (25) |
| **Velocità** | Quanto velocemente si muove lo scintillio. Velocità più lente suonano delicate e rigogliose; più veloci suonano più come un vibrato. | 0 a 10 Hz (1.1) |
| **Feedback** | Quanto dell'effetto viene reimmesso in sé stesso. Valori più alti rendono il chorus più risonante e intenso. | -99 a +99% (25) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Subtle** | Un delicato ispessimento che aggiunge calore senza attirare l'attenzione su di sé. |
| **Lush** | Un chorus ricco e classico. Un'ottima impostazione tuttofare per chitarre e tastiere. |
| **Ensemble** | Uno scintillio pieno e stratificato che fa suonare un singolo strumento come se ne fossero diversi. |
| **Vibrato** | Completamente wet con una velocità rapida, per un vibrato oscillante invece di un chorus sottile. |
| **Wide** | Uno scintillio lento e ampio che apre l'immagine stereo. Spazioso e sognante. |
| **Twelve-String** | Uno scintillio brillante e risonante che ricorda una chitarra a dodici corde. |

## Distorsione (grinta e mordente)

**Cosa fa:** aggiunge grinta e mordente sovraccaricando il suono. Scegli un preset, oppure imposta tu stesso il drive, l'output e il tono. Irruvidisce deliberatamente il suono, da un mordente caldo e grintoso a un timbro rotto e fuzzy. È un effetto creativo, per divertirsi, più che un modo per migliorare la qualità, quindi usalo in piccole quantità. È divertente su brani elettronici, rock e sperimentali. Abbassa l'Output se un preset pesante diventa troppo forte.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Drive** | Quanto duramente il suono è distorto. Valori più alti sono più grintosi e più aggressivi. | 0 a 100% (15) |
| **Output** | Il livello di uscita dopo la distorsione. Abbassalo se un'impostazione pesante diventa troppo forte. | -60 a 0 dB (-18) |
| **Tono** | Attenua gli alti prima della distorsione. Valori più bassi suonano più scuri e caldi. | 100 a 8000 Hz (8000) |
| **Centro** | Intorno a quale frequenza è focalizzata la distorsione. Sposta il carattere verso il più brillante o il più scuro. | 100 a 8000 Hz (2400) |
| **Larghezza** | Quanto è ampio quel focus. Stretto suona netto e nasale; ampio suona pieno e aperto. | 100 a 8000 Hz (2400) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Warm Drive** | Una grinta leggera e calda che aggiunge mordente senza cambiare molto il carattere. |
| **Crunch** | Un classico overdrive croccante, deciso e ritmico. |
| **Overdrive** | Un timbro brillante e spinto con tanto mordente. Ottimo per i suoni solisti. |
| **Fuzz** | Un fuzz corposo e saturo. Pesante e pieno di armoniche. |
| **Metal** | Un timbro serrato, focalizzato sui medi e ad alto guadagno per suoni aggressivi e pesanti. |
| **Screamer** | Un overdrive con medi potenziati che buca il mix, come un tube screamer. |
| **LoFi** | Una distorsione schiacciata a banda stretta per un carattere grintoso lo-fi. |

## Rotate (stereo rotante)

**Cosa fa:** fa girare il suono intorno al campo stereo per un effetto rotante e vorticoso. Scegli un preset, oppure imposta tu stesso la velocità. Sposta lentamente il suono intorno ai tuoi canali sinistro e destro, un po' come un altoparlante rotante, il che aggiunge una sensazione vorticosa e ipnotica. Impostazioni lente sono delicate e ampie, mentre impostazioni veloci sono vertiginose ed evidenti. È un effetto stereo, quindi è più notevole in cuffia o con altoparlanti ben posizionati.

**Cursore:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Velocità** | Quanto velocemente il suono gira intorno al campo stereo. Valori negativi girano dall'altra parte; zero lo tiene fermo. | -5 a +5 Hz (1.0) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Slow Pan** | Una deriva lenta e delicata da un lato all'altro. Sottile e ampia. |
| **Sway** | Un dondolio costante sinistra-destra. Aggiunge movimento delicato all'immagine stereo. |
| **Rotary** | Una rotazione media che ricorda un altoparlante rotante. |
| **Fast Spin** | Una rotazione veloce intorno al campo stereo per un effetto vertiginoso e vorticoso. |
| **Reverse** | Una rotazione media nella direzione opposta. |
| **Whirl** | Un vortice molto veloce. Intenso e disorientante. |

## Crossfeed (suono naturale in cuffia)

Sugli altoparlanti, ciascuno dei tuoi orecchi sente sia l'altoparlante sinistro sia quello destro, solo con tempi e volumi leggermente diversi. In cuffia, quella fusione naturale scompare: il tuo orecchio sinistro sente solo il canale sinistro e quello destro solo il destro. Questo «super stereo» può far sembrare la musica divisa dentro la tua testa, e le registrazioni con panning netto, dove uno strumento sta interamente su un lato, possono risultare innaturali o affaticanti negli ascolti lunghi.

Il Crossfeed risolve questo mescolando una piccola quantità filtrata di ciascun canale nell'altro, con un minuscolo delay e una delicata attenuazione delle alte frequenze. Questo è vicino a come il suono di altoparlanti reali raggiunge entrambi i tuoi orecchi, incluso il modo in cui la tua testa ombreggia leggermente l'orecchio più lontano. Il risultato è un'immagine più naturale, simile a quella degli altoparlanti, che sta un po' davanti a te invece che dentro la tua testa, e riduce l'affaticamento nelle sessioni lunghe. Flacbox usa il ben noto metodo **bs2b (Bauer stereophonic-to-binaural)**, un rispettato crossfeed open-source usato da molti lettori audiophile. Puoi leggere dell'algoritmo sulla [pagina del progetto bs2b](https://bs2b.sourceforge.net/).

La **Frequenza di taglio** controlla quanto suona caldo il mix, e il **Livello di feed** controlla quanto è forte. I preset coprono i classici livelli bs2b, da un tocco appena percettibile fino a un mix deciso, simile agli altoparlanti. Il Crossfeed è un effetto per cuffie, quindi lascialo spento quando ascolti sugli altoparlanti.

**Cursori:**

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza di taglio** | Imposta dove il travaso tra i canali inizia ad attenuarsi. Valori più bassi danno un effetto più caldo e più pronunciato. | 300 a 2000 Hz (700) |
| **Livello di feed** | Controlla quanto di un canale travasa nell'altro. Valori più alti producono un suono più simile agli altoparlanti. | 1 a 15 dB (4.5) |

**Preset:**

| Preset | Cosa fa |
|---|---|
| **Subtle** | Crossfeed appena percettibile per un ascolto casuale. Ammorbidisce lo stereo con panning netto senza cambiare l'equilibrio timbrico. |
| **Chu Moy** | Il classico predefinito tuttofare. Bilanciato e leggermente caldo, funziona su quasi ogni materiale. Parti da qui. |
| **Strong** | Travaso più forte per mix con panning più netto. Restringimento stereo più evidente. |
| **Jan Meier** | Popolare tra gli appassionati di cuffie. Feed più ampio, presentazione più simile agli altoparlanti, leggera spinta sui bassi. |
| **Speaker-like** | Regolato per la riproduzione più naturale in stile altoparlanti in cuffia. |
| **Vintage Stereo** | Crossfeed aggressivo regolato per i mix anni '60 e '70 con batteria e voci con panning netto. |

## Elaborazione del segnale: costruisci la tua catena DSP

Oltre agli effetti già pronti, Flacbox ti permette di costruire la tua catena in **Impostazioni > Lettore audio > Elaborazione del segnale**. Come spiega l'app quando la catena è vuota: *«Tocca + per aggiungere un effetto. Attiva o disattiva ciascuno con il suo interruttore, trascina per riordinare, tocca per modificare i suoi parametri e tieni premuto a lungo per duplicare o eliminare.»*

L'**ordine conta**: un filtro prima di una distorsione suona diverso dallo stesso filtro dopo di essa. Puoi anche indirizzare l'intera catena verso **Tutti i canali**, il **Canale sinistro** o il **Canale destro**.

Qui sotto c'è ogni blocco, con il testo stesso dell'app per ciascun cursore e ciascun preset.

### Gain (regolazione del livello)

Alza o abbassa il livello in un punto della catena.

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Gain** | Aumenta o taglia il livello in questo punto della catena. Usalo per recuperare livello dopo altri effetti, o per spingere quelli che seguono. | -24 a +24 dB (0) |

| Preset | Cosa fa |
|---|---|
| **Unity** | Nessun cambiamento di livello. Un punto di partenza neutro. |
| **Cut** | Un grande taglio. Doma una sorgente forte, o fa spazio prima degli effetti che seguono. |
| **Trim** | Un taglio delicato per tirare un po' indietro il livello. |
| **Lift** | Un aumento modesto per sollevare una sorgente silenziosa. |
| **Boost** | Un aumento forte per materiale silenzioso, o per spingere più duramente gli effetti che seguono. |
| **Max** | Aumento massimo. Forte, attenzione al clipping più avanti nella catena. |

### Low Pass (rimuove gli alti)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza di taglio** | Imposta dove il filtro inizia ad attenuare gli alti. Abbassala per scurire e ammorbidire il suono; alzala verso l'alto per aprire completamente. | 20 Hz a 20 kHz (20 kHz) |
| **Risonanza** | Enfatizza le frequenze proprio alla frequenza di taglio. Tienila bassa per un'attenuazione pulita; alzala per un bordo con picco, sibilante. | 0,1 a 10 (0.707) |

| Preset | Cosa fa |
|---|---|
| **Air** | Rifila solo la parte più alta. Toglie un po' di mordente senza spegnere il suono. |
| **Warm** | Una delicata attenuazione degli alti per un timbro più caldo e rotondo. |
| **Mellow** | Notevolmente ammorbidito. Tira indietro la brillantezza per un'atmosfera rilassata. |
| **Muffled** | Scuro e ovattato, come sentito attraverso un muro. |
| **Telephone** | Un picco stretto e risonante in basso nella gamma. Una voce sottile, tipo telefono. |

### High Pass (rimuove i bassi)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza di taglio** | Imposta dove il filtro inizia ad attenuare i bassi. Alzala per assottigliare le basse frequenze e rimuovere il rimbombo; abbassala verso il fondo per aprire completamente. | 20 Hz a 20 kHz (20 Hz) |
| **Risonanza** | Enfatizza le frequenze proprio alla frequenza di taglio. Tienila bassa per un'attenuazione pulita; alzala per un bordo con picco, sibilante. | 0,1 a 10 (0.707) |

| Preset | Cosa fa |
|---|---|
| **Rumble Cut** | Rimuove il rimbombo subsonico e l'offset DC senza toccare le basse frequenze udibili. |
| **Tighten** | Rifila le basse frequenze rimbombanti per un basso più serrato e pulito. |
| **Thin** | Taglia il calore e il corpo, lasciando un suono più leggero e sottile. |
| **Radio** | Restano solo i medi e gli alti, come un piccolo altoparlante radio. |
| **Telephone** | Un picco stretto e risonante in alto nella gamma. Una voce sottile, tipo telefono. |

### Band Pass (mantiene una banda centrale)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Centro** | Imposta la frequenza che il filtro lascia passare. Tutto sopra e sotto viene attenuato. Spazzalo per isolare bassi, medi o alti. | 20 Hz a 20 kHz (1 kHz) |
| **Risonanza** | Controlla quanto è ampia la banda. Valori bassi lasciano passare una gamma ampia; alzala per restringere sul centro per un timbro netto e risonante. | 0,1 a 10 (0.707) |

| Preset | Cosa fa |
|---|---|
| **Voice** | Una banda ampia intorno alla gamma media dove sta la maggior parte delle voci. Un punto di partenza neutro. |
| **Bass** | Isola le basse frequenze, lasciando solo il basso e la cassa. |
| **Body** | Si focalizza sui bassi-medi per un corpo caldo e squadrato. |
| **Presence** | Alza i medio-alti per chiarezza e presenza. |
| **Telephone** | Una banda media stretta. Un suono sottile, tipo telefono. |
| **Wah** | Un picco molto stretto e risonante. Spazza il centro per un effetto wah. |

### Notch (rimuove una banda stretta)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza** | Imposta la frequenza che il filtro rimuove. Tutto sopra e sotto passa. Sintonizzala su un ronzio o una risonanza per eliminarlo. | 20 Hz a 20 kHz (60 Hz) |
| **Risonanza** | Controlla quanto è ampio il taglio. Valori bassi scavano una gamma ampia; alzala per rimuovere solo una banda puntuale e lasciare intatto il resto. | 0,1 a 10 (8.0) |

| Preset | Cosa fa |
|---|---|
| **Mains Hum 60** | Rimuove il ronzio elettrico a 60 Hz (rete nordamericana). Un punto di partenza neutro. |
| **Mains Hum 50** | Rimuove il ronzio elettrico a 50 Hz (rete europea e altre). |
| **Rumble** | Taglia un rimbombo o una risonanza a bassa frequenza senza assottigliare tutto il fondo. |
| **Mud** | Scava il fango dei bassi-medi per un suono più pulito e chiaro. |
| **Boxy** | Rimuove un rimbombo squadrato della gamma media. |
| **Harsh** | Doma un picco aspro e penetrante nei medio-alti. |

### Peaking (banda EQ parametrica)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza** | Il centro della banda da aumentare o tagliare. Spazzalo per trovare la frequenza che vuoi modellare. | 20 Hz a 20 kHz (1 kHz) |
| **Gain** | Quanto aumentare o tagliare al centro. Positivo solleva la banda; negativo la scava. | -15 a +15 dB (0) |
| **Fattore Q** | Imposta quanto è ampia la banda. Valori bassi modellano un'area ampia; valori alti restringono per cambiamenti chirurgici e puntuali. | 0,1 a 10 (1.0) |

| Preset | Cosa fa |
|---|---|
| **Presence** | Un ampio sollevamento dei medio-alti per chiarezza e presenza. Un punto di partenza neutro. |
| **Warmth** | Un ampio aumento dei bassi-medi che aggiunge corpo e calore. |
| **Vocal Boost** | Solleva la gamma centrale della voce per portare avanti le voci. |
| **Cut Mud** | Scava il fango squadrato dei bassi-medi per un suono più pulito. |
| **Tame Harsh** | Un taglio stretto per domare un picco aspro e penetrante. |
| **Punch** | Un aumento basso che aggiunge punch e impatto alle basse frequenze. |
| **Sub Boost** | Un aumento profondo proprio in fondo per un peso extra dei sub-bassi. |
| **Air** | Un ampio sollevamento in cima per una brillantezza aperta e ariosa. |
| **Clarity** | Solleva i medio-alti per aggiungere definizione e mordente. |
| **De-Ess** | Un taglio stretto nella gamma delle sibilanti per domare le S aspre. |
| **De-Boom** | Taglia un accumulo rimbombante a bassa frequenza per un fondo più serrato. |
| **Scoop** | Un ampio avvallamento della gamma media per un timbro scavato e moderno. |

### Low Shelf (controllo dei bassi e aumento dei bassi)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza** | Imposta l'angolo al di sotto del quale lo shelf ha effetto. Tutto ciò che sta sotto viene aumentato o tagliato insieme. | 20 a 2000 Hz (200) |
| **Gain** | Quanto sollevare o abbassare le basse frequenze. Positivo aggiunge peso e calore; negativo le assottiglia. | -15 a +15 dB (0) |

| Preset | Cosa fa |
|---|---|
| **Warmth** | Un delicato sollevamento delle basse frequenze per calore e corpo. Un punto di partenza neutro. |
| **Bass Boost** | Un solido aumento dei bassi per peso e punch. |
| **Fullness** | Riempie i bassi-medi per un suono più pieno e rotondo. |
| **Trim Bass** | Un taglio modesto per alleggerire un mix carico di bassi. |
| **Cut Lows** | Un forte taglio per assottigliare o togliere il rimbombo alle basse frequenze. |
| **Big Bottom** | Un grande aumento delle basse frequenze per il massimo peso e rimbombo. |

### High Shelf (controllo degli acuti)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Frequenza** | Imposta l'angolo al di sopra del quale lo shelf ha effetto. Tutto ciò che sta sopra viene aumentato o tagliato insieme. | 1 a 20 kHz (8 kHz) |
| **Gain** | Quanto sollevare o abbassare le alte frequenze. Positivo aggiunge brillantezza e aria; negativo ammorbidisce e scurisce. | -15 a +15 dB (0) |

| Preset | Cosa fa |
|---|---|
| **Presence** | Un delicato sollevamento degli alti per chiarezza e dettaglio. Un punto di partenza neutro. |
| **Air** | Apre la parte più alta per un suono arioso e aperto. |
| **Bright** | Un forte aumento per un timbro nitido, brillante e in avanti. |
| **Soften** | Un taglio modesto per togliere il mordente agli alti aspri. |
| **Tame Highs** | Un forte taglio per scurire e ammorbidire un suono eccessivamente brillante. |
| **Sparkle** | Un grande aumento in cima per il massimo scintillio e brillantezza. |

### Soft Clip (saturazione calda)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Drive** | Spinge il segnale più duramente nel waveshaper. Piccole quantità aggiungono calore delicato; quantità elevate arrotondano i picchi in una saturazione corposa e grintosa. | 0 a 40 dB (0) |

| Preset | Cosa fa |
|---|---|
| **Warm** | Un tocco di drive per un calore delicato, in stile analogico. |
| **Drive** | Saturazione notevole che ispessisce e colora il suono. |
| **Crunch** | Drive pesante con un bordo croccante udibile. |
| **Fuzz** | Distorsione corposa e fuzzy. I picchi sono schiacciati duramente. |
| **Destroy** | Drive massimo. Grinta aggressiva e completamente satura. |

### Bit Crusher (retrò lo-fi)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Profondità di bit** | Imposta quanti bit descrivono ogni campione. Meno bit significano passi più grossolani e più rumore di quantizzazione, per un suono digitale croccante e grintoso. | 1 a 16 bit (16) |
| **Frequenza di campionamento** | Riduce il campionamento dell'audio. Al cento per cento la frequenza è intatta; abbassala per tenere ogni campione più a lungo, spegnendo gli alti e aggiungendo un bordo aspro e con aliasing. | 1% a 100% (100%) |

| Preset | Cosa fa |
|---|---|
| **Vintage** | Un sottile calo di qualità, come un primo campionatore digitale. |
| **LoFi** | Classico lo-fi a 8 bit, mezza frequenza. Granuloso e retrò. |
| **Crunch** | Schiacciamento più pesante con un bordo croccante udibile. |
| **Gritty** | Grossolano e grintoso. I passi tra i livelli sono evidenti. |
| **Destroy** | Riduzione estrema. Aspro, rotto, a malapena riconoscibile. |

### Ring Modulator (toni metallici e robotici)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Portante** | Imposta la frequenza del tono per cui il segnale è moltiplicato. Pochi hertz danno un tremolo oscillante; frequenze più alte aggiungono armoniche metalliche, campanellanti e robotiche. | 1 a 4000 Hz (440) |
| **Mix** | Fonde il suono modulato con l'originale. A zero per cento senti solo il segnale dry; al cento per cento solo il tono completamente modulato. | 0% a 100% (0%) |

| Preset | Cosa fa |
|---|---|
| **Tremolo** | Una portante molto bassa lo trasforma in un tremolo di ampiezza, oscillando il volume. |
| **Robot** | Una portante media aggiunge armoniche metalliche per un classico effetto voce-robot. |
| **Metallic** | Armoniche dense e inarmoniche per un timbro aspro e metallico. |
| **Bell** | Una portante più alta dà un tintinnio brillante, tipo campana. |
| **Alien** | Completamente wet con una portante alta. Estremo, alieno, a malapena riconoscibile. |

### Tremolo (oscillazione del volume)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Velocità** | Imposta quanto velocemente pulsa il volume. Velocità più lente danno un dondolio morbido; più veloci danno uno stutter rapido. | 0,1 a 20 Hz (5) |
| **Profondità** | Imposta quanto cala il volume a ogni pulsazione. A zero per cento il livello è costante; al cento per cento scende fino al silenzio. | 0% a 100% (0%) |

| Preset | Cosa fa |
|---|---|
| **Gentle** | Un dondolio lento e superficiale. Movimento sottile senza attirare l'attenzione. |
| **Classic** | Il classico tremolo da amplificatore: velocità media e profondità moderata. |
| **Deep** | Una pulsazione forte e profonda che quasi scende al silenzio a ogni ciclo. |
| **Fast** | Un rapido tremolio per una sensazione scintillante e nervosa. |
| **Chop** | Veloce e a piena profondità. Un chop duro e a scatti. |

### Delay (eco)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Tempo** | Imposta la pausa prima di ogni eco. Tempi brevi danno uno slapback serrato; tempi più lunghi distanziano di più le ripetizioni. | 0,01 a 2 s (0.25) |
| **Feedback** | Imposta quanto di ogni eco viene reimmesso. Valori bassi danno una singola ripetizione; valori più alti costruiscono una lunga serie di echi trascinati. | 0 a 0.95 (0.4) |
| **Mix** | Fonde gli echi con l'originale. A zero per cento senti solo il segnale dry; al cento per cento solo gli echi. | 0% a 100% (0%) |

| Preset | Cosa fa |
|---|---|
| **Slapback** | Un singolo eco breve, serrato contro l'originale. Rockabilly e raddoppio vocale. |
| **Echo** | Il classico eco: una ripetizione chiara con alcune code trascinate. |
| **Ping** | Una ripetizione rapida e rimbalzante che aggiunge movimento ritmico. |
| **Ambient** | Ripetizioni più lunghe e morbide che si dissolvono in una coda spaziosa. |
| **Dub** | Alto feedback per lunghe cascate dubby di eco. |
| **Cavern** | Ripetizioni lunghe e profonde, come suono che riecheggia in un enorme spazio. |

### Stereo Width (restringi o allarga)

| Controllo | Cosa fa | Intervallo (predefinito) |
|---|---|---|
| **Larghezza** | Restringe o allarga l'immagine stereo. Zero per cento collassa in mono, cento per cento la lascia intatta, e valori più alti spingono i lati più larghi. Influisce solo sui brani stereo con destinazione Tutti i canali. | 0% a 200% (100%) |

| Preset | Cosa fa |
|---|---|
| **Wide** | Un delicato allargamento che apre l'immagine stereo. Un punto di partenza neutro. |
| **Wider** | Una diffusione più forte per un campo stereo grande e immersivo. |
| **Max** | Larghezza massima. Molto ampia, ma attenzione ai problemi di compatibilità mono. |
| **Narrow** | Tira i lati verso l'interno per un'immagine più serrata e centrata. |
| **Focused** | Quasi centrata, con solo un accenno di stereo. |
| **Mono** | Completamente collassata in mono. Entrambi gli altoparlanti riproducono lo stesso segnale. |

## Come funziona tutto sotto il cofano (versione semplice)

- **Motori:** ne scegli uno in Impostazioni > Lettore audio > Motore di riproduzione: **Standard** (sistema), **Universal** (FFmpeg) o **Sound FX** (il **motore BASS™** di [Un4seen Developments](https://www.un4seen.com/)). Il motore che scegli decide quali formati vengono riprodotti, e gli effetti, l'equalizzatore e la catena DSP funzionano solo nel motore Sound FX.
- **Formati:** il motore BASS™ aggiunge FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e la musica a moduli (tracker) oltre ai formati di sistema e FFmpeg.
- **Effetti:** l'equalizzatore, il compressore e la maggior parte degli effetti usano gli add-on per effetti di BASS™. Freeverb è il riverbero Freeverb. Chorus, Flanger e Distorsione usano classici effetti in stile DirectX con i propri controlli.
- **Normalizzazione del volume:** un livellatore di loudness **EBU R128** in tempo reale (lo standard di loudness usato in broadcast e streaming).
- **Crossfeed:** il crossfeed **bs2b (Bauer)**, eseguito dentro il motore BASS™.
- **Catena DSP:** i tuoi blocchi personalizzati, applicati nell'esatto ordine che imposti, su tutti i canali o su un solo lato.
- **Uscita:** puoi impostare la frequenza di campionamento, il numero di canali e la dimensione del buffer per adattarli alla tua attrezzatura.

Poiché tutto questo viene eseguito in tempo reale mentre la musica suona, gli effetti:

- Funzionano in **tempo reale** su tutto, inclusi file su cloud, trasmissioni e musica a moduli.
- **Non cambiano né risalvano mai** i tuoi file. Spegni un effetto e l'originale ritorna.
- **Ricordano le tue impostazioni** per ogni effetto.
- Possono essere **mescolati e combinati** liberamente, poiché ognuno è separato.

## Ricette semplici da provare

**Ascolto di tutti i giorni**

- **Più bassi, in modo pulito:** Equalizzatore > Bass Booster, poi abbassa il Preamplificatore di 1 o 2 dB. Oppure aggiungi un Low Shelf DSP su Bass Boost.
- **Volume uniforme su una playlist mista:** Normalizzazione del volume > Standard, più Compressore > Soft.
- **Rifinitura complessiva delicata:** Compressore > Transparent, più Normalizzazione del volume > Light.
- **Voci più chiare:** Equalizzatore > Vocal Booster, o un blocco Peaking DSP su Vocal Boost.
- **Suono più pieno sui piccoli altoparlanti del telefono:** Equalizzatore > Small Speakers.

**Cuffie**

- **Più gradevole e meno affaticante in cuffia:** Crossfeed > Chu Moy o Jan Meier.
- **Suono più ampio in cuffia:** Stereo Width DSP > Wide, più Crossfeed > Chu Moy.
- **Correggi i dischi anni '60 e '70 con panning netto:** Crossfeed > Vintage Stereo.
- **Un po' di aria e spazio:** Freeverb > Ambience, tenuto basso, più Crossfeed > Subtle.

**Momenti tranquilli e audio parlato**

- **Ascolto silenzioso a tarda notte:** Normalizzazione del volume > Night, più Compressore > Late Night.
- **Podcast e audiolibri:** Compressore > Voice / Podcast, più Equalizzatore > Spoken Word.
- **Suono più forte e uniforme in un'auto rumorosa:** Normalizzazione del volume > Strong, più Compressore > Heavy.

**Risoluzione dei problemi**

- **Doma una registrazione aspra e brillante:** Equalizzatore > Treble Reducer, o un blocco Peaking DSP su Tame Harsh.
- **Rimuovi il ronzio elettrico:** catena DSP > Notch > Mains Hum 60 (o Mains Hum 50 in Europa).
- **Bassi più serrati e puliti:** High Pass DSP > Tighten, per tagliare le basse frequenze rimbombanti.
- **Meno rimbombo in un mix carico di bassi:** Low Shelf DSP > Trim Bass, o Peaking > De-Boom.

**Creativo e divertente**

- **Atmosfera calda e spaziosa:** Freeverb > Hall, tenuto basso.
- **Chitarre sognanti e spaziose:** Chorus > Wide, più Echo > Long.
- **Retrò lo-fi:** catena DSP > Bit Crusher (LoFi) in Soft Clip (Warm).
- **Movimento funky sui brani elettronici:** Auto Wah > Funky, o Phaser > Fast.
- **Classica spazzata dell'aereo a reazione:** Flanger > Jet.

## Domande frequenti

{{% details title="Quale motore audio usa Flacbox?" closed="true" %}}
Scegli un unico Motore di riproduzione in Impostazioni > Lettore audio: Standard (il motore di sistema di Apple), Universal (il motore FFmpeg) o Sound FX (il motore BASS™ di Un4seen Developments, un4seen.com). Il motore che scegli decide quali formati di file vengono riprodotti. Sound FX è quello che riproduce formati extra come FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus e musica MOD o tracker, ed è l'unico motore che fornisce gli effetti in tempo reale, l'equalizzatore a 10 bande e la catena DSP. Per usare gli effetti, imposta il Motore di riproduzione su Sound FX.
{{% /details %}}

{{% details title="Flacbox può riprodurre MOD, XM, IT e altra musica tracker o a moduli?" closed="true" %}}
Sì. Il motore BASS™ ha un lettore a moduli integrato che carica file MOD, XM, IT, S3M, MTM, UMX e MO3 e ricostruisce la canzone dal vivo dai suoi pattern e suoni di strumenti, nel modo in cui la musica tracker è pensata per essere riprodotta. I normali lettori per iPhone non possono farlo. Gli effetti e l'equalizzatore funzionano anche sulla musica a moduli.
{{% /details %}}

{{% details title="Flacbox supporta i file DSD e ad alta risoluzione?" closed="true" %}}
Sì. Flacbox riproduce i file DSD (DSF e DFF) attraverso il motore BASS™ usando DSD over PCM così funzionano su hardware di uscita normale, oltre a FLAC, WavPack, Monkey's Audio (APE), Musepack e TrueAudio per la riproduzione lossless.
{{% /details %}}

{{% details title="Quali effetti sonori ha Flacbox?" closed="true" %}}
Un equalizzatore a 10 bande, Normalizzazione del volume, Compressore, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distorsione, Rotate e Crossfeed, più una catena DSP costruita da te con filtri, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay e stereo width. Ognuno è separato e può essere combinato con gli altri.
{{% /details %}}

{{% details title="Cos'è un preset?" closed="true" %}}
Un preset è un'impostazione già pronta per un effetto. Invece di muovere i cursori tu stesso, tocchi un preset e il suono cambia di conseguenza. Ogni effetto in Flacbox ha diversi preset, e questa guida elenca cosa fa ciascuno. Se muovi un cursore dopo aver scelto un preset, l'effetto mostra «Manuale» per dirti che ora sta usando i tuoi valori.
{{% /details %}}

{{% details title="Come apro gli effetti audio in Flacbox?" closed="true" %}}
Apri il lettore Now Playing, tocca il pulsante ⋯ (Altre azioni) e scegli Effetti audio. Oppure vai su Impostazioni > Lettore audio > Effetti audio. Tocca un effetto, attiva il suo interruttore e scegli un preset, oppure apri i cursori per regolare con precisione.
{{% /details %}}

{{% details title="Dov'è l'equalizzatore e quali sono le migliori impostazioni?" closed="true" %}}
Vai su Impostazioni > Lettore audio > Equalizzatore audio. Ha 10 bande da 32 Hz a 16 kHz, ciascuna da -12 a +12 dB, più un Preamplificatore da -24 a +24 dB e 22 preset. Per più bassi, usa Bass Booster. Per voci più chiare, usa Vocal Booster o Pop. Per un suono più brillante, usa Treble Booster. Poi regola le singole bande a piacere.
{{% /details %}}

{{% details title="Come aumento i bassi in Flacbox?" closed="true" %}}
Due modi facili. Nell'Equalizzatore audio, scegli Bass Booster (o alza le bande a 32 Hz e 64 Hz di pochi dB). Oppure, in Elaborazione del segnale, aggiungi un blocco Low Shelf impostato su Bass Boost. In entrambi i casi, abbassa il Preamplificatore o aggiungi un blocco Gain di 1 o 2 dB così i bassi restano puliti e non distorcono.
{{% /details %}}

{{% details title="Quale preset dell'equalizzatore è il migliore per la mia musica?" closed="true" %}}
Rock ed Electronic aggiungono energia con bassi e alti forti. Acoustic, Jazz e Classical restano caldi e naturali. Pop e Vocal Booster portano avanti le voci. Bass Booster e Hip-Hop aggiungono peso. Deep e Loudness suonano più pieni a basso volume. Parti da quello che corrisponde al tuo genere, poi regola con precisione.
{{% /details %}}

{{% details title="Cos'è la Normalizzazione del volume e in cosa è diversa da ReplayGain?" closed="true" %}}
Fa suonare ogni brano circa allo stesso loudness. Misura il vero loudness usando lo standard EBU R128 (in LUFS, come i servizi di streaming) e regola ogni brano verso il tuo obiettivo, con un limite di boost massimo. A differenza di ReplayGain, non ha bisogno di tag nei tuoi file e funziona su qualsiasi sorgente, dal vivo, senza cambiare l'audio. Preset: Light, Standard, Strong e Night.
{{% /details %}}

{{% details title="Cos'è il Crossfeed e dovrei usarlo?" closed="true" %}}
Il Crossfeed mescola un po' dei canali sinistro e destro così le cuffie sembrano più altoparlanti reali e meno come se il suono fosse bloccato nella tua testa. È solo per le cuffie, quindi spegnilo per gli altoparlanti. Flacbox usa il metodo bs2b (Bauer), con preset come Chu Moy e Jan Meier.
{{% /details %}}

{{% details title="Qual è la differenza tra il Compressore e la Normalizzazione del volume?" closed="true" %}}
La Normalizzazione del volume abbina il loudness tra canzoni diverse. Il Compressore uniforma le parti forti e deboli all'interno di una singola canzone. Risolvono problemi diversi e lavorano bene insieme, specialmente in auto o in un posto rumoroso.
{{% /details %}}

{{% details title="Cos'è la catena di Elaborazione del segnale (DSP)?" closed="true" %}}
È un rack costruito da te in Impostazioni > Lettore audio > Elaborazione del segnale. Aggiungi blocchi come filtri, shelf, gain, soft clip, bit crusher, ring modulator, tremolo, delay e stereo width, mettili in qualsiasi ordine, attiva o disattiva ciascuno e indirizza la catena verso tutti i canali, sinistro o destro. Poiché l'ordine conta, puoi progettare esattamente il suono che vuoi.
{{% /details %}}

{{% details title="Qual è la differenza tra l'Equalizzatore, gli effetti e la catena DSP?" closed="true" %}}
L'Equalizzatore è un semplice controllo del timbro a 10 bande. Gli Effetti audio sono strumenti già pronti (compressore, riverbero, echo e così via) con preset. La catena DSP è dove costruisci il tuo ordine di effetti da singoli blocchi. Puoi eseguire tutti e tre contemporaneamente.
{{% /details %}}

{{% details title="Gli effetti cambiano o danneggiano i miei file musicali?" closed="true" %}}
No. Tutto viene applicato in tempo reale mentre la musica suona. I tuoi file non vengono mai cambiati né risalvati. Spegni un effetto e il suono originale ritorna all'istante.
{{% /details %}}

{{% details title="Posso usare più di un effetto contemporaneamente?" closed="true" %}}
Sì. Ogni effetto ha il proprio interruttore e non c'è un interruttore master, quindi funziona qualsiasi combinazione. Per esempio, Normalizzazione del volume più Compressore per un ascolto uniforme, o Freeverb più Crossfeed in cuffia, con l'equalizzatore in cima.
{{% /details %}}

{{% details title="Perché i controlli dell'effetto sono in grigio?" closed="true" %}}
L'effetto è spento. Attiva il suo interruttore in cima all'editor per usare i controlli. Ogni effetto è spento per impostazione predefinita.
{{% /details %}}

{{% details title="Cosa significa l'etichetta Manuale?" closed="true" %}}
Significa che hai spostato un cursore lontano da un preset, quindi l'effetto ora sta usando i tuoi valori personalizzati invece di un preset con nome. Ogni cursore ha un pulsante di ripristino, e scegliere di nuovo un preset sostituisce i tuoi valori manuali.
{{% /details %}}

{{% details title="Posso salvare e condividere i miei preset dell'equalizzatore?" closed="true" %}}
Sì. Oltre ai 22 preset integrati, puoi crearne di tuoi, riordinarli ed esportarli o importarli per spostare le tue impostazioni su un altro dispositivo.
{{% /details %}}

{{% details title="Gli effetti funzionano con CarPlay, lo streaming e la riproduzione in background?" closed="true" %}}
Sì. Gli effetti vengono eseguiti dentro il motore BASS™, quindi si applicano a file locali, drive su cloud, media server, trasmissioni e musica a moduli, e continuano a funzionare durante CarPlay e la riproduzione in background.
{{% /details %}}

{{% details title="Posso cambiare la qualità dell'uscita audio?" closed="true" %}}
Sì. In Impostazioni > Lettore audio puoi impostare la frequenza di campionamento in uscita, il numero di canali e la dimensione del buffer per adattarli alle tue cuffie, altoparlanti o DAC.
{{% /details %}}

{{% details title="Qual è una buona configurazione di partenza per le cuffie?" closed="true" %}}
Attiva la Normalizzazione del volume (Standard), aggiungi un Compressore leggero (Soft), scegli un preset dell'equalizzatore che ti piace e attiva il Crossfeed (Chu Moy o Jan Meier). Lascia spenti riverbero, echo e distorsione a meno che tu non voglia un suono creativo.
{{% /details %}}

---

*BASS è un marchio di Un4seen Developments Ltd. Vedi [un4seen.com](https://www.un4seen.com/). Il Crossfeed usa l'algoritmo bs2b (Bauer stereophonic-to-binaural); vedi la [pagina del progetto bs2b](https://bs2b.sourceforge.net/).*
