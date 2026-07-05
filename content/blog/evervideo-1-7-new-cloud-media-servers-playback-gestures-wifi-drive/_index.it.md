---
title: "Evervideo 1.7: nuovi Plex, Jellyfin, streaming cloud, gesti di riproduzione"
date: 2026-05-18
description: "Evervideo 1.7 aggiunge oltre 10 nuove connessioni — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — più nuovi gesti di riproduzione (doppio tocco per cercare, tocca e tieni premuto per la velocità 2x), un Wi-Fi Drive rinnovato con upload in batch e aggiornamenti UI Liquid Glass per iPhone, iPad e Mac."
keywords: ["Evervideo 1.7", "aggiornamento Evervideo", "lettore video HD iPhone", "lettore video Plex iOS", "Jellyfin video iPhone", "lettore video Emby iOS", "video Subsonic iOS", "video Navidrome iOS", "streaming video Internxt", "lettore video Proton Drive", "lettore video QNAP iPhone", "lettore video Nextcloud iOS", "streaming video Amazon S3", "lettore video SFTP iPhone", "lettore video FTP iOS", "streaming video NFS iPhone", "streaming video da NAS iPhone", "lettore MKV iPhone", "gesti lettore video iOS", "doppio tocco per cercare video", "trasferimento video Wi-Fi Drive iPhone", "design Liquid Glass", "lettore video cloud iOS 2026", "streaming film da cloud iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gesti di riproduzione", "Liquid Glass", "Novità"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evervideo 1.7](/products/evervideo) è un aggiornamento importante per il lettore video HD per iPhone, iPad e Mac. La release aggiunge oltre 10 nuove connessioni cloud, NAS e media server — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, oltre ai più popolari media server **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** ed **Emby**, e tre protocolli di rete: **FTP**, **SFTP** e **NFS**. I nuovi **gesti di riproduzione** ti permettono di toccare due volte per saltare avanti o indietro, tocca e tieni premuto per andare a 2x e un singolo tocco per attivare/disattivare i controlli — il tutto senza uscire dalla modalità a schermo intero. Wi-Fi Drive ottiene un'interfaccia rinnovata con modalità a selezione multipla e una coda di upload più intelligente. L'intera app è regolata per il nuovo design **Liquid Glass** di Apple.

---

## Ciao a tutti!

Arriva un grande aggiornamento di Evervideo. Questa è una delle release più grandi che abbiamo mai pubblicato: **oltre 10 nuove connessioni cloud, server e di rete**, nuovissimi **gesti di riproduzione** per un controllo più rapido a schermo intero, un'esperienza **Wi-Fi Drive** rinnovata e un'interfaccia regolata per **Liquid Glass** su iPhone, iPad e Mac.

[Scarica Evervideo 1.7 dall'App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) o aggiorna dalla tua versione esistente. Gli utenti Mac possono prendere la [versione desktop qui](https://apps.apple.com/app/evervideo/id6743504109).

## Oltre 10 nuove connessioni cloud, NAS e media server

Evervideo 1.7 amplia ciò che conta come la tua 'libreria video'. Se i tuoi film, serie o registrazioni vivono su un cloud di cui ti fidi, su un NAS di casa o su un media server auto-ospitato, Evervideo ora può fare streaming direttamente da lì — senza download, senza conversioni, senza ricodifica.

### Archiviazione cloud orientata alla privacy: Internxt e Proton Drive

Se ci tieni alla crittografia end-to-end e all'archiviazione zero-knowledge, due dei cloud più rispettati orientati alla privacy sono ora nativi in Evervideo:

- **Internxt** — cloud spagnolo open-source, crittografato post-quantum, conforme al GDPR. Piano gratuito disponibile.
- **Proton Drive** — archiviazione con crittografia end-to-end dai creatori di Proton Mail e Proton VPN, con sede in Svizzera. Piano gratuito disponibile con piani a pagamento per librerie più grandi.

Connettiti una volta e i tuoi video vengono trasmessi attraverso il tunnel crittografato — Evervideo non vede mai i tuoi dati in chiaro, e nemmeno il server del provider.

### Archiviazione auto-ospitata: QNAP, Nextcloud, Amazon S3

Per gli utenti che gestiscono la propria infrastruttura:

- **QNAP** — connessione API nativa ai dispositivi QNAP NAS per una riproduzione video veloce e affidabile su Wi-Fi locale o accesso remoto. Streaming di file 4K MKV direttamente senza ricodifica.
- **Nextcloud** — connettiti a qualsiasi istanza Nextcloud auto-ospitata o gestita. Ottimo se hai già migrato via da Google Drive o Dropbox per motivi di privacy.
- **Amazon S3** — punta Evervideo verso qualsiasi bucket S3 (o archiviazione compatibile con S3 come Backblaze B2, Wasabi, MinIO, Cloudflare R2) e fai streaming della tua collezione direttamente.

### <a id="media-servers"></a>Media server: Plex, Subsonic, Navidrome, Jellyfin, Emby

Questa è la grande novità per i fan dei video auto-ospitati. Evervideo 1.7 trasforma il tuo iPhone, iPad o Mac in un client di prima classe per i più popolari media server open-source e freemium:

- **Plex** — Plex Media Server è **gratuito** da scaricare ed eseguire, con un abbonamento opzionale **Plex Pass** per funzionalità come sincronizzazione mobile, transcoding hardware e TV in diretta. Evervideo funziona sia con le librerie gratuite che con Plex Pass — fai streaming della tua intera collezione di film e TV.
- **Subsonic** — il server di streaming auto-ospitato originale. Il server Subsonic ufficiale è **a pagamento** (1 dollaro al mese dopo una prova di 30 giorni), ed Evervideo parla anche l'API Subsonic con server video compatibili.
- **Navidrome** — server moderno, leggero, **completamente gratuito e open-source**. Implementa l'API Subsonic. Funziona su un Raspberry Pi, NAS o qualsiasi box Linux.
- **Jellyfin** — media server **completamente gratuito e open-source** (un fork comunitario di Emby). Gestisce film, TV, musica, libri e video casalinghi. Senza account, senza telemetria, senza abbonamenti. La scelta preferita per gli utenti che vogliono lo streaming auto-ospitato senza vincoli commerciali.
- **Emby** — media server **freemium**. Il server di base è gratuito; **Emby Premiere** è un acquisto una tantum o annuale che sblocca le app mobili, la sincronizzazione offline, Cinema Mode e altro. Evervideo si connette sia alle librerie gratuite che Premiere.

Qualunque server tu utilizzi, Evervideo trasmette in streaming la tua intera libreria — film, serie, video casalinghi e tracce di sottotitoli incorporate — con l'equalizzatore video, supporto 360°, Picture-in-Picture, AirPlay e Chromecast.

### Nuovi protocolli di rete: FTP, SFTP, NFS

Per gli utenti con server personalizzati, home lab o box NAS generici che non vengono forniti con un'app mobile rifinita, Evervideo 1.7 aggiunge tre protocolli classici:

- **SFTP (SSH File Transfer Protocol)** — la risposta giusta per lo **streaming video remoto sicuro dal tuo server**. SFTP viaggia su SSH, quindi l'intero trasferimento (autenticazione e dati video) è crittografato. Se hai un VPS, un server dedicato o un box Linux a casa con accesso SSH, puoi mettere una cartella di video su di esso e fare streaming attraverso internet pubblico senza esporre nient'altro. Supporta autenticazione con password e con chiave.
- **FTP** — lo standard di lunga data per il trasferimento di file. Utile se il tuo **NAS di casa** (Synology, ASUS, D-Link, TerraMaster più vecchi o box generici) espone un server FTP ma non ha un'integrazione API nativa. Meglio utilizzato all'interno della tua rete locale.
- **NFS (Network File System)** — il protocollo di condivisione de facto su Linux e sulla maggior parte dei dispositivi NAS. Le condivisioni NFS sono comuni negli home lab e nelle reti di piccole imprese; Evervideo ora le monta e fa streaming di video 4K e HD con overhead ridotto.

> **Suggerimento:** SFTP è il protocollo che vuoi per lo streaming su internet aperto. FTP e NFS sono migliori all'interno della tua rete locale — tienili fuori da internet pubblico a meno che non li avvolgi in una VPN.

## Nuovi gesti di riproduzione

Guardare video a schermo intero dovrebbe sembrare senza sforzo. Evervideo 1.7 introduce un set pulito di gesti a tocco che ti permettono di controllare la riproduzione senza esporre i controlli sullo schermo — perfetto per film, lezioni o qualsiasi cosa tu voglia guardare senza interruzioni.

### Doppio tocco — salta avanti o indietro

Tocca due volte il **lato destro** dello schermo per **saltare avanti** di un numero configurabile di secondi. Tocca due volte il **lato sinistro** per **saltare indietro**. Puoi cambiare l'intervallo (predefinito: 10 secondi) in **Impostazioni → Riproduzione → Intervallo di salto gesto** — scegli qualsiasi cosa da 5 secondi (per ricerca fine) a 60 secondi (per saltare le sigle).

Questo è il gesto che gli utenti YouTube e Netflix riconosceranno immediatamente, ed è ora nativo in Evervideo per qualsiasi video, da qualsiasi fonte.

### Tocca e tieni premuto — velocità 2x temporanea

Premi e tieni premuto ovunque sullo schermo per **accelerare temporaneamente la riproduzione a 2x**. Rilascia per tornare alla velocità normale. Perfetto per:

- Saltare scene lente senza impegnarsi in un cambio di velocità permanente.
- Scansionare rapidamente lezioni, tutorial o podcast per trovare la sezione rilevante.
- Assaggiare film prima di impegnarti a guardare la versione completa.

Il gesto di tenere premuto non cambia la tua velocità di riproduzione salvata — rilascia e sei di nuovo dove hai iniziato.

### Singolo tocco — mostra / nascondi controlli

Un singolo tocco sullo schermo attiva/disattiva i controlli di riproduzione (riproduci, pausa, barra di ricerca, sottotitoli, equalizzatore). Tocca una volta per farli apparire, tocca di nuovo per nasconderli. Combinato con il doppio tocco e il tenere premuto, ciò significa che puoi passare quasi un intero film in modalità schermo intero pulita e potrai comunque cercare, mettere in pausa e scansionare la velocità ogni volta che ne hai bisogno.

## Wi-Fi Drive: nuova UI e upload più rapidi

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) è la funzionalità integrata di Evervideo per **trasferire video in modo wireless dal tuo computer al tuo iPhone o iPad — senza iTunes, senza cavi, senza account cloud richiesto**. Entrambi i dispositivi devono essere sulla stessa rete Wi-Fi. Avvii il server sull'app iOS e poi:

- Apri l'URL in qualsiasi browser desktop (Safari, Chrome, Firefox, Edge), trascina i tuoi file video nella pagina, e verranno caricati direttamente sul dispositivo, oppure
- Monta il dispositivo come condivisione di rete tramite **Mac Finder** ('Connetti al server...') o **Windows File Explorer** (Mappa unità di rete) utilizzando WebDAV.

È il modo più veloce per spostare una grande collezione video locale sul telefono o sul tablet senza alcun servizio di terze parti. Vedi la [guida passo passo qui](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

In Evervideo 1.7, Wi-Fi Drive ottiene:

- **Interfaccia utente ridisegnata** — più pulita, più facile da leggere a colpo d'occhio e aggiornata per Liquid Glass.
- **Nuova modalità di selezione per azioni in batch** — scegli più file o cartelle e agisci su di essi in massa (elimina, sposta, copia).
- **Coda di upload file migliorata** — migliore feedback di avanzamento e resilienza ai problemi di rete, in modo che una connessione Wi-Fi instabile non rovini più un trasferimento da 30 GB.
- **Migliori prestazioni di trasferimento complessive** — upload misurabilmente più veloci per librerie di grandi dimensioni, specialmente per file 4K MKV e collezioni di film.

## Altri miglioramenti

### Aggiornamenti del design Liquid Glass

L'interfaccia di Evervideo 1.7 è aggiornata per il nuovo materiale **Liquid Glass** di Apple in tutta l'app — superfici traslucide, animazioni più fluide e controlli raffinati che si adattano naturalmente a iOS 26, iPadOS 26 e macOS 26. Now Playing, il browser dei file e le schermate delle impostazioni sono stati tutti ritarati per corrispondere alla nuova estetica di sistema.

### Librerie di connessione aggiornate

Abbiamo aggiornato le librerie sottostanti che Evervideo utilizza per parlare con **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** e altri servizi. Il risultato: meno fallimenti di connessione edge-case, migliore supporto per le versioni di server più recenti e affidabilità migliorata durante lo streaming video su connessioni più lente o geograficamente distanti.

### Correzioni di bug di riproduzione

- Corretti problemi di riproduzione su determinati server auto-ospitati dove gli stream si bloccavano dopo la ricerca su grandi file MKV.
- Migliore comportamento di ripresa quando la rete cade brevemente durante la riproduzione.
- Sincronizzazione dei sottotitoli più fluida su contenuti in formato lungo.

### Correzioni di localizzazione

Correzioni di traduzione in più lingue basate sul feedback diretto degli utenti. Migliore adattamento del testo sui pulsanti più piccoli e nelle lingue europee più lunghe (tedesco, olandese, francese).

### Piccole rifiniture ispirate al tuo feedback

Molti miglioramenti più piccoli basati sulle recensioni dell'App Store e sulle email a support@everappz.com. Leggiamo ogni messaggio.

## Perché questo aggiornamento è importante

Evervideo 1.7 è costruito attorno a tre idee:

1. **I tuoi video, ovunque tu li conservi.** Che la tua libreria viva su iCloud Drive, un cloud orientato alla privacy come Proton Drive o Internxt, un media server come Plex o Jellyfin, un NAS a casa o un Raspberry Pi che esegue Navidrome — Evervideo ora si connette ad esso nativamente, con la stessa esperienza di riproduzione ovunque.
2. **Video a schermo intero che sembra senza sforzo.** I nuovi gesti a tocco (doppio tocco, tocca e tieni premuto, singolo tocco) portano il tipo di controllo fluido che le app di streaming come YouTube e Netflix hanno addestrato gli utenti ad aspettarsi, applicato alla *tua* collezione video.
3. **Trasferimenti più rapidi dal tuo computer.** Un Wi-Fi Drive rinnovato con selezione in batch e una coda di upload più intelligente rende il trasferimento di grandi collezioni di film 4K sul tuo iPhone o iPad genuinamente veloce — senza cavi, senza iTunes, senza compressione.

## Ottieni Evervideo 1.7

[**Scarica Evervideo dall'App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) o aggiorna dall'interno dell'App Store. La [versione Mac](https://apps.apple.com/app/evervideo/id6743504109) è disponibile separatamente come app Mac universale. Evervideo è un download gratuito con upgrade in-app opzionali per funzionalità avanzate. Le nuove connessioni cloud, il supporto per media server, i gesti di riproduzione, i miglioramenti Wi-Fi Drive e l'UI Liquid Glass fanno parte dell'aggiornamento base.

Se ti piace l'app, lascia per favore una valutazione sull'App Store — aiuta davvero. Hai feedback o riscontri un problema? Scrivici a **support@everappz.com**. Leggiamo ogni messaggio.

## Domande frequenti

{{% details title="Cosa c'è di nuovo in Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduce il supporto per oltre 10 nuove connessioni (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nuovi gesti di riproduzione (doppio tocco per cercare, tocca e tieni premuto per velocità 2x, singolo tocco per attivare/disattivare i controlli), un Wi-Fi Drive ridisegnato con modalità di selezione e una coda di upload più intelligente, aggiornamenti al design Liquid Glass, librerie di connessione aggiornate e numerose correzioni di bug.
{{% /details %}}

{{% details title="Evervideo funziona con Plex?" closed="true" %}}
Sì. A partire da Evervideo 1.7, puoi connetterti a un Plex Media Server e fare streaming della tua intera libreria video — film, serie TV e video casalinghi. Plex Media Server è gratuito da eseguire; Plex Pass è opzionale. Evervideo supporta sia le configurazioni gratuite che Plex Pass, inclusa la riproduzione diretta di MKV, MP4, AVI, MOV e altri formati senza ricodifica.
{{% /details %}}

{{% details title="Jellyfin o Navidrome sono supportati in Evervideo?" closed="true" %}}
Sì. Sia Jellyfin che Navidrome sono completamente supportati in Evervideo 1.7. Jellyfin è un media server gratuito e open-source che gestisce video e audio. Navidrome è un server gratuito e open-source che implementa l'API Subsonic. Evervideo si connette a entrambi nativamente.
{{% /details %}}

{{% details title="Plex, Jellyfin, Emby, Navidrome e Subsonic sono gratuiti?" closed="true" %}}
- **Plex** — il server è gratuito; Plex Pass è un upgrade a pagamento opzionale.
- **Jellyfin** — completamente gratuito e open-source.
- **Emby** — il server è gratuito; Emby Premiere è a pagamento e sblocca la sincronizzazione mobile e offline.
- **Navidrome** — completamente gratuito e open-source.
- **Subsonic** — il server ufficiale costa 1 dollaro al mese dopo una prova di 30 giorni, ma la sua API è aperta e molti server gratuiti (incluso Navidrome) la implementano.
{{% /details %}}

{{% details title="Posso fare streaming dal mio NAS di casa tramite SFTP, FTP o NFS?" closed="true" %}}
Sì. Evervideo 1.7 aggiunge SFTP, FTP e NFS come tipi di connessione nativi. SFTP è la scelta consigliata per lo streaming dal tuo server su internet pubblico perché tutto il traffico è crittografato tramite SSH. FTP e NFS sono meglio utilizzati all'interno della tua rete locale o dietro una VPN.
{{% /details %}}

{{% details title="Come collego Evervideo a un server personalizzato usando SFTP?" closed="true" %}}
Apri Evervideo, vai alla scheda Connessioni, scegli SFTP e inserisci hostname o IP del tuo server, porta (di solito 22), nome utente e password o chiave privata SSH. Evervideo sfoglierà le tue cartelle remote e farà streaming dei file video direttamente con crittografia end-to-end.
{{% /details %}}

{{% details title="Evervideo supporta Internxt e Proton Drive?" closed="true" %}}
Sì. Entrambi i cloud orientati alla privacy sono supportati a partire da Evervideo 1.7. Si uniscono a MEGA e altri servizi privacy-first già disponibili nell'app.
{{% /details %}}

{{% details title="Come funzionano i nuovi gesti di riproduzione?" closed="true" %}}
Nella riproduzione video a schermo intero, **tocca due volte il lato destro** per saltare avanti e **tocca due volte il lato sinistro** per saltare indietro di un intervallo configurabile (predefinito 10 secondi — modificalo in Impostazioni). **Tocca e tieni premuto** ovunque sullo schermo per accelerare temporaneamente a 2x; rilascia per tornare al normale. **Singolo tocco** ovunque per attivare/disattivare i controlli di riproduzione (mostra o nascondi).
{{% /details %}}

{{% details title="Posso cambiare l'intervallo di salto del doppio tocco?" closed="true" %}}
Sì. Vai a **Impostazioni → Riproduzione → Intervallo di salto gesto** e scegli un valore tra 5 e 60 secondi. La maggior parte degli utenti lo mantiene a 10 o 15 secondi.
{{% /details %}}

{{% details title="Cos'è Wi-Fi Drive in Evervideo?" closed="true" %}}
Wi-Fi Drive è la funzionalità di trasferimento file wireless integrata di Evervideo. Ti consente di caricare video dal tuo computer al tuo iPhone o iPad sulla tua rete Wi-Fi locale — senza iTunes, senza cavi, senza account cloud. Puoi usare qualsiasi browser desktop o un client WebDAV come Mac Finder o Windows File Explorer. Vedi la [guida completa Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="Evervideo riproduce MKV, AVI e altri formati da Plex o Jellyfin?" closed="true" %}}
Sì. Evervideo riproduce praticamente ogni formato video — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — e li trasmette direttamente da Plex, Jellyfin, Emby e altri media server senza richiedere transcoding per la maggior parte dei codec. Ciò significa un carico CPU inferiore sul tuo server e tempi di avvio più rapidi.
{{% /details %}}

{{% details title="Evervideo 1.7 è gratuito da aggiornare?" closed="true" %}}
Sì. Evervideo è un download gratuito dall'App Store e 1.7 è un aggiornamento gratuito per tutti gli utenti esistenti. Le nuove integrazioni cloud, il supporto per media server, i gesti di riproduzione, i miglioramenti Wi-Fi Drive e l'UI Liquid Glass fanno parte dell'aggiornamento base.
{{% /details %}}

{{% details title="Su quali dispositivi è disponibile Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 funziona su iPhone, iPad e Mac. AirPlay e Chromecast ti permettono di trasmettere la riproduzione a uno schermo più grande. La sincronizzazione iCloud Drive mantiene la tua libreria e le tue impostazioni coerenti tra i dispositivi.
{{% /details %}}
