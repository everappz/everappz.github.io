---
title: "Conexiones"
date: 2020-01-01
description: "Aprende a conectar servicios en la nube, ordenadores, dispositivos NAS y a gestionar tus archivos de música con Evermusic. Guía paso a paso para Wi-Fi Drive, SMB, DLNA, WebDAV, uso compartido de archivos de iTunes y más."
keywords: [
  "Evermusic", "reproductor de música en la nube", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "uso compartido de archivos iTunes",
  "conectar almacenamiento en la nube", "transferencia de música iPhone", "gestor de archivos iOS"
]
tags: ["evermusic", "guía", "conexiones"]
readingTime: 11
---


En la pantalla de Conexiones puedes conectar cada fuente que contiene tu música — servicios en la nube populares, servidores multimedia autohospedados, tu Mac o PC, un NAS personal, Apple Time Capsule, WD My Cloud Home, incluso una unidad flash USB — y usarlos todos desde una interfaz unificada. Conexiones es también donde configuras el Acceso rápido a carpetas de nube profundamente anidadas y donde autentificas Last.fm para el scrobbling.

La pantalla está dividida en secciones claramente etiquetadas: Acceso rápido en la parte superior (tus carpetas de nube favoritas), Almacenamiento en la nube (las cuentas que has añadido), Red local (dispositivos descubiertos por Bonjour), Ordenador (Wi-Fi Drive, uso compartido de archivos iTunes, SMB), Accesorios externos (unidades flash USB conectadas) y Otros servicios (Last.fm y similares).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Conexiones de Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Conectar al almacenamiento en la nube

- Abre la pestaña Conexiones.
- Selecciona 'Conectar al almacenamiento en la nube' del menú.
- Elige un servicio de almacenamiento en la nube de la lista.
- Inicia sesión en la página de autorización oficial del proveedor (Evermusic nunca ve tu contraseña).
- Pulsa Hecho.

{{< cards cols="1">}}
  {{< card title="" subtitle="Selector de proveedor de almacenamiento en la nube" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Si encuentras algún problema, verifica tu conexión a internet y credenciales de acceso, y asegúrate de que la autenticación de dos factores esté correctamente configurada para ese servicio.  
En la versión Premium de la app puedes añadir un número ilimitado de servicios. Los usuarios gratuitos pueden conectar una sola cuenta en la nube a la vez.

## Servicios de almacenamiento en la nube compatibles

Evermusic es compatible con toda la gama de servicios populares en la nube y autohospedados. Los usuarios gratuitos obtienen el mismo catálogo de proveedores pero con el límite de una cuenta; Premium desbloquea cuentas ilimitadas y elimina la mayoría de los demás límites.

- **Cuentas personales en la nube:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidores autohospedados y bibliotecas multimedia:** Plex · Jellyfin · Emby · Subsonic (y todo servidor compatible con Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (y Owncloud mediante la API compartida) · Synology Drive · QNAP.
- **NAS y protocolos de uso compartido de archivos:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (contraseña o autenticación de clave pública), NFS y DLNA (solo lectura — reproducción y descarga).
- **Almacenamiento de objetos compatible con S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage o cualquier endpoint S3-API.
- **Descubrimiento en red local:** la sección 'Dispositivos disponibles' lista automáticamente cualquier dispositivo en tu Wi-Fi que se anuncie mediante Bonjour / mDNS — Plex, Jellyfin, servidores Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routers AirPort con unidades conectadas, etc.

## Seguridad y privacidad

Utilizamos solo el SDK oficial y una conexión segura para interactuar con los servicios en la nube conectados. Tu nombre de usuario y contraseña no están disponibles para la aplicación. Todas las solicitudes de la aplicación al servicio en la nube están cifradas.

Cuando introduces tu usuario y contraseña, la aplicación te muestra la página de autorización oficial del proveedor del servicio en la nube y todo el proceso de autorización se realiza fuera de la aplicación. El proveedor del servicio en la nube envía un token de autenticación a la aplicación tras una autorización exitosa, y ese token se utiliza para realizar llamadas a la API.

El token de autenticación es una clave digital que permite a aplicaciones de terceros interactuar con el almacenamiento en la nube. Se almacena en tu dispositivo en un almacenamiento seguro del sistema llamado Keychain. Puedes descargar tus archivos del servicio en la nube conectado al dispositivo y esos archivos se ubicarán en el directorio 'Documentos' de la aplicación. Puedes eliminar esos archivos en cualquier momento usando el gestor de archivos integrado.

La aplicación no comparte ninguna información de la cuenta en la nube conectada. Puedes revocar el acceso a tu cuenta en la nube en cualquier momento abriendo la página de configuración de la cuenta en tu navegador web.

## Rechazar el token de autenticación

Inicia sesión en tu cuenta en el navegador web y navega a la página de configuración. Allí puedes encontrar todas las aplicaciones de terceros conectadas a tu cuenta en la nube y eliminar cualquiera de ellas si ya no quieres usar esa aplicación. Instrucciones detalladas disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

También puedes desconectar las cuentas en la nube conectadas en la aplicación y el token de autenticación también se eliminará de tu dispositivo. Si eliminas la aplicación de tu dispositivo, también se eliminarán todos los datos descargados y los tokens de acceso.

## Desconectar un almacenamiento en la nube o cambiar la configuración

- Accede a las Opciones de Almacenamiento en la Nube: primero localiza el almacenamiento en la nube que deseas gestionar en la interfaz de la aplicación.
- Pulsa el botón '...': junto al título del servicio verás un botón '...'. Púlsalo para acceder a opciones adicionales.
  - **Renombrar**: si quieres cambiar el nombre del servicio en la nube tal como aparece en tu lista, selecciona 'Renombrar'.
  - **Ajustes**: para modificar la configuración o los datos de autenticación del servicio en la nube, elige 'Ajustes'. A veces puede que necesites volver a autorizar el servicio en la nube conectado si el token de autorización ha caducado.
  - **Desconectar**: si deseas desconectar completamente la conexión entre la app y el servicio en la nube, selecciona 'Desconectar'. Ten en cuenta que al elegir esta opción se eliminarán todas las canciones asociadas a este servicio en la nube de la biblioteca de música de la app, pero permanecerán en el servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú Más acciones para el almacenamiento en la nube conectado" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Conectar a un Ordenador o NAS

También puedes conectar tu ordenador, NAS personal u otros dispositivos de red usando el protocolo SMB, DLNA o WebDAV.

## Conectar al ordenador usando SMB

- Pulsa 'Conectar al almacenamiento en la nube' → SMB.
- Introduce la dirección IP del ordenador y el nombre de la carpeta compartida en el campo URL con el formato smb://dirección-ip-ordenador/nombre-carpeta-compartida
- Elige la versión del protocolo: Auto, SMB1, SMB2
- Introduce el usuario y la contraseña (si es necesario)
- Pulsa 'Hecho'.

Si la conexión tiene éxito, verás el almacenamiento conectado en la sección 'Almacenamiento en la nube'.  
Un tutorial completo sobre cómo conectar tu Mac o PC usando SMB está disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuración de conexión SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Conectar al NAS usando WebDAV

Todos los pasos son los mismos excepto en el campo URL.  
El URL debe tener el formato http://nombre-servidor, o https://nombre-servidor si el servidor admite SSL.
Un tutorial completo sobre cómo conectar NAS usando el protocolo WebDAV está disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuración de conexión WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Conectar al Ordenador o NAS usando DLNA

También puedes compartir una biblioteca de música ubicada en tu Windows PC o NAS personal usando el protocolo DLNA y acceder a esa biblioteca en la app como se describe [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA es un protocolo popular y ampliamente usado, pero solo te permite reproducir o descargar música. No puedes subir archivos ni crear nuevas carpetas en el servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuración de conexión DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dispositivos disponibles

Esta sección muestra todos los dispositivos dentro de tu red local a los que puedes conectarte a través de la aplicación.  
Para establecer una conexión con un dispositivo, sigue estos pasos:

- Abre la app y ve a la sección 'Dispositivos disponibles'.
- Pulsa el dispositivo al que quieres conectarte desde la lista.
- Si es necesario, introduce tus datos de acceso para completar la conexión.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositivos disponibles en la red local" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive es una conveniente tecnología que permite transferencias inalámbricas de archivos desde tu ordenador a tu dispositivo iOS a través de un navegador de escritorio.  
Para usar esta función eficazmente, asegúrate de que tu dispositivo y ordenador estén conectados a la misma red Wi-Fi.  
Aquí tienes una guía paso a paso sobre cómo usar Wi-Fi Drive.

## Activar Wi-Fi Drive

- Abre la aplicación y ve a la pestaña 'Conexiones'.
- Selecciona 'Conectar por Wi-Fi' para acceder a la pantalla principal de Wi-Fi Drive.
- Pulsa 'Iniciar Wi-Fi Drive' para activar Wi-Fi Drive.

## Acceder a Wi-Fi Drive en tu Ordenador

- En tu ordenador (de escritorio o portátil), abre un navegador web (como Chrome, Firefox o Safari).
- En la barra de direcciones del navegador, introduce la URL proporcionada por la aplicación.

## Transferir Archivos Inalámbricamente

Una vez que se abra la página web correspondiente a tu dispositivo iOS en el navegador, puedes arrastrar y soltar fácilmente archivos desde tu ordenador a la página web.  
Los archivos que arrastres y sueltes comenzarán a transferirse a tu dispositivo iOS y serán accesibles dentro de la aplicación.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuración del servidor Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Instrucciones detalladas sobre cómo transferir archivos de forma inalámbrica con WiFi-Drive están disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Uso compartido de archivos de iTunes

El uso compartido de archivos de iTunes es otra tecnología que te permite transferir archivos desde el ordenador al dispositivo usando la app Finder en tu Mac y un cable Lightning.  
- Simplemente conecta un dispositivo al ordenador usando un cable y ejecuta la app Finder en tu Mac.
- Abre 'Ubicaciones' → 'Tu dispositivo conectado' → 'Archivos' → y encuentra la app Evermusic.
- Pulsa el icono de la app para ver todas las carpetas compartidas.
- Copia archivos del ordenador a la carpeta compartida en el dispositivo usando arrastrar y soltar.

Instrucciones detalladas sobre cómo usar el uso compartido de archivos de iTunes están disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Uso compartido de archivos iTunes / Finder en Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Conectar una tarjeta flash USB

Si tienes una tarjeta SD, puedes conectarla usando un lector de tarjetas lightning. La app actualmente es compatible con lectores de tarjetas certificados por Apple e iXpand Flash Drives. Si tienes un iXpand Flash Drive, insértalo en el puerto lightning y abre la aplicación. Verás un mensaje 'Dispositivo externo conectado' e información del dispositivo. Simplemente pulsa en el icono de la unidad flash para acceder a la carpeta de música y pulsa en cualquier archivo de audio para comenzar a reproducir. Instrucciones detalladas sobre cómo conectar una tarjeta flash USB al iPhone están disponibles [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de Archivos

Una vez que hayas conectado un servicio de almacenamiento en la nube, pulsa su icono para ver todos los archivos y carpetas disponibles. Puedes usar el gestor de archivos integrado para trabajar con estos archivos — descargar, renombrar, mover y más. Cuando inicias una descarga, el archivo aparecerá en la cola de transferencia. Para ver la cola de transferencia, ve a la pestaña 'Archivos locales' y pulsa las flechas giratorias en la esquina superior izquierda. Todos los archivos y carpetas descargados están disponibles en la sección 'Archivos locales'.

## Barra de Herramientas Superior

La barra de herramientas superior, ubicada convenientemente bajo la barra de navegación, ofrece varias acciones útiles. Puedes mostrar u ocultar esta barra con un gesto de deslizamiento hacia abajo. Estas son las acciones disponibles:

- **Buscar**: Esta opción te permite realizar una búsqueda rápida dentro del directorio actual para localizar archivos o carpetas específicos.
- **Continuar reproducción**: Si está habilitada en la configuración de la aplicación, esta función restaura la cola del reproductor de audio y la última posición de medios para la carpeta actual.
- **Reproducir todo**: Al seleccionar esta acción, la app escaneará la carpeta actual y sus subcarpetas, añadiendo todos los archivos de audio encontrados a una nueva cola del reproductor.
- **Reproducción aleatoria**: Similar a 'Reproducir todo', esta acción escanea la carpeta actual y sus subcarpetas pero mezcla los archivos antes de añadirlos a la cola del reproductor de audio.

{{< cards cols="1">}}
  {{< card title="" subtitle="Barra de herramientas superior dentro de una carpeta en la nube" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opciones de Carpeta

Cuando abres una carpeta dentro de la app, encontrarás un conjunto de acciones disponibles pulsando el botón '...' en la esquina superior derecha de la pantalla.  
Aquí tienes un desglose de estas acciones:

- **Seleccionar**: Activa el modo de selección de archivos. Este modo te permite elegir uno o más archivos dentro de la carpeta.
- **Nueva Carpeta**: Crea una nueva carpeta dentro de la carpeta actual.
- **Activar modo offline**: Activa el modo sin conexión para la carpeta actual. El modo sin conexión va más allá de la simple descarga; monitoriza activamente la carpeta para detectar cambios. Si añades nuevos archivos a la carpeta en línea, la app los descargará automáticamente a tu dispositivo.
- **Subir Archivos**: Sube archivos desde tu dispositivo a la carpeta en línea.
- **Buscar**: Busca archivos específicos dentro de la carpeta actual.
- **Ordenar**: Ordena archivos dentro de la carpeta por criterios como nombre, tamaño o fecha de edición.
- **Vista cuadrícula/lista**: Cambia entre dos modos de visualización: vista de tabla y vista de miniaturas.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú Más acciones para la carpeta actual" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Editar Archivos en Línea

Cuando necesitas gestionar varios archivos en tu almacenamiento en la nube en Evermusic, puedes usar el modo de selección. Sigue estos pasos:

- **Activar Modo de Selección**: Abre la app en tu dispositivo y navega a la sección que contiene tu almacenamiento en la nube. Busca el botón '...' (puntos suspensivos) en la esquina superior derecha. Púlsalo y elige 'Seleccionar' para activar el modo de selección.
- **Elegir Archivos**: Verás casillas de verificación junto a cada archivo o carpeta. Elige uno o varios archivos o carpetas simplemente pulsando en las casillas.
- **Realizar Varias Acciones**: Una vez hayas seleccionado los archivos o carpetas que quieres gestionar, tendrás acceso a varias acciones.

{{< cards cols="1">}}
  {{< card title="" subtitle="Modo de selección para archivos en línea" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Acciones de archivo

Junto al título del archivo, verás el símbolo de puntos suspensivos '...' (tres puntos) — este es el menú de acciones.  
Púlsalo para revelar la lista de acciones disponibles:

- **Reproducir a continuación**: Inserta el archivo elegido en la parte superior de tu cola del reproductor.
- **Reproducir después**: Añade el archivo al final de tu cola del reproductor.
- **Añadir a la Biblioteca de Música**: Esta acción te permite incorporar el archivo a tu biblioteca de música, organizado ordenadamente por artista, álbum, género o compositor.
- **Añadir a una Lista de Reproducción**: Usa esta acción para añadir el archivo a una lista de reproducción existente o crear una nueva.
- **Editar etiquetas de audio**: Al seleccionar esta opción, puedes acceder al editor de etiquetas integrado de Evermusic. El archivo se descargará temporalmente y luego se subirá al almacenamiento después de confirmar los cambios.
- **Añadir a Favoritos**: Esta acción añade el archivo a tu lista de archivos favoritos.
- **Descargar**: Elige esta acción para descargar el archivo o carpeta a tu dispositivo.
- **Renombrar**: Esta opción te permite renombrar el archivo directamente en el almacenamiento remoto.
- **Mover**: Elige esta acción para reubicar el archivo en una carpeta diferente dentro de tu almacenamiento en la nube.
- **Abrir con**: Usa esta acción para exportar el archivo a otra app compatible.
- **Eliminar**: Ten cuidado con esta acción, ya que elimina permanentemente el archivo de tu almacenamiento en la nube. Esta eliminación no se puede deshacer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú Más acciones para un archivo individual" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Si la lista de acciones supera el espacio de pantalla disponible, simplemente desplázate hacia abajo dentro del menú de acciones.

## Acciones de carpeta

Para cada carpeta en tu almacenamiento en la nube, tienes varias acciones disponibles. Para acceder a estas opciones, simplemente pulsa el icono de puntos suspensivos '...' ubicado junto al título de la carpeta. Las acciones disponibles son:

- **Reproducir todo**: Reemplaza la cola del reproductor actual con todos los elementos de la carpeta seleccionada.
- **Reproducir a continuación**: Añade la carpeta completa a la parte superior de la cola del reproductor.
- **Reproducir después**: Añade el contenido de la carpeta al final de la cola del reproductor.
- **Añadir a la Biblioteca de Música**: Esta acción incorpora perfectamente el contenido de la carpeta a tu biblioteca de música.
- **Añadir a Lista de Reproducción**: Puedes incluir la carpeta completa en una lista de reproducción, asignándose automáticamente el nombre de la carpeta.
- **Añadir a Favoritos**: Usa esta acción para añadir la carpeta a tu lista de archivos favoritos.
- **Activar modo offline**: Al activar el modo sin conexión, la aplicación escanea continuamente para detectar cambios y los nuevos archivos se descargan automáticamente.
- **Descargar**: Descarga todo el contenido de la carpeta a tu dispositivo para acceso sin conexión.
- **Renombrar**: Renombra la carpeta directamente en el almacenamiento remoto.
- **Mover**: Reubica la carpeta en una ubicación diferente dentro de tu almacenamiento en la nube.
- **Eliminar**: Ten precaución ya que esta acción elimina permanentemente la carpeta y su contenido. Esta acción no se puede deshacer.


## Acceso Rápido

La sección de Acceso Rápido está ubicada en la parte superior de la pantalla. Te da acceso rápido a tus carpetas favoritas y archivos abiertos recientemente de los servicios en la nube conectados.
Siempre que abres un archivo o carpeta de la nube, se añade a la lista 'Abiertos recientemente'. Para borrar esta lista, abre 'Recientes', pulsa el botón 'Más acciones' y elige 'Eliminar lista'. También puedes marcar carpetas profundamente anidadas como Favoritas para acceder a ellas rápidamente sin navegar por la estructura de directorios.

## Otros Servicios

Esta sección muestra funciones adicionales. Actualmente, la app es compatible con el scrobbling de Last.fm. Cuando está conectado, tus estadísticas de reproducción se envían automáticamente a tu cuenta de Last.fm. Puedes visitar tu perfil de Last.fm más tarde para ver análisis de escucha y obtener recomendaciones musicales personalizadas. Las instrucciones de configuración detalladas están disponibles [aquí](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
