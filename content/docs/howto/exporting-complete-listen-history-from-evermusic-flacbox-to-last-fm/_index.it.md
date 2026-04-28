---
title: "Esporta la cronologia di ascolto completa da Evermusic e Flacbox su Last.fm"
date: 2024-01-30
description: "Scopri come esportare la cronologia musicale da Evermusic e Flacbox e caricarla su Last.fm utilizzando file CSV e lo strumento Last.fm Scrubbler per Windows."
keywords: ["evermusic", "flacbox", "lastfm", "cronologia musicale", "scrobbling", "esportare brani", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recenti", "lastfm", "esportazione", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Riepilogo:** Esporta la cronologia di ascolto da Evermusic o Flacbox come file CSV, quindi caricala su Last.fm utilizzando lo strumento gratuito Last.fm-Scrubbler-WPF su Windows. Lo scrobbling automatico è disponibile anche nativamente in entrambe le app.

**Aggiornamento:** Lo scrobbling automatico è ora disponibile! Scopri di più qui: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

Lo scrobbling è un modo semplice per salvare automaticamente dettagli di base come il titolo e l'artista del brano che stai ascoltando in un servizio online. Successivamente, puoi rivedere la tua cronologia di ascolto.

[Last.fm](https://www.last.fm/home), alimentato da un sistema di raccomandazione musicale chiamato Audioscrobbler, offre questo servizio gratuitamente. Crea un profilo dettagliato del tuo gusto musicale registrando i brani che ascolti, che siano da stazioni radio internet, dal tuo computer o da vari dispositivi musicali portatili. Puoi visitare il sito web in seguito per ricevere raccomandazioni per nuovi artisti o album che corrispondono al tuo gusto musicale.

Puoi caricare la tua cronologia di ascolto su [Last.fm](http://Last.fm) dalle app Evermusic e Flacbox utilizzando uno strumento gratuito, e ti guideremo attraverso il processo.

Apri la sezione 'Libreria musicale' dell'applicazione e scorri fino alla sezione 'Accesso rapido'. Tocca la voce di menu 'Recenti'.

![schermata libreria musicale](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

Nella schermata 'Recenti' tocca il pulsante 'Altro' nell'angolo in alto a destra per attivare il menu 'Altre azioni'. Tocca la voce di menu 'Esporta elenco brani'.

![schermata recenti](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

Nella schermata 'Seleziona formato file' hai la possibilità di selezionare il formato del file di destinazione. Opzioni disponibili - CSV, TXT, M3U.

![schermata seleziona formato file](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Significa Valori Separati da Virgola, perfetto per organizzare i tuoi dati in un formato tabella ordinato. Nel file di destinazione, troverai parametri come Nome Artista, Nome Album, Nome Brano, Timestamp (il momento in cui hai ascoltato i brani), Nome Artista Album e Durata Brano.

TXT: Qui parliamo di un file di testo semplice. È semplice e diretto, con parametri che includono Nome Artista, Nome Album, Nome Brano e Durata.

M3U: Questo formato è essenzialmente lo standard per la creazione di playlist. È ottimo perché puoi esportare la tua lista di brani e goderti le tue tracce su qualsiasi dispositivo, anche se non hai i file originali (a patto che selezioni l'opzione URL assoluto per i file multimediali). Nel file di output, troverai parametri come Durata, Nome Artista, Nome Brano e Posizione File Multimediale.

Per il nostro compito, selezionare CSV è la strada giusta. Useremo questo file con il software gratuito Last.fm-Scrubbler-WPF per caricare la nostra cronologia di ascolto sul servizio [Last.fm](http://Last.fm). Scegli semplicemente CSV e premi il pulsante 'Esporta'.

![schermata esportazione completata](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Dopo il completamento dell'esportazione, tocca semplicemente il pulsante 'Mostra file', e l'app rivelerà il file creato nella tua cartella documenti. Quindi, tocca il pulsante 'Altre azioni' accanto al nome del file e seleziona l'opzione 'Apri in' dal menu. Il nostro prossimo passo è copiare il file esportato sul tuo computer desktop. Puoi farlo facilmente selezionando l'opzione AirDrop dal menu 'Apri in'.

![altre azioni per il file esportato](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

Successivamente, useremo un client [Last.FM](http://Last.FM) gratuito open source disponibile solo sulla piattaforma Windows. Questo client ti permette di aggiornare efficacemente la tua cronologia di ascolto su [Last.FM](http://Last.FM) utilizzando il file CSV che abbiamo appena esportato.

Se attualmente non stai usando un computer Windows, non preoccuparti. Puoi accedere a questo client installando VirtualBox sul tuo Mac e usando il file immagine ufficiale dell'ambiente di sviluppo Windows.

Ecco cosa devi fare:

- Installa VirtualBox dal seguente link: [Scarica VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Scarica e installa l'ambiente di sviluppo Windows da questo link: [Ambiente di sviluppo Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

Sul tuo computer Windows (o app VirtualBox con immagine Windows Development) scarica e installa [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - software gratuito open source disponibile su GitHub. Abbiamo testato la versione 1.28 che puoi scaricare qui: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![pagina di download Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

Nella sezione 'Assets' tocca [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) per scaricare l'archivio di installazione. Decomprimi il file scaricato e apri la cartella decompressa.

- IMPORTANTE

Questa app è ancora in beta. I creatori dell'app non hanno fatto molti test. Raccomandano di provare prima a fare scrobbling su un account di prova e verificare se le cose che vuoi scrobblare funzionano correttamente. Specialmente se fai scrobbling di molti brani contemporaneamente. Per favore, fai attenzione con i tuoi account.

Esegui Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

Nella schermata principale dell'applicazione, tocca semplicemente 'Non connesso', situato nell'angolo in basso a sinistra, per attivare la schermata 'Aggiungi account'.

![schermata aggiungi account](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Inserisci le tue credenziali di accesso.

![schermata inserimento credenziali](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Tocca il pulsante 'Accedi' per aggiungere il tuo account.

![Tocca il pulsante Accedi per aggiungere il tuo account.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Apri la scheda 'File Parse Scrobbler' per iniziare l'importazione del file CSV dall'app Evermusic.

![Apri la scheda File Parse Scrobbler per iniziare l'importazione del file CSV dall'app Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Scegli 'Parser: CSV' e tocca il pulsante 'Impostazioni'.

Nella schermata successiva, puoi scegliere l'ordine dei parametri nel tuo file CSV.

I campi individuali possono essere racchiusi tra virgolette e DEVONO essere racchiusi tra virgolette se il campo contiene uno dei delimitatori impostati. Ad esempio:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Quindi lascia tutte le impostazioni predefinite, l'unica cosa che devi cambiare è abilitare la casella di controllo nel campo 'Has Fields Enclosed In Quotes'.

Tocca 'Salva e chiudi' per applicare le modifiche.

![scegli l'ordine dei parametri nel tuo file CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

Lo scrobbling di analisi file ha due modalità. Possono essere cambiate con il ComboBox 'Scrobbling Mode'.

Modalità Normale: In questa modalità, i brani verranno scrobblati con il timestamp dello scrobble analizzato. Solo gli scrobble più recenti di 14 giorni possono essere scrobblati.

Modalità Importazione: In questa modalità, i brani verranno scrobblati con il timestamp calcolato dal 'Tempo di Fine' e dalla durata selezionata tra ogni brano. Questo consente lo scrobbling dei brani anche se il timestamp dello scrobble analizzato è più vecchio di 14 giorni. Pertanto il primo brano (più in alto) nel file CSV verrà scrobblato con il 'Tempo di Fine'.

Scegli un file CSV precedentemente generato dall'app Evermusic nel campo 'File:' e tocca 'Parse'. In alcuni casi, potresti vedere un avviso di errore che dice che alcuni scrobble non sono stati analizzati. Va bene se hai alcuni brani senza metadati completi come il Nome Artista.

![alcuni scrobble non sono stati analizzati](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Tocca il pulsante 'Seleziona tutto' per selezionare tutti i brani analizzati.

![Tocca il pulsante Seleziona tutto per selezionare tutti i brani analizzati.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Tocca il pulsante 'Anteprima' per verificare tutte le modifiche che verranno pubblicate sul server.

![Tocca il pulsante Anteprima per verificare tutte le modifiche che verranno pubblicate sul server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Tocca il pulsante 'Scrobble' per caricare tutte le modifiche sul server.

![Tocca il pulsante Scrobble per caricare tutte le modifiche sul server.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

In precedenza Last.fm-Scrubbler-WPF non aveva un limite giornaliero di scrobble. Questo è cambiato poiché alcune persone hanno usato Scrubbler per fare scrobbling di così tanti brani da causare problemi alla pagina Last.fm. Il limite di scrobbling è attualmente di 2800 scrobble al giorno. Quando provi a scrobblare di più riceverai un messaggio di errore. Ci sono piani per aggiungere una 'coda di scrobbling', quindi se hai bisogno di scrobblare più di 2800 brani, verranno aggiunti a una coda e scrobblati automaticamente dopo qualche tempo. Puoi controllare quanti scrobble ti restano nella vista di selezione utente.

Una volta che tutti i record sono stati caricati con successo sul server, vedrai un messaggio nella parte inferiore della finestra dell'app che conferma: 'Brani selezionati scrobblati con successo.'

![Brani selezionati scrobblati con successo.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Ora puoi aprire il tuo profilo sulla pagina [Last.fm](http://Last.fm) e verificare tutte le modifiche.

![il tuo profilo sulla pagina Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Domande frequenti

{{% details title="Posso fare scrobbling automaticamente senza esportare file CSV?" closed="true" %}}
Sì. Sia Evermusic che Flacbox ora supportano lo scrobbling automatico su Last.fm. Consulta la guida: [Come fare scrobbling su Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="E se il mio CSV ha brani più vecchi di 14 giorni?" closed="true" %}}
Usa la Modalità Importazione in Last.fm-Scrubbler-WPF. Ricalcola i timestamp dal Tempo di Fine, permettendoti di fare scrobbling dei brani indipendentemente dalla loro data originale.
{{% /details %}}

{{% details title="Non ho un computer Windows. Posso comunque usare Last.fm-Scrubbler?" closed="true" %}}
Sì. Installa VirtualBox sul tuo Mac e scarica l'immagine gratuita dell'ambiente di sviluppo Windows da Microsoft. Esegui Last.fm-Scrubbler-WPF all'interno della macchina virtuale.
{{% /details %}}

{{% details title="Perché alcuni scrobble non vengono analizzati?" closed="true" %}}
I brani privi di metadati essenziali (come il nome dell'artista) non possono essere analizzati. Questo è previsto e non influisce sugli altri brani nel file.
{{% /details %}}

{{% details title="C'è un limite giornaliero di scrobbling?" closed="true" %}}
Sì. Last.fm-Scrubbler-WPF consente fino a 2.800 scrobble al giorno. Se hai bisogno di fare più scrobble, dividi il processo su più giorni.
{{% /details %}}
