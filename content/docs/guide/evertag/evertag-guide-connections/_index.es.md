---
title: "Conexiones"
date: 2020-02-01
description: "Aprende a conectar almacenamiento en la nube, NAS y tu computadora a Evertag. Accede y edita archivos de audio directamente desde almacenamiento en la nube, NAS personal o Mac/PC."
keywords: [
  "configuración cloud Evertag", "conectar iCloud a Evertag", "acceso a archivos SMB iOS",
  "editor de etiquetas de audio WebDAV", "edición de metadatos NAS", "Wi-Fi Drive Evertag",
  "transferir archivos de audio a iPhone", "Evertag iTunes File Sharing", "editar etiquetas FLAC desde la nube"
]
tags: ["guía", "evertag", "conexiones"]
readingTime: 11
---


En esta pantalla, puedes conectar varias fuentes que contienen tus archivos de audio. Puedes integrar servicios de nube populares como Google Drive, Dropbox, OneDrive, iCloud y otros, así como conectar tu Mac o PC. Además, tienes la opción de editar archivos de audio ubicados en Apple Time Capsule, WD Cloud Home o cualquier NAS que hable SMB o WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Connections Screen" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Acceso rápido

En la parte superior de la pantalla Conexiones encontrarás una lista de **Acceso rápido**. Cualquier carpeta en la nube que agregues a favoritos — incluso una enterrada varios niveles de profundidad — aparece aquí para que puedas acceder a ella sin navegar por las carpetas principales cada vez.

## Conectar a almacenamiento en la nube

- Abre la pestaña «Conexiones»
- Selecciona «Conectar a almacenamiento en la nube» del menú
- Elige un servicio de almacenamiento en la nube de la lista
- Ingresa tus credenciales y toca «Hecho».

Si encuentras algún problema, asegúrate de revisar tu conexión a internet y nombre de usuario/contraseña.
En la versión Premium de la app, puedes añadir un número ilimitado de servicios.

## Servicios de almacenamiento en la nube compatibles

Actualmente, la aplicación es compatible con los servicios de almacenamiento en la nube más populares: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), así como cualquier servidor SMB o WebDAV.

## Seguridad y privacidad

Usamos solo SDKs oficiales y conexiones seguras para interactuar con los servicios de nube conectados. Tu nombre de usuario y contraseña no son accesibles para la aplicación. Todas las solicitudes de la aplicación al servicio en la nube están cifradas.

Cuando introduces tu nombre de usuario y contraseña, la aplicación te muestra la página de autorización oficial proporcionada por el proveedor del servicio en la nube, y todo el proceso de autorización ocurre fuera de la aplicación. El proveedor del servicio en la nube envía un token de autenticación a la aplicación tras la autorización exitosa, y ese token se usa para hacer llamadas a la API.

Un token de autenticación es una clave digital que permite que aplicaciones de terceros interactúen con el almacenamiento en la nube. El token de autenticación se almacena en tu dispositivo en un almacenamiento seguro del sistema llamado Keychain. Puedes descargar tus archivos del servicio de nube conectado al dispositivo, y esos archivos se colocarán en el directorio «Documents» de la app. Puedes eliminar esos archivos en cualquier momento usando el gestor de archivos integrado.

La aplicación no comparte ninguna información de la cuenta de nube conectada. Puedes revocar el acceso a tu cuenta de nube en cualquier momento abriendo la página de configuración de la cuenta en tu navegador web.

## Revocar token de autenticación

Inicia sesión en tu cuenta en un navegador web y navega a la página de configuración. Allí puedes encontrar todas las aplicaciones de terceros que están conectadas a tu cuenta de nube y eliminar cualquiera de ellas si ya no quieres usar esa aplicación. Las instrucciones detalladas están disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

También puedes desconectar las cuentas de nube conectadas en la aplicación, y el token de autenticación también se eliminará de tu dispositivo. Si eliminas la aplicación de tu dispositivo, todos los datos descargados y los tokens de acceso también se eliminarán.

## Desconectar un almacenamiento en la nube o cambiar la configuración

- Acceder a las Opciones de Almacenamiento en la Nube: Primero, localiza el almacenamiento en la nube que deseas gestionar dentro de la interfaz de la app.
- Toca el botón «...»: Junto al título del servicio, verás un botón «...». Tócalo para acceder a opciones adicionales.
  - **Renombrar**: Si quieres cambiar el nombre del servicio de nube tal como aparece en tu lista, selecciona «Renombrar».
  - **Ajustes**: Para modificar la configuración o los datos de autenticación del servicio en la nube, elige «Ajustes». A veces, puede que necesites reautorizar el servicio de nube conectado si el token de autorización ha expirado.
  - **Desconectar**: Si deseas cortar completamente la conexión entre la app y el servicio en la nube, selecciona «Desconectar». Ten en cuenta que elegir esta opción eliminará todas las canciones asociadas a este servicio de nube de la biblioteca musical de tu app, pero permanecerán en el servidor.

## Conectar a Computadora o NAS

También puedes conectar tu computadora, NAS personal u otros dispositivos de red usando el protocolo SMB, DLNA o WebDAV.

## Conectar a computadora usando SMB

- Toca «Conectar a almacenamiento en la nube» → SMB.
- Introduce la dirección IP de la computadora y el nombre de la carpeta compartida en el campo URL usando el formato smb://dirección-ip-computadora/nombre-carpeta-compartida
- Elige la versión del protocolo: Auto, SMB1, SMB2
- Introduce nombre de usuario y contraseña (si se requiere)
- Toca «Hecho».

Si la conexión es exitosa, verás el almacenamiento conectado en la sección «Almacenamiento en la nube».
Un tutorial completo sobre cómo conectar tu Mac o PC usando SMB está disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Conectar a NAS usando WebDAV

Todos los pasos son iguales excepto por el campo URL.
La URL debe estar en el formato http://nombre-servidor, o https://nombre-servidor si el servidor admite SSL.
Un tutorial completo sobre cómo conectar NAS usando el protocolo WebDAV está disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dispositivos disponibles

Esta sección muestra todos los dispositivos dentro de tu red local a los que puedes conectarte a través de la aplicación.
Para establecer una conexión con un dispositivo, sigue estos pasos:

- Abre la app y ve a la sección «Dispositivos disponibles».
- Toca el dispositivo al que quieres conectarte de la lista.
- Si es necesario, introduce tus datos de inicio de sesión para completar la conexión.

## Wi-Fi Drive

Wi-Fi Drive es una conveniente tecnología que permite transferencias inalámbricas de archivos desde tu computadora a tu dispositivo iOS a través de un navegador de escritorio.
Para usar esta función de manera efectiva, asegúrate de que tu dispositivo y tu computadora estén conectados a la misma red Wi-Fi.
Aquí tienes una guía paso a paso sobre cómo usar Wi-Fi Drive.

## Activar Wi-Fi Drive

- Abre la aplicación y ve a la pestaña «Conexiones».
- Selecciona «Conectar via Wi-Fi» para acceder a la pantalla principal de Wi-Fi Drive.
- Toca «Iniciar Wi-Fi Drive» para activar Wi-Fi Drive.

## Acceder a Wi-Fi Drive en Tu Computadora

- En tu computadora (de escritorio o portátil), abre un navegador web (como Chrome, Firefox o Safari).
- En la barra de direcciones del navegador, introduce la URL proporcionada por la aplicación.

## Transferir Archivos de Forma Inalámbrica

Una vez que la página web correspondiente a tu dispositivo iOS se abra en el navegador, puedes arrastrar y soltar archivos fácilmente desde tu computadora a la página web.
Los archivos que arrastres y sueltes comenzarán a transferirse a tu dispositivo iOS y estarán accesibles dentro de la aplicación.

Las instrucciones detalladas sobre cómo transferir archivos de forma inalámbrica usando Wi-Fi Drive están disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing es otra tecnología que te permite transferir archivos de una computadora a un dispositivo usando la app Finder en tu Mac y un cable Lightning.
- Simplemente conecta el dispositivo a la computadora usando un cable y ejecuta la app Finder en tu Mac.
- Abre «Ubicaciones» → «Tu Dispositivo Conectado» → «Archivos» → y busca la app actual.
- Toca en el icono de la app para ver todas las carpetas compartidas.
- Copia archivos de la computadora a la carpeta compartida en el dispositivo usando arrastrar y soltar.

Las instrucciones detalladas sobre cómo usar iTunes File Sharing están disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Conectar una tarjeta USB flash

Si tienes una tarjeta SD o un pendrive USB, puedes conectarlo usando un lector de tarjetas Lightning o USB-C en iPhone/iPad, o conectarlo directamente a un Mac. La app actualmente admite lectores de tarjetas certificados por Apple. Tenemos instrucciones detalladas sobre cómo conectar una tarjeta USB flash a tu iPhone o iPad y gestionar los archivos ubicados en ella, disponibles [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Las unidades conectadas aparecen en la sección **Accesorios conectados** de la pantalla Conexiones.

## Gestor de archivos

Una vez que hayas conectado un servicio de almacenamiento en la nube, toca su icono para ver todos los archivos y carpetas disponibles. Puedes usar el gestor de archivos integrado para trabajar con estos archivos — descargar, renombrar, mover y más. Cuando inicias una descarga, el archivo aparecerá en la cola de transferencia. Para ver la cola de transferencia, ve a la pestaña «Archivos Locales» y toca las flechas giratorias en la esquina superior izquierda. Todos los archivos y carpetas descargados están disponibles en la sección «Archivos Locales».

## Barra de herramientas superior

La barra de herramientas superior, convenientemente ubicada debajo de la barra de navegación, ofrece varias acciones útiles para fácil acceso. Puedes mostrar u ocultar esta barra de herramientas usando un simple gesto de deslizamiento hacia abajo. Aquí están las acciones disponibles:

- **Buscar**: Esta opción te permite realizar una búsqueda rápida dentro del directorio actual, facilitando la localización de archivos o carpetas específicas.

## Opciones de Carpeta

Cuando abres una carpeta dentro de la app, encontrarás un conjunto de acciones disponibles tocando el botón «...» en la esquina superior derecha de la pantalla.
Aquí hay un desglose de estas acciones:

- **Seleccionar**: Activa el modo de selección de archivos. Este modo te permite elegir uno o más archivos dentro de la carpeta, facilitando la realización de acciones en los elementos seleccionados.
- **Nueva Carpeta**: Crea una nueva carpeta dentro de la carpeta actual. Esta función te permite organizar tus archivos y mantener tu biblioteca bien estructurada.
- **Subir Archivos**: Sube archivos desde tu dispositivo a la carpeta online. Esta acción te permite transferir archivos a la nube o al servidor, haciéndolos accesibles desde cualquier lugar.
- **Buscar**: Busca archivos específicos dentro de la carpeta actual. Esto es especialmente útil para localizar rápidamente elementos específicos en una gran colección.
- **Ordenar**: Ordena archivos dentro de la carpeta por criterios como nombre, tamaño o fecha de edición. El modo de ordenación predeterminado generalmente refleja el orden de clasificación en el servidor, pero puedes cambiarlo según tus preferencias.
- **Vista de cuadrícula/lista**: Cambia entre dos modos de visualización: vista de tabla y vista de miniaturas. La vista de tabla presenta archivos en una lista, mientras que la vista de miniaturas muestra representaciones visuales de los archivos, facilitando la identificación del contenido a primera vista.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Cloud Folder Sort" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Editar Archivos en Línea

Cuando necesitas gestionar varios archivos dentro de tu almacenamiento en la nube en esta app, puedes usar el modo de selección para agilizar tus acciones. Sigue estos pasos para una gestión efectiva de archivos:

- **Activar Modo de Selección**: Abre la app en tu dispositivo y navega a la sección que contiene tu almacenamiento en la nube. Busca la esquina superior derecha donde encontrarás el botón «...» (puntos suspensivos). Tócalo y elige el elemento de menú «Seleccionar» para activar el modo de selección.
- **Elegir Archivos**: Notarás casillas de verificación apareciendo junto a cada archivo o carpeta listada. Elige uno o varios archivos o carpetas simplemente tocando las casillas de verificación junto a ellos.
- **Realizar Varias Acciones**: Una vez que hayas seleccionado los archivos o carpetas que deseas gestionar, tendrás acceso a varias acciones adaptadas a tus necesidades:

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Select" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Acciones de archivo

Cerca del título del archivo, notarás un símbolo de puntos suspensivos «...» (tres puntos) – este sirve como el menú de acciones.
Tócalo para revelar una lista de acciones disponibles:

- **Editar etiquetas de audio**: Al seleccionar esta opción, puedes acceder al editor de etiquetas integrado, lo que te permite modificar las etiquetas de audio para el archivo elegido. El archivo se descargará temporalmente a un directorio temporal y luego se subirá al almacenamiento después de que confirmes los cambios.
- **Añadir a Favoritos**: Esta acción añade el archivo a tu lista de archivos favoritos para acceso rápido y conveniente.
- **Descargar**: Elige esta acción para descargar el archivo o carpeta a tu dispositivo, haciéndolo accesible para uso sin conexión.
- **Renombrar**: Esta opción te permite renombrar el archivo directamente en el almacenamiento remoto, permitiendo nombres de archivo personalizados.
- **Mover**: Opta por esta acción para reubicar el archivo en una carpeta diferente dentro de tu almacenamiento en la nube, ayudando a mantener una estructura de archivos organizada.
- **Abrir en**: Usa esta acción para exportar el archivo a otra app compatible. El archivo se descargará a tu dispositivo y luego aparecerá el diálogo de compartir para más acciones o interacción.
- **Eliminar**: Ten cuidado con esta acción, ya que elimina permanentemente el archivo de tu almacenamiento en la nube. **Esta eliminación no se puede deshacer**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag File Options" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Si la lista de acciones supera el espacio de pantalla disponible, simplemente desplázate hacia abajo dentro del menú de acciones para acceder a opciones adicionales.

## Acciones de carpeta

Para cada carpeta en tu almacenamiento en la nube, tienes varias acciones disponibles. Para acceder a estas opciones, simplemente toca el icono de puntos suspensivos «...» ubicado junto al título de la carpeta. Si no ves todas las acciones, desplázate hacia abajo para revelar más opciones. Aquí están las acciones disponibles:

- **Añadir a Favoritos**: Usa esta acción para añadir la carpeta a tu lista de archivos favoritos para acceso rápido y conveniente.
- **Descargar**: Descarga todo el contenido de la carpeta a tu dispositivo para acceso sin conexión.
- **Renombrar**: Renombra la carpeta directamente en el almacenamiento remoto.
- **Mover**: Reubica la carpeta en una ubicación diferente dentro de tu almacenamiento en la nube.
- **Eliminar**: Ten cuidado con esta acción, ya que elimina permanentemente la carpeta y su contenido de tu almacenamiento en la nube. **Esta acción no se puede deshacer**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evertag Folder Options" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
