---
title: "Come importare una playlist M3U in Evermusic e Flacbox"
date: 2024-01-31
description: "Scopri come importare file playlist M3U, M3U8 e CUE dal cloud, dall'archiviazione locale o dal dispositivo in Evermusic e Flacbox."
keywords: ["evermusic", "flacbox", "playlist", "m3u", "m3u8", "cue", "importare", "app musicale"]
tags: ["evermusic", "importare", "playlist", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Riepilogo:** Evermusic e Flacbox supportano l'importazione di file playlist M3U, M3U8 e CUE dall'archiviazione cloud, dai file locali dell'app o dal tuo dispositivo. Vai su Playlist > Altro > Importa playlist, seleziona una fonte, scegli il tuo file e l'app crea automaticamente la tua playlist.

M3U, che sta per MP3 URL o Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, è un formato di file per computer utilizzato per le playlist multimediali. Uno dei suoi usi principali è creare file playlist a singola voce che puntano a stream su Internet. Questi file offrono un accesso comodo ai contenuti in streaming e sono comunemente usati per download, e-mail e ascolto di radio Internet.

Nonostante il suo uso diffuso, non esiste una specifica formale per il formato M3U; è diventato uno standard de facto. Un file M3U è essenzialmente un file di testo semplice che specifica le posizioni di uno o più file multimediali. A seconda della codifica, viene salvato con l'estensione "m3u" o "m3u8". Ogni voce nel file specifica la posizione di un file multimediale, che può essere un percorso locale assoluto, un percorso locale relativo alla posizione del file M3U o un URL. Le voci sono separate da interruzioni di riga, con alcuni dispositivi che richiedono interruzioni di riga rappresentate come CR LF.

Inoltre, i file M3U possono includere commenti preceduti dal carattere "#". Nel M3U esteso, "#" introduce direttive M3U estese, che possono supportare parametri terminati con due punti ":".

Nelle nostre app Evermusic e Flacbox, abbiamo implementato la funzionalità di importazione file M3U, eliminando la necessità di creare playlist manualmente. Questa guida ti accompagnerà nell'importazione delle tue playlist dall'archiviazione cloud, dai file locali o dai file sul tuo dispositivo direttamente nell'app.

Per prima cosa, naviga alla sezione 'Playlist'. Quindi, tocca il pulsante 'Altro' situato nell'angolo in alto a destra. Dal menu che appare, seleziona l'opzione 'Importa playlist'.

![azione di importazione playlist](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

Nella schermata successiva, scegli la posizione del file. Le opzioni supportate includono:

- Archiviazione cloud connessa;
- File nell'applicazione;
- File sul tuo dispositivo;

![seleziona posizione file](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Selezioniamo l'archiviazione cloud connessa e apriamo la cartella contenente il file playlist. Le estensioni di file playlist supportate includono M3U, M3U8 e CUE. Seleziona il file playlist e tocca 'Fatto' per confermare la selezione.

![seleziona file M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

L'app analizzerà il file playlist e creerà un elenco di brani. Quindi localizzerà quei file nell'archiviazione e compilerà una playlist finale che verrà importata nella libreria musicale. È fondamentale che il tuo file M3U/CUE contenga i percorsi corretti per i file multimediali e che i file si trovino in quei percorsi nella tua archiviazione.

![playlist importata](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

L'app supporta sia percorsi relativi che URL di file assoluti.

Ad esempio:

Playlist con percorsi relativi:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Playlist con URL assoluti:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Se importi un file playlist situato all'interno dell'app (sezione File locali), non sono necessari passaggi aggiuntivi.

Tuttavia, se vuoi importare una playlist situata sul tuo dispositivo utilizzando il selettore file di sistema, c'è una considerazione importante da tenere presente.

A causa delle politiche di sicurezza, l'applicazione può accedere solo al file che selezioni tramite il selettore file di sistema. Tuttavia, il file playlist potrebbe includere collegamenti ad altri file multimediali sul tuo dispositivo. Per importare una playlist dal tuo dispositivo, devi selezionare una cartella contenente sia il file playlist che tutti i file multimediali collegati ad esso. In questo caso, l'app scansionerà la cartella selezionata, troverà il file playlist, costruirà l'elenco dei brani e lo importerà nella libreria musicale.

Inoltre, puoi importare più playlist contemporaneamente toccando il pulsante "Altre azioni" e selezionando "Importa playlist da una cartella". L'app scansionerà quindi il contenuto della cartella, troverà i file playlist supportati e li importerà nella libreria.

## Domande frequenti

{{% details title="Quali formati di playlist supportano Evermusic e Flacbox?" closed="true" %}}
Entrambe le app supportano i formati di file playlist M3U, M3U8 e CUE. Questi coprono gli standard di playlist più comuni utilizzati dai lettori musicali e dai software multimediali.
{{% /details %}}

{{% details title="Posso importare playlist dall'archiviazione cloud?" closed="true" %}}
Sì. Puoi importare file playlist da qualsiasi servizio di archiviazione cloud connesso, inclusi Google Drive, Dropbox, OneDrive e server WebDAV.
{{% /details %}}

{{% details title="Perché mancano alcuni brani dopo l'importazione?" closed="true" %}}
Il file playlist deve contenere percorsi corretti verso i tuoi file multimediali e quei file devono esistere nelle posizioni specificate nella tua archiviazione. Verifica che i percorsi dei file nel tuo file M3U o CUE corrispondano alle posizioni effettive dei file.
{{% /details %}}

{{% details title="Posso importare più playlist contemporaneamente?" closed="true" %}}
Sì. Usa il pulsante Altre azioni e seleziona "Importa playlist da una cartella". L'app scansiona la cartella per tutti i file playlist supportati e li importa in un unico passaggio.
{{% /details %}}

{{% details title="Devo creare le playlist manualmente?" closed="true" %}}
No. La funzione di importazione elimina la creazione manuale delle playlist. Basta puntare l'app al tuo file M3U, M3U8 o CUE esistente e crea la playlist automaticamente.
{{% /details %}}
