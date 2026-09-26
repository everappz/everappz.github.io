---
title: "Com reproduir música FLAC (sense pèrdua) al meu iPhone"
date: 2024-01-29
lastmod: 2026-09-26
description: "Com reproduir FLAC a l'iPhone i l'iPad el 2026 amb Flacbox, un reproductor d'alta resolució amb més de 120 formats, sortida fins a 384 kHz, suport per a USB DAC, un equalitzador de 10 bandes, el motor d'àudio BASS, efectes en temps real com reverberació i retard, un processador DSP i un visualitzador de música amb 500 preajustos. Transmet des del núvol o el NAS i reprodueix fora de línia."
keywords: ["com reproduir flac a l'iphone", "reproductor flac iphone", "flac", "iphone", "sense pèrdua", "àudio d'alta resolució", "reproductor dsd ios", "usb dac iphone", "384khz", "música", "flacbox", "transmetre", "fora de línia", "equalitzador", "dsp", "visualitzador de música", "motor bass"]
tags: ["música", "núvol", "reproductor", "descarregador", "equalitzador", "sense pèrdua", "alta resolució", "fora de línia", "FLAC", "DSD", "DAC", "transmissió", "visualitzador", "DSP"]
readingTime: 8
---

{{< author-byline >}}


**En resum:** Per reproduir FLAC en un iPhone necessites un reproductor de tercers, perquè l'app Música d'Apple no admet FLAC. Instal·la [Flacbox](/products/flacbox) (és gratuït) i, a continuació, transfereix els teus fitxers mitjançant Wi-Fi Drive o USB, o connecta el teu emmagatzematge al núvol o NAS. La teva biblioteca FLAC es reprodueix amb la màxima qualitat, fins a 384 kHz i 32-bit mitjançant un USB DAC. Flacbox també reprodueix més de 120 formats, incloent-hi FLAC, DSD, ALAC, APE, WAV, OGG i OPUS, i afegeix un equalitzador de 10 bandes, el motor d'àudio professional BASS amb efectes en temps real, un processador DSP i un visualitzador de música a pantalla completa.

[{{< figure src="/docs/howto/how-to-play-flac-music-on-iphone/Flacbox_Icon-App-1024x1024.webp" alt="Flacbox Icon - FLAC music player and downloader" width="160" >}}](/products/flacbox)

## Per què el meu iPhone no reprodueix FLAC de forma nativa?

Apple té el seu propi format sense pèrdua anomenat ALAC (Apple Lossless), i l'app Música està construïda al voltant d'aquest en lloc de FLAC. Des d'iOS 11, l'app Fitxers pot previsualitzar un únic fitxer FLAC, però no té biblioteca musical, ni llistes de reproducció, ni cua, ni equalitzador, ni transmissió al núvol. És un visor de fitxers, no un reproductor de música.

Així que tens dues opcions reals:

1. Reproduir FLAC amb una app de reproductor, de manera que els teus fitxers es mantinguin exactament com són. Aquesta és la que recomanem.
2. Convertir FLAC a ALAC, que és de sense pèrdua a sense pèrdua, i després sincronitzar amb l'app Música.

Si tens una col·lecció FLAC de veritat, la primera opció és millor. Evites una biblioteca duplicada, t'estalvies el temps de conversió i les teves carpetes i qualitat d'alta resolució queden intactes. Flacbox està fet exactament per a això.

## Opció 1: Reproduir FLAC amb Flacbox

Flacbox és un reproductor de música d'alta resolució per a iPhone, iPad i Mac. Converteix el teu emmagatzematge al núvol, NAS o ordinador en la teva pròpia biblioteca musical privada, sense conversió ni subscripció.

### Pas 1. Instal·la Flacbox

Flacbox és una descàrrega gratuïta i funciona en iPhone, iPad i Mac.

{{< app-details product="flacbox" >}}

### Pas 2. Incorpora els teus fitxers FLAC

Tria la manera que et resulti més fàcil:

- **Wi-Fi Drive** — obre Connexions, després Computer, després Connect using Wi-Fi, i arrossega els fitxers des de qualsevol navegador d'escriptori. Consulta la [guia de Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).
- **Emmagatzematge al núvol** — connecta iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive i 20 més, i després transmet directament des del núvol.
- **NAS o ordinador** — connecta't mitjançant SMB, WebDAV, DLNA, FTP, SFTP o NFS (Synology, QNAP, WD My Cloud, Time Capsule o qualsevol recurs compartit Samba). La llista completa és a la [guia de Connexions](/docs/guide/flacbox/flacbox-guide-connections).
- **Unitat flash USB** — connecta una SanDisk iXpand o qualsevol lector extern i reprodueix [directament des de la unitat](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it), sense importar res.
- **Compartició de fitxers d'iTunes o Finder** — mitjançant un cable Lightning o USB-C.

### Pas 3. Prem Reprodueix

Les teves pistes apareixen a la biblioteca amb les etiquetes i les caràtules llegides dels mateixos fitxers, agrupades per Àlbum, Artista, Gènere i Compositor. Cada pista mostra el seu còdec i resolució exactes, per exemple FLAC, 96 kHz, 24-bit.

## Sortida d'alta resolució, USB DAC i multicanal

Flacbox està fet per a la gent que es preocupa per la qualitat del so, no només per la reproducció casual:

- **Freqüència de mostreig** — reprodueix des de 8 kHz fins a 384 kHz, amb sortida multicanal d'1 a 7 canals (fins a 5.1 i ITU BS.775-1).
- **Suport per a USB DAC** — qualsevol cosa per sobre de 48 kHz es reprodueix a la seva resolució real mitjançant un USB DAC. A través de la sortida pròpia de l'iPhone, iOS remostra l'àudio com fa amb totes les apps, així que un DAC és la manera d'obtenir alta resolució amb bit perfecte.
- **Sortida ajustable** — configura la freqüència de mostreig, el nombre de canals i la durada del buffer IO (al voltant de 5 ms per a alta resolució de baixa latència) a Configuració, després Audio Player.
- **To i velocitat** — correcció fina del to, més velocitat de reproducció de 0.02× a 3.00×.

## Reprodueix més de 120 formats, no només FLAC

Al costat de FLAC, Flacbox integra FFmpeg perquè pugui reproduir formats que iOS no pot obrir per si sol. No cal convertir ni netejar prèviament una biblioteca mixta:

- **Sense pèrdua i alta resolució** — FLAC, ALAC, WAV, AIFF, APE, WV (WavPack) i DSD (DSF i DFF, incloent-hi DSD64, DSD128 i DSD256).
- **Amb pèrdua** — MP3, AAC, M4A, OGG, OPUS, WMA, MPC i més.
- **Música tracker i MOD** — fitxers clàssics de chiptune i demoscene MOD, XM, IT, S3M, MTM, UMX i MO3 que la majoria de reproductors no poden obrir.

Això és més de 120 formats en total, que cobreix pràcticament qualsevol cosa en una col·lecció de música moderna.

## Tres motors d'àudio, inclòs el motor BASS

Pots triar el motor de reproducció a Configuració, després Audio Player, després Audio Codec:

- **System Codec + FFmpeg** — màxima compatibilitat i estabilitat.
- **FFmpeg** — força el camí de FFmpeg, que desbloqueja la correcció del to i una freqüència de mostreig de sortida personalitzada.
- **Motor BASS™** — el nucli de reproducció professional afegit a [Flacbox 7.6](/blog/flacbox-7-6-bass-audio-engine-effects-dsp-music-visualizer). Desbloqueja els efectes d'àudio en temps real, el processador DSP, el visualitzador de música, la reproducció tracker i MOD, i el remostreig d'alta qualitat. També afegeix control independent del to (±60 semitones) i control del tempo (0.1× a 4×).

## Equalitzador de 10 bandes, potenciador de greus i preamplificador

Flacbox inclou un equalitzador gràfic de 10 bandes amb preajustos a l'estil iPod com Acoustic, Bass Booster, Rock, Pop, Jazz, Classical i Dance. Hi ha un preamplificador per elevar les pistes fluixes sense retallar, i pots desar els teus propis preajustos. Ajusta'l per a auriculars intraauriculars, un HomePod o un equip de so del cotxe. Per a una explicació completa, consulta la [guia de l'equalitzador](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Equalitzador del reproductor d'àudio de Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Efectes d'àudio en temps real

Quan el motor BASS està activat, obtens onze efectes en temps real que pots apilar i ajustar mentre sona la música. No es torna a codificar res, i desactivar un efecte torna el so original a l'instant:

- **Reverberació** — des d'una habitació petita fins a una catedral.
- **Retard i eco multitap** — des d'un slapback ajustat fins a una cua ambiental llarga.
- **Crossfeed** — barreja els canals estèreo perquè els auriculars sonin més com altaveus reals en mescles amb panoràmica marcada.
- **Compressor** — anivella les parts fortes i fluixes, cosa que és ideal per al cotxe o el gimnàs.
- **Chorus, Flanger, Phaser, Auto-Wah, Distortion i Stereo Rotation** — efectes creatius de modulació i de caràcter.

Flacbox també té anivellament automàtic de volum basat en l'estàndard de sonoritat de qualitat de radiodifusió EBU R128. Els àlbums i les llistes de reproducció aleatòries sonen a un nivell constant, així no has d'ajustar el volum contínuament. Ve amb els preajustos Light, Standard, Strong i Night.

## Crea el teu propi processador DSP

Més enllà dels efectes, Flacbox et dona un processador DSP de 14 filtres en temps real que configures tu mateix. Pots afegir filtres professionals i bandes d'EQ paramètric, saturació i un bit crusher, i processadors creatius com tremolo, ring modulator i stereo width. Tot funciona en directe sobre allò que reprodueixes, des d'un FLAC local fins a una transmissió al núvol, i la configuració DSP fins i tot està disponible a CarPlay.

## Visualitzador de música a pantalla completa

Flacbox té un visualitzador de música integrat que pinta visuals en moviment i acolorits al ritme de la teva música. Utilitza el conegut motor Milkdrop (projectM) amb 500 preajustos, dibuixats amb OpenGL a iPhone, iPad i Mac. Obre'l des del reproductor tocant el botó Més accions i després Visualització. Tria un preajust o utilitza el mode Auto per anar-los canviant cada 30 segons amb una transició suau. Per a ajuda pas a pas, consulta la guia sobre [com activar el visualitzador de música](/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Visualitzador de música de Flacbox (Milkdrop and projectM)" image="/docs/howto/how-to-turn-on-a-music-visualizer-while-playing-music-on-iphone-ipad-mac/music-visualizer-starfield-sectors-preset.webp" >}}
{{< /cards >}}

## Núvol, NAS i reproducció fora de línia

Transmet directament des de més de 30 serveis al núvol, incloent-hi iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, pCloud, Proton Drive i Internxt. També pots connectar servidors autoallotjats com Plex, Jellyfin, Emby, Subsonic i Navidrome, i qualsevol NAS mitjançant SMB, WebDAV, DLNA, FTP, SFTP o NFS.

Quan vulguis la teva música a sobre, el gestor de descàrregues integrat desa llistes de reproducció, artistes, àlbums o carpetes senceres per escoltar-los fora de línia. El mode fora de línia després sincronitza automàticament les pistes noves a mesura que apareixen al núvol. T'estàs quedant sense espai? Esborra la memòria cau amb un sol toc i continua transmetent.

## Tot el que volen els oients seriosos

- **Biblioteca organitzada** — agrupada per Cançons, Àlbums, Artistes de l'àlbum, Artistes, Gèneres i Compositors, amb cerca ràpida que funciona fora de línia.
- **Editor d'etiquetes ID3** — corregeix metadades desordenades i codificacions trencades (ciríl·lic, japonès, xinès) i escriu els canvis de nou al fitxer.
- **Llistes de reproducció** — crea, reordena, importa i exporta M3U, M3U8 i CUE, i posa-les disponibles fora de línia.
- **Apple CarPlay** — una pantalla dedicada al cotxe per a la biblioteca, el núvol, la música local i fora de línia, amb l'equalitzador a bord.
- **AirPlay 2 i Chromecast** — envia contingut a HomePods, Apple TV i altaveus compatibles amb Cast.
- **Eines per a audiollibres** — múltiples marcadors, velocitat ajustable, un temporitzador de repòs i represa des d'on ho vas deixar.
- **Widgets i més** — widgets de la pantalla d'inici i la pantalla de bloqueig, scrobbling de Last.fm, lletres sincronitzades i LRC, i accessibilitat completa amb VoiceOver.

Flacbox és gratuït de descarregar. Premium elimina els límits de la versió gratuïta en comptes al núvol, llistes de reproducció i carpetes fora de línia, i està disponible com a compra única de per vida o com a subscripció mensual o anual, amb Compartició en família.

{{< app-details product="flacbox" >}}

## Opció 2: Convertir FLAC a ALAC per a l'app Música

Si realment vols els teus rips dins de l'app Música d'Apple, els pots convertir. De FLAC a ALAC és de sense pèrdua a sense pèrdua, així que no perds cap qualitat:

1. Al teu ordinador, converteix per lots amb una eina gratuïta com XLD al Mac o foobar2000 a Windows. Totes dues conserven les teves etiquetes.
2. Afegeix els fitxers ALAC a la teva biblioteca de Música o iTunes.
3. Sincronitza a l'iPhone amb el Finder al Mac o l'app Apple Devices a Windows.

Les contrapartides són reals. Ara mantens dues còpies de la teva biblioteca, cada edició de metadades implica una altra sincronització, i la disposició de l'app Música es manté fixa, sense llistes de reproducció basades en regles, ni equalitzador, ni DSP, ni transmissió al núvol o NAS al dispositiu. Per això la majoria de la gent amb col·leccions FLAC serioses tria la primera opció.

## Preguntes freqüents

{{% details title="Pot l'iPhone reproduir fitxers FLAC de forma nativa?" closed="true" %}}
Només de manera limitada. L'app Fitxers pot previsualitzar un únic fitxer FLAC des d'iOS 11, però no hi ha biblioteca, llistes de reproducció, cua, equalitzador ni transmissió al núvol. Per escoltar de veritat, fes servir una app de reproductor com Flacbox.
{{% /details %}}

{{% details title="Puc reproduir FLAC de 24-bit o 96kHz (o superior) a l'iPhone?" closed="true" %}}
Sí. Flacbox admet sortida d'alta resolució fins a 384 kHz. Per reproduir per sobre de 48 kHz a la resolució real, connecta un USB DAC extern, perquè la sortida integrada de l'iPhone remostra l'àudio per a totes les apps.
{{% /details %}}

{{% details title="Flacbox converteix FLAC a un altre format?" closed="true" %}}
No. Flacbox reprodueix FLAC en la seva qualitat original sense pèrdua i sense conversió. Els efectes i el DSP s'apliquen en directe només durant la reproducció, i mai no canvien els teus fitxers.
{{% /details %}}

{{% details title="Perdo qualitat en convertir FLAC a ALAC?" closed="true" %}}
No. FLAC i ALAC són tots dos sense pèrdua, així que la conversió és bit perfecte. Només hi inverteixes temps i renuncies a comoditat, ja que acabes amb dues biblioteques per mantenir i has de tornar a sincronitzar després de les edicions.
{{% /details %}}

{{% details title="Quins formats d'àudio admet Flacbox?" closed="true" %}}
Més de 120 formats, incloent-hi FLAC, DSD (DSF i DFF), ALAC, APE, WAV, AIFF, WV, OGG, OPUS, MP3, AAC, M4A, WMA, i fins i tot música tracker i MOD com MOD, XM, IT i S3M.
{{% /details %}}

{{% details title="Té Flacbox un equalitzador, efectes i un visualitzador?" closed="true" %}}
Sí. Té un equalitzador de 10 bandes amb preajustos i un preamplificador. També té un motor professional BASS amb onze efectes en temps real (reverberació, retard, eco multitap, crossfeed, compressor, chorus, flanger, phaser, auto-wah, distortion i stereo rotation), més anivellament de volum EBU R128, un processador DSP de 14 filtres i un visualitzador Milkdrop a pantalla completa amb 500 preajustos.
{{% /details %}}

{{% details title="Puc transmetre FLAC des del meu NAS o núvol?" closed="true" %}}
Sí. Flacbox es connecta a més de 30 serveis al núvol i a un NAS o ordinador mitjançant SMB, WebDAV, DLNA, FTP, SFTP i NFS. Tota la teva biblioteca està disponible sense copiar fitxers a l'iPhone, i pots descarregar pistes per a reproducció fora de línia en qualsevol moment.
{{% /details %}}

{{% details title="Flacbox és realment gratuït?" closed="true" %}}
Flacbox és gratuït de descarregar, amb funcions bàsiques com l'equalitzador, la transmissió al núvol i la reproducció fora de línia. Premium elimina els límits de la versió gratuïta en comptes al núvol, llistes de reproducció i carpetes fora de línia, i ve com a compra única de per vida o com a subscripció mensual o anual, amb Compartició en família.
{{% /details %}}
