---
title: "Com utilitzar els efectes de so d'Evermusic: reverberació, retard, distorsió, compressor, crossfeed i normalització de volum"
date: 2026-07-05
description: "Una guia completa dels efectes d'àudio en temps real d'Evermusic a l'iPhone, l'iPad i el Mac. Aprèn què fan la reverberació, el retard, la distorsió, el compressor, el crossfeed i la normalització de volum, com estan construïts i com activar, preajustar i afinar cadascun."
keywords: ["efectes d'àudio Evermusic", "efectes de so reproductor de música iPhone", "reverberació reproductor de música iOS", "efecte de retard i eco iPhone", "efecte d'àudio distorsió iOS", "compressor reproductor de música iPhone", "crossfeed auriculars iOS", "normalització de volum iPhone", "normalització de sonoritat reproductor de música", "EBU R128 iOS", "com afegir reverberació a la música iPhone", "efectes d'àudio reproductor de música iOS 2026", "efectes DSP reproductor de música iPhone"]
tags: ["Evermusic", "Efectes d'àudio", "Com fer-ho", "Reverberació", "Retard", "Distorsió", "Compressor", "Crossfeed", "Normalització de volum", "EBU R128", "Equalitzador", "Auriculars"]
readingTime: 8
---

{{< author-byline >}}

**En resum:** Evermusic inclou sis efectes d'àudio en temps real: **normalització de volum, compressor, reverberació, crossfeed, retard i distorsió**. Obre'ls des del menú **⋯ (Més) > Efectes d'àudio** del reproductor, o des de **Configuració > Reproductor d'àudio > Efectes d'àudio**. Toca un efecte, posa'n l'interruptor en **ACTIVAT** (a dalt a la dreta), tria un **predefinit** i, opcionalment, obre el **mode avançat** per afinar els controls lliscants. Cada efecte funciona de manera independent i s'aplica en temps real a tot el que reprodueixes: fitxers locals, transmissions al núvol i ràdio per internet, sense recodificar.

## Què són els efectes d'àudio d'Evermusic?

Els efectes d'àudio canvien el caràcter del teu so mentre sona. Evermusic els executa com a **nodes de processament natius i en temps real** dins del seu motor de reproducció, de manera que s'apliquen a totes les fonts (fitxers locals, discs al núvol, servidors multimèdia i ràdio per internet) sense modificar ni recodificar mai els teus fitxers. Desactiva un efecte i el so original torna a l'instant.

Hi ha sis efectes, i cadascun és **independent**: no hi ha cap interruptor mestre únic, així que en pots executar un, uns quants o tots alhora:

1. **Normalització de volum**: manté cada pista a una sonoritat constant.
2. **Compressor**: iguala les parts fortes i fluixes dins d'una pista.
3. **Reverberació**: afegeix sensació d'espai, des d'una sala petita fins a una catedral.
4. **Crossfeed**: fa que els auriculars sonin més com altaveus reals.
5. **Retard**: afegeix un eco, des d'un rebot ràpid fins a una cua ambiental llarga.
6. **Distorsió**: afegeix aspresa i caràcter lo-fi, per divertir-se.

La normalització de volum i el compressor tenen a veure amb la **coherència i la claredat**. La reverberació, el retard i la distorsió són **efectes creatius**. El crossfeed és una eina de **comoditat per als auriculars**. Junts converteixen Evermusic en un petit estudi a la butxaca.

## Com obrir els efectes d'àudio

Hi ha dues maneres d'arribar a la pantalla d'efectes d'àudio.

**Des del reproductor (la més ràpida):**

1. Obre la pantalla **En reproducció / reproductor**.
2. Toca el botó **⋯ (Més)**.
3. Toca **Efectes d'àudio**.

**Des de la configuració:**

1. Ves a la pestanya **Configuració**.
2. Toca **Reproductor d'àudio**.
3. Toca **Efectes d'àudio**.

Sigui com sigui, arribes a la llista d'**Efectes d'àudio**, que mostra els sis efectes en aquest ordre: **normalització de volum, compressor, reverberació, crossfeed, retard, distorsió**. Toca'n qualsevol per obrir-ne l'editor.

## Com funciona l'editor de cada efecte

Cada editor d'efectes segueix el mateix patró senzill, de manera que quan n'aprens un els coneixes tots:

- **Interruptor d'activació (a dalt a la dreta).** Posa l'efecte en **ACTIVAT** o **DESACTIVAT**. Cada efecte està desactivat per defecte. Quan està desactivat, els controls apareixen atenuats.
- **Commutador Simple / Avançat (a dalt a la dreta).** El mode *Simple* només mostra una llista de predefinits amb descripcions en llenguatge planer: la manera més fàcil d'aconseguir un bon so amb un sol toc. El mode *Avançat* afegeix controls lliscants d'afinació.
- **Selector de predefinits.** Una fila de "bombolles" de predefinits en vertical, o una columna de predefinits en horitzontal. Tria un punt de partida i després ajusta si vols.
- **Controls lliscants (mode avançat).** Cada control mostra el seu valor actual i té un petit botó de **restabliment** (una fletxa circular) per tornar-lo al valor per defecte. Ajustar qualsevol control passa l'efecte a un estat **Manual**, així sempre saps quan t'has allunyat d'un predefinit.

Els canvis es desen automàticament. A continuació, què fa cada efecte i com configurar-lo.

## Normalització de volum

**Què fa:** Algunes cançons estan masteritzades més fortes que altres, així que sempre acabes tocant el volum. La normalització de volum mesura la sonoritat percebuda real de cada pista i la anivella suaument cap a un objectiu constant, de manera que tot sona aproximadament al mateix volum. Utilitza l'estàndard de sonoritat de nivell professional **EBU R128** (ITU-R BS.1770), funciona en temps real amb qualsevol font i, a diferència de ReplayGain, no necessita **cap etiqueta de sonoritat als teus fitxers** i mai no altera l'àudio.

**Predefinits:** Suau, Estàndard, Fort i Nit.

**Controls avançats:**

- **Sonoritat objectiu**: la sonoritat cap a la qual s'anivella cada pista, mostrada en LUFS. Més alta (per exemple, −14 LUFS) fa que tot soni més fort en general; més baixa (−23 LUFS) és més tranquil·la i calmada.
- **Guany màxim**: limita quant es pot amplificar una pista fluixa, en dB. Els valors més alts acosten els enregistraments suaus a l'objectiu.

**Com utilitzar-la:** Activa-la i tria **Estàndard** per a una sonoritat estil transmissió, o **Nit** per escoltar de manera constant i tranquil·la al vespre. Perfecta per a llistes aleatòries que barregen enregistraments antics i nous.

## Compressor

**Què fa:** Dins d'una sola cançó, les parts fluixes poden ser massa suaus i les fortes massa altes. El compressor les acosta perquè tota la pista sigui fàcil de sentir: al cotxe, corrent o en qualsevol lloc sorollós. És un processador de dinàmica complet basat en l'`AUDynamicsProcessor` d'Apple.

**Predefinits:** Transparent, Suau, Estàndard, Fort, Veu / Podcast, Enregistraments antics, Nit tancada, Diàleg de pel·lícula, Ajust de transmissió i Sonoritat màxima.

**Controls avançats (set controls lliscants):**

- **Llindar**: el nivell on comença la compressió. Més baix, més comprimeix.
- **Marge (headroom)**: espai per sobre del llindar abans que s'activi la limitació dura.
- **Ràtio d'expansió**: com de fort s'abaixen els sons molt fluixos (com el soroll de fons).
- **Llindar d'expansió**: el nivell per sota del qual comença aquesta obertura de porta.
- **Atac**: com de ràpid reacciona l'efecte a un pic fort sobtat.
- **Alliberament**: com de ràpid deixa anar després que passi la part forta.
- **Guany mestre**: increment de compensació final aplicat després del processament.

**Com utilitzar-lo:** Per a la majoria d'escoltes, activa'l i tria **Estàndard**. Tria **Veu / Podcast** o **Diàleg de pel·lícula** per a contingut parlat, **Nit tancada** per escoltar tranquil·lament, o **Sonoritat màxima** per al resultat més fort i uniforme.

## Reverberació

**Què fa:** Fa que la música soni com si es reproduís en un espai real, amb una cua natural d'eco, des d'una sala íntima fins a una gran sala o catedral. Basada en l'`AVAudioUnitReverb` d'Apple.

**Predefinits (13):** Sala petita, Sala mitjana, Sala gran, Sala de concert mitjana, Sala de concert gran, Placa, Cambra mitjana, Cambra gran, Catedral, i diverses variacions de sales i cambres.

**Control avançat:**

- **Mescla**: quanta reverberació s'hi barreja, des del 0% (sec, so original) fins al 100% (plenament dins de l'espai triat).

**Com utilitzar-la:** Activa-la, tria un espai (per exemple, **Sala de concert mitjana** per a una sensació càlida i espaiosa) i mantén la **Mescla** moderada: una mica ja fa molt. Fes-la servir per donar aire a enregistraments amb micròfon de prop o "secs".

## Crossfeed

**Què fa:** Amb auriculars, els canals esquerre i dret queden completament separats, cosa que pot fer que la música sembli encaixonada dins del cap, especialment en mescles estèreo antigues amb panoramitzat extrem. El crossfeed barreja una petita quantitat filtrada de cada canal amb l'altre, tal com les orelles senten de manera natural els altaveus en una sala, així el so sembla més natural i menys cansat en escoltes llargues. Està construït sobre el conegut algorisme **Bauer stereophonic-to-binaural (bs2b)**.

**Predefinits (6):** Subtil, Chu Moy, Fort, Jan Meier, Tipus altaveu i Estèreo vintage.

**Controls avançats:**

- **Freqüència de tall**: on comença a atenuar-se la barreja entre canals. Els valors més baixos donen un efecte més càlid i pronunciat.
- **Nivell d'aportació**: quant d'un canal es barreja amb l'altre. Els valors més alts sonen més com altaveus.

**Com utilitzar-lo:** És un efecte d'**auriculars**: deixa'l desactivat per als altaveus. Activa'l i prova **Chu Moy** o **Jan Meier** (tots dos favorits dels audiòfils), o **Estèreo vintage** per a enregistraments dels anys 60 i 70 amb panoramitzat extrem.

## Retard (eco)

**Què fa:** Repeteix el so com un eco a les muntanyes. Una mica fa que la música sembli més plena; més deixa un eco clar i rítmic després de cada nota. Basat en l'`AVAudioUnitDelay` d'Apple.

**Predefinits (10):** Slapback, Doblador, Eco curt, Estàndard, Eco de cinta, Eco brillant, Eco llarg, Dub, Espaiós i Ambiental.

**Controls avançats:**

- **Temps de retard**: la pausa entre el so original i el seu eco. Curt és un rebot ràpid; llarg és una repetició clara.
- **Retroalimentació**: quantes vegades es repeteix l'eco abans d'esvair-se.
- **To**: filtra la brillantor de l'eco per a un so més càlid, tipus cinta.
- **Mescla**: quant d'eco s'hi barreja.

**Com utilitzar-lo:** Activa'l i comença amb **Slapback** o **Eco de cinta** per a una profunditat subtil, o **Ambiental** i **Dub** per a cues llargues i espaioses.

## Distorsió

**Què fa:** Fa que la música soni aspra i granulada, com un altaveu trencat o una transmissió lo-fi. És un efecte creatiu i per divertir-se, més que una eina de fidelitat, així que fes-lo servir amb moderació. Basat en l'`AVAudioUnitDistortion` d'Apple.

**Predefinits (22):** inclosos Bit Brush, Broken Speaker, Cellphone Concert, Radio Tower, Alien Chatter, Cosmic Interference i molts més.

**Controls avançats:**

- **Preguany**: com de fort empeny el senyal la distorsió. Més alt és més agressiu.
- **Mescla**: quanta distorsió es barreja amb el so net.

**Com utilitzar-la:** Activa-la, tria un predefinit de caràcter i mantén la **Mescla** baixa si no vols un so molt trencat. Divertida en pistes electròniques i experimentals.

## Com estan construïts els efectes

Els efectes d'Evermusic s'executen dins d'una cadena de processament moderna d'**AVAudioEngine**. Cada efecte és un node d'àudio natiu col·locat a la ruta del senyal, i només està actiu quan l'actives; en cas contrari, s'ometeix amb cost zero. La reverberació, el retard i la distorsió utilitzen les unitats d'àudio integrades d'Apple (`AVAudioUnitReverb`, `AVAudioUnitDelay`, `AVAudioUnitDistortion`); el compressor utilitza l'`AUDynamicsProcessor` d'Apple; el crossfeed és un node personalitzat basat en l'algorisme de codi obert **bs2b**; i la normalització de volum és un node de sonoritat **EBU R128** en temps real.

Com que els efectes formen part del mateix motor de reproducció:

- S'apliquen en **temps real** a tot el que reprodueixes, incloses les transmissions al núvol i la ràdio en directe.
- **Mai no modifiquen ni recodifiquen** els teus fitxers: desactiva un efecte i el so original torna.
- **Recorden la teva configuració** entre sessions, per a cada efecte.
- Es poden combinar lliurement, ja que cadascun és independent.

També funcionen juntament amb l'**equalitzador gràfic de 10 bandes** d'Evermusic i la seva **reproducció sense pauses**, així pots modelar el to, anivellar la sonoritat i mantenir les transicions fluides tot alhora.

## Consells

- **Comença en mode Simple.** Tria primer un predefinit; només obre el mode avançat quan vulguis afinar.
- **Menys és més** per a la reverberació, el retard i la distorsió: mantén la Mescla moderada per a resultats musicals.
- **El crossfeed és per a auriculars**, no per a altaveus.
- **La normalització de volum + el compressor** junts donen el resultat més constant i fàcil de sentir per a llistes barrejades i escoltes al cotxe.
- Cada control lliscant té un botó de **restabliment** si vols tornar al valor per defecte.

## Preguntes freqüents

{{% details title="Com afegeixo reverberació, retard o altres efectes a la meva música a Evermusic?" closed="true" %}}
Obre el reproductor, toca el botó ⋯ (Més) i tria Efectes d'àudio (o ves a Configuració > Reproductor d'àudio > Efectes d'àudio). Toca l'efecte que vulguis, posa'n l'interruptor en ACTIVAT a dalt a la dreta i tria un predefinit. Obre el mode avançat per afinar els controls lliscants. L'efecte s'aplica immediatament al que estigui sonant.
{{% /details %}}

{{% details title="Quins efectes d'àudio té Evermusic?" closed="true" %}}
Sis efectes en temps real: normalització de volum (anivellament de sonoritat EBU R128), compressor (dinàmica), reverberació (espai i cua d'eco), crossfeed (imatge natural amb auriculars), retard (eco) i distorsió (aspresa lo-fi). Cadascun és independent i es pot fer servir sol o combinat.
{{% /details %}}

{{% details title="Els efectes canvien o malmeten els meus fitxers d'àudio?" closed="true" %}}
No. Tots els efectes s'apliquen en temps real només durant la reproducció. Mai no modifiquen ni recodifiquen els teus fitxers. Desactiva un efecte i el so original torna a l'instant.
{{% /details %}}

{{% details title="Puc utilitzar més d'un efecte alhora?" closed="true" %}}
Sí. Cada efecte és independent (no hi ha cap interruptor mestre), així que pots activar qualsevol combinació. Per exemple, normalització de volum més compressor per a una escolta constant i còmoda, o reverberació més crossfeed amb auriculars.
{{% /details %}}

{{% details title="Què és el crossfeed i l'hauria de fer servir?" closed="true" %}}
El crossfeed barreja una petita quantitat filtrada de cada canal estèreo amb l'altre perquè els auriculars sonin més com altaveus reals, reduint la sensació "dins del cap" de les mescles amb panoramitzat extrem. És un efecte per a auriculars (deixa'l desactivat per als altaveus). Està construït sobre l'algorisme Bauer stereophonic-to-binaural (bs2b) i inclou predefinits com Chu Moy i Jan Meier.
{{% /details %}}

{{% details title="Què és la normalització de volum i en què es diferencia de ReplayGain?" closed="true" %}}
La normalització de volum manté cada pista a una sonoritat constant mesurant la sonoritat percebuda amb l'estàndard EBU R128 i anivellant cap a un objectiu. A diferència de ReplayGain, no necessita etiquetes de sonoritat als teus fitxers i no altera l'àudio: funciona en directe amb qualsevol font, incloses les transmissions al núvol i la ràdio per internet. Predefinits: Suau, Estàndard, Fort i Nit.
{{% /details %}}

{{% details title="Quina diferència hi ha entre el mode Simple i l'Avançat?" closed="true" %}}
El mode Simple mostra una llista de predefinits amb descripcions planeres, així pots aconseguir un bon so amb un sol toc. El mode Avançat afegeix els controls lliscants de paràmetres (per exemple, Mescla per a la reverberació, o els set controls del compressor) per a un afinament precís. Commuta entre tots dos amb el botó de mode a dalt a la dreta de cada editor d'efectes.
{{% /details %}}

{{% details title="Per què els controls de l'efecte estan atenuats?" closed="true" %}}
L'efecte està desactivat. Activa l'interruptor de l'efecte a dalt a la dreta del seu editor per activar els controls. Cada efecte està desactivat per defecte.
{{% /details %}}

{{% details title="Els efectes funcionen amb la transmissió i CarPlay?" closed="true" %}}
Sí. Els efectes s'executen dins del motor de reproducció, així que s'apliquen a fitxers locals, discs al núvol, servidors multimèdia i ràdio per internet, i continuen funcionant durant la reproducció amb CarPlay.
{{% /details %}}
