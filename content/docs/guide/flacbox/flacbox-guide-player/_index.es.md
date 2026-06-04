---
title: "Reproductor de Audio"
date: 2020-02-01
description: "Aprende a usar el reproductor de audio de Flacbox en iPhone, iPad y Mac. Controla la reproducción, gestiona colas, configura el motor de audio FFmpeg / sistema, cambia la frecuencia de muestreo, corrección de tono, duración del búfer IO, ecualizador, marcadores de audio, AirPlay 2, Google Cast, CarPlay, widgets y atajos de teclado de Mac."
keywords: [
  "guía reproductor Flacbox", "configuración reproductor de audio", "ecualizador Flacbox",
  "streaming música AirPlay", "música Google Cast", "marcadores de audio",
  "cola de reproducción Flacbox", "repetir aleatorio Flacbox", "control de volumen Flacbox",
  "mini reproductor macOS", "app de música voiceover",
  "FFmpeg Flacbox", "corrección de tono Flacbox", "frecuencia de muestreo Flacbox",
  "DAC externo Flacbox", "sonido surround Flacbox", "búfer IO Flacbox",
  "velocidad de reproducción Flacbox", "temporizador de sueño Flacbox"
]
tags: ["guía", "flacbox", "reproductor"]
readingTime: 14
---


El Reproductor de Audio es la pantalla principal de la app donde controlas la música y la mayoría de las funciones de reproducción. También es donde el motor de audio de alta resolución de Flacbox — construido sobre los códecs del sistema más la biblioteca **FFmpeg** incluida — hace el trabajo pesado. Exploremos cómo usarlo.

## Acceso al Reproductor de Audio

Puedes llegar al reproductor de pantalla completa desde la barra del mini reproductor. En iPhone, el mini reproductor está en la parte inferior de la pantalla principal. En iPad y Mac, está en el lado izquierdo. Para ocultar el mini reproductor en iPhone, tócalo una vez y desliza hacia abajo. Para cerrar completamente el reproductor de pantalla completa, toca el botón de cerrar en la esquina inferior derecha.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla Principal del Reproductor de Audio de Flacbox" image="/docs/guide/flacbox/img/audio-player-main-screen.webp" >}}
{{< /cards >}}

## Formatos de Audio Compatibles

Flacbox reproduce los formatos de audio más populares — tanto los códecs del sistema de Apple como muchos formatos adicionales gestionados por el motor FFmpeg incluido:

3g2, 3gp, 3gp2, 3gpp, 8svx, aa, aac, aax, ac3, act, adt, adts, aif, aifc, aiff, alac, amr, amv, ape, asf, au, avi, awb, caf, cavs, cdda, cue, dct, dff, drc, dsf, dss, dvf, dvr-ms, ec3, f4a, f4b, f4p, f4v, flac, flv, gif, gifv, gsm, gxf, h261, h263, h264, ifv, iklax, ivf, ivs, l16, latm, loas, m2t, m2ts, m2v, m3u, m3u8, m4a, m4b, m4p, m4r, m4v, mka, mkv, mmf, mng, mod, mogg, mov, mp1, mp2, mp3, mp4, mp4v, mpa, mpc, mpe, mpeg, mpg, mpv, msv, mts, mxf, nsf, nsv, nut, oga, ogg, ogv, opus, pcm, pls, qt, ra, raw, rm, rmvb, roq, rv, sln, snd, svi, tod, tta, vob, voc, vox, vtt, w64, wav, wave, webm, wma, wmv, wv, xhe, xmv, y4m, yuv.

Eso cubre prácticamente todos los formatos modernos con y sin pérdida que puedas tener en una colección de música personal.

## Controles de Reproducción

En la parte inferior de la pantalla del reproductor, verás botones para Reproducir, Pausar, Pista Siguiente y Pista Anterior. También hay botones opcionales como Siguientes 30 seg y Anteriores 30 seg que puedes activar en los ajustes de la app (muy útiles para audiolibros). Puedes avanzar o retroceder manteniendo pulsados los botones Siguiente / Anterior. Para saltar a una parte específica de una pista, arrastra el deslizador de reproducción.

## Repetir y Aleatorio

Toca el botón de repetir para recorrer los modos de repetición:

- **Repetir Todo** — repite en bucle todas las pistas de tu cola.
- **Repetir Una** — repite solo la pista actual.
- **Repetir Stop** — pausa cuando termina la pista actual.
- **Sin Repetición** — reproduce la cola una sola vez sin repetir.

Usa el botón **Aleatorio** para aleatorizar el orden de las pistas en la cola.

## Control de Volumen

Abre la pantalla de Ajustes de Audio tocando el icono de sonido bajo los controles de reproducción para acceder al deslizador de volumen. También encontrarás aquí botones para **Google Cast** y **AirPlay** para cambiar rápidamente la reproducción a otro dispositivo.

## Google Cast (Chromecast)

Para los usuarios de Google Cast, el icono de **Cast** aparece en la parte inferior del reproductor. Tócalo para elegir un dispositivo y comenzar a transmitir. Asegúrate de que tu dispositivo y el receptor Google Cast estén en la misma red Wi-Fi. Nota: no todos los formatos de audio son compatibles con Google Cast — algunos formatos de alta resolución pueden necesitar transcodificación.

## AirPlay

Para AirPlay, busca el botón **AirPlay** en la parte inferior del reproductor. Tócalo y selecciona un dispositivo para transmitir. Flacbox admite **AirPlay 2**, por lo que puedes reproducir en varios HomePods, Apple TVs o altavoces compatibles con AirPlay 2 al mismo tiempo.

## Ecualizador de Audio

Flacbox incluye un **ecualizador de 10 bandas** con preajustes estilo iPod. Toca Ecualizador en la vista de volumen, luego actívalo en la esquina superior derecha. Puedes usar preajustes como Acústico y Realzador de Graves, o ajustar cada banda de frecuencia con deslizadores. Crea tus propios preajustes, guárdalos bajo cualquier nombre y aumenta el volumen general con el preamplificador. Tenemos instrucciones más detalladas sobre cómo usar el ecualizador [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecualizador del Reproductor de Audio de Flacbox" image="/docs/guide/flacbox/img/audio-player-equalizer.webp" >}}
{{< /cards >}}

## Barra de Herramientas del Modo Reproductor

Para algunos estilos de reproductor, hay una barra de herramientas dedicada en la parte superior del reproductor de pantalla completa. Esta barra de herramientas tiene tres botones útiles:

- **Buscar** — localiza rápidamente una pista específica en tu cola del reproductor.
- **Control de Velocidad de Reproducción** — ajusta la velocidad de reproducción desde 0,02× hasta 3,00×. Perfecto para audiolibros, pódcasts y conferencias. Toca Normal para volver a la velocidad predeterminada.
- **Marcadores de Audio** — crea múltiples marcadores por pista. Tenemos instrucciones completas sobre cómo usar marcadores [aquí](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

## Cola del Reproductor

Para ver tu cola del reproductor, toca el botón de cola en el lado derecho de la canción actual. Cada canción en la cola tiene más acciones — toca los tres puntos para verlas. Para reordenar una canción en la cola, usa el indicador de reordenamiento cerca del título y arrástralo a una nueva posición.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cola de Reproducción de Flacbox" image="/docs/guide/flacbox/img/playback_queue.webp" >}}
{{< /cards >}}

## Comentarios / Letras

Para ver los comentarios de una pista y las letras integradas, así como los archivos LRC, sigue estos pasos:

1. Abre **Ajustes**.
2. Ve a **Reproductor de Audio**.
3. Selecciona **Personalización**.
4. Toca **Botones en la pantalla principal**.
5. Activa **Comentarios**.

Después de esto, toca el botón de cola del reproductor en la parte inferior de la pantalla varias veces para cambiar de la vista de portada / cola a la vista de comentarios. En la pantalla de Comentarios, desplázate hacia la derecha para cambiar entre **Comentarios**, **Letras Integradas** y el **Archivo LRC**. Las instrucciones completas están disponibles [aquí](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Letras y Comentarios de Flacbox" image="/docs/guide/flacbox/img/lyrics-screen.webp" >}}
{{< /cards >}}

## Menú de Opciones

Cada canción en la cola del reproductor de audio tiene un menú con más acciones, al que se accede tocando el botón de tres puntos cerca del título de la canción.

- **Reproducir a Continuación** — añade la canción al inicio de la cola del reproductor.
- **Añadir a Lista de Reproducción** — incluye la canción en una lista de reproducción, con la opción de crear una nueva.
- **Añadir a Favoritos** — marca la canción como favorita para acceso rápido.
- **Descargar** — guarda la canción en los archivos locales, apareciendo en la pestaña **Archivos Locales** y en la sección **Música sin conexión**.
- **Editar Etiquetas de Audio** — abre el editor de etiquetas de audio integrado para corregir metadatos faltantes, modificando la canción en tu almacenamiento.
- **Mostrar en Carpeta** — revela la carpeta donde está almacenado el archivo de audio.
- **Mostrar en Finder** — para archivos importados desde tu Mac, revela la carpeta donde está ubicado el archivo de audio en tu Mac.
- **Abrir en** — exporta el archivo de audio a otra app.
- **Eliminar de la Cola** — elimina la canción seleccionada de la cola del reproductor de audio.
- **Eliminar del Servicio en la Nube** — elimina la canción tanto de la biblioteca de música como del almacenamiento en la nube. **Esta acción es irreversible.**
- **Eliminar de Archivos Locales** — elimina la canción tanto de la biblioteca de música como del almacenamiento local. **Esta acción es irreversible.**
- **Eliminar de la Biblioteca Musical** — elimina la canción de tu biblioteca de música, manteniendo el archivo en el almacenamiento.

Las mismas opciones están disponibles para el elemento que se está reproduciendo actualmente en la cola del reproductor de audio, al que puedes acceder tocando el icono **Más Acciones** cerca del título de la pista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opciones de Flacbox para un Elemento en la Cola de Reproducción" image="/docs/guide/flacbox/img/options-for-item-in-playback-queue.webp" >}}
{{< /cards >}}

## Acciones Adicionales del Reproductor

Toca el botón **Más Acciones** "..." en el lado izquierdo del título de la canción que se está reproduciendo actualmente para ver acciones adicionales.

- **Continuar Reproducción** — reanuda desde donde lo dejaste, incluyendo la cola y la posición en el medio. Especialmente útil para audiolibros. Se activa en los ajustes de la app.
- **Buscar** — encuentra rápidamente una pista específica en tu cola del reproductor de audio.
- **Marcadores** — ve tu lista de marcadores de audio creados.
- **Comentarios** — ve los comentarios de la pista y las letras integradas, así como los archivos LRC. Instrucciones completas [aquí](/docs/howto/how-to-add-and-view-comments-to-your-audio-tracks-on-iphone-ipad-and-mac-with-evermusic-and-flacbox).
- **Velocidad** — ajusta la velocidad de reproducción a tu gusto.
- **Recientes** — accede a una lista de canciones reproducidas recientemente.
- **Favoritos** — ve tu colección de canciones favoritas.
- **Ecualizador de Audio** — activa el ecualizador de audio.
- **Temporizador de Sueño** — establece un temporizador para detener la reproducción después de un intervalo especificado. Ideal para cuando quieres dormirte con tu música.
- **Guardar Cola como Lista de Reproducción** — guarda la cola actual del reproductor de audio como una nueva lista de reproducción.
- **Eliminar Cola** — borra tu cola del reproductor y detiene la reproducción.
- **Ajustes** — accede a los ajustes del reproductor de audio.
- **Ayuda** — encuentra asistencia y orientación.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Más Acciones del Reproductor de Audio de Flacbox" image="/docs/guide/flacbox/img/audio-player-more-actions-screen.webp" >}}
{{< /cards >}}

## Marcadores de Audio

Esta función te permite crear múltiples marcadores para pistas en tu biblioteca de música — perfecto para audiolibros, conferencias, largas mezclas de DJ o para marcar el estribillo de una pista favorita.

Para crear un nuevo marcador:

- Comienza a reproducir la canción deseada.
- Abre la pantalla del reproductor.
- Toca el botón **Marcadores** en la barra de herramientas del modo reproductor.
- Selecciona **Añadir Marcador**.
- Elige el tiempo del marcador y toca **Hecho** en la esquina superior derecha.

Editar marcadores para la pista actual es fácil: toca Editar en la esquina superior derecha para entrar en modo de edición. En este modo, puedes reorganizar marcadores, eliminarlos, ajustar el tiempo del marcador y cambiar los títulos de los marcadores. Instrucciones más detalladas sobre marcadores de audio están disponibles [aquí](/docs/howto/how-to-listen-to-audiobooks-on-iphone-ipad-mac-using-evermusic).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Marcadores de Audio de Flacbox" image="/docs/guide/flacbox/img/audio-bookmarks.webp" >}}
{{< /cards >}}

## Recientes y Favoritos

En la pantalla del reproductor, toca los tres puntos para acceder a Recientes y Favoritos. En ambas secciones, puedes buscar canciones, reproducir todas, aleatorizar todas, exportar la lista y borrar la lista. Tenemos instrucciones detalladas sobre cómo exportar listas de canciones [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

## Apple CarPlay (iPhone)

Conecta tu iPhone a tu coche mediante USB o Apple CarPlay inalámbrico y Flacbox aparece en tu pantalla de inicio de CarPlay, listo para reproducir música de forma segura mientras conduces. La interfaz de CarPlay incluye pestañas dedicadas para Biblioteca, Conexiones, Archivos Locales y Ajustes, con controles de reproducción, aleatorio, repetición, gestión de cola y el ecualizador de audio todo disponible sin coger el teléfono. Configura la experiencia CarPlay en Ajustes → CarPlay — opciones de ordenación, paginación, color degradado de los iconos del menú, si se cargan imágenes y una opción para pausar la reproducción automáticamente cuando se conecta CarPlay.

[Lee la guía completa de CarPlay](/docs/howto/how-to-play-your-own-music-on-iphone-using-carplay/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox en Apple CarPlay" image="/docs/guide/flacbox/img/carplay-main.webp" >}}
{{< /cards >}}

## Widgets de Pantalla de Inicio (iPhone y iPad)

Flacbox admite widgets de Pantalla de Inicio y Pantalla de Bloqueo de iOS para que puedas ver y controlar la reproducción de un vistazo. Asegúrate de que los Widgets estén activados en Ajustes → Widgets → Activar Widgets, luego mantén pulsada tu Pantalla de Inicio o Pantalla de Bloqueo, toca **+**, busca **Flacbox** y añade un widget. El widget se actualiza durante la reproducción para mostrar la portada, el título y el artista de la pista que suena.

## Ventana del Mini Reproductor (Exclusivo de Mac)

Los usuarios de Mac pueden usar un mini reproductor compacto siempre en primer plano. Mueve el cursor al borde inferior derecho de la ventana Flacbox, redúcela al mínimo y toca el botón de colapsar. Mantenlo sobre cualquier otra ventana seleccionando Ventana → Mostrar Ventana Siempre en Primer Plano en la barra de menús — perfecto para mantener los controles de música visibles mientras trabajas en otra app.

## Atajos de Teclado (Exclusivo de Mac)

Para los usuarios de Mac, hay un menú de reproducción del sistema disponible en la barra de estado con atajos de teclado. Por ejemplo, pulsa la barra espaciadora para Reproducir / Pausar. También están disponibles atajos para Detener, Siguiente Canción, Canción Anterior, Saltar Tiempo, Repetir, Aleatorio y Velocidad de Reproducción.

## Ajustes del Reproductor de Audio

Para acceder a los ajustes, toca el botón Más en la pantalla del reproductor y elige Ajustes. Aquí encontrarás varias secciones, que se enumeran a continuación.

### General

Estos ajustes cubren los aspectos fundamentales del reproductor de audio, incluyendo la cola de reproducción, la salida de audio y el guardado del estado del reproductor.

- **Modo de Repetición** — elige cómo se comporta el reproductor de audio cuando termina una pista:
  - **Repetir Todo** — reproduce en bucle todas las pistas de tu cola.
  - **Repetir Una** — repite solo la pista actual.
  - **Repetir Stop** — pausa la reproducción cuando termina la pista actual.
  - **Sin Repetición** — permite que tu cola se reproduzca sin repetir.
- **Modo Aleatorio** — aleatoriza el orden de las pistas en tu cola. Puedes activarlo (**Aleatorio activado**) o desactivarlo (**Aleatorio desactivado**).
- **Códec de Audio** — elige el motor de audio utilizado para la reproducción:
  - **Códec del Sistema + FFmpeg** — prioriza el códec de audio del sistema donde sea posible, mejorando la compatibilidad y estabilidad. La corrección de tono y los ajustes de frecuencia de muestreo de salida de audio pueden estar limitados en este modo.
  - **FFmpeg** — fuerza el códec FFmpeg para todos los archivos de audio, permitiéndote ajustar la corrección de tono y la frecuencia de muestreo de salida de audio.
- **Frecuencia de Muestreo de Salida de Audio** — ajusta la frecuencia de muestreo de salida de audio para optimizar la calidad del sonido, especialmente útil con un DAC externo. Valores disponibles: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** y **96 kHz**.
- **Número de Canales de Salida de Audio** — para sistemas de audio multicanal con un DAC externo, especifica el número de canales: **Mono, Estéreo, Centro / Izquierda / Derecha, Centro / Izquierda / Derecha / Surround, ITU BS.775-1, 5.1 Surround** y **SDDS**.
- **Duración del Búfer IO Preferido de Salida de Audio** — configura la duración del búfer de entrada / salida para la reproducción de audio. Un valor típico para minimizar la latencia al reproducir audio de alta resolución es alrededor de **5 milisegundos (0,005 segundos)**. El tamaño de búfer aceptable depende de tu hardware y entorno de software, así que prueba diferentes duraciones en tu dispositivo y elige la que mejor equilibre baja latencia y reproducción sin interrupciones.
- **Modo de Salida de Audio (solo iOS)** — configura el modo de salida de audio mixta para que el audio de Flacbox se mezcle con otras aplicaciones. Las instrucciones detalladas están [aquí](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Guardar Posición de Reproducción** — garantiza que la aplicación guarda y restaura la posición de reproducción de las canciones en tu biblioteca de música.
- **Guardar Estado del Reproductor de Audio** — preserva el estado de tu reproductor de audio antes de cerrar la app. Para continuar la reproducción, toca **Continuar Reproducción** en la parte superior de cualquier carpeta, álbum, artista o género cuando vuelvas a abrir la app. También puedes restaurar la reproducción de archivos individuales tocando la pista específica.

Una vez que hayas activado tanto **Guardar Posición de Reproducción** como **Guardar Estado del Reproductor de Audio**, abre cualquier carpeta, álbum, artista o género y verás un botón **Continuar Reproducción** en la parte superior de la pantalla junto con la última pista y posición guardadas. Tócalo para reanudar exactamente donde lo dejaste.

### Personalización

La Personalización te permite personalizar el aspecto de la pantalla del reproductor de audio, cambiar los controles disponibles en la pantalla principal, pantalla de bloqueo y barra de estado, y configurar los controles de salto de tiempo.

- **Estilo de Pantalla del Reproductor de Audio** — configura el posicionamiento de los elementos en la pantalla del reproductor de audio.
- **Estilo de Desplazamiento de Portadas de Álbumes** — configura el estilo de desplazamiento preferido para las portadas de álbumes.
- **Elementos Adicionales** — activa elementos extra en la pantalla del reproductor de audio. **Información de Formato de Audio** muestra la información de audio de la pista que suena sobre la portada; **Deslizador de Volumen de Audio** muestra el deslizador de salida de audio debajo de los controles de reproducción.
- **Acciones de Pantalla Principal** — configura qué botones deben ser visibles en la pantalla principal del reproductor de audio por defecto: **Modo Repetir y Aleatorio, Canción Siguiente y Anterior, Saltar Tiempo, Temporizador de Sueño, Google Chromecast, AirPlay y Bluetooth, Ecualizador de Audio, Buscar, Marcadores, Velocidad, Añadir Marcador, Añadir a Favoritos, Comentarios** y más.
- **Controles de Reproducción en la Pantalla de Bloqueo** — elige qué controles aparecen en la pantalla de bloqueo. Valores posibles: **Saltar Tiempo, Añadir Marcador, Añadir a Favoritos**.
- **Botones de Saltar Tiempo** — elige el intervalo de tiempo para los botones de **Saltar Tiempo**.

### Carga de Archivos

Durante el proceso de carga de archivos, puedes cambiar el tipo de red utilizado para cargar canciones. Opciones disponibles: **Wi-Fi**, **Wi-Fi y Datos Móviles**.

- **Tiempo de Precarga** — establece el intervalo de tiempo de almacenamiento en búfer. Auméntalo si tienes una conexión de red deficiente.
- **Usar URL Directa** — cuando está activado, se usa una URL directa para cargar la canción si el servidor lo admite. Esto puede acelerar la carga de canciones pero puede afectar la estabilidad de reproducción.

### Ecualizador de Audio

Personaliza los ajustes del ecualizador de audio. Puedes leer más sobre cómo configurar el ecualizador de audio [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocidad de Reproducción

Ajusta la velocidad de reproducción del reproductor de audio desde **0,02× hasta 3,00×**. Toca el icono de configuración en la esquina superior derecha para cambiar al **modo preciso** para ajustes más finos.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Velocidad de Reproducción de Flacbox" image="/docs/guide/flacbox/img/playback-speed.webp" >}}
{{< /cards >}}

### Corrección de Tono

Cambia los ajustes de corrección de tono usando los valores predefinidos. También puedes alternar entre valores predefinidos y modo preciso tocando el botón en la esquina superior derecha. La corrección de tono está disponible en la ruta del códec FFmpeg, con un rango de **-1000 a +1000**.

### Caché de Reproducción

Las canciones en la cola del reproductor de audio se descargan automáticamente para garantizar una reproducción fluida. Si descargas archivos de audio manualmente, puedes desactivar esta opción para evitar duplicados. También puedes configurar el tamaño de caché del reproductor de audio aquí.

### Temporizador de Sueño

Activa un temporizador para detener automáticamente la reproducción después de un período especificado — muy útil cuando quieres dormirte con música. Toca el icono de configuración en la esquina superior derecha para el **modo preciso** con granularidad minuto a minuto.

## Accesibilidad

Flacbox es totalmente accesible con **VoiceOver**. Cada componente tiene una etiqueta y descripción bien diseñadas. Cuando VoiceOver está activo, la app cambia al **Modo Texto** para que solo se muestren los elementos relevantes — mejorando la velocidad de navegación y la claridad. También puedes activar el Modo Texto en **Ajustes → Accesibilidad → Modo Texto**.

### Ajustar Controles Deslizantes con VoiceOver

1. **Selecciona el control deslizante** — desliza a izquierda o derecha hasta que VoiceOver lo anuncie.
2. **Ajusta el valor** — doble toque y mantén el control deslizante, luego arrastra arriba o abajo para cambiar el valor rápidamente. VoiceOver anuncia el nuevo valor mientras lo haces.

### Ajustar la Posición de una Pista en una Lista con VoiceOver

1. Toca el icono del indicador de reordenamiento cerca del título de la pista para darle foco.
2. Toca rápidamente dos veces el indicador de reordenamiento. En el segundo toque, no sueltes el dedo — mantenlo hasta que escuches un sonido que indica que la celda está lista para moverse.
3. Mueve la celda a su nueva posición.

Los demás componentes funcionan como se espera, usando los patrones de VoiceOver proporcionados por el sistema.
