---
title: "Come collegare un archivio NAS tramite WebDAV e ascoltare musica su iPhone o Mac"
date: 2024-07-28
description: "Scopri come configurare WebDAV sul tuo Synology NAS e riprodurre musica in streaming su iPhone o Mac usando Evermusic o Flacbox. Segui la nostra guida passo dopo passo."
keywords: ["collegare nas", "webdav synology", "streaming musica nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["musica", "streaming", "archiviazione", "nas", "collegare", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**In breve:** Installa e abilita WebDAV sul tuo Synology NAS, configura i permessi della cartella condivisa, quindi connettiti da Evermusic o Flacbox usando l'indirizzo IP del NAS e la porta WebDAV (predefinita 5005/5006). Puoi riprodurre in streaming e gestire l'intera libreria musicale senza copiare file sul tuo dispositivo.

Scopri come collegare il tuo archivio NAS tramite WebDAV e riprodurre in streaming la tua libreria musicale su iPhone o Mac senza sforzo. WebDAV (Web-based Distributed Authoring and Versioning) è un protocollo che ti permette di gestire e condividere file su Internet. Configurando WebDAV sul tuo NAS, puoi accedere alla tua collezione musicale e riprodurla in streaming, assicurandoti di avere sempre i tuoi brani preferiti a portata di mano.

In questa guida, ti mostreremo come configurare una connessione WebDAV su uno dei server NAS più popolari, Synology NAS. Segui i nostri semplici passaggi per configurare WebDAV sul tuo Synology NAS, e potrai sfogliare, riprodurre in streaming e gestire la tua libreria musicale direttamente dal tuo iPhone o Mac.

## Passo 1: Installare WebDAV su Synology NAS

1. Accedi al tuo Synology NAS e apri il **Centro pacchetti**.
2. Cerca "webdav" e installa il pacchetto WebDAV se non è già installato. Apri il server WebDAV per configurarlo.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Installare WebDAV su Synology" width="600" >}}

## Passo 2: Configurare il server WebDAV

1. Nella pagina delle impostazioni WebDAV, seleziona le caselle per **Abilita HTTP**, **Abilita HTTPS**, **Abilita WebDAV anonimo** e **Abilita DavDepthInfinity**.
2. Clicca su **Applica** per salvare le modifiche. Annota i numeri di porta per le connessioni HTTP e HTTPS, che sono 5005 e 5006 per impostazione predefinita.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurare le impostazioni WebDAV" width="600" >}}

## Passo 3: Configurare i permessi della cartella condivisa

1. Apri il **Pannello di controllo** e vai alla sezione **Cartella condivisa**.
2. Seleziona la cartella **Musica** e clicca su **Modifica**.
3. Nella scheda **Permessi**, configura i permessi. Abilita l'accesso ospite con Sola lettura se hai solo bisogno di ascoltare musica, o Lettura/Scrittura se devi modificare file. Salva le modifiche.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permessi della cartella condivisa" width="600" >}}

## Passo 4: Trovare l'indirizzo IP del Synology NAS

1. Apri il **Pannello di controllo** e vai alla scheda **Interfaccia di rete**, o usa il tuo browser web per visitare [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Trovare l'indirizzo IP del NAS" width="600" >}}

2. Annota l'indirizzo IP del tuo Synology NAS (es. 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Indirizzo IP del Synology NAS" width="600" >}}

## Passo 5: Connettersi al Synology NAS con Evermusic/Flacbox

1. Apri l'app Evermusic o Flacbox e vai alla scheda **Connessioni**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Scheda Connessioni in Evermusic" width="600" >}}

2. Per la connessione automatica, trova il tuo Synology NAS nella sezione **Dispositivi disponibili** e toccalo per connetterti.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista dei dispositivi disponibili" width="600" >}}

3. Per la connessione manuale, scegli **Connetti un servizio cloud** e seleziona **WebDAV**. Inserisci l'indirizzo del server nel formato: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (es. [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configurazione manuale di WebDAV" width="600" >}}

4. Lascia i campi login e password vuoti per l'accesso ospite, o inserisci le tue credenziali Synology. Tocca **Accedi**.

## Passo 6: Navigare e riprodurre musica

1. Una volta connesso, il dispositivo apparirà nell'elenco **Accessori connessi**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Dispositivi connessi in Evermusic" width="600" >}}

2. Naviga alla cartella **Musica** e tocca qualsiasi file audio per avviare la riproduzione.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Esplorare la cartella Musica" width="600" >}}

## Passo 7: Aggiungere la cartella cloud connessa alla libreria musicale

1. Apri la sezione **Libreria musicale** nell'app.
2. Scegli **Aggiungi musica** e seleziona **Connessioni**.
3. Scegli il server NAS connesso e seleziona la cartella **Musica**. Tocca **Fatto**.
4. L'app eseguirà la scansione della cartella musicale e aggiungerà i file audio supportati alla libreria musicale. I metadati verranno caricati e i tuoi brani saranno raggruppati per album, artista e genere.

## Conclusione

Seguendo questi passaggi, puoi facilmente configurare una connessione WebDAV sul tuo Synology NAS e riprodurre in streaming la tua libreria musicale su iPhone o Mac usando Evermusic o Flacbox. Goditi un accesso fluido ai tuoi brani preferiti in qualsiasi momento.

## FAQ

{{% details title="Quali dispositivi NAS supportano WebDAV?" closed="true" %}}
La maggior parte dei marchi NAS popolari supporta WebDAV, inclusi Synology, QNAP, TrueNAS e Western Digital. Consulta la documentazione del produttore del tuo NAS per le istruzioni di configurazione di WebDAV.
{{% /details %}}

{{% details title="Qual è la differenza tra WebDAV e SMB per lo streaming musicale dal NAS?" closed="true" %}}
WebDAV funziona tramite HTTP/HTTPS ed è più adatto per l'accesso remoto via Internet. SMB è tipicamente più veloce sulle reti locali. Evermusic e Flacbox supportano entrambi i protocolli, quindi scegli in base alla necessità di accesso locale o remoto.
{{% /details %}}

{{% details title="Ho bisogno di nome utente e password per WebDAV su Synology?" closed="true" %}}
No, se abiliti l'accesso anonimo WebDAV e configuri i permessi ospite sulla cartella condivisa. Per una maggiore sicurezza, puoi utilizzare le tue credenziali Synology.
{{% /details %}}

{{% details title="Posso riprodurre in streaming FLAC e altri formati ad alta risoluzione dal NAS tramite WebDAV?" closed="true" %}}
Sì. Sia Evermusic che Flacbox supportano FLAC, ALAC, WAV, DSD e altri formati ad alta risoluzione durante lo streaming dall'archivio NAS tramite WebDAV.
{{% /details %}}

{{% details title="Perché l'app non riesce a trovare il mio NAS nei Dispositivi disponibili?" closed="true" %}}
Assicurati che il tuo iPhone/Mac e il NAS siano sulla stessa rete Wi-Fi. Se il rilevamento automatico non funziona, usa l'opzione di connessione manuale e inserisci direttamente l'indirizzo IP del NAS e la porta WebDAV.
{{% /details %}}
