---
title: "Evermusic 8.7: reproducció sense pauses real, efectes d'àudio, normalització de volum i equalitzador redissenyat"
date: 2026-07-05
description: "Evermusic 8.7 per a iPhone, iPad i Mac afegeix reproducció sense pauses real, cinc efectes d'àudio d'estudi (reverberació, retard, distorsió, compressor, crossfeed), normalització de volum EBU R128, un equalitzador de 10 bandes redissenyat amb importació/exportació de predefinits, un motor de transmissió AVAudioEngine reconstruït amb suport per a FLAC i Ogg Vorbis, i un CarPlay i En reproducció més ràpids i precisos."
keywords: ["Evermusic 8.7", "actualització Evermusic", "reproducció sense pauses real iPhone", "reproductor de música sense pauses iOS", "reproducció sense pauses CarPlay", "efectes d'àudio reproductor de música iPhone", "reverberació retard distorsió compressor crossfeed iOS", "crossfeed auriculars iOS", "normalització de volum iPhone", "normalització de sonoritat reproductor de música", "normalització EBU R128 iOS", "alternativa a replay gain iPhone", "equalitzador de 10 bandes iPhone", "equalitzador gràfic app iOS", "importació exportació de predefinits equalitzador", "reproductor FLAC iPhone", "reproductor Ogg Vorbis iOS", "reproductor de música sense pèrdua iPhone 2026", "reproductor de música AVAudioEngine", "reproductor de música CarPlay iPhone", "precisió En reproducció pantalla de bloqueig", "reproductor de música al núvol iOS 2026"]
tags: ["Evermusic", "Evermusic 8.7", "Reproducció sense pauses", "Efectes d'àudio", "Reverberació", "Retard", "Distorsió", "Compressor", "Crossfeed", "Normalització de volum", "EBU R128", "Equalitzador", "FLAC", "Ogg Vorbis", "CarPlay", "En reproducció", "Liquid Glass", "Novetats"]
cascade:
  type: docs
authors:
  - name: "Artem Meleshko"
    link: "https://www.linkedin.com/in/artem-meleshko/"
    image: "/images/about/artem-meleshko-founder-everappz.webp"
---

{{< author-byline >}}

**En resum:** [Evermusic 8.7](/products/evermusic) és una versió centrada en la qualitat de so per a iPhone, iPad i Mac. Porta **reproducció sense pauses real** (sense pauses, clics ni tics entre pistes), un conjunt complet d'**efectes d'àudio d'estudi** (reverberació, retard, distorsió, compressor i crossfeed) i **normalització de volum EBU R128** que manté la sonoritat constant de cançó a cançó sense etiquetes de ReplayGain. L'**equalitzador de 10 bandes** s'ha redissenyat amb nous controls lliscants, canvi de predefinits més ràpid, predefinits personalitzats que pots importar i exportar, i una millor disposició en horitzontal i a l'iPad. Per dins, un **motor de transmissió AVAudioEngine reconstruït** millora la fiabilitat i el suport de formats, incloent-hi **FLAC** i **Ogg Vorbis**. **CarPlay** i **En reproducció** són més ràpids i precisos a la pantalla de bloqueig, al cotxe i des dels comandaments dels auriculars.

---

## Hola a tothom!

Evermusic 8.7 ja es pot descarregar. Aquesta actualització tracta de com *sona* la teva música. Hem reconstruït el motor de reproducció per aconseguir una reproducció sense pauses real, hem afegit un conjunt d'efectes d'àudio de nivell d'estudi, hem introduït la normalització de sonoritat i hem redissenyat l'equalitzador des dels controls lliscants. Tot plegat embolcallat amb el nou disseny **Liquid Glass** d'Apple.

[Descarrega Evermusic 8.7 des de l'App Store](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o actualitza des de la teva versió actual. Evermusic és una descàrrega gratuïta amb millores opcionals dins de l'aplicació.

## Reproducció sense pauses real

La reproducció sense pauses vol dir que el silenci entre dues pistes desapareix. Sense pausa, sense clic, sense tic: la cançó actual flueix directament cap a la següent. És més important per a la música dissenyada per escoltar-se com un tot: **enregistraments en directe, sessions de DJ, obres clàssiques i àlbums conceptuals** on una pista s'esvaeix directament cap a una altra.

Això és el que ha canviat tècnicament. El motor d'àudio d'Evermusic manté dues pistes en joc alhora: la que estàs escoltant i la següent de la cua. Mentre l'actual sona, la següent ja s'està **recuperant, descodificant i emmagatzemant per endavant** en segon pla. Quan l'actual arriba al final, el motor fa el traspàs a la pista següent **dins del reproductor, no dins del flux d'àudio**. El bucle de renderitzat de sortida continua extraient mostres d'àudio d'una memòria intermèdia circular contínua sense aturar-se mai, així l'oient no sent mai cap canvi. El traspàs passa entre mostres, i per això no hi ha cap buit audible.

Això funciona igual tant si el fitxer és al dispositiu, al núvol o en un servidor multimèdia: l'emmagatzematge per endavant simplement comença una mica abans per a les fonts remotes.

## Efectes d'àudio d'estudi

Evermusic 8.7 afegeix cinc efectes d'àudio en temps real que pots apilar sobre la teva música. Cadascun s'executa com a node de processament d'àudio natiu al motor de reproducció, així s'aplica a tot el que reprodueixes (fitxers locals, transmissions al núvol i ràdio per internet per igual) sense recodificar.

Cada efecte porta una **biblioteca curada de predefinits** perquè aconsegueixis un so excel·lent amb un sol toc, i Evermusic **recorda la teva configuració exacta** entre sessions. Ajusta qualsevol control i l'efecte passa a un estat **Manual**, així sempre saps quan t'has allunyat d'un predefinit.

### Reverberació

Afegeix sensació d'espai, des d'una sala petita fins a una catedral. Basada en l'`AVAudioUnitReverb` d'Apple, ofereix **13 predefinits de sala** (Sala petita, Sala de concert mitjana, Placa, Catedral i més) més un control de **mescla humit/sec** del 0 al 100% perquè decideixis quant espai afegir.

### Retard (eco)

Un eco clàssic amb **10 predefinits**: Slapback, Eco de cinta, Dub, Ambiental i altres. Pots ajustar el **temps de retard** (fins a 2 segons), la **retroalimentació** (quantes repeticions), un **tall de passa baixos** per escalfar les repeticions i la **mescla humit/sec**.

### Distorsió

Des d'una aspresa subtil fins a una destrucció lo-fi completa, impulsada per l'`AVAudioUnitDistortion` amb **22 predefinits de caràcter** (Bit Brush, Cellphone Concert, Radio Tower i més), un control de **preguany** i una mescla humit/sec perquè puguis barrejar l'efecte de nou amb el senyal net.

### Compressor

Un processador de dinàmica (l'`AUDynamicsProcessor` d'Apple) que iguala els passatges forts i fluixos. Exposa el conjunt de controls professional complet (**llindar, ràtio/marge, atac, alliberament, expansió i guany de compensació**) amb **10 predefinits** ajustats per a situacions reals: Veu / Podcast, Nit tancada, Diàleg de pel·lícula, Ajust de transmissió i Sonoritat màxima, entre altres.

### Crossfeed

El crossfeed fa que l'escolta amb auriculars soni més natural barrejant una mica del canal esquerre amb el dret i viceversa, tal com les orelles senten els altaveus reals. Està construït sobre el conegut algorisme **Bauer stereophonic-to-binaural (bs2b)**, amb control sobre el **nivell de crossfeed** i la **freqüència de tall**, i **6 predefinits**, incloses les configuracions favorites dels audiòfils *Chu Moy* i *Jan Meier*. És especialment bo en mescles estèreo antigues dels anys 60 i 70 amb panoramitzat extrem.

## Normalització de volum

Alguna vegada has fet una llista on una pista rebenta i la següent és un xiuxiueig? La normalització de volum ho arregla. Evermusic 8.7 fa servir la **mesura de sonoritat EBU R128** (el mateix estàndard ITU-R BS.1770 que s'utilitza a la radiodifusió i als serveis de transmissió) per mesurar la sonoritat percebuda real de cada pista i dirigir-la suaument cap a un objectiu constant.

A diferència de ReplayGain, **no** requereix cap etiqueta als teus fitxers i **no** modifica el teu àudio. Funciona en temps real amb qualsevol cosa que reprodueixis, incloses les transmissions al núvol i la ràdio en directe, i es reinicia netament quan avances o canvies de pista.

Quatre predefinits cobreixen els casos habituals:

- **Suau**: anivellament suau (objectiu −20 LUFS).
- **Estàndard**: el predeterminat, sonoritat estil transmissió (objectiu −16 LUFS, fins a +12 dB d'elevació per a pistes fluixes).
- **Fort**: ajust agressiu per a biblioteques molt barrejades (objectiu −14 LUFS).
- **Nit**: més tranquil i constant per a escoltes de volum baix al vespre (objectiu −23 LUFS).

Ja no cal que toquis el volum entre cançons.

## Equalitzador redissenyat

L'**equalitzador gràfic de 10 bandes** d'Evermusic ha rebut un redisseny complet. Les bandes cobreixen de **32 Hz a 16 kHz** (32, 64, 125, 250, 500 Hz, 1, 2, 4, 8, 16 kHz), cadascuna ajustable de **−12 dB a +12 dB** en passos fins de 0,1 dB, amb un **preamplificador** de −24 dB a +24 dB per evitar la saturació quan reforces.

Novetats de la 8.7:

- **Nous controls lliscants**: controls precisos i sensibles que adopten l'aspecte del control lliscant natiu del sistema d'iOS 26 i el material **Liquid Glass**.
- **Canvi de predefinits més ràpid i fluid**: salta entre predefinits a l'instant, amb una barra de predefinits horitzontal redissenyada en vertical i una columna de predefinits vertical en horitzontal.
- **Millor disposició en horitzontal i a l'iPad**: els controls lliscants i el selector de predefinits es reorganitzen per aprofitar l'amplada extra en lloc d'amuntegar-se en una columna de mida de telèfon.
- **Predefinits personalitzats**: crea i desa les teves pròpies corbes, reordena-les i **importa i exporta** predefinits com a fitxers `.eqp` per moure'ls entre dispositius o compartir-los.

L'equalitzador s'executa de manera nativa al motor (`AVAudioUnitEQ`), així s'aplica a totes les fonts, i també funciona per AirPlay, Chromecast i CarPlay allà on estigui admès.

## Motor de reproducció reconstruït

Per dins, Evermusic 8.7 funciona amb un **motor de transmissió reconstruït** basat en l'`AVAudioEngine` d'Apple amb una canalització de renderitzat personalitzada. Això és el que fa possibles el traspàs sense pauses, la cadena d'efectes i l'equalitzador, i també fa que la reproducció diària sigui més fiable.

- **Millor suport de formats**: incloent-hi **FLAC** (via Core Audio) i **Ogg Vorbis** (via `libvorbisfile`), a més de MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i més.
- **Emmagatzematge més intel·ligent**: un emmagatzematge per endavant adaptatiu que s'escala amb la teva connexió, amb una memòria intermèdia circular contínua que alimenta la sortida perquè els talls breus de xarxa no es converteixin en interrupcions.
- **Recuperació automàtica**: una màquina d'estats de reemmagatzematge i una lògica de reintent amb marge reprenen la reproducció netament després d'un moment de senyal feble en lloc d'aturar la pista.
- **Menys interrupcions**: el mateix motor gestiona fitxers locals, transmissions al núvol, servidors multimèdia i ràdio per internet, així el comportament és coherent a tot arreu.

## En reproducció i CarPlay

Les pantalles que realment mires mentre escoltes (la **pantalla de bloqueig**, **CarPlay** i els botons dels comandaments del cotxe o dels auriculars) són més precises i ràpides a la 8.7.

- **Informació d'En reproducció més precisa.** Evermusic captura l'estat del reproductor sota un bloqueig abans de publicar-lo, així el títol, el temps transcorregut, la durada i l'estat de reproducció/pausa mai no poden contradir-se a la pantalla de bloqueig o al cotxe. Els estats d'emmagatzematge i càrrega ara es reporten correctament en lloc de mostrar "en reproducció" mentre una pista encara s'està recuperant.
- **Comandaments a distància fiables.** Reproduir, pausar, següent, anterior, avançar, saltar, aleatori, repetir i velocitat de reproducció responen de manera coherent des dels botons dels auriculars, els controls del cotxe i la pantalla de bloqueig, gestionats per `MPRemoteCommandCenter`.
- **Caràtules més ràpides a CarPlay.** Les caràtules d'àlbum ara es carreguen diverses vegades més ràpid a les llistes llargues (el ritme de lots s'ha reduït d'1,0 s a 0,25 s, amb la primera pantalla visible carregant-se a l'instant), i ara apareixen a les files compactes de la llista de CarPlay d'iOS 26 que abans no mostraven cap caràtula.
- **Correccions d'ordenació i estabilitat a CarPlay.** Ordenació més ràpida en biblioteques grans i protecció contra fallades en casos límit en desplaçar-se per llistes llargues.
- **Actualitzacions de metadades limitades.** Les actualitzacions d'En reproducció i dels comandaments a distància es limiten perquè els canvis ràpids ja no inundin el sistema, cosa que manté els controls de la pantalla de bloqueig i de CarPlay sensibles.

## Altres millores

- **Refinaments del disseny Liquid Glass** a tota l'aplicació: superfícies translúcides, animacions més fluides i controls refinats a iOS, iPadOS i macOS.
- **Nous ginys de la pantalla d'inici** amb una lògica d'actualització millorada que els manté sincronitzats sense gastar bateria extra.
- Correccions per a les versions recents d'iOS.
- Correccions de localització en diversos idiomes.
- Moltes millores més petites basades en els vostres correus i ressenyes de l'App Store.

## Per què importa aquesta actualització

Evermusic 8.7 està construït al voltant d'una sola idea: **la teva música ha de sonar el millor possible, en qualsevol font.**

1. **Àlbums sencers, tal com es van pensar.** La reproducció sense pauses real fa que els sets en directe, les sessions de DJ i els àlbums conceptuals finalment sonin tal com l'artista els va masteritzar.
2. **Un estudi a la butxaca.** Reverberació, retard, distorsió, compressor, crossfeed, un equalitzador redissenyat i normalització de sonoritat et donen un control real del teu so, no només un interruptor d'activar/desactivar.
3. **La mateixa experiència a tot arreu.** Fitxers locals, discs al núvol, servidors multimèdia i ràdio per internet passen tots pel mateix motor reconstruït, amb un En reproducció precís i un CarPlay més ràpid al damunt.

## Aconsegueix Evermusic 8.7

[**Descarrega Evermusic des de l'App Store**](https://apps.apple.com/app/evermusic-offline-music-player/id885367198) o actualitza des de dins de l'App Store. Evermusic és una descàrrega gratuïta amb millores opcionals dins de l'aplicació per a funcions avançades.

Si gaudeixes de l'aplicació, deixa una valoració a l'App Store: ajuda de veritat. Tens comentaris o has trobat un problema? Escriu-nos a **support@everappz.com**. Llegim cada missatge.

## Preguntes freqüents

{{% details title="Què hi ha de nou a Evermusic 8.7?" closed="true" %}}
Evermusic 8.7 afegeix reproducció sense pauses real, cinc efectes d'àudio d'estudi (reverberació, retard, distorsió, compressor i crossfeed), normalització de volum EBU R128, un equalitzador de 10 bandes redissenyat amb predefinits personalitzats i importació/exportació, un motor de transmissió AVAudioEngine reconstruït amb millor suport de formats (incloent-hi FLAC i Ogg Vorbis), un CarPlay i En reproducció més ràpids i precisos, actualitzacions del disseny Liquid Glass, ginys renovats de la pantalla d'inici, i correccions d'errors i de localització.
{{% /details %}}

{{% details title="Evermusic té reproducció sense pauses real?" closed="true" %}}
Sí. A partir d'Evermusic 8.7, la reproducció és realment sense pauses: no hi ha cap pausa, clic ni tic entre pistes. El motor emmagatzema i descodifica per endavant la pista següent mentre l'actual sona i fa el traspàs entre mostres d'àudio en una memòria intermèdia circular contínua, així la transició és inaudible. Funciona amb fitxers locals, transmissions al núvol i servidors multimèdia, i és ideal per a àlbums en directe, sessions de DJ i àlbums conceptuals.
{{% /details %}}

{{% details title="Quins efectes d'àudio inclou Evermusic 8.7?" closed="true" %}}
Cinc efectes en temps real: **reverberació** (13 predefinits de sala, mescla humit/sec), **retard/eco** (10 predefinits amb temps de retard, retroalimentació, passa baixos i mescla), **distorsió** (22 predefinits de caràcter amb preguany i mescla), **compressor** (un processador de dinàmica complet amb llindar, ràtio, atac, alliberament, expansió i guany de compensació, més 10 predefinits) i **crossfeed** (crossfeed per a auriculars Bauer bs2b amb controls de nivell i tall i 6 predefinits). Cada efecte porta predefinits curats, i la teva configuració personalitzada es recorda entre sessions.
{{% /details %}}

{{% details title="Què és el crossfeed i per què el faria servir?" closed="true" %}}
El crossfeed barreja una petita quantitat filtrada de cada canal estèreo amb l'altre, tal com les orelles senten de manera natural els altaveus reals en una sala. Amb auriculars, això redueix la separació exagerada i "dins del cap" dels enregistraments amb panoramitzat extrem i fa més còmodes les escoltes llargues. Evermusic fa servir el conegut algorisme Bauer stereophonic-to-binaural (bs2b) i inclou predefinits com Chu Moy i Jan Meier. És especialment efectiu en mescles estèreo antigues dels anys 60 i 70.
{{% /details %}}

{{% details title="Com funciona la normalització de volum a Evermusic?" closed="true" %}}
Evermusic 8.7 mesura la sonoritat percebuda de cada pista amb l'estàndard EBU R128 (ITU-R BS.1770) en temps real i ajusta suaument el nivell cap a un objectiu constant perquè les pistes no saltin de volum. No requereix etiquetes de ReplayGain i no altera els teus fitxers. Hi ha quatre predefinits disponibles (Suau −20 LUFS, Estàndard −16 LUFS, Fort −14 LUFS i Nit −23 LUFS) i la normalització es reinicia netament quan avances o canvies de pista.
{{% /details %}}

{{% details title="La normalització de volum d'Evermusic és el mateix que ReplayGain?" closed="true" %}}
Aconsegueix el mateix objectiu (sonoritat constant entre pistes) però funciona de manera diferent. ReplayGain depèn d'etiquetes de sonoritat desades dins dels teus fitxers. El normalitzador d'Evermusic mesura la sonoritat en directe amb EBU R128, així funciona amb qualsevol font, incloses les transmissions al núvol i la ràdio per internet, fins i tot quan els fitxers no tenen cap etiqueta.
{{% /details %}}

{{% details title="Quantes bandes té l'equalitzador d'Evermusic i puc fer els meus propis predefinits?" closed="true" %}}
L'equalitzador d'Evermusic és un equalitzador gràfic de 10 bandes que cobreix de 32 Hz a 16 kHz, amb cada banda ajustable de −12 dB a +12 dB en passos de 0,1 dB i un preamplificador de −24 dB a +24 dB. Inclou predefinits integrats, et permet crear i desar predefinits personalitzats, i admet importar i exportar predefinits com a fitxers .eqp perquè els puguis moure o compartir entre dispositius.
{{% /details %}}

{{% details title="Què ha canviat a l'equalitzador d'Evermusic 8.7?" closed="true" %}}
L'equalitzador s'ha redissenyat amb nous controls lliscants més precisos que adopten l'aspecte del control lliscant del sistema d'iOS 26 i de Liquid Glass, un canvi de predefinits més ràpid i fluid, i una millor disposició en horitzontal i a l'iPad (una barra de predefinits horitzontal en vertical i una columna de predefinits vertical en horitzontal). S'admeten predefinits personalitzats i importació/exportació de .eqp.
{{% /details %}}

{{% details title="Evermusic 8.7 admet FLAC i Ogg Vorbis?" closed="true" %}}
Sí. El motor reconstruït reprodueix FLAC (via Core Audio) i Ogg Vorbis (via libvorbisfile), juntament amb MP3, AAC, Apple Lossless (ALAC), WAV, AIFF, AC-3, CAF i més, des de fitxers locals, discs al núvol i servidors multimèdia.
{{% /details %}}

{{% details title="Què ha millorat a CarPlay i a la pantalla de bloqueig?" closed="true" %}}
Les caràtules d'àlbum de CarPlay es carreguen diverses vegades més ràpid a les llistes llargues i ara apareixen a les files compactes de la llista d'iOS 26 que abans no en mostraven cap. La informació d'En reproducció a la pantalla de bloqueig i a CarPlay és més precisa: el títol, el temps transcorregut, la durada i l'estat de reproducció/pausa es capturen junts perquè no puguin contradir-se, i els estats d'emmagatzematge es reporten correctament. Els comandaments a distància (reproduir, pausar, següent, anterior, avançar, aleatori, repetir, velocitat) responen de manera fiable des dels auriculars i el cotxe, i l'ordenació de CarPlay en biblioteques grans és més ràpida.
{{% /details %}}

{{% details title="Els efectes d'àudio i l'equalitzador funcionen amb la transmissió al núvol i CarPlay?" closed="true" %}}
Sí. Els efectes, l'equalitzador i la normalització de volum s'executen de manera nativa dins del motor de reproducció, així s'apliquen a tot el que reprodueix Evermusic (fitxers locals, discs al núvol, servidors multimèdia i ràdio per internet) i continuen funcionant durant la reproducció amb CarPlay i, allà on estigui admès, per AirPlay i Chromecast.
{{% /details %}}

{{% details title="Evermusic 8.7 és una actualització gratuïta i quins dispositius admet?" closed="true" %}}
Sí. Evermusic és una descàrrega gratuïta de l'App Store, i la 8.7 és una actualització gratuïta per als usuaris existents, amb millores opcionals dins de l'aplicació per a funcions avançades. Funciona a iPhone, iPad i Mac. CarPlay requereix un vehicle o una unitat principal compatible amb CarPlay.
{{% /details %}}
