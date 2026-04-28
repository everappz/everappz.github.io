---
title: "Come collegare l'archivio interno del Bluesound VAULT da Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Scopri come accedere al disco rigido interno del Bluesound VAULT da Evermusic, Flacbox ed Evertag utilizzando il protocollo SMB per gestire, modificare e riprodurre file audio."
keywords: ["bluesound vault", "collegare archivio smb", "evermusic smb", "flacbox vault", "evertag smb", "archivio nas musica", "unità interna vault"]
tags: ["evermusic", "collegare", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Riepilogo:** Collegati all'archivio interno del tuo Bluesound VAULT tramite SMB utilizzando Evermusic, Flacbox o Evertag. Trova l'indirizzo IP del VAULT nell'app BluOS, inseriscilo come connessione SMB con accesso ospite e inizia a riprodurre o gestire i tuoi file musicali.

Il Bluesound VAULT ha un disco rigido interno e funziona come un Network Attached Storage (NAS). L'accesso al disco rigido interno del VAULT ti consente di aggiungere/eliminare file, modificare i tag dei metadati dalle nostre app Evermusic, Flacbox, Evertag.

**Di seguito i passaggi per accedere al disco rigido interno del tuo VAULT:**

1. Nell'app BluOS, seleziona **Aiuto > Diagnostica**.

2. Dalla pagina **Diagnostica**, ottieni l'**Indirizzo IP** del VAULT. Questo **Indirizzo IP** verrà utilizzato nei passaggi successivi.

3. Apri Evermusic, Flacbox o Evertag.

   ![Applicazioni Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Apri la schermata "Connessioni" e seleziona la voce di menu "Connetti un servizio cloud".

   ![Schermata Connessioni di Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Seleziona il servizio cloud "SMB".

   ![Schermata Connetti un Servizio Cloud di Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. Nella "Schermata di configurazione SMB" inserisci l'URL nel seguente formato:

   ```
   SMB://<<VAULT-IP>>
   ```

   Sostituisci `<<VAULT-IP>>` con l'**Indirizzo IP** ottenuto nel Passaggio 2.

   **Nota:** Lascia vuoti i campi Login e Password perché l'archivio VAULT supporta la modalità OSPITE.

   ![Schermata connessione SMB di Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Tocca il pulsante "Accedi" per salvare la configurazione.

8. Apri l'archivio cloud collegato, naviga nella cartella con i file audio e tocca qualsiasi file per avviare il lettore audio.

   ![Schermata Server SMB Aperto di Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. Puoi anche modificare i file utilizzando il file manager integrato.

   ![Schermata File Manager di Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Con questi semplici passaggi, puoi accedere facilmente al disco rigido interno del tuo Bluesound VAULT e prendere il controllo della tua libreria musicale utilizzando Evermusic, Flacbox o Evertag.

## FAQ

{{% details title="Ho bisogno di un nome utente e una password per connettermi al Bluesound VAULT?" closed="true" %}}
No. Il Bluesound VAULT supporta l'accesso ospite (anonimo) tramite SMB. Lascia vuoti i campi Login e Password durante la configurazione della connessione.
{{% /details %}}

{{% details title="Posso modificare i tag musicali sul Bluesound VAULT?" closed="true" %}}
Sì. Utilizzando Evertag, puoi modificare i tag dei metadati (titolo, artista, album, ecc.) per i file audio memorizzati direttamente sul disco rigido interno del VAULT.
{{% /details %}}

{{% details title="Quali protocolli supporta il Bluesound VAULT?" closed="true" %}}
Il Bluesound VAULT espone il suo archivio interno tramite SMB (Server Message Block). Evermusic, Flacbox ed Evertag supportano tutti le connessioni SMB, rendendo la connessione semplice.
{{% /details %}}

{{% details title="Posso riprodurre musica in streaming dal VAULT senza copiare file sul mio iPhone?" closed="true" %}}
Sì. Una volta connesso tramite SMB, puoi riprodurre in streaming file audio direttamente dall'unità interna del VAULT senza copiarli sul tuo dispositivo.
{{% /details %}}
