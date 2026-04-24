---
title: "Trasferire file dal computer all'iPhone usando il protocollo SMB"
description: "Scopri come trasferire e accedere a file di grandi dimensioni dal tuo Mac o PC Windows al tuo iPhone o iPad usando Evermusic e il protocollo SMB. Una guida passo passo per lo streaming e la gestione dei file senza interruzioni."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["trasferire file su iPhone SMB", "streaming musica PC su iPhone", "collegare Mac a iPhone SMB", "configurazione Evermusic SMB", "accesso file computer iPhone", "condivisione musica Windows iOS", "trasferimento file SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Riepilogo:** Usa Evermusic sul tuo iPhone o iPad per accedere ai file archiviati sul tuo Mac o PC Windows tramite la rete locale via SMB. Nessun cavo, nessun iTunes, nessun caricamento cloud necessario. Abilita la condivisione file sul tuo computer, connettiti nell'app e sfoglia o riproduci i tuoi file in modalità wireless.

Hai una vasta collezione di file di grandi dimensioni sul tuo MAC o PC e desideri accedervi facilmente dal tuo iPhone o iPad? Le nostre app forniscono una soluzione semplice.

Segui questi passaggi per abilitare l'accesso senza interruzioni tra il tuo computer e il dispositivo iOS usando il protocollo SMB:

## Passaggio 1: Abilitare il protocollo SMB sul tuo computer

**Per MAC:**

1. Apri "Preferenze di Sistema" sul tuo MAC.
2. Fai clic su "Condivisione".
3. Abilita il servizio "Condivisione file".
4. Aggiungi la tua cartella musicale alla sezione "Cartelle condivise". Aggiungi un utente e scegli il livello di autorizzazione (Lettura e scrittura o Solo lettura). Puoi optare per "Tutti: Solo lettura" per la cartella musicale aggiunta.

   ![Schermata impostazioni Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Ricorda l'URL del computer (smb://192.168.xx.xx), poiché lo userai nei passaggi successivi.
6. Fai clic su "Opzioni" e attiva "Condividi file e cartelle tramite SMB".

   ![Schermata condivisione file Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Abilita "Condivisione file Windows" per gli account disponibili.

   ![Schermata condivisione SMB Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Per Windows PC:**

1. Fai clic con il pulsante destro sulla tua cartella musicale.
2. Seleziona "Proprietà".
3. Vai alla scheda "Condivisione".
4. Fai clic su "Condividi..."
5. Scegli le persone con cui vuoi condividere la cartella e specifica il livello di autorizzazione. Puoi selezionare "Tutti: Lettura" per la cartella musicale scelta.

   ![Schermata condivisione SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Fai clic su "Fatto".
7. Fai clic su "Fatto" nella finestra "Condivisione file" e ricorda il percorso della cartella.

   ![Cartella condivisa SMB Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Passaggio 2: Collegare il tuo dispositivo iOS

1. Apri l'app sul tuo iPhone o iPad.
2. Vai alla scheda "Connessioni".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Schermata Connessioni di Evermusic"
  caption="Schermata Connessioni di Evermusic"
  width="400"
>}}

*Se il tuo computer appare nella sezione "Dispositivi disponibili":*

Se il tuo computer è visibile nella sezione "Dispositivi disponibili" e hai selezionato "Tutti: Solo lettura" nel passaggio precedente, tocca semplicemente il tuo computer e si connetterà automaticamente.

*Se il tuo computer non appare automaticamente:*

1. Tocca "Connetti un servizio cloud".
2. Seleziona "SMB" nella schermata "Connetti un servizio cloud".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Schermata Connetti un servizio cloud di Evermusic"
  caption="Schermata Connetti un servizio cloud di Evermusic"
  width="400"
>}}

3. Nella schermata "Connessione SMB", inserisci l'URL del server con il percorso della cartella condivisa. Puoi usare il nome del server o l'IP del server:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Inserisci il tuo nome utente e la password oppure lascia questi campi vuoti se hai selezionato "Tutti: Solo lettura" nel passaggio precedente.
5. Il campo "WORKGROUP" è opzionale e deve essere usato se hai un Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Schermata connettore SMB di Evermusic"
  caption="Schermata connettore SMB di Evermusic"
  width="400"
>}}

6. Una volta collegato il tuo computer usando il protocollo SMB, apparirà nella sezione "Servizi cloud" della schermata "Connessioni".
7. Apri il servizio collegato e naviga verso la cartella desiderata.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Cartella SMB aperta in Evermusic"
  caption="Cartella SMB aperta in Evermusic"
  width="400"
>}}

8. Puoi utilizzare il gestore file integrato per modificare i tuoi file secondo necessità.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Gestore file Evermusic"
  caption="Gestore file Evermusic"
  width="400"
>}}

## Passaggio 3: Soluzione per cartelle SMB2 con caratteri speciali

A volte potresti riscontrare problemi con cartelle contenenti caratteri speciali quando usi il protocollo SMB2. Ecco alcuni passaggi per risolvere questo problema:

1. **Abilitare SMB 1:**  
   • Come soluzione temporanea, prova ad abilitare SMB 1 sul tuo server e nelle impostazioni dell'app. Questo può aiutare a bypassare i problemi relativi ai caratteri speciali nei nomi delle cartelle.

2. **Usare il menu di apertura file di sistema:**  
   • Naviga su "File locali".  
   • Scorri verso il basso fino alla sezione "File su questo dispositivo".  
   • Tocca "Apri file..." o "Apri cartelle...".  
   • Individua il tuo server e seleziona i file o le cartelle di cui hai bisogno.  
   • Tocca "Apri" per confermare la selezione.

3. **Protocolli alternativi:**  
   • Se il problema persiste, considera di collegarti al tuo NAS usando i protocolli WebDAV o DLNA se il tuo NAS supporta queste opzioni. Questi protocolli potrebbero gestire i caratteri speciali in modo più appropriato.

Seguendo questi passaggi, puoi mitigare i problemi con i caratteri speciali nei nomi delle cartelle quando usi il protocollo SMB2.

## Conclusione

Con questi passaggi, puoi accedere facilmente alla tua vasta collezione di file dal tuo MAC o PC sul tuo iPhone o iPad usando le nostre app.

## Domande frequenti

{{% details title="Posso accedere ai file sul mio PC dal mio iPhone senza iTunes?" closed="true" %}}
Sì. Evermusic si connette al tuo computer tramite SMB sulla tua rete Wi-Fi locale. Non è necessaria la sincronizzazione con iTunes o Finder. Abilita la condivisione file sul tuo PC e connettiti direttamente dall'app.
{{% /details %}}

{{% details title="L'accesso ai file SMB funziona tramite internet?" closed="true" %}}
No. SMB è un protocollo di rete locale. Il tuo iPhone e il computer devono essere sulla stessa rete Wi-Fi. Per l'accesso remoto, carica i file su un servizio cloud come Google Drive o Dropbox e connettiti ad esso in Evermusic.
{{% /details %}}

{{% details title="Quali tipi di file posso accedere tramite SMB?" closed="true" %}}
Evermusic supporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC e altri formati audio. Puoi anche sfogliare e gestire file non audio usando il gestore file integrato.
{{% /details %}}

{{% details title="Posso trasferire file da un NAS al mio iPhone usando SMB?" closed="true" %}}
Sì. La maggior parte dei dispositivi NAS (Synology, QNAP, WD My Cloud e altri) supportano SMB. Connettiti al tuo NAS seguendo gli stessi passaggi di questa guida.
{{% /details %}}

{{% details title="Devo copiare i file sul mio iPhone per riprodurli?" closed="true" %}}
No. Evermusic trasmette i file in streaming direttamente dal tuo computer o NAS attraverso la rete. I file non vengono copiati sul tuo iPhone a meno che tu non scelga di scaricarli per la riproduzione offline.
{{% /details %}}

{{% details title="La condivisione file SMB è sicura?" closed="true" %}}
La condivisione file SMB funziona solo sulla tua rete locale. Altri dispositivi su reti diverse non possono accedere alle tue cartelle condivise. Per una sicurezza aggiuntiva, usa un nome utente e una password invece dell'accesso anonimo (Tutti).
{{% /details %}}
