---
title: "Impostazioni"
date: 2026-08-20
description: "Una panoramica completa delle impostazioni di Everdisk: profilo del dispositivo (nome e avatar), i cinque server di connessione, i controlli di accesso, la cifratura SMB (SMB3/AES), la qualità di foto e video, le porte personalizzate, le miniature DLNA, le opzioni di rete e trasferimento, le opzioni del gestore file e Premium."
keywords: ["impostazioni Everdisk", "nome avatar dispositivo", "server di connessione", "qualità foto video", "porte personalizzate HTTP WebDAV FTP", "miniature DLNA", "trasferimenti paralleli", "eliminare file permanentemente", "cache miniature", "Everdisk Premium"]
tags: ["everdisk", "guida", "impostazioni"]
readingTime: 12
---


La scheda **Impostazioni** raggruppa tutto in tre aree principali - **Condivisione**, **Rete** e **Gestore file** - più Premium, feedback e link legali. Questa pagina spiega ogni impostazione e il suo valore predefinito.

## Premium

In cima a Impostazioni vedi il tuo stato Premium, oppure un pulsante **Sblocca tutte le funzioni**. Everdisk è gratuito con alcuni limiti; un acquisto **Premium Lifetime** una tantum li rimuove. Vedi [Premium](#premium-lifetime) alla fine di questa pagina.

## Impostazioni di condivisione

### Generale

- **Avvia automaticamente la condivisione del dispositivo**: avvia la condivisione non appena apri l'app. *(Premium.)*
- **Condividi la cartella Documenti**: condividi la cartella Documenti dell'app. Attiva per impostazione predefinita.
- **Avvisa prima di disconnettere**: ti ricorda di riaprire l'app prima che il sistema la sospenda in background. Disattivata per impostazione predefinita; la prima volta chiede l'autorizzazione alle notifiche.

### Profilo del dispositivo

- **Nome del dispositivo**: il nome che gli altri dispositivi vedono per te sulla rete. Tocca per modificarlo. *(Premium.)*
- **Avatar del dispositivo**: l'icona e il colore di sfondo per il tuo dispositivo. Puoi scegliere un'icona, un gradiente di sfondo oppure **scegliere un avatar da Foto**. *(Premium.)*
- **Rigenera nome e avatar** e **Rigenera avatar**: ottieni un nuovo nome e/o avatar casuale. *(Gratis.)*

### Accesso

- **Login** e **Password**: richiedi un accesso per le connessioni Browser, Computer e Altre app.
- **Modifica file**: consenti ai dispositivi collegati di caricare, rinominare ed eliminare. Attiva per impostazione predefinita.
- **Dispositivi bloccati**: gestisci i dispositivi che hai bloccato.

Vedi [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access) per i dettagli.

### Connessioni

Attiva o disattiva ogni server. Tutti e cinque sono attivi per impostazione predefinita e ognuno ha un pulsante info (ⓘ) con le istruzioni di connessione:

- **TV e Media Center** (DLNA)
- **Browser** (HTTP)
- **Computer** (WebDAV)
- **Computer (avanzate)** (SMB) - un'unità di rete per Mac, Windows e Linux; su un Mac compare da sola nella barra laterale del Finder. L'unica connessione che può essere cifrata.
- **Altre app e dispositivi** (FTP)

### Foto

- **Formato**: Originale o Massima compatibilità (JPEG).
- **Qualità**: Originale, Alta, Media o Bassa.

Qualsiasi opzione diversa da Originale converte le foto mentre vengono condivise, il che è più lento. La conversione è una funzione Premium.

### Video

- **Formato**: Originale o Massima compatibilità (H.264 MP4).
- **Qualità**: Originale, Alta, Media o Bassa.

Stesso principio delle Foto: l'originale è il più veloce e la conversione è Premium. Riduci la qualità se una TV più vecchia non riesce a riprodurre un video.

### Avanzate

- **Porta HTTP** (predefinita 80), **Porta WebDAV** (predefinita 8080), **Porta SMB** (predefinita 4455), **Porta FTP** (predefinita 2121). Il DLNA sceglie la sua porta automaticamente. *(La modifica delle porte è Premium; gli utenti gratuiti possono vedere i valori.)*

### Cifratura SMB

- **Richiedi cifratura SMB**: cifra ogni trasferimento SMB con la **cifratura SMB3 (AES)** così nessun altro sulla rete può leggere i tuoi file. Disattivata per impostazione predefinita. Richiede un **login e una password** impostati sopra (le connessioni cifrate non possono essere anonime) e un client che supporti SMB3, come il Finder su un Mac moderno o Windows 10 e versioni successive. Le modifiche hanno effetto al successivo avvio della condivisione. *(Premium.)*

### Miniature DLNA

- **Mostra miniature**: pubblica le immagini di anteprima per le TV. Attiva per impostazione predefinita (gratis).
- Scegli quali dimensioni pubblicare: **Piccola (160px)**, **Media (640px)**, **Grande (1024px)**, **Extra grande (4096px)**.

## Impostazioni di rete

- **Trasferimenti file**: usa solo **Wi-Fi**, oppure **Wi-Fi e dati cellulari**, per download e caricamenti. Predefinito Wi-Fi.
- **Limite di trasferimenti paralleli**: quanti trasferimenti eseguire contemporaneamente. Predefinito 5.
- **Trasferimenti in background**: mantieni attivi i trasferimenti mentre usi altre schermate. Attivi per impostazione predefinita.
- **Miniature per i file**: se recuperare le miniature dei file su altri dispositivi solo tramite Wi-Fi o anche tramite dati cellulari. Predefinito Wi-Fi.

## Impostazioni del gestore file

- **Elimina i file permanentemente**: elimina immediatamente senza cestino. Disattivata per impostazione predefinita. Vedi [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access).
- **Reimposta tutti i messaggi di avviso**: ripristina i banner di suggerimento che hai chiuso.
- **Cache delle miniature**: vedi quanto spazio occupano le miniature memorizzate nella cache e **Svuota la cache delle miniature**.

## Feedback e note legali

In fondo puoi **Valutare questa app**, **Inviare un feedback**, **Scoprire altre app** e aprire i **Termini e condizioni** e l'**Informativa sulla privacy**.

## Premium Lifetime

Everdisk è gratuito. Un unico acquisto **Premium Lifetime** - un pagamento una tantum, non un abbonamento - sblocca:

- **Cartelle illimitate**: condividi più di 5 cartelle.
- **Connessioni illimitate**: salva più di 10 server nella scheda Dispositivi.
- **Conversione di foto e video**: condividi in qualsiasi qualità diversa da Originale.
- **Cifratura SMB**: proteggi i trasferimenti SMB con la cifratura SMB3 (AES).
- **Porte personalizzate**: imposta le tue porte HTTP, WebDAV, SMB e FTP.
- **Avvio automatico della condivisione**: avvia la condivisione automaticamente quando apri l'app.
- **Personalizzazione del dispositivo**: un nome del dispositivo personalizzato, un'icona avatar, un gradiente di sfondo o un avatar con foto.

Premium è legato al tuo Apple ID. Usa **Ripristina acquisti** per sbloccarlo sui tuoi altri dispositivi con lo stesso Apple ID.

## Prossimi passi

- [Condivisione](/docs/guide/everdisk/everdisk-guide-sharing): la schermata Condivisione nel dettaglio.
- [Accesso e privacy](/docs/guide/everdisk/everdisk-guide-access): password, modifiche e blocco.
- [FAQ](/docs/faq/everdisk): risposte rapide alle domande comuni.
