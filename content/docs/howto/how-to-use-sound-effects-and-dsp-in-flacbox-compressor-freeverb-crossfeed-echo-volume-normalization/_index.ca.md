---
title: "Com utilitzar els efectes de so i el DSP a Flacbox: Compressor, Freeverb, Crossfeed, Echo, Normalització de volum i molt més"
date: 2026-07-24
description: "La guia completa de l'àudio de Flacbox a l'iPhone, l'iPad i el Mac. Aprèn com funciona el motor BASS, quins formats addicionals reprodueix (inclosa la música MOD i tracker i el DSD), i exactament què fa cada efecte, cada control lliscant i cada preajust al teu so, a més de l'equalitzador de 10 bandes i la cadena DSP personalitzada."
keywords: ["efectes d'àudio Flacbox", "preajustos Flacbox explicats", "motor BASS Flacbox", "biblioteca d'àudio BASS iOS", "reproductor de música MOD iPhone", "reproductor de música tracker iOS", "reproduir MOD XM IT S3M iPhone", "reproductor DSD iOS", "reproductor FLAC iPhone", "reproductor de música sense pèrdua iOS", "preajustos equalitzador Flacbox", "equalitzador de 10 bandes iPhone", "normalització de volum iPhone", "EBU R128 iOS", "normalització de sonoritat reproductor de música", "crossfeed auriculars iOS", "crossfeed bs2b", "preajustos compressor reproductor de música", "reverberació freeverb iOS", "echo delay reproductor de música", "cadena DSP reproductor de música", "reforç de greus iPhone", "com afegir efectes a la música Flacbox", "millors ajustos equalitzador iPhone"]
tags: ["Flacbox", "Efectes d'àudio", "Com fer-ho", "BASS", "Equalitzador", "Reforç de greus", "Compressor", "Freeverb", "Crossfeed", "Echo", "Normalització de volum", "EBU R128", "Música MOD", "Música tracker", "DSD", "FLAC", "DSP", "Auriculars", "Preajustos"]
readingTime: 30
---

{{< author-byline >}}

{{< full-width-tables >}}

**Resposta ràpida:** A Flacbox tries un **Motor de reproducció** a **Configuració > Reproductor d'àudio**: **Standard** (el motor del sistema d'Apple), **Universal** (el motor FFmpeg) o **Sound FX** (el **motor BASS™**). El motor que tries decideix quins formats de fitxer es reprodueixen, així que l'elecció importa. El motor **Sound FX** reprodueix formats addicionals que la majoria d'aplicacions de l'iPhone ignoren (FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i vella **música MOD i tracker** com MOD, XM, IT i S3M), i és l'únic motor que impulsa les eines de so: un **equalitzador de 10 bandes**, **Normalització de volum**, **Compressor**, **Freeverb**, **Auto Wah**, **Phaser**, **Flanger**, **Echo**, **Chorus**, **Distorsió**, **Rotate**, **Crossfeed** i una **cadena DSP** que crees tu mateix. Així que per utilitzar els efectes d'aquesta guia, primer estableix el teu Motor de reproducció a **Sound FX**. Cada eina té **preajustos** preparats. Obre'ls a **Configuració > Reproductor d'àudio** (Efectes d'àudio, Equalitzador d'àudio, Processament de senyal), o toca el botó **⋯ (Més accions)** al reproductor i tria **Efectes d'àudio**. Res del que facis aquí canvia mai els teus fitxers.

> Les explicacions dels controls lliscants i dels preajustos següents són les mateixes descripcions breus que Flacbox et mostra dins de l'aplicació, barrejades amb una mica de context addicional perquè tinguis la imatge completa abans de tocar.

## Com llegir aquesta guia

Cada eina funciona de la mateixa manera:

1. **Activa-la.** Cada efecte té el seu propi interruptor d'encès/apagat. Al principi estan tots apagats. Pots activar-ne tants com vulguis alhora.
2. **Tria un preajust.** Un preajust és una configuració preparada. Toca'n un i el so canvia a l'instant. Aquesta guia enumera què fa **cada** preajust.
3. **Ajusta amb precisió (opcional).** Obre els controls lliscants per ajustar-los a mà. En el moment que mous un control lliscant, l'efecte mostra **Manual**, així saps que has deixat el preajust. Cada control lliscant té un botó de restabliment.

No es desa res als teus fitxers. Aquests són efectes en directe. Apaga un efecte i el teu so original torna a l'instant.

## Tria el teu motor de reproducció (Sound FX té els efectes)

Flacbox no barreja els motors. En tries **un** a **Configuració > Reproductor d'àudio > Motor de reproducció**, i el motor que tries decideix quins formats de fitxer pots reproduir i si els efectes estan disponibles. Hi ha tres opcions, mostrades a l'aplicació amb aquests noms exactes:

1. **Standard.** El motor del sistema integrat d'Apple. Utilitza la descodificació per maquinari per a un menor consum de bateria.
2. **Universal.** El motor FFmpeg, que obre una gamma molt àmplia de formats.
3. **Sound FX.** El **motor BASS™**. Reprodueix fitxers sense pèrdua i d'alta resolució amb tota la precisió, afegeix música de mòdul (tracker) i impulsa cada efecte, l'equalitzador de 10 bandes i la cadena DSP d'aquesta guia.

Com que cada motor admet el seu propi conjunt de formats, els fitxers que pots reproduir canvien amb el motor que seleccionis. Més important encara, els efectes, l'equalitzador i la cadena DSP funcionen **només** amb el motor **Sound FX**, així que tria'l primer si els vols utilitzar.

Sound FX es basa en **BASS™**, una biblioteca d'àudio professional de Un4seen Developments. En pots llegir més a la seva pàgina d'inici a [un4seen.com](https://www.un4seen.com/).

## Formats de música: què afegeix el motor Sound FX (BASS™) (inclosa la música MOD i tracker)

Amb el motor **Sound FX (BASS™)** seleccionat, Flacbox reprodueix els formats especialitzats de sota, a més dels de cada dia. El més especial és la **música de mòdul**, també anomenada **música tracker**. Un fitxer de mòdul no és un enregistrament normal. Conté petits sons d'instruments més una «partitura» que diu com reproduir-los, i Flacbox reconstrueix la cançó en directe a partir d'aquesta partitura, tal com aquests fitxers estaven pensats per reproduir-se. Els reproductors normals no poden fer-ho.

| Tipus de música | Formats | Bo saber |
|---|---|---|
| **Música de mòdul / tracker** | MOD, XM, IT, S3M, MTM, UMX, MO3 | Reconstruïda en directe pel reproductor de mòduls BASS™. Perfecta per a chiptunes i velles cançons de la demoscene o d'Amiga. |
| **Sense pèrdua modern** | FLAC | Qualitat completa, més petit que WAV. |
| **Altres sense pèrdua** | WavPack (WV), Monkey's Audio (APE), TrueAudio (TTA), Musepack (MPC) | Tipus sense pèrdua menys habituals, tots admesos. |
| **DSD d'alta resolució** | DSF, DFF | Es reprodueix en maquinari normal utilitzant DSD sobre PCM. |
| **Amb pèrdua modern** | Opus, Ogg Vorbis, MP3 | Els tipus habituals de streaming i descàrrega. |

El motor Sound FX també reprodueix els formats principals d'Apple (AAC, ALAC, M4A, WAV, AIFF) i les transmissions en directe, així que els efectes i l'equalitzador també funcionen amb aquests.

**Per què t'ajuda això:** si tens una barreja d'àlbums FLAC, fitxers DSD d'alta resolució i una carpeta de velles cançons tracker MOD o XM, Flacbox les reprodueix totes, i l'equalitzador i els efectes funcionen amb cadascuna d'elles.

## Els tres menús que utilitzaràs

Flacbox manté les seves eines de so en tres llocs, tots dins de la configuració del reproductor d'àudio. Primer assegura't que el teu **Motor de reproducció** estigui establert a **Sound FX** (Configuració > Reproductor d'àudio > Motor de reproducció), perquè els efectes, l'equalitzador i la cadena DSP només estan disponibles amb aquest motor.

- **Efectes d'àudio** (el rack d'efectes): obre el reproductor, toca **⋯ (Més accions)**, toca **Efectes d'àudio**. O ves a **Configuració > Reproductor d'àudio > Efectes d'àudio**.
- **Equalitzador d'àudio** (10 bandes i preajustos): **Configuració > Reproductor d'àudio > Equalitzador d'àudio**.
- **Processament de senyal** (la teva pròpia cadena DSP): **Configuració > Reproductor d'àudio > Processament de senyal**.

També pots establir la **freqüència de mostreig de sortida**, els **canals** i la **mida del buffer** a **Configuració > Reproductor d'àudio**.

## L'equalitzador de 10 bandes

**Què fa:** Canvia el to de la música, des dels greus profunds fins als aguts brillants. És la millor eina per a un **reforç de greus** net o un extrem superior més brillant i clar. Pensa-hi com deu botons de volum, cadascun per a una porció diferent del so. Puja una banda per portar aquesta part endavant, baixa-la per tirar-la enrere. Els canvis petits d'uns pocs dB solen sonar millor, i funciona amb tot el que reprodueixes.

**Com funciona:** Deu controls lliscants a **32, 64, 125, 250, 500 Hz i 1, 2, 4, 8, 16 kHz**. Cadascun va de **-12 dB (tall)** a **+12 dB (reforç)**. També hi ha un **Preamplificador** de **-24 a +24 dB** per al nivell general. Pots desar els teus propis preajustos i **exportar-los o importar-los** entre dispositius.

**Què fa cada preajust integrat (22 preajustos):**

| Preajust | Què fa al teu so |
|---|---|
| **Flat** | Cap canvi. Totes les bandes a zero. Un punt de partida net. |
| **Acoustic** | Greus càlids i aguts nítids i presents. Fa que les guitarres acústiques i les veus semblin naturals i vives. |
| **Bass Booster** | Fort augment a l'extrem baix, mitjos i aguts intactes. Més cop i pes. |
| **Bass Reducer** | Retalla l'extrem baix. Útil per a sales retronants, auriculars barats o pistes pesades. |
| **Treble Booster** | Puja només els aguts. Afegeix brillantor i aire, més detall. |
| **Treble Reducer** | Suavitza els aguts. Domina els enregistraments durs o punxeguts. |
| **Classical** | Greus plens i aguts suaus amb una lleugera baixada de mitjos. Suau i espaiós per a música orquestral. |
| **Dance** | Greus grans i aguts brillants amb mitjos rebaixats. Contundent i enèrgic per a pistes de club. |
| **Deep** | Extrem baix càlid i espès amb aguts més suaus. Un so acollidor i relaxat. |
| **Electronic** | Greus forts i aguts brillants per a sintetitzadors i ritmes. Ampli i modern. |
| **Hip-Hop** | Greus pesats i aguts clars amb mitjos controlats. Amb pes i contundent. |
| **Jazz** | Càlid i suau, amb una petita baixada de mitjos. Fàcil i natural per a jazz acústic. |
| **Latin** | Greus i aguts reforçats amb mitjos nets. Brillant i viu. |
| **Loudness** | Reforça greus i aguts fortament (una corba de «somriure»). Sona més ple a volum baix. |
| **Lounge** | Mitjos endavant amb vores suaus. Relaxat i amigable per a veus. |
| **Piano** | Mitjos i aguts clars perquè les notes del piano ressonin netament. |
| **Pop** | Mitjos elevats per a les veus, amb greus i aguts tirats enrere. Les veus queden al davant. |
| **R&B** | Calidesa de mitjos-baixos molt forta i aguts clars. Suau i ric. |
| **Rock** | Greus i aguts reforçats per a guitarres i bateries. Enèrgic i ple. |
| **Small Speakers** | Reforça els greus i retalla els aguts per ajudar els altaveus diminuts a sonar més plens. |
| **Spoken Word** | Puja el rang de la veu i retalla els greus profunds. Fa clar el discurs. |
| **Vocal Booster** | Empeny el mig on viuen les veus, retalla al voltant. Les veus destaquen. |

**Consell per als greus:** Comença amb **Bass Booster**, després, si sona tèrbol, baixa el Preamplificador 1 o 2 dB perquè res es distorsioni.

## Normalització de volum (sonoritat uniforme)

**Què fa:** Algunes cançons es reprodueixen més fort que altres, així que no pares de canviar el volum. Això fa que cada cançó es reprodueixi a més o menys el mateix volum per si sola, així no ho has de fer tu. És perfecte per a llistes de reproducció aleatòries que barregen enregistraments vells i nous, àlbums diferents o fonts diferents, on una pista pot ser molt més forta que la següent.

**Com funciona:** Escolta la sonoritat real de cada pista utilitzant l'estàndard **EBU R128** (mesurat en **LUFS**, la mateixa idea que utilitzen els serveis de streaming), i després ajusta cada pista cap al teu objectiu. No necessita etiquetes als teus fitxers i mai canvia l'àudio. EBU R128 mesura la sonoritat que les teves orelles realment senten al llarg de tota la cançó, no només el pic més alt, per això coincideix amb com de fortes semblen realment les pistes. Flacbox ho calcula en directe mentre sona la música (i comprova la sonoritat amb antelació quan pot), després aplica un únic canvi de volum constant a la pista. El límit de **Reforç màxim** evita que els enregistraments molt fluixos siguin empesos tan fort que es distorsionin. Com que llegeix el mateix so, funciona amb qualsevol font, inclosos els fitxers al núvol, les transmissions en directe i la música de mòdul, fins i tot quan els fitxers no tenen cap etiqueta de sonoritat.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Sonoritat objectiu** | Estableix la sonoritat cap a la qual s'anivella cada pista. Els valors més alts fan que tot es reprodueixi més fort en general. | -30 a -6 LUFS (-16) |
| **Reforç màxim** | Limita quant es poden amplificar les pistes fluixes. Els valors més alts acosten els enregistraments suaus a l'objectiu. | 0 a 24 dB (12) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Light** | Anivellament suau per a escolta casual. Iguala els salts de volum evidents sense empènyer fort les pistes fluixes. |
| **Standard** | El predeterminat multiús. Un objectiu de sonoritat d'estil streaming que s'adapta a la majoria de música. Comença aquí. |
| **Strong** | Coincidència agressiva que empeny fermament amunt les pistes fluixes. Millor per a biblioteques barrejades amb grans diferències de nivell. |
| **Night** | Un objectiu general més tranquil que encara aixeca els passatges suaus, així l'escolta nocturna es manté constant i baixa. |

## Compressor (iguala les parts fortes i fluixes)

**Què fa:** En una mateixa cançó, les parts fluixes poden ser massa suaus i les fortes massa fortes. Això les acosta, així tota la cançó és fàcil de sentir, fins i tot al cotxe o en un lloc sorollós. Baixa suaument els moments més forts i aixeca els més suaus, així deixes d'estirar el volum durant una sola pista. Això és diferent de la Normalització de volum: el Compressor iguala les coses **dins** d'una cançó, mentre que la Normalització de volum iguala la sonoritat **entre** cançons. Els dos funcionen bé junts. Comença amb un preajust, i només obre els controls lliscants si vols més control.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Threshold** | El nivell on comença la compressió. Els valors més baixos aixafen més el so, mantenint les parts fluixes i fortes més juntes. | -60 a 0 dB (-20) |
| **Ratio** | Amb quina força es retenen les parts fortes un cop passen el llindar. Els valors més alts comprimeixen més fort, mantenint el so més uniforme. | 1:1 a 30:1 (4:1) |
| **Attack** | Amb quina rapidesa respon l'efecte a un pic fort sobtat. Els valors curts capten els transitoris; els més llargs els deixen passar. | 0.1 a 1000 ms (10 ms) |
| **Release** | Amb quina rapidesa deixa anar l'efecte després que passi la part forta. Els valors curts poden bombejar; els més llargs sonen més suaus. | 10 ms a 5 s (100 ms) |
| **Master gain** | Reforç de sortida final aplicat després del processament. Puja això per aixecar la sonoritat general un cop igualada la dinàmica. | -30 a +30 dB (0) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Transparent** | Xarxa de seguretat gairebé imperceptible. Preserva la dinàmica gairebé del tot i només capta els pics més forts. |
| **Soft** | Anivellament lleuger per a escolta hi-fi a casa. Suavitzat subtil sense aixafar la música. |
| **Standard** | Predeterminat sensat per a reproducció de música de cada dia. El primer preajust a provar. |
| **Heavy** | Anivellament agressiu per a entorns sorollosos. Cotxe, sala plena, escolta a volum baix. |
| **Voice / Podcast** | Ajustat per a la veu. Un atac més lent deixa passar les sibilants, un guany de compensació generós puja les veus. |
| **Old Recordings** | Àlbums vintage i vinil restaurat, on el nivell mitjà és inferior al de les publicacions modernes. |
| **Late Night** | Compressió pesada més un gran reforç per a escolta tranquil·la quan importen els veïns o la família adormida. |
| **Movie Dialog** | Aixeca el discurs davant la música i els efectes de so en una banda sonora variada. |
| **Streaming Match** | Apunta aproximadament a la normalització de sonoritat dels serveis de streaming moderns al voltant de -14 LUFS. |
| **Maximum Loudness** | A totes. Arriba al limitador; espera un senyal aixafat i molt anivellat. El preajust literal de volum màxim. |

## Freeverb (reverberació, una sensació d'espai)

**Què fa:** Afegeix una sensació d'espai a la música, des d'una sala petita fins a una gran sala de concerts. Tria un preajust, o ajusta tu mateix la barreja seca i humida, la mida de la sala, l'esmorteïment i l'amplada. La reverberació és l'eco natural que sents en qualsevol espai real, i Freeverb la recrea per programari. Una mica fa que els enregistraments plans o de micròfon proper se sentin més oberts i vius. Molta col·loca la música en un espai gran i llunyà. És un efecte creatiu, així que mantén la barreja humida modesta per a resultats naturals.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Dry mix** | Quant es manté del so original, intacte. Els valors més alts deixen més senyal seca a la barreja. | 0 a 1 (0.0) |
| **Wet mix** | Quant so reverberat s'afegeix. Els valors més alts fan la reverberació més forta i evident. | 0 a 3 (1.0) |
| **Room size** | La mida de l'espai imaginat. Els valors més alts donen una cua de reverberació més llarga i gran, des d'una sala petita fins a una catedral. | 0 a 1 (0.5) |
| **Damp** | Amb quina rapidesa s'esvaeixen les freqüències altes a la cua. Els valors més alts fan la reverberació més fosca i càlida. | 0 a 1 (0.5) |
| **Width** | La dispersió estèreo de la reverberació. Els valors més alts fan l'espai més ampli entre els canals esquerre i dret. | 0 a 1 (1.0) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Room** | Un espai petit i ajustat. Ambient subtil que afegeix una sensació de lloc sense esborrar el so. |
| **Studio** | Una sala d'enregistrament seca i controlada. Just la reflexió suficient per sonar natural. |
| **Hall** | Una gran sala de concerts. Una cua llarga i exuberant que s'adapta a la música orquestral i acústica. |
| **Cathedral** | Un enorme espai de pedra amb ressò. La cua de reverberació més llarga i dramàtica. |
| **Plate** | Una reverberació de placa d'estudi brillant i densa. Clàssica per a veus i bateries. |
| **Ambience** | Un ambient curt i airós. Afegeix una lleugera sensació d'espai mantenint-se majoritàriament sec. |

## Auto Wah (escombrat de filtre funky)

**Què fa:** Un filtre que fa un escombrat amunt i avall per si sol per a un so wah funky, semblant a una veu. Tria un preajust, o estableix tu mateix la barreja humida, la realimentació, la velocitat, el rang i la freqüència. És el mateix escombrat «wah» que fa un pedal wah de guitarra, però aquí es mou per si sol al ritme de la música. Sona genial en funk, disco i pistes electròniques. És un efecte atrevit i evident, així que una mica arriba lluny en l'escolta de cada dia.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Wet mix** | Com de fort és l'efecte wah a la barreja. Els valors més alts fan el filtre d'escombrat més evident. | -2 a +2 (1.5) |
| **Feedback** | Quant de la sortida es realimenta a l'efecte. Els valors més alts fan el wah més ressonant i pronunciat. | -1 a +1 (0.5) |
| **Rate** | Amb quina rapidesa el filtre fa l'escombrat amunt i avall. Els valors més alts donen un wah més ràpid i rítmic. | 0.1 a 9 Hz (2.0) |
| **Range** | Fins on arriba l'escombrat del filtre, en octaves. Els valors més alts donen un escombrat més ampli i dramàtic. | 0.1 a 9 octaves (4.3) |
| **Frequency** | La freqüència base al voltant de la qual fa l'escombrat el filtre. Els valors més baixos sonen més profunds; els més alts més brillants. | 1 a 1000 Hz (50) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Classic** | Un escombrat wah equilibrat i clàssic. Un bon punt de partida per a funk i rock. |
| **Slow** | Un escombrat lent i ampli que deriva suaument amunt i avall. Genial per a pads i notes llargues. |
| **Funky** | Un escombrat ràpid i contundent amb molt de moviment. Afegeix mossegada rítmica a guitarres i sintetitzadors. |
| **Deep** | Un escombrat profund i ampli que parteix d'una freqüència baixa. Gran i dramàtic. |
| **Subtle** | Un moviment suau i discret. Afegeix caràcter sense dominar el so. |
| **Resonant** | Un wah agut i ressonant amb realimentació alta. Semblant a una veu i expressiu. |

## Phaser (remolí sibilant)

**Què fa:** Un filtre d'escombrat que afegeix un moviment de remolí i xiulet al so. Tria un preajust, o estableix tu mateix la realimentació, la velocitat, el rang i la freqüència. Afegeix moviment suau i brillantor sense canviar les notes. És subtil en veus i pads, i dramàtic en sintetitzadors i guitarres. Prova Slow per a una sensació onírica o Jet per a un remolí fort.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Feedback** | Quant de la sortida es realimenta a l'efecte. Els valors més alts fan el phaser més ressonant i pronunciat. | -1 a +1 (0.0) |
| **Rate** | Amb quina rapidesa el filtre fa l'escombrat amunt i avall. Els valors més alts donen un phasing més ràpid i rítmic. | 0.1 a 9 Hz (1.0) |
| **Range** | Fins on arriba l'escombrat del filtre, en octaves. Els valors més alts donen un escombrat més ampli i dramàtic. | 0.1 a 9 octaves (4.0) |
| **Frequency** | La freqüència base al voltant de la qual fa l'escombrat el filtre. Els valors més baixos sonen més profunds; els més alts més brillants. | 1 a 1000 Hz (100) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Classic** | Un escombrat de phaser equilibrat i clàssic. Un bon punt de partida per a guitarres i teclats. |
| **Slow** | Un escombrat lent i ampli que deriva suaument amunt i avall. Genial per a pads i notes llargues. |
| **Fast** | Un escombrat ràpid i brillant amb molt de moviment. Afegeix moviment i energia. |
| **Deep** | Un escombrat profund i ampli que parteix d'una freqüència baixa. Gran i dramàtic. |
| **Subtle** | Un moviment suau i discret. Afegeix caràcter sense dominar el so. |
| **Jet** | Un escombrat intens i ressonant amb realimentació alta, el clàssic xiulet d'avió a reacció. |

## Flanger (escombrat d'avió a reacció)

**Què fa:** Un retard curt i mòbil que dóna al so un xiulet d'escombrat semblant a un avió a reacció. Tria un preajust, o estableix tu mateix la profunditat, la realimentació, la velocitat i el retard. És un cosí més fort i metàl·lic del phaser, famós pel xiulet d'escombrat del rock clàssic i de la música electrònica. Els ajustos subtils afegeixen moviment suau, mentre que els ajustos profunds són dramàtics i evidents. Millor utilitzat amb moderació, per a efecte.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Depth** | Com de fort és l'efecte d'escombrat. Els valors més alts fan el flanging més evident. | 0 a 100% (25) |
| **Feedback** | Quant de la sortida es realimenta a l'efecte. Els valors més alts fan el flanger més ressonant i metàl·lic. | -99 a +99% (-50) |
| **Rate** | Amb quina rapidesa es mou l'escombrat amunt i avall. Els valors més alts donen un moviment més ràpid i brillant. | 0 a 10 Hz (0.25) |
| **Delay** | El temps de retard base sobre el qual es construeix l'escombrat. Els valors més alts donen un caràcter més profund i buit. | 0 a 4 ms (2.0) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Classic** | Un flanger equilibrat i clàssic. Un bon punt de partida per a guitarres i teclats. |
| **Subtle** | Un escombrat suau i discret. Afegeix moviment sense dominar el so. |
| **Deep** | Un escombrat profund i pesat amb realimentació forta. Gran i dramàtic. |
| **Jet** | Un escombrat intens amb realimentació positiva, el clàssic xiulet d'avió a reacció. |
| **Fast** | Un escombrat ràpid i brillant amb molt de moviment i energia. |
| **Wide** | Un escombrat lent i ampli amb un retard llarg. Exuberant i espaiós. |

## Echo (repeticions)

**Què fa:** Repeteix el so com ecos que s'esvaeixen per a una sensació d'espai i profunditat. Tria un preajust, o estableix tu mateix la barreja humida, la realimentació i el retard. És com cridar en un canó: el so torna una o més vegades després d'un breu buit. Una única repetició curta afegeix cos i una sensació retro, mentre que les repeticions més llargues amb més realimentació creen cues espaioses i persistents. El preajust Ping Pong fa rebotar les repeticions entre les teves orelles esquerra i dreta, la qual cosa és divertida amb auriculars. Mantén la barreja humida modesta perquè els ecos donin suport a la música en lloc de cobrir-la.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Wet mix** | Com de fort són els ecos comparats amb el so original. Els valors més alts fan que les repeticions destaquin més. | -2 a +2 (0.6) |
| **Feedback** | Quantes vegades es repeteix l'eco. Els valors més alts donen més repeticions que triguen més a esvair-se. | -1 a +1 (0.5) |
| **Delay** | El temps entre ecos. Els valors més curts donen un slap-back ajustat; els més llargs donen repeticions espaiades. | 0.01 a 2 s (0.4) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Slapback** | Una única repetició ajustada just darrere del so. Slap-back clàssic de rockabilly. |
| **Room** | Un eco curt i natural, com una sala petita. Afegeix espai sense difuminar el so. |
| **Tape** | Repeticions càlides i mitjanes que s'esvaeixen gradualment, com un vell retard de cinta. |
| **Dub** | Repeticions llargues i pesades amb realimentació forta. Gran, dubby i espaiós. |
| **Ping Pong** | Els ecos reboten entre els altaveus esquerre i dret per a un ampli efecte estèreo. |
| **Long** | Repeticions lentes i molt espaiades que s'allunyen molt darrere del so. |

## Chorus (so més gruixut i ampli)

**Què fa:** Engreixa i amplia el so superposant una còpia canviant sobre l'original. Tria un preajust, o estableix tu mateix la barreja humida/seca, la profunditat, la velocitat i la realimentació. Fa que un instrument o veu soni com diversos tocant junts, afegint còpies lleugerament desafinades i mòbils. Això afegeix riquesa i una brillantor suau. Els ajustos subtils escalfen les coses, mentre que els ajustos forts sonen exuberants i onírics. És popular en guitarres, teclats i veus.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Wet/Dry** | Quant chorus sents comparat amb el so original. Els valors més alts fan l'efecte més evident. | 0 a 100% (50) |
| **Depth** | Fins on oscil·la el to amunt i avall. Els valors més alts donen un so més gruixut i brillant. | 0 a 100% (25) |
| **Rate** | Amb quina rapidesa es mou la brillantor. Les velocitats més lentes sonen suaus i exuberants; les més ràpides sonen més com un vibrato. | 0 a 10 Hz (1.1) |
| **Feedback** | Quant de l'efecte es realimenta a si mateix. Els valors més alts fan el chorus més ressonant i intens. | -99 a +99% (25) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Subtle** | Un engreixament suau que afegeix calidesa sense cridar l'atenció sobre si mateix. |
| **Lush** | Un chorus ric i clàssic. Un gran ajust polivalent per a guitarres i teclats. |
| **Ensemble** | Una brillantor plena i en capes que fa que un únic instrument soni com diversos. |
| **Vibrato** | Completament humit amb una velocitat ràpida, per a un vibrato oscil·lant en lloc d'un chorus subtil. |
| **Wide** | Una brillantor lenta i àmplia que obre la imatge estèreo. Espaiós i oníric. |
| **Twelve-String** | Una brillantor brillant i ressonant que recorda una guitarra de dotze cordes. |

## Distorsió (aspror i vora)

**Què fa:** Afegeix aspror i vora sobrepilotant el so. Tria un preajust, o estableix tu mateix el drive, la sortida i el to. Endureix deliberadament el so, des d'una vora càlida i aspra fins a un to trencat i difús. És un efecte creatiu i divertit més que una manera de millorar la qualitat, així que utilitza'l en petites quantitats. És divertit en pistes electròniques, de rock i experimentals. Baixa la Sortida si un preajust pesat es fa massa fort.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Drive** | Com de fort es distorsiona el so. Els valors més alts són més aspres i agressius. | 0 a 100% (15) |
| **Output** | El nivell de sortida després de la distorsió. Baixa'l si un ajust pesat es fa massa fort. | -60 a 0 dB (-18) |
| **Tone** | Retalla els aguts abans de la distorsió. Els valors més baixos sonen més foscos i càlids. | 100 a 8000 Hz (8000) |
| **Center** | Al voltant de quina freqüència es focalitza la distorsió. Desplaça el caràcter cap a més brillant o més fosc. | 100 a 8000 Hz (2400) |
| **Width** | Com d'amplia és aquest focus. Estret sona agut i nasal; ampli sona ple i obert. | 100 a 8000 Hz (2400) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Warm Drive** | Una aspror lleugera i càlida que afegeix vora sense canviar gaire el caràcter. |
| **Crunch** | Un overdrive cruixent clàssic, contundent i rítmic. |
| **Overdrive** | Un to brillant i impulsat amb molta mossegada. Genial per a sons solistes. |
| **Fuzz** | Un fuzz gruixut i saturat. Pesat i ple d'harmònics. |
| **Metal** | Un to d'alt guany, ajustat i centrat en mitjos per a sons agressius i pesats. |
| **Screamer** | Un overdrive amb mitjos reforçats que talla, com un tube screamer. |
| **LoFi** | Una distorsió aixafada i de banda estreta per a un caràcter lo-fi aspre. |

## Rotate (estèreo giratori)

**Què fa:** Fa girar el so pel camp estèreo per a un efecte rotatori i de remolí. Tria un preajust, o estableix tu mateix la velocitat. Mou lentament el so pels teus canals esquerre i dret, una mica com un altaveu giratori, la qual cosa afegeix una sensació de remolí i hipnòtica. Els ajustos lents són suaus i amplis, mentre que els ajustos ràpids són marejadors i evidents. És un efecte estèreo, així que es nota més amb auriculars o altaveus ben col·locats.

**Control lliscant:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Rate** | Amb quina rapidesa gira el so pel camp estèreo. Els valors negatius giren en sentit contrari; zero el manté quiet. | -5 a +5 Hz (1.0) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Slow Pan** | Una deriva lenta i suau de banda a banda. Subtil i àmplia. |
| **Sway** | Un balanceig constant esquerra-dreta. Afegeix moviment suau a la imatge estèreo. |
| **Rotary** | Un gir mitjà que recorda un altaveu giratori. |
| **Fast Spin** | Un gir ràpid pel camp estèreo per a un efecte marejador i de remolí. |
| **Reverse** | Un gir mitjà en la direcció oposada. |
| **Whirl** | Un remolí molt ràpid. Intens i desorientador. |

## Crossfeed (so natural amb auriculars)

Amb altaveus, cadascuna de les teves orelles sent tant l'altaveu esquerre com el dret, només que en moments i volums lleugerament diferents. Amb auriculars, aquesta barreja natural desapareix: la teva orella esquerra sent només el canal esquerre i la teva orella dreta només el dret. Aquest «súper estèreo» pot fer que la música sembli dividida dins del teu cap, i els enregistraments amb panoràmica extrema, on un instrument seu completament en un costat, poden semblar antinaturals o cansats en escoltes llargues.

Crossfeed ho arregla barrejant una petita quantitat filtrada de cada canal a l'altre, amb un retard diminut i un descens suau de les freqüències altes. Això s'apropa a com el so d'altaveus reals arriba a totes dues orelles, incloent la manera com el teu cap fa una lleugera ombra a l'orella llunyana. El resultat és una imatge més natural, semblant a la d'altaveus, que seu una mica davant teu en lloc de dins del teu cap, i redueix la fatiga d'escolta en sessions llargues. Flacbox utilitza el conegut mètode **bs2b (Bauer stereophonic-to-binaural)**, un crossfeed de codi obert respectat que utilitzen molts reproductors audiòfils. En pots llegir sobre l'algoritme a la [pàgina del projecte bs2b](https://bs2b.sourceforge.net/).

El **Cutoff** controla com de càlida sona la barreja, i el **Feed level** controla com de forta és. Els preajustos cobreixen els nivells clàssics de bs2b, des d'un toc gairebé imperceptible fins a una barreja ferma, semblant a la d'altaveus. Crossfeed és un efecte per a auriculars, així que deixa'l apagat quan escoltis amb altaveus.

**Controls lliscants:**

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Cutoff** | Estableix on comença a descendir la fuga entre canals. Els valors més baixos donen un efecte més càlid i pronunciat. | 300 a 2000 Hz (700) |
| **Feed level** | Controla quant d'un canal es fuga a l'altre. Els valors més alts produeixen un so més semblant al d'altaveus. | 1 a 15 dB (4.5) |

**Preajustos:**

| Preajust | Què fa |
|---|---|
| **Subtle** | Crossfeed gairebé imperceptible per a escolta casual. Suavitza l'estèreo de panoràmica extrema sense canviar l'equilibri tonal. |
| **Chu Moy** | El predeterminat clàssic multiús. Equilibrat i lleugerament càlid, funciona amb gairebé qualsevol material. Comença aquí. |
| **Strong** | Fuga més forta per a mescles de panoràmica més extrema. Estretament estèreo més evident. |
| **Jan Meier** | Popular entre els entusiastes dels auriculars. Fuga més àmplia, presentació més semblant a la d'altaveus, lleuger augment de greus. |
| **Speaker-like** | Ajustat per a la reproducció d'estil altaveu més natural amb auriculars. |
| **Vintage Stereo** | Crossfeed agressiu ajustat per a mescles dels anys 1960 i 1970 amb bateries i veus de panoràmica extrema. |

## Processament de senyal: construeix la teva pròpia cadena DSP

Més enllà dels efectes preparats, Flacbox et permet construir la teva pròpia cadena a **Configuració > Reproductor d'àudio > Processament de senyal**. Com explica l'aplicació quan la cadena és buida: *«Toca + per afegir un efecte. Activa o desactiva cadascun amb el seu interruptor, arrossega per reordenar, toca per editar-ne els paràmetres, i mantén premut per duplicar o eliminar.»*

L'**ordre importa**: un filtre abans d'una distorsió sona diferent del mateix filtre després. També pots dirigir tota la cadena a **Tots els canals**, **Canal esquerre** o **Canal dret**.

A sota hi ha cada bloc, amb el text propi de l'aplicació per a cada control lliscant i cada preajust.

### Gain (retall de nivell)

Puja o baixa el nivell en un punt de la cadena.

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Gain** | Reforça o retalla el nivell en aquest punt de la cadena. Utilitza'l per compensar el nivell després d'altres efectes, o per impulsar els que segueixen. | -24 a +24 dB (0) |

| Preajust | Què fa |
|---|---|
| **Unity** | Cap canvi de nivell. Un punt de partida neutre. |
| **Cut** | Un gran tall. Domina una font forta, o fa lloc abans dels efectes que segueixen. |
| **Trim** | Un tall suau per tirar el nivell una mica enrere. |
| **Lift** | Un reforç modest per pujar una font fluixa. |
| **Boost** | Un reforç fort per a material fluix, o per impulsar més fort els efectes següents. |
| **Max** | Reforç màxim. Fort, vigila el retall més endavant a la cadena. |

### Low Pass (elimina aguts)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Cutoff** | Estableix on comença el filtre a descendir els aguts. Baixa'l per enfosquir i suavitzar el so; puja'l cap amunt per obrir del tot. | 20 Hz a 20 kHz (20 kHz) |
| **Resonance** | Emfatitza les freqüències just al punt de tall. Mantén-lo baix per a un descens net; puja'l per a una vora punxeguda i sibilant. | 0.1 a 10 (0.707) |

| Preajust | Què fa |
|---|---|
| **Air** | Retalla només la part més alta. Treu una mica de vora sense apagar el so. |
| **Warm** | Un descens suau dels aguts per a un to més càlid i arrodonit. |
| **Mellow** | Notablement suavitzat. Tira la brillantor enrere per a una sensació relaxada. |
| **Muffled** | Fosc i esmorteït, com si se sentís a través d'una paret. |
| **Telephone** | Un pic estret i ressonant a la part baixa del rang. Una veu prima, semblant a un telèfon. |

### High Pass (elimina greus)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Cutoff** | Estableix on comença el filtre a descendir els greus. Puja'l per aprimar l'extrem baix i eliminar el retruny; baixa'l cap avall per obrir del tot. | 20 Hz a 20 kHz (20 Hz) |
| **Resonance** | Emfatitza les freqüències just al punt de tall. Mantén-lo baix per a un descens net; puja'l per a una vora punxeguda i sibilant. | 0.1 a 10 (0.707) |

| Preajust | Què fa |
|---|---|
| **Rumble Cut** | Elimina el retruny subsònic i el desplaçament de DC sense tocar l'extrem baix audible. |
| **Tighten** | Retalla les freqüències baixes retronants per a uns greus més ajustats i nets. |
| **Thin** | Retalla la calidesa i el cos, deixant un so més lleuger i prim. |
| **Radio** | Només romanen els mitjos i els aguts, com un petit altaveu de ràdio. |
| **Telephone** | Un pic estret i ressonant a la part alta del rang. Una veu prima, semblant a un telèfon. |

### Band Pass (manté una banda central)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Center** | Estableix la freqüència que passa el filtre. Tot per sobre i per sota es descendeix. Fes un escombrat per triar greus, mitjos o aguts. | 20 Hz a 20 kHz (1 kHz) |
| **Resonance** | Controla com d'amplia és la banda. Els valors baixos deixen passar un rang ampli; puja'l per estretir cap al centre per a un to agut i ressonant. | 0.1 a 10 (0.707) |

| Preajust | Què fa |
|---|---|
| **Voice** | Una banda àmplia al voltant del rang mitjà on seu la majoria de veus. Un punt de partida neutre. |
| **Bass** | Aïlla l'extrem baix, deixant només el baix i el bombo. |
| **Body** | Es focalitza en els mitjos-baixos per a un cos càlid i encaixonat. |
| **Presence** | Aixeca els mitjos-alts per a claredat i presència. |
| **Telephone** | Una banda de rang mitjà estreta. Un so prim, semblant a un telèfon. |
| **Wah** | Un pic molt estret i ressonant. Fes un escombrat del centre per a un efecte wah. |

### Notch (elimina una banda estreta)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Frequency** | Estableix la freqüència que elimina el filtre. Tot per sobre i per sota hi passa. Ajusta'l sobre un brunzit o ressonància per tallar-lo. | 20 Hz a 20 kHz (60 Hz) |
| **Resonance** | Controla com d'ampli és el tall. Els valors baixos treuen un rang ampli; puja'l per eliminar només una banda puntual i deixar la resta intacta. | 0.1 a 10 (8.0) |

| Preajust | Què fa |
|---|---|
| **Mains Hum 60** | Elimina el brunzit elèctric de 60 Hz (xarxa nord-americana). Un punt de partida neutre. |
| **Mains Hum 50** | Elimina el brunzit elèctric de 50 Hz (xarxa europea i d'altres). |
| **Rumble** | Retalla un retruny o ressonància de baixa freqüència sense aprimar tot l'extrem baix. |
| **Mud** | Treu el fang dels mitjos-baixos per a un so més net i clar. |
| **Boxy** | Elimina un ressò encaixonat de rang mitjà. |
| **Harsh** | Domina un pic dur i penetrant als mitjos-alts. |

### Peaking (banda EQ paramètrica)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Frequency** | El centre de la banda a reforçar o retallar. Fes un escombrat per trobar la freqüència que vols modelar. | 20 Hz a 20 kHz (1 kHz) |
| **Gain** | Quant reforçar o retallar al centre. Positiu aixeca la banda; negatiu la treu. | -15 a +15 dB (0) |
| **Q factor** | Estableix com d'amplia és la banda. Els valors baixos modelen una àrea àmplia; els alts estreteixen per a canvis quirúrgics i puntuals. | 0.1 a 10 (1.0) |

| Preajust | Què fa |
|---|---|
| **Presence** | Un ampli augment de mitjos-alts per a claredat i presència. Un punt de partida neutre. |
| **Warmth** | Un ampli reforç de mitjos-baixos que afegeix cos i calidesa. |
| **Vocal Boost** | Aixeca el rang vocal central per portar les veus endavant. |
| **Cut Mud** | Treu el fang encaixonat de mitjos-baixos per a un so més net. |
| **Tame Harsh** | Un tall estret per dominar un pic dur i penetrant. |
| **Punch** | Un reforç baix que afegeix cop i impacte a l'extrem baix. |
| **Sub Boost** | Un reforç profund a la part més baixa per a pes subgreu addicional. |
| **Air** | Un ampli augment a la part més alta per a una lluïssor oberta i airosa. |
| **Clarity** | Aixeca els mitjos-alts per afegir definició i vora. |
| **De-Ess** | Un tall estret al rang de sibilància per dominar els sons S durs. |
| **De-Boom** | Retalla una acumulació retronant de baixa freqüència per a un extrem baix més ajustat. |
| **Scoop** | Una àmplia baixada de rang mitjà per a un to rebaixat i modern. |

### Low Shelf (control de greus i reforç de greus)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Frequency** | Estableix el punt per sota del qual actua el shelf. Tot per sota es reforça o es retalla junt. | 20 a 2000 Hz (200) |
| **Gain** | Quant aixecar o baixar l'extrem baix. Positiu afegeix pes i calidesa; negatiu l'aprima. | -15 a +15 dB (0) |

| Preajust | Què fa |
|---|---|
| **Warmth** | Un augment suau de l'extrem baix per a calidesa i cos. Un punt de partida neutre. |
| **Bass Boost** | Un reforç sòlid als greus per a pes i cop. |
| **Fullness** | Omple els mitjos-baixos per a un so més ple i arrodonit. |
| **Trim Bass** | Un tall modest per alleugerir una mescla amb greus pesats. |
| **Cut Lows** | Un tall fort per aprimar o treure el retruny de l'extrem baix. |
| **Big Bottom** | Un gran reforç de l'extrem baix per a pes i retruny màxims. |

### High Shelf (control d'aguts)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Frequency** | Estableix el punt per sobre del qual actua el shelf. Tot per sobre es reforça o es retalla junt. | 1 a 20 kHz (8 kHz) |
| **Gain** | Quant aixecar o baixar l'extrem alt. Positiu afegeix brillantor i aire; negatiu suavitza i enfosqueix. | -15 a +15 dB (0) |

| Preajust | Què fa |
|---|---|
| **Presence** | Un augment suau de l'extrem alt per a claredat i detall. Un punt de partida neutre. |
| **Air** | Obre la part més alta per a un so airós i obert. |
| **Bright** | Un reforç fort per a un to nítid, brillant i endavant. |
| **Soften** | Un tall modest per treure la vora dels aguts durs. |
| **Tame Highs** | Un tall fort per enfosquir i suavitzar un so massa brillant. |
| **Sparkle** | Un gran reforç de la part més alta per a brillantor i lluïssor màximes. |

### Soft Clip (saturació càlida)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Drive** | Empeny el senyal més fort dins del modelador d'ona. Quantitats baixes afegeixen calidesa suau; quantitats altes arrodoneixen els pics en saturació espessa i aspror. | 0 a 40 dB (0) |

| Preajust | Què fa |
|---|---|
| **Warm** | Un toc de drive per a una calidesa suau d'estil analògic. |
| **Drive** | Saturació notable que engreixa i acoloreix el so. |
| **Crunch** | Drive pesat amb una vora cruixent audible. |
| **Fuzz** | Distorsió espessa i difusa. Els pics s'aixafen fort. |
| **Destroy** | Drive màxim. Aspror agressiva i totalment saturada. |

### Bit Crusher (lo-fi retro)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Bit depth** | Estableix quants bits descriuen cada mostra. Menys bits signifiquen passos més grollers i més soroll de quantificació, per a un so digital cruixent i aspre. | 1 a 16 bits (16) |
| **Sample rate** | Redueix el mostreig de l'àudio. Al cent per cent la freqüència queda intacta; baixa-la per mantenir cada mostra més temps, apagant els aguts i afegint una vora dura i amb àlies. | 1% a 100% (100%) |

| Preajust | Què fa |
|---|---|
| **Vintage** | Una caiguda subtil de qualitat, com un dels primers mostrejadors digitals. |
| **LoFi** | Lo-fi clàssic de 8 bits, a mitja freqüència. Granulós i retro. |
| **Crunch** | Aixafament més pesat amb una vora cruixent audible. |
| **Gritty** | Groller i aspre. Els passos entre nivells són evidents. |
| **Destroy** | Reducció extrema. Dur, trencat, gairebé irrecognoscible. |

### Ring Modulator (tons metàl·lics i robòtics)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Carrier** | Estableix la freqüència del to pel qual es multiplica el senyal. Uns pocs hertzs donen un tremolo oscil·lant; les freqüències més altes afegeixen sobretons metàl·lics, de campana i robòtics. | 1 a 4000 Hz (440) |
| **Mix** | Barreja el so modulat amb l'original. Al zero per cent només sents el senyal sec; al cent per cent només el to totalment modulat. | 0% a 100% (0%) |

| Preajust | Què fa |
|---|---|
| **Tremolo** | Una portadora molt baixa el converteix en un tremolo d'amplitud, oscil·lant el volum. |
| **Robot** | Una portadora mitjana afegeix sobretons metàl·lics per a un efecte clàssic de veu de robot. |
| **Metallic** | Sobretons densos i inharmònics per a un to dur i metàl·lic. |
| **Bell** | Una portadora més alta dóna un dring brillant, semblant a una campana. |
| **Alien** | Totalment humit amb una portadora alta. Extrem, alienígena, gairebé irrecognoscible. |

### Tremolo (oscil·lació de volum)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Rate** | Estableix amb quina rapidesa pulsa el volum. Les velocitats més lentes donen un balanceig suau; les més ràpides donen un tremolor ràpid. | 0.1 a 20 Hz (5) |
| **Depth** | Estableix quant baixa el volum a cada pols. Al zero per cent el nivell és constant; al cent per cent baixa fins al silenci total. | 0% a 100% (0%) |

| Preajust | Què fa |
|---|---|
| **Gentle** | Un balanceig lent i superficial. Moviment subtil sense cridar l'atenció. |
| **Classic** | El tremolo clàssic d'amplificador: una velocitat mitjana i profunditat moderada. |
| **Deep** | Un pols fort i profund que gairebé baixa al silenci a cada cicle. |
| **Fast** | Un tremolor ràpid per a una sensació brillant i nerviosa. |
| **Chop** | Ràpid i a profunditat total. Un tall dur i entretallat. |

### Delay (eco)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Time** | Estableix el buit abans de cada eco. Els temps curts donen un slapback ajustat; els més llargs espaien més les repeticions. | 0.01 a 2 s (0.25) |
| **Feedback** | Estableix quant de cada eco es realimenta. Els valors baixos donen una única repetició; els més alts construeixen una llarga sèrie persistent d'ecos. | 0 a 0.95 (0.4) |
| **Mix** | Barreja els ecos amb l'original. Al zero per cent només sents el senyal sec; al cent per cent només els ecos. | 0% a 100% (0%) |

| Preajust | Què fa |
|---|---|
| **Slapback** | Un únic eco curt, ajustat contra l'original. Rockabilly i doblatge de veus. |
| **Echo** | L'eco clàssic: una repetició clara amb unes poques cues persistents. |
| **Ping** | Una repetició ràpida i rebotant que afegeix moviment rítmic. |
| **Ambient** | Repeticions més llargues i suaus que es dilueixen en una cua espaiosa. |
| **Dub** | Realimentació alta per a llargues cascades dubby d'eco. |
| **Cavern** | Repeticions llargues i profundes, com un so fent eco a través d'un espai enorme. |

### Stereo Width (estretir o ampliar)

| Control | Què fa | Rang (predeterminat) |
|---|---|---|
| **Width** | Estretix o amplia la imatge estèreo. El zero per cent col·lapsa a mono, el cent per cent la deixa intacta, i els valors més alts empenyen els costats més amplis. Només afecta les pistes estèreo amb l'objectiu Tots els canals. | 0% a 200% (100%) |

| Preajust | Què fa |
|---|---|
| **Wide** | Una ampliació suau que obre la imatge estèreo. Un punt de partida neutre. |
| **Wider** | Una dispersió més forta per a un camp estèreo gran i immersiu. |
| **Max** | Amplada màxima. Molt ampli, però vigila els problemes de compatibilitat mono. |
| **Narrow** | Tira els costats endins per a una imatge més ajustada i centrada. |
| **Focused** | Gairebé centrat, amb només un toc d'estèreo. |
| **Mono** | Totalment col·lapsat a mono. Tots dos altaveus reprodueixen el mateix senyal. |

## Com funciona tot per dins (versió simple)

- **Motors:** en tries un a Configuració > Reproductor d'àudio > Motor de reproducció: **Standard** (sistema), **Universal** (FFmpeg) o **Sound FX** (el **motor BASS™** de [Un4seen Developments](https://www.un4seen.com/)). El motor que tries decideix quins formats es reprodueixen, i els efectes, l'equalitzador i la cadena DSP funcionen només al motor Sound FX.
- **Formats:** el motor BASS™ afegeix FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i música de mòdul (tracker) a més dels formats del sistema i de FFmpeg.
- **Efectes:** l'equalitzador, el compressor i la majoria d'efectes utilitzen els complements d'efectes de BASS™. Freeverb és la reverberació Freeverb. Chorus, Flanger i Distorsió utilitzen efectes clàssics d'estil DirectX amb els seus propis controls.
- **Normalització de volum:** un anivellador de sonoritat **EBU R128** en directe (l'estàndard de sonoritat utilitzat en la difusió i el streaming).
- **Crossfeed:** el crossfeed **bs2b (Bauer)**, executat dins del motor BASS™.
- **Cadena DSP:** els teus blocs personalitzats, aplicats en l'ordre exacte que estableixes, a tots els canals o només a un costat.
- **Sortida:** pots establir la freqüència de mostreig, el nombre de canals i la mida del buffer per adaptar-se al teu equip.

Com que tot això s'executa en directe mentre sona la música, els efectes:

- Funcionen en **temps real** amb tot, inclosos els fitxers al núvol, les transmissions i la música de mòdul.
- **Mai canvien ni tornen a desar** els teus fitxers. Apaga un efecte i l'original torna.
- **Recorden els teus ajustos** de cada efecte.
- Es poden **barrejar i combinar** lliurement, ja que cadascun és independent.

## Receptes senzilles per provar

**Escolta de cada dia**

- **Més greus, netament:** Equalitzador > Bass Booster, després baixa el Preamplificador 1 o 2 dB. O afegeix un Low Shelf de DSP a Bass Boost.
- **Volum uniforme en una llista de reproducció barrejada:** Normalització de volum > Standard, més Compressor > Soft.
- **Poliment general suau:** Compressor > Transparent, més Normalització de volum > Light.
- **Veus més clares:** Equalitzador > Vocal Booster, o un bloc Peaking de DSP a Vocal Boost.
- **So més ple en altaveus petits de telèfon:** Equalitzador > Small Speakers.

**Auriculars**

- **Més agradable, menys cansat amb auriculars:** Crossfeed > Chu Moy o Jan Meier.
- **So més ampli amb auriculars:** Stereo Width de DSP > Wide, més Crossfeed > Chu Moy.
- **Arregla discos de panoràmica extrema dels anys 1960 i 1970:** Crossfeed > Vintage Stereo.
- **Una mica d'aire i espai:** Freeverb > Ambience, mantingut baix, més Crossfeed > Subtle.

**Estones tranquil·les i àudio parlat**

- **Escolta tranquil·la nocturna:** Normalització de volum > Night, més Compressor > Late Night.
- **Podcasts i audiollibres:** Compressor > Voice / Podcast, més Equalitzador > Spoken Word.
- **El so més fort i uniforme en un cotxe sorollós:** Normalització de volum > Strong, més Compressor > Heavy.

**Solucionar problemes**

- **Domina un enregistrament dur i brillant:** Equalitzador > Treble Reducer, o un bloc Peaking de DSP a Tame Harsh.
- **Elimina el brunzit elèctric:** cadena DSP > Notch > Mains Hum 60 (o Mains Hum 50 a Europa).
- **Greus més ajustats i nets:** High Pass de DSP > Tighten, per tallar l'extrem baix retronant.
- **Menys retruny en una mescla amb greus pesats:** Low Shelf de DSP > Trim Bass, o Peaking > De-Boom.

**Creatiu i divertit**

- **Sensació càlida i espaiosa:** Freeverb > Hall, mantingut baix.
- **Guitarres oníriques i espaioses:** Chorus > Wide, més Echo > Long.
- **Lo-fi retro:** cadena DSP > Bit Crusher (LoFi) cap a Soft Clip (Warm).
- **Moviment funky en pistes electròniques:** Auto Wah > Funky, o Phaser > Fast.
- **Escombrat clàssic d'avió a reacció:** Flanger > Jet.

## Preguntes freqüents

{{% details title="Quin motor de so utilitza Flacbox?" closed="true" %}}
Tries un Motor de reproducció a Configuració > Reproductor d'àudio: Standard (el motor del sistema d'Apple), Universal (el motor FFmpeg) o Sound FX (el motor BASS™ de Un4seen Developments, un4seen.com). El motor que tries decideix quins formats de fitxer es reprodueixen. Sound FX és el que reprodueix formats addicionals com FLAC, DSD, WavPack, APE, Musepack, TrueAudio, Opus i música MOD o tracker, i és l'únic motor que proporciona els efectes en directe, l'equalitzador de 10 bandes i la cadena DSP. Per utilitzar els efectes, estableix el Motor de reproducció a Sound FX.
{{% /details %}}

{{% details title="Pot Flacbox reproduir música MOD, XM, IT i altra música tracker o de mòdul?" closed="true" %}}
Sí. El motor BASS™ té un reproductor de mòduls integrat que carrega fitxers MOD, XM, IT, S3M, MTM, UMX i MO3 i reconstrueix la cançó en directe a partir dels seus patrons i sons d'instruments, tal com la música tracker està pensada per reproduir-se. Els reproductors normals de l'iPhone no poden fer-ho. Els efectes i l'equalitzador també funcionen amb la música de mòdul.
{{% /details %}}

{{% details title="Admet Flacbox fitxers DSD i d'alta resolució?" closed="true" %}}
Sí. Flacbox reprodueix fitxers DSD (DSF i DFF) a través del motor BASS™ utilitzant DSD sobre PCM perquè funcionin en maquinari de sortida normal, a més de FLAC, WavPack, Monkey's Audio (APE), Musepack i TrueAudio per a reproducció sense pèrdua.
{{% /details %}}

{{% details title="Quins efectes de so té Flacbox?" closed="true" %}}
Un equalitzador de 10 bandes, Normalització de volum, Compressor, Freeverb, Auto Wah, Phaser, Flanger, Echo, Chorus, Distorsió, Rotate i Crossfeed, a més d'una cadena DSP que crees tu mateix amb filtres, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay i stereo width. Cadascun és independent i es pot combinar amb els altres.
{{% /details %}}

{{% details title="Què és un preajust?" closed="true" %}}
Un preajust és una configuració preparada per a un efecte. En lloc de moure els controls lliscants tu mateix, toques un preajust i el so canvia per coincidir-hi. Cada efecte de Flacbox té diversos preajustos, i aquesta guia enumera què fa cadascun. Si mous un control lliscant després de triar un preajust, l'efecte mostra «Manual» per dir-te que ara utilitza els teus propis valors.
{{% /details %}}

{{% details title="Com obro els efectes d'àudio a Flacbox?" closed="true" %}}
Obre el reproductor En reproducció, toca el botó ⋯ (Més accions) i tria Efectes d'àudio. O ves a Configuració > Reproductor d'àudio > Efectes d'àudio. Toca un efecte, activa el seu interruptor i tria un preajust, o obre els controls lliscants per ajustar amb precisió.
{{% /details %}}

{{% details title="On és l'equalitzador i quins són els millors ajustos?" closed="true" %}}
Ves a Configuració > Reproductor d'àudio > Equalitzador d'àudio. Té 10 bandes de 32 Hz a 16 kHz, cadascuna de -12 a +12 dB, més un Preamplificador de -24 a +24 dB i 22 preajustos. Per a més greus, utilitza Bass Booster. Per a veus més clares, utilitza Vocal Booster o Pop. Per a un so més brillant, utilitza Treble Booster. Després ajusta bandes individuals al teu gust.
{{% /details %}}

{{% details title="Com reforço els greus a Flacbox?" closed="true" %}}
Dues maneres fàcils. A l'Equalitzador d'àudio, tria Bass Booster (o puja les bandes de 32 Hz i 64 Hz uns pocs dB). O, a Processament de senyal, afegeix un bloc Low Shelf establert a Bass Boost. En tots dos casos, baixa el Preamplificador o afegeix un bloc Gain d'1 o 2 dB perquè els greus es mantinguin nets i no es distorsionin.
{{% /details %}}

{{% details title="Quin preajust d'equalitzador és millor per a la meva música?" closed="true" %}}
Rock i Electronic afegeixen energia amb greus i aguts forts. Acoustic, Jazz i Classical es mantenen càlids i naturals. Pop i Vocal Booster porten les veus endavant. Bass Booster i Hip-Hop afegeixen pes. Deep i Loudness sonen més plens a volum baix. Comença amb el que coincideixi amb el teu gènere, després ajusta amb precisió.
{{% /details %}}

{{% details title="Què és la Normalització de volum i en què es diferencia de ReplayGain?" closed="true" %}}
Fa que cada pista es reprodueixi a més o menys la mateixa sonoritat. Mesura la sonoritat real utilitzant l'estàndard EBU R128 (en LUFS, com els serveis de streaming) i ajusta cada pista cap al teu objectiu, amb un límit de reforç màxim. A diferència de ReplayGain, no necessita etiquetes als teus fitxers i funciona amb qualsevol font, en directe, sense canviar l'àudio. Preajustos: Light, Standard, Strong i Night.
{{% /details %}}

{{% details title="Què és Crossfeed i l'hauria d'utilitzar?" closed="true" %}}
Crossfeed barreja una mica dels canals esquerre i dret perquè els auriculars se sentin més com altaveus reals i menys com si el so estigués atrapat al teu cap. És només per a auriculars, així que apaga'l per a altaveus. Flacbox utilitza el mètode bs2b (Bauer), amb preajustos com Chu Moy i Jan Meier.
{{% /details %}}

{{% details title="Quina és la diferència entre el Compressor i la Normalització de volum?" closed="true" %}}
La Normalització de volum iguala la sonoritat entre cançons diferents. El Compressor iguala les parts fortes i fluixes dins d'una sola cançó. Resolen problemes diferents i funcionen bé junts, especialment en un cotxe o en un lloc sorollós.
{{% /details %}}

{{% details title="Què és la cadena de Processament de senyal (DSP)?" closed="true" %}}
És un rack que crees tu mateix a Configuració > Reproductor d'àudio > Processament de senyal. Afegeix blocs com filtres, shelves, gain, soft clip, bit crusher, ring modulator, tremolo, delay i stereo width, posa'ls en qualsevol ordre, activa o desactiva cadascun, i dirigeix la cadena a tots els canals, l'esquerre o el dret. Com que l'ordre importa, pots dissenyar exactament el so que vols.
{{% /details %}}

{{% details title="Quina és la diferència entre l'Equalitzador, els efectes i la cadena DSP?" closed="true" %}}
L'Equalitzador és un simple control de to de 10 bandes. Els Efectes d'àudio són eines preparades (compressor, reverberació, echo, etc.) amb preajustos. La cadena DSP és on construeixes el teu propi ordre d'efectes a partir de blocs individuals. Pots executar tots tres alhora.
{{% /details %}}

{{% details title="Els efectes canvien o malmeten els meus fitxers de música?" closed="true" %}}
No. Tot s'aplica en directe mentre sona la música. Els teus fitxers no es canvien ni es tornen a desar mai. Apaga un efecte i el so original torna a l'instant.
{{% /details %}}

{{% details title="Puc utilitzar més d'un efecte alhora?" closed="true" %}}
Sí. Cada efecte té el seu propi interruptor i no hi ha cap interruptor mestre, així que qualsevol combinació funciona. Per exemple, Normalització de volum més Compressor per a una escolta uniforme, o Freeverb més Crossfeed amb auriculars, amb l'equalitzador a sobre.
{{% /details %}}

{{% details title="Per què els controls de l'efecte estan atenuats?" closed="true" %}}
L'efecte està apagat. Activa el seu interruptor a la part superior de l'editor per utilitzar els controls. Cada efecte està apagat de manera predeterminada.
{{% /details %}}

{{% details title="Què significa l'etiqueta Manual?" closed="true" %}}
Significa que has mogut un control lliscant lluny d'un preajust, així que l'efecte ara utilitza els teus propis valors personalitzats en lloc d'un preajust amb nom. Cada control lliscant té un botó de restabliment, i triar un preajust de nou substitueix els teus valors manuals.
{{% /details %}}

{{% details title="Puc desar i compartir els meus preajustos d'equalitzador?" closed="true" %}}
Sí. A més dels 22 preajustos integrats, pots fer-ne de propis, reordenar-los i exportar-los o importar-los per moure els teus ajustos a un altre dispositiu.
{{% /details %}}

{{% details title="Els efectes funcionen amb CarPlay, streaming i reproducció en segon pla?" closed="true" %}}
Sí. Els efectes s'executen dins del motor BASS™, així que s'apliquen a fitxers locals, unitats al núvol, servidors multimèdia, transmissions i música de mòdul, i continuen funcionant durant CarPlay i la reproducció en segon pla.
{{% /details %}}

{{% details title="Puc canviar la qualitat de sortida d'àudio?" closed="true" %}}
Sí. A Configuració > Reproductor d'àudio pots establir la freqüència de mostreig de sortida, el nombre de canals i la mida del buffer per adaptar-se als teus auriculars, altaveus o DAC.
{{% /details %}}

{{% details title="Quina és una bona configuració inicial per a auriculars?" closed="true" %}}
Activa la Normalització de volum (Standard), afegeix un Compressor lleuger (Soft), tria un preajust d'equalitzador que t'agradi, i activa el Crossfeed (Chu Moy o Jan Meier). Deixa la reverberació, l'echo i la distorsió apagats tret que vulguis un so creatiu.
{{% /details %}}

---

*BASS és una marca comercial de Un4seen Developments Ltd. Consulta [un4seen.com](https://www.un4seen.com/). Crossfeed utilitza l'algoritme bs2b (Bauer stereophonic-to-binaural); consulta la [pàgina del projecte bs2b](https://bs2b.sourceforge.net/).*
