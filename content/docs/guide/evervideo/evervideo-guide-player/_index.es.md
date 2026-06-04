---
title: "Reproductor Multimedia"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprende a usar el reproductor multimedia de Evervideo en iPhone, iPad y Mac. Picture-in-Picture, decodificación hardware H.264/HEVC, ecualizadores de audio y video, subtítulos primarios y secundarios, selección de pistas de audio y video, escalado y rotación de video, velocidad de reproducción, temporizador de sueño, AirPlay 2, Google Chromecast, transmisiones RTSP y el reproductor compacto siempre visible."
keywords: [
  "guía reproductor Evervideo", "ajustes reproductor video", "ecualizador Evervideo",
  "Picture-in-Picture iPhone", "PiP video iPad", "PiP video Mac",
  "AirPlay 2 video", "Google Chromecast video",
  "subtítulos video iPhone", "subtítulos SRT externos",
  "reproductor subtítulos ASS SSA", "libass iOS",
  "subtítulos duales aprendizaje idiomas",
  "ecualizador video brillo contraste", "ecualizador audio reproductor video",
  "bloqueo rotación reproductor video", "modo escalado video iOS",
  "decodificador hardware H.264 iPhone", "decodificador hardware HEVC iPad",
  "velocidad reproducción video", "reproductor video FFmpeg iOS",
  "reproductor RTSP iPhone", "reproductor video compacto",
  "reproductor video VR 360 iPhone"
]
tags: ["guía", "evervideo", "reproductor", "PiP", "subtítulos", "ecualizador de video"]
readingTime: 14
---


El Reproductor Multimedia es la pantalla principal de la app donde controlas la reproducción y la mayoría de las funciones de Evervideo. Reproduce tanto archivos de video como de audio y está construido sobre un motor de reproducción personalizado basado en FFmpeg con decodificación H.264 y HEVC acelerada por hardware. Vamos a explorar cómo usarlo.

## Acceder al Reproductor Multimedia

Puedes llegar al reproductor de pantalla completa desde la barra de reproductor compacto. En iPhone, el reproductor compacto se encuentra en la parte superior de la pantalla principal. En iPad y Mac, está en el lado izquierdo (o en la parte superior del panel principal). Para contraer el reproductor de pantalla completa de vuelta a la vista compacta, toca el botón de cerrar en la esquina inferior derecha o desliza hacia abajo. Para ocultar completamente el reproductor compacto, toca y desliza hacia abajo una vez más.

El reproductor compacto permanece visible mientras navegas por tu biblioteca, tu gestor de archivos o tus ajustes, para que nunca pierdas tu video mientras buscas el siguiente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Reproductor Multimedia de Evervideo a Pantalla Completa" image="/docs/guide/evervideo/img/evervideo-media-player-fullscreen.webp" >}}
{{< /cards >}}

## Formatos de Video y Audio Admitidos

Evervideo reproduce prácticamente cualquier contenedor y códec moderno a través del motor FFmpeg incluido, con decodificación H.264 y HEVC acelerada por hardware en dispositivos compatibles.

- **Contenedores de video:** MP4, M4V, MKV, MOV, AVI, FLV, WMV, ASF, WebM, TS, M2TS, MTS, MPG, MPEG, OGV, 3GP, 3G2, F4V, RM, RMVB, VOB, DAT — y muchos más.
- **Códecs de video:** H.264 (AVC), H.265 (HEVC), VP9, VP8, AV1, MPEG-2, MPEG-4, MJPEG, ProRes, Theora, WMV — más prácticamente cualquier otro códec que FFmpeg admite.
- **Códecs de audio:** AAC, MP3, FLAC, ALAC, OGG / Vorbis, OPUS, AC-3, EAC-3, DTS, AMR, WMA, APE, TTA, MPC, WV — y muchos más.
- **Formatos de subtítulos:** SRT, VTT (WebVTT), ASS / SSA y pistas de subtítulos de texto o imagen integradas.
- **Protocolos de streaming:** HTTP / HTTPS, HLS (m3u8), RTSP (cámaras IP e IPTV) y streaming directo de archivos mediante SMB / WebDAV / FTP / SFTP / NFS / DLNA.

Eso cubre prácticamente cualquier archivo de video que sea probable que encuentres — incluyendo rips MKV, transmisiones RTSP de cámaras de seguridad y descargas web AV1 webm.

## Controles de Reproducción

En la parte inferior de la pantalla del reproductor verás botones para Reproducir, Pausar, Siguiente y Anterior. También hay botones opcionales como Saltar Adelante y Saltar Atrás (10 segundos por defecto) que puedes activar en los ajustes de la app. Mantén presionados los botones Siguiente / Anterior para avanzar o retroceder rápidamente. Arrastra el control deslizante de reproducción para saltar a cualquier posición.

## Repetir y Reproducir Aleatoriamente

Toca el botón de repetir para alternar entre modos de repetición:

- **Repetir Todo** — repite cada video de tu cola.
- **Repetir Uno** — repite solo el video actual.
- **Parar al Terminar** — pausa cuando termina el video actual.
- **Sin Repetir** — reproduce la cola una vez sin repetir.

Usa el botón de **Aleatorio** para aleatorizar el orden de los videos en la cola.

## Picture-in-Picture (PiP)

En iPhone y iPad, Evervideo admite completamente Picture-in-Picture (PiP). Toca el icono PiP en la pantalla del reproductor o simplemente desliza Evervideo al segundo plano — el video continúa reproduciéndose en una ventana flotante sobre todas las demás apps. Arrastra la ventana flotante a cualquier esquina; pellizca para cambiar el tamaño; toca una vez para mostrar controles básicos de reproducción / pausa / omisión; toca el pequeño botón de expandir para volver al Evervideo completo.

PiP funciona con cada formato de video que Evervideo reproduce, incluyendo archivos transmitidos desde la nube y transmisiones RTSP. PiP también sigue funcionando mientras tu teléfono está bloqueado (dependiendo de tu configuración de Bloqueo Automático).

## Reproductor Compacto

El reproductor compacto es un mini reproductor persistente que permanece visible en la parte superior de cada pantalla de la app mientras navegas por la biblioteca, el gestor de archivos o los ajustes. Tócalo para expandirlo al reproductor de pantalla completa; desliza hacia abajo para contraerlo de nuevo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ajustes de Video de Evervideo desde el Reproductor Compacto en la Pantalla Principal" image="/docs/guide/evervideo/img/evervideo-video-settings-from-compact-player-view-on-the-main-screen.webp" >}}
{{< /cards >}}

## AirPlay 2

Para AirPlay, toca el botón AirPlay en el reproductor. Evervideo admite AirPlay 2, por lo que puedes transmitir video a Apple TV, HomePod o cualquier altavoz o smart TV compatible con AirPlay 2. En una configuración con múltiples dispositivos AirPlay, puedes enrutar el audio a múltiples receptores simultáneamente.

## Google Chromecast

Para usuarios de Google Cast, el icono Cast aparece en el reproductor. Tócalo para elegir un dispositivo y comenzar a transmitir. Asegúrate de que tu teléfono y el receptor Cast estén en la misma red Wi-Fi. No todos los códecs son compatibles con el hardware de Chromecast — algunos archivos pueden necesitar transcodificación.

## Transmisiones en Vivo RTSP

Evervideo puede reproducir fuentes RTSP directamente — cámaras IP, cámaras de timbre, transmisiones IPTV, emisiones y cualquier otra URL `rtsp://`. Agrega la transmisión como una conexión RTSP en Archivos → Enlaces en Línea → Agregar enlace, luego tócala para comenzar a ver. Las transmisiones RTSP funcionan en Picture-in-Picture, el reproductor compacto, y se transmiten por AirPlay 2 y Chromecast igual que un video normal.

## Selección de Pista de Audio

Para videos con múltiples pistas de audio (comentarios, doblajes alternativos, pistas del director), toca el botón Más acciones en el reproductor y elige Pista de Audio — luego selecciona la pista que deseas. Esto es esencial para películas en idiomas extranjeros, archivos BDMV / MKV con múltiples doblajes y contenido instructivo con pistas de comentarios.

## Selección de Pista de Video

Algunos archivos de video incluyen múltiples transmisiones de video (Blu-rays multi-ángulo, cortes alternativos). Elige Pista de Video del menú Más acciones para cambiar entre ellas durante la reproducción.

## Subtítulos — Internos y Externos

Evervideo te da un control detallado sobre los subtítulos:

- **Pista de subtítulos** — selecciona entre las pistas integradas en el archivo.
- **Archivos de subtítulos externos** — carga archivos `.srt`, `.vtt`, `.ass` o `.ssa` desde tu dispositivo, iCloud Drive o cualquier servicio en la nube conectado.
- **Renderizado Libass** — el estilo avanzado de ASS / SSA (fuentes, colores, posiciones, efectos de karaoke) se renderiza correctamente gracias a la librería libass incluida.
- **Selección de fuente** — elige una fuente personalizada para los subtítulos primarios y una fuente separada para los secundarios. Fuentes incluidas más cualquier fuente instalada en tu dispositivo están disponibles.

Puedes configurar todo esto en Ajustes → Subtítulos antes de la reproducción, o usar Más acciones → Subtítulos desde el reproductor para cambiar al vuelo.

## Ecualizador de Audio

Evervideo incluye un ecualizador de audio completo para ajustar las bandas sonoras de video para tus auriculares, altavoces o equipo hi-fi. Toca el icono del ecualizador en la vista de volumen (o la acción Ecualizador de Audio en el menú Más acciones del reproductor), activa el ecualizador con el interruptor en la esquina superior derecha, y elige un preset o arrastra los controles deslizantes de banda para crear el tuyo propio. Los presets personalizados se pueden exportar e importar para compartirlos entre dispositivos o hacer copias de seguridad.

## Ecualizador de Video

Para ajustar la imagen, Evervideo proporciona un ecualizador de video dedicado — ajusta brillo, contraste, saturación y matiz en tiempo real durante la reproducción. Al igual que el ecualizador de audio, los presets de video personalizados se pueden exportar e importar para compartir o hacer copias de seguridad. Úsalo para iluminar una escena oscura en un día soleado, aumentar la saturación en contenido desvaído o calentar un tono de color frío.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ecualizador de Video de Evervideo" image="/docs/guide/evervideo/img/evervideo-video-equalizer.webp" >}}
{{< /cards >}}

## Modo de Escalado de Video

Elige cómo el video llena la pantalla:

- **Ajustar** — preservar la relación de aspecto original; barras negras donde sea necesario.
- **Llenar** — llenar toda la pantalla, recortando el video si es necesario.
- **Estirar** — estirar el video para llenar la pantalla, distorsionando si es necesario.
- **Original** — mantener la resolución nativa a 1:1.

## Rotación de Video

Para videos grabados con la orientación incorrecta, elige **Más acciones → Rotación** y selecciona **0°**, **90°**, **180°** o **270°** para rotar la imagen sin salir del reproductor.

## Decodificación Hardware (H.264 y HEVC)

En Ajustes → Reproductor → Video, puedes activar / desactivar Decodificación Hardware H.264 y Decodificación Hardware H.265 (HEVC) de forma independiente. La decodificación hardware es más rápida, usa menos batería y funciona más fresco — pero en casos raros (archivos corruptos, perfiles exóticos) puede que necesites desactivar la decodificación hardware y recurrir a la decodificación por software FFmpeg. Evervideo te permite hacerlo archivo por archivo desde el menú Más acciones del reproductor.

## Viewport VR 360°

Evervideo incluye un viewport VR / 360° para archivos de video esférico. Al reproducir un video 360°, puedes arrastrar para mirar alrededor, pellizcar para hacer zoom, y Evervideo deformará el renderizado en tiempo real.

## Velocidad de Reproducción

Toca el control de Velocidad en la barra de herramientas del reproductor para cambiar la velocidad de reproducción — desacelera para análisis (0,25× o 0,5×) o acelera para tutoriales y conferencias (1,25×, 1,5×, 2× y hasta 3×). Toca el icono de configuración en la esquina superior derecha de la pantalla de Velocidad para cambiar al modo preciso con ajustes más finos. También está disponible la corrección de tono por pista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Velocidad de Reproducción de Evervideo en la Barra de Herramientas Principal" image="/docs/guide/evervideo/img/evervideo-media-player-playback-speed-on-main-toolbar.webp" >}}
{{< /cards >}}

## Cola del Reproductor

Para ver tu cola del reproductor, toca el botón de cola en el reproductor. Cada video en la cola tiene más acciones — toca los tres puntos para verlas. Para reordenar un video en la cola, usa el indicador de reordenamiento cerca del título y arrástralo a una nueva posición.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cola de Reproducción de Evervideo" image="/docs/guide/evervideo/img/evervideo-playback-queue.webp" >}}
{{< /cards >}}

## Temporizador de Sueño

Abre Ajustes → Reproductor → Temporizador de Sueño, actívalo y elige cuánto tiempo quieres que continúe la reproducción antes de parar automáticamente. También puedes agregar el botón Temporizador de Sueño directamente a la pantalla principal del reproductor a través de Ajustes → Reproductor → Personalización → Acciones de la Pantalla Principal.

## Marcadores del Reproductor

Guarda tu lugar en videos largos — conferencias, audiolibros en video, tutoriales, descargas de YouTube de horas — tocando Agregar Marcador del menú Más acciones. Los marcadores aparecen en la lista Más acciones → Marcadores del video y persisten entre sesiones.

## Menú de Más Acciones

Toca el botón de Más Acciones "..." en el reproductor para acceder a funciones adicionales.

- **Continuar Reproducción** — reanudar la cola desde la última posición.
- **Buscar** — encontrar un video específico en tu cola.
- **Marcadores** — ver y saltar a marcadores.
- **Velocidad** — ajustar la velocidad de reproducción.
- **Recientes** — videos reproducidos recientemente.
- **Favoritos** — videos favoritos.
- **Ecualizador de Audio** — activar el ecualizador de audio.
- **Ecualizador de Video** — activar el ecualizador de video.
- **Pista de Audio** — seleccionar la transmisión de audio.
- **Pista de Video** — seleccionar la transmisión de video.
- **Subtítulos** — pista primaria / secundaria, archivo externo, fuente.
- **Rotación** — rotar la imagen 0° / 90° / 180° / 270°.
- **Modo de Escalado** — Ajustar / Llenar / Estirar / Original.
- **Picture-in-Picture** — entrar en modo PiP.
- **AirPlay** / **Chromecast** — enviar a un dispositivo.
- **Temporizador de Sueño** — establecer un temporizador para detener la reproducción.
- **Guardar Cola como Lista de Reproducción** — guardar la cola actual como una nueva lista de reproducción.
- **Eliminar Cola** — vaciar la cola y detener la reproducción.
- **Ajustes** — ir directamente a los ajustes del reproductor.
- **Ayuda** — abrir la guía.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Más Acciones del Reproductor de Evervideo" image="/docs/guide/evervideo/img/evervideo-media-player-more-actions.webp" >}}
{{< /cards >}}

## Ajustes del Reproductor

El árbol completo de ajustes del reproductor está documentado en la [guía de Ajustes](/docs/guide/evervideo/evervideo-guide-settings/). Las secciones más usadas:

- **General** — Modo de repetición, modo aleatorio, guardar estado del reproductor, guardar posición de reproducción, intervalos de tiempo de salto.
- **Video** — Decodificación hardware H.264 / HEVC, ecualizador de video, modo de escalado, rotación, modo de visualización, FPS preferidas, formato de píxel preferido, viewport VR.
- **Audio** — Ecualizador de audio, frecuencia de muestreo, canales, duración del buffer IO, modo mixto.
- **Subtítulos** — Pista primaria / secundaria, selección de archivo externo, fuente, fuente secundaria.
- **Dispositivos** (iOS) — AirPlay / Chromecast.
- **Personalización** — Estilo de diseño del reproductor (Minimal / Inferior / Antiguo / Clásico), acciones de la pantalla principal, controles de la pantalla de bloqueo.
- **Caché de Reproducción** — caché de disco para streaming más fluido.
- **Temporizador de Sueño** — parada automática.

## Accesibilidad

Evervideo es completamente accesible con VoiceOver. Cada componente tiene una etiqueta y descripción bien diseñadas. Cuando VoiceOver está activo, la app cambia al Modo Texto para que solo se muestren elementos significativos — mejorando la velocidad de navegación y la claridad. También puedes activar el Modo Texto en Ajustes → Accesibilidad → Modo Texto.

### Ajustar Controles Deslizantes con VoiceOver

1. **Selecciona el control deslizante** — desliza hacia la izquierda o derecha hasta que VoiceOver lo anuncie.
2. **Ajusta el valor** — toca dos veces y mantén presionado el control deslizante, luego arrastra hacia arriba o abajo para cambiar el valor rápidamente. VoiceOver anuncia el nuevo valor mientras avanzas.

Otros componentes funcionan como se espera, usando los patrones de VoiceOver proporcionados por el sistema.
