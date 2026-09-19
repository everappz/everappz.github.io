---
title: "Accesso e privacy"
date: 2026-08-20
description: "Mantieni sicura la condivisione con Everdisk: proteggi l'accesso con login e password, cifra la connessione SMB con SMB3 (AES), controlla se i dispositivi collegati possono caricare, rinominare ed eliminare con Modifica file, blocca i dispositivi sconosciuti, scegli tra cestino ed eliminazione permanente e scopri perché tutto rimane sulla tua rete locale."
keywords: ["protezione password Everdisk", "cifratura SMB", "cifratura SMB3 AES", "interruttore modifica file", "bloccare dispositivo", "dispositivi bloccati", "eliminare file permanentemente", "solo rete locale", "condivisione file privata", "DLNA senza password", "sicurezza di rete"]
tags: ["everdisk", "guida", "accesso", "privacy", "sicurezza"]
readingTime: 8
---


Everdisk mantiene i tuoi file sulla tua rete e ti offre controlli semplici su chi può raggiungerli e cosa può fare. Trovi questi controlli in **Impostazioni → Condivisione → Accesso**, più alcune impostazioni correlate nel Gestore file.

## Proteggere l'accesso con login e password

Per impostazione predefinita, chiunque sia sulla stessa rete e abbia il tuo indirizzo può aprire i tuoi file condivisi. Per richiedere un accesso:

1. Vai in **Impostazioni → Condivisione → Accesso**.
2. Inserisci un **Login** e una **Password**.
3. Ora le connessioni **Browser (HTTP)**, **Computer (WebDAV)**, **Computer (avanzate) (SMB)** e **Altre app e dispositivi (FTP)** chiedono tutte questi dati prima di mostrare i tuoi file.

Lascia entrambi i campi vuoti per l'accesso aperto. La tua password è conservata in modo sicuro nel Keychain del dispositivo.

> **Il DLNA è sempre aperto.** La connessione TV e Media Center (DLNA) non può essere protetta da password, quindi una volta attiva, qualsiasi dispositivo sulla stessa rete Wi-Fi può sfogliare i tuoi contenuti condivisi. Disattivala se vuoi solo connessioni protette, e condividi solo su reti di cui ti fidi.

## Cifrare la connessione SMB (SMB3 / AES)

Un login e una password controllano **chi** può collegarsi, ma i dati stessi viaggiano ancora in chiaro sulla maggior parte delle connessioni. **SMB è l'unica connessione che Everdisk può cifrare**, cosa che rende illeggibile ogni trasferimento così nessun altro sulla stessa rete può leggerlo.

Per attivarla:

1. Imposta un **Login** e una **Password** come sopra: le connessioni cifrate non possono essere anonime.
2. Vai in **Impostazioni → Condivisione** e attiva **Richiedi cifratura SMB**.
3. **Interrompi e riavvia** la condivisione così la modifica ha effetto.

Ogni trasferimento SMB è quindi protetto con la **cifratura SMB3 (AES)**. Il dispositivo che si collega deve supportare SMB3: il Finder su un Mac moderno, o **Windows 10 e versioni successive**. È una scelta ottima su un Wi-Fi di cui non ti fidi del tutto. La Cifratura SMB è una funzione Premium.

## Consentire o bloccare le modifiche (Modifica file)

L'interruttore **Modifica file** controlla se i dispositivi collegati possono solo guardare i tuoi file, oppure anche modificarli.

- **Attivo** (impostazione predefinita): i dispositivi collegati possono **caricare, rinominare ed eliminare** i tuoi file condivisi, così il tuo dispositivo funziona come una vera unità di rete bidirezionale.
- **Disattivo**: i tuoi file condivisi sono di **sola lettura**. Gli altri possono visualizzare e scaricare, ma non possono aggiungere o modificare nulla.

Attivandolo appare un breve avviso, perché consente ad altre persone di modificare i tuoi file. Porta un badge **Importante** mentre è attivo.

## Bloccare un dispositivo

Se vedi un dispositivo che non riconosci:

1. Nella schermata Condivisione, trovalo sotto **Chi è collegato**.
2. Tocca il suo pulsante altre azioni e scegli **Blocca questo dispositivo**.

I dispositivi bloccati sono elencati in **Impostazioni → Condivisione → Accesso → Dispositivi bloccati**, dove puoi **sbloccarne** uno o **Sbloccare tutti**. Il blocco segue il dispositivo anche se il suo indirizzo di rete cambia (per le connessioni Browser, Computer e TV).

## Cestino contro eliminazione permanente

Quando un file viene eliminato, da te nel gestore file o da un dispositivo collegato, normalmente va in un **cestino** recuperabile, così puoi riaverlo.

Se preferisci che i file vengano rimossi immediatamente senza possibilità di recupero, attiva **Elimina i file permanentemente** in **Impostazioni → Gestore file → Eliminazione dei file**. È disattivato per impostazione predefinita. **Riguarda il gestore file sul dispositivo** e **le eliminazioni effettuate in rete**; non cambia il modo in cui la libreria Foto o la libreria Musica del sistema gestiscono l'eliminazione.

## Tutto rimane locale

Everdisk condivide solo sulla tua **rete locale**: niente viene caricato su internet e non c'è alcun account cloud nel mezzo. Alcune cose che vale la pena sapere:

- Everdisk ha bisogno dell'autorizzazione **Rete locale** di iOS, così i dispositivi vicini possono trovarlo. Se quell'autorizzazione è disattivata, un avviso spiega come riattivarla nell'app Impostazioni di iOS.
- Per la massima privacy, condividi solo mentre sei su una rete Wi-Fi **domestica o privata** di cui ti fidi, e fai attenzione sul Wi-Fi pubblico. Un login e una password aiutano, ma non sostituiscono una rete affidabile.
- L'**opzione più privata di tutte è un cavo USB verso un Mac**: i dati passano direttamente attraverso il cavo e non toccano mai il router o internet. Vedi [Collega i tuoi dispositivi](/docs/guide/everdisk/everdisk-guide-connect).

## Prossimi passi

- [Condivisione](/docs/guide/everdisk/everdisk-guide-sharing): scegli cosa condividere e avvia la condivisione.
- [Impostazioni](/docs/guide/everdisk/everdisk-guide-settings): tutte le impostazioni di Accesso e Gestore file in un unico posto.
