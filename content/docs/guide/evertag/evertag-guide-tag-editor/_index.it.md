---
title: "Editor tag"
date: 2020-02-01
description: "Scopri come usare l'Editor tag di Evertag per aggiornare i metadati musicali, modificare le copertine degli album, eseguire la modifica batch di più file e gestire i tag da MusicBrainz. Ideale per organizzare la tua libreria musicale su iOS e Mac."
keywords: [
  "editor tag Evertag", "editor metadati audio", "editor tag musicali",
  "modifica tag audio iPhone", "editor copertina album", "modifica batch tag audio",
  "metadati MusicBrainz", "app organizzatore musicale", "guida Evertag", "editor tag ID3"
]
tags: ["guida", "evertag", "editor tag"]
readingTime: 5
---


**L'Editor tag** è la schermata principale dell'app Evertag dove puoi visualizzare e modificare i metadati dei file audio. Apri questa schermata toccando un file dalla sezione **File locali** o da qualsiasi account di **archiviazione cloud** connesso.

{{< cards cols="1">}}
  {{< card title="" subtitle="Schermata Editor tag Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Modalità di modifica

Evertag fornisce due modalità di modifica:

- **Modalità file singolo**  
  - Naviga tra i file scorrendo a sinistra o a destra sul carosello delle copertine.  

- **Modalità batch**  
  - Modifica più file contemporaneamente e applica metadati condivisi.  
  - Per attivare, scorri in basso e tocca **Modifica file contemporaneamente**.

## Modalità file singolo

Per impostazione predefinita, l'app apre l'editor tag in modalità file singolo con solo le opzioni di modifica principali abilitate. In questa modalità puoi modificare i campi di metadati più comuni, come:

**Titolo brano, Sottotitolo, Artista album, Album, Artista, Compositore, Esecutore, Genere, Commento, Battiti per minuto, Podcast, Compilation, Numero disco, Numero brano, Totale brano, Valutazione, Anno**

Per accedere a tutti i tag disponibili, scorri fino in fondo alla schermata e tocca l'opzione **Mostra tag estesi**. Questo commuta l'editor in modalità estesa, permettendoti di modificare oltre **120 campi di metadati**, inclusi **Tag MusicBrainz**, **Testi**, **Classificazioni consultive**, valori replay-gain, ordini di ordinamento, metadati podcast e altro. Usa **Impostazioni → Editor tag audio → Pulsanti sulla schermata principale** per attivare in modo permanente Mostra tag estesi in modo che sia sempre attivo.

{{< cards cols="1">}}
{{< card title="" subtitle="Pannello azioni in basso" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Modalità batch

Puoi accedere alla modifica batch in due modi:

1. **Dal Gestore file**  
   - Tocca **Altre azioni** (•••) in alto a destra.  
   - Tocca **Selezionare**, scegli più file, poi tocca **Modificare i tag audio**.

2. **Dall'Editor tag**  
   - Apri qualsiasi file, scorri in basso e tocca **Modifica file contemporaneamente** per caricare tutti i file dalla stessa cartella.

{{< cards cols="1">}}
{{< card title="" subtitle="Modalità modifica batch" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Dopo la modifica, tocca **Salvare** per applicare le modifiche.

## Modifica testi

L'editor esteso espone il campo **Testi**. Toccalo per aprire l'elenco dei testi — ogni voce di testi ha la propria lingua e descrizione, quindi un singolo brano può memorizzare più traduzioni.

Non devi digitare i testi da zero. L'editor include scorciatoie di ricerca con un tocco verso i database di testi più popolari sul web, pre-compilati con l'artista e il titolo del brano corrente:

- **Lrclib** — il database pubblico principale per **testi temporizzati (in stile LRC)**. Usalo quando vuoi testi sincronizzati che scorrono riga per riga nei lettori che li supportano.
- **Genius** — ampio catalogo con annotazioni e testi in testo normale accurati.
- **Lyricsify** — database gestito dalla community con testi normali e temporizzati.
- **Google** — una ricerca web generale come fallback quando i database dedicati non hanno una corrispondenza.

Ogni scorciatoia appare solo quando il servizio corrispondente è raggiungibile dal tuo dispositivo. Tocca un servizio, copia i testi (o i timestamp LRC) che desideri, torna su Evertag e incollali nel campo di testo — poi **Salvare** per scrivere i testi nei tag del file audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pagine testi" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Scegli una lingua dal selettore:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selettore lingua testi" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Poi incolla o digita il testo dei testi. Evertag supporta sia testo normale che testi temporizzati (sincronizzati) — il segnaposto mostra un esempio del formato in stile LRC, che è esattamente ciò che Lrclib e Lyricsify restituiscono per i risultati sincronizzati.

{{< cards cols="1">}}
  {{< card title="" subtitle="Editor di testo testi" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Imposta una valutazione e una valutazione consultiva

L'editor esteso offre un controllo a stelle **Valutazione** insieme a un controllo segmentato **Valutazione consultiva**.

### Valutazione a stelle

Usa il campo **Valutazione** per assegnare a un brano un punteggio personale da una a cinque stelle. Il valore viene scritto nel tag di valutazione standard del file (POPM per ID3, `rate` per MP4, `RATING` per Vorbis/APE, ecc.), quindi altre app che leggono questo tag — inclusa l'app Musica, Plex, Roon e la maggior parte degli editor tag desktop — raccoglieranno immediatamente i tuoi punteggi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Valutazione" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Valutazione consultiva

La **Valutazione consultiva** contrassegna il contenuto di un brano usando uno dei valori dello standard Parental Advisory che l'iTunes Store e la maggior parte delle piattaforme musicali utilizzano:

- **Non offensivo** — il default per i brani senza informazioni di controllo parentale. Il file è trattato come adatto a tutti gli ascoltatori e non mostrerà alcuna etichetta consultiva nei lettori che rispettano il tag.
- **Esplicito** — il brano contiene linguaggio o contenuti espliciti. I lettori che rispettano i controlli parentali (l'app Musica, l'app Apple TV, le esportazioni Spotify, Plex, ecc.) visualizzeranno un badge **E** accanto al titolo e, quando le restrizioni sono abilitate sul dispositivo o sull'account, potrebbero nascondere il brano dai profili per bambini o rifiutare di riprodurlo.
- **Pulito** — una versione censurata o modificata di un brano altrimenti esplicito. I lettori visualizzano un badge **C** in modo che gli ascoltatori possano distinguere un'edizione pulita dal master esplicito originale, il che è utile quando entrambe le versioni si trovano nella stessa libreria.

Vuoi impostare o correggere questo campo quando:

- Un file ha l'etichetta sbagliata (ad esempio un'edizione radio pulita erroneamente contrassegnata come Esplicita, o viceversa).
- I brani sono stati estratti o scaricati senza il tag e ora vengono visualizzati come Non offensivi anche se contengono contenuti espliciti — necessario per far funzionare correttamente i controlli parentali e le librerie condivise in famiglia.
- Stai preparando un album per la presentazione o la condivisione e hai bisogno che ogni brano abbia metadati coerenti.
- Vuoi che CarPlay, la schermata di blocco, i lettori in stile Apple Music o il software DJ mostrino il badge corretto **E** / **C** accanto al titolo del brano.

Il valore è memorizzato nel campo di valutazione consultiva standard per il formato file (`rtng` per MP4, `TXXX:ITUNESADVISORY` per ID3, `ITUNESADVISORY` per Vorbis), quindi qualsiasi lettore che legge i metadati di controllo parentale vedrà il tuo aggiornamento.

{{< cards cols="1">}}
  {{< card title="" subtitle="Valutazione consultiva testi" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Modifica la copertina dell'album

Per cambiare una copertina dell'album:

1. Tocca l'**icona Fotocamera** nel carosello delle copertine.  
2. Scegli la posizione dell'immagine: File locali, Cloud, Download o Libreria Foto.  
3. Seleziona un'immagine da applicare come copertina.

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleziona immagine" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Altre azioni nell'Editor tag

Ulteriori opzioni di modifica sono disponibili tramite la barra degli strumenti sotto la vista delle copertine.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu altre azioni" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Ricerca automatica tag audio

Questa azione attiva il motore di ricerca tag intelligente, che trova e compila i metadati completi per il tuo file audio in base alle informazioni esistenti.  
L'app usa il database MusicBrainz — uno dei database tag più completi — con oltre **50 milioni** di brani.

### Cerca copertina album

Usa i metadati per cercare sul web la copertina dell'album corretta.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Cerca copertina album" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Una volta trovata, salva l'immagine nelle tue **Foto** usando il menu contestuale di sistema.

{{< cards cols="1">}}
  {{< card title="" subtitle="Aggiungi immagine a Foto" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Successivamente, torna all'editor tag, tocca l'icona Fotocamera, vai alla **Libreria Foto** e seleziona l'immagine salvata. L'app la imposterà come copertina per il tuo file audio.

Puoi regolare come le immagini di copertina vengono ridimensionate nelle impostazioni dell'app.

### Salva copertina album

Questa azione salva la copertina dell'album corrente nella cartella **Documents**, in modo da poterla riutilizzare in seguito.

### Normalizza codifica

Questa azione normalizzerà la codifica del testo di tutti i tag nei metadati del file audio. È particolarmente utile se stai passando da un PC Windows, dove i file potrebbero usare codifiche diverse che appaiono come caratteri illeggibili o confusi su un Mac.

### Ricerca manuale tag

Cerca i metadati dell'album manualmente usando il database MusicBrainz.  

- Seleziona l'album  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleziona album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Scegli la canzone corretta  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleziona canzone" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Scegli quali tag applicare  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleziona tag audio" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Tocca **Fatto** per applicare i metadati selezionati al tuo brano.

### Elimina tag audio

Cancella tutti i campi di metadati per un file. Utile quando si riparte da zero. Tocca **Salvare** per confermare.

## Impostazioni editor tag

Vai a **Impostazioni → Editor tag audio** per personalizzare il comportamento.

### Ridimensionamento copertina album

Seleziona come le copertine degli album devono essere ridimensionate quando salvate nei file audio. Puoi disabilitare il ridimensionamento per mantenere la dimensione originale dell'immagine, ma tieni presente che alcuni lettori potrebbero non supportare file di copertina di grandi dimensioni. L'opzione "dimensione originale" fa parte delle funzionalità di personalizzazione Premium.

### Opzioni di salvataggio tag

- **ID3v2.4** — Quando abilitato, l'app salva i tag nel formato ID3v2.4 quando possibile. Disabilita per tornare al ID3v2.3 più ampiamente supportato se i tuoi tag audio non vengono visualizzati correttamente su lettori o dispositivi più vecchi.
- **Tag duplicati** — Quando abilitato, i campi di metadati comuni vengono duplicati in entrambe le sezioni tag del file. Questo migliora la compatibilità con i vecchi lettori audio, ma nella maggior parte dei casi non è necessario.

### Opzioni di aggiornamento dei metadati dei file cloud

Puoi controllare come l'app aggiorna i metadati per i file audio memorizzati nei servizi cloud:

- **Mostra messaggio di conferma**  
  Chiedi prima di applicare le modifiche ai metadati ai file cloud.

- **Aggiorna automaticamente i metadati del file**  
  Salva le modifiche ai metadati nel file cloud automaticamente dopo la modifica.

- **Non aggiornare i metadati del file**  
  Salta l'aggiornamento dei file cloud — le modifiche verranno applicate solo localmente.

### Modifica file online

Scegli cosa accade alle copie scaricate localmente dei file cloud dopo la modifica:

- **Elimina sempre il file scaricato**  
  Rimuovi la copia locale dopo aver salvato le modifiche.

- **Non eliminare il file scaricato**  
  Mantieni il file scaricato sul dispositivo dopo la modifica.

### Pulsanti schermata principale

Personalizza quali azioni appaiono nella schermata principale dell'editor tag (Ricerca automatica tag audio, Ricerca manuale tag audio, Cerca copertina album, Salva copertina album, Normalizza codifica, Elimina tag audio). Puoi anche attivare **Mostra tag estesi** e **Modifica file contemporaneamente** in modo che l'editor si apra sempre nella tua modalità preferita.
