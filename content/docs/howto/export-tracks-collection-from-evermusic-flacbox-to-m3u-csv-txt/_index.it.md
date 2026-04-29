---
title: "Come esportare la collezione di brani in M3U, CSV e TXT in Evermusic e Flacbox"
date: 2024-01-31
description: "Scopri come esportare i recenti, i preferiti, le playlist e gli album da Evermusic e Flacbox nei formati M3U, CSV o TXT. Perfetto per lo scrobbling su Last.fm e la riproduzione su altri dispositivi."
keywords: ["evermusic esportazione", "flacbox esportazione", "esportare in m3u", "esportare playlist in csv", "m3u txt csv playlist", "esportazione musica"]
tags: ["evermusic", "recenti", "preferiti", "esportazione", "m3u", "playlist", "csv", "txt", "album"]
---

{{< author-byline >}}


**In breve:** Evermusic e Flacbox ti permettono di esportare qualsiasi collezione di brani (recenti, preferiti, playlist, album) in file CSV, TXT o M3U. Usa queste esportazioni per lo scrobbling su Last.fm, il backup della tua libreria o la riproduzione delle tue playlist su altri dispositivi.

## Introduzione

Esportare i tuoi recenti, preferiti, album e playlist dall'app in un file esterno può essere incredibilmente utile. Puoi usare questi file per aggiornare la tua cronologia di ascolto su servizi di scrobbling come [Last.fm](http://Last.fm) o ascoltare le tue playlist su dispositivi esterni. Con Evermusic e Flacbox, questo processo è semplice. Qui ti mostreremo come esportare i tuoi recenti in CSV/TXT e le tue playlist in M3U. Tuttavia, questa funzionalità è disponibile per qualsiasi collezione di brani all'interno dell'app.

## Scegli il formato

Per esportare i tuoi recenti, apri la sezione 'Libreria musicale' e seleziona la voce di menu 'Recenti'.

![libreria musicale](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

Nella schermata successiva, tocca il pulsante 'Altro' nell'angolo in alto a destra e scegli 'Esporta elenco brani'.

![esporta recenti](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

Nella schermata 'Seleziona formato file' hai diverse opzioni - CSV, TXT, M3U.

- CSV

Questo sta per Comma-Separated Values (valori separati da virgola), perfetto per organizzare i tuoi dati in un formato tabellare ordinato. Nel file di destinazione troverai parametri come Nome artista, Nome album, Nome brano, Timestamp (l'ora in cui hai ascoltato i brani), Nome artista dell'album e Durata del brano. Puoi usare quel file in seguito per aggiornare la tua cronologia di ascolto su servizi di scrobbling come [Last.fm](http://Last.fm) come descritto [qui](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Qui parliamo di un semplice file di testo. È semplice e diretto, con parametri che includono Nome artista, Nome album, Nome brano e Durata. Utile se hai solo bisogno di un elenco di brani in formato testuale.

- M3U

Questo formato è essenzialmente lo standard per la creazione di playlist. È ottimo perché puoi esportare la tua lista di brani e goderti le tue tracce su qualsiasi dispositivo, anche se non hai i file originali (se selezioni l'opzione URL assoluto per l'esportazione dei file multimediali). Nel file di output troverai parametri come Durata, Nome artista, Nome brano e Posizione del file multimediale.

## Formato CSV

Ora selezioniamo CSV e vediamo cosa otterremo. Scegli semplicemente CSV e premi il pulsante 'Esporta'.

![seleziona formato file](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Una volta completata l'esportazione, vedrai un avviso con due opzioni. Toccando 'Mostra file' verrà mostrato il file risultante nella directory dei documenti.

![esportazione completata](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Ora puoi inviare quel file, aprirlo in un editor di testo esterno o usarlo per aggiornare i tuoi progressi di ascolto su [Last.fm](http://Last.fm).

![cartella di esportazione con file risultanti](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

Il file CSV di output conterrà i campi nel seguente formato:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Ad esempio:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![file csv esportato](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formato TXT

Il file TXT di output conterrà i campi nel seguente formato:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Ad esempio:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![file txt esportato](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formato M3U

Successivamente, ti guideremo attraverso l'esportazione della tua playlist nel formato M3U, che è lo standard de facto per i file playlist. Il prerequisito principale per un'esportazione riuscita della playlist è che tutti i file nella playlist devono trovarsi nello stesso archivio, che si tratti di un servizio cloud come Google Drive, file locali o file sul tuo dispositivo. Per iniziare il processo di esportazione, apri qualsiasi playlist e tocca il pulsante 'Altro' nell'angolo in alto a destra, poi scegli la voce di menu 'Esporta elenco brani'.

![schermata playlist](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

Nella schermata successiva, seleziona il formato file 'M3U', dove troverai due opzioni per il 'Tipo di posizione file multimediale':

![schermata selezione formato file di esportazione](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Se scegli 'Percorso relativo', la playlist verrà creata con le posizioni dei file multimediali scritte in modo relativo rispetto al file della playlist. Ad esempio:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   In questo caso, evita di modificare la posizione del file M3U dopo il completamento dell'esportazione, poiché ciò interromperà i percorsi dei file multimediali. Per avviare la riproduzione della tua playlist, tocca semplicemente il file della playlist esportata e l'app troverà automaticamente i file multimediali nel tuo archivio e avvierà la riproduzione. Puoi anche esportare le tue playlist nell'archivio e poi reimportarle sul tuo nuovo dispositivo.

2. Se scegli 'URL Assoluto', l'app genererà URL diretti per i tuoi file multimediali. Questo ti permette di riprodurre la playlist su qualsiasi dispositivo/applicazione senza bisogno che tutti i file multimediali si trovino nello stesso archivio del file della playlist. Questa opzione è supportata solo per i servizi di archiviazione cloud in grado di generare URL diretti dei file. Tuttavia, tieni presente che in alcuni casi gli URL generati potrebbero avere una durata limitata e possono scadere dopo un certo tempo. Ecco l'elenco dei servizi cloud supportati: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (se in modalità ospite)  

L'URL del file multimediale di output sarà qualcosa del tipo:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Dopo aver selezionato il 'Tipo di posizione file multimediale', tocca 'Esporta'. L'app ti chiederà di scegliere una cartella di destinazione per l'esportazione del file M3U. Tocca 'Fatto' per confermare la tua selezione.

![seleziona una cartella](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

L'app genererà un file M3U e lo caricherà/sposterà nella cartella di destinazione.

![caricamento file m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Una volta completata l'esportazione, apparirà un avviso di sistema con l'opzione 'Mostra file'.

![avviso esportazione completata](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Toccando questo verrà mostrato il file esportato nell'app.

![file m3u esportato nell'elenco file](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Se hai selezionato 'Percorso relativo' come 'Tipo di posizione file multimediale' nel passaggio precedente, il file di output sarà nel seguente formato:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![esempio m3u con percorsi relativi](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Per l'opzione 'URL Assoluto', l'app genererà un file M3U nel formato:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![esempio m3u con URL assoluti dei file](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Puoi aprire quel file su qualsiasi dispositivo/applicazione che supporta le playlist M3U.

![playlist m3u aperta in un'app esterna](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Considerazioni finali

Esportare i tuoi brani da Evermusic e Flacbox ti dà il completo controllo sui tuoi dati musicali. Che tu stia facendo il backup della cronologia di ascolto, scrobblando su Last.fm o godendoti le playlist su dispositivi esterni, queste opzioni di esportazione: M3U, CSV e TXT - sono strumenti potenti progettati per flessibilità e compatibilità. Approfitta di queste funzionalità per migliorare il modo in cui organizzi, condividi e riscopri la tua collezione musicale su diverse piattaforme.

## Domande frequenti

{{% details title="Quale formato di esportazione dovrei usare per lo scrobbling su Last.fm?" closed="true" %}}
Usa il CSV. Include timestamp e metadati completi richiesti dagli strumenti di scrobbling come Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="Posso esportare qualsiasi collezione di brani, non solo le playlist?" closed="true" %}}
Sì. Puoi esportare recenti, preferiti, album, playlist e qualsiasi altra collezione di brani nell'app usando gli stessi passaggi.
{{% /details %}}

{{% details title="La mia playlist M3U funzionerà su altri dispositivi?" closed="true" %}}
Se scegli l'opzione URL Assoluto durante l'esportazione, il file M3U può essere riprodotto su qualsiasi dispositivo che supporta le playlist M3U. Tieni presente che alcuni URL cloud potrebbero scadere nel tempo.
{{% /details %}}

{{% details title="La funzione di esportazione è gratuita?" closed="true" %}}
Sì. L'esportazione delle collezioni di brani in M3U, CSV e TXT è disponibile sia nella versione gratuita che in quella premium di Evermusic e Flacbox.
{{% /details %}}

{{% details title="Quali servizi cloud supportano l'esportazione con URL Assoluto?" closed="true" %}}
L'esportazione con URL Assoluto è supportata per iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive e WebDAV (modalità ospite).
{{% /details %}}
