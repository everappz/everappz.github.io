---
title: "Come trasferire la tua libreria musicale tra dispositivi in Evermusic: guida passo dopo passo"
description: "Trasferisci facilmente la tua libreria musicale Evermusic, playlist, copertine degli album e impostazioni da un iPhone, iPad o Mac a un altro usando Wi-Fi Drive e strumenti di backup."
date: 2024-12-29
tags: ["libreria musicale", "trasferimento", "wifi", "backup", "webdav", "ripristino"]
keywords: ["trasferire libreria musicale Evermusic", "backup e ripristino playlist Evermusic", "Evermusic WiFi Drive", "sincronizzare Evermusic tra dispositivi", "spostare database Evermusic", "trasferimento file Evermusic", "ripristinare impostazioni lettore audio", "trasferimento musica WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**In breve:** Per trasferire la tua libreria Evermusic su un nuovo dispositivo, crea un backup sul dispositivo sorgente, avvia Wi-Fi Drive, collega il secondo dispositivo sulla stessa rete, scarica il backup e i file musicali, poi ripristina dal backup. L'intero processo richiede circa 10 minuti a seconda della dimensione della libreria.

In questa guida, ti accompagneremo nel trasferimento dell'intera libreria musicale — inclusi database, copertine degli album e impostazioni — da un dispositivo (iPhone o Mac) a un altro. Mentre la sincronizzazione automatica della libreria musicale e delle playlist è una funzionalità prevista per il futuro, questo processo deve attualmente essere eseguito manualmente.

## Passaggio 1: Creare un backup sul primo dispositivo

1. **Apri l'app sul tuo primo dispositivo** (quello con la tua libreria musicale, playlist e servizi cloud collegati).
2. **Vai alle Impostazioni** e seleziona l'opzione **Backup e ripristino**.

![Backup e ripristino](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. Nella schermata **Backup e ripristino**, scegli gli elementi da includere nel file di backup:
   - **Database** (include la tua libreria musicale e le playlist)
   - **Copertine degli album**
   - **Impostazioni**

Queste opzioni sono abilitate per impostazione predefinita.

![Opzioni di backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Tocca **Backup dei dati dell'applicazione** per avviare il processo.

![Backup dei dati dell'applicazione](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Una volta completato il backup, apparirà un avviso informativo.

![Backup completato](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Tocca **Mostra file** per rivelare il file di backup nella directory **Documenti**. I file di backup vengono solitamente salvati nella cartella **Backup**.

![Mostra file di backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Passaggio 2: Avviare il server Wi-Fi Drive

1. Vai alla sezione **Connessioni** nell'app.
2. Scorri verso il basso fino a **Connetti tramite Wi-Fi** e toccalo.

![Connetti tramite Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. Nella schermata successiva, tocca **Avvia Wi-Fi Drive**.

- Facoltativamente, puoi impostare un nome utente e una password per la sicurezza, ma non è necessario per le reti domestiche.

4. Una volta avviato, vedrai gli indirizzi del server disponibili. Questo può essere utilizzato per browser desktop o app WebDAV, ma in questa guida procederemo direttamente ai passaggi successivi.

![Wi-Fi Drive avviato](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Passaggio 3: Collegare il secondo dispositivo al primo

1. Apri l'app sul secondo dispositivo (dove vuoi trasferire la libreria).
2. Assicurati che entrambi i dispositivi siano collegati alla stessa rete Wi-Fi.
3. Sul secondo dispositivo, apri la scheda **Connessioni** e seleziona **Dispositivi disponibili**.

![Dispositivi disponibili](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Dovresti vedere una connessione WebDAV chiamata **Evermusic** (il server che abbiamo avviato sul primo dispositivo). Toccala per connetterti.

5. Una volta connesso, vedrai tutte le cartelle dal primo dispositivo.

![Connesso al primo dispositivo](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Passaggio 4: Preparazione per il trasferimento dei file

1. Sul secondo dispositivo, vai in **Impostazioni > Gestore file** e abilita **Salva file scaricati in - Chiedi ogni volta**.

- Questo assicura che puoi selezionare la cartella di destinazione per ogni download.

2. Torna alla scheda **Connessioni** e naviga verso il server WebDAV collegato.

![Preparazione per il trasferimento dei file](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Passaggio 5: Trasferire backup e file musicali

1. Apri la cartella **Backup** sul server WebDAV collegato.

![Cartella backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Tocca il pulsante **Altre azioni** (tre punti) vicino al file di backup e seleziona **Scaricare**.

3. Crea una cartella **Backup** sul secondo dispositivo per memorizzare i file scaricati. Conferma la selezione toccando **Fatto**.

![Scarica backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Trasferisci eventuali file musicali aggiuntivi:
   - Controlla la cartella **Scaricare** o altre cartelle pertinenti sul server WebDAV.

![Trasferimento file musicali](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Usa l'opzione **Selezionare** per scegliere i file, poi tocca **Altre azioni > Scaricare**. Salvali nella cartella corrispondente sul secondo dispositivo per mantenere la stessa struttura di directory.

L'obiettivo è trasferire tutti i file dal primo dispositivo al dispositivo attuale, assicurandosi che la struttura delle cartelle rimanga identica. In questo modo, i collegamenti nella libreria musicale e nelle playlist rimangono intatti. Nota che i file locali memorizzati al di fuori della directory Documenti dell'app sul primo dispositivo devono essere trasferiti separatamente. Poiché l'app non può accedere a questi file in modalità Wi-Fi Drive, dovrai utilizzare l'app File di sistema per il loro trasferimento.

![Trasferimento completato](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Passaggio 6: Monitorare il progresso del trasferimento

1. Sul secondo dispositivo, vai alla sezione **File locali** (o scheda **Scaricare** su iPad/Mac).

2. Tocca il pulsante **Attività di trasferimento** nell'angolo in alto a sinistra per monitorare la coda di trasferimento.

![Monitorare trasferimento](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Passaggio 7: Ripristinare i dati dal backup

1. Una volta che il file di backup e tutti i file audio necessari sono stati scaricati sul secondo dispositivo, apri la cartella **Backup**.

2. Tocca il file di backup e apparirà un messaggio di conferma.

![Ripristina backup](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Nota:** Il ripristino sostituirà tutti i dati attuali della libreria musicale, le playlist, le impostazioni e le copertine degli album con i dati del backup.

3. Tocca **Ripristina** per avviare il processo.

![Processo di ripristino](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Dopo il completamento del ripristino, un avviso confermerà il successo.

![Ripristino completato](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Controlla le sezioni **Playlist** o **Libreria musicale** per verificare il ripristino.

![Verifica ripristino](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Passaggio 8: Reindicizzare la libreria musicale

1. Per risultati ottimali, reindicizza la tua libreria per assicurarti che tutti i file vengano rilevati con successo.

2. Vai in **Impostazioni > Libreria musicale > Sincronizzazione musica offline** e seleziona **Avvia scansione cartelle locali**.

Seguendo questi passaggi, trasferirai con successo la tua libreria musicale, le playlist e le impostazioni su un altro dispositivo. Se riscontri problemi, non esitare a contattare il supporto.

## Domande frequenti

{{% details title="Posso trasferire la mia libreria Evermusic senza Wi-Fi?" closed="true" %}}
Wi-Fi Drive richiede che entrambi i dispositivi siano sulla stessa rete Wi-Fi. Attualmente non esiste un'opzione di trasferimento Bluetooth o cellulare. In alternativa, puoi usare AirDrop o l'app File per spostare manualmente il file di backup e le cartelle musicali tra i dispositivi.
{{% /details %}}

{{% details title="Le connessioni ai servizi cloud verranno trasferite con il backup?" closed="true" %}}
Il backup include il database, le playlist, le copertine degli album e le impostazioni. Le credenziali di accesso ai servizi cloud non sono incluse per motivi di sicurezza. Dovrai ricollegare i tuoi account cloud sul nuovo dispositivo dopo il ripristino.
{{% /details %}}

{{% details title="Cosa succede alla mia libreria esistente sul secondo dispositivo?" closed="true" %}}
Il ripristino di un backup sostituisce tutti i dati esistenti della libreria musicale, le playlist, le impostazioni e le copertine degli album sul secondo dispositivo. Fai un backup separato del secondo dispositivo prima se vuoi conservare i suoi dati.
{{% /details %}}

{{% details title="Questo processo funziona tra iPhone e Mac?" closed="true" %}}
Sì. Evermusic supporta il trasferimento Wi-Fi Drive tra qualsiasi combinazione di iPhone, iPad e Mac. Entrambi i dispositivi devono solo essere sulla stessa rete Wi-Fi.
{{% /details %}}

{{% details title="Quanto tempo richiede il trasferimento?" closed="true" %}}
Il tempo di trasferimento dipende dalla dimensione della tua libreria musicale e dalla velocità del Wi-Fi. Una libreria tipica di pochi gigabyte viene trasferita in 5-15 minuti su una rete domestica standard.
{{% /details %}}
