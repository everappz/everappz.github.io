---
title: "Come collegare il Synology NAS e ascoltare musica su iPhone o Mac"
date: 2024-09-19
description: "Scopri come collegare il tuo Synology NAS utilizzando l'API nativa o QuickConnect e riprodurre in streaming musica di alta qualità sul tuo iPhone o Mac con Evermusic e Flacbox."
keywords: ["synology nas", "streaming musica", "quickconnect", "evermusic synology", "flacbox synology", "lettore musicale nas", "musica iphone nas"]
tags: ["musica", "streaming", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Riepilogo:** Collega il tuo Synology NAS a Evermusic o Flacbox utilizzando l'API nativa di Synology -- manualmente tramite indirizzo IP o automaticamente tramite QuickConnect ID. QuickConnect ti permette di riprodurre musica in streaming da remoto senza port forwarding. Entrambe le app supportano FLAC, MP3, WAV e altri formati hi-res.

Se stai cercando un modo semplice per collegare il tuo Synology NAS e goderti la tua libreria musicale su iPhone o Mac, le app Evermusic e Flacbox sono le soluzioni perfette. Queste app supportano un'ampia gamma di formati audio, tra cui FLAC, MP3 e WAV, rendendo facile lo streaming e l'ascolto di musica di alta qualità direttamente dal tuo Synology NAS.

In questa guida, ti mostreremo come collegare il tuo Synology NAS all'app Evermusic o Flacbox utilizzando l'API nativa di Synology e la funzione QuickConnect. Sfruttando l'API diretta di Synology, puoi accedere in modo sicuro alla tua libreria musicale al di fuori della tua rete domestica senza necessità di configurazioni complicate come WebDAV, SMB, DLNA. Con QuickConnect, potrai riprodurre in streaming e gestire la tua musica da qualsiasi luogo, utilizzando il tuo iPhone o Mac.

## Passaggio 1: Configurare i permessi della cartella condivisa (Opzionale)

1. Apri il **Pannello di controllo** e vai alla sezione **Cartella condivisa**.

![Cartella condivisa](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Seleziona la cartella **Musica** e clicca su **Modifica**.

3. Nella scheda **Permessi**, configura i permessi. Abilita l'accesso ospite con sola lettura se hai solo bisogno di ascoltare musica, o lettura/scrittura se hai bisogno di modificare i file. Salva le modifiche.

![Permessi](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Passaggio 2: Trovare l'indirizzo IP del Synology NAS

1. Apri il **Pannello di controllo** e vai alla scheda **Interfaccia di rete**.

![Interfaccia di rete](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. Oppure usa il tuo browser web per visitare [find.synology.com](http://find.synology.com).

![Trova Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Annota l'indirizzo IP del tuo Synology NAS (es. 192.168.18.137).

## Passaggio 3: Trovare le porte di rete del Synology NAS

Puoi trovare la documentazione ufficiale di Synology per le porte di rete predefinite di DSM in questo [articolo del Centro conoscenza Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM utilizza le seguenti porte predefinite:
- **HTTP (Accesso Web):** Porta **5000**
- **HTTPS (Accesso Web sicuro):** Porta **5001**

Queste sono le porte predefinite per accedere all'interfaccia DSM.

![Porte di rete](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Passaggio 4: Abilitare la funzione QuickConnect ID

Un QuickConnect ID Synology è un identificatore univoco che ti permette di accedere al tuo Synology NAS da remoto tramite internet senza dover configurare impostazioni di rete complicate come il port forwarding. QuickConnect semplifica l'accesso remoto utilizzando i server di Synology per stabilire una connessione tra il tuo NAS e il tuo dispositivo, come lo smartphone o il computer, tramite il QuickConnect ID.

**Come trovare o configurare il tuo QuickConnect ID:**

1. **Accedi a DSM.**
2. Vai a **Pannello di controllo > Accesso esterno > QuickConnect**.
3. **Abilita QuickConnect** e crea o visualizza il tuo QuickConnect ID univoco.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Passaggio 5: Collegare il Synology NAS su iPhone/Mac usando Evermusic o Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) e [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) sono app di riproduzione musicale progettate per dispositivi iOS e macOS, ciascuna che offre funzionalità e capacità uniche per gestire e goderti la tua libreria musicale.

1. Apri l'app Evermusic o Flacbox e vai alla scheda **Connessioni**.

![Connessioni](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Scegli **Connetti un servizio cloud** e seleziona **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Hai due opzioni di connessione: **manuale** utilizzando l'indirizzo IP e la porta del server, o **automatica** tramite QuickConnect ID.

### Connessione manuale

Per il metodo manuale, avrai bisogno dell'indirizzo IP diretto e del numero di porta che hai ottenuto nei passaggi precedenti.

1. Inserisci l'URL del server ottenuto nel passaggio 2, utilizzando il seguente formato: PROTOCOLLO://INDIRIZZO_IP:NUMERO_PORTA
   - Usa la **porta 5000** per HTTP e la **porta 5001** per le connessioni HTTPS.

   Ad esempio:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. Il numero di porta effettivo può essere confermato nel passaggio 3 della configurazione.
3. Inserisci il tuo **nome utente** e la **password** per il Synology NAS.
4. Tocca **Accedi** per stabilire la connessione.

![Connessione manuale](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Connessione automatica

Per la connessione automatica, utilizzerai il **QuickConnect ID** dal passaggio 4. Invece di inserire manualmente l'indirizzo IP e il numero di porta del tuo Synology NAS, inserisci semplicemente il **QuickConnect ID**. L'app recupererà automaticamente le informazioni di connessione necessarie.

Questo metodo ti permette di accedere al tuo NAS da remoto, anche al di fuori della tua rete domestica, così puoi gestire i tuoi file da internet senza dover configurare il port forwarding o indirizzi IP statici.

![Connessione automatica](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autenticazione a due fattori

A partire da DSM 4.2, Synology ha introdotto la **verifica in 2 passaggi** per migliorare la sicurezza. Questa funzione richiede un codice **password monouso (OTP)**, generato da un'app di autenticazione, oltre alle normali credenziali di accesso. Se hai abilitato la verifica in 2 passaggi, dopo aver inserito nome utente e password, dovrai anche inserire l'OTP per accedere alla sessione DSM.

Tieni presente che una volta scaduta la sessione, l'app dovrà essere riautorizzata manualmente. Per riautorizzare:

1. Vai alla scheda **Connessioni** nell'app.
2. Tocca il pulsante **Altre azioni** accanto al nome del server.
3. Seleziona **Impostazioni** dal menu per inserire il nuovo codice di autenticazione e completare il processo di riautorizzazione.

Questo garantisce che anche se accedi al tuo NAS da una rete non affidabile, i tuoi dati rimangono sicuri.

## Passaggio 6: Navigare e riprodurre musica

1. Una volta connesso, il dispositivo apparirà nell'elenco **Dispositivi connessi**.

![Dispositivi connessi](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Naviga nella cartella **Musica** e tocca qualsiasi file audio per avviare la riproduzione.

![Riprodurre musica](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Passaggio 7: Aggiungere la cartella cloud connessa alla libreria musicale

1. Apri la sezione **Libreria musicale** nell'app.
2. Scegli **Aggiungi musica** e seleziona **Connessioni**.
3. Scegli il server NAS connesso e seleziona la cartella **Musica**. Tocca **Fatto**.
4. L'app scansionerà la cartella musicale e aggiungerà i file audio supportati alla libreria musicale. I metadati verranno caricati e i tuoi brani verranno raggruppati per album, artista e genere.

## Conclusione

Seguendo questi passaggi, puoi facilmente configurare una connessione sul tuo Synology NAS e riprodurre in streaming l'intera libreria musicale sul tuo iPhone o Mac usando Evermusic o Flacbox. Che tu sia a casa o in viaggio, goditi un accesso fluido e di alta qualità ai tuoi brani preferiti da qualsiasi luogo usando QuickConnect. Approfitta della flessibilità e della comodità che queste app offrono e inizia a gestire la tua collezione musicale con facilità su tutti i tuoi dispositivi.

Con l'accesso remoto sicuro tramite QuickConnect e il supporto per un'ampia gamma di formati audio, non sarai mai lontano dalla tua musica. Ora, i tuoi file archiviati sul NAS sono a portata di un tocco!

## FAQ

{{% details title="Qual è la differenza tra connessione manuale e QuickConnect?" closed="true" %}}
La connessione manuale utilizza l'indirizzo IP e la porta del NAS, che funziona sulla tua rete locale. QuickConnect utilizza il servizio di relay di Synology per stabilire una connessione da qualsiasi luogo tramite internet, senza port forwarding.
{{% /details %}}

{{% details title="Posso riprodurre in streaming musica dal Synology NAS al di fuori della mia rete domestica?" closed="true" %}}
Sì. Abilita QuickConnect sul tuo Synology NAS e usa il QuickConnect ID in Evermusic o Flacbox per riprodurre musica in streaming da qualsiasi luogo con una connessione internet.
{{% /details %}}

{{% details title="Quali formati audio sono supportati durante lo streaming dal Synology NAS?" closed="true" %}}
Evermusic e Flacbox supportano FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD e molti altri formati. Tutti i formati supportati funzionano durante lo streaming dal Synology NAS.
{{% /details %}}

{{% details title="Ho bisogno dell'autenticazione a due fattori per connettermi?" closed="true" %}}
No, l'autenticazione a due fattori è opzionale. Tuttavia, se hai abilitato la verifica in 2 passaggi sul tuo Synology DSM, l'app chiederà una password monouso durante l'accesso. Dovrai riautorizzare quando la sessione scade.
{{% /details %}}

{{% details title="Dovrei usare l'API nativa Synology, WebDAV o SMB per connettermi?" closed="true" %}}
L'API nativa Synology con QuickConnect è la scelta migliore per l'accesso remoto. Per l'uso sulla rete locale, SMB è tipicamente l'opzione più veloce. WebDAV funziona bene sia per l'accesso locale che remoto. Evermusic e Flacbox supportano tutti e tre i protocolli.
{{% /details %}}
