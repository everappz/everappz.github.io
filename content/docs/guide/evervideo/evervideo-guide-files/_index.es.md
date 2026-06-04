---
title: "Archivos"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprende a usar la pestaña Archivos en Evervideo en iPhone, iPad y Mac. Conecta servicios en la nube, dispositivos NAS, servidores multimedia y transmisiones RTSP en un solo lugar. Gestiona videos sin conexión, la cola de transferencias, descargas, Wi-Fi Drive, compartición de archivos de iTunes / Finder y unidades USB. Incluye iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA y almacenamiento compatible con S3."
keywords: [
  "archivos Evervideo", "conexiones Evervideo", "archivos locales Evervideo",
  "configuración video en la nube iPhone", "conectar video Google Drive", "streaming SMB video",
  "reproductor video WebDAV iOS", "DLNA video iPhone", "streaming NAS video",
  "transferencia video Wi-Fi Drive", "compartición archivos iTunes Evervideo", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "modo sin conexión video Evervideo", "cola transferencias Evervideo",
  "gestor archivos Evervideo", "carpeta documentos Evervideo",
  "reproductor video Synology", "reproductor video QNAP",
  "reproductor video Apple Time Capsule", "USB DAC video",
  "reproductor video iXpand", "reproductor video S3"
]
tags: ["guía", "evervideo", "archivos", "conexiones", "nube", "NAS", "Plex", "RTSP"]
readingTime: 14
---

La pestaña Archivos es el gestor de archivos todo en uno de Evervideo. A diferencia de la mayoría de las aplicaciones de video que separan el almacenamiento en la nube de los archivos locales en diferentes pestañas, Evervideo fusiona ambos en una sola pantalla con desplazamiento para que puedas pasar de un servidor Plex a una carpeta en la nube a la carpeta de Documentos de tu iPhone sin cambiar de pestaña.

La pestaña Archivos se divide en secciones claras que aparecen en este orden en tu pantalla:

- **Acceso Rápido** — recientes y favoritos para los archivos y carpetas que abriste más recientemente.
- **Archivos en Esta Aplicación** — lo que está en la carpeta Documentos con sandbox de Evervideo.
- **Archivos en Este iPhone / iPad / Mac** — videos en otro lugar de tu dispositivo, accesibles a través del selector de archivos del sistema.
- **Almacenamiento en la Nube** — cada cuenta en la nube, NAS y servidor multimedia que has conectado.
- **Dispositivos disponibles** — servidores y unidades descubiertos automáticamente por Bonjour / mDNS en tu red local.

En la esquina superior derecha de la pantalla Archivos hay un botón de Transferencias (un icono de flechas giratorias). Tócalo para abrir la Cola de Transferencias donde monitoreas cada descarga y carga en todas tus fuentes.

{{< cards cols="1">}}
  {{< card title="" subtitle="Archivos Evervideo en Almacenamientos Conectados" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Conectar al Almacenamiento en la Nube

La sección de Almacenamiento en la Nube de la pestaña Archivos es donde vive cada cuenta conectada, NAS, servidor multimedia y transmisión — uno al lado del otro, en una lista con desplazamiento.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sección de Almacenamiento en la Nube de Evervideo en la Pestaña Archivos" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Abre la pestaña **Archivos**.
- Desplázate a la sección **Almacenamiento en la Nube**.
- Toca **Conectar con almacenamiento en la nube** del menú.
- Elige un servicio de almacenamiento en la nube de la lista.
- Ingresa tus credenciales en la página de autorización oficial del proveedor de la nube, luego toca **Hecho**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Conectar un Servicio de Almacenamiento en la Nube" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Si encuentras algún problema, verifica tu conexión a internet y tu nombre de usuario / contraseña. En la versión Premium de la app, puedes agregar un número ilimitado de servicios; la versión gratuita admite hasta tres.

## Servicios de Almacenamiento en la Nube, Servidores Multimedia y Protocolos Admitidos

Evervideo admite una gama excepcionalmente amplia de fuentes para tus videos. Todo lo siguiente funciona desde un único flujo de Conectar con almacenamiento en la nube.

**Almacenamiento personal en la nube:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidores multimedia auto-alojados:** Plex · Jellyfin · Emby · Subsonic (y cada servidor compatible con Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (y ownCloud mediante la API compartida) · Synology Drive · QNAP.

**NAS y protocolos para compartir archivos:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, contraseña o autenticación por clave pública) · NFS · DLNA / UPnP (reproducción y descarga).

**Transmisiones en vivo y de cámaras IP:** RTSP — apunta Evervideo a cualquier URL `rtsp://` y simplemente se reproduce. Ideal para cámaras de seguridad, transmisiones IPTV, cámaras de timbre, monitores de bebé y fuentes similares en vivo.

**Almacenamiento de objetos compatible con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces y cualquier otro endpoint de S3-API.

**Bibliotecas en el dispositivo:** la biblioteca de Fotos (todos los videos, grabaciones de pantalla, álbumes de fotos) y la biblioteca de la app Música (Álbumes, Géneros, Listas de reproducción) — ambas aparecen dentro de la Biblioteca Multimedia para que no tengas que copiar nada.

**Descubrimiento de red local:** la sección Dispositivos disponibles lista automáticamente cada servicio Bonjour / mDNS en tu red Wi-Fi — Plex, Jellyfin, servidores Emby, Synology, QNAP, routers AirPort con unidades conectadas, Apple Time Capsule — para que puedas tocar para conectar sin escribir una dirección IP.

Cada conexión usa el SDK oficial o el protocolo abierto del servicio, con autorización basada en OAuth donde se admite. Puedes conectar múltiples cuentas del mismo servicio (por ejemplo, dos cuentas de Google Drive, o tanto un servidor Plex como uno Jellyfin) y navegar por ellas lado a lado en la sección de Almacenamiento en la Nube.

## Seguridad y Privacidad

Evervideo usa solo SDK oficiales y conexiones seguras para interactuar con los servicios en la nube conectados. Tu nombre de usuario y contraseña no son accesibles para la aplicación — todas las transferencias están cifradas con TLS.

Cuando ingresas tu nombre de usuario y contraseña, la aplicación te muestra la página de autorización oficial proporcionada por el proveedor del servicio en la nube, y todo el proceso de autorización tiene lugar fuera de la aplicación. El proveedor del servicio en la nube luego envía un auth-token a la aplicación después de una autorización exitosa, y ese token se usa para hacer llamadas API.

Un auth-token es una clave digital que permite a aplicaciones de terceros interactuar con el almacenamiento en la nube en tu nombre. El token se almacena en tu dispositivo en el almacenamiento seguro del sistema de Apple (Keychain), que está cifrado en reposo y protegido por el código de acceso de tu dispositivo o bloqueo biométrico. Puedes descargar archivos de los servicios en la nube conectados a tu dispositivo; esos archivos se colocan en el directorio Documentos de la app y pueden eliminarse en cualquier momento usando el gestor de archivos integrado.

La aplicación no comparte ninguna información de tus cuentas en la nube conectadas con Everappz, anunciantes o ningún tercero. Puedes revocar el acceso a tu cuenta en la nube en cualquier momento abriendo la página de configuración de la cuenta en tu navegador web.

## Rechazar Auth-Token

Para revocar un auth-token, inicia sesión en tu cuenta en la nube en un navegador web y navega a la página de seguridad o de apps conectadas. Allí puedes encontrar cada app de terceros que está conectada a tu cuenta en la nube y eliminar cualquiera de ellas si ya no quieres usarla. Las instrucciones detalladas para cuentas de Google están disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

También puedes desconectar la cuenta en la nube dentro de la propia aplicación — cuando lo haces, el auth-token se elimina inmediatamente de tu dispositivo. Si desinstala la aplicación de tu dispositivo, todos los datos descargados y los tokens de acceso se eliminan automáticamente con ella.

## Desconectar un Almacenamiento en la Nube o Cambiar la Configuración

- **Accede a las opciones de almacenamiento en la nube** — localiza el servicio conectado en la sección **Almacenamiento en la Nube** de la pestaña Archivos.
- **Toca el botón "..."** junto al título del servicio para abrir opciones adicionales:
  - **Renombrar** — cambia el nombre del servicio en la nube tal como aparece en tu lista.
  - **Ajustes** — modifica la configuración o los datos de autenticación. A veces puede que necesites volver a autorizar el servicio en la nube conectado si el token de autorización ha expirado.
  - **Desconectar** — severs completamente la conexión entre la app y el servicio en la nube. Esto elimina todos los videos asociados con ese servicio de tu biblioteca multimedia, pero los deja intactos en el servidor.

## Conectar a un Ordenador o NAS

Puedes conectar tu ordenador, NAS personal u otro dispositivo de red usando el protocolo SMB, WebDAV, FTP / FTPS, SFTP, NFS o DLNA. Esta es la forma más fácil de traer una biblioteca multimedia doméstica existente — ya sea en un Mac, PC con Windows, Synology, QNAP, Apple Time Capsule o WD My Cloud Home — a Evervideo sin copiar nada.

### Conectar a un Ordenador Usando SMB

- Toca **Conectar con almacenamiento en la nube → SMB**.
- Ingresa la dirección IP del ordenador y el nombre de la carpeta compartida usando el formato `smb://computer-ip-address/shared-folder-name`.
- Elige la versión del protocolo: **Auto**, **SMB1** o **SMB2**.
- Ingresa tu nombre de usuario y contraseña (si es necesario).
- Toca **Hecho**.

Si la conexión es exitosa, el recurso compartido aparece en la sección de Almacenamiento en la Nube. Un tutorial completo sobre cómo conectar tu Mac o PC usando SMB está disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Conectar a un NAS Usando WebDAV

Todos los pasos son iguales que con SMB, excepto por el campo URL. Usa `http://server-name` o `https://server-name` si el servidor admite SSL. WebDAV funciona con Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home y cualquier otro servidor con un endpoint WebDAV.

Un tutorial completo sobre WebDAV está disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Conectar vía DLNA / UPnP

Comparte una biblioteca multimedia en tu PC con Windows o NAS usando el protocolo DLNA / UPnP y accede a ella dentro de Evervideo como se describe [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA es ampliamente compatible, pero solo te permite reproducir o descargar videos — no puedes subir archivos ni crear nuevas carpetas en un servidor DLNA.

### Conectar Usando FTP, FTPS o SFTP

Evervideo también admite los protocolos clásicos de transferencia de archivos. Para conectar un servidor vía FTP o FTPS, toca Conectar con almacenamiento en la nube → FTP, ingresa la URL del host en la forma `ftp://server-name` (o `ftps://server-name` para una conexión cifrada), proporciona tu nombre de usuario y contraseña, luego toca Hecho. Para SFTP (SSH File Transfer Protocol), elige SFTP y proporciona ya sea una contraseña o un par de claves SSH.

### Conectar a un Recurso NFS

Evervideo incluye soporte NFS (Network File System) — útil para hosts Linux, servidores BSD y dispositivos NAS que prefieren exponer bibliotecas de video sobre NFS en lugar de SMB. Selecciona NFS en el menú Conectar con almacenamiento en la nube, ingresa la dirección del servidor y la ruta exportada, y toca Hecho.

## Conectar un Plex Media Server

Evervideo puede conectarse directamente a un Plex Media Server y navegar por tus bibliotecas de Películas, Programas de TV y Videos Domésticos. Toca Conectar con almacenamiento en la nube → Plex, inicia sesión con tu cuenta Plex, elige un servidor, y la biblioteca aparece junto a tus servicios en la nube. Los servidores Plex en la misma red local también se descubren automáticamente en la sección Dispositivos disponibles.

## Conectar un Servidor Jellyfin o Emby

Tanto Jellyfin (código abierto) como Emby (comercial) funcionan nativamente en Evervideo. Toca Conectar con almacenamiento en la nube → Jellyfin o Emby, ingresa la URL de tu servidor (típicamente algo como `http://server-ip:8096`) y las credenciales, y tu biblioteca está lista para transmitir.

## Conectar un Servidor Subsonic o Navidrome

Evervideo habla la API de Subsonic, lo que significa que funciona con Subsonic, Navidrome y todos los demás servidores compatibles con Subsonic — incluyendo Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) y Ampache. Toca Conectar con almacenamiento en la nube → Subsonic, ingresa la URL del servidor y las credenciales, y la biblioteca aparece en la sección de Almacenamiento en la Nube.

## Conectar una Transmisión RTSP (Cámaras IP, TV en Vivo, IPTV)

Evervideo tiene soporte RTSP nativo, por lo que puedes apuntarlo a cualquier fuente RTSP — cámaras de seguridad, cámaras de timbre, proveedores IPTV, monitores de bebé, transmisiones de difusión — y Evervideo extraerá y decodificará la transmisión en vivo. Toca Enlaces en Línea → Agregar enlace, pega la URL completa (`rtsp://camera-ip:port/stream-path`), proporciona nombre de usuario y contraseña si es necesario, y toca Hecho.

## Conectar al Almacenamiento de Objetos Compatible con S3

Para usuarios que se alojan a sí mismos y usuarios avanzados que usan almacenamiento de objetos en la nube, Evervideo incluye un conector compatible con S3. Toca Conectar con almacenamiento en la nube → Almacenamiento S3, luego ingresa la URL del endpoint, región, clave de acceso, clave secreta y nombre del bucket. Esto funciona con AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces y cualquier otro endpoint de S3-API.

## Dispositivos Disponibles

Esta sección muestra cada dispositivo en tu red local al que puedes conectarte desde Evervideo mediante descubrimiento Bonjour / mDNS — Plex, Jellyfin, servidores Emby, Synology, QNAP, routers AirPort con unidades conectadas, Apple Time Capsule, etc. Para establecer una conexión:

- Desplázate a la sección Dispositivos disponibles en la pestaña Archivos.
- Toca el dispositivo al que quieres conectarte.
- Si es necesario, ingresa tus datos de inicio de sesión para completar la conexión.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Dispositivos Disponibles en la Red Local" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive te permite transferir archivos inalámbricamente desde tu ordenador a tu dispositivo iOS mediante cualquier navegador de escritorio, Finder o Explorador de archivos. Tu dispositivo y ordenador deben estar en la misma red Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Activar Wi-Fi Drive

- En la pestaña Archivos, desplázate a Almacenamiento en la Nube → Conectar vía Wi-Fi para abrir la pantalla principal de Wi-Fi Drive.
- (Opcional) Establece un nombre de usuario y contraseña para el servidor web integrado.
- Toca Iniciar Wi-Fi Drive.

### Acceder a Wi-Fi Drive en tu Ordenador

- Abre un navegador web en tu ordenador (Chrome, Firefox, Safari, etc.).
- Ingresa la URL que muestra la aplicación.
- Arrastra y suelta archivos desde tu ordenador en la página web — comenzarán a transferirse a tu dispositivo iOS.

También puedes montar Wi-Fi Drive directamente en **Finder** en macOS (Ir → Conectar al Servidor…) o en el Explorador de archivos en Windows (Conectar unidad de red…) y tratar tu iPhone o iPad como una unidad de red normal.

Las instrucciones detalladas están disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Compartición de Archivos de iTunes / Finder

La Compartición de Archivos de iTunes (ahora Compartición de Archivos de Finder en macOS Catalina y posteriores) te permite transferir archivos usando un cable Lightning o USB-C. Conecta el dispositivo, abre Finder en Mac (o iTunes en Windows), busca Evervideo en la lista de apps y copia archivos en su carpeta compartida.

## Conectar una Unidad Flash USB o Tarjeta SD

Conecta una unidad USB o tarjeta SD a tu iPhone, iPad o Mac mediante el adaptador Lightning a USB / USB-C o lector de tarjetas. Abre Archivos → Archivos en Este iPhone → Abrir Carpeta, navega a la unidad y elige un archivo de video o carpeta. Evervideo reproduce archivos directamente desde la unidad sin copiarlos al almacenamiento interno — práctico para bibliotecas 4K muy grandes.

## Navegación de Carpetas en Almacenamientos Conectados

Toca cualquier servicio en la nube conectado para abrir su navegador de archivos. Las carpetas muestran miniaturas de video cuando están disponibles, y tocar un video inicia la reproducción inmediatamente mientras continúa transmitiendo el resto del archivo en segundo plano.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Navegación de Carpetas en Almacenamientos Conectados" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Acceso Rápido

La sección de Acceso Rápido se encuentra en la parte superior de la pestaña Archivos. Te da acceso rápido a tus archivos y carpetas favoritas y abiertos recientemente — tanto de servicios en la nube como del almacenamiento del dispositivo. Siempre que abres un archivo o carpeta desde la nube, se añade a la lista de Abiertos Recientemente. Puedes marcar carpetas profundamente anidadas como Favoritos para acceder a ellas rápidamente sin navegar por la estructura de directorios.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Enlaces en Línea y Acceso Rápido" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Archivos en Esta Aplicación

Esta sección muestra archivos y carpetas almacenados en el directorio Documentos con sandbox de Evervideo — todo lo que has descargado de la nube, transferido vía Wi-Fi Drive, copiado a través de Compartición de Archivos de Finder, o importado desde otra app.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Archivos en Esta Aplicación" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Carpeta de Documentos

La carpeta de Documentos es la raíz de todo dentro de Archivos en Esta Aplicación. Puedes crear subcarpetas, renombrar archivos, moverlos y agruparlos como quieras.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Archivos Locales — Carpeta de Documentos" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Archivos en Este iPhone / iPad / Mac

Esta sección muestra videos ubicados en tu dispositivo pero en diferentes aplicaciones. Puedes importarlos a Evervideo usando el selector de archivos del sistema:

- Toca Abrir Archivos… para seleccionar archivos específicos.
- Toca Abrir Carpeta… para seleccionar una carpeta completa.

También puedes usar Conectar una Carpeta para crear un enlace a una carpeta en tu dispositivo con acceso de lectura / escritura — perfecto para trabajar con una carpeta en iCloud Drive o una unidad USB conectada sin copiar nada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Archivos en Este Dispositivo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Carpetas Especiales

Dentro de la pestaña Archivos verás varias carpetas especiales que Evervideo crea y usa automáticamente:

- **Descargas** — cada archivo descargado de la nube aparece aquí de forma predeterminada. Personaliza en Ajustes → Gestor de Archivos → Guardar Archivos Descargados En.
- **Caché del Reproductor** — la caché del reproductor multimedia. De forma predeterminada, el reproductor descarga los próximos videos para una reproducción fluida. Puedes desactivar la caché en la configuración de la app o simplemente eliminar esta carpeta.
- **iCloud** — los archivos en esta carpeta se sincronizan en todos tus dispositivos conectados a la misma cuenta de iCloud.
- **Carpetas sin conexión** — cuando marcas una carpeta, lista de reproducción, álbum o género como disponible sin conexión, los archivos se descargan en esta carpeta.

## Barra de Herramientas Superior

La barra de herramientas superior, ubicada debajo de la barra de navegación, ofrece varias acciones que puedes mostrar u ocultar con un gesto de deslizar hacia abajo:

- **Buscar** — realiza una búsqueda dentro de la carpeta o sección actual.
- **Continuar Reproducción** — si está activado en los ajustes, restaura la cola del reproductor y la última posición del video para la carpeta actual.
- **Reproducir Todo** — escanea la carpeta actual y sus subcarpetas y añade archivos a la cola del reproductor.
- **Reproducir Aleatoriamente** — como Reproducir Todo, pero mezcla antes de añadir.

## Opciones de Carpeta

Cuando abres una carpeta, toca el botón **"..."** en la esquina superior derecha para estas acciones:

- **Seleccionar** — activar el modo de selección de archivos.
- **Nueva Carpeta** — crea una nueva carpeta dentro de la carpeta actual.
- **Activar modo offline** — activa la sincronización sin conexión para la carpeta actual. Los nuevos archivos añadidos en línea se descargan automáticamente.
- **Subir Archivos** — sube archivos desde tu dispositivo a la carpeta en línea.
- **Buscar** — busca dentro de la carpeta.
- **Ordenar** — ordena archivos por nombre, tamaño, fecha de modificación o metadatos.
- **Vista de Cuadrícula / Lista** — alterna entre la vista de tabla y la vista de miniaturas. La vista de miniaturas muestra grandes previsualizaciones de pósters de video.

## Modo de Selección

Toca **"..."** en la esquina superior derecha y elige **Seleccionar** para entrar en el modo de selección. Aparecen casillas de verificación junto a cada archivo y carpeta. Toca para seleccionar uno o varios elementos, luego realiza acciones en lote: Reproducir Siguiente, Reproducir Más Tarde, Agregar a la Biblioteca Multimedia, Agregar a una Lista de Reproducción, Copiar, Subir, Mover, Renombrar o Eliminar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modo de Selección de Evervideo en el Gestor de Archivos" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Si prefieres tratar el almacenamiento en la nube conectado como de solo lectura (para evitar eliminaciones accidentales), activa Ajustes → Gestor de Archivos → Editar Archivos en Línea → Desactivado para ocultar todas las operaciones destructivas de la interfaz.

## Acciones de Archivos

Toca el icono **"..."** cerca del título de un archivo para revelar su menú de acciones:

- **Reproducir Siguiente** — inserta el archivo en la parte superior de la cola del reproductor.
- **Reproducir Más Tarde** — añade el archivo al final de la cola del reproductor.
- **Agregar a la Biblioteca Multimedia** — incorpora el archivo a tu biblioteca multimedia, organizada por Álbum y Género.
- **Agregar a una Lista de Reproducción** — añade el archivo a una lista de reproducción existente o crea una nueva.
- **Editar Etiquetas** — abre el editor de etiquetas integrado para modificar metadatos. Para archivos en línea, el archivo se descarga temporalmente, se edita y luego se vuelve a subir después de confirmar.
- **Agregar a Favoritos** — añade el archivo a tu lista de favoritos para acceso rápido.
- **Descargar** — descarga el archivo o carpeta a tu dispositivo para uso sin conexión.
- **Renombrar** — renombra el archivo directamente en el almacenamiento remoto.
- **Mover** — reubica el archivo en una carpeta diferente dentro de tu almacenamiento en la nube.
- **Agregar al Archivo** — agrupa el archivo en un único archivo ZIP (función Premium).
- **Abrir En** — exporta el archivo a otra app compatible a través de la hoja de Compartir del sistema.
- **Eliminar** — elimina permanentemente el archivo. **Esta acción no se puede deshacer.**

## Acciones de Carpeta

Para cada carpeta en tu almacenamiento en la nube, tienes muchas acciones disponibles tocando el icono **"..."** junto al título de la carpeta.

- **Reproducir Todo** — reemplaza la cola del reproductor actual con cada video de la carpeta.
- **Reproducir Siguiente / Reproducir Más Tarde** — añade la carpeta completa a la cola.
- **Agregar a la Biblioteca Multimedia** — incorpora el contenido de la carpeta a tu biblioteca multimedia.
- **Agregar a Lista de Reproducción** — añade la carpeta completa a una lista de reproducción.
- **Agregar a Favoritos** — añade la carpeta a tus favoritos.
- **Activar modo offline** — más allá de una simple descarga, esto monitorea continuamente la carpeta para nuevos archivos y los descarga automáticamente conforme aparecen en línea.
- **Descargar** — descarga todos los contenidos de la carpeta a tu dispositivo para acceso sin conexión.
- **Renombrar / Mover** — renombra o reubica la carpeta en el almacenamiento remoto.
- **Agregar al Archivo** — agrupa el contenido de la carpeta en un archivo ZIP (función Premium).
- **Eliminar** — elimina permanentemente la carpeta y sus contenidos. **Esta acción no se puede deshacer.**

## Cola de Transferencias

En la esquina superior derecha de la pestaña Archivos hay un botón de **Transferencias** (un icono de flechas giratorias). Tócalo para abrir la Cola de Transferencias — una lista de cada descarga y carga activa en todas tus fuentes, con progreso en tiempo real, velocidad y ETA por archivo.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cola de Transferencias de Archivos de Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Puedes pausar, reanudar, reintentar transferencias fallidas, reorganizar elementos para priorizar descargas específicas, o cancelarlos individualmente. También puedes ajustar la velocidad de la cola de transferencias (máximo de tareas paralelas), el tipo de red (solo Wi-Fi o Wi-Fi + datos móviles) y las transferencias en segundo plano en Ajustes → Gestor de Archivos.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Acciones en la Cola de Transferencias de Archivos" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Modo Sin Conexión y Carpetas Sin Conexión Sincronizadas

El modo sin conexión es una función útil que te permite ver tus videos favoritos incluso cuando no estás conectado a internet. Cuando activas el modo sin conexión para cualquier carpeta, lista de reproducción, álbum o género, todos los archivos dentro de esa colección se descargan automáticamente a tu dispositivo para reproducción sin conexión. Aparecen en la sección Carpetas sin conexión.

Cuando añades nuevos archivos al servidor remoto, también se descargan automáticamente — para que tu colección sin conexión se mantenga actualizada sin que tengas que hacer nada. Para re-sincronizar manualmente, toca los tres puntos en la esquina superior derecha de una carpeta sin conexión y selecciona Sincronizar.

Puedes ajustar el tiempo de espera de sincronización en Ajustes → Gestor de Archivos → Carpetas offline sincronizadas → Intervalo de Tiempo.

Las instrucciones detalladas están disponibles [aquí](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalización

En Ajustes → Personalización puedes configurar cómo se presenta la pestaña Archivos:

- **Estilo de la Pantalla de Archivos** — Menú Simple (muestra la lista de carpetas directamente) o Menú Agrupado (agrupa el contenido por categoría — Acceso Rápido, Carpetas Especiales, Almacenamiento en la Nube, etc.).
