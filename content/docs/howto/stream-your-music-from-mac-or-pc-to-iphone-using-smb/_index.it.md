---
title: "Riproduci la tua musica in streaming da Mac o PC su iPhone usando SMB"
description: "Scopri come riprodurre in streaming la tua collezione musicale da Mac o Windows PC sul tuo iPhone o iPad usando Evermusic e il protocollo SMB. Una semplice guida passo dopo passo per connettersi e godersi l'audio senza sincronizzazione."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["streaming musica da Mac a iPhone", "SMB audio streaming iOS", "configurazione Evermusic SMB", "collegare musica PC iPhone", "condivisione musica Mac iOS", "SMB Windows streaming file", "accesso Evermusic cartelle PC"]
---

{{< author-byline >}}


**In breve:** Usa l'app Evermusic per iPhone o iPad per riprodurre in streaming la musica dal tuo Mac o Windows PC tramite la tua rete locale usando SMB. Nessuna sincronizzazione, nessuna copia -- basta abilitare la condivisione file sul tuo computer, connettersi nell'app e riprodurre. La configurazione richiede meno di 5 minuti.

Stai affogando in un mare di musica sul tuo MAC o PC e vuoi goderti il tutto senza problemi sul tuo iPhone o iPad? Non cercare oltre Evermusic. Con Evermusic, è incredibilmente semplice collegare il tuo computer usando il protocollo SMB e riprodurre in streaming le tue melodie preferite senza preoccuparti di occupare spazio aggiuntivo sul dispositivo o affrontare problemi di sincronizzazione. Ecco una guida passo dopo passo per iniziare:

## Passo 1: Abilita il protocollo SMB sul tuo computer

![Evermusic - Supporto SMB - Schermata condivisione Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Se usi MAC

- Apri Preferenze di Sistema -> Condivisione.
- Abilita il servizio Condivisione File.
- Nella sezione "Cartelle condivise", aggiungi la tua cartella musicale, seleziona un utente e imposta i livelli di autorizzazione (Lettura e Scrittura o Solo Lettura).
- Per maggiore comodità, puoi selezionare "Tutti: Solo Lettura" per la cartella musicale, rendendola facilmente accessibile in Evermusic.
- Non dimenticare di ricordare l'URL del tuo computer (smb://192.168.xx.xx) per i prossimi passi.

![Evermusic - Supporto SMB - Schermata condivisione file](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Tocca "Opzioni" e abilita "Condividi file e cartelle usando SMB."
- Abilita "Condivisione file Windows" per gli account disponibili.

![Evermusic - Supporto SMB - Schermata condivisione file e cartelle](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Se usi un Windows PC

![Evermusic - Supporto SMB - Condivisione file su Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Fai clic destro sulla tua cartella musicale.
- Seleziona "Proprietà."
- Apri la scheda "Condivisione."
- Fai clic su "Condividi..."
- Scegli le persone con cui condividere e imposta i loro livelli di autorizzazione.
- Come con MAC, puoi optare per "Tutti: Lettura" per la cartella musicale selezionata.
- Fai clic su "Fatto" per salvare le tue impostazioni.

![Evermusic - Supporto SMB - Cartella condivisa su Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Passo 2: Aggiungi il tuo computer automaticamente

- Ora apri Evermusic e vai alla scheda "Connessioni" ("Rete" se stai usando una vecchia versione dell'app).
- Se vedi il tuo computer nella sezione "Dispositivi disponibili" ("Condivisioni disponibili" se stai usando una vecchia versione dell'app) e hai selezionato "Tutti: Solo Lettura" nel passo precedente, tocca semplicemente il tuo computer e si connetterà automaticamente.
- Se questo non accade, puoi aggiungere il tuo computer manualmente.

![Evermusic - Supporto SMB - Schermata connessione account](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Passo 3: Aggiungi il tuo computer manualmente

- Tocca "Connetti un servizio cloud" ("Aggiungi account" se stai usando una vecchia versione dell'app)
- Seleziona "SMB" dall'elenco dei server disponibili nella schermata successiva.
- Nella schermata delle impostazioni "SMB":
  - Inserisci l'URL del server con il percorso della cartella condivisa. Puoi inserire il nome del server o l'IP del server. Ad esempio:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Inserisci il tuo Nome utente e Password o lascia questi campi vuoti se hai selezionato "Tutti: Solo Lettura" nel passo precedente.
  - Il campo "WORKGROUP" è facoltativo e deve essere usato se hai un dominio Active Directory.

![Evermusic - Supporto SMB - Schermata inserimento credenziali](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Una volta connesso il tuo account SMB, apparirà nella sezione "Servizi cloud" ("Account"). Apri l'account connesso toccandolo, naviga alla cartella musicale e tocca qualsiasi file audio per avviare il lettore.

![Evermusic - Supporto SMB - Schermata apertura cartella connessa](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Goditi la tua collezione musicale senza problemi sul tuo iPhone o iPad con Evermusic.

![Evermusic - Supporto SMB - Schermata lettore audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Passo 4: Soluzione alternativa SMB2

Se riscontri problemi nella navigazione delle cartelle o nella riproduzione di file che contengono simboli speciali (come ü, ö, é), questo potrebbe essere correlato al protocollo SMB2. Stiamo lavorando attivamente per risolvere questo problema.

Come soluzione temporanea, prova ad abilitare SMB 1 sul tuo server e nelle impostazioni dell'app. In alternativa, puoi connetterti al tuo server SMB usando il menu di apertura file del sistema. Ecco come:

1. Naviga su "File locali."
2. Scorri verso il basso fino alla sezione "File su questo dispositivo" e tocca "Apri file..." o "Apri cartelle..."
3. Individua il tuo server e seleziona i file o le cartelle di cui hai bisogno.
4. Tocca "Apri" per confermare la tua selezione.

## Passo 5: Soluzione alternativa WebDAV

Inoltre, puoi provare a connetterti al tuo NAS usando i protocolli WebDAV o DLNA se supportati.

Seguendo questi passi, puoi aggirare i problemi relativi ai simboli speciali nei nomi dei file e continuare a goderti i tuoi file multimediali.

P.S. Puoi anche trasferire file audio dal tuo MAC/PC al tuo iPhone usando la Condivisione File di iTunes e riprodurre file audio locali. Scopri di più su questa funzione nella nostra guida: [Come riprodurre i file iTunes su iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Domande frequenti

{{% details title="Posso riprodurre in streaming la musica dal mio PC al mio iPhone senza iTunes?" closed="true" %}}
Sì. Evermusic si connette al tuo PC tramite SMB sulla tua rete Wi-Fi locale. iTunes non è necessario. Basta abilitare la condivisione file sul tuo PC e connettersi nell'app.
{{% /details %}}

{{% details title="Lo streaming SMB utilizza dati mobili?" closed="true" %}}
No. SMB funziona tramite la tua rete Wi-Fi locale. Non è necessaria una connessione Internet o dati mobili.
{{% /details %}}

{{% details title="Quali formati audio supporta Evermusic tramite SMB?" closed="true" %}}
Evermusic supporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC e altri formati audio comuni. I file vengono riprodotti direttamente dalla condivisione SMB.
{{% /details %}}

{{% details title="Posso riprodurre in streaming la musica da un NAS al mio iPhone?" closed="true" %}}
Sì. Se il tuo NAS supporta SMB (la maggior parte lo fa, inclusi Synology, QNAP e WD My Cloud), puoi connetterti ad esso usando gli stessi passi di questa guida.
{{% /details %}}

{{% details title="Devo tenere il mio computer acceso durante lo streaming?" closed="true" %}}
Sì. Poiché Evermusic riproduce in streaming i file direttamente dal tuo computer, deve essere acceso e connesso alla stessa rete del tuo iPhone.
{{% /details %}}

{{% details title="C'è un limite di dimensione file per lo streaming SMB?" closed="true" %}}
No. Evermusic riproduce in streaming file di qualsiasi dimensione tramite SMB. I file lossless di grandi dimensioni (FLAC, WAV) funzionano senza problemi.
{{% /details %}}
