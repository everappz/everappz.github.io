---
title: "Evermusic 8.6: nuovo CarPlay, Plex, Jellyfin, SFTP, widget testi"
date: 2026-05-08
description: "Evermusic 8.6 introduce un'esperienza CarPlay completamente ridisegnata, supporto a Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS, un widget di testi sincronizzati sulla schermata Home, miglioramenti a Wi-Fi Drive e aggiornamenti dell'interfaccia Liquid Glass."
keywords: ["Evermusic 8.6", "aggiornamento Evermusic", "lettore musicale CarPlay iPhone", "lettore Plex iOS", "Jellyfin iPhone musica", "lettore Emby iOS", "app Subsonic iOS", "client Navidrome iOS", "streaming musica Internxt", "lettore Proton Drive", "lettore musicale QNAP iPhone", "lettore Nextcloud iOS", "streaming musica Amazon S3", "lettore SFTP iPhone", "lettore audio FTP iOS", "streaming musica NFS iPhone", "widget testi sincronizzati iPhone", "widget testi schermata Home iOS", "Wi-Fi Drive iPhone", "lettore Baidu Netdisk", "lettore Aliyun Drive", "design Liquid Glass", "lettore musicale cloud iOS 2026"]
tags: ["Evermusic", "Evermusic 8.6", "CarPlay", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Widget testi", "Widget schermata Home", "Liquid Glass", "Novità"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evermusic 8.6](/products/evermusic) è un aggiornamento importante per iPhone, iPad e Mac. CarPlay è ricostruito da zero con ordinamento rapido, più schemi di colore, schermata In riproduzione ridisegnata, vista completa della coda e indice alfabetico a scorrimento veloce. La versione aggiunge oltre 10 nuove connessioni — **Plex**, **Jellyfin**, **Emby**, **Subsonic**, **Navidrome**, **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3** e i protocolli **FTP**, **SFTP** e **NFS**. Un nuovo **widget di testi sincronizzati per la schermata Home** mostra i testi a tempo mentre ascolti. Wi-Fi Drive ha una nuova interfaccia, modalità di selezione e una coda di upload più veloce. L'intera app è aggiornata al design **Liquid Glass** e lo streaming dai server cinesi come **Baidu Netdisk (百度网盘)** e **Aliyun Drive (阿里云盘)** è più affidabile.

---

## Ciao a tutti!

Evermusic 8.6 è disponibile per il download. È uno degli aggiornamenti più grandi che abbiamo rilasciato: un'esperienza CarPlay completamente ridisegnata, oltre dieci nuove integrazioni cloud e server, un nuovissimo widget di testi sincronizzati per la schermata Home e un'interfaccia Liquid Glass aggiornata in tutta l'app.

[Scarica Evermusic 8.6 dall'App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) oppure aggiorna dalla tua versione attuale.

## Una nuovissima esperienza CarPlay

Abbiamo ricostruito Evermusic per **Apple CarPlay** da zero. Il risultato è più veloce, più fluido e molto più facile da usare al volante.

- **Ordinamento rapido** — trova qualsiasi traccia in pochi secondi tra album, artisti, playlist e cartelle.
- **Più schemi di colore** — scegli un tema che si abbini al cruscotto o all'illuminazione interna dell'auto.
- **Schermata In riproduzione ridisegnata** — copertine più grandi, controlli più chiari e nuove azioni di riproduzione attivabili con un tocco.
- **Coda di riproduzione completa a colpo d'occhio** — vedi cosa viene dopo senza uscire dalla schermata corrente.
- **Indice alfabetico a scorrimento veloce** — sposta tra librerie enormi (oltre 10.000 tracce) senza scorrere all'infinito.
- **Caricamento dei contenuti più fluido** — niente più blocchi all'apertura di cartelle grandi, directory cloud o librerie di server multimediali.

Se trasmetti musica dal cloud mentre guidi — Dropbox, Google Drive, OneDrive, iCloud Drive, [Plex](#media-servers), [Jellyfin](#media-servers) e altri — la nuova esperienza CarPlay rende tutto naturale all'interno dell'auto.

## Oltre 10 nuove integrazioni cloud, NAS e server

Evermusic 8.6 amplia il concetto di "libreria musicale". Se i tuoi file audio si trovano in un cloud di cui ti fidi, su un NAS a casa o su un server multimediale auto-ospitato, Evermusic può ora riprodurli direttamente — senza sincronizzazioni o esportazioni.

### Cloud orientati alla privacy: Internxt e Proton Drive

Se ti interessano la cifratura end-to-end e l'archiviazione zero-knowledge, due dei nomi più noti del cloud privato sono ora nativi in Evermusic:

- **Internxt** — cloud spagnolo open source, con cifratura post-quantistica e conforme al GDPR. Piano gratuito disponibile.
- **Proton Drive** — archiviazione cifrata end-to-end dei creatori di Proton Mail e Proton VPN, con sede in Svizzera. Piano gratuito disponibile, con piani a pagamento per librerie più grandi.

Connettiti una volta e la tua musica passerà attraverso il tunnel cifrato — Evermusic non vede mai i tuoi dati in chiaro, e nemmeno il server del provider.

### Archiviazione auto-ospitata: QNAP, Nextcloud, Amazon S3

Per chi gestisce la propria infrastruttura:

- **QNAP** — connessione API nativa ai NAS QNAP per una riproduzione rapida e affidabile via Wi-Fi locale o accesso remoto.
- **Nextcloud** — collega qualsiasi istanza Nextcloud auto-ospitata o gestita. Ottimo se hai già lasciato Google Drive o Dropbox per motivi di privacy.
- **Amazon S3** — punta Evermusic a qualsiasi bucket S3 (o storage S3-compatibile come Backblaze B2, Wasabi, MinIO, Cloudflare R2) e riproduci direttamente la tua collezione.

### <a id="media-servers"></a>Server multimediali: Plex, Subsonic, Navidrome, Jellyfin, Emby

Questa è la grande novità per gli appassionati di musica auto-ospitata. Evermusic 8.6 trasforma il tuo iPhone, iPad o Mac in un client di prima classe per i server multimediali open source e freemium più popolari:

- **Plex** — Plex Media Server è **gratuito** da scaricare ed eseguire. L'abbonamento **Plex Pass** è opzionale e sblocca funzioni come sync mobile, transcodifica hardware e TV in diretta. Evermusic funziona sia con librerie gratuite sia con Plex Pass.
- **Subsonic** — il server originale di streaming musicale auto-ospitato. Il server ufficiale Subsonic è **a pagamento** (1 $/mese dopo una prova di 30 giorni), ma Evermusic parla anche l'API Subsonic con decine di server compatibili.
- **Navidrome** — server musicale moderno e leggero, **completamente gratuito e open source**, scritto in Go. Implementa l'API Subsonic. Gira su Raspberry Pi, NAS o qualunque macchina Linux. Molto consigliato per librerie fino a qualche centinaio di migliaia di tracce.
- **Jellyfin** — server multimediale **completamente gratuito e open source** (un fork comunitario di Emby). Gestisce musica, film, TV, libri e audiolibri. Niente account, niente telemetria, niente abbonamenti.
- **Emby** — server multimediale **freemium**. Il server di base è gratuito; **Emby Premiere** è un acquisto una tantum o annuale che sblocca app mobili, sync offline, modalità Cinema e altro. Evermusic si connette sia a librerie gratuite sia Premiere.

Qualunque server tu usi, Evermusic riproduce in streaming l'intera libreria — album, artisti, playlist, generi e copertine integrate — con cache offline, riproduzione gapless e crossfade, equalizzatore a 10 bande, AirPlay, Chromecast e **CarPlay**. Il tuo server tiene la cronologia di ascolto; Evermusic la rispetta.

### Nuovi protocolli di rete: FTP, SFTP, NFS

Per chi ha server personalizzati, homelab o NAS generici senza una bella app mobile, Evermusic 8.6 aggiunge tre protocolli classici:

- **SFTP (SSH File Transfer Protocol)** — la risposta giusta per **streaming remoto sicuro dal proprio server**. SFTP gira su SSH, quindi l'intero trasferimento (autenticazione e dati audio) è cifrato. Se hai un VPS, un server dedicato o un PC Linux a casa con accesso SSH, puoi caricarci una cartella di musica e ascoltarla via Internet pubblica senza esporre nient'altro. Supporta autenticazione con password e con chiave.
- **FTP** — lo standard storico di trasferimento file. Utile se il tuo **NAS di casa** (Synology vecchio, ASUS, D-Link, TerraMaster o box generici) espone un server FTP ma non ha un'integrazione API nativa. Meglio sulla rete locale.
- **NFS (Network File System)** — il protocollo di condivisione di fatto su Linux e sulla maggior parte dei NAS. Le condivisioni NFS sono comuni in homelab e piccole reti aziendali; Evermusic ora le monta e riproduce direttamente. Overhead inferiore rispetto a SMB sullo stesso hardware.

> **Suggerimento:** SFTP è il protocollo che vuoi per lo streaming dall'Internet pubblica. FTP e NFS è meglio usarli sulla rete locale — non esporli su Internet a meno di incapsularli in una VPN.

## Wi-Fi Drive: nuova interfaccia e upload più veloci

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) è la funzione integrata di Evermusic per **trasferire musica in modalità wireless dal computer all'iPhone o all'iPad — senza iTunes, senza cavi e senza account cloud**. Entrambi i dispositivi devono trovarsi sulla stessa rete Wi-Fi. Avvii il server nell'app iOS e poi:

- apri l'URL in qualsiasi browser desktop (Safari, Chrome, Firefox, Edge), trascina i tuoi file musicali nella pagina e vengono caricati direttamente sul dispositivo, oppure
- monta il dispositivo come condivisione di rete tramite **Mac Finder** ("Connetti al server…") o **Windows File Explorer** (Connetti unità di rete) usando WebDAV.

È il modo più veloce di spostare una grande libreria musicale locale sul telefono senza servizi di terze parti. Vedi la [guida passo-passo qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

In Evermusic 8.6, Wi-Fi Drive ottiene:

- **Nuova interfaccia utente** — più pulita e più leggibile a colpo d'occhio.
- **Modalità di selezione** — scegli più file o cartelle e agisci in blocco.
- **Coda di upload migliorata** — feedback di avanzamento più chiaro e maggiore resilienza ai cali di rete.
- **Migliori prestazioni complessive** — trasferimenti più rapidi per librerie grandi.

## Nuovo widget di testi sincronizzati per la schermata Home

Una delle funzioni più richieste è finalmente qui: **un widget di testi sincronizzati che puoi fissare alla schermata Home di iPhone, iPad o Mac**.

Quando riproduci una traccia con testi a tempo, il widget mostra la **riga corrente** del brano in tempo reale — e la riga avanza con la musica. Tocca il widget per aprire Evermusic nella vista completa dei testi.

Cosa fa:

- Mostra **testi sincronizzati e con timestamp** per la traccia in riproduzione.
- Si aggiorna con l'avanzamento del brano — niente refresh manuali, niente scorrimenti.
- Funziona con i testi LRC integrati nei file audio e con i testi recuperati nell'app.
- Disponibile in **più dimensioni di widget** così scegli quanto testo entra sulla schermata Home.
- Funziona su **iPhone**, **iPad** e **Mac** (schermata Home e centro notifiche dove supportato).

Il widget è perfetto per chi ama seguire i testi mentre il telefono è sulla scrivania, su uno stand o sulla schermata di blocco durante un ascolto lungo. Si abbina particolarmente bene ad audiolibri e contenuti tipo podcast, dove leggere aiuta la comprensione.

Per attivarlo, tieni premuta la schermata Home, tocca **Modifica > Aggiungi widget**, cerca **Evermusic** e scegli il widget **Testi** nella dimensione che preferisci.

## Altre migliorie

### Aggiornamenti del design Liquid Glass

L'interfaccia di Evermusic 8.6 è aggiornata al nuovo materiale **Liquid Glass** di Apple in tutta l'app — superfici traslucide, animazioni più fluide e controlli rifiniti che si integrano naturalmente in iOS, iPadOS e macOS.

### Maggiore affidabilità per i server cinesi

In questa versione abbiamo investito molto nella stabilità di riproduzione di **Baidu Netdisk (百度网盘)** e **Aliyun Drive (阿里云盘)**. Se hai già usato questi servizi con Evermusic, noterai:

- Elenco delle directory più rapido in librerie con migliaia di file.
- Streaming più affidabile su connessioni lente o geograficamente distanti.
- Meno disconnessioni durante sessioni di ascolto lunghe.
- Logica di retry e ripresa migliorata quando la rete cade brevemente.

Questi due cloud sono i servizi di archiviazione consumer più popolari in Cina, ed Evermusic è uno dei pochi player musicali iOS con supporto nativo di prima classe per entrambi.

### Librerie di connessione aggiornate

Abbiamo aggiornato le librerie interne usate da Evermusic per dialogare con **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** e altri servizi. Tradotto: meno fallimenti di connessione in casi limite, miglior supporto delle versioni più recenti dei server e migliori prestazioni complessive.

### Nuovi widget per la schermata Home e aggiornamenti più intelligenti

Oltre al nuovo widget testi, i widget esistenti — In riproduzione, Coda di riproduzione, Riprodotti di recente — sono stati raffinati con una **migliore logica di aggiornamento**, così restano sincronizzati senza consumare batteria extra. Ci sono anche nuovi layout di widget per chi vuole più controllo su cosa appare a colpo d'occhio.

### Correzioni di bug e rifiniture

- Risolti problemi di riproduzione su alcuni server multimediali e configurazioni auto-ospitate.
- Correzioni di localizzazione in diverse lingue.
- Tante piccole migliorie basate sui feedback diretti dalle recensioni App Store ed e-mail a support@everappz.com.

## Perché questo aggiornamento è importante

Evermusic 8.6 è costruito intorno a tre idee:

1. **La tua musica, ovunque la conservi.** Che la libreria stia su iCloud Drive, su un cloud orientato alla privacy come Proton Drive o Internxt, su un server multimediale come Plex o Jellyfin, su un NAS a casa o su un Raspberry Pi con Navidrome — Evermusic ora si collega in modo nativo, con la stessa esperienza di riproduzione ovunque.
2. **Migliore in auto.** CarPlay è lo schermo che molti utenti guardano di più, e l'esperienza ricostruita lo riflette.
3. **Testi sulla schermata Home.** Il nuovo widget di testi sincronizzati porta sulla tua superficie principale qualcosa che nessun altro fa davvero bene.

## Ottieni Evermusic 8.6

[**Scarica Evermusic dall'App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o aggiorna dall'App Store. Evermusic è un download gratuito con upgrade in-app opzionali per le funzioni avanzate. Il nuovo CarPlay, il widget testi e tutte le nuove integrazioni server fanno parte dell'aggiornamento di base.

Se ti piace l'app, lascia una valutazione sull'App Store — aiuta davvero. Hai feedback o un problema? Scrivici a **support@everappz.com**. Leggiamo ogni messaggio.

## Domande frequenti

{{% details title="Cosa c'è di nuovo in Evermusic 8.6?" closed="true" %}}
Evermusic 8.6 introduce un'esperienza CarPlay completamente ridisegnata, supporto a oltre 10 nuove connessioni (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un nuovo widget di testi sincronizzati per la schermata Home, miglioramenti all'interfaccia di Wi-Fi Drive con modalità di selezione, aggiornamenti del design Liquid Glass, maggiore affidabilità per Baidu Netdisk e Aliyun Drive e molte correzioni di bug.
{{% /details %}}

{{% details title="Evermusic funziona con Plex?" closed="true" %}}
Sì. A partire da Evermusic 8.6 puoi connetterti a un server Plex Media e riprodurre l'intera libreria musicale. Plex Media Server è gratuito; Plex Pass è opzionale. Evermusic supporta sia configurazioni gratuite sia Plex Pass.
{{% /details %}}

{{% details title="Jellyfin e Navidrome sono supportati in Evermusic?" closed="true" %}}
Sì. Sia Jellyfin sia Navidrome sono pienamente supportati in Evermusic 8.6. Jellyfin è un server multimediale gratuito e open source. Navidrome è un server musicale gratuito e open source che implementa l'API Subsonic. Evermusic si collega nativamente a entrambi.
{{% /details %}}

{{% details title="Plex, Jellyfin, Emby, Navidrome e Subsonic sono gratuiti?" closed="true" %}}
- **Plex** — il server è gratuito; Plex Pass è un upgrade a pagamento opzionale.
- **Jellyfin** — completamente gratuito e open source.
- **Emby** — il server è gratuito; Emby Premiere è a pagamento e sblocca sync mobile e offline.
- **Navidrome** — completamente gratuito e open source.
- **Subsonic** — il server ufficiale costa 1 $/mese dopo 30 giorni di prova, ma la sua API è aperta e molti server gratuiti (incluso Navidrome) la implementano.
{{% /details %}}

{{% details title="Posso fare streaming dal NAS di casa via SFTP, FTP o NFS?" closed="true" %}}
Sì. Evermusic 8.6 aggiunge SFTP, FTP e NFS come tipi di connessione nativi. SFTP è la scelta consigliata per fare streaming dal proprio server via Internet pubblica perché tutto il traffico è cifrato tramite SSH. FTP e NFS sono migliori sulla rete locale o dietro una VPN.
{{% /details %}}

{{% details title="Come collego Evermusic a un server personalizzato usando SFTP?" closed="true" %}}
Apri Evermusic, vai alla scheda Connessioni, scegli SFTP e inserisci hostname o IP del server, porta (di solito 22), nome utente e una password o una chiave SSH privata. Evermusic mostrerà le tue cartelle remote e farà streaming dei file audio direttamente con cifratura end-to-end.
{{% /details %}}

{{% details title="Evermusic supporta Internxt e Proton Drive?" closed="true" %}}
Sì. Entrambi i cloud orientati alla privacy sono supportati a partire da Evermusic 8.6. Si aggiungono a Mega e ad altri servizi privacy-first già disponibili nell'app.
{{% /details %}}

{{% details title="Cos'è Wi-Fi Drive in Evermusic?" closed="true" %}}
Wi-Fi Drive è la funzione integrata di Evermusic per il trasferimento file wireless. Ti permette di caricare musica dal computer all'iPhone o all'iPad sulla rete Wi-Fi locale — senza iTunes, senza cavi, senza account cloud. Puoi usare qualsiasi browser desktop o un client WebDAV come Mac Finder o Windows File Explorer. Vedi la [guida completa di Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Come funziona il nuovo widget testi?" closed="true" %}}
Il widget testi mostra testi sincronizzati a tempo sulla schermata Home di iPhone, iPad o Mac per la traccia in riproduzione. La riga visualizzata avanza automaticamente con il brano. Aggiungilo tenendo premuta la schermata Home, toccando Modifica > Aggiungi widget, cercando Evermusic e scegliendo il widget Testi.
{{% /details %}}

{{% details title="Evermusic 8.6 risolve i problemi di riproduzione su Baidu Netdisk e Aliyun Drive?" closed="true" %}}
Sì. Abbiamo apportato significativi miglioramenti di affidabilità per 百度网盘 (Baidu Netdisk) e 阿里云盘 (Aliyun Drive), inclusi listing delle directory più veloce, retry più intelligenti su connessioni deboli e migliore comportamento di ripresa nelle sessioni di ascolto lunghe.
{{% /details %}}

{{% details title="L'aggiornamento a Evermusic 8.6 è gratuito?" closed="true" %}}
Sì. Evermusic è un download gratuito dall'App Store, e la 8.6 è un aggiornamento gratuito per tutti gli utenti esistenti. Il nuovo CarPlay, il widget testi e tutte le nuove integrazioni server sono parte dell'aggiornamento di base.
{{% /details %}}

{{% details title="Su quali dispositivi è disponibile Evermusic 8.6?" closed="true" %}}
Evermusic 8.6 funziona su iPhone, iPad e Mac. Il supporto CarPlay richiede un veicolo o un'unità principale aftermarket compatibile CarPlay.
{{% /details %}}
