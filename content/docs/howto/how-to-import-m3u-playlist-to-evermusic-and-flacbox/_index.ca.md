---
title: "Com importar una llista de reproducció M3U a Evermusic i Flacbox"
date: 2024-01-31
description: "Apreneu com importar fitxers de llistes de reproducció M3U, M3U8 i CUE des del núvol, l'emmagatzematge local o el dispositiu a Evermusic i Flacbox."
keywords: ["evermusic", "flacbox", "llista de reproducció", "m3u", "m3u8", "cue", "importar", "aplicació de música"]
tags: ["evermusic", "importar", "llistes de reproducció", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Resum:** Evermusic i Flacbox admeten la importació de fitxers de llistes de reproducció M3U, M3U8 i CUE des de l'emmagatzematge al núvol, fitxers locals de l'aplicació o el vostre dispositiu. Aneu a Llistes de reproducció > Més > Importar llista de reproducció, seleccioneu una font, trieu el fitxer i l'aplicació crearà la llista de reproducció automàticament.

M3U, que significa MP3 URL o Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, és un format de fitxer d'ordinador utilitzat per a llistes de reproducció multimèdia. Un dels seus usos principals és crear fitxers de llistes de reproducció d'una sola entrada que apunten a fluxos a Internet. Aquests fitxers ofereixen un accés còmode al contingut en streaming i s'utilitzen habitualment per a descàrregues, correu electrònic i escoltar ràdio per Internet.

Malgrat el seu ús generalitzat, no hi ha cap especificació formal per al format M3U; s'ha convertit en un estàndard de facto. Un fitxer M3U és essencialment un fitxer de text pla que especifica les ubicacions d'un o més fitxers multimèdia. Depenent de la codificació, es desa amb l'extensió "m3u" o "m3u8". Cada entrada del fitxer especifica la ubicació d'un fitxer multimèdia, que pot ser un camí local absolut, un camí local relatiu a la ubicació del fitxer M3U o un URL. Les entrades estan separades per salts de línia, i alguns dispositius requereixen salts de línia representats com CR LF.

A més, els fitxers M3U poden incloure comentaris prefixats pel caràcter "#". En M3U estès, "#" introdueix directives M3U esteses, que poden admetre paràmetres acabats amb dos punts ":".

A les nostres aplicacions Evermusic i Flacbox, hem implementat la funcionalitat d'importació de fitxers M3U, eliminant la necessitat de crear llistes de reproducció manualment. Aquesta guia us acompanyarà en la importació de les vostres llistes de reproducció des de l'emmagatzematge al núvol, fitxers locals o fitxers del vostre dispositiu directament a l'aplicació.

Primer, navegueu a la secció 'Llistes de reproducció'. A continuació, toqueu el botó 'Més' situat a la cantonada superior dreta. Al menú que apareix, seleccioneu l'opció 'Importar llista de reproducció'.

![acció d'importar llista de reproducció](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

A la pantalla següent, trieu la ubicació del fitxer. Les opcions compatibles inclouen:

- Emmagatzematge al núvol connectat;
- Fitxers a l'aplicació;
- Fitxers al vostre dispositiu;

![seleccionar ubicació del fitxer](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Seleccionem l'emmagatzematge al núvol connectat i obrim la carpeta que conté el fitxer de la llista de reproducció. Les extensions de fitxer de llistes de reproducció compatibles inclouen M3U, M3U8 i CUE. Seleccioneu el fitxer de la llista de reproducció i toqueu 'Fet' per confirmar la vostra selecció.

![seleccionar fitxer M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

L'aplicació analitzarà el fitxer de la llista de reproducció i crearà una llista de pistes. A continuació, localitzarà aquests fitxers a l'emmagatzematge i compilarà una llista de reproducció final que s'importarà a la biblioteca de música. És crucial que el vostre fitxer M3U/CUE contingui els camins correctes per als fitxers multimèdia, i els fitxers han d'estar ubicats en aquests camins al vostre emmagatzematge.

![llista de reproducció importada](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

L'aplicació admet tant camins relatius com URL absoluts de fitxers.

Per exemple:

Llista de reproducció amb camins relatius:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Llista de reproducció amb URL absoluts:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Si importeu un fitxer de llista de reproducció ubicat dins de l'aplicació (secció de fitxers locals), no cal cap pas addicional.

No obstant això, si voleu importar una llista de reproducció ubicada al vostre dispositiu mitjançant el selector de fitxers del sistema, hi ha una consideració important a tenir en compte.

A causa de les polítiques de seguretat, l'aplicació només pot accedir al fitxer que seleccioneu amb el selector de fitxers del sistema. No obstant això, el fitxer de la llista de reproducció pot incloure enllaços a altres fitxers multimèdia del vostre dispositiu. Per importar una llista de reproducció del vostre dispositiu, heu de seleccionar una carpeta que contingui tant el fitxer de la llista de reproducció com tots els fitxers multimèdia vinculats. En aquest cas, l'aplicació escanejarà la carpeta seleccionada, trobarà el fitxer de la llista de reproducció, crearà la llista de pistes i l'importarà a la biblioteca de música.

A més, podeu importar diverses llistes de reproducció alhora tocant el botó "Més accions" i seleccionant "Importar llistes de reproducció des d'una carpeta". L'aplicació escanejarà el contingut de la carpeta, trobarà els fitxers de llistes de reproducció compatibles i els importarà a la biblioteca.

## Preguntes freqüents

{{% details title="Quins formats de llistes de reproducció admeten Evermusic i Flacbox?" closed="true" %}}
Ambdues aplicacions admeten els formats de fitxer de llistes de reproducció M3U, M3U8 i CUE. Aquests cobreixen els estàndards de llistes de reproducció més comuns utilitzats pels reproductors de música i el programari multimèdia.
{{% /details %}}

{{% details title="Puc importar llistes de reproducció des de l'emmagatzematge al núvol?" closed="true" %}}
Sí. Podeu importar fitxers de llistes de reproducció des de qualsevol servei d'emmagatzematge al núvol connectat, inclosos Google Drive, Dropbox, OneDrive i servidors WebDAV.
{{% /details %}}

{{% details title="Per què falten algunes pistes després de la importació?" closed="true" %}}
El fitxer de la llista de reproducció ha de contenir camins correctes als vostres fitxers multimèdia, i aquests fitxers han d'existir a les ubicacions especificades al vostre emmagatzematge. Comproveu que els camins dels fitxers al vostre fitxer M3U o CUE coincideixin amb les ubicacions reals dels fitxers.
{{% /details %}}

{{% details title="Puc importar diverses llistes de reproducció alhora?" closed="true" %}}
Sí. Utilitzeu el botó Més accions i seleccioneu "Importar llistes de reproducció des d'una carpeta". L'aplicació escaneja la carpeta per trobar tots els fitxers de llistes de reproducció compatibles i els importa en un sol pas.
{{% /details %}}

{{% details title="Necessito crear les llistes de reproducció manualment?" closed="true" %}}
No. La funció d'importació elimina la creació manual de llistes de reproducció. Simplement apunteu l'aplicació al vostre fitxer M3U, M3U8 o CUE existent i crearà la llista de reproducció automàticament.
{{% /details %}}
