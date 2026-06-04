---
title: "Editor d'etiquetes"
date: 2020-02-01
description: "Aprèn a utilitzar l'Editor d'etiquetes d'Evertag per actualitzar metadades musicals, editar portades, editar per lots múltiples fitxers i gestionar etiquetes de MusicBrainz. Ideal per organitzar la teva biblioteca musical a iOS i Mac."
keywords: [
  "editor d'etiquetes Evertag", "editor de metadades d'àudio", "editor d'etiquetes musicals",
  "editar etiquetes d'àudio iPhone", "editor de portades", "edició per lots d'etiquetes d'àudio",
  "metadades MusicBrainz", "aplicació organitzadora de música", "guia Evertag", "editor d'etiquetes ID3"
]
tags: ["guia", "evertag", "editor d'etiquetes"]
readingTime: 5
---


L'**Editor d'etiquetes** és la pantalla principal de l'aplicació Evertag on pots visualitzar i editar les metadades dels fitxers d'àudio. Obre aquesta pantalla tocant un fitxer de la secció **Fitxers locals** o des de qualsevol compte d'**emmagatzematge al núvol** connectat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de l'Editor d'etiquetes d'Evertag" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Modes d'edició

Evertag proporciona dos modes d'edició:

- **Mode de fitxer únic**  
  - Navega entre fitxers lliscant a l'esquerra o la dreta al carrusel de portades.  

- **Mode per lots**  
  - Edita múltiples fitxers alhora i aplica metadades compartides.  
  - Per activar-lo, desplaça't fins al final i toca **Edita diversos fitxers simultàniament**.

## Mode de fitxer únic

De manera predeterminada, l'aplicació obre l'editor d'etiquetes en mode de fitxer únic amb només les opcions d'edició principals activades. En aquest mode, pots editar els camps de metadades més comuns, com ara:

**Títol de la pista, Subtítol, Artista de l'àlbum, Àlbum, Artista, Compositor, Intèrpret, Gènere, Comentari, Pulsacions per minut, Podcast, Recopilació, Número de disc, Número de pista, Total de pistes, Valoració, Any**

Per accedir a totes les etiquetes disponibles, desplaça't fins al final de la pantalla i toca l'opció **Mostra etiquetes ampliades**. Això canviarà l'editor al mode ampliat, permetent-te editar més de **120 camps de metadades**, incloent **Etiquetes MusicBrainz**, **Lletres**, **Valoracions de contingut**, valors de replay-gain, ordres de classificació, metadades de podcasts i molt més. Utilitza **Configuració → Editor d'etiquetes d'àudio → Botons a la pantalla principal** per activar permanentment Mostra etiquetes ampliades perquè sempre estigui actiu.

{{< cards cols="1">}}
{{< card title="" subtitle="Panell d'accions inferior" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Mode per lots

Pots entrar a l'edició per lots de dues maneres:

1. **Des del Gestor de fitxers**  
   - Toca **Més accions** (•••) a la cantonada superior dreta.  
   - Toca **Seleccionar**, tria múltiples fitxers i després toca **Editar etiquetes d'àudio**.

2. **Des de l'Editor d'etiquetes**  
   - Obre qualsevol fitxer, desplaça't fins al final i toca **Edita fitxers simultàniament** per carregar tots els fitxers de la mateixa carpeta.

{{< cards cols="1">}}
{{< card title="" subtitle="Mode d'edició per lots" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Després d'editar, toca **Desar** per aplicar els canvis.

## Editar lletres

L'editor ampliat exposa el camp **Lletres**. Toca'l per obrir la llista de lletres — cada entrada de lletres té el seu propi idioma i descripció, de manera que una sola pista pot emmagatzemar diverses traduccions.

No cal que escriguis les lletres des de zero. L'editor inclou dreceres de cerca d'un toc a les bases de dades de lletres més populars del web, omplerts prèviament amb l'artista i el títol de la pista actual:

- **Lrclib** — la base de dades pública de referència per a **lletres temporitzades (estil LRC)**. Utilitza-la quan vulguis lletres sincronitzades que avancin línia per línia en reproductors que les suportin.
- **Genius** — gran catàleg amb anotacions i lletres en text pla precises.
- **Lyricsify** — base de dades comunitària amb lletres en text pla i temporitzades.
- **Google** — una cerca web general com a alternativa quan les bases de dades especialitzades no troben coincidències.

Cada drecera només apareix quan el servei corresponent és accessible des del teu dispositiu. Toca un servei, copia les lletres (o les marques de temps LRC) que vols, torna a Evertag i enganxa-les al camp de text — després **Desar** per escriure les lletres de tornada a les etiquetes del fitxer d'àudio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pàgines de lletres" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Tria un idioma del selector:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selector d'idioma de lletres" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Després enganxa o escriu el text de les lletres. Evertag és compatible tant amb el text pla com amb les lletres temporitzades (sincronitzades) — el marcador de posició mostra un exemple del format LRC, que és exactament el que retornen Lrclib i Lyricsify per als resultats sincronitzats.

{{< cards cols="1">}}
  {{< card title="" subtitle="Editor de text de lletres" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Establir una valoració i una valoració de contingut

L'editor ampliat ofereix un control de **Valoració** per estrelles al costat d'un control segmentat de **Valoració de contingut**.

### Valoració per estrelles

Utilitza el camp **Valoració** per donar a una pista una puntuació personal d'una a cinc estrelles. El valor s'escriu a l'etiqueta de valoració estàndard del fitxer (POPM per a ID3, `rate` per a MP4, `RATING` per a Vorbis/APE, etc.), de manera que altres aplicacions que llegeixen aquesta etiqueta — incloent l'aplicació Music, Plex, Roon i la majoria dels editors d'etiquetes d'escriptori — recolliran les teves puntuacions immediatament.

{{< cards cols="1">}}
  {{< card title="" subtitle="Valoració" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Valoració de contingut

La **Valoració de contingut** marca el contingut d'una pista utilitzant un dels valors de l'estàndard Parental Advisory que utilitzen l'iTunes Store i la majoria de plataformes musicals:

- **No ofensiu** — el valor predeterminat per a pistes sense informació de control parental. El fitxer es tracta com a adequat per a tots els oients i no mostrarà cap etiqueta de contingut als reproductors que respectin l'etiqueta.
- **Explícit** — la pista conté llenguatge o contingut explícit. Els reproductors que respectin els controls parentals (l'aplicació Music, l'aplicació Apple TV, exportacions de Spotify, Plex, etc.) mostraran una insígnia **E** al costat del títol i, quan les restriccions estiguin activades al dispositiu o compte, podrien amagar la pista dels perfils infantils o refusar-ne la reproducció.
- **Net** — una versió censurada o editada d'una pista que d'altra manera seria explícita. Els reproductors mostren una insígnia **C** perquè els oients puguin distingir una edició neta de l'original explícit, útil quan ambdues versions conviuen a la mateixa biblioteca.

Voldràs establir o corregir aquest camp quan:

- Un fitxer té l'etiqueta incorrecta (per exemple, una edició de ràdio neta erròniament etiquetada com a Explícita, o a l'inrevés).
- Les pistes es van rippear o descarregar sense l'etiqueta i ara es mostren com a No ofensives tot i contenir contingut explícit — necessari perquè els controls parentals i les biblioteques compartides familiars funcionin correctament.
- Estàs preparant un àlbum per a la seva presentació o distribució i necessites que cada pista tingui metadades coherents.
- Vols que CarPlay, la pantalla de bloqueig, reproductors d'estil Apple Music o programari de DJ mostrin la insígnia **E** / **C** correcta al costat del títol de la pista.

El valor s'emmagatzema al camp de valoració de contingut estàndard per al format de fitxer (`rtng` per a MP4, `TXXX:ITUNESADVISORY` per a ID3, `ITUNESADVISORY` per a Vorbis), de manera que qualsevol reproductor que llegeixi metadades de control parental veurà la teva actualització.

{{< cards cols="1">}}
  {{< card title="" subtitle="Valoració de contingut de lletres" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Editar la portada

Per canviar una portada:

1. Toca la **icona de càmera** al carrusel de portades.  
2. Tria la ubicació de la imatge: Fitxers locals, Núvol, Descàrregues o Biblioteca de Fotos.  
3. Selecciona una imatge per aplicar-la com a portada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleccionar imatge" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Més Accions a l'Editor d'etiquetes

Les opcions d'edició addicionals estan disponibles a través de la barra d'eines sota la vista de portada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de Més Accions" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Cerca automàtica d'etiquetes d'àudio

Aquesta acció activa el motor de cerca d'etiquetes intel·ligent, que troba i omple les metadades completes del teu fitxer d'àudio en funció de la informació existent.  
L'aplicació utilitza la base de dades MusicBrainz — una de les bases de dades d'etiquetes més completes — amb més de **50 milions** de pistes.

### Cerca portada

Utilitza les metadades per cercar al web les portades correctes.  

{{< cards cols="1">}}
  {{< card title="" subtitle="Cerca portada" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Un cop trobades, desa la imatge a les teves **Fotos** utilitzant el menú contextual del sistema.

{{< cards cols="1">}}
  {{< card title="" subtitle="Afegir imatge a Fotos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Després d'això, torna a l'editor d'etiquetes, toca la icona de càmera, ves a **Biblioteca de Fotos** i selecciona la imatge desada. L'aplicació la configurarà com a portada del teu fitxer d'àudio.

Pots ajustar com s'escalen les imatges de portada a la configuració de l'aplicació.

### Desa la portada

Aquesta acció desa la portada actual a la carpeta **Documents**, perquè puguis reutilitzar-la més tard.

### Normalitza la codificació

Aquesta acció normalitzarà la codificació de text de totes les etiquetes a les metadades del fitxer d'àudio. És especialment útil si estàs canviant des d'un PC amb Windows, on els fitxers poden utilitzar codificacions diferents que apareixen com a caràcters il·legibles o deformats en un Mac.

### Cerca manual d'etiquetes

Cerca manualment les metadades de l'àlbum utilitzant la base de dades MusicBrainz.  

- Selecciona l'àlbum  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleccionar àlbum" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Tria la cançó correcta  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleccionar cançó" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Tria quines etiquetes aplicar  

{{< cards cols="1">}}
  {{< card title="" subtitle="Seleccionar etiquetes d'àudio" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Toca **Fet** per aplicar les metadades seleccionades a la teva pista.

### Eliminar etiquetes d'àudio

Esborra tots els camps de metadades d'un fitxer. Útil quan es comença des de zero. Toca **Desar** per confirmar.

## Configuració de l'Editor d'etiquetes

Navega fins a **Configuració → Editor d'etiquetes d'àudio** per personalitzar el comportament.

### Escalat de la portada

Selecciona com s'han d'escalar les portades quan es desen als fitxers d'àudio. Pots desactivar l'escalat per mantenir la mida original de la imatge, però tingues en compte que alguns reproductors poden no ser compatibles amb fitxers de portades grans. L'opció "mida original" és part de les funcions de personalització Premium.

### Opcions de desat d'etiquetes

- **ID3v2.4** — quan s'activa, l'aplicació desa les etiquetes en format ID3v2.4 quan sigui possible. Desactiva per tornar a l'ID3v2.3 amb un suport més ampli si les teves etiquetes d'àudio no es mostren correctament en reproductors o dispositius antics.
- **Etiquetes duplicades** — quan s'activa, els camps de metadades comuns es dupliquen a les dues seccions d'etiquetes del fitxer. Això millora la compatibilitat amb reproductors d'àudio antics, però en la majoria dels casos no és necessari.

### Opcions d'actualització de metadades de fitxers al núvol

Pots controlar com l'aplicació actualitza les metadades dels fitxers d'àudio emmagatzemats als serveis al núvol:

- **Mostra el missatge de confirmació**  
  Pregunta abans d'aplicar canvis de metadades als fitxers al núvol.

- **Actualitza automàticament les metadades del fitxer**  
  Desa els canvis de metadades al fitxer al núvol automàticament després de l'edició.

- **No actualitzis les metadades del fitxer**  
  Salta l'actualització dels fitxers al núvol — els canvis s'aplicaran només localment.

### Editar fitxers en línia

Tria què passa amb les còpies locals descarregades dels fitxers al núvol després de l'edició:

- **Elimina sempre el fitxer descarregat**  
  Elimina la còpia local després de desar els canvis.

- **No elimineu el fitxer descarregat**  
  Mantén el fitxer descarregat al teu dispositiu després de l'edició.

### Botons de la pantalla principal

Personalitza quines accions apareixen a la pantalla principal de l'editor d'etiquetes (Cerca automàtica d'etiquetes d'àudio, Cerca manual d'etiquetes d'àudio, Cerca portada, Desa portada, Normalitza codificació, Elimina etiquetes d'àudio). També pots activar **Mostra etiquetes ampliades** i **Edita fitxers simultàniament** perquè l'editor sempre s'obri en el teu mode preferit.
