---
title: "Evervideo 1.7: nuevos Plex, Jellyfin, streaming en la nube y gestos de reproducción"
date: 2026-05-18
description: "Evervideo 1.7 añade más de 10 nuevas conexiones — Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS — además de nuevos gestos de reproducción (doble toque para avanzar, mantener pulsado para velocidad 2x), un Wi-Fi Drive renovado con carga por lotes y actualizaciones de interfaz Liquid Glass para iPhone, iPad y Mac."
keywords: ["Evervideo 1.7", "actualización Evervideo", "reproductor de vídeo HD iPhone", "reproductor de vídeo Plex iOS", "vídeo Jellyfin iPhone", "reproductor de vídeo Emby iOS", "vídeo Subsonic iOS", "vídeo Navidrome iOS", "streaming de vídeo Internxt", "reproductor de vídeo Proton Drive", "reproductor de vídeo QNAP iPhone", "reproductor de vídeo Nextcloud iOS", "streaming de vídeo Amazon S3", "reproductor de vídeo SFTP iPhone", "reproductor de vídeo FTP iOS", "streaming de vídeo NFS iPhone", "transmitir vídeo desde NAS iPhone", "reproductor MKV iPhone", "gestos reproductor de vídeo iOS", "doble toque para buscar vídeo", "transferencia de vídeo Wi-Fi Drive iPhone", "diseño Liquid Glass", "reproductor de vídeo en la nube iOS 2026", "transmitir películas desde la nube iPhone"]
tags: ["Evervideo", "Evervideo 1.7", "Plex", "Jellyfin", "Emby", "Subsonic", "Navidrome", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Gestos de reproducción", "Liquid Glass", "Novedades"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-director-everappz.webp"
---

{{< author-byline >}}

**Resumen:** [Evervideo 1.7](/products/evervideo) es una gran actualización del reproductor de vídeo HD para iPhone, iPad y Mac. La versión añade más de 10 nuevas conexiones a la nube, NAS y servidores multimedia — **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, además de los servidores multimedia más populares **Plex**, **Subsonic**, **Navidrome**, **Jellyfin** y **Emby**, y tres protocolos de red: **FTP**, **SFTP** y **NFS**. Los nuevos **gestos de reproducción** te permiten dar un doble toque para saltar adelante o atrás, mantener pulsado para reproducir a 2x y un solo toque para mostrar u ocultar los controles — todo sin salir de la pantalla completa. Wi-Fi Drive estrena una interfaz renovada con modo de selección y una cola de carga más inteligente. Toda la app está adaptada al nuevo diseño **Liquid Glass** de Apple.

---

## ¡Hola a todos!

Llega una gran actualización de Evervideo. Esta es una de las versiones más grandes que hemos publicado: **más de 10 nuevas conexiones a la nube, servidores y red**, **gestos de reproducción** completamente nuevos para un control más rápido en pantalla completa, una experiencia **Wi-Fi Drive** renovada y una interfaz adaptada a **Liquid Glass** en iPhone, iPad y Mac.

[Descarga Evervideo 1.7 desde el App Store](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) o actualiza desde tu versión actual. Los usuarios de Mac pueden conseguir la [versión de escritorio aquí](https://apps.apple.com/app/evervideo/id6743504109).

## Más de 10 nuevas conexiones a la nube, NAS y servidores multimedia

Evervideo 1.7 amplía lo que se considera tu 'biblioteca de vídeo'. Si tus películas, series o grabaciones viven en una nube en la que confías, en un NAS de casa o en un servidor multimedia autoalojado, Evervideo ahora puede transmitir directamente desde allí — sin descargas, sin conversiones, sin recodificación.

### Almacenamiento en la nube centrado en la privacidad: Internxt y Proton Drive

Si te importa el cifrado de extremo a extremo y el almacenamiento de conocimiento cero, dos de las nubes más respetadas centradas en la privacidad ya están integradas de forma nativa en Evervideo:

- **Internxt** — nube española de código abierto, con cifrado post-cuántico y conforme con el RGPD. Plan gratuito disponible.
- **Proton Drive** — almacenamiento con cifrado de extremo a extremo de los creadores de Proton Mail y Proton VPN, con sede en Suiza. Plan gratuito disponible y planes de pago para bibliotecas más grandes.

Conéctate una vez y tus vídeos se transmiten por el túnel cifrado — Evervideo nunca ve tus datos en claro, y tampoco el servidor del proveedor.

### Almacenamiento autoalojado: QNAP, Nextcloud, Amazon S3

Para usuarios que gestionan su propia infraestructura:

- **QNAP** — conexión API nativa a dispositivos QNAP NAS para una reproducción de vídeo rápida y fiable por Wi-Fi local o acceso remoto. Transmite archivos 4K MKV directamente sin recodificación.
- **Nextcloud** — conéctate a cualquier instancia autoalojada o gestionada de Nextcloud. Ideal si ya te has migrado de Google Drive o Dropbox por razones de privacidad.
- **Amazon S3** — apunta Evervideo a cualquier bucket S3 (o a almacenamiento compatible con S3 como Backblaze B2, Wasabi, MinIO, Cloudflare R2) y transmite tu colección directamente.

### <a id="media-servers"></a>Servidores multimedia: Plex, Subsonic, Navidrome, Jellyfin, Emby

Esta es la novedad estrella para los aficionados al vídeo autoalojado. Evervideo 1.7 convierte tu iPhone, iPad o Mac en un cliente de primera clase para los servidores multimedia open-source y freemium más populares:

- **Plex** — Plex Media Server se descarga y se ejecuta **gratis**, con suscripción opcional **Plex Pass** para funciones como sincronización móvil, transcodificación por hardware y TV en directo. Evervideo funciona tanto con bibliotecas gratuitas como con Plex Pass — transmite toda tu colección de películas y series.
- **Subsonic** — el servidor de streaming autoalojado original. El servidor oficial Subsonic es **de pago** (1 $/mes después de una prueba de 30 días), y Evervideo también habla la API de Subsonic con servidores de vídeo compatibles.
- **Navidrome** — servidor moderno, ligero, **completamente gratuito y de código abierto**. Implementa la API de Subsonic. Funciona en una Raspberry Pi, un NAS o cualquier máquina Linux.
- **Jellyfin** — servidor multimedia **completamente gratuito y de código abierto** (un fork comunitario de Emby). Gestiona películas, series, música, libros y vídeos caseros. Sin cuentas, sin telemetría, sin suscripciones. La opción preferida para usuarios que quieren streaming autoalojado sin ataduras comerciales.
- **Emby** — servidor multimedia **freemium**. El servidor básico es gratuito; **Emby Premiere** es una compra única o anual que desbloquea apps móviles, sincronización offline, Cinema Mode y más. Evervideo se conecta tanto a bibliotecas gratuitas como Premiere.

Sea cual sea el servidor que ejecutes, Evervideo transmite toda tu biblioteca — películas, series, vídeos caseros y pistas de subtítulos incrustados — con el ecualizador de vídeo, soporte 360°, Picture-in-Picture, AirPlay y Chromecast.

### Nuevos protocolos de red: FTP, SFTP, NFS

Para usuarios con servidores personalizados, home labs o cajas NAS genéricas que no traen una app móvil pulida, Evervideo 1.7 añade tres protocolos clásicos:

- **SFTP (SSH File Transfer Protocol)** — la respuesta adecuada para **streaming remoto seguro de vídeo desde tu propio servidor**. SFTP funciona sobre SSH, por lo que toda la transferencia (autenticación y datos de vídeo) está cifrada. Si tienes un VPS, un servidor dedicado o una máquina Linux en casa con acceso SSH, puedes dejar una carpeta de vídeos y transmitir por la red pública sin exponer nada más. Admite autenticación por contraseña y por clave.
- **FTP** — el estándar de toda la vida para la transferencia de archivos. Útil si tu **NAS doméstico** (Synology antiguo, ASUS, D-Link, TerraMaster o cajas genéricas) expone un servidor FTP pero no tiene una integración API nativa. Lo mejor es usarlo dentro de tu red local.
- **NFS (Network File System)** — el protocolo de compartición por defecto en Linux y en la mayoría de los dispositivos NAS. Los recursos compartidos NFS son habituales en home labs y pequeñas redes corporativas; Evervideo ahora los monta y transmite vídeo 4K y HD con bajo consumo.

> **Consejo:** SFTP es el protocolo que quieres para streaming por la red pública. FTP y NFS son ideales dentro de tu red local — mantenlos fuera de la red pública a menos que los envuelvas en una VPN.

## Nuevos gestos de reproducción

Ver vídeos en pantalla completa debería ser cómodo. Evervideo 1.7 introduce un conjunto limpio de gestos táctiles que te permiten controlar la reproducción sin mostrar los controles en pantalla — perfecto para películas, clases o cualquier cosa que quieras ver sin interrupciones.

### Doble toque — Saltar adelante o atrás

Da un doble toque en el **lado derecho** de la pantalla para **avanzar** un número configurable de segundos. Da un doble toque en el **lado izquierdo** para **retroceder**. Puedes cambiar el intervalo (por defecto: 10 segundos) en **Ajustes → Reproducción → Intervalo de salto del gesto** — elige cualquier valor entre 5 segundos (para búsqueda fina) y 60 segundos (para saltar intros).

Es el gesto que los usuarios de YouTube y Netflix reconocerán al instante, y ahora es nativo en Evervideo para cualquier vídeo de cualquier fuente.

### Mantener pulsado — Velocidad 2x temporal

Mantén pulsado en cualquier parte de la pantalla para **acelerar temporalmente la reproducción a 2x**. Suelta para volver a la velocidad normal. Perfecto para:

- Saltar escenas lentas sin comprometerte con un cambio de velocidad permanente.
- Recorrer rápidamente clases, tutoriales o podcasts para encontrar la parte relevante.
- Probar películas antes de comprometerte a verlas enteras.

El gesto de mantener pulsado no cambia tu velocidad de reproducción guardada — suelta y vuelves donde estabas.

### Toque sencillo — Mostrar / Ocultar controles

Un toque sencillo en la pantalla alterna los controles de reproducción (reproducir, pausar, barra de búsqueda, subtítulos, ecualizador). Toca una vez para mostrarlos, vuelve a tocar para ocultarlos. Combinado con el doble toque y mantener pulsado, esto significa que puedes pasar casi toda una película en modo pantalla completa limpio y seguir buscando, pausando y escaneando rápido cuando lo necesites.

## Wi-Fi Drive: nueva interfaz y cargas más rápidas

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) es la función integrada de Evervideo para **transferir vídeos de forma inalámbrica desde el ordenador a tu iPhone o iPad — sin iTunes, sin cables, sin cuenta en la nube**. Ambos dispositivos tienen que estar en la misma red Wi-Fi. Inicias el servidor en la app de iOS y luego:

- Abres la URL en cualquier navegador de escritorio (Safari, Chrome, Firefox, Edge), arrastras tus archivos de vídeo a la página y se cargan directamente en el dispositivo, o
- Montas el dispositivo como recurso de red mediante el **Finder de Mac** ('Conectarse al servidor…') o el **Explorador de archivos de Windows** (Conectar a unidad de red) usando WebDAV.

Es la forma más rápida de mover una gran colección local de vídeo a tu móvil o tableta sin ningún servicio de terceros. Consulta la [guía paso a paso aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).

En Evervideo 1.7, Wi-Fi Drive recibe:

- **Interfaz rediseñada** — más limpia, más fácil de leer de un vistazo y actualizada para Liquid Glass.
- **Nuevo modo de selección para acciones por lotes** — elige varios archivos o carpetas y actúa sobre ellos en bloque (eliminar, mover, copiar).
- **Cola de carga de archivos mejorada** — mejor indicador de progreso y resistencia a los altibajos de la red, de modo que una conexión Wi-Fi inestable ya no arruine una transferencia de 30 GB.
- **Mejor rendimiento general de transferencia** — cargas medibles más rápidas para bibliotecas grandes, especialmente para archivos 4K MKV y colecciones de películas.

## Otras mejoras

### Actualizaciones de diseño Liquid Glass

La interfaz de Evervideo 1.7 está adaptada al nuevo material **Liquid Glass** de Apple en toda la app — superficies translúcidas, animaciones más suaves y controles refinados que encajan de forma natural en iOS 26, iPadOS 26 y macOS 26. Now Playing, el explorador de archivos y las pantallas de ajustes se han ajustado a la nueva estética del sistema.

### Bibliotecas de conexión actualizadas

Hemos refrescado las bibliotecas subyacentes que usa Evervideo para hablar con **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive**, **iCloud Drive**, **MEGA** y otros servicios. Resultado: menos fallos de conexión en casos límite, mejor soporte para versiones más recientes de servidor y mayor fiabilidad al transmitir vídeo en conexiones lentas o geográficamente distantes.

### Corrección de errores de reproducción

- Solucionados los problemas de reproducción en ciertos servidores autoalojados, donde las transmisiones se quedaban paradas tras buscar en archivos MKV grandes.
- Mejor comportamiento de reanudación cuando la red se interrumpe brevemente durante la reproducción.
- Sincronización de subtítulos más fluida en contenido de larga duración.

### Correcciones de localización

Corrección de traducciones en varios idiomas según los comentarios directos de los usuarios. Mejor ajuste de texto en botones más pequeños y en idiomas europeos más largos (alemán, neerlandés, francés).

### Pequeños refinamientos inspirados en tus comentarios

Muchas pequeñas mejoras basadas en las reseñas del App Store y los correos a support@everappz.com. Leemos cada mensaje.

## Por qué importa esta actualización

Evervideo 1.7 se construye sobre tres ideas:

1. **Tus vídeos, donde sea que los tengas.** Tanto si tu biblioteca vive en iCloud Drive, en una nube centrada en la privacidad como Proton Drive o Internxt, en un servidor multimedia como Plex o Jellyfin, en un NAS de casa o en una Raspberry Pi con Navidrome — Evervideo se conecta ahora a ello de forma nativa, con la misma experiencia de reproducción en todas partes.
2. **Vídeo en pantalla completa que se siente sin esfuerzo.** Los nuevos gestos táctiles (doble toque, mantener pulsado, toque sencillo) aportan el tipo de control fluido al que las apps de streaming como YouTube y Netflix han acostumbrado a los usuarios, aplicado a *tu* colección de vídeo.
3. **Transferencias más rápidas desde tu ordenador.** Un Wi-Fi Drive renovado con selección por lotes y una cola de carga más inteligente hace que mover grandes colecciones de películas 4K a tu iPhone o iPad sea realmente rápido — sin cables, sin iTunes, sin compresión.

## Consigue Evervideo 1.7

[**Descarga Evervideo desde el App Store**](https://apps.apple.com/app/evervideo-hd-video-player/id6602897336) o actualiza desde dentro del App Store. La [versión para Mac](https://apps.apple.com/app/evervideo/id6743504109) está disponible por separado como aplicación universal de Mac. Evervideo es una descarga gratuita con mejoras opcionales dentro de la app para funciones avanzadas. Las nuevas conexiones a la nube, el soporte para servidores multimedia, los gestos de reproducción, las mejoras de Wi-Fi Drive y la interfaz Liquid Glass forman parte de la actualización base.

Si disfrutas de la app, deja una valoración en el App Store — realmente ayuda. ¿Tienes comentarios o algún problema? Escríbenos a **support@everappz.com**. Leemos cada mensaje.

## Preguntas frecuentes

{{% details title="¿Qué hay de nuevo en Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 introduce soporte para más de 10 nuevas conexiones (Plex, Jellyfin, Emby, Subsonic, Navidrome, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), nuevos gestos de reproducción (doble toque para buscar, mantener pulsado para velocidad 2x, toque sencillo para mostrar/ocultar controles), un Wi-Fi Drive rediseñado con modo de selección y una cola de carga más inteligente, actualizaciones de diseño Liquid Glass, bibliotecas de conexión actualizadas y muchas correcciones de errores.
{{% /details %}}

{{% details title="¿Funciona Evervideo con Plex?" closed="true" %}}
Sí. A partir de Evervideo 1.7, puedes conectarte a un Plex Media Server y transmitir toda tu biblioteca de vídeo — películas, series y vídeos caseros. Plex Media Server es gratuito; Plex Pass es opcional. Evervideo es compatible tanto con configuraciones gratuitas como con Plex Pass, incluida la reproducción directa de MKV, MP4, AVI, MOV y otros formatos sin recodificación.
{{% /details %}}

{{% details title="¿Se soportan Jellyfin o Navidrome en Evervideo?" closed="true" %}}
Sí. Tanto Jellyfin como Navidrome son totalmente compatibles con Evervideo 1.7. Jellyfin es un servidor multimedia gratuito y de código abierto que gestiona vídeo y audio. Navidrome es un servidor gratuito y de código abierto que implementa la API de Subsonic. Evervideo se conecta a ambos de forma nativa.
{{% /details %}}

{{% details title="¿Son gratuitos Plex, Jellyfin, Emby, Navidrome y Subsonic?" closed="true" %}}
- **Plex** — el servidor es gratis; Plex Pass es una mejora opcional de pago.
- **Jellyfin** — completamente gratis y de código abierto.
- **Emby** — el servidor es gratis; Emby Premiere es de pago y desbloquea la sincronización móvil y el modo offline.
- **Navidrome** — completamente gratis y de código abierto.
- **Subsonic** — el servidor oficial cuesta 1 $/mes tras una prueba de 30 días, pero su API es abierta y muchos servidores gratuitos (incluido Navidrome) la implementan.
{{% /details %}}

{{% details title="¿Puedo transmitir desde mi NAS doméstico por SFTP, FTP o NFS?" closed="true" %}}
Sí. Evervideo 1.7 añade SFTP, FTP y NFS como tipos de conexión nativos. SFTP es la opción recomendada para transmitir desde tu propio servidor por la red pública, ya que todo el tráfico se cifra mediante SSH. FTP y NFS se usan mejor dentro de tu red local o detrás de una VPN.
{{% /details %}}

{{% details title="¿Cómo conecto Evervideo a un servidor personalizado por SFTP?" closed="true" %}}
Abre Evervideo, ve a la pestaña Conexiones, elige SFTP e introduce el nombre de host o IP del servidor, el puerto (normalmente 22), el nombre de usuario y una contraseña o una clave SSH privada. Evervideo examinará tus carpetas remotas y transmitirá los archivos de vídeo directamente con cifrado de extremo a extremo.
{{% /details %}}

{{% details title="¿Evervideo es compatible con Internxt y Proton Drive?" closed="true" %}}
Sí. Ambas nubes centradas en la privacidad se admiten a partir de Evervideo 1.7. Se suman a MEGA y a otros servicios con prioridad a la privacidad ya disponibles en la app.
{{% /details %}}

{{% details title="¿Cómo funcionan los nuevos gestos de reproducción?" closed="true" %}}
En la reproducción de vídeo a pantalla completa, **da un doble toque en el lado derecho** para avanzar y **un doble toque en el lado izquierdo** para retroceder un intervalo configurable (por defecto 10 segundos — cámbialo en Ajustes). **Mantén pulsado** en cualquier parte de la pantalla para acelerar temporalmente a 2x; suelta para volver a la normalidad. **Un toque sencillo** en cualquier parte muestra u oculta los controles de reproducción.
{{% /details %}}

{{% details title="¿Puedo cambiar el intervalo de salto del doble toque?" closed="true" %}}
Sí. Ve a **Ajustes → Reproducción → Intervalo de salto del gesto** y elige un valor entre 5 y 60 segundos. La mayoría de los usuarios lo mantiene en 10 o 15 segundos.
{{% /details %}}

{{% details title="¿Qué es Wi-Fi Drive en Evervideo?" closed="true" %}}
Wi-Fi Drive es la función integrada de transferencia inalámbrica de archivos de Evervideo. Te permite subir vídeos desde tu ordenador a tu iPhone o iPad a través de tu red Wi-Fi local — sin iTunes, sin cables, sin cuenta en la nube. Puedes usar cualquier navegador de escritorio o un cliente WebDAV como el Finder de Mac o el Explorador de archivos de Windows. Consulta la [guía completa de Wi-Fi Drive](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/).
{{% /details %}}

{{% details title="¿Reproduce Evervideo MKV, AVI y otros formatos desde Plex o Jellyfin?" closed="true" %}}
Sí. Evervideo reproduce prácticamente cualquier formato de vídeo — MKV, AVI, MP4, MOV, FLV, WMV, WEBM, M4V, TS, 3GP — y los transmite directamente desde Plex, Jellyfin, Emby y otros servidores multimedia sin requerir transcodificación para la mayoría de los códecs. Esto significa menos carga de CPU en tu servidor y tiempos de inicio más rápidos.
{{% /details %}}

{{% details title="¿Es gratis actualizar a Evervideo 1.7?" closed="true" %}}
Sí. Evervideo es una descarga gratuita del App Store, y 1.7 es una actualización gratuita para todos los usuarios actuales. Las nuevas integraciones en la nube, el soporte para servidores multimedia, los gestos de reproducción, las mejoras de Wi-Fi Drive y la interfaz Liquid Glass forman parte de la actualización base.
{{% /details %}}

{{% details title="¿En qué dispositivos está disponible Evervideo 1.7?" closed="true" %}}
Evervideo 1.7 funciona en iPhone, iPad y Mac. AirPlay y Chromecast te permiten enviar la reproducción a una pantalla más grande. La sincronización con iCloud Drive mantiene tu biblioteca y ajustes consistentes en todos los dispositivos.
{{% /details %}}
