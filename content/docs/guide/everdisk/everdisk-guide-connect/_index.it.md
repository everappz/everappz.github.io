---
title: "Collega i tuoi dispositivi"
date: 2026-08-20
description: "Istruzioni passo dopo passo per collegarti alla tua unità wireless Everdisk: guarda i contenuti su una smart TV tramite DLNA, apri i tuoi file in qualsiasi browser web, monta il tuo dispositivo come unità di rete in Finder, Windows o Linux tramite WebDAV, collega app per file tramite FTP e trasferisci tramite cavo USB verso un Mac senza Wi-Fi."
keywords: ["collegarsi a Everdisk", "streaming su TV DLNA", "aprire file nel browser", "montare unità di rete Finder", "WebDAV Windows Linux", "app per file FTP", "trasferimento via cavo USB Mac", "collegare iPhone al computer", "unità di rete iPhone"]
tags: ["everdisk", "guida", "collegamento"]
readingTime: 11
---


Una volta che tocchi **Avvia** nella schermata [Condivisione](/docs/guide/everdisk/everdisk-guide-sharing), gli altri dispositivi possono collegarsi ai tuoi file in quattro modi diversi. Scegli il metodo adatto al dispositivo che vuoi usare. In ogni caso, l'**indirizzo** esatto che ti serve è mostrato nella sezione **Come collegarsi** della schermata Condivisione.

> Entrambi i dispositivi devono essere sulla **stessa rete Wi-Fi**, oppure, per un Mac, collegati con un **cavo USB** (vedi l'ultima sezione).

## Guardare su una TV (DLNA)

Usa questo metodo per mostrare foto, video e musica su una smart TV o un lettore multimediale.

1. In **Impostazioni → Condivisione → Connessioni**, assicurati che **TV e Media Center** sia attivo (lo è per impostazione predefinita).
2. Nella schermata Condivisione, tocca **Avvia**.
3. Sulla tua TV, apri il lettore multimediale integrato o l'app media server (potrebbe chiamarsi Media Player, SmartShare, AllShare o simili).
4. Il tuo dispositivo appare nell'elenco dei media server con il suo nome (per esempio "Speedy-Hare"). Selezionalo.
5. Sfoglia le foto, i video e la musica condivisi e avvia la riproduzione. Le miniature di anteprima appaiono automaticamente.

Note:

- Il DLNA non può essere protetto da password, quindi questa connessione è aperta a chiunque sia sulla stessa rete Wi-Fi mentre è attiva.
- Se un video non viene riprodotto su una TV più vecchia, riduci la qualità del video in **Impostazioni → Condivisione → Video**, così Everdisk lo converte in un formato più compatibile.

## Aprire in un browser web (HTTP)

Usa questo metodo per passare i file a chiunque abbia un browser web, senza alcuna app da installare.

1. In **Impostazioni → Condivisione → Connessioni**, assicurati che **Browser** sia attivo.
2. Tocca **Avvia**.
3. Nella schermata Condivisione, copia l'indirizzo **Browser** (o mostra il suo codice QR).
4. Sull'altro telefono, tablet o computer, apri un qualsiasi browser web (Safari, Chrome, Edge, Firefox) e digita quell'indirizzo.
5. La pagina si apre con i tuoi file condivisi.

Nel browser l'altra persona può:

- Passare tra la vista a **elenco** e a **griglia** e ordinare per nome, data o dimensione.
- Vedere le **miniature** reali di foto, video, PDF e copertine musicali.
- Aprire una foto in una **galleria** a schermo intero con scorrimento, zoom con le dita e presentazione.
- Riprodurre la musica in un **lettore** integrato con coda, riproduzione casuale e ripetizione.
- **Scaricare** qualsiasi file, oppure scaricare un'intera cartella (o diversi elementi selezionati) come un unico **Archive.zip**.
- **Caricare** file di nuovo sul tuo dispositivo, ma solo se hai attivato **Modifica file** (vedi [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access)).

## Usarlo come unità di rete (WebDAV)

Usa questo metodo per far apparire il tuo dispositivo come un normale disco su un Mac, un PC Windows o una macchina Linux, così puoi trascinare i file in entrambe le direzioni.

**Su un Mac (Finder)**

1. In **Impostazioni → Condivisione → Connessioni**, assicurati che **Computer** sia attivo.
2. Tocca **Avvia** e prendi nota dell'indirizzo **Computer (WebDAV)**.
3. In Finder, scegli **Vai → Connessione al server** (oppure premi **⌘K**).
4. Digita l'indirizzo WebDAV esattamente come mostrato e fai clic su **Connetti**.
5. Inserisci il login e la password se ne hai impostati, altrimenti connettiti come ospite.
6. Il tuo dispositivo si apre come qualsiasi altra unità di rete. Trascina i file dentro o fuori.

**Su Windows**

1. Apri **Esplora file**, fai clic con il tasto destro su **Questo PC** e scegli **Aggiungi percorso di rete** (oppure connetti un'unità di rete).
2. Inserisci l'indirizzo WebDAV mostrato in Everdisk.
3. Inserisci il login e la password se ne hai impostati.

**Su Linux**

1. Apri il tuo gestore file e scegli **Connessione al server** (oppure usa `davs://` / `dav://`).
2. Inserisci l'indirizzo WebDAV mostrato in Everdisk.

Se la connessione è di sola lettura o bidirezionale dipende dall'impostazione **Modifica file**. Con essa attiva, puoi copiare i file sul tuo dispositivo e rinominarli o eliminarli; con essa disattivata, l'unità è di sola lettura.

## Collegare un'app per file (FTP)

Usa questo metodo per app di gestione e trasferimento file che parlano FTP (per esempio FileZilla o Cyberduck su un computer).

1. In **Impostazioni → Condivisione → Connessioni**, assicurati che **Altre app e dispositivi** sia attivo.
2. Tocca **Avvia** e prendi nota dell'indirizzo **FTP**.
3. Nella tua app FTP, aggiungi una nuova connessione usando quell'indirizzo.
4. Inserisci il login e la password se ne hai impostati, oppure lasciali vuoti per l'accesso anonimo.

## Trasferire tramite cavo USB (Mac, senza bisogno di Wi-Fi)

Usa questo metodo quando non c'è Wi-Fi, o quando vuoi il trasferimento più veloce e più privato. Funziona solo con un **Mac**.

1. Collega il tuo iPhone o iPad al Mac con il normale cavo di ricarica.
2. Se richiesto sul dispositivo, tocca **Autorizza questo computer**.
3. In Everdisk, tocca **Avvia**. Appare un avviso **Connessione veloce disponibile** e la schermata Condivisione mostra un indirizzo aggiuntivo con un badge **Connessione via cavo** che termina con `.local`.
4. Sul Mac, apri Finder → **Vai → Connessione al server** (**⌘K**) e inserisci quell'indirizzo `.local` (funziona sia per la connessione Browser sia per quella Computer).
5. Il tuo dispositivo si apre tramite il cavo, più veloce del Wi-Fi, e i dati non toccano mai il router o internet.

Note:

- Usa il **nome `.local`**, non un indirizzo IP (gli indirizzi IP funzionano solo via Wi-Fi), e mai `localhost`.
- Il percorso via cavo è **solo per Mac**. I PC Windows e i dispositivi Android devono usare il Wi-Fi.
- Puoi anche trascinare i file nella cartella di Everdisk usando Finder su un Mac, oppure l'app Dispositivi Apple (o iTunes) su Windows, tramite la condivisione file standard di iOS.

## Prossimi passi

- [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access): aggiungi una password, consenti i caricamenti, blocca un dispositivo.
- [Foto, musica e video](/docs/guide/everdisk/everdisk-guide-media): condividi tutta la tua libreria e imposta la qualità.
- [Collegati ai server](/docs/guide/everdisk/everdisk-guide-devices): raggiungi altri dispositivi da Everdisk.
