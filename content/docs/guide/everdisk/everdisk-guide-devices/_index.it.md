---
title: "Collegati ai server"
date: 2026-08-20
description: "Usa la scheda Dispositivi in Everdisk per collegarti ad altri server sulla tua rete. Aggiungi e sfoglia server DLNA, WebDAV, FTP, SFTP e SMB e unità NAS, riproduci in streaming audio e video, scarica file e crea, carica, rinomina, sposta o elimina sui server che lo consentono."
keywords: ["scheda Dispositivi Everdisk", "collegarsi a NAS", "client DLNA iPhone", "client WebDAV iPhone", "client FTP iPhone", "client SFTP iPhone", "client SMB iPhone", "connettersi a condivisione SMB", "sfogliare server di rete", "streaming da NAS", "scaricare da server", "collegare cloud WebDAV"]
tags: ["everdisk", "guida", "dispositivi", "connessioni"]
readingTime: 9
---


Everdisk non è solo un'unità wireless: è anche un client per gli altri dispositivi della tua rete. La scheda **Dispositivi** ti permette di collegarti a server **DLNA**, **WebDAV**, **FTP**, **SFTP** e **SMB**, inclusi Mac, PC Windows, macchine Linux, unità NAS e media server, per poi sfogliare, riprodurre in streaming e scaricare i loro file.

## La schermata Dispositivi

La scheda Dispositivi ha due parti:

- **Connessioni**: i server che hai già salvato.
- **Dispositivi disponibili**: i server che Everdisk trova automaticamente sulla tua rete locale.

Per collegarti a qualcosa che Everdisk ha già trovato, basta toccarlo in **Dispositivi disponibili**. Per aggiungere un server manualmente, tocca il pulsante **più (+)** o **Nuova connessione**.

## Aggiungere una nuova connessione

Tocca **Nuova connessione** e scegli il tipo di server che vuoi raggiungere:

- **DLNA / UPnP**: ideale per i media server. Riproduci in streaming video, musica e foto da librerie multimediali, unità di archiviazione di rete e TV e computer compatibili con DLNA. Il DLNA è di sola lettura: puoi sfogliare, riprodurre in streaming e scaricare, ma non puoi caricare o modificare i file.
- **WebDAV**: collegati a file server, unità di archiviazione di rete e unità cloud che supportano WebDAV. Lettura e scrittura quando il server lo consente.
- **FTP**: comune su router, unità di archiviazione di rete e hosting web. La porta predefinita è 21 (990 per FTPS sicuro); puoi impostare una porta personalizzata nell'indirizzo, per esempio `ftp://host:2121`. Lascia vuoti il login e la password per l'accesso anonimo.
- **SFTP**: collegati in modo sicuro tramite SSH. La porta predefinita è 22; usa una porta personalizzata nell'indirizzo se necessario, per esempio `sftp://host:2222`.
- **SMB**: connettiti a Mac, PC Windows, server Linux e archivi di rete (NAS) che condividono cartelle tramite **SMB / CIFS**. Inserisci un indirizzo come `smb://server-address/share-name/` (esempi: `smb://local-server-name/share-name/folder-path`, `smb://192.168.1.105/share-name/folder-path`, `smb://remote-server.com`). SMB aggiunge due campi opzionali: un nome del **Gruppo di lavoro** e una **Versione del protocollo** che puoi lasciare su **Automatica** o forzare a **SMB1** o **SMB2**. Se file o cartelle con caratteri speciali non si aprono, prova a cambiare la versione in **SMB1**.

> Everdisk si collega solo a questi protocolli di rete locale e con indirizzo diretto. Non accede ad account cloud come Google Drive o Dropbox. Un'unità cloud è raggiungibile solo se quel servizio offre un indirizzo **WebDAV** che puoi digitare.

## Inserire l'indirizzo e accedere

Nell'editor della connessione, compila:

- **Titolo**: un nome facile da riconoscere per la connessione.
- **URL / indirizzo**: l'indirizzo del server (per ogni tipo vengono mostrati alcuni esempi).
- **Login** e **Password**: lasciali entrambi vuoti se il server consente l'accesso anonimo.

Per WebDAV puoi consentire i certificati non validi se il tuo server ne usa uno autofirmato. Se l'identità di un server sicuro non può essere verificata, Everdisk ti chiede di confermare prima di considerarlo attendibile.

Gli utenti gratuiti possono salvare fino a **10** connessioni. Premium rimuove il limite.

## Sfogliare, riprodurre in streaming e scaricare

Una volta collegato, tocca il server per aprirlo:

- **Sfoglia** le cartelle a elenco o a griglia, ordinale e vedi le miniature. I server DLNA mostrano anche i dettagli musicali e le copertine.
- **Riproduci in streaming** audio e video. L'audio va nella coda del mini player; il video viene riprodotto a schermo intero. Il riavvolgimento funziona mentre un file è in streaming.
- **Scarica** i file sul tuo dispositivo. Selezionane diversi contemporaneamente per un download in blocco. I download appaiono in **Trasferimenti file** e finiscono nella tua cartella **Documenti**.
- **Info** su qualsiasi elemento ne mostra il tipo, la dimensione, la data, il percorso e i dettagli multimediali.

## Modificare i file su un server

Sui server che consentono la scrittura, ovvero **WebDAV, FTP, SFTP e SMB**, puoi anche gestire i file:

- **Nuova cartella**
- **Carica file** dal tuo dispositivo
- **Rinomina**, **Sposta** ed **Elimina** (un elemento o diversi contemporaneamente)

I server **DLNA** sono di sola lettura, quindi lì queste azioni non sono disponibili.

## Tenere traccia dei trasferimenti

I download e i caricamenti vengono eseguiti in background e compaiono in **Trasferimenti file**, che apri dall'angolo in alto a sinistra della scheda **Documenti**. Lì puoi seguire l'avanzamento e mettere in pausa, riprendere, riprovare, annullare o cancellare le attività. Puoi anche regolare i trasferimenti in [Impostazioni → Rete](/docs/guide/everdisk/everdisk-guide-settings) (solo Wi-Fi oppure Wi-Fi e dati cellulari, quanti eseguirne contemporaneamente e se devono continuare in background).

## Prossimi passi

- [File e documenti](/docs/guide/everdisk/everdisk-guide-files): gestisci tutto ciò che scarichi.
- [Foto, musica e video](/docs/guide/everdisk/everdisk-guide-media): riproduci ciò che trasmetti in streaming.
- [Impostazioni](/docs/guide/everdisk/everdisk-guide-settings): limiti di connessione e opzioni di trasferimento.
