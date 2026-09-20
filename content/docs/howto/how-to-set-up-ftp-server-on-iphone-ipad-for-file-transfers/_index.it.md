---
title: "Come configurare un server FTP su iPhone e iPad per il trasferimento dei file"
description: "Trasforma iPhone o iPad in un server FTP con Everdisk e trasferisci file da un Mac, un PC Windows, Linux, Android, un'app FTP come FileZilla o un altro iPhone via Wi-Fi. Configurazione completa, l'indirizzo e la porta ftp, l'accesso ospite e la connessione passo passo per ogni dispositivo."
date: 2026-09-19
tags: ["everdisk", "ftp", "trasferimento file", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["server FTP iPhone", "server FTP iPad", "come configurare FTP su iPhone", "app server ftp iphone", "collegare FileZilla a iPhone", "Cyberduck iPhone FTP", "trasferire file iPhone FTP", "ftp iphone al computer", "ftp iphone a iphone", "collegarsi a iPhone FTP da Windows", "indirizzo porta ftp iphone", "ftp anonimo iphone", "condividere file iphone ftp", "iphone ftp per fotocamera nas"]
readingTime: 9
---

{{< author-byline >}}

FTP è il vecchio affidabile del trasferimento file. È in giro da decenni, ed è esattamente per questo che è così utile: quasi tutto ciò che può parlare con un server lo capisce. Fotocamere, smart TV, router, dischi di rete, strumenti di automazione e ogni app FTP desktop parlano FTP. Con [Everdisk](/products/everdisk) puoi eseguire un server FTP sul tuo iPhone o iPad, così il telefono diventa un posto a cui quei dispositivi e app possono collegarsi per spostare i file.

Ricorri a FTP quando le altre opzioni non vanno bene, per esempio un dispositivo più vecchio o un'app che sa collegarsi solo tramite FTP. Questa guida copre la configurazione e come collegarti da un Mac, Windows, un'app FTP, Linux, Android e un secondo iPhone.

## Cosa ti serve

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installato.
- Un computer, un'app o un dispositivo sulla **stessa rete Wi-Fi**.
- I file che vuoi condividere, nella cartella Documenti di Everdisk o nelle cartelle che aggiungi.

## Configura il server FTP in Everdisk

### Passo 1: scegli cosa condividere e imposta l'accesso

Apri Everdisk, vai alla scheda **Condivisione** e tocca **Cosa condividere**. La cartella Documenti è condivisa per impostazione predefinita. Aggiungine altre con **Aggiungi cartella** e **Aggiungi file**.

Apri **Impostazioni**, poi **Condivisione**, poi **Accesso**. Attiva **Modifica dei file** se vuoi che le persone possano caricare, rinominare ed eliminare, o disattivala per consentire solo i download. Imposta un **Login** e una **Password** se vuoi un accesso, oppure lasciali vuoti così chiunque può collegarsi come ospite.

### Passo 2: attiva il server FTP

Vai su **Impostazioni**, poi **Condivisione**, poi **Connessioni**, e attiva **Altre app e dispositivi**. Quello è il server FTP (porta il tag FTP).

### Passo 3: avvia la condivisione e annota l'indirizzo

Torna alla scheda **Condivisione** e tocca **Avvia**. La sezione **Come collegarsi** mostra l'indirizzo FTP. Ha questo aspetto:

```
ftp://192.168.1.20:2121
```

Il numero dopo i due punti è la **porta**, che è **2121** per impostazione predefinita. La prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi il tuo sarà diverso. Tieni Everdisk aperto sullo schermo mentre un dispositivo è collegato.

## Collegarsi da un Mac

1. Apri **Finder**, scegli **Vai**, poi **Connessione al server** (o premi **Command e K**).
2. Digita l'indirizzo FTP mostrato in Everdisk, per esempio `ftp://192.168.1.20:2121`.
3. Clicca **Connetti**, poi scegli **Ospite** o inserisci il tuo **Login** e la tua **Password**.

Il Finder monta la condivisione FTP così puoi sfogliare e copiare file sul tuo Mac. Nota che il Finder apre l'FTP in sola lettura. Quando vuoi caricare da un Mac, usa un'app FTP come descritto qui sotto.

## Collegarsi da Windows

1. Apri **Esplora file** e clicca la barra degli indirizzi in alto.
2. Digita l'indirizzo FTP da Everdisk, per esempio `ftp://192.168.1.20:2121`, e premi **Invio**.
3. Inserisci il tuo **Login** e la tua **Password** se ne hai impostati, oppure continua come ospite.

I file condivisi compaiono nella finestra e puoi copiarli sul tuo PC.

## Collegarsi con un'app FTP (FileZilla, Cyberduck)

Per i caricamenti e il pieno controllo, un'app FTP è lo strumento migliore. **FileZilla** e **Cyberduck** sono gratuiti e girano su Windows, Mac e Linux.

1. Apri l'app e crea una nuova connessione.
2. Imposta l'**Host** sull'indirizzo Wi-Fi del tuo iPhone, e la **Porta** su **2121**.
3. Per il login, inserisci il tuo **Login** e la tua **Password**, oppure scegli **Anonimo** se non ne hai impostato uno.
4. Connetti, e trascina i file in entrambe le direzioni (i caricamenti richiedono Modifica dei file attiva).

## Collegarsi da Linux

1. Apri il tuo gestore file e scegli **Connessione al server** o **Altre posizioni**.
2. Inserisci l'indirizzo, per esempio `ftp://192.168.1.20:2121`.
3. Collegati come ospite o con il tuo login.

Puoi anche usare qualsiasi client FTP Linux dal terminale, puntandolo allo stesso host e alla porta 2121.

## Collegarsi da Android

Android non ha un browser FTP di sistema, quindi usa un'app:

1. Installa un client FTP come **AndFTP**, **FTPCafe**, o un gestore file con supporto FTP come **Solid Explorer**.
2. Aggiungi una connessione con l'host, la **porta 2121** e il tuo login o Anonimo.
3. Sfoglia e trasferisci.

## Collegarsi da un altro iPhone o iPad

L'app File di iOS non include un client FTP, quindi usa una di queste sul secondo dispositivo:

- **La scheda Dispositivi di Everdisk.** Apri Everdisk, vai su **Dispositivi**, tocca **Nuova connessione**, scegli **FTP** e inserisci l'indirizzo, per esempio `ftp://192.168.1.20:2121`. È la via più semplice.
- **Un'app FTP dedicata** per iOS, usando lo stesso host, la porta 2121 e il login.

## Collegare altri apparecchi: fotocamere, TV, router e NAS

È qui che l'FTP brilla. Molti dispositivi hanno un client FTP integrato che può inviare o recuperare file:

- **Le fotocamere** che caricano foto tramite FTP possono inviarle direttamente al tuo iPhone.
- **Smart TV, router, box NAS e strumenti di automazione** che supportano l'FTP possono collegarsi allo stesso modo.

Puntali all'indirizzo Wi-Fi del tuo iPhone, alla porta **2121** e al tuo login (o Anonimo), usando l'indirizzo mostrato in Everdisk.

## Sola lettura o lettura e scrittura

L'interruttore **Modifica dei file** in Impostazioni, Condivisione, Accesso controlla questo. Attivo permette alle persone di caricare, rinominare ed eliminare. Disattivo significa che possono solo scaricare. Scegli la sola lettura quando stai consegnando file e non vuoi che nulla venga cambiato sul tuo telefono.

## Modi reali in cui le persone lo usano

- **Collegare FileZilla al tuo iPhone** e spingere un lotto di file sul telefono in una sola volta.
- **Lasciare che una vecchia app o un dispositivo che parla solo FTP** raggiunga i tuoi file quando nient'altro riesce a collegarsi.
- **Ricevere foto da una fotocamera** che carica tramite FTP.
- **Spostare file tra un iPhone e un iPad** usando la scheda Dispositivi di Everdisk sul dispositivo ricevente.

## Qualche consiglio

- Tieni Everdisk aperto mentre un dispositivo è collegato, poiché iOS mette in pausa le app in background dopo un po'.
- Per caricare da un Mac, usa FileZilla o Cyberduck invece del Finder, perché il Finder apre l'FTP in sola lettura.
- Lascia il login vuoto per la più ampia compatibilità, poi collegati come Anonimo, cosa che la maggior parte dei client FTP offre.
- L'FTP non cifra il suo traffico. Su una rete di cui non ti fidi, usa invece il [server SMB con la cifratura](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/).

## Domande frequenti

{{% details title="Qual è l'indirizzo e la porta FTP del mio iPhone?" closed="true" %}}
Dopo aver avviato la condivisione, Everdisk mostra l'indirizzo nella schermata Condivisione. Ha l'aspetto ftp://192.168.1.20:2121. Il 2121 è la porta che Everdisk usa per FTP, e la prima parte è l'indirizzo del tuo iPhone sul Wi-Fi, quindi il tuo sarà diverso.
{{% /details %}}

{{% details title="Come collego FileZilla o Cyberduck al mio iPhone?" closed="true" %}}
Apri l'app e crea una nuova connessione. Imposta l'Host sull'indirizzo Wi-Fi del tuo iPhone e la Porta su 2121. Inserisci il tuo Login e la tua Password, oppure scegli Anonimo se non ne hai impostato uno in Everdisk. Connetti, e puoi trascinare i file in entrambe le direzioni quando Modifica dei file è attiva.
{{% /details %}}

{{% details title="Posso collegarmi all'FTP del mio iPhone da Windows?" closed="true" %}}
Sì. Apri Esplora file, clicca la barra degli indirizzi, digita l'indirizzo FTP da Everdisk (per esempio ftp://192.168.1.20:2121) e premi Invio. Inserisci il tuo login se ne hai impostato uno, oppure continua come ospite. Per i caricamenti e più controllo, usa invece un'app FTP come FileZilla.
{{% /details %}}

{{% details title="Mi serve un login per l'FTP?" closed="true" %}}
No, il login è facoltativo. Lascia vuoti Login e Password in Impostazioni, Condivisione, Accesso, e collegati come Anonimo, cosa che la maggior parte dei client FTP offre. Imposta un login se vuoi che le connessioni accedano prima.
{{% /details %}}

{{% details title="Perché riesco solo a scaricare e non a caricare via FTP?" closed="true" %}}
Due sono le cause comuni. Primo, l'interruttore Modifica dei file in Impostazioni, Condivisione, Accesso deve essere attivo per consentire caricamenti, rinomine ed eliminazioni. Secondo, il Finder di Mac apre l'FTP in sola lettura, quindi usa un'app FTP come FileZilla o Cyberduck quando vuoi caricare.
{{% /details %}}

{{% details title="Posso usare FTP tra due iPhone?" closed="true" %}}
Sì. Avvia il server FTP sul primo iPhone. Sul secondo, apri Everdisk, vai alla scheda Dispositivi, tocca Nuova connessione, scegli FTP e inserisci l'indirizzo mostrato sul primo telefono. Funziona anche un'app FTP dedicata per iOS, poiché l'app File di iOS non include un client FTP.
{{% /details %}}

{{% details title="L'FTP è sicuro?" closed="true" %}}
L'FTP semplice non cifra il suo traffico, quindi trattalo come uno strumento per reti di cui ti fidi, come il tuo Wi-Fi di casa. Su una rete che non controlli, usa il server SMB con Richiedi cifratura SMB attivo, che protegge ogni trasferimento.
{{% /details %}}

{{% details title="Quali dispositivi possono collegarsi via FTP?" closed="true" %}}
Quasi tutto ciò che ha un client FTP. Questo include computer Mac, Windows e Linux, app FTP come FileZilla e Cyberduck, gestori file Android e hardware come fotocamere, smart TV, router, box NAS e strumenti di automazione. Quell'ampia portata è il motivo principale per scegliere l'FTP.
{{% /details %}}

{{% details title="Perché è caduta la mia connessione FTP?" closed="true" %}}
Il tuo iPhone è il server, e iOS mette in pausa le app che restano troppo a lungo in background. Tieni Everdisk aperto sullo schermo mentre un dispositivo è collegato, e collegalo all'alimentazione per i trasferimenti lunghi. Assicurati anche che entrambi i dispositivi siano ancora sulla stessa rete Wi-Fi.
{{% /details %}}

{{% details title="Everdisk è gratis?" closed="true" %}}
Sì, Everdisk si scarica gratis e il server FTP è incluso. Un acquisto Premium opzionale una tantum aggiunge extra come le porte personalizzate e la conversione di foto e video. Puoi configurare l'FTP e trasferire file senza pagare.
{{% /details %}}

Pronto a provarlo? [Scarica Everdisk dall'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e collega il tuo primo client FTP in un paio di minuti. Domande o feedback? Scrivici a **support@everappz.com**.
