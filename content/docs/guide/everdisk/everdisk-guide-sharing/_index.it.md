---
title: "Condivisione"
date: 2026-08-20
description: "Scopri come funziona la condivisione in Everdisk: tocca Avvia per trasformare il tuo iPhone o iPad in un'unità wireless, scegli cosa condividere (file, cartelle, foto e musica), esegui i cinque server (DLNA, HTTP, WebDAV, SMB, FTP), cifra la connessione SMB con SMB3 (AES), leggi gli indirizzi di connessione, controlla chi è collegato e mantieni la condivisione attiva tramite Wi-Fi o un cavo USB."
keywords: ["condivisione Everdisk", "unità wireless iPhone", "avviare la condivisione", "condividere file iPhone", "condividere foto in rete", "DLNA HTTP WebDAV FTP", "cosa condividere", "come collegarsi", "tenere l'app aperta", "condivisione via Wi-Fi o cavo USB"]
tags: ["everdisk", "guida", "condivisione"]
readingTime: 9
---


La scheda **Condivisione** è il cuore di Everdisk. È qui che trasformi il tuo iPhone o iPad in un'unità wireless, scegli esattamente cosa vuoi condividere e ottieni gli indirizzi che gli altri dispositivi usano per collegarsi. È la prima scheda che vedi quando apri l'app.

## Avviare e interrompere la condivisione

Al centro della schermata Condivisione c'è un grande pulsante rotondo.

- Tocca **Avvia** per mettere online tutti i server abilitati in una sola volta. Il pulsante mostra **Avvio in corso...**, poi **Interrompi** quando la condivisione è attiva.
- Tocca **Interrompi** per rimettere tutto offline. I dispositivi collegati vengono disconnessi.

Mentre la condivisione è attiva, i file, le foto e la musica che hai scelto sono disponibili per qualsiasi dispositivo della stessa rete che si colleghi usando uno dei cinque metodi qui sotto.

> La condivisione funziona solo mentre l'app è aperta. Vedi **Tieni l'app aperta** verso la fine di questa pagina per capire il motivo e come mantenere attivi i trasferimenti di grandi dimensioni.

## Scegliere cosa condividere

Prima di avviare, tocca l'intestazione **Cosa condividere** per aprire tre gruppi. Puoi condividere una qualsiasi combinazione di essi e devi scegliere almeno un elemento prima di poter avviare la condivisione.

**File e cartelle**

- La cartella **Documenti** dell'app viene condivisa per impostazione predefinita. Se preferisci, puoi interromperne la condivisione.
- Tocca **Aggiungi cartella** per condividere una cartella da qualsiasi punto del dispositivo, oppure **Aggiungi file** per condividere singoli file.
- Ogni elemento condiviso ha un pulsante **Info** e un pulsante **Interrompi condivisione**.

**Foto e video**

- Attiva **Consenti l'accesso a tutta la libreria Foto** per condividere l'intera libreria di foto e video, oppure
- Tocca **Aggiungi foto** per selezionare a mano solo le foto e i video che vuoi condividere.

**Musica**

- Attiva **Consenti l'accesso a tutta la libreria Musica** per condividere l'intera libreria musicale, oppure
- Tocca **Aggiungi brani** per condividere solo i brani selezionati.
- I brani protetti (DRM) o archiviati solo nel cloud non possono essere condivisi.

Se provi ad avviare senza aver selezionato nulla, Everdisk mostra un avviso **Niente da condividere**. Se modifichi ciò che è condiviso mentre la condivisione è attiva, **interrompi e riavvia** per applicare la modifica.

## I cinque server

Everdisk condivide gli stessi contenuti in cinque modi contemporaneamente. Ognuno è pensato per un tipo di dispositivo diverso e ognuno può essere attivato o disattivato in **Impostazioni → Condivisione → Connessioni**. Per impostazione predefinita tutti e cinque sono attivi.

- **TV e Media Center (DLNA)**: per smart TV e lettori multimediali. Rilevano da soli il tuo dispositivo e mostrano le tue foto, i video e la musica, con miniature di anteprima.
- **Browser (HTTP)**: per qualsiasi telefono, tablet o computer. L'altra persona apre un link in un browser web per sfogliare e scaricare i tuoi file. Niente da installare.
- **Computer (WebDAV)**: per un Mac, un PC Windows o una macchina Linux. Il tuo dispositivo appare come una normale unità di rete, così puoi trascinare i file in entrambe le direzioni.
- **Computer (avanzate) (SMB)**: un'unità di rete per Mac, Windows e Linux. Su un Mac compare da sola nella barra laterale del Finder; su Windows, aprila in Esplora file con un indirizzo `smb://`. È l'unica connessione che puoi **cifrare**, con la cifratura SMB3 (AES).
- **Altre app e dispositivi (FTP)**: per app per file e utenti esperti che parlano FTP.

Per le istruzioni di connessione passo dopo passo per ogni tipo, vedi [Collega i tuoi dispositivi](/docs/guide/everdisk/everdisk-guide-connect).

## Come collegarsi e indirizzi di connessione

Dopo aver toccato Avvia, la sezione **Come collegarsi** mostra una scheda per ogni server attivo con l'**indirizzo** esatto da digitare sull'altro dispositivo. Ogni indirizzo è facile da copiare: toccalo per copiarlo, usa il pulsante **Condividi** per inviarlo oppure tocca il pulsante **info (ⓘ)** per istruzioni dettagliate per ciascun protocollo.

- La scheda DLNA mostra un indirizzo di descrizione del dispositivo che termina con `/device-desc.xml` per i lettori che lo richiedono.
- Quando il tuo dispositivo è collegato a un Mac tramite cavo, appare un indirizzo aggiuntivo con un badge **Connessione via cavo** che usa il nome `.local` del tuo dispositivo.

Puoi anche aprire l'indirizzo come **codice QR**, così la fotocamera di un altro dispositivo può raggiungerlo direttamente.

## Chi è collegato

La sezione **Chi è collegato** elenca in tempo reale i dispositivi attualmente collegati a te. Tocca il pulsante altre azioni accanto a un qualsiasi dispositivo per **Bloccare questo dispositivo** se non lo riconosci. I dispositivi bloccati si gestiscono in [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access).

## Il nome e l'avatar del tuo dispositivo

Ogni dispositivo ha un nome facile da riconoscere (come "Speedy-Hare") e un avatar colorato. È il nome che una TV, un computer o un'altra app mostrano per il tuo dispositivo sulla rete, così è facile da individuare. Puoi rigenerare gratuitamente il nome e l'avatar, oppure impostare un nome, un'icona o un avatar con foto personalizzati con Premium. Vedi [Impostazioni](/docs/guide/everdisk/everdisk-guide-settings).

## Condivisione via Wi-Fi o cavo USB

La condivisione può funzionare in due situazioni:

- **Via Wi-Fi**: il tuo dispositivo e gli altri dispositivi sono sulla stessa rete Wi-Fi.
- **Via cavo USB**: il tuo dispositivo è collegato a un **Mac** tramite cavo, anche quando non c'è alcuna rete Wi-Fi. È più veloce del Wi-Fi e continua a funzionare in aereo, in hotel o su una rete bloccata.

Se non sono disponibili né il Wi-Fi né un cavo, il pulsante **Avvia** è disabilitato e appare un avviso **Nessuna connessione Wi-Fi**. Se la connessione cade durante la condivisione, Everdisk interrompe automaticamente la condivisione e ti avvisa. Tocca il pulsante info su uno qualsiasi di questi avvisi per una spiegazione completa.

## Tieni l'app aperta

Poiché il tuo iPhone o iPad funge da server, **la condivisione funziona solo mentre Everdisk è aperto sullo schermo**. Se chiudi l'app o blocchi il dispositivo per molto tempo, il sistema può sospendere l'app e la condivisione si interrompe.

Per i trasferimenti di grandi dimensioni:

- Tieni Everdisk aperto e in primo piano.
- Collega il tuo dispositivo all'alimentazione.
- Imposta il **Blocco automatico** su **Mai** nell'app Impostazioni di iOS durante il trasferimento.

Puoi attivare **Avvisa prima di disconnettere** (in Impostazioni → Condivisione), così Everdisk ti ricorda di riaprire l'app prima che il sistema la sospenda. Tocca il pulsante info sul banner **Tieni l'app aperta** per maggiori dettagli.

## Prossimi passi

- [Collega i tuoi dispositivi](/docs/guide/everdisk/everdisk-guide-connect): collega una TV, un computer, un browser, un telefono o un cavo USB.
- [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access): aggiungi una password e controlla le modifiche.
- [Impostazioni](/docs/guide/everdisk/everdisk-guide-settings): attiva o disattiva i server e regola la qualità.
