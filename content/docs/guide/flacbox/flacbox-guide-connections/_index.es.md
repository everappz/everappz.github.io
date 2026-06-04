---
title: "Conexiones"
date: 2020-02-01
description: "Aprende a conectar servicios en la nube y dispositivos NAS a Flacbox. Transmite música de alta resolución desde iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk y más. Usa SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing y unidades flash USB."
keywords: [
  "configuración cloud Flacbox", "conectar Google Drive a Flacbox", "streaming de música SMB",
  "reproductor WebDAV iOS", "app de música DLNA", "streaming de audio NAS", "Wi-Fi Drive iPhone",
  "transferir archivos al iPhone", "Flacbox iTunes File Sharing", "conectar NAS al iPhone",
  "app de música Synology Drive", "app de música QNAP", "app de música Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "app de música scrobbling Last.fm",
  "música iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["guía", "flacbox", "conexiones", "cloud", "NAS"]
readingTime: 12
---


En esta pantalla, puedes conectar cada fuente que contiene tu música. Puedes integrar servicios en la nube populares como Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive y muchos más, así como tu Mac, PC o NAS mediante protocolos estándar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Conexiones de Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Conectar al Almacenamiento en la Nube

- Abre la pestaña **Conexiones**.
- Selecciona **Conectar al almacenamiento en la nube** del menú.
- Elige un servicio de almacenamiento en la nube de la lista.
- Introduce tus credenciales en la página de autorización oficial del proveedor de la nube y luego pulsa **Hecho**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Añadir un Servicio de Almacenamiento en la Nube" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Si encuentras algún problema, verifica tu conexión a internet y tu login / contraseña. En la versión Premium puedes añadir servicios ilimitados; la versión gratuita admite hasta tres.

## Servicios de Almacenamiento en la Nube, Servidores de Medios y Protocolos Compatibles

Flacbox admite una gama excepcionalmente amplia de fuentes para tu música.

**Almacenamiento personal en la nube:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidores autohospedados:** Plex · Jellyfin · Emby · Subsonic (y cada servidor compatible — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (y ownCloud mediante la API compartida) · Synology Drive · QNAP.

**Protocolos NAS y de uso compartido de archivos:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, contraseña o autenticación por clave pública) · NFS · DLNA / UPnP (reproducción y descarga).

**Almacenamiento de objetos compatible con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces y cualquier otro endpoint de S3-API.

**Descubrimiento de red local:** La sección «Dispositivos disponibles» lista automáticamente cada servicio Bonjour / mDNS en tu red Wi-Fi.

## Seguridad y Privacidad

Usamos únicamente SDKs oficiales y conexiones seguras para interactuar con los servicios de nube conectados. Tu login y contraseña no son accesibles para la aplicación — todas las transferencias están cifradas con TLS.

Un auth-token se almacena en tu dispositivo en el almacenamiento seguro del sistema de Apple (Keychain).

La aplicación no comparte ninguna información de tus cuentas de nube conectadas con Everappz, anunciantes ni terceros.

## Revocar Auth-Token

Para revocar un auth-token, inicia sesión en tu cuenta de nube en un navegador web y navega a la página de seguridad o aplicaciones conectadas. Las instrucciones detalladas para cuentas de Google están disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

## Desconectar un Almacenamiento en la Nube o Cambiar la Configuración

- **Acceder a las opciones del almacenamiento en la nube** — localiza el servicio conectado en la pantalla **Conexiones**.
- **Pulsa el botón "..."** junto al título del servicio:
  - **Renombrar** — cambia el nombre del servicio de nube.
  - **Ajustes** — modifica la configuración o los datos de autenticación.
  - **Desconectar** — desconecta completamente la app del servicio de nube.

## Conectar a un Ordenador o NAS

También puedes conectar tu ordenador, un NAS personal u otros dispositivos de red usando los protocolos SMB, DLNA o WebDAV.

## Conectar a un Ordenador Usando SMB

- Pulsa **Conectar al almacenamiento en la nube → SMB**.
- Introduce la dirección IP del ordenador y el nombre de la carpeta compartida en el campo URL: `smb://dirección-ip-ordenador/carpeta-compartida`.
- Elige la versión del protocolo: **Auto**, **SMB1** o **SMB2**.
- Introduce tu login y contraseña (si es necesario).
- Pulsa **Hecho**.

Un tutorial completo está disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Conectar a un NAS Usando WebDAV

Todos los pasos son iguales que en SMB, excepto el campo URL. La URL debe estar en el formato `http://nombre-servidor` o `https://nombre-servidor`. WebDAV funciona con **Synology, QNAP, Nextcloud, ownCloud** y muchos otros servidores.

Un tutorial completo está disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Conectar a un Ordenador o NAS Usando DLNA

También puedes compartir una biblioteca de música usando el protocolo DLNA / UPnP, como se describe [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone).

## Conectar a un NAS o Servidor Usando FTP, FTPS o SFTP

Pulsa **Conectar al almacenamiento en la nube → FTP**, introduce la URL del host en el formato `ftp://nombre-servidor` (o `ftps://nombre-servidor`), proporciona tu login y contraseña y pulsa **Hecho**. Para **SFTP** elige **SFTP** y proporciona una contraseña o un par de claves SSH.

## Conectar a un Recurso Compartido NFS

Flacbox incluye soporte **NFS** (Network File System). Elige **NFS** en el menú **Conectar al almacenamiento en la nube**, introduce la dirección del servidor y la ruta exportada y pulsa **Hecho**.

## Conectar un Plex Media Server

Pulsa **Conectar al almacenamiento en la nube → Plex**, inicia sesión con tu cuenta Plex, elige un servidor y la biblioteca aparece junto a tus servicios de nube.

## Conectar un Servidor Jellyfin o Emby

Pulsa **Conectar al almacenamiento en la nube → Jellyfin** o **Emby**, introduce la URL de tu servidor y las credenciales, y tu biblioteca musical estará lista para reproducirse.

## Conectar un Servidor Subsonic o Navidrome

Pulsa **Conectar al almacenamiento en la nube → Subsonic**, introduce la URL del servidor y las credenciales y la biblioteca aparece en la pantalla Conexiones.

## Conectar al Almacenamiento de Objetos Compatible con S3

Pulsa **Conectar al almacenamiento en la nube → Almacenamiento S3**, luego introduce la URL del endpoint, región, clave de acceso, clave secreta y nombre del bucket.

## Dispositivos Disponibles

Esta sección muestra cada dispositivo en tu red local que puedes conectar mediante descubrimiento Bonjour.

- Abre la app y ve a la sección **Dispositivos disponibles** en Conexiones.
- Pulsa el dispositivo al que quieres conectarte.
- Si es necesario, introduce tus datos de inicio de sesión.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Dispositivos Disponibles en la Red Local" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive es una tecnología conveniente que permite transferencias inalámbricas de archivos desde tu ordenador a tu dispositivo iOS mediante cualquier navegador de escritorio.

### Activar Wi-Fi Drive

- Abre la aplicación y ve a la pestaña **Conexiones**.
- Selecciona **Conectar vía Wi-Fi** para acceder a la pantalla principal de Wi-Fi Drive.
- (Opcional) Establece un nombre de usuario y contraseña para el servidor web integrado.
- Pulsa **Iniciar Wi-Fi Drive**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Acceder a Wi-Fi Drive desde tu Ordenador

- Abre un navegador web (Chrome, Firefox o Safari).
- En la barra de direcciones, introduce la URL proporcionada por la aplicación.

### Transferir Archivos de Forma Inalámbrica

Una vez que la página web de tu dispositivo iOS se abra en el navegador, puedes arrastrar y soltar archivos desde tu ordenador.

También puedes montar Wi-Fi Drive directamente en Finder en macOS (Ir → Conectarse al servidor…) o en el Explorador de archivos en Windows (Conectar unidad de red…).

Instrucciones detalladas disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (ahora Finder File Sharing en macOS Catalina y versiones posteriores) es otra forma de transferir archivos usando un cable Lightning o USB-C.

- Conecta el dispositivo al ordenador usando un cable y ejecuta **Finder** en Mac (o **iTunes** en Windows).
- Abre **Ubicaciones → Tu dispositivo conectado → Archivos** y encuentra la app Flacbox.
- Pulsa el icono de la app para ver todas las carpetas compartidas.
- Copia archivos arrastrando y soltando.

Instrucciones detalladas disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Conectar una Unidad Flash USB

Si tienes una tarjeta SD o unidad USB, puedes conectarla usando un lector de tarjetas SD Lightning a USB o una unidad USB-C (en iPad y iPhone 15 / 16 / 17 / Pro).

Instrucciones detalladas disponibles [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de Archivos

Una vez conectado un servicio de almacenamiento en la nube, pulsa su icono para ver todos los archivos y carpetas disponibles.

## Barra de Herramientas Superior

La barra de herramientas superior ofrece varias acciones útiles.

- **Buscar** — realiza una búsqueda rápida en el directorio actual.
- **Continuar Reproducción** — restaura la cola del reproductor de audio y la última posición para la carpeta actual.
- **Reproducir Todo** — escanea la carpeta actual y sus subcarpetas y añade todos los archivos de audio a una nueva cola.
- **Reproducir Todo en Orden Aleatorio** — como Reproducir Todo, pero mezcla los archivos antes de añadirlos.

## Opciones de Carpeta

Al abrir una carpeta, encontrarás acciones disponibles pulsando el botón **"..."** en la esquina superior derecha.

- **Seleccionar** — activar el modo de selección de archivos.
- **Nueva Carpeta** — crear una nueva carpeta.
- **Activar modo offline** — activar el modo sin conexión para la carpeta actual.
- **Subir Archivos** — subir archivos desde tu dispositivo a la carpeta online.
- **Buscar** — buscar archivos específicos.
- **Ordenar** — ordenar archivos por nombre, tamaño, fecha de modificación o metadatos.
- **Cuadrícula / Lista** — cambiar entre vista de tabla y vista en miniatura.

## Editar Archivos Online

Para gestionar varios archivos, usa el **Modo de Selección**:

- **Activar Modo de Selección** — pulsa **"..."** en la esquina superior derecha y elige **Seleccionar**.
- **Elegir Archivos** — aparecen casillas de verificación junto a cada archivo.
- **Realizar Acciones** — Reproducir Siguiente, Reproducir Después, Añadir a la Biblioteca Musical, Añadir a una Lista de Reproducción, Copiar, Subir, Mover, Renombrar y Eliminar.

## Acciones de Archivo

Pulsa el icono **"..."** junto al título de un archivo para revelar el menú de acciones:

- **Reproducir Siguiente** — insertar el archivo en la parte superior de la cola.
- **Reproducir Después** — añadir el archivo al final de la cola.
- **Añadir a la Biblioteca Musical** — incorporar el archivo a tu biblioteca musical.
- **Añadir a una Lista de Reproducción** — añadir a una lista existente o crear una nueva.
- **Editar etiquetas de audio** — abrir el editor de etiquetas integrado.
- **Añadir a Favoritos** — añadir a tu lista de favoritos.
- **Descargar** — descargar el archivo o carpeta para uso sin conexión.
- **Renombrar** — renombrar el archivo directamente en el almacenamiento remoto.
- **Mover** — reubicar el archivo en otra carpeta.
- **Abrir En** — exportar el archivo a otra app compatible.
- **Eliminar** — eliminar permanentemente el archivo. **Esta acción no se puede deshacer.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Más Acciones para un Archivo en el Almacenamiento Cloud Conectado" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

## Acciones de Carpeta

Para cada carpeta, pulsa el icono **"..."** junto al título:

- **Reproducir Todo** — reemplazar la cola actual con todos los elementos.
- **Reproducir Siguiente** — añadir la carpeta entera a la parte superior de la cola.
- **Reproducir Después** — añadir el contenido al final de la cola.
- **Añadir a la Biblioteca Musical** — incorporar el contenido de la carpeta.
- **Añadir a Lista de Reproducción** — añadir la carpeta entera a una lista.
- **Añadir a Favoritos** — añadir la carpeta a favoritos.
- **Activar modo offline** — supervisar continuamente la carpeta para nuevos archivos.
- **Descargar** — descargar todos los contenidos.
- **Renombrar** — renombrar la carpeta.
- **Mover** — reubicar en otra ubicación.
- **Archivar (ZIP)** — comprimir el contenido en un archivo ZIP (función Premium).
- **Eliminar** — eliminar permanentemente. **Esta acción no se puede deshacer.**

## Acceso Rápido

La sección de Acceso Rápido está ubicada en la parte superior de la pantalla y te da acceso rápido a tus archivos favoritos y abiertos recientemente.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Enlaces Online y Acceso Rápido" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Otros Servicios

Esta sección muestra funciones adicionales. Actualmente, la app admite scrobbling de **Last.fm** — cuando está conectado, tus estadísticas de reproducción se envían automáticamente a tu cuenta Last.fm. Las instrucciones detalladas de configuración están disponibles [aquí](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Conectar Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
