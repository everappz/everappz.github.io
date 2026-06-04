---
date: 2020-01-01
title: 'Flacbox'
description: 'Aprende a usar Flacbox — el reproductor de música en la nube con alta resolución FLAC, DSD, ALAC y FFmpeg para iPhone, iPad y Mac. Conecta iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB y DLNA. Transmite y descarga audio de alta resolución, edita metadatos, escucha audiolibros, haz scrobble en Last.fm, usa Apple CarPlay y widgets de pantalla de inicio, y personaliza el ecualizador de 10 bandas.'
keywords: [
  "guía de usuario Flacbox", "cómo usar Flacbox", "reproductor de música hi-res iPhone", "reproductor FLAC iPhone",
  "reproductor DSD iOS", "reproductor ALAC Mac", "app de música sin pérdidas", "reproductor de música en la nube iPhone",
  "reproductor FLAC offline Mac", "gestor de biblioteca musical", "editor de etiquetas de audio",
  "reproductor FLAC CarPlay", "app de audio Chromecast", "música AirPlay 2",
  "widgets Flacbox", "CarPlay Flacbox", "reproductor de música FFmpeg iOS",
  "reproductor de audiolibros iPhone", "marcadores de audio iOS", "corrección de tono app de música",
  "tasa de muestreo de salida de audio", "DAC externo iPhone", "USB DAC Mac",
  "app de música Synology", "app de música QNAP", "reproductor de música NAS iPhone",
  "reproductor de música WebDAV", "streaming de música SMB", "reproductor de música DLNA",
  "música iCloud Drive", "Google Drive FLAC", "reproductor FLAC Dropbox",
  "transferencia de música Wi-Fi Drive", "importar playlist M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "guía", "hi-res", "FLAC", "FFmpeg", "cloud", "CarPlay", "widgets"]
---


### Bienvenido a la Guía de Flacbox

Flacbox es un reproductor de música de alta resolución para iPhone, iPad y Mac que te permite convertir tu almacenamiento en la nube favorito, NAS y servidores de medios en tu propio servicio de streaming personal.

Flacbox se conecta a una lista notablemente amplia de fuentes, todo en una sola app:

- **Almacenamiento en la nube personal:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores autohospedados:** Plex · Jellyfin · Emby · Subsonic (y cada servidor compatible con Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (y ownCloud mediante la API compartida) · Synology Drive · QNAP.
- **Protocolos NAS y de uso compartido de archivos:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (contraseña o autenticación por clave pública) · NFS · DLNA / UPnP (reproducción y descarga).
- **Almacenamiento de objetos compatible con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces y cualquier otro endpoint de S3-API.
- **Descubrimiento de red local:** La sección «Dispositivos disponibles» lista automáticamente cada servicio Bonjour / mDNS en tu Wi-Fi.

Mientras la mayoría de las apps de música se limitan al motor de audio integrado de Apple, Flacbox incluye **FFmpeg** junto con los códecs del sistema para reproducir formatos que iOS no admite de serie — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, además de la familia habitual MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC.

### Disfruta de Streaming Fluido y Reproducción Sin Conexión

Flacbox cuenta con almacenamiento en búfer inteligente para un streaming fluido y un gestor de descargas incorporado para descargar playlists, artistas, álbumes, carpetas o pistas individuales.

### Biblioteca Musical Organizada Automáticamente

Cuando importas pistas de audio, Flacbox escanea sus metadatos y las organiza en una biblioteca musical ordenada — agrupadas por Canciones, Canciones no reproducidas, Álbumes, Artistas de álbum, Artistas, Géneros y Compositores.

### Corrige Metadatos y Etiqueta tu Música

El Editor de Etiquetas ID3 integrado puede limpiar etiquetas corruptas — de forma manual o con búsquedas automáticas en MusicBrainz.

### Transferencias Sencillas desde Mac, PC o NAS

Mueve música entre tu ordenador y tu iPhone o iPad con cualquiera de estas herramientas: SMB, WebDAV, DLNA, Wi-Fi Drive, iTunes / Finder File Sharing mediante cable Lightning o USB-C, unidades flash USB o iXpand Flash Drives.

### Personaliza tu Sonido con el Ecualizador

Flacbox incluye un ecualizador de 10 bandas con presets estilo iPod, un preamplificador y la posibilidad de guardar tus propios presets.

### Ideal para Audiolibros

Flacbox es un excelente reproductor de audiolibros — múltiples marcadores por pista, velocidad de reproducción detallada (0,02× a 3,00×), continuar reproducción exactamente donde la dejaste y un temporizador de sueño. Los marcadores de capítulo M4B y los archivos largos son totalmente compatibles.

### Transmite en Cualquier Lugar — Incluso en tu Coche y Pantalla de Inicio

Transmite música a Apple TV / HomePod mediante AirPlay 2, envíala a altavoces Google Chromecast y televisores con Cast, y lleva todo contigo con Apple CarPlay.

### Privacidad y Seguridad

Flacbox usa únicamente SDKs oficiales e inicios de sesión basados en OAuth de cada proveedor de nube — tu contraseña nunca llega a la app.

### Primeros Pasos con Flacbox

Esta guía te lleva por cada parte de Flacbox en iPhone, iPad y Mac.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navegación" subtitle="Barra de pestañas en iPhone, menú izquierdo en iPad y Mac, mini reproductor, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Conexiones" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Biblioteca Musical" subtitle="Canciones, Álbumes, Artistas, Géneros, Compositores — sincronizar, buscar, editar metadatos." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Listas de reproducción" subtitle="Crear, importar M3U / M3U8 / CUE, reordenar y exportar a M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Archivos Locales" subtitle="Música offline, unidades USB, Wi-Fi Drive, gestor de archivos, carpetas offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Reproductor de Audio" subtitle="Salida hi-res, ecualizador, tono, marcadores, AirPlay, Chromecast, velocidad, temporizador de sueño." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Ajustes" subtitle="Motor de audio, biblioteca, gestor de archivos, CarPlay, widgets, personalización, idioma, copia de seguridad." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Encuentra respuestas a las 50 preguntas más frecuentes sobre Flacbox." >}}

{{< /cards >}}
