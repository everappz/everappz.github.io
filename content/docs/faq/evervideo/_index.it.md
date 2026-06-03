---
date: '2025-06-12T17:00:00+00:00'
title: 'Evervideo'
description: "FAQ di Evervideo: lettore video cloud HD e 4K per iPhone, iPad e Mac. Streaming e download di video da iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP/SFTP, DLNA e S3 — oltre a Plex, Jellyfin, Emby, Subsonic e Navidrome. Risposte su MKV, HEVC, AV1, video 360°/VR da Insta360 e GoPro Max, Picture-in-Picture, sottotitoli primari e secondari (SRT, VTT, ASS, libass), equalizzatori audio e video con preset, stream di telecamere IP RTSP, AirPlay 2, Chromecast, decodifica hardware H.264/HEVC, integrazione con le librerie Foto e Apple Music, modalità offline, backup, Family Sharing e piani Premium."
keywords: [
  "FAQ Evervideo", "Evervideo iPhone", "Evervideo iPad", "Evervideo Mac",
  "lettore video cloud", "lettore video HD iOS", "lettore video 4K iPhone",
  "lettore MKV iOS", "lettore HEVC iPhone", "lettore AV1 iOS",
  "lettore video FFmpeg", "lettore MP4 Mac", "lettore AVI iOS",
  "lettore video 360 iPhone", "lettore video VR iPhone", "lettore video Insta360",
  "Picture-in-Picture video iPhone", "lettore video PiP iPad",
  "lettore RTSP iPhone", "visualizzatore telecamera IP", "lettore video DLNA",
  "client Plex iPhone", "client Jellyfin iOS", "client Emby iPad",
  "video Subsonic", "client Navidrome", "lettore sottotitoli video",
  "sottotitoli SRT VTT ASS", "sottotitoli secondari iPhone", "doppi sottotitoli",
  "equalizzatore video iOS", "preset equalizzatore video",
  "streaming video da Google Drive", "streaming video da Dropbox",
  "streaming video da OneDrive", "streaming video da iCloud Drive",
  "streaming video da NAS", "video Chromecast iPhone", "video AirPlay 2",
  "lettore video libreria Foto", "lettore video Apple Music",
  "trasferimento video Wi-Fi Drive", "playlist video M3U", "video USB flash drive iPhone",
  "Evervideo Premium", "app video Family Sharing", "lettore video stile YouTube"
]
tags: ["evervideo", "faq", "streaming video", "lettore offline", "app video ios", "PiP", "sottotitoli", "video 360", "FFmpeg", "Plex", "RTSP"]
---


<div class="hx:mt-6"></div>

Evervideo è un **lettore video cloud** HD e 4K per **iPhone, iPad e Mac** che esegue lo streaming e scarica video da iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology, QNAP e qualsiasi sorgente WebDAV, SMB, NFS, FTP/SFTP, DLNA o S3 — oltre a server multimediali self-hosted come **Plex, Jellyfin, Emby, Subsonic** e **Navidrome**, e stream **RTSP** in diretta da telecamere IP. Costruito su un **motore di riproduzione basato su FFmpeg** personalizzato con **decodifica H.264/HEVC accelerata hardware**, tracce di sottotitoli primarie e secondarie (SRT/VTT/ASS/libass), un equalizzatore video con preset, un equalizzatore audio, **Picture-in-Picture**, **riproduzione 360°/VR** per filmati Insta360 e GoPro Max, casting **AirPlay 2** e **Chromecast**, e un lettore compatto sempre visibile. Questo FAQ risponde alle domande che gli utenti inviano più spesso. Per guide più approfondite, consulta la [Guida utente di Evervideo](/docs/guide/evervideo/).

<div class="hx:w-full">

{{% details title="Cos'è Evervideo?" closed="true" %}}
**Evervideo è un lettore video cloud HD e 4K completo di funzionalità per iPhone, iPad e Mac** che trasforma qualsiasi account di archiviazione cloud, NAS o server multimediale nella tua libreria video personale con il pieno controllo dei tuoi file.<br><br>

Costruito su un motore di riproduzione personalizzato basato su FFmpeg con decodifica H.264 e HEVC accelerata hardware, Evervideo riproduce praticamente qualsiasi container e codec moderno (MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS e la lunga lista di formati FFmpeg), supporta sottotitoli primari e secondari, include equalizzatore audio e video, e funziona in modalità Picture-in-Picture in modo da poter continuare a guardare mentre si usano altre app.
{{% /details %}}

{{% details title="Evervideo è gratuito? Qual è la differenza tra la versione Gratuita e la Premium?" closed="true" %}}
**Sì — Evervideo è gratuito da scaricare e usare**, con acquisti in-app opzionali per rimuovere i limiti e sbloccare il set completo di funzionalità Premium.<br><br>

Il Premium è disponibile come **acquisto una tantum a vita** o come **abbonamento mensile o annuale**, in modo da poter scegliere l'opzione più adatta. I prezzi possono variare in base al paese. Il **Family Sharing** è abilitato per ogni piano, quindi puoi condividere Premium con un massimo di cinque membri della tua famiglia. Gli acquisti a vita e gli abbonamenti sono condivisi tra iOS e macOS tramite iCloud — installa la versione più recente su ogni dispositivo, accedi con lo stesso Apple ID e attendi circa un minuto per la sincronizzazione delle informazioni di acquisto.<br><br>

**Evervideo Premium** rimuove ogni limite della versione gratuita: riproduzione senza pubblicità, playlist illimitate, servizi cloud connessi illimitati, preferiti illimitati, download offline illimitati, archivio (ZIP) di raccolte multimediali e personalizzazione completa (icona dell'app personalizzata, temi, schema colori).<br><br>

[Leggi il confronto completo Gratuito vs Premium](/docs/faq/evervideo/what-is-the-difference-between-evervideo-and-evervideo-premium/)
{{% /details %}}

{{% details title="Evervideo è sicuro?" closed="true" %}}
Evervideo utilizza solo SDK ufficiali e connessioni sicure per interagire con i servizi cloud collegati. Il tuo login e la tua password non sono disponibili per l'applicazione. Tutte le richieste dall'applicazione al servizio cloud sono crittografate.<br>
Quando inserisci login e password, l'applicazione ti mostra la pagina di autorizzazione ufficiale fornita dal provider del servizio cloud e l'intero processo di autorizzazione avviene al di fuori dell'applicazione. Il provider del servizio cloud invia un auth-token all'applicazione dopo l'autorizzazione riuscita e tale token viene utilizzato per effettuare chiamate API.<br><br>

L'auth-token è una chiave digitale che consente alle applicazioni di terze parti di interagire con l'archiviazione cloud. L'auth-token è memorizzato sul tuo dispositivo in un archivio di sistema sicuro chiamato Keychain. Puoi scaricare i tuoi file dal servizio cloud connesso al dispositivo e tali file verranno posizionati nella directory "Documenti" dell'app. Puoi rimuovere quei file in qualsiasi momento usando il file manager integrato.<br>
L'applicazione non condivide alcuna informazione dall'account cloud connesso. Puoi revocare l'accesso al tuo account cloud in qualsiasi momento aprendo la pagina delle impostazioni dell'account nel browser web.<br><br>

Per rifiutare l'auth-token accedi al tuo account nel browser web e vai alla pagina delle impostazioni. Lì puoi trovare tutte le app di terze parti collegate al tuo account cloud e rimuoverne qualsiasi se non vuoi più usare quell'applicazione.<br><br>

Un tutorial completo è disponibile qui:<br>
[Come disconnettere un'app di terze parti dal tuo account Google](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account/)<br><br>

Puoi anche disconnettere gli account cloud connessi nell'applicazione e l'auth-token verrà rimosso anche dal tuo dispositivo. Se rimuovi l'applicazione dal tuo dispositivo, tutti i dati scaricati e i token di accesso verranno rimossi.<br><br>

{{% /details %}}

{{% details title="Quali formati video supporta Evervideo?" closed="true" %}}
**Evervideo riproduce praticamente ogni container e codec video moderno su iPhone, iPad e Mac** grazie al motore FFmpeg integrato combinato con la decodifica H.264/HEVC accelerata hardware.<br><br>

**Container:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT e molti altri.<br>
**Codec video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV e praticamente ogni altro codec supportato da FFmpeg.<br>
**Codec audio (dentro il video):** AAC, MP3, FLAC, ALAC, OGG/Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE.<br>
**Sottotitoli:** SRT, VTT (WebVTT), ASS/SSA (renderizzati tramite libass), tracce di immagini e testo incorporate.<br>
**Protocolli di streaming:** HTTP/HTTPS, HLS (m3u8), RTSP (telecamere IP e IPTV).<br>
**Streaming diretto:** SMB/WebDAV/FTP/SFTP/NFS/DLNA.<br>
{{% /details %}}

{{% details title="Evervideo riproduce file MKV su iPhone?" closed="true" %}}
**Sì — Evervideo riproduce file MKV in modo nativo su iPhone, iPad e Mac** senza necessità di conversione, inclusi i container MKV con video H.264, HEVC, VP9 o AV1, tracce audio multiple e sottotitoli SRT/ASS incorporati.<br><br>

Questo è uno dei motivi principali per cui le persone installano Evervideo invece del lettore predefinito di Apple: iOS non apre affatto gli MKV, ma Evervideo li gestisce tramite il motore FFmpeg integrato. Puoi eseguire lo streaming di file MKV direttamente dall'archiviazione cloud o da un NAS senza scaricarli.
{{% /details %}}

{{% details title="Evervideo supporta video 4K e HDR?" closed="true" %}}
**Sì — Evervideo riproduce video 4K (Ultra HD) e contenuti con codifica HDR** su ogni dispositivo dotato dell'hardware per decodificarli. I moderni iPhone, iPad e Mac Apple Silicon decodificano tutti 4K H.264 e 4K HEVC in hardware, quindi la riproduzione è fluida e rispettosa della batteria.<br><br>

Per i migliori risultati sul 4K in streaming dal cloud, aumenta il **Tempo di precaricamento** in **Impostazioni → Lettore → Caricamento file** in modo che il buffer possa stare al passo con i file ad alto bitrate, e connettiti a una rete Wi-Fi invece che alla rete cellulare.
{{% /details %}}

{{% details title="Evervideo supporta la decodifica hardware H.264 e HEVC?" closed="true" %}}
**Sì — Evervideo utilizza decoder hardware H.264 (AVC) e H.265 (HEVC) per impostazione predefinita** su ogni iPhone, iPad e Mac che li supporta, il che significa riproduzione più fluida, minore consumo della batteria e temperatura del dispositivo più bassa rispetto alla decodifica software pura.<br><br>

Puoi attivare o disattivare la decodifica hardware in modo indipendente per H.264 e HEVC in **Impostazioni → Lettore → Video → Decodifica hardware H.264/H.265**. Se un file specifico ha problemi di compatibilità (flussi corrotti, profili esotici), disabilita la decodifica hardware per quel file per tornare alla decodifica software FFmpeg.
{{% /details %}}

{{% details title="Evervideo supporta Picture-in-Picture (PiP)?" closed="true" %}}
**Sì — Evervideo supporta completamente Picture-in-Picture su iPhone e iPad.** Quando tocchi l'icona PiP sul lettore, il video continua a essere riprodotto in una finestra mobile sopra ogni altra app.<br><br>

Trascina la finestra mobile in qualsiasi angolo, pizzicala per ridimensionarla, tocca una volta per visualizzare i controlli base di play/pausa/salta e tocca il piccolo pulsante di espansione per tornare a Evervideo. PiP funziona con **ogni formato video riprodotto da Evervideo**, inclusi i file in streaming dal cloud e i flussi RTSP di telecamere IP, e continua a funzionare anche quando il telefono è bloccato.
{{% /details %}}

{{% details title="Evervideo ha un'interfaccia lettore in stile YouTube per i miei video locali?" closed="true" %}}
**Sì — il layout predefinito di Evervideo è costruito attorno a un'esperienza in stile YouTube per i tuoi video: un lettore video compatto permanentemente visibile nella parte superiore dello schermo mentre sfogli la tua libreria in basso.**<br><br>

Il **lettore compatto** rimane visibile in ogni scheda — Recenti, Preferiti, Libreria multimediale, Playlist, File e Impostazioni — in modo da poter sfogliare, cercare, organizzare e accodare il video successivo senza mai interrompere la riproduzione. Tocca il lettore compatto per espanderlo nella vista a schermo intero; scorri verso il basso per ridurlo nuovamente a compatto senza fermare il video. Su macOS, il lettore compatto può essere staccato in una **finestra mobile always-on-top** separata per un vero multitasking in stile picture-in-picture sul desktop.<br><br>

A differenza di YouTube, non ci sono pubblicità, raccomandazioni algoritmiche, prompt di riproduzione automatica né tracciamento — mantieni il pieno controllo sulla tua libreria video personale da iCloud, Google Drive, Dropbox, il tuo NAS, Plex/Jellyfin/Emby o qualsiasi altra fonte.
{{% /details %}}

{{% details title="Evervideo riproduce video a 360° da Insta360 e altre fotocamere 360?" closed="true" %}}
**Sì — Evervideo riproduce direttamente video 360°/VR (sferici), senza pre-elaborazione o conversione necessaria**, inclusi i filmati di Insta360 (One X, X3, X4, ONE RS, GO 3), GoPro Max, Ricoh Theta, Samsung Gear 360, Vuze e qualsiasi altra sorgente equirettangolare 360°.<br><br>

Basta inserire il video 360° in iCloud Drive, Google Drive, Dropbox, il tuo NAS, o riprodurlo dalla libreria Foto di iOS — Evervideo riconosce il formato sferico e passa automaticamente al rendering del viewport VR. Da lì puoi:<br>

- **Ruotare il dispositivo** — inclina e gira fisicamente iPhone o iPad e il viewport video ruota in tempo reale per guardare intorno alla scena.<br>
- **Trascinare con il dito** per spostarti in qualsiasi direzione senza muovere il dispositivo.<br>
- **Pizzicare per zoomare** avanti e indietro nella vista sferica.<br>
- Cambiare modalità di proiezione/visualizzazione nel menu Altre azioni del lettore e usare un visore VR per un'esperienza completamente immersiva.<br><br>

Ciò significa che il tuo filmato Insta360 funziona immediatamente su iPhone e iPad — nessuna app extra, nessuna transcodifica, nessun abbonamento cloud richiesto.
{{% /details %}}

{{% details title="Come si usa l'equalizzatore video e i preset?" closed="true" %}}
**Apri il lettore, tocca Altre azioni → Equalizzatore video, poi trascina i cursori per luminosità, contrasto, saturazione e tonalità — oppure scegli un preset.**<br><br>

L'**equalizzatore video** di Evervideo è uno strumento di regolazione dell'immagine in tempo reale che funziona all'interno della pipeline di rendering FFmpeg:<br>

- **Luminosità** — aumenta una scena scura ripresa in scarsa illuminazione, o riduci un'esposizione sovraesposta.<br>
- **Contrasto** — aggiungi incisività a contenuti sbiaditi o ammorbidisci una sorgente troppo contrastata.<br>
- **Saturazione** — scalda i colori attenuati o desatura per un look cinematografico.<br>
- **Tonalità** — sposta l'equilibrio dei colori per correggere una dominante verde o magenta.<br><br>

Puoi salvare le tue impostazioni preferite come **preset personalizzato** e riapplicarlo con un tocco su qualsiasi video futuro. I preset possono anche essere **esportati e importati** per condividerli tra iPhone, iPad e Mac, o per eseguirne il backup. Combina l'equalizzatore video con l'**equalizzatore audio** (EQ a 10 bande con la propria libreria di preset) per il controllo completo di immagine e suono.
{{% /details %}}

{{% details title="Come si ruota o cambia la modalità di scala di un video?" closed="true" %}}
**Tocca Altre azioni sul lettore e scegli Rotazione (0°/90°/180°/270°) o Modalità di scala (Adatta/Riempi/Allunga/Originale).**<br><br>

La **Rotazione** è utile per i video registrati di lato o capovolti — ruota l'immagine senza uscire dal lettore. La **Modalità di scala** controlla come l'immagine riempie lo schermo:<br>

- **Adatta** — mantieni il rapporto d'aspetto originale con barre nere dove necessario.<br>
- **Riempi** — riempi l'intero schermo, ritagliando il video se necessario.<br>
- **Allunga** — allunga per riempire lo schermo, distorcendo l'immagine.<br>
- **Originale** — mantieni la risoluzione nativa a 1:1.
{{% /details %}}

{{% details title="Come si sceglie una diversa traccia audio (doppiaggio, commento) in un video?" closed="true" %}}
**Tocca il pulsante Altre azioni ("...") sul lettore e scegli Traccia audio — poi seleziona la traccia desiderata dall'elenco.**<br><br>

Per i video con più tracce audio (doppiaggi in lingue alternative, commento del regista, mix originali/live), Evervideo mostra ogni traccia incorporata con la sua lingua e il codec. Funziona per MKV, MP4, M2TS e qualsiasi altro container che espone più flussi audio.
{{% /details %}}

{{% details title="Come si aggiungono o cambiano i sottotitoli in Evervideo?" closed="true" %}}
**Tocca il pulsante Altre azioni ("...") sul lettore e scegli Sottotitoli — poi seleziona una traccia di sottotitoli incorporata, carica un file di sottotitoli esterno o cambia il font.**<br><br>

Evervideo elenca automaticamente ogni traccia di sottotitoli incorporata in un video. Per caricare un file di sottotitoli esterno, scegli **File esterno** e seleziona un file `.srt`, `.vtt`, `.ass` o `.ssa` dal tuo dispositivo, da iCloud Drive o da qualsiasi servizio cloud connesso. Puoi anche configurare il comportamento predefinito dei sottotitoli in **Impostazioni → Lettore → Sottotitoli**.
{{% /details %}}

{{% details title="Evervideo supporta file di sottotitoli SRT, VTT e ASS esterni?" closed="true" %}}
**Sì — Evervideo carica file di sottotitoli esterni in formato SRT, VTT (WebVTT), ASS e SSA** da qualsiasi posizione sul dispositivo o su qualsiasi servizio cloud connesso.<br><br>

I file ASS/SSA con stili avanzati (font personalizzati, colori, posizioni, effetti karaoke) vengono renderizzati correttamente grazie alla libreria **libass** integrata — perfetta per anime con fansub, file di didascalie professionali e presentazioni. Puoi anche assegnare un font specifico ai sottotitoli in **Impostazioni → Lettore → Sottotitoli → Font**.
{{% /details %}}

{{% details title="Come si elimina un video da Evervideo senza eliminarlo dall'archiviazione cloud?" closed="true" %}}
**Su qualsiasi video, tocca "..." → Elimina dalla libreria multimediale — questo rimuove la voce dal database della libreria ma lascia il file originale intatto nell'archiviazione cloud, nel NAS o nella libreria Foto di iOS.**<br><br>

Se vuoi rimuovere anche il file dalla sua sorgente, scegli invece **Elimina dal servizio cloud** o **Elimina dai file locali**. Queste azioni distruttive non possono essere annullate, quindi fai attenzione quando hai più video selezionati.<br><br>

Per rimuovere una copia scaricata senza toccare nulla nel cloud, apri la scheda **File**, trova il video in **File in questa applicazione** o **Cartelle offline**, e usa **"..." → Elimina**. L'originale nel cloud rimane esattamente dov'era — Evervideo rimuove solo la copia locale.
{{% /details %}}

{{% details title="Come si cambia la velocità di riproduzione in Evervideo?" closed="true" %}}
**Apri il lettore, tocca il controllo Velocità sulla barra degli strumenti e trascina il cursore — sono supportate velocità da 0,25× a 3,00×.**<br><br>

Puoi rallentare i contenuti per un'analisi fotogramma per fotogramma (0,25×/0,5×) o accelerarli per tutorial e lezioni (1,25×/1,5×/2×). Tocca l'icona di configurazione nell'angolo in alto a destra della schermata Velocità per passare alla modalità precisa per regolazioni più fini. La correzione del tono per traccia mantiene l'audio che suona naturale a velocità diverse da 1×.
{{% /details %}}

{{% details title="Come si imposta un timer di sonno in Evervideo?" closed="true" %}}
**Apri Impostazioni → Lettore → Timer di sonno, attivalo e scegli per quanto tempo vuoi che la riproduzione continui prima di fermarsi automaticamente.**<br><br>

Puoi anche aggiungere il pulsante **Timer di sonno** direttamente alla schermata principale del lettore tramite **Impostazioni → Lettore → Personalizzazione → Azioni schermata principale**. Tocca l'icona di configurazione per la modalità precisa con granularità minuto per minuto — utile per addormentarsi guardando uno show.
{{% /details %}}

{{% details title="Come si aggiunge un segnalibro a una posizione specifica in un video?" closed="true" %}}
**Apri il lettore e tocca Aggiungi segnalibro dal menu Altre azioni per salvare la posizione di riproduzione corrente — i segnalibri appaiono in Altre azioni → Segnalibri.**<br><br>

I segnalibri sono memorizzati per video e persistono tra le sessioni, rendendoli perfetti per video lunghi, lezioni, audiolibri in video, serie di tutorial e registrazioni di concerti dove vuoi tornare a momenti specifici.
{{% /details %}}

{{% details title="Come si riprende una playlist dal punto in cui si era rimasti?" closed="true" %}}
Prima, assicurarsi che "Salva stato lettore multimediale" sia abilitato in Impostazioni > Lettore multimediale > Generale. Quando si passa a un'altra playlist e si ritorna, si vedranno quattro azioni nella barra degli strumenti superiore sotto l'artwork dell'album: "Cerca," "Riprendi riproduzione," "Riproduci tutto," e "Riproduzione casuale." Tocca "Riprendi riproduzione" per riprendere la playlist dall'ultimo stato salvato e dalla posizione multimediale.
{{% /details %}}

{{% details title="Come si trasmette un video da Evervideo su Chromecast o AirPlay?" closed="true" %}}
**Apri il lettore video, tocca l'icona AirPlay o Chromecast e scegli il tuo TV, Apple TV, HomePod o smart speaker dall'elenco.**<br><br>

Sia **AirPlay 2** che **Google Chromecast** sono supportati su iOS. AirPlay 2 consente anche di trasmettere a più dispositivi compatibili contemporaneamente. Alcuni file hi-res o HEVC potrebbero dover essere transcodificati per l'hardware Chromecast.
{{% /details %}}

{{% details title="Evervideo supporta Apple CarPlay?" closed="true" %}}
**No — Evervideo non supporta Apple CarPlay.** Apple CarPlay è limitato alle app solo audio (musica, podcast, audiolibri, navigazione), quindi un lettore video non può essere eseguito su uno schermo CarPlay per le regole di Apple.<br><br>

Se vuoi un'app connessa al cloud che supporti CarPlay, le nostre app musicali **Evermusic** e **Flacbox** funzionano entrambe completamente su CarPlay con schede dedicate per Libreria, Connessioni, File locali e Impostazioni.
{{% /details %}}

{{% details title="Quali servizi cloud supporta Evervideo?" closed="true" %}}
**Evervideo si connette a praticamente ogni provider di archiviazione cloud popolare, server multimediale self-hosted e protocollo di condivisione file — tutto da un'unica schermata Connetti all'archiviazione cloud.**<br><br>

**Archiviazione cloud personale:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).<br>

**Server multimediali self-hosted:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud · Synology Drive · QNAP.<br>

**Protocolli NAS:** SMB · WebDAV · FTP/FTPS · SFTP · NFS · DLNA/UPnP.<br>

**Stream live e telecamere IP:** RTSP.<br>

**Archiviazione oggetti compatibile con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces.<br><br>

Gli utenti Premium possono connettere un numero illimitato di servizi; la versione gratuita è limitata a tre.
{{% /details %}}

{{% details title="Evervideo supporta Plex, Jellyfin, Emby, Subsonic e Navidrome?" closed="true" %}}
**Sì — Evervideo si connette nativamente a Plex Media Server, Jellyfin, Emby, Subsonic e Navidrome**, in modo da poter eseguire lo streaming della tua libreria video self-hosted direttamente senza esporre la condivisione file sottostante.<br><br>

- **Plex Media Server** — tocca **File → Connetti all'archiviazione cloud → Plex**, accedi con il tuo account Plex e scegli un server. I server Plex sulla stessa rete locale vengono anche auto-scoperti nella sezione **Dispositivi disponibili**.<br>
- **Jellyfin** (open-source) — tocca **File → Connetti all'archiviazione cloud → Jellyfin**, inserisci l'URL del tuo server (qualcosa come `http://server-ip:8096`) e le credenziali.<br>
- **Emby** (commerciale) — tocca **File → Connetti all'archiviazione cloud → Emby** e inserisci l'URL del server e il login.<br>
- **Subsonic e server compatibili con Subsonic** — tocca **File → Connetti all'archiviazione cloud → Subsonic**, inserisci l'URL del server e le credenziali. Lo stesso percorso API funziona con **Navidrome**, **Airsonic**, **Funkwhale**, **Gonic**, **Logitech Media Server (LMS)** e **Ampache**.<br><br>

Una volta connesso, ogni server appare accanto ai tuoi account cloud nella scheda File. Puoi sfogliare Film, Serie TV, Video domestici, Musica, Playlist e raccolte; scaricare per la riproduzione offline; accodare elementi nel lettore; e importarli nella tua Libreria multimediale globale — tutto senza uscire da Evervideo.
{{% /details %}}

{{% details title="Evervideo si connette tramite SMB, WebDAV, FTP/SFTP, NFS e DLNA?" closed="true" %}}
**Sì — Evervideo supporta ogni principale protocollo NAS e di condivisione file: SMB (SMB1, SMB2, Auto), WebDAV (HTTP/HTTPS), FTP/FTPS, SFTP (autenticazione con password o chiave pubblica), NFS e DLNA/UPnP.**<br><br>

Questo ti permette di connetterti a quasi qualsiasi dispositivo NAS (Synology, QNAP, WD My Cloud Home, Buffalo, Apple Time Capsule), una condivisione file Linux/macOS/Windows, un server Nextcloud/ownCloud self-hosted o qualsiasi server multimediale UPnP/DLNA, tutto dal menu **File → Connetti all'archiviazione cloud**.
{{% /details %}}

{{% details title="Evervideo supporta l'archiviazione oggetti compatibile con S3?" closed="true" %}}
**Sì — Evervideo include un connettore compatibile con S3** che funziona con **AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces** e qualsiasi altro servizio che espone un endpoint API S3.<br><br>

Tocca **File → Connetti all'archiviazione cloud → Archiviazione S3**, poi inserisci l'URL dell'endpoint, la regione, la chiave di accesso, la chiave segreta e il nome del bucket. Una volta connesso, il bucket si comporta come qualsiasi altro cloud — sfoglia, esegui lo streaming, scarica, accoda e aggiungi alla tua libreria.
{{% /details %}}

{{% details title="Posso riprodurre stream RTSP (telecamere IP, IPTV) in Evervideo?" closed="true" %}}
**Sì — Evervideo ha il supporto RTSP nativo**, quindi puoi puntarlo a qualsiasi URL `rtsp://` — telecamere di sicurezza, telecamere per citofoni, baby monitor, provider IPTV, feed di trasmissione — ed Evervideo estrarrà e decodificherà il flusso live.<br><br>

Tocca **File → Link online → Aggiungi link**, incolla l'URL completo (`rtsp://camera-ip:port/stream-path`), fornisci login e password se richiesto, e tocca **Fatto**. Gli stream RTSP funzionano in Picture-in-Picture, nel lettore compatto, e trasmettono tramite AirPlay 2 e Chromecast proprio come un normale video.
{{% /details %}}

{{% details title="Come si trasferiscono video su Evervideo dal computer?" closed="true" %}}
Puoi connettere il tuo computer o NAS personale usando i protocolli SMB, WebDAV o DLNA. In alternativa, usa iTunes File Sharing per trasferire file multimediali.<br><br>

Per connettere un computer usando il protocollo SMB tocca "File" "Connetti all'archiviazione cloud" → SMB. Inserisci l'indirizzo IP del computer e il nome della cartella condivisa nel campo URL usando il formato smb://computer-ip-address/shared-folder-name, inserisci login e password e tocca "Fatto". Se la connessione ha avuto successo vedrai l'archiviazione connessa nella sezione "Archiviazione cloud".<br><br>

Un tutorial completo è disponibile qui:<br>
[Trasferisci i tuoi file dal computer a iPhone usando il protocollo SMB](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/)<br><br>

Per il protocollo WebDAV, tutti i passaggi sono gli stessi tranne per il campo URL. L'URL deve essere nel formato http://server-name o https://server-name se il server supporta SSL.<br><br>

Un tutorial completo è disponibile qui:<br>
[Come connettere l'archiviazione NAS usando WebDAV e ascoltare musica su iPhone o Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)<br><br>

Wi-Fi Drive è una tecnologia popolare che consente di trasferire file dal computer a un dispositivo iOS senza fili usando un browser desktop. Per usare questa funzione il dispositivo e il computer devono essere connessi alla stessa rete Wi-Fi. Apri "File" → "Computer" → "Connetti tramite Wi-Fi" e abilita il server. Dopodiché apri un browser desktop e inserisci l'URL dall'applicazione. Puoi trascinare i file dal computer sulla pagina web aperta e appariranno sul dispositivo.<br>
Tutorial più dettagliato disponibile qui:<br>
[Come trasferire file in modalità wireless da un computer a iPhone usando WiFi-Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)<br><br>

iTunes File Sharing è un'altra tecnologia che consente di trasferire file dal computer al dispositivo usando iTunes e il cavo lightning. Basta connettere il dispositivo al computer usando un cavo ed eseguire iTunes. Apri iTunes → "Sezione Applicazioni" → e trova Evervideo. Tocca l'icona dell'app per vedere la cartella condivisa. Copia i file dal computer alla cartella condivisa sul dispositivo.<br><br>

Istruzioni dettagliate disponibili qui:<br>
[Come riprodurre file locali (file iTunes) sul mio iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone)<br><br>

{{% /details %}}

{{% details title="Come si usa la funzione Wi-Fi Drive in Evervideo?" closed="true" %}}

**Trasferimento wireless tramite browser desktop**<br>
1. Avvia l'app: Apri Evervideo.<br>
2. Connetti tramite Wi-Fi: Vai a File → "Computer" → "Connetti tramite Wi-Fi".<br>
3. (Opzionale) Aggiungi sicurezza: Inserisci nome utente e password se necessario.<br>
4. Avvia Wi-Fi Drive: Tocca "Avvia Wi-Fi Drive" e copia l'URL fornito.<br>
5. Apri un browser (Safari, Chrome, Opera, Firefox, ecc.) e inserisci l'URL.<br>
6. Usa il file manager integrato per caricare, scaricare, rinominare o eliminare file. Puoi trascinare i file direttamente sul tuo iPhone.<br>
7. Quando hai finito, tocca "Ferma Wi-Fi Drive" sul tuo iPhone.<br><br>

Nota: Assicurati che JavaScript sia abilitato e stai usando la versione più recente del browser per le migliori prestazioni.<br><br>

**Trasferire file usando Mac Finder**<br>
1. Nel Finder, clicca "Vai" → "Connetti al server…".<br>
2. Inserisci l'URL del server mostrato nell'app Evervideo.<br>
3. Clicca "Connetti" e gestisci i file sul tuo iPhone come qualsiasi unità di rete.<br><br>

**Trasferire file usando Windows File Explorer**<br>
1. Fai clic destro su "Questo PC" → "Connetti unità di rete…".<br>
2. Inserisci l'URL del server dall'app Evervideo nel campo "Cartella".<br>
3. Scegli una lettera di unità, clicca "Fine" e sfoglia i file del tuo iPhone direttamente.<br><br>

[Leggi di più](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive)

{{% /details %}}

{{% details title="Come si usa un'unità flash USB o una scheda SD con Evervideo su iPhone?" closed="true" %}}
**Inserisci l'unità nel tuo iPhone, iPad o Mac tramite Lightning-a-USB, USB-C o un lettore di schede, poi in Evervideo apri File → File su questo iPhone → Apri cartella, naviga fino all'unità e scegli il video.**<br><br>

Evervideo riproduce i file direttamente dall'unità senza copiarli nell'archiviazione interna — perfetto per librerie 4K o HDR molto grandi. Funziona con lettori di schede certificati Apple.
{{% /details %}}

{{% details title="Come si importano video dalla libreria Foto di iOS?" closed="true" %}}
**Apri la scheda Libreria multimediale → Libreria Foto per sfogliare ogni video nell'app Foto di iOS, organizzato per Tutti i video, Brevi, Medi, Lunghi, Registrazioni schermo e Album foto.**<br><br>

Non devi copiare nulla da Foto — Evervideo li riproduce sul posto, con supporto completo dei sottotitoli, Picture-in-Picture, equalizzatore e Chromecast/AirPlay. Registrazioni della fotocamera, clip ricevuti via AirDrop, album condivisi iCloud e Album intelligenti sono tutti inclusi.
{{% /details %}}

{{% details title="Come si cerca un video, album o genere in Evervideo?" closed="true" %}}
**Tocca l'icona della lente d'ingrandimento in qualsiasi elenco — Libreria multimediale, Playlist, Album, Generi, Recenti, Preferiti, o all'interno di una cartella — e digita un nome per filtrare istantaneamente i risultati.**<br><br>

La ricerca è locale e viene eseguita sul database della libreria video, quindi i risultati appaiono mentre digiti anche su reti lente. Puoi anche cercare all'interno di una playlist, album o cartella specifica per trovare un singolo video tra centinaia. Titoli, album, generi, cartelle e playlist sono tutti ricercabili.
{{% /details %}}

{{% details title="Come si visualizzano i video visti di recente con il progresso di riproduzione?" closed="true" %}}
**Apri la scheda Recenti (Evervideo si apre qui per impostazione predefinita) per vedere ogni video che hai guardato di recente, ciascuno con una miniatura e una barra di progresso di visione per file in modo da poter riprendere uno qualsiasi con un tocco.**<br><br>

Evervideo traccia la posizione di riproduzione di ogni video che guardi, quindi anche i video che non hai esplicitamente aggiunto ai segnalibri possono essere ripresi esattamente dove ti eri fermato. Cambia quante voci mantiene l'elenco Recenti tramite **Impostazioni → Libreria multimediale → Recenti → Cambia dimensione elenco**. Puoi anche esportare l'elenco in M3U, CSV o TXT per eseguire il backup della cronologia di visione, oppure cancellarlo con **Elimina elenco** per ripartire da zero.
{{% /details %}}

{{% details title="Come si aggiunge un video ai preferiti in Evervideo?" closed="true" %}}
**Tocca "..." su qualsiasi video e scegli Aggiungi ai preferiti — i preferiti appaiono in Libreria multimediale → Preferiti e, opzionalmente, in File → Preferiti.**<br><br>

Abilita la **Modifica simultanea** in **Impostazioni → Libreria multimediale → Preferiti** per rispecchiare i preferiti tra la sezione libreria multimediale e la sezione file. Puoi anche esportare l'elenco dei preferiti in M3U, CSV o TXT per il backup, e raggiungere i preferiti dalla scheda **Preferiti** dedicata nella barra delle schede inferiore.
{{% /details %}}

{{% details title="Come si crea una playlist su Evervideo?" closed="true" %}}
- Apri la sezione Playlist.<br>
- Tocca il pulsante "+" o il pulsante "..." nell'angolo in alto a destra e seleziona "Nuova playlist."<br>
- Inserisci un nome per la playlist e tocca "Salva". Apparirà la finestra di dialogo "Aggiungi file multimediali".<br>
- Seleziona le tracce che vuoi aggiungere alla playlist.<br><br>

{{% /details %}}

{{% details title="Come si importa una playlist M3U, M3U8 o CUE in Evervideo?" closed="true" %}}
**Apri la scheda Playlist, tocca il menu "...", seleziona Importa playlist, poi scegli il file .m3u, .m3u8 o .cue dall'archiviazione cloud o dal dispositivo.**<br><br>

Evervideo analizza il file della playlist, individua ogni video referenziato nella tua archiviazione e crea una vera playlist nella tua libreria. Assicurati che i percorsi all'interno del file della playlist corrispondano a dove si trovano effettivamente i file video.
{{% /details %}}

{{% details title="Come si riproducono video scaricati localmente su iPhone?" closed="true" %}}
Una volta installata l'applicazione, apri la schermata "File" e scorri verso il basso fino alla sezione "File su questo iPhone". Da lì, scegli "Apri file..." se devi selezionare più file o "Apri cartella..." se vuoi scegliere una cartella multimediale. L'app eseguirà la scansione del contenuto della cartella e tutti i file multimediali trovati verranno selezionati. Naviga fino alla tua cartella multimediale, tocca "Apri" per confermare la selezione e i file verranno aggiunti alla coda del lettore. Questi file verranno riprodotti direttamente dalla posizione selezionata senza essere copiati nel bundle dell'applicazione.<br><br>

**Aggiunta di una cartella ai preferiti per un accesso rapido**<br>
Semplifica il processo aggiungendo una cartella situata sul tuo dispositivo ai preferiti. In questo modo non dovrai ripetere i passaggi ogni volta che vuoi riprodurre musica. Apri la schermata "File", scorri fino alla sezione "Accesso rapido" e tocca "Preferiti" per accedere alla schermata "File preferiti". Tocca il pulsante altre azioni (tre punti) nell'angolo in alto a destra e seleziona "Aggiungi cartella." Naviga fino alla cartella desiderata e tocca "Apri" per confermare. La tua cartella verrà aggiunta a "File preferiti", fornendo un accesso rapido ai tuoi file multimediali.<br><br>

**Importazione di file locali nella libreria**<br>
Se preferisci organizzare i tuoi file locali all'interno della tua libreria, apri la schermata "Libreria", tocca il pulsante a tre punti nell'angolo in alto a destra e seleziona "+ Aggiungi file multimediali". Scegli la voce di menu "File su questo dispositivo" e tocca "Apri file...". Seleziona i file che vuoi aggiungere e tocca "Apri" per confermare. L'app eseguirà la scansione dei file selezionati e li aggiungerà alla tua libreria, organizzandoli per metadati.<br><br>

**Aggiunta di file locali a una playlist**<br>
Per aggiungere file locali a una playlist, apri la schermata "Playlist" e tocca il pulsante altro nell'angolo in alto a destra. Seleziona "+ Nuova playlist," inserisci un nome per la tua nuova playlist, e nella schermata successiva, seleziona l'opzione "File su questo dispositivo" e tocca "Apri file...". Seleziona i file multimediali che vuoi aggiungere e tocca "Apri" per confermare. I file verranno aggiunti alla tua playlist, dove puoi cambiare l'ordine delle tracce ed eseguire altre azioni usando il pulsante altro.<br><br>

{{% /details %}}

{{% details title="Come si abilita la modalità offline in Evervideo?" closed="true" %}}
- Connetti all'archiviazione cloud:<br>
 • Vai alla scheda "File".<br>
 • Seleziona "Connetti all'archiviazione cloud" e segui le istruzioni per connettere il servizio desiderato.<br><br>

- Naviga alla cartella dei file multimediali:<br>
 • Apri il servizio di archiviazione cloud connesso e trova la tua cartella multimediale.<br><br>

- Abilita la modalità offline:<br>
 • Tocca il pulsante "Altre azioni" accanto al nome della cartella.<br>
 • Scegli "Abilitare la modalità offline."<br><br>

- Scarica il contenuto:<br>
 • La cartella selezionata e tutto il suo contenuto verrà scaricato in "File" > "Cartelle offline."<br><br>

- Aggiornamenti automatici:<br>
 • L'app eseguirà continuamente la scansione delle modifiche. I nuovi file aggiunti alla cartella online verranno scaricati automaticamente.<br><br>

- Configura il timeout di scansione:<br>
 • Vai a "Impostazioni" > "Gestione file" > "Cartelle offline" > "Intervallo di tempo" per impostare la frequenza di scansione.<br><br>

- Sincronizzazione manuale:<br>
 • Per sincronizzare manualmente, vai a "Impostazioni" > "Gestione file" > "Cartelle offline" > "Cartelle offline sincronizzate."<br>
 • Tocca "Altre azioni" e seleziona "Avvia sincronizzazione."<br><br>

{{% /details %}}

{{% details title="Come si scarica un video?" closed="true" %}}
Prima di poter scaricare video e guardarli offline devi connettere un'archiviazione cloud.<br>
Basta aprire la schermata "File" e connettere la tua archiviazione cloud.<br>
Una volta aggiunta puoi scaricare il tuo video dal cloud.<br><br>

**Per scaricare video dal cloud**<br>
– Apri l'archiviazione cloud connessa.<br>
– Naviga all'interno della cartella che vuoi scaricare.<br>
– Tocca il pulsante altre azioni "..." nell'angolo in alto a destra e scegli la voce di menu "Seleziona".<br>
– Seleziona i file che vuoi scaricare e tocca il pulsante "Scarica".<br><br>

**Per abilitare la modalità offline per Artista/Playlist/Album**<br>
– Apri la schermata Artisti/Album/Playlist<br>
– Tocca la casella "Modalità offline"<br>
– L'artista/album/playlist offline apparirà nella sezione "File" -> "Cartelle offline".<br><br>

Un'altra opzione è scaricare video da YouTube e importarli in Evervideo, come descritto qui:<br>
[Come scaricare musica da YouTube e ascoltare musica offline su iPhone](/docs/howto/how-to-download-music-from-youtube-and-listen-to-offline-music-on-iphone/)<br><br>

{{% /details %}}

{{% details title="Posso usare Evervideo senza connessione internet?" closed="true" %}}
**Sì — una volta scaricati i video o abilitata la modalità offline per una cartella, Evervideo riproduce tutto completamente offline.**<br><br>

Il contenuto offline si trova in **File → File in questa applicazione** e continua a funzionare in modalità aereo, durante i voli e ovunque senza Wi-Fi o dati mobili. I video solo cloud (quelli che non hai scaricato) appariranno in grigio finché non recuperi una connessione. Per i viaggi, abilita la **Modalità offline** per le cartelle rilevanti o scarica video specifici prima di partire.
{{% /details %}}

{{% details title="Come si abilita la modalità scura in Evervideo?" closed="true" %}}
**Apri Impostazioni → Personalizzazione → Schema colori, poi scegli Scuro, Chiaro o Predefinito (che segue l'aspetto del sistema).**<br><br>

Puoi anche scegliere icone alternative per l'app in **Impostazioni → Personalizzazione → Icona applicazione** (Premium) e scegliere un poster sfocato come sfondo dell'app in **Stile sfondo**.
{{% /details %}}

{{% details title="Come si cambia la lingua dell'interfaccia di Evervideo?" closed="true" %}}
**Apri Impostazioni → Lingua, scegli tra oltre 120 lingue supportate, poi riavvia l'app perché la modifica abbia effetto.**<br><br>

L'app supporta localizzazioni incluse inglese, francese, tedesco, spagnolo, italiano, portoghese, russo, ucraino, polacco, olandese, arabo, ebraico, hindi, giapponese, coreano, cinese (semplificato e tradizionale), vietnamita, turco e molti altri. Scegli **Predefinito** per seguire automaticamente l'impostazione della lingua del dispositivo.
{{% /details %}}

{{% details title="Come si protegge Evervideo con un codice di accesso?" closed="true" %}}
**Apri Impostazioni → Codice di accesso, tocca Abilita e scegli un codice a 4 cifre — ti verrà chiesto di inserirlo ogni volta che l'app viene avviata.**<br><br>

Evervideo usa un codice numerico fisso a 4 cifre. Il codice impedisce a chiunque abbia accesso al tuo dispositivo di aprire Evervideo e sfogliare i tuoi account cloud connessi, i video scaricati e la libreria. Combinalo con iOS Face ID/Touch ID sul dispositivo per una protezione extra.
{{% /details %}}

{{% details title="Come si abilitano i widget di Evervideo sulla schermata Home o sulla schermata di blocco di iPhone?" closed="true" %}}
**Abilita gli aggiornamenti dei widget in Impostazioni → Widget, poi tieni premuto la schermata Home o la schermata di blocco, tocca "+", cerca "Evervideo" e scegli una dimensione del widget.**<br><br>

Il widget mostra il video in riproduzione con titolo, poster e controlli di base. Poiché gli aggiornamenti dei widget usano una piccola quantità di energia, l'interruttore **Abilita widget** è disattivato per impostazione predefinita — attivalo solo se usi attivamente i widget. I widget funzionano sulla schermata Home e sulla schermata di blocco di iPhone e iPad, e nel Centro notifiche di macOS.
{{% /details %}}

{{% details title="Come si condivide Evervideo Premium con la propria famiglia?" closed="true" %}}
**Tutti i piani Evervideo Premium: a vita, mensile e annuale funzionano con Apple Family Sharing, quindi chiunque nel tuo gruppo familiare può installare Evervideo e usare Premium senza costi aggiuntivi.**<br><br>

Configura Family Sharing in iOS/macOS **Impostazioni → Famiglia**, poi fai in modo che ogni membro della famiglia installi Evervideo dall'App Store e lo esegua una volta mentre è connesso con il proprio Apple ID. Premium viene riconosciuto automaticamente entro un minuto. Lo stesso piano è condiviso tra iPhone, iPad e Mac per ogni membro della famiglia.
{{% /details %}}

{{% details title="Come si annulla l'abbonamento a Evervideo Premium?" closed="true" %}}
**Apri iOS o macOS Impostazioni → [il tuo nome] → Abbonamenti, trova Evervideo e tocca Annulla abbonamento — le funzionalità Premium rimangono attive fino alla fine del periodo di fatturazione corrente.**<br><br>

Gli acquisti in-app a vita non sono abbonamenti e non devono essere annullati. Per i rimborsi, usa la pagina **Segnala un problema** di Apple (`reportaproblem.apple.com`) — i rimborsi vengono emessi da Apple, non da Everappz.
{{% /details %}}

{{% details title="Come si esegue il backup e il ripristino della libreria di Evervideo?" closed="true" %}}
**Apri Impostazioni → Backup e ripristino, seleziona cosa includere (Database, Copertine album, Impostazioni), tocca "Backup dati applicazione" e salva il file di backup — aprilo su un altro dispositivo per ripristinare.**<br><br>

Il backup contiene le voci della libreria multimediale, le playlist, i preferiti, il progresso di visione, le impostazioni e la cache dei poster. **Non** include i file video scaricati offline (che renderebbero il backup enorme). Sposta il file di backup sul nuovo dispositivo tramite iCloud Drive, AirDrop o qualsiasi servizio cloud connesso, poi aprilo in Evervideo per applicarlo.
{{% /details %}}

{{% details title="Come si libera spazio di archiviazione usato da Evervideo?" closed="true" %}}
**Apri Impostazioni → Gestione file → Elimina file temporanei e Impostazioni → Libreria multimediale → Copertine album → Elimina tutto per svuotare le cache; usa la scheda File per eliminare i video scaricati che non ti servono più.**<br><br>

Puoi anche rimuovere le singole cartelle offline in **Impostazioni → Gestione file → Cartelle offline sincronizzate → "..." → Disabilita modalità offline**, che elimina le copie locali. I video solo in streaming non usano affatto l'archiviazione del dispositivo. Svuotare la cartella **Cache lettore** in **File → File in questa applicazione** può anche liberare diversi gigabyte dopo una riproduzione intensa di contenuti 4K ad alto bitrate.
{{% /details %}}

{{% details title="Perché il mio video cloud va in buffering o si blocca?" closed="true" %}}
**Il buffering è quasi sempre causato da rete lenta, file di grandi dimensioni o impostazioni basse del buffer del lettore — aumenta il Tempo di precaricamento e passa a una rete più veloce o scarica il file.**<br><br>

Alcuni consigli pratici:<br>

- **Aumenta il buffer** in **Impostazioni → Lettore → Caricamento file → Tempo di precaricamento** per contenuti 4K o HEVC ad alto bitrate.<br>
- **Passa al Wi-Fi** se sei su rete mobile, o avvicinati al router.<br>
- **Abilita la decodifica hardware** per H.264 e HEVC in **Impostazioni → Lettore → Video** in modo che la CPU non sia il collo di bottiglia.<br>
- **Scarica il file per la riproduzione offline** se la sorgente è più lenta della tua velocità di visione — i file 4K grandi possono facilmente superare la larghezza di banda mobile.<br>
- **Ri-autorizza il tuo account cloud** nella scheda File se una connessione è scaduta.
{{% /details %}}

{{% details title="Come si contatta il supporto di Evervideo?" closed="true" %}}
**Apri Impostazioni → Invia feedback per inviare un'e-mail al nostro team di supporto direttamente dall'app, con le informazioni diagnostiche allegate automaticamente.**<br><br>

Puoi anche visitare il [Centro assistenza](/docs/), sfogliare le [Guide pratiche](/docs/howto/), o consultare le [FAQ](/docs/faq/) più ampie per risposte in autonomia. Di solito rispondiamo entro un giorno lavorativo.
{{% /details %}}

</div>
