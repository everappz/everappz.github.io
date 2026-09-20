---
title: "Come configurare un server WebDAV su iPhone e iPad per l'accesso e la condivisione dei file"
description: "Trasforma iPhone o iPad in un server WebDAV con Everdisk e montalo come disco di rete su Finder di Mac, Esplora file di Windows, Linux, Android o un altro iPhone via Wi-Fi. Configurazione completa, l'indirizzo e la porta WebDAV, e la connessione passo passo per ogni dispositivo."
date: 2026-09-19
tags: ["everdisk", "webdav", "disco di rete", "condivisione file", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["server WebDAV iPhone", "server WebDAV iPad", "come configurare WebDAV su iPhone", "montare iPhone come disco di rete", "collegare iPhone WebDAV Mac Finder", "WebDAV Esplora file Windows iPhone", "disco di rete iphone Windows", "WebDAV Linux iPhone", "accedere ai file iPhone dal computer", "webdav iphone a iphone", "condividere file iPhone WebDAV", "mappare disco di rete iphone", "trasferire file iphone webdav", "indirizzo porta webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV trasforma una cartella in un disco di rete che un computer può aprire nel suo normale gestore file. Gira sullo stesso protocollo web che usa il tuo browser, ed è per questo che viaggia bene tra Mac, Windows e Linux senza driver speciali. Con [Everdisk](/products/everdisk) puoi eseguire un server WebDAV sul tuo iPhone o iPad, così il telefono compare come un disco che puoi sfogliare, da cui copiare e su cui copiare da quasi qualsiasi computer.

WebDAV è la scelta migliore quando c'è di mezzo Windows, perché Esplora file di Windows si collega ad esso in modo pulito. Questa guida copre la configurazione e come collegarti da un Mac, Windows, Linux, Android e un secondo iPhone.

## Cosa ti serve

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installato.
- Un computer o un altro dispositivo sulla **stessa rete Wi-Fi**.
- I file che vuoi condividere, nella cartella Documenti di Everdisk o nelle cartelle che aggiungi.

## Configura il server WebDAV in Everdisk

### Passo 1: scegli cosa condividere e imposta l'accesso

Apri Everdisk, vai alla scheda **Condivisione** e tocca **Cosa condividere**. La cartella Documenti è condivisa per impostazione predefinita. Aggiungine altre con **Aggiungi cartella** e **Aggiungi file**.

Apri **Impostazioni**, poi **Condivisione**, poi **Accesso**. Attiva **Modifica dei file** se vuoi che i computer collegati possano copiare file sul tuo telefono e rinominarli o eliminarli, o disattivala per un disco di sola lettura. Imposta qui un **Login** e una **Password** se vuoi un accesso, oppure lasciali vuoti per l'accesso ospite.

### Passo 2: attiva il server WebDAV

Vai su **Impostazioni**, poi **Condivisione**, poi **Connessioni**, e attiva **Computer**. Quello è il server WebDAV (porta il tag WebDAV).

### Passo 3: avvia la condivisione e annota l'indirizzo

Torna alla scheda **Condivisione** e tocca **Avvia**. La sezione **Come collegarsi** mostra l'indirizzo WebDAV. Ha questo aspetto:

```
http://192.168.1.20:8080
```

Il numero dopo i due punti è la **porta**, che è **8080** per impostazione predefinita. La prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi il tuo sarà diverso. Tieni Everdisk aperto sullo schermo mentre un dispositivo è collegato.

## Collegarsi da un Mac

1. Apri **Finder**, scegli **Vai**, poi **Connessione al server** (o premi **Command e K**).
2. Digita l'indirizzo WebDAV mostrato in Everdisk, per esempio `http://192.168.1.20:8080`.
3. Clicca **Connetti**, poi scegli **Ospite** o inserisci il tuo **Login** e la tua **Password**.

Il tuo iPhone si apre in una finestra del Finder e si comporta come una normale cartella. Copia i file in entrambe le direzioni se Modifica dei file è attiva.

## Collegarsi da Windows

Windows ha un client WebDAV integrato, quindi funziona da Esplora file.

1. Apri **Esplora file**, fai clic destro su **Questo PC** nella barra laterale e scegli **Aggiungi percorso di rete** (puoi anche usare **Connetti unità di rete**).
2. Quando ti viene chiesto l'indirizzo, digita lo stesso indirizzo WebDAV da Everdisk, per esempio `http://192.168.1.20:8080`, poi clicca **Avanti**.
3. Inserisci il tuo **Login** e la tua **Password** se ne hai impostati.

Il dispositivo compare quindi sotto Questo PC come un percorso di rete che puoi aprire e da cui copiare file. Se Windows si rifiuta di connettersi la prima volta, assicurati che il servizio **WebClient** sia in esecuzione (cerca Servizi nel menu Start, trova WebClient e impostalo su avvio), poi riprova.

## Collegarsi da Linux

1. Apri il tuo gestore file e scegli **Connessione al server** o **Altre posizioni**.
2. Inserisci l'indirizzo con un prefisso WebDAV, per esempio `dav://192.168.1.20:8080` (usa `davs://` solo se hai configurato il TLS).
3. Collegati come ospite oppure inserisci il tuo login.

## Collegarsi da Android

Android non ha un browser WebDAV di sistema, quindi usa un gestore file che lo supporti:

1. Installa un'app come **Solid Explorer** o **CX File Explorer**.
2. Aggiungi una nuova connessione **WebDAV**.
3. Inserisci l'host e la **porta 8080**, scegli lo schema `http` e aggiungi il tuo login se ne hai impostato uno.

## Collegarsi da un altro iPhone o iPad

L'app File di iOS non include un client WebDAV, quindi usa una di queste:

- **La scheda Dispositivi di Everdisk.** Sul secondo dispositivo, apri Everdisk, vai su **Dispositivi**, tocca **Nuova connessione**, scegli **WebDAV** e inserisci l'indirizzo, per esempio `http://192.168.1.20:8080`. È la via più semplice e non richiede nulla in più.
- **Un'app WebDAV** come Documents di Readdle, che può aggiungere una connessione WebDAV con lo stesso indirizzo e login.

## Preferisci un link rapido invece di un disco?

Se ti serve solo prendere velocemente un file e non vuoi montare alcun disco, attiva la connessione **Browser** in Impostazioni, Condivisione, Connessioni. Everdisk ti fornisce quindi un indirizzo web che puoi aprire in qualsiasi browser su qualsiasi dispositivo per sfogliare e scaricare i tuoi file. È il modo più veloce per passare un file a un PC Windows, un Chromebook o al telefono di un amico.

## Sola lettura o lettura e scrittura

L'interruttore **Modifica dei file** in Impostazioni, Condivisione, Accesso decide questo. Attivo significa che i computer collegati possono caricare, rinominare ed eliminare. Disattivo significa che il disco è di sola lettura, quindi gli altri possono vedere e copiare i tuoi file ma non cambiarli.

## Modi reali in cui le persone lo usano

- **Copiare file sul tuo iPhone da un PC Windows** mappandolo come percorso di rete e trascinandoli attraverso.
- **Scaricare foto e documenti su un portatile** usando il gestore file che già conosci, senza cavo e senza iTunes.
- **Modificare un documento in loco** dal tuo Mac, aprendolo direttamente dal telefono e risalvandolo.
- **Spostare una cartella tra un iPhone e un iPad** usando la scheda Dispositivi di Everdisk sul dispositivo ricevente.

## Qualche consiglio

- Tieni Everdisk aperto mentre un dispositivo è collegato. Bloccare il telefono a lungo può mettere in pausa l'app.
- Su Windows, se la connessione fallisce, avvia il servizio WebClient e riprova con l'indirizzo.
- WebDAV e SMB si montano entrambi come dischi di rete. Usa WebDAV quando è coinvolto Windows, e [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) quando vuoi la velocità del Finder e la cifratura.
- Per i trasferimenti più veloci, mantieni la qualità di foto e video su Originale nelle Impostazioni.

## Domande frequenti

{{% details title="Qual è l'indirizzo e la porta WebDAV del mio iPhone?" closed="true" %}}
Dopo aver avviato la condivisione, Everdisk mostra l'indirizzo nella schermata Condivisione. Ha l'aspetto http://192.168.1.20:8080. Il 8080 è la porta che Everdisk usa per WebDAV, e la prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi il tuo sarà diverso.
{{% /details %}}

{{% details title="Come mi collego al WebDAV del mio iPhone da Windows?" closed="true" %}}
Apri Esplora file, fai clic destro su Questo PC e scegli Aggiungi percorso di rete o Connetti unità di rete. Inserisci l'indirizzo WebDAV da Everdisk, per esempio http://192.168.1.20:8080, poi inserisci il tuo login se ne hai impostato uno. Se Windows non si connette, assicurati che il servizio WebClient sia in esecuzione (cerca Servizi, trova WebClient, avvialo) e riprova.
{{% /details %}}

{{% details title="Posso usare WebDAV tra due iPhone?" closed="true" %}}
Sì, ma l'app File di iOS non ha un client WebDAV, quindi usa Everdisk sul secondo dispositivo. Apri la scheda Dispositivi, tocca Nuova connessione, scegli WebDAV e inserisci l'indirizzo mostrato sul primo telefono. Funziona anche un'app WebDAV come Documents di Readdle.
{{% /details %}}

{{% details title="WebDAV richiede una password?" closed="true" %}}
No, il login è facoltativo. Lascia vuoti Login e Password in Impostazioni, Condivisione, Accesso per l'accesso ospite, oppure impostali se vuoi che le connessioni accedano.
{{% /details %}}

{{% details title="Altre persone possono modificare i miei file via WebDAV?" closed="true" %}}
Solo se lo consenti. L'interruttore Modifica dei file in Impostazioni, Condivisione, Accesso controlla questo. Attivo permette ai dispositivi collegati di caricare, rinominare ed eliminare. Disattivo rende il disco di sola lettura, quindi gli altri possono vedere e copiare ma non cambiare nulla.
{{% /details %}}

{{% details title="WebDAV o SMB, qual è la differenza?" closed="true" %}}
Entrambi montano il tuo iPhone come un disco di rete. WebDAV gira sul protocollo web e si collega in modo pulito da Esplora file di Windows, che è il suo punto di forza principale. SMB è la condivisione file nativa su Mac, Linux e dispositivi NAS, di solito è più veloce su un Mac, ed è l'unica connessione di Everdisk che può cifrare i trasferimenti. Everdisk può eseguirli entrambi contemporaneamente.
{{% /details %}}

{{% details title="Perché il mio disco WebDAV si disconnette?" closed="true" %}}
Il tuo iPhone è il server, e iOS mette in pausa le app che restano troppo a lungo in background. Tieni Everdisk aperto sullo schermo mentre un dispositivo è collegato, e collegalo all'alimentazione per i trasferimenti lunghi. Verifica anche che entrambi i dispositivi siano ancora sulla stessa rete Wi-Fi.
{{% /details %}}

{{% details title="Posso collegarmi via WebDAV senza Wi-Fi?" closed="true" %}}
Sì, se colleghi il tuo iPhone a un Mac con un cavo. Everdisk mostra allora un indirizzo di connessione via cavo aggiuntivo che il Mac collegato può aprire in Finder, che funziona anche senza alcun Wi-Fi. Sul cavo, solo quel Mac può raggiungere il dispositivo.
{{% /details %}}

{{% details title="Everdisk è gratis?" closed="true" %}}
Sì, Everdisk si scarica gratis e il server WebDAV è incluso. Un acquisto Premium opzionale una tantum aggiunge extra come le porte personalizzate e la conversione di foto e video. Puoi configurare WebDAV e condividere file senza pagare.
{{% /details %}}

Pronto a provarlo? [Scarica Everdisk dall'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e monta il tuo iPhone come disco in un paio di minuti. Domande o feedback? Scrivici a **support@everappz.com**.
