---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: 'Aprende a usar Evervideo — el reproductor de video en la nube todo en uno para iPhone, iPad y Mac. Transmite y descarga videos desde iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA y S3 — además de Plex, Jellyfin, Emby, Subsonic y Navidrome. Picture-in-Picture, subtítulos primarios y secundarios, ecualizadores de audio y video, transmisiones RTSP de cámaras IP, Chromecast, AirPlay 2, decodificación hardware H.264/HEVC, integración con la biblioteca de Fotos y Apple Music, y un reproductor compacto siempre visible.'
keywords: [
  "guía Evervideo", "cómo usar Evervideo", "reproductor de video en la nube iPhone", "reproductor de video Mac",
  "reproductor MKV iOS", "reproductor de video FFmpeg", "reproductor HEVC iPhone",
  "Picture-in-Picture video iPhone", "reproductor PiP video iPad",
  "reproductor RTSP iPhone", "visor de cámara IP", "reproductor DLNA video",
  "cliente Plex iPhone", "cliente Jellyfin iOS", "cliente Emby iPad",
  "reproductor subtítulos iOS", "subtítulos SRT VTT ASS", "subtítulos secundarios iPhone",
  "ecualizador de video iOS", "ecualizador de audio reproductor de video", "DAC externo video",
  "transmitir video desde Google Drive", "transmitir video desde Dropbox",
  "transmitir video desde OneDrive", "transmitir video desde iCloud Drive",
  "transmitir video desde MEGA", "transmitir video desde NAS",
  "Chromecast video iPhone", "AirPlay 2 video", "reproductor video iCloud",
  "reproductor video biblioteca Fotos", "reproductor video Apple Music",
  "transferencia video Wi-Fi Drive", "lista de reproducción M3U video",
  "Evervideo Premium", "aplicación video Family Sharing"
]
tags: ["evervideo", "guía", "reproductor de video", "PiP", "subtítulos", "RTSP", "nube", "FFmpeg"]
---


### Bienvenido a la Guía de Evervideo

Evervideo es un reproductor de medios en la nube con todas las funciones para iPhone, iPad y Mac que convierte cualquier cuenta de almacenamiento en la nube, NAS o servidor multimedia en tu biblioteca multimedia personal, sin necesidad de volver a subir nada y manteniendo el control total de tus archivos.

Construido sobre un motor de reproducción personalizado basado en FFmpeg con decodificación H.264 y HEVC acelerada por hardware, Evervideo reproduce prácticamente cualquier contenedor y códec moderno — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS y la larga lista de formatos FFmpeg — con plena calidad, con almacenamiento en búfer inteligente para una transmisión fluida por Wi-Fi o datos móviles. Picture-in-Picture mantiene tu video sobre todas las demás aplicaciones, el reproductor compacto siempre visible te permite seguir viendo mientras navegas por tu biblioteca, y Chromecast y AirPlay 2 envían la reproducción a tu televisor, HomePod o sistema de altavoces con un toque.

Evervideo se conecta a una lista notablemente amplia de fuentes, todo desde una sola aplicación:

- **Almacenamiento personal en la nube:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores multimedia auto-alojados:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (y ownCloud mediante la API compartida) · Synology Drive · QNAP.
- **NAS y protocolos para compartir archivos:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (contraseña o autenticación por clave pública) · NFS · DLNA · UPnP.
- **Transmisiones en vivo y de cámaras IP:** RTSP — apunta Evervideo a cualquier URL RTSP (`rtsp://camera-ip/stream`) y simplemente se reproduce.
- **Almacenamiento de objetos compatible con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces y cualquier otro endpoint de S3-API.
- **Fuentes en el dispositivo:** la biblioteca de Fotos (Todos los Videos, Cortos / Medianos / Largos, Grabaciones de Pantalla, más tus Álbumes de Fotos), la biblioteca de la app Música (Álbumes, Géneros, Listas de reproducción), unidades USB / SD y Archivos Locales.

### Un Reproductor para Cada Formato y Códec

Mientras que la mayoría de las apps iOS se detienen en H.264 / H.265 dentro de MP4 / MOV, Evervideo incluye FFmpeg junto a los códecs del sistema de Apple para que puedas reproducir formatos que el sistema no reconoce — contenedores MKV, VP9, AV1, MPEG-2, OGG, Vorbis y muchos más — y cambia automáticamente entre la decodificación hardware H.264/HEVC y la decodificación por software según el archivo y el dispositivo.

Puedes seleccionar la pista de video (rips Blu-ray multi-stream), la pista de audio (pistas de comentarios, doblajes alternativos) y la pista de subtítulos. Los archivos externos de subtítulos SRT, VTT y ASS/SSA se cargan con un toque; el estilo avanzado de ASS/SSA se renderiza correctamente gracias a la librería libass incluida.

### Subtítulos Inteligentes

- **Selección de pista de subtítulos** perfecta para el aprendizaje de idiomas.
- **Archivos de subtítulos externos** (`.srt`, `.vtt`, `.ass`, `.ssa`) cargados desde cualquier lugar de tu dispositivo o desde la nube.
- **libass** para renderizado ASS/SSA con estilos completos.
- **Selección de fuente por pista y global** para subtítulos.
- **Selección de pista de audio** — elige el doblaje, el comentario o la pista del director.
- **Selección de pista de video** para archivos multi-ángulo o multi-versión.

### Ajusta la Imagen y el Sonido

Dos ecualizadores, uno al lado del otro: un ecualizador de audio para ajustar bajos y agudos (con importación / exportación de presets personalizados) y un ecualizador de video para ajustar brillo, contraste, saturación y matiz (también con importación / exportación). Ambos motores también exponen controles audiófilos: frecuencia de muestreo de salida de audio, número de canales, duración del buffer IO y modo mixto — para usuarios con DAC externos y receptores de cine en casa.

### Cast, AirPlay y Picture-in-Picture

- **Picture-in-Picture (PiP):** sigue viendo mientras usas otras aplicaciones.
- **AirPlay 2:** envía video a Apple TV, HomePod o cualquier altavoz / TV compatible con AirPlay 2.
- **Google Chromecast:** transmite directamente a un Chromecast o TV con Cast.
- **Reproductor compacto:** un mini reproductor persistente sobre cada pantalla para que puedas navegar por tu biblioteca sin perder el video.

### Privacidad y Seguridad

Evervideo usa los SDK oficiales e inicios de sesión basados en OAuth de cada proveedor de nube para que tu contraseña nunca llegue a la aplicación. Los tokens de acceso viven cifrados en el Keychain de iOS/MacOS, cada transferencia está protegida por TLS, y revocar el acceso desde tu cuenta en la nube (o eliminar Evervideo del dispositivo) borra todo de inmediato. Protege tu biblioteca con un código de acceso opcional de 4 dígitos para una capa adicional de privacidad.

### Primeros Pasos con Evervideo

Esta guía te lleva por cada parte de Evervideo en iPhone, iPad y Mac — desde conectar servicios en la nube, navegar por tu biblioteca, descargar y transferir archivos, gestionar listas de reproducción, hasta ajustar el reproductor multimedia, los ecualizadores, los subtítulos y Picture-in-Picture. Usa las tarjetas a continuación para ir directamente a la sección que necesitas.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navegación" subtitle="Barra de pestañas en iPhone, menú izquierdo en iPad y Mac, reproductor multimedia compacto siempre visible." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Archivos" subtitle="Una pestaña unificada para cloud, NAS, transmisiones RTSP, archivos locales, unidades USB y la cola de transferencias." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Biblioteca Multimedia" subtitle="Navega por Álbumes, Géneros, Recientes, Favoritos — más la biblioteca de Fotos de iOS y Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Listas de reproducción" subtitle="Crea listas de reproducción desde la nube, archivos locales, Fotos o la biblioteca de Música, importa M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Reproductor Multimedia" subtitle="Picture-in-Picture, pistas de audio y video, subtítulos, ecualizadores de audio + video, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Ajustes" subtitle="Motor de audio, decodificador de video, subtítulos, biblioteca, gestor de archivos, widgets, personalización, idioma, copia de seguridad." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Encuentra respuestas a las preguntas más frecuentes sobre Evervideo." >}}

{{< /cards >}}
