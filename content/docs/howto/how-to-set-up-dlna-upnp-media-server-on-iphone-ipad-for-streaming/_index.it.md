---
title: "Come configurare un media server DLNA/UPnP su iPhone e iPad per lo streaming"
description: "Trasforma iPhone o iPad in un media server DLNA/UPnP con Everdisk e trasmetti foto, video e musica su smart TV, console di gioco, VLC o Kodi via Wi-Fi. Configurazione completa e come collegarti da TV Samsung, LG e Sony, Windows, Mac, Linux, Android e un altro iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "media server", "streaming", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["server DLNA iPhone", "server UPnP iPad", "come configurare DLNA su iPhone", "streaming su smart TV da iPhone", "media server DLNA iOS", "trasmettere video alla TV senza cavo", "riprodurre foto iPhone sulla TV", "DLNA iPhone TV Samsung", "DLNA iPhone TV LG", "DLNA iPhone Sony Bravia", "VLC DLNA iPhone", "media server DLNA Kodi", "media server UPnP AV iOS", "streaming musica alla TV da iPhone", "app media server iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (chiamato anche UPnP AV) è il motore silenzioso dietro la maggior parte delle smart TV. È un linguaggio condiviso che permette a una TV o a un lettore multimediale di trovare una libreria multimediale sulla stessa rete Wi-Fi e riprodurne i contenuti, senza dover installare nulla sulla TV. Se il tuo iPhone o iPad può fare da libreria, le tue foto, i video e la musica compaiono da soli sul grande schermo.

Questa guida mostra come trasformare il tuo iPhone o iPad in un media server DLNA/UPnP usando [Everdisk](/products/everdisk), e come aprire quella libreria da una smart TV, una console di gioco, VLC, Kodi, un computer, un telefono Android e persino un secondo iPhone. Tutto gira sulla tua rete Wi-Fi locale, quindi niente viene caricato da nessuna parte.

## Cosa ti serve

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) installato.
- Una TV, un lettore o un computer sulla **stessa rete Wi-Fi** del tuo dispositivo.
- Le foto, i video o la musica che vuoi riprodurre, già presenti sul tuo iPhone (nell'app Foto, nell'app Musica o nella cartella Documenti di Everdisk).

## Configura il server DLNA in Everdisk

### Passo 1: scegli cosa condividere

Apri Everdisk e vai alla scheda **Condivisione**. Tocca **Cosa condividere** e scegli i tuoi contenuti:

- Attiva **Consenti l'accesso a tutta la libreria Foto** per condividere ogni album, oppure tocca **Aggiungi foto** per sceglierne alcune.
- Attiva **Consenti l'accesso a tutta la libreria Musica** per condividere i tuoi brani, oppure tocca **Aggiungi brani** per una selezione.
- Aggiungi cartelle o file con **Aggiungi cartella** e **Aggiungi file**. La cartella Documenti dell'app è condivisa per impostazione predefinita.

Devi selezionare almeno un elemento prima di poter avviare la condivisione.

### Passo 2: attiva TV e centro multimediale (DLNA)

Vai su **Impostazioni**, poi **Condivisione**, poi **Connessioni**. Assicurati che **TV e centro multimediale** sia attivo. È attivo per impostazione predefinita e porta il tag DLNA. È il server che TV e lettori cercano.

### Passo 3: avvia la condivisione

Torna alla scheda **Condivisione** e tocca il grande pulsante **Avvia**. Il tuo dispositivo è ora un media server sulla tua rete Wi-Fi. Compare agli altri dispositivi con il suo nome descrittivo, quello mostrato come nome del dispositivo nell'app (qualcosa come "Speedy-Hare" finché non lo cambi).

Lo streaming DLNA è sempre aperto, quindi non c'è nessuna password da inserire sulla TV. Tieni Everdisk aperto sullo schermo mentre guardi, perché iOS mette in pausa le app spinte completamente in background.

## Riprodurre su una smart TV

È il caso più comune, e di solito richiede circa trenta secondi.

1. Metti la TV sulla **stessa rete Wi-Fi** del tuo iPhone.
2. Apri il lettore multimediale integrato della TV. Il nome dipende dalla marca: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** o **SmartThings** (Samsung), **Content Share** o **SimplyShare**.
3. Cerca l'elenco dei media server o delle sorgenti. Il tuo dispositivo compare lì con il suo nome.
4. Selezionalo, sfoglia tra foto, video o musica e premi play.

Le miniature di anteprima compaiono automaticamente, così puoi trovare l'album delle vacanze o il film giusto senza tirare a indovinare.

### Quali TV funzionano

La maggior parte delle TV di **Samsung, LG, Sony BRAVIA, Panasonic (firmware VIERA), Philips e Hisense** ha il DLNA integrato e funziona subito. Anche **le console PlayStation e Xbox e la maggior parte dei ricevitori AV** lo supportano.

Alcune piattaforme lo tralasciano: **le TV Roku, Amazon Fire TV, Vizio SmartCast e la semplice Google TV** senza un'app multimediale del produttore. Se la tua TV è una di queste e non riesce a trovare il tuo dispositivo, di solito è questo il motivo. Su quelle TV, installa un'app lettore DLNA come VLC o Kodi, oppure raggiungi i tuoi file tramite un browser web usando la [guida alla configurazione di WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Alcune marche hanno mantenuto il DLNA funzionante anche dopo aver rimosso il logo DLNA ufficiale, quindi se sembra mancare, cerca uno dei nomi di lettore multimediale qui sopra.

## Riprodurre in VLC o Kodi su Windows, Mac e Linux

VLC e Kodi sono gratuiti, girano su ogni sistema desktop e parlano bene il DLNA. Sono il modo affidabile per aprire la tua libreria Everdisk su un computer.

**VLC (Windows, Mac, Linux):**

1. Apri VLC.
2. Mostra la playlist (su Windows e Linux premi **Ctrl+L**, su Mac apri la **Playlist** dal menu Vista).
3. Nella barra laterale, apri **Universal Plug'n'Play** sotto Rete locale.
4. Il tuo dispositivo compare nell'elenco. Aprilo e scegli un file.

**Kodi (Windows, Mac, Linux):**

1. Vai su **Video**, **Musica** o **Immagini**, poi **File**, poi **Aggiungi sorgente** (o **Sfoglia**).
2. Scegli **Dispositivi UPnP**.
3. Seleziona il tuo dispositivo e sfoglia la tua libreria.

Su Windows puoi anche aprire **Windows Media Player**, espandere **Altre librerie** nella barra laterale, e il tuo dispositivo comparirà lì.

## Riprodurre su Android

I telefoni e i tablet Android non hanno un browser DLNA di sistema, quindi usa un'app:

- **VLC per Android**: apri il menu laterale, tocca **Rete locale**, e il tuo dispositivo compare tra i server UPnP.
- **BubbleUPnP** o un'app UPnP simile: il tuo dispositivo compare nell'elenco dei server, e queste app possono anche inviare la riproduzione a una TV.

## Riprodurre su un altro iPhone o iPad

Due dispositivi, una libreria. Diciamo che le foto sono sul tuo iPhone e vuoi guardarle sull'iPad.

- La via più semplice è la scheda **Dispositivi** di Everdisk sul secondo dispositivo. Funziona sia come client DLNA che come server. Apri Everdisk sull'iPad, vai su **Dispositivi**, e il tuo iPhone compare tra i **Dispositivi disponibili**. Toccalo per sfogliare e riprodurre.
- Funziona anche qualsiasi app lettore DLNA per iOS, come VLC o un browser UPnP. Apri la sua vista della rete locale e scegli il tuo iPhone.

## Riprodurre su una console di gioco

- **PlayStation 5 e 4**: apri l'app **Media** (Galleria multimediale), e il tuo dispositivo compare come un media server che puoi sfogliare.
- **Xbox**: usa un'app lettore multimediale che supporti il DLNA, poi scegli il tuo dispositivo dall'elenco dei server.

## Se il tuo dispositivo non compare nell'elenco

Alcuni lettori ti permettono di aggiungere un media server tramite indirizzo invece di aspettare che venga rilevato. Nella schermata **Condivisione** di Everdisk, la scheda DLNA mostra un indirizzo di descrizione del dispositivo che termina in `/device-desc.xml`. Inserisci quell'indirizzo nel campo di aggiunta server del lettore.

Se ancora non compare, controlla tre cose: che entrambi i dispositivi siano sulla stessa rete Wi-Fi (non una rete ospiti che blocca il traffico tra dispositivi), che Everdisk sia aperto e la condivisione avviata, e che **TV e centro multimediale** sia attivo nelle Impostazioni.

## Se un video non viene riprodotto

Il DLNA passa il file alla TV così com'è, e la TV deve essere in grado di decodificarlo. Se un filmato si rifiuta di partire, probabilmente il suo formato non è supportato da quella TV. Due soluzioni:

- Apri **Impostazioni**, poi **Condivisione**, poi **Video**, e abbassa la **Qualità**. Everdisk converte quindi il video in un formato più compatibile mentre lo trasmette. (La conversione è una funzione Premium.)
- Oppure apri lo stesso file in un browser web usando il link del browser di Everdisk, che è più tollerante riguardo ai formati.

## Modi reali in cui le persone lo usano

- **Serata film in famiglia.** I video girati con il telefono si riproducono sulla TV del soggiorno senza un cavo o una Apple TV.
- **Le foto delle vacanze sul grande schermo.** Apri la tua libreria Foto sulla TV e scorri il viaggio con tutti nella stanza.
- **Musica di sottofondo a una festa.** Punta un altoparlante DLNA o un ricevitore AV alla tua libreria Musica e lascialo suonare.
- **Guardare su una TV d'hotel** che ha un lettore multimediale, una volta che entrambi i dispositivi sono sul Wi-Fi della stanza.

## Qualche consiglio

- Tieni Everdisk aperto mentre trasmetti. Se blocchi il telefono a lungo, iOS potrebbe mettere in pausa l'app e la riproduzione si ferma.
- Collega il telefono all'alimentazione per le lunghe sessioni di film.
- Per lo streaming più veloce, mantieni **Formato** e **Qualità** su **Originale** nelle Impostazioni, e abbassali solo se una TV specifica fatica con un file.
- Il DLNA è solo streaming. Nessuno dal lato TV può modificare o eliminare i tuoi file. Per il trasferimento file bidirezionale, usa invece il server [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) o [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/).

## Domande frequenti

{{% details title="Qual è la differenza tra DLNA e UPnP?" closed="true" %}}
Sono strettamente correlati. UPnP è lo standard di rete sottostante, e DLNA è il profilo multimediale costruito sopra di esso che TV e lettori usano per condividere e riprodurre foto, video e musica. Nell'uso quotidiano i termini sono intercambiabili. Quando attivi TV e centro multimediale in Everdisk, il tuo dispositivo diventa un media server DLNA/UPnP che qualsiasi client DLNA può sfogliare.
{{% /details %}}

{{% details title="Devo installare qualcosa sulla mia TV?" closed="true" %}}
No. Se la tua TV supporta il DLNA, ha già un lettore multimediale in grado di trovare il tuo dispositivo sul Wi-Fi. Devi installare Everdisk solo sull'iPhone o iPad che contiene i contenuti. Se la tua TV non supporta il DLNA, installa un lettore come VLC o Kodi su un dispositivo collegato ad essa.
{{% /details %}}

{{% details title="Perché il mio iPhone non compare sulla TV?" closed="true" %}}
Controlla che entrambi i dispositivi siano sulla stessa rete Wi-Fi. Le reti ospiti e alcune reti aziendali o d'hotel impediscono ai dispositivi di vedersi tra loro, il che blocca il DLNA. Poi verifica che Everdisk sia aperto con la condivisione avviata, e che TV e centro multimediale sia attivo in Impostazioni, Condivisione, Connessioni. Se la TV ancora non riesce a trovarlo, aggiungi il server manualmente usando l'indirizzo di descrizione del dispositivo che termina in /device-desc.xml.
{{% /details %}}

{{% details title="Lo streaming DLNA richiede una password?" closed="true" %}}
No. Il DLNA è sempre aperto a chiunque sia sulla stessa rete Wi-Fi mentre è attivo, ed è per questo che non c'è alcun login dal lato TV. Va bene su una rete domestica di cui ti fidi. Su una rete di cui non ti fidi, disattiva TV e centro multimediale quando hai finito, oppure usa invece il server SMB con la cifratura.
{{% /details %}}

{{% details title="Posso trasmettere a un Chromecast o Roku?" closed="true" %}}
Chromecast e Roku non fanno da lettori DLNA per impostazione predefinita, quindi non troveranno direttamente il tuo dispositivo. La soluzione è installare un'app DLNA in grado di trasmettere, come VLC o BubbleUPnP su un telefono, e inviare la riproduzione al Chromecast o al Roku da lì. Sulla maggior parte delle altre smart TV, il DLNA funziona senza tutto questo.
{{% /details %}}

{{% details title="Un video parte senza audio o non si apre. Cosa posso fare?" closed="true" %}}
È un formato che la TV non riesce a decodificare. Apri Impostazioni, Condivisione, Video in Everdisk e abbassa la Qualità così l'app converte il video in un formato più compatibile mentre lo trasmette. Puoi anche aprire lo stesso file tramite il link del browser, che gestisce più formati.
{{% /details %}}

{{% details title="Posso trasmettere musica, non solo video?" closed="true" %}}
Sì. Attiva Consenti l'accesso a tutta la libreria Musica, oppure aggiungi brani specifici, poi avvia la condivisione. I tuoi brani compaiono su qualsiasi altoparlante DLNA, ricevitore AV o TV, con copertina e dettagli della traccia. La musica è sempre condivisa nella sua qualità originale.
{{% /details %}}

{{% details title="L'app deve restare aperta mentre guardo?" closed="true" %}}
Sì. Il tuo iPhone fa da server, e iOS mette in pausa le app spinte completamente in background per molto tempo. Tieni Everdisk sullo schermo mentre trasmetti, e collegalo all'alimentazione per le sessioni lunghe.
{{% /details %}}

{{% details title="Come faccio streaming da un iPhone a un altro iPad?" closed="true" %}}
Avvia la condivisione sull'iPhone, poi apri Everdisk sull'iPad e vai alla scheda Dispositivi. L'iPhone compare tra i Dispositivi disponibili come media server. Toccalo per sfogliare e riprodurre. Everdisk funziona sia come client DLNA che come server, quindi non ti serve un'altra app.
{{% /details %}}

{{% details title="Everdisk è gratis?" closed="true" %}}
Sì, Everdisk si scarica gratis e il media server DLNA è incluso. Un acquisto Premium Lifetime opzionale una tantum aggiunge extra come la conversione di foto e video per le TV più vecchie, porte personalizzate e altro. Puoi configurare e usare lo streaming DLNA senza pagare.
{{% /details %}}

Pronto a provarlo? [Scarica Everdisk dall'App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) e trasmetti il tuo primo album alla TV in un paio di minuti. Domande o feedback? Scrivici a **support@everappz.com**.
