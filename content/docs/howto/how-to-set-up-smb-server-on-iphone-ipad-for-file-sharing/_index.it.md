---
title: "Come configurare un server SMB su iPhone e iPad per la condivisione dei file"
description: "Trasforma iPhone o iPad in un server file SMB con Everdisk e aprilo come un disco di rete da un Mac, un altro iPhone, Linux o Android via Wi-Fi. Configurazione completa, l'indirizzo e la porta smb, la cifratura SMB3 opzionale e la connessione passo passo per ogni dispositivo."
date: 2026-09-19
tags: ["everdisk", "smb", "condivisione file", "disco di rete", "iphone", "ipad", "mac", "finder", "cifratura", "wifi"]
keywords: ["server SMB iPhone", "server SMB iPad", "come configurare SMB su iPhone", "condivisione SMB iPhone", "collegare iPhone SMB Mac Finder", "smb iphone a iphone", "app File iOS connessione al server SMB", "condividere file iPhone SMB", "disco di rete iPhone Finder", "cifratura SMB3 iOS", "condivisione smb iPhone Android", "collegarsi a SMB da Linux", "iphone come disco di rete", "condividere file tra iphone wifi", "mappare iphone come disco di rete"]
readingTime: 10
---

{{< author-byline >}}

SMB è la condivisione file integrata in macOS, Windows e Linux, e in quasi tutti i dischi di rete (NAS). Quando ti colleghi a una cartella condivisa su un altro computer e questa si apre come un normale disco in Finder o in Esplora file, è SMB a fare il lavoro. Con [Everdisk](/products/everdisk) puoi mettere una condivisione SMB sul tuo iPhone o iPad, così il telefono stesso compare come un disco di rete che gli altri dispositivi sfogliano, da cui copiano e su cui copiano.

È l'opzione a cui ricorrere quando vuoi che il tuo iPhone si comporti come un vero disco, non come una pagina web. È veloce, trascina e rilascia in entrambe le direzioni, ed è l'unico tipo di connessione in Everdisk che può cifrare ogni trasferimento. Questa guida copre la configurazione e come collegarti da un Mac, un altro iPhone o iPad, Linux, Android e Windows.

## Cosa ti serve

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installato.
- Un altro dispositivo sulla **stessa rete Wi-Fi**.
- I file che vuoi condividere, nella cartella Documenti di Everdisk o nelle cartelle che aggiungi.

## Configura il server SMB in Everdisk

### Passo 1: scegli cosa condividere e chi può scrivere

Apri Everdisk, vai alla scheda **Condivisione** e tocca **Cosa condividere**. La cartella Documenti è condivisa per impostazione predefinita. Aggiungine altre con **Aggiungi cartella** e **Aggiungi file**, e attiva la tua libreria Foto o Musica se vuoi renderle disponibili anche quelle.

Decidi se gli altri dispositivi possono solo leggere i tuoi file, o anche modificarli. Apri **Impostazioni**, poi **Condivisione**, poi **Accesso**, e imposta **Modifica dei file**. Con questa attiva, i dispositivi collegati possono copiare file sul tuo telefono e rinominarli o eliminarli. Con questa disattivata, la condivisione è di sola lettura.

Se vuoi un login, imposta un **Login** e una **Password** nella stessa schermata Accesso. Lascia entrambi vuoti per consentire l'accesso ospite.

### Passo 2: attiva il server SMB

Vai su **Impostazioni**, poi **Condivisione**, poi **Connessioni**, e attiva **Computer (avanzate)**. Quello è il server SMB (porta il tag SMB).

### Passo 3: avvia la condivisione e annota l'indirizzo

Torna alla scheda **Condivisione** e tocca **Avvia**. La sezione **Come collegarsi** mostra ora l'indirizzo SMB. Ha questo aspetto:

```
smb://192.168.1.20:4455/Share
```

Tre cose da sapere su quell'indirizzo:

- Il numero dopo i due punti è la **porta**. Everdisk usa **4455** per impostazione predefinita.
- La condivisione si chiama **Share**.
- La prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi sarà diverso sulla tua rete.

Tieni Everdisk aperto mentre i dispositivi sono collegati, perché iOS mette in pausa le app che restano troppo a lungo in background.

## Collegarsi da un Mac

È il caso più fluido, perché macOS parla SMB in modo nativo.

Il modo più rapido: apri **Finder** e guarda nella barra laterale sotto **Posizioni** o **Rete**. Everdisk si annuncia sul Wi-Fi, quindi il tuo iPhone spesso compare lì da solo. Cliccaci, poi clicca **Connetti come** e scegli **Ospite**, oppure inserisci il tuo login.

Per collegarti manualmente:

1. In Finder, scegli **Vai**, poi **Connessione al server** (o premi **Command e K**).
2. Digita l'indirizzo SMB mostrato in Everdisk, per esempio `smb://192.168.1.20:4455/Share`.
3. Clicca **Connetti**, poi scegli **Ospite** o inserisci il tuo **Login** e la tua **Password**.

Il tuo iPhone si apre in una finestra del Finder. Copia i file dentro o fuori trascinandoli, esattamente come con qualsiasi altro disco (se Modifica dei file è attiva).

## Collegarsi da un altro iPhone o iPad

iOS e iPadOS possono aprire le condivisioni SMB nell'app **File** integrata, il che rende i trasferimenti da telefono a telefono puliti e rapidi.

Sul secondo dispositivo:

1. Apri l'app **File**.
2. Tocca il pulsante **altro** (i tre puntini, in alto a destra su iPhone) e scegli **Connessione al server**.
3. Inserisci l'indirizzo SMB da Everdisk, per esempio `smb://192.168.1.20:4455/Share`.
4. Scegli **Ospite**, oppure **Utente registrato** e inserisci il tuo login.
5. La condivisione compare sotto Posizioni in File. Sfoglia e copia in entrambe le direzioni.

Puoi anche usare la scheda **Dispositivi** di Everdisk sul secondo dispositivo, che include un client SMB. Apri Everdisk, vai su **Dispositivi**, tocca **Nuova connessione**, scegli **SMB** e inserisci l'indirizzo.

## Collegarsi da Linux

1. Apri il tuo gestore file (File/Nautilus su GNOME, Dolphin su KDE).
2. Scegli **Altre posizioni** o **Connessione al server**.
3. Inserisci l'indirizzo, per esempio `smb://192.168.1.20:4455/Share`.
4. Collegati come ospite, oppure inserisci il tuo login.

Da un terminale puoi anche eseguire `smbclient //192.168.1.20/Share -p 4455` e inserire il tuo login quando richiesto.

## Collegarsi da Android

Android non ha un browser SMB di sistema, quindi usa un gestore file che supporti SMB:

1. Installa un'app come **CX File Explorer**, **Solid Explorer** o **X-plore File Manager**.
2. Aggiungi una nuova connessione **SMB** o **LAN**.
3. Inserisci l'host (l'indirizzo Wi-Fi del tuo iPhone), imposta la **porta su 4455** e il nome della condivisione **Share**.
4. Collegati come ospite o con il tuo login, poi sfoglia e copia.

## Collegarsi da Windows

Windows può leggere le condivisioni SMB, con un particolare che vale la pena conoscere in anticipo. Esplora file integrato parla SMB solo sulla porta standard e non ti permette di digitare una porta personalizzata nel percorso, ed Everdisk usa la porta 4455. Quindi la semplice via **Connetti unità di rete** spesso non riesce a raggiungerlo.

Su Windows hai due buone opzioni:

- Usa un gestore file o un client SMB che ti permetta di impostare una porta personalizzata, e puntalo all'indirizzo del tuo iPhone con la porta **4455** e il nome della condivisione **Share**.
- Oppure collegati da Windows usando uno degli altri server di Everdisk. La [configurazione WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) e la [configurazione FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funzionano entrambe bene da Esplora file di Windows, e il link del browser funziona in qualsiasi browser.

Se vuoi comunque provare Connetti unità di rete: apri **Esplora file**, fai clic destro su **Questo PC**, scegli **Connetti unità di rete** e inserisci l'host e il nome della condivisione mostrati in Everdisk. Se non riesce a connettersi, è la limitazione della porta di cui sopra, quindi passa a WebDAV o FTP.

## Attivare la cifratura per il Wi-Fi non fidato

SMB è l'unica connessione di Everdisk che può cifrare ogni trasferimento, il che conta su un Wi-Fi che non controlli del tutto, come quello di un bar o di una rete aziendale.

1. In **Impostazioni**, **Condivisione**, **Accesso**, imposta un **Login** e una **Password**. Le connessioni cifrate non possono essere anonime, quindi questo passaggio è obbligatorio.
2. In **Impostazioni**, **Condivisione**, attiva **Richiedi cifratura SMB**.
3. Interrompi e riavvia la condivisione così la modifica ha effetto.

Ogni trasferimento SMB è quindi protetto con la **cifratura SMB3 (AES)**. Il dispositivo che si collega deve supportare SMB3, cosa che il Finder su un Mac moderno e Windows 10 o versioni successive fanno entrambi. La cifratura SMB fa parte dell'acquisto Premium una tantum.

## Sola lettura o lettura e scrittura

L'interruttore **Modifica dei file** in Impostazioni, Condivisione, Accesso controlla questo per ogni server, incluso SMB. Attivalo e i dispositivi collegati possono caricare, rinominare ed eliminare. Disattivalo e possono solo sfogliare e copiare i file dal tuo telefono. Scegli la sola lettura quando consegni file a qualcuno a cui non vuoi far cambiare nulla.

## Modi reali in cui le persone lo usano

- **Spostare una cartella grande sul tuo iPhone da un Mac** trascinandola nella finestra del Finder, più veloce di un caricamento via web.
- **Prelevare una giornata di foto e video dal telefono** su un portatile senza iTunes o un cavo.
- **Inviare file tra due iPhone** tramite l'app File, senza una terza app da nessuna parte.
- **Lavorare su un file in loco**, aprendo un documento direttamente dal telefono in un'app sul Mac e risalvandolo.

## Qualche consiglio

- Tieni Everdisk aperto mentre un dispositivo è collegato. Bloccare il telefono a lungo può mettere in pausa l'app e far cadere la connessione.
- Se un Mac non vede il telefono nella barra laterale del Finder, collegati manualmente con Connessione al server e l'indirizzo smb completo.
- Per la migliore velocità sui trasferimenti grandi, mantieni la qualità di foto e video su Originale nelle Impostazioni.
- Su una rete non fidata, attiva Richiedi cifratura SMB e disattiva gli altri server mentre lavori.

## Domande frequenti

{{% details title="Qual è l'indirizzo e la porta SMB del mio iPhone?" closed="true" %}}
Dopo aver avviato la condivisione, Everdisk mostra l'indirizzo nella schermata Condivisione. Ha l'aspetto smb://192.168.1.20:4455/Share. Il 4455 è la porta che Everdisk usa per SMB, e Share è il nome della cartella condivisa. La prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi il tuo sarà diverso.
{{% /details %}}

{{% details title="Posso collegarmi alla condivisione SMB del mio iPhone da Windows?" closed="true" %}}
Esplora file di Windows si collega a SMB solo sulla porta standard e non accetta una porta personalizzata nel percorso, mentre Everdisk usa la porta 4455. Quindi la semplice via Connetti unità di rete spesso non riesce a raggiungerlo. Usa un gestore file che ti permetta di impostare una porta personalizzata, oppure collegati da Windows con WebDAV, FTP o il link del browser. Tutti questi funzionano da Windows senza alcun problema di porta.
{{% /details %}}

{{% details title="Come condivido file tra due iPhone con SMB?" closed="true" %}}
Avvia il server SMB sul primo iPhone in Everdisk. Sul secondo iPhone, apri l'app File, tocca il pulsante altro, scegli Connessione al server e inserisci l'indirizzo smb mostrato in Everdisk (per esempio smb://192.168.1.20:4455/Share). Collegati come Ospite o con il tuo login, e la condivisione compare in File. Puoi anche usare la scheda Dispositivi di Everdisk sul secondo telefono.
{{% /details %}}

{{% details title="Il mio iPhone compare automaticamente nella barra laterale del Finder su Mac?" closed="true" %}}
Di solito sì. Everdisk annuncia la condivisione SMB sul tuo Wi-Fi, quindi il tuo iPhone spesso compare sotto Posizioni o Rete nella barra laterale del Finder. Cliccaci e scegli Connetti come, poi Ospite o il tuo login. Se non compare, collegati manualmente con Vai, Connessione al server e l'indirizzo smb completo.
{{% /details %}}

{{% details title="Mi serve una password per usare SMB?" closed="true" %}}
No, il login è facoltativo. Lascia vuoti Login e Password in Impostazioni, Condivisione, Accesso per consentire l'accesso ospite. Impostali se vuoi che le connessioni accedano. Un login e una password sono obbligatori solo se attivi Richiedi cifratura SMB, perché le connessioni cifrate non possono essere anonime.
{{% /details %}}

{{% details title="La connessione SMB è cifrata?" closed="true" %}}
Può esserlo. SMB è l'unica connessione di Everdisk che supporta la cifratura. Imposta un login e una password, poi attiva Richiedi cifratura SMB in Impostazioni, Condivisione. Ogni trasferimento è quindi protetto con SMB3 (AES). L'altro dispositivo deve supportare SMB3, cosa che i Mac moderni e Windows 10 o versioni successive fanno. La cifratura è una funzione Premium.
{{% /details %}}

{{% details title="Le persone possono modificare o eliminare i miei file via SMB?" closed="true" %}}
Solo se lo consenti. L'interruttore Modifica dei file in Impostazioni, Condivisione, Accesso controlla questo. Con esso attivo, i dispositivi collegati possono caricare, rinominare ed eliminare. Con esso disattivato, la condivisione è di sola lettura e gli altri possono sfogliare e copiare i file dal tuo telefono ma non cambiare nulla.
{{% /details %}}

{{% details title="Perché è caduta la mia connessione SMB?" closed="true" %}}
Il tuo iPhone è il server, e iOS mette in pausa le app che restano troppo a lungo in background. Tieni Everdisk aperto sullo schermo mentre un dispositivo è collegato, e collega il telefono all'alimentazione durante i trasferimenti lunghi. Assicurati anche che entrambi i dispositivi siano rimasti sulla stessa rete Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV o FTP, quale dovrei usare?" closed="true" %}}
Usa SMB quando vuoi che il telefono si comporti come un vero disco di rete su un Mac, un altro iPhone, Linux o un NAS, e quando vuoi la cifratura. Usa WebDAV quando vuoi un disco di rete che funzioni bene anche da Windows. Usa FTP per la più ampia compatibilità con dispositivi e app più vecchi. Everdisk può eseguirli tutti contemporaneamente, quindi non sei vincolato a uno solo.
{{% /details %}}

{{% details title="Everdisk è gratis?" closed="true" %}}
Sì, Everdisk si scarica gratis e il server SMB è incluso. L'acquisto Premium opzionale una tantum aggiunge la cifratura SMB, le porte personalizzate e qualche altro extra. Puoi configurare SMB e condividere file senza pagare.
{{% /details %}}

Pronto a provarlo? [Scarica Everdisk dall'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e apri il tuo iPhone in Finder in circa un minuto. Domande o feedback? Scrivici a **support@everappz.com**.
