---
title: "Come abilitare il server multimediale DLNA su Windows 10 e riprodurre la musica su iPhone"
date: 2019-11-26
description: "Abilita il server DLNA su Windows 10 e trasmetti la tua musica su iPhone con l'app Evermusic. Guida alla configurazione passo dopo passo inclusa."
keywords: ["evermusic", "dlna", "windows 10", "streaming musica iphone", "server multimediale", "rete locale", "upnp"]
tags: ["evermusic", "musica", "cloud", "iphone", "archiviazione", "locale", "nas", "windows", "wifi", "ascoltare", "rete", "remoto", "casa", "online", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**In breve:** Windows 10 ha un server DLNA integrato. Abilitalo nelle impostazioni di Rete e condivisione, poi usa l'app gratuita **Evermusic** sul tuo iPhone per trasmettere in streaming l'intera libreria musicale via Wi-Fi. Nessun software server di terze parti necessario.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Copertina" caption="Streaming musicale DLNA su iPhone usando Windows 10 ed Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) è uno strumento potente che ti permette di trasmettere facilmente vari contenuti multimediali, inclusa la musica, tra dispositivi compatibili DLNA sulla tua rete. La buona notizia è che Windows 10, e le versioni precedenti, includono una funzione DLNA integrata, eliminando la necessità di server multimediali di terze parti. Ecco come abilitare il server multimediale DLNA su Windows 10 e goderti lo streaming musicale sul tuo iPhone.

## Come abilitare il server multimediale DLNA su Windows 10

1. Clicca sul pulsante 'Start'.  
2. Seleziona l'icona 'Impostazioni'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Configurazione server" caption="Apri Impostazioni Windows" width="500" >}}

3. Nella schermata 'Impostazioni Windows', scegli 'Rete e Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Impostazioni Windows" caption="Seleziona Rete e Internet" width="500" >}}

4. Sotto 'Rete', seleziona 'Centro connessioni di rete e condivisione'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centro condivisione" caption="Apri Centro connessioni di rete e condivisione" width="500" >}}

5. Nella schermata 'Centro connessioni di rete e condivisione', clicca su 'Modifica impostazioni di condivisione avanzate' nel menu a sinistra.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Impostazioni di condivisione avanzate" caption="Modifica impostazioni di condivisione avanzate" width="500" >}}

6. Nella schermata 'Impostazioni di condivisione avanzate', scorri fino alla sezione 'Tutte le reti' ed espandila cliccando sulla freccia.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Attiva individuazione" caption="Espandi impostazioni di tutte le reti" width="500" >}}

7. Clicca su 'Attiva flusso multimediale' per attivare il server DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Attiva server" caption="Abilita il server di streaming multimediale" width="500" >}}

8. Dai un nome alla tua libreria multimediale e seleziona i dispositivi autorizzati ad accedervi.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nome libreria multimediale" caption="Assegna un nome alla tua libreria multimediale DLNA" width="500" >}}

9. Clicca 'OK' per confermare. Ora le tue cartelle personali come Musica, Immagini e Video saranno visibili a qualsiasi dispositivo di streaming con supporto UPnP.

## Come disabilitare il server multimediale DLNA su Windows 10

1. Clicca 'Start' e digita 'services' nel campo di ricerca.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Servizi Windows" caption="Apri Servizi Windows" width="500" >}}

2. Nella schermata 'Servizi', scorri per trovare 'Windows Media Player Network Sharing Service'.  
3. Fai doppio clic e imposta il 'Tipo di avvio' su 'Manuale'.  
4. Arresta il servizio cliccando sul pulsante 'Arresta'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Arresta servizio DLNA" caption="Disabilita il servizio di condivisione rete DLNA" width="500" >}}

## Come riprodurre musica dal server DLNA su iPhone

1. Installa l'app gratuita **Evermusic** dall'App Store:  
   [App Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Apri la scheda 'Connessioni' e tocca 'Dispositivi disponibili' nella sezione 'Rete locale'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Connessioni Evermusic" caption="Evermusic: schermata Connessioni" width="500" >}}

3. Attendi qualche secondo mentre la lista dei dispositivi si carica e tocca il server Windows Media Player DLNA (es. 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dispositivi disponibili" caption="Server DLNA disponibili in Evermusic" width="500" >}}

4. Vedrai un elenco di cartelle disponibili sul server multimediale.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Cartelle Evermusic" caption="Sfoglia le cartelle condivise dal server DLNA" width="500" >}}

5. Apri qualsiasi cartella contenente file audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Contenuto cartella" caption="Visualizza contenuti delle cartelle DLNA condivise" width="500" >}}

6. Tocca qualsiasi file per avviare il lettore audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Lettore audio" caption="Riproduci file audio da DLNA in Evermusic" width="500" >}}

7. Per migliorare la tua esperienza audio, tocca l'icona 'Equalizzatore' vicino all'indicatore del volume in basso sullo schermo per attivare l'equalizzatore stile iPod con preamplificatore.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Equalizzatore" caption="Usa l'equalizzatore integrato per una riproduzione migliorata" width="500" >}}

## Conclusione

Con il server multimediale DLNA su Windows 10 ed Evermusic sul tuo iPhone, puoi goderti uno streaming musicale fluido dal computer al dispositivo mobile. Addio alle limitazioni di archiviazione e benvenuta la musica on demand!

## Domande frequenti

{{% details title="Devo installare software server su Windows 10?" closed="true" %}}
No. Windows 10 include un server multimediale DLNA integrato. Devi solo abilitare lo streaming multimediale nelle impostazioni del Centro connessioni di rete e condivisione. Non è necessario software di terze parti.
{{% /details %}}

{{% details title="Il mio iPhone deve essere sulla stessa rete Wi-Fi?" closed="true" %}}
Sì. Lo streaming DLNA funziona sulla tua rete locale. Sia il tuo PC Windows 10 che il tuo iPhone devono essere connessi alla stessa rete Wi-Fi affinché Evermusic possa scoprire il server DLNA.
{{% /details %}}

{{% details title="Quali formati audio posso trasmettere via DLNA?" closed="true" %}}
Il server Windows DLNA condivide i file dalla cartella Musica indipendentemente dal formato. Evermusic supporta MP3, FLAC, AAC, WAV, OGG, AIFF e molti altri formati, quindi puoi riprodurre praticamente qualsiasi file audio dal server.
{{% /details %}}

{{% details title="Posso usare Flacbox invece di Evermusic?" closed="true" %}}
Sì. Flacbox supporta anche la navigazione e la riproduzione DLNA/UPnP. Puoi usare entrambe le app per scoprire e riprodurre musica dal tuo server Windows DLNA.
{{% /details %}}

{{% details title="Lo streaming DLNA usa dati mobili?" closed="true" %}}
No. DLNA funziona interamente sulla tua rete Wi-Fi locale. Non usa alcun dato mobile. Tuttavia, entrambi i dispositivi devono rimanere connessi alla stessa rete durante la riproduzione.
{{% /details %}}
