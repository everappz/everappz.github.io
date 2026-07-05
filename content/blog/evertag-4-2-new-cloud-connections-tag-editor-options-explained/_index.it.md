---
title: "Evertag 4.2: nuove connessioni cloud, opzioni dell'editor di tag spiegate"
date: 2026-05-09
description: "Evertag 4.2 aggiunge connessioni a Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP e NFS, rinnova Wi-Fi Drive e aggiorna l'interfaccia per Liquid Glass. Questo articolo spiega anche tutte le opzioni dell'editor di tag — incluse ID3v2.4 vs ID3v2.3, scalatura della copertina, tag duplicati, modalità di upload sul cloud e le impostazioni giuste per Spotify e altri servizi di streaming."
keywords: ["Evertag 4.2", "aggiornamento Evertag", "editor tag ID3 iPhone", "ID3v2.4 vs ID3v2.3", "modificare tag FLAC iOS", "modificare tag MP3 iPhone", "modificare copertina album iOS", "editor di tag per Spotify", "editor di tag Plex", "editor di tag Apple Music", "editor di tag cloud Evertag", "editor di tag Internxt", "editor di tag Proton Drive", "editor di tag QNAP", "editor di tag Nextcloud", "editor di tag Amazon S3", "editor di tag SFTP iPhone", "editor di tag FTP audio", "editor di tag NFS iPhone", "Wi-Fi Drive editor di tag", "tag ID3 duplicati", "scalatura copertina", "design Liquid Glass", "editor metadati audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor di tag", "ID3", "ID3v2.4", "ID3v2.3", "Tag FLAC", "Tag MP3", "Copertina album", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Novità"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evertag 4.2](/products/evertag) è un aggiornamento importante per l'editor di tag audio per iPhone, iPad e Mac. Abbiamo schiacciato bug chiave nell'editing dei tag e aggiunto oltre 6 nuove connessioni cloud e server: **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, oltre ai protocolli **FTP**, **SFTP** e **NFS**. Wi-Fi Drive ha un'interfaccia rinnovata, modalità a selezione multipla, una coda di upload più intelligente e trasferimenti più rapidi. Tutta l'app è regolata per il design **Liquid Glass**. Questo articolo entra anche a fondo nelle impostazioni dell'editor di tag — spiegando **ID3v2.4 vs ID3v2.3**, **scalatura della copertina**, **tag duplicati**, **modalità di upload sul cloud**, **eliminazione del file scaricato**, e quali opzioni scegliere se prepari l'audio per **Spotify**, **Apple Music**, **Plex**, **Jellyfin** o qualunque altro servizio di streaming.

---

## Ciao a tutti!

Arriva un grande aggiornamento di Evertag. Abbiamo schiacciato bug chiave nell'editing dei tag e aggiunto **oltre 6 nuove connessioni cloud e server** per gestire i metadati audio in modo più semplice che mai — che la tua libreria viva su un cloud orientato alla privacy, su un NAS auto-ospitato o su un server FTP/SFTP/NFS generico.

[Scarica Evertag 4.2 dall'App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) oppure aggiorna dalla tua versione attuale.

## Supporto cloud e server ampliato

Evertag si collega ora in modo nativo a una gamma più ampia di opzioni cloud e auto-ospitate. Puoi modificare i tag ID3, MP4, FLAC, OGG e APE su file ovunque si trovino.

### Cloud orientato alla privacy: Internxt e Proton Drive

Se ti interessano la cifratura end-to-end e l'archiviazione zero-knowledge, due dei nomi più rispettati nel cloud privacy-first sono ora nativi in Evertag:

- **Internxt** — cloud spagnolo open source, con cifratura post-quantistica e conforme al GDPR. Piano gratuito disponibile.
- **Proton Drive** — archiviazione cifrata end-to-end dei creatori di Proton Mail e Proton VPN, con sede in Svizzera. Piano gratuito disponibile, con piani a pagamento per librerie più grandi.

Ora puoi modificare i metadati direttamente sui file audio archiviati in entrambi i servizi — il file rimane cifrato durante il trasferimento e solo i nuovi tag vengono riscritti.

### Soluzioni auto-ospitate: QNAP, Nextcloud, Amazon S3

Per chi gestisce la propria infrastruttura:

- **QNAP** — connessione API nativa ai NAS QNAP. Modifica i tag sui file del tuo QNAP via Wi-Fi locale o accesso remoto.
- **Nextcloud** — collega qualunque istanza Nextcloud auto-ospitata o gestita.
- **Amazon S3** — punta Evertag a qualunque bucket S3 (o storage S3-compatibile come Backblaze B2, Wasabi, MinIO, Cloudflare R2) e modifica i metadati sul posto.

### Nuovi protocolli di rete: FTP, SFTP, NFS

Evertag 4.2 aggiunge tre protocolli classici per chi ha server personalizzati, homelab o NAS generici:

- **SFTP (SSH File Transfer Protocol)** — la risposta giusta per **modifica remota e sicura dei tag dal proprio server**. SFTP gira su SSH, quindi l'intero trasferimento (autenticazione e dati audio) è cifrato. Se hai un VPS, un server dedicato o un PC Linux a casa con accesso SSH, puoi modificare i tag su file remoti senza esporre nient'altro. Supporta autenticazione con password e con chiave.
- **FTP** — lo standard storico di trasferimento file. Utile per NAS domestici più vecchi che espongono FTP ma non hanno un'API nativa.
- **NFS (Network File System)** — il protocollo di condivisione di fatto su Linux e sulla maggior parte dei NAS. Overhead più basso rispetto a SMB sullo stesso hardware.

> **Suggerimento:** SFTP è il protocollo che vuoi per la modifica remota tramite Internet aperta. FTP e NFS è meglio usarli sulla rete locale — non esporli su Internet a meno di incapsularli in una VPN.

## Aggiornamenti di Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) è la funzione integrata in Evertag per trasferire file audio in modalità wireless tra computer e iPhone o iPad — senza iTunes, senza cavi, senza account cloud. Entrambi i dispositivi devono trovarsi sulla stessa rete Wi-Fi.

In Evertag 4.2, Wi-Fi Drive ottiene:

- **Interfaccia rinnovata e moderna** — più pulita, più leggibile a colpo d'occhio e aggiornata per Liquid Glass.
- **Modalità a selezione multipla** — scegli più file o cartelle e agisci in blocco.
- **Coda di upload più intelligente** — feedback di avanzamento più chiaro e maggiore resilienza ai cali di rete.
- **Velocità e affidabilità complessive migliorate** — trasferimenti più rapidi per librerie grandi.

È il modo più rapido per spostare un lotto di file audio dal computer al telefono, modificarne i tag e rispedirli — senza alcun servizio di terze parti.

## Impostazioni dell'editor di tag: analisi a fondo

È la parte che la maggior parte degli utenti non legge mai — ed è quella che decide se i tuoi tag funzionano ovunque o solo in alcune app. Apri Evertag, poi vai nella sezione **impostazioni dell'editor di tag audio**. Ecco cosa fa ogni opzione e quale scegliere a seconda di ciò che vuoi ottenere.

### Scalatura della copertina

Quando salvi la copertina dell'album dentro un file audio, Evertag può scalare l'immagine prima di incorporarla. Le opzioni sono:

- **Piccola** — minimo impatto sulla dimensione del file, qualità d'immagine più bassa.
- **Media** — scelta bilanciata per la maggior parte degli utenti.
- **Grande** — alta qualità, adatta a player con schermi grandi e CarPlay.
- **Extra grande** — qualità molto alta, aumento sensibile della dimensione del file.
- **Originale (Disattivata)** — incorpora la copertina alla risoluzione originale. **Nessuna scalatura.**

**Perché è importante:**

- **Più qualità = file più grande.** Una copertina 3.000 × 3.000 pixel può aggiungere diversi MB a ogni traccia. Moltiplicato per un intero album, il costo in disco si accumula in fretta.
- **Alcuni player non gestiscono bene immagini incorporate molto grandi.** Dispositivi più vecchi, alcuni sistemi auto e diversi player desktop legacy possono andare in difficoltà oltre i ~1.500 px o non visualizzarle.
- **Per la maggior parte dei flussi cloud e streaming**, **Media** o **Grande** è il punto giusto. Usa **Originale** solo se serve qualità d'archivio o stai preparando file per un player di cui ti fidi.

> L'opzione **Originale** fa parte dell'aggiornamento personalizzazione premium di Evertag. Le dimensioni standard (Piccola/Media/Grande/Extra grande) sono gratuite.

### Opzioni di salvataggio dei tag: ID3v2.4 vs ID3v2.3

È la singola impostazione più importante per la compatibilità. ID3v2 è il formato di metadati usato all'interno dei file MP3. Esistono due versioni molto diffuse, e differiscono in dettagli sottili ma importanti.

#### ID3v2.4

- Più recente, supporta la **codifica testo UTF-8** — gestione corretta di scritture non latine (cinese, russo, giapponese, arabo, ebraico, ecc.).
- Più tipi di frame (volume relativo, preset di equalizzatore, ecc.).
- **Consigliato per i player moderni** che lo supportano.

#### ID3v2.3

- Più vecchio ma **la versione di ID3 più universalmente supportata**.
- Non supporta UTF-8 direttamente (usa UTF-16 per il testo Unicode).
- **Consigliato quando serve la massima compatibilità** con player più vecchi, autoradio e alcune app desktop.

#### Quando attivare ID3v2.4 in Evertag

- Usi **player audio moderni** come Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versioni attuali) o player Android moderni. ✅ **Attiva ID3v2.4.**
- La tua libreria contiene **caratteri non latini** (cinese, coreano, giapponese, russo, arabo, greco, ebraico). ✅ **Attiva ID3v2.4** — UTF-8 li gestisce molto più puliti.

#### Quando disattivare ID3v2.4 in Evertag (usa ID3v2.3)

- Stai preparando file per **un'autoradio o un'unità integrata più vecchia** che non legge i tag v2.4.
- Vedi **testo illeggibile o tag mancanti** in alcune app dopo la modifica — è un segnale chiaro che lì v2.4 non è supportato. Torna a v2.3.
- Stai puntando a **player desktop legacy** o vecchi player portatili (primi iPod, certi MP3 player anni 2000–2010).

> **Regola pratica:** se i tuoi tag sono visualizzati correttamente ovunque con v2.4, lascia attivato. Se anche un solo player importante mostra caratteri sbagliati, vuoti o non riesce a leggere i tag, disattiva v2.4 e risalva.

#### Tag duplicati

Quando attivi **Tag duplicati**, Evertag scrive i campi metadati comuni (titolo, artista, album, ecc.) in **entrambe le sezioni ID3v1 e ID3v2** del file. Migliora la compatibilità con player molto vecchi che leggono solo ID3v1 (il tag originale di 128 byte alla fine del file).

- **La maggior parte degli utenti non ne ha bisogno.** I player moderni leggono prima ID3v2.
- **Attivalo solo se** hai a che fare con hardware vintage o software specifico che ignora ID3v2.

### Aggiornare i file online: come Evertag gestisce le modifiche cloud

Quando modifichi i tag su un file salvato su un cloud collegato (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, ecc.), Evertag deve ricaricare il file modificato. Tu controlli come:

- **Mostra messaggio di conferma** *(predefinito, consigliato)* — Evertag chiede prima di caricare. Ottimo per utenti prudenti e librerie condivise.
- **Aggiorna automaticamente i metadati del file** — carica in silenzio dopo ogni modifica. Ottimo per utenti singoli con connessioni veloci e affidabili che modificano molto.
- **Non aggiornare i metadati del file** — Evertag modifica solo la copia locale. Utile per anteprima delle modifiche senza propagare al cloud.

### Modificare file online: pulizia del file locale

Per modificare un file remoto, Evertag lo scarica prima sul dispositivo. Dopo la modifica, scegli cosa succede a quella copia locale:

- **Elimina sempre il file scaricato** — Evertag rimuove il file temporaneo dopo la modifica. **Consigliato** se hai poco spazio o lavori su file altrui.
- **Non eliminare il file scaricato** — mantiene il file modificato sul dispositivo. Utile per avere sia una copia offline sia una copia cloud aggiornata.

### Pulsanti nella schermata principale

La schermata principale dell'editor di tag di Evertag può mostrare o nascondere pulsanti per singole operazioni. Attiva solo quelli che usi davvero per mantenere l'interfaccia focalizzata:

- **Cerca tag audio automaticamente** — trova metadati mancanti online dall'impronta audio del file.
- **Cerca tag audio manualmente** — cerca per titolo/artista quando la ricerca automatica fallisce.
- **Cerca copertina** — trova e incorpora copertine di alta qualità.
- **Salva copertina** — esporta la copertina incorporata nella libreria foto o nei file.
- **Normalizza codifica** — corregge testo non latino mal codificato da vecchie codifiche (molto utile per tracce in cirillico, cinese e giapponese rippate con software legacy).
- **Elimina tag audio** — rimuove tutti i tag dal file. Utile prima di un re-tagging pulito.

### Mostra tag estesi

Attivalo per visualizzare l'insieme completo dei campi metadati oltre il classico titolo/artista/album/anno — inclusi BPM, direttore, artista originale, mood, copyright, encoder, commenti, testi e altro. Funzione per utenti avanzati; la maggior parte degli utenti casuali non ne ha bisogno.

### Modificare file simultaneamente

Attivata, Evertag ti consente di modificare i metadati su **più file selezionati contemporaneamente** — imposta lo stesso album artist, anno o genere per un intero album in una sola operazione. È il modo più rapido per riordinare una grande libreria disorganizzata.

## Modificare i tag per Spotify, Apple Music e piattaforme di streaming

Una domanda comune: «ho modificato i tag in Evertag, ho caricato i file e il servizio di streaming mostra metadati sbagliati. Cosa succede?».

Risposta breve: **i servizi di streaming non sempre rispettano i tuoi tag locali**. Apple Music e Spotify hanno i propri database interni — quando riconoscono una traccia, sovrascrivono i metadati mostrati con i loro. Ma per i **file caricati**, i tuoi file locali (la funzione «Libreria» di Apple Music, i File locali di Spotify) e i **caricamenti dei distributori sulle piattaforme di streaming**, i tuoi tag contano eccome. Ecco come impostare Evertag per ogni scenario:

### Preparare file per Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music gestisce UTF-8 correttamente.
- **Copertina: Grande** — le app Apple rendono bene le copertine grandi; Originale è eccessiva.
- **Tag duplicati: OFF** — non servono.
- Assicurati che **Album Artist** sia compilato correttamente — Apple Music lo usa per il raggruppamento.

### Preparare file per i File locali di Spotify

I File locali di Spotify mostrano solo file ben taggati. I tag che Spotify legge sono limitati.

- **ID3v2.4: ON** nella maggior parte dei casi. Se una traccia non appare correttamente in Spotify dopo la modifica, **prova a salvare con ID3v2.4 OFF** (cioè come ID3v2.3) — il parser di Spotify è stato storicamente conservatore con v2.4.
- **Copertina: Media o Grande** — Spotify la riscala comunque.
- Compila almeno **Titolo**, **Artista**, **Album** e **Numero traccia**.

### Preparare file per upload distributore (DistroKid, TuneCore, CD Baby, ecc.)

Se sei un artista che carica il proprio lavoro sulle piattaforme di streaming, il distributore di solito legge i tag ma chiede anche i metadati nella sua interfaccia. In ogni caso:

- **ID3v2.3** è spesso la scelta più sicura — molte pipeline dei distributori sono state costruite anni fa e preferiscono il formato vecchio.
- Incorpora copertina **Grande** (la maggior parte dei distributori richiede ≥ 1.400 × 1.400 px — controlla le loro linee guida).
- Non fare affidamento sui tag estesi — i distributori leggono solo i campi core.

### Preparare file per Plex, Jellyfin, Navidrome, Subsonic, Emby

Questi server multimediali auto-ospitati sono molto tolleranti. Leggono sia v2.3 sia v2.4 in modo pulito e gestiscono bene UTF-8.

- **ID3v2.4: ON** va bene.
- **Copertina: Grande** o **Extra grande** — questi server servono la copertina ai client mobili e agli schermi CarPlay, quindi la qualità conta.
- **Album Artist** fortemente consigliato — è ciò che Plex/Jellyfin usano per raggruppare gli album per artista correttamente.

### Preparare file per autoradio e hardware vecchio

- **ID3v2.4: OFF** (usa ID3v2.3) — le unità più vecchie spesso non supportano v2.4.
- **Copertina: Media** — molti display auto si bloccano con copertine grandi incorporate.
- **Tag duplicati: ON** — alcune autoradio vecchie leggono solo il fallback ID3v1.

## Altre migliorie

### Design Liquid Glass

L'interfaccia di Evertag 4.2 è regolata sul nuovo materiale **Liquid Glass** di Apple in tutta l'app — superfici traslucide, animazioni più fluide e controlli rifiniti che si integrano naturalmente in iOS, iPadOS e macOS.

### Librerie di connessione aggiornate

Abbiamo rinfrescato le librerie interne usate da Evertag per dialogare con **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** e altri servizi. Risultato: meno fallimenti di connessione in casi limite, miglior supporto delle versioni più recenti dei server e maggiore affidabilità nella modifica dei tag su file remoti.

### Correzioni di traduzione e localizzazione

Più correzioni linguistiche nell'interfaccia in base ai feedback diretti degli utenti. Migliore adattamento del testo su pulsanti più piccoli in diverse lingue.

### Piccole rifiniture ispirate dai vostri feedback

Tante piccole migliorie basate sulle recensioni App Store e sulle email a support@everappz.com. Leggiamo ogni messaggio.

## Ottieni Evertag 4.2

[**Scarica Evertag dall'App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) o aggiorna dall'App Store. Evertag è un download gratuito con upgrade in-app opzionali per le funzioni avanzate. Le nuove connessioni cloud, i protocolli di rete, le migliorie di Wi-Fi Drive e l'interfaccia Liquid Glass sono parte dell'aggiornamento di base.

Se ti piace l'app, lascia una valutazione sull'App Store — aiuta davvero. Hai feedback o un problema? Scrivici a **support@everappz.com**. Leggiamo ogni messaggio.

## Domande frequenti

{{% details title="Cosa c'è di nuovo in Evertag 4.2?" closed="true" %}}
Evertag 4.2 aggiunge oltre 6 nuove connessioni cloud e server (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un Wi-Fi Drive rinnovato con selezione multipla e una coda di upload più intelligente, aggiornamenti dell'interfaccia Liquid Glass, librerie di connessione aggiornate, correzioni chiave nell'editing dei tag e migliorie alla traduzione.
{{% /details %}}

{{% details title="Devo usare ID3v2.4 o ID3v2.3 in Evertag?" closed="true" %}}
Usa **ID3v2.4** per i player moderni (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, app Android moderne) e per le librerie con caratteri non latini — il supporto UTF-8 significa tag più puliti in cinese, coreano, giapponese, russo, arabo ed ebraico. Usa **ID3v2.3** se i tag si visualizzano male in alcune app, se punti ad autoradio più vecchie o se la pipeline di un distributore di streaming rifiuta v2.4. Puoi sempre cambiare e risalvare.
{{% /details %}}

{{% details title="Perché i miei tag in Spotify sono sbagliati dopo la modifica?" closed="true" %}}
Spotify mostra principalmente metadati dal proprio catalogo — i tuoi tag locali si usano solo per i «File locali» o per contenuti che hai caricato come artista. Se stai taggando file per i File locali di Spotify e non si visualizzano correttamente, prova a disattivare ID3v2.4 in Evertag e a salvare come ID3v2.3 — il parser di Spotify è stato storicamente conservatore con v2.4.
{{% /details %}}

{{% details title="Quale dimensione di copertina dovrei scegliere in Evertag?" closed="true" %}}
Per la maggior parte degli utenti: **Grande**. Sta benissimo su telefoni, iPad, Mac e moderni display auto senza gonfiare troppo i file. Usa **Media** se hai una libreria enorme e vuoi risparmiare disco. Usa **Originale** (nessuna scalatura) solo per master d'archivio o quando serve davvero la massima qualità — ma sappi che alcuni player più vecchi hanno difficoltà con copertine incorporate molto grandi. **Originale** fa parte dell'upgrade personalizzazione premium di Evertag.
{{% /details %}}

{{% details title="Le copertine più grandi renderanno i miei file più grandi?" closed="true" %}}
Sì. Incorporare una copertina 3.000 × 3.000 px può aggiungere vari megabyte a un singolo file audio. Su una libreria di 1.000 tracce diventa qualche gigabyte. Se lo spazio è poco, usa Media o Grande; se trasmetti da un NAS dove la dimensione non conta, Extra grande o Originale vanno bene.
{{% /details %}}

{{% details title="Cosa sono i tag duplicati e dovrei attivarli?" closed="true" %}}
I tag duplicati scrivono i metadati core sia nella sezione ID3v1 (legacy 128 byte) sia in quella ID3v2 (moderna) del file. Attivali solo se punti a player molto vecchi o hardware che legge ID3v1. Per tutto ciò che è moderno (smartphone, computer, autoradio recenti), lascia disattivato.
{{% /details %}}

{{% details title="Evertag modifica i tag direttamente su file in cloud?" closed="true" %}}
Sì. Connettiti al cloud (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, ecc.) o tramite FTP/SFTP/NFS, apri un file e modifica i tag come se fosse locale. Evertag scarica il file, applica le modifiche e ricarica la versione aggiornata. Nelle impostazioni puoi scegliere tra le modalità «Chiedi sempre», «Auto-upload» o «Non caricare».
{{% /details %}}

{{% details title="Posso modificare i tag FLAC su iPhone con Evertag?" closed="true" %}}
Sì. Evertag supporta FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE e altri formati importanti con pieno supporto in lettura/scrittura dei tag, inclusa la copertina incorporata.
{{% /details %}}

{{% details title="Come modifico in modo sicuro i tag sul mio server domestico con SFTP?" closed="true" %}}
Apri Evertag, vai a Connessioni, scegli SFTP e inserisci hostname o IP del server, porta (di solito 22), nome utente e una password o una chiave SSH privata. Evertag mostrerà le tue cartelle remote e modificherà i tag direttamente con cifratura end-to-end su SSH.
{{% /details %}}

{{% details title="Posso modificare i tag su più file contemporaneamente?" closed="true" %}}
Sì. Attiva **Modifica file simultaneamente** nelle impostazioni. Seleziona più file, apri l'editor di tag e qualunque campo modifichi sarà applicato a tutti i file selezionati. È il modo più rapido per impostare lo stesso album artist, anno o genere su un intero album.
{{% /details %}}

{{% details title="L'aggiornamento a Evertag 4.2 è gratuito?" closed="true" %}}
Sì. Evertag è un download gratuito dall'App Store, e la 4.2 è un aggiornamento gratuito per tutti gli utenti esistenti. Le nuove integrazioni cloud, le migliorie di Wi-Fi Drive e l'interfaccia Liquid Glass sono parte dell'aggiornamento di base.
{{% /details %}}

{{% details title="Su quali dispositivi è disponibile Evertag 4.2?" closed="true" %}}
Evertag 4.2 funziona su iPhone, iPad e Mac. La sincronizzazione iCloud Drive mantiene coerenti tra dispositivi le impostazioni dell'editor di tag.
{{% /details %}}
