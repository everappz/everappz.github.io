---
title: "Editor de Etiquetas"
date: 2020-02-01
description: "Aprende a usar el Editor de Etiquetas de Evertag para actualizar metadatos de música, editar portadas de álbumes, editar por lotes múltiples archivos y gestionar etiquetas de MusicBrainz. Ideal para organizar tu biblioteca musical en iOS y Mac."
keywords: [
  "editor de etiquetas Evertag", "editor de metadatos de audio", "editor de etiquetas de música",
  "editar etiquetas de audio iPhone", "editor de portada de álbum", "edición por lotes de etiquetas de audio",
  "metadatos MusicBrainz", "app organizadora de música", "guía Evertag", "editor de etiquetas ID3"
]
tags: ["guía", "evertag", "editor de etiquetas"]
readingTime: 5
---


El **Editor de Etiquetas** es la pantalla principal de la app Evertag donde puedes ver y editar los metadatos de archivos de audio. Abre esta pantalla tocando un archivo de la sección **Archivos Locales** o de cualquier cuenta de **almacenamiento en la nube** conectada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Tag Editor Screen" image="/docs/guide/evertag/img/tag-editor.webp" >}}
{{< /cards >}}

## Modos de Edición

Evertag proporciona dos modos de edición:

- **Modo de un solo archivo**
  - Navega entre archivos deslizando a la izquierda o a la derecha en el carrusel de portadas.

- **Modo por lotes**
  - Edita múltiples archivos a la vez y aplica metadatos compartidos.
  - Para activar, desplázate hacia abajo y toca **Editar archivos simultáneamente**.

## Modo de Archivo Individual

De forma predeterminada, la app abre el editor de etiquetas en modo de archivo individual con solo las opciones de edición principales habilitadas. En este modo, puedes editar los campos de metadatos más comunes, como:

**Título de la pista, Subtítulo, Artista del álbum, Álbum, Artista, Compositor, Intérprete, Género, Comentario, Pulsos por minuto, Podcast, Recopilación, Número de disco, Número de pista, Total de pistas, Valoración, Año**

Para acceder a todas las etiquetas disponibles, desplázate hasta el final de la pantalla y toca la opción **Mostrar etiquetas extendidas**. Esto cambiará el editor al modo extendido, lo que te permite editar más de **120 campos de metadatos**, incluidas **Etiquetas MusicBrainz**, **Letras**, **Clasificaciones de Contenido**, valores de replay-gain, órdenes de clasificación, metadatos de podcasts y más. Usa **Ajustes → Editor de etiquetas de audio → Botones en la pantalla principal** para activar permanentemente Mostrar etiquetas extendidas para que siempre esté activo.

{{< cards cols="1">}}
{{< card title="" subtitle="Bottom Actions Panel" image="/docs/guide/evertag/img/tag-editor-bottom-actions.webp" >}}
{{< /cards >}}

## Modo por Lotes

Puedes entrar en la edición por lotes de dos maneras:

1. **Desde el Gestor de Archivos**
   - Toca **Más acciones** (•••) en la esquina superior derecha.
   - Toca **Seleccionar**, elige múltiples archivos y luego toca **Editar etiquetas de audio**.

2. **Desde el Editor de Etiquetas**
   - Abre cualquier archivo, desplázate hacia abajo y toca **Editar archivos simultáneamente** para cargar todos los archivos de la misma carpeta.

{{< cards cols="1">}}
{{< card title="" subtitle="Batch Editing Mode" image="/docs/guide/evertag/img/tag-editor-batch-editing.webp" >}}
{{< /cards >}}

Después de editar, toca **Guardar** para aplicar los cambios.

## Editar Letras

El editor extendido expone el campo **Letras**. Tócalo para abrir la lista de letras — cada entrada de letras tiene su propio idioma y descripción, por lo que una sola pista puede almacenar varias traducciones.

No tienes que escribir letras desde cero. El editor incluye accesos directos de búsqueda con un toque a las bases de datos de letras más populares en la web, pre-rellenadas con el artista y título actuales de la pista:

- **Lrclib** — la base de datos pública de referencia para **letras sincronizadas (estilo LRC)**. Úsala cuando quieras letras sincronizadas que se desplacen línea por línea en reproductores que las soporten.
- **Genius** — gran catálogo con anotaciones y letras precisas en texto plano.
- **Lyricsify** — base de datos impulsada por la comunidad con letras simples y con marca de tiempo.
- **Google** — una búsqueda web general como alternativa cuando las bases de datos dedicadas no tienen una coincidencia.

Cada acceso directo solo aparece cuando el servicio correspondiente es accesible desde tu dispositivo. Toca un servicio, copia las letras (o las marcas de tiempo LRC) que deseas, regresa a Evertag y pégalas en el campo de texto — luego **Guardar** para escribir las letras de nuevo en las etiquetas del archivo de audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Pages" image="/docs/guide/evertag/img/tag-editor-lyrics-pages.webp" >}}
{{< /cards >}}

Elige un idioma del selector:

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Language Selector" image="/docs/guide/evertag/img/tag-editor-lyrics-language-select.webp" >}}
{{< /cards >}}

Luego pega o escribe el texto de las letras. Evertag admite tanto texto plano como letras con marca de tiempo (sincronizadas) — el marcador de posición muestra un ejemplo del formato estilo LRC, que es exactamente lo que devuelven Lrclib y Lyricsify para resultados sincronizados.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Text Editor" image="/docs/guide/evertag/img/tag-editor-lyrics-text.webp" >}}
{{< /cards >}}

## Establecer una Valoración y Clasificación de Contenido

El editor extendido ofrece un control de **Valoración** por estrellas junto a un control segmentado de **Clasificación de Contenido**.

### Valoración por Estrellas

Usa el campo **Valoración** para darle a una pista una puntuación personal de uno a cinco estrellas. El valor se escribe en el campo de etiqueta de valoración estándar del archivo (POPM para ID3, `rate` para MP4, `RATING` para Vorbis/APE, etc.), por lo que otras apps que lean esta etiqueta — incluida la app Música, Plex, Roon y la mayoría de los editores de etiquetas de escritorio — recogerán tus puntuaciones de inmediato.

{{< cards cols="1">}}
  {{< card title="" subtitle="Rating" image="/docs/guide/evertag/img/tag-editor-rating.webp" >}}
{{< /cards >}}

### Clasificación de Contenido

La **Clasificación de Contenido** marca el contenido de una pista usando uno de los valores del estándar Parental Advisory que usa la iTunes Store y la mayoría de las plataformas musicales:

- **Sin contenido explícito** — el valor predeterminado para pistas sin información de aviso parental. El archivo se trata como adecuado para todos los oyentes y no mostrará ninguna etiqueta de aviso en reproductores que respeten la etiqueta.
- **Explícito** — la pista contiene lenguaje o contenido explícito. Los reproductores que respetan los controles parentales (la app Música, la app Apple TV, exportaciones de Spotify, Plex, etc.) mostrarán una insignia **E** junto al título y, cuando las restricciones estén habilitadas en el dispositivo o cuenta, pueden ocultar la pista de perfiles infantiles o negarse a reproducirla.
- **Limpio** — una versión censurada o editada de una pista de otro modo explícita. Los reproductores muestran una insignia **C** para que los oyentes puedan distinguir una edición limpia del master explícito original, lo cual es útil cuando ambas versiones existen en la misma biblioteca.

Querrás establecer o corregir este campo cuando:

- Un archivo tiene la etiqueta incorrecta (por ejemplo una edición de radio limpia que fue etiquetada por error como explícita, o viceversa).
- Las pistas fueron grabadas o descargadas sin la etiqueta y ahora se muestran como inofensivas aunque contengan contenido explícito.
- Estás preparando un álbum para su envío o difusión y necesitas que cada pista lleve metadatos consistentes.
- Quieres que CarPlay, la Pantalla de Bloqueo, reproductores estilo Apple Music o software de DJ muestre la insignia correcta **E** / **C** junto al título de la pista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Lyrics Advisory Rating" image="/docs/guide/evertag/img/lyrics-advisory-rating.webp" >}}
{{< /cards >}}

## Editar Portada del Álbum

Para cambiar una portada de álbum:

1. Toca el **icono de Cámara** en el carrusel de portadas.
2. Elige la ubicación de la imagen: Archivos Locales, Nube, Descargas o Biblioteca de Fotos.
3. Selecciona una imagen para aplicar como arte de portada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Image" image="/docs/guide/evertag/img/select-image.webp" >}}
{{< /cards >}}

## Más Acciones en el Editor de Etiquetas

Las opciones de edición adicionales están disponibles a través de la barra de herramientas debajo de la vista de portada.

{{< cards cols="1">}}
  {{< card title="" subtitle="More Actions Menu" image="/docs/guide/evertag/img/tag-editor-more-actions.webp" >}}
{{< /cards >}}

### Búsqueda Automática de Etiquetas de Audio

Esta acción activa el motor de búsqueda inteligente de etiquetas, que encuentra y rellena los metadatos completos para tu archivo de audio basándose en la información existente.
La app usa la base de datos MusicBrainz — una de las bases de datos de etiquetas más completas — con más de **50 millones** de pistas.

### Buscar Portada del Álbum

Usa los metadatos para buscar en la web la portada de álbum correcta.

{{< cards cols="1">}}
  {{< card title="" subtitle="Search Album Cover" image="/docs/guide/evertag/img/search-album-cover.webp" >}}
{{< /cards >}}

Una vez encontrada, guarda la imagen en tus **Fotos** usando el menú contextual del sistema.

{{< cards cols="1">}}
  {{< card title="" subtitle="Add Image to Photos" image="/docs/guide/evertag/img/add-image-to-photos.webp" >}}
{{< /cards >}}

Después de eso, regresa al editor de etiquetas, toca el icono de Cámara, ve a **Biblioteca de Fotos** y selecciona la imagen guardada. La app la establecerá como portada para tu archivo de audio.

Puedes ajustar cómo se escalan las imágenes de portada en la configuración de la app.

### Guardar Arte del Álbum

Esta acción guarda el arte del álbum actual en la carpeta **Documents**, para que puedas reutilizarlo más tarde.

### Normalizar Codificación

Esta acción normalizará la codificación de texto de todas las etiquetas en los metadatos del archivo de audio. Es especialmente útil si estás cambiando desde un PC con Windows, donde los archivos pueden usar codificaciones diferentes que aparecen como caracteres ilegibles o dañados en un Mac.

### Búsqueda Manual de Etiquetas

Busca metadatos de álbum manualmente usando la base de datos MusicBrainz.

- Selecciona el álbum

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Album" image="/docs/guide/evertag/img/select-album-results.webp" >}}
{{< /cards >}}

- Elige la canción correcta

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Song" image="/docs/guide/evertag/img/select-a-song.webp" >}}
{{< /cards >}}

- Elige qué etiquetas aplicar

{{< cards cols="1">}}
  {{< card title="" subtitle="Select Audio Tags" image="/docs/guide/evertag/img/select-audio-tags.webp" >}}
{{< /cards >}}

Toca **Hecho** para aplicar los metadatos seleccionados a tu pista.

### Eliminar Etiquetas de Audio

Borra todos los campos de metadatos de un archivo. Útil cuando empiezas desde cero. Toca **Guardar** para confirmar.

## Ajustes del Editor de Etiquetas

Navega a **Ajustes → Editor de etiquetas de audio** para personalizar el comportamiento.

### Escala de Portada del Álbum

Selecciona cómo deben escalarse las portadas de álbumes al guardarlas en archivos de audio. Puedes deshabilitar el escalado para mantener el tamaño de imagen original, pero ten en cuenta que algunos reproductores pueden no admitir archivos de portada grandes. La opción «tamaño original» es parte de las funciones de personalización Premium.

### Opciones de Guardado de Etiquetas

- **ID3v2.4** — Cuando está habilitado, la app guarda las etiquetas en formato ID3v2.4 cuando es posible. Desactívalo para volver al ID3v2.3 más ampliamente compatible si tus etiquetas de audio no se muestran correctamente en reproductores o dispositivos más antiguos.
- **Etiquetas duplicadas** — Cuando está habilitado, los campos de metadatos comunes se duplican en ambas secciones de etiquetas del archivo. Esto mejora la compatibilidad con reproductores de audio más antiguos, pero en la mayoría de los casos no es necesario.

### Opciones de Actualización de Metadatos de Archivos en la Nube

Puedes controlar cómo la app actualiza los metadatos de los archivos de audio almacenados en servicios en la nube:

- **Mostrar mensaje de confirmación**
  Preguntar antes de aplicar cambios de metadatos a archivos en la nube.

- **Actualizar automáticamente los metadatos del archivo**
  Guardar cambios de metadatos en el archivo en la nube automáticamente después de editar.

- **No actualizar los metadatos del archivo**
  Omitir la actualización de archivos en la nube — los cambios se aplicarán solo localmente.

### Editar Archivos en Línea

Elige qué ocurre con las copias descargadas localmente de archivos en la nube después de editarlos:

- **Eliminar siempre el archivo descargado**
  Eliminar la copia local después de guardar los cambios.

- **No eliminar el archivo descargado**
  Mantener el archivo descargado en tu dispositivo después de editarlo.

### Botones de Pantalla Principal

Personaliza qué acciones aparecen en la pantalla principal del editor de etiquetas (Búsqueda automática de etiquetas, Búsqueda manual de etiquetas, Buscar portada de álbum, Guardar portada de álbum, Normalizar codificación, Eliminar etiquetas de audio). También puedes alternar **Mostrar etiquetas extendidas** y **Editar archivos simultáneamente** para que el editor siempre se abra en tu modo preferido.
