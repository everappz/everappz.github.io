---
title: "Cómo conectar un almacenamiento NAS mediante WebDAV y escuchar música en tu iPhone o Mac"
date: 2024-07-28
description: "Aprende a configurar WebDAV en tu Synology NAS y transmitir música a tu iPhone o Mac usando Evermusic o Flacbox. Sigue nuestra guía paso a paso."
keywords: ["conectar nas", "webdav synology", "transmitir música nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["música", "streaming", "almacenamiento", "nas", "conectar", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Resumen:** Instala y habilita WebDAV en tu Synology NAS, configura los permisos de la carpeta compartida y luego conéctate desde Evermusic o Flacbox usando la dirección IP del NAS y el puerto WebDAV (predeterminado 5005/5006). Puedes transmitir y gestionar toda tu biblioteca musical sin copiar archivos a tu dispositivo.

Descubre cómo conectar tu almacenamiento NAS mediante WebDAV y transmitir fácilmente tu biblioteca musical a tu iPhone o Mac. WebDAV (Web-based Distributed Authoring and Versioning) es un protocolo que te permite gestionar y compartir archivos a través de Internet. Al configurar WebDAV en tu NAS, puedes acceder y transmitir tu colección musical, asegurándote de tener siempre tus canciones favoritas al alcance de tu mano.

En esta guía, te mostraremos cómo configurar una conexión WebDAV en uno de los servidores NAS más populares, Synology NAS. Sigue nuestros sencillos pasos para configurar WebDAV en tu Synology NAS, y podrás explorar, transmitir y gestionar tu biblioteca musical directamente desde tu iPhone o Mac.

## Paso 1: Instalar WebDAV en Synology NAS

1. Inicia sesión en tu Synology NAS y abre el **Centro de paquetes**.
2. Busca "webdav" e instala el paquete WebDAV si aún no está instalado. Abre el servidor WebDAV para configurarlo.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instalar WebDAV en Synology" width="600" >}}

## Paso 2: Configurar el servidor WebDAV

1. En la página de configuración de WebDAV, marca las casillas de **Habilitar HTTP**, **Habilitar HTTPS**, **Habilitar WebDAV anónimo** y **Habilitar DavDepthInfinity**.
2. Haz clic en **Aplicar** para guardar los cambios. Anota los números de puerto para las conexiones HTTP y HTTPS, que son 5005 y 5006 por defecto.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurar ajustes de WebDAV" width="600" >}}

## Paso 3: Configurar permisos de la carpeta compartida

1. Abre el **Panel de control** y ve a la sección **Carpeta compartida**.
2. Selecciona la carpeta **Música** y haz clic en **Editar**.
3. En la pestaña **Permisos**, configura los permisos. Habilita el acceso de invitado con Solo lectura si solo necesitas escuchar música, o Lectura/Escritura si necesitas modificar archivos. Guarda los cambios.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permisos de carpeta compartida" width="600" >}}

## Paso 4: Encontrar la dirección IP del Synology NAS

1. Abre el **Panel de control** y ve a la pestaña **Interfaz de red**, o usa tu navegador web para visitar [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Encontrar la dirección IP del NAS" width="600" >}}

2. Anota la dirección IP de tu Synology NAS (por ejemplo, 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Dirección IP del Synology NAS" width="600" >}}

## Paso 5: Conectar a Synology NAS usando Evermusic/Flacbox

1. Abre la app Evermusic o Flacbox y ve a la pestaña **Conexiones**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Pestaña Conexiones en Evermusic" width="600" >}}

2. Para la conexión automática, encuentra tu Synology NAS en la sección **Dispositivos disponibles** y tócalo para conectar.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Lista de dispositivos disponibles" width="600" >}}

3. Para la conexión manual, elige **Conectar un servicio en la nube** y selecciona **WebDAV**. Ingresa la dirección del servidor en el formato: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (por ejemplo, [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configuración manual de WebDAV" width="600" >}}

4. Deja los campos de usuario y contraseña vacíos para el acceso de invitado, o ingresa tus credenciales de Synology. Toca **Iniciar sesión**.

## Paso 6: Navegar y reproducir música

1. Una vez conectado, el dispositivo aparecerá en la lista de **Accesorios conectados**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Dispositivos conectados en Evermusic" width="600" >}}

2. Navega a la carpeta **Música** y toca cualquier archivo de audio para iniciar la reproducción.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Explorando la carpeta de música" width="600" >}}

## Paso 7: Agregar la carpeta en la nube conectada a la biblioteca musical

1. Abre la sección **Biblioteca musical** en la app.
2. Elige **Agregar música** y selecciona **Conexiones**.
3. Elige tu servidor NAS conectado y selecciona la carpeta **Música**. Toca **Hecho**.
4. La app escaneará la carpeta de música y agregará los archivos de audio compatibles a la biblioteca musical. Se cargarán los metadatos y tus pistas se agruparán por álbum, artista y género.

## Conclusión

Siguiendo estos pasos, puedes configurar fácilmente una conexión WebDAV en tu Synology NAS y transmitir tu biblioteca musical a tu iPhone o Mac usando Evermusic o Flacbox. Disfruta de acceso fluido a tus canciones favoritas en cualquier momento.

## Preguntas frecuentes

{{% details title="¿Qué dispositivos NAS son compatibles con WebDAV?" closed="true" %}}
La mayoría de las marcas populares de NAS son compatibles con WebDAV, incluyendo Synology, QNAP, TrueNAS y Western Digital. Consulta la documentación del fabricante de tu NAS para las instrucciones de configuración de WebDAV.
{{% /details %}}

{{% details title="¿Cuál es la diferencia entre WebDAV y SMB para transmitir música desde NAS?" closed="true" %}}
WebDAV funciona sobre HTTP/HTTPS y es más adecuado para el acceso remoto a través de Internet. SMB es típicamente más rápido en redes locales. Evermusic y Flacbox son compatibles con ambos protocolos, así que elige según si necesitas acceso local o remoto.
{{% /details %}}

{{% details title="¿Necesito un nombre de usuario y contraseña para WebDAV en Synology?" closed="true" %}}
No, si habilitas el acceso anónimo a WebDAV y configuras los permisos de invitado en tu carpeta compartida. Para mayor seguridad, puedes usar tus credenciales de Synology en su lugar.
{{% /details %}}

{{% details title="¿Puedo transmitir FLAC y otros formatos de alta resolución desde NAS vía WebDAV?" closed="true" %}}
Sí. Tanto Evermusic como Flacbox son compatibles con FLAC, ALAC, WAV, DSD y otros formatos de alta resolución al transmitir desde el almacenamiento NAS vía WebDAV.
{{% /details %}}

{{% details title="¿Por qué la app no puede encontrar mi NAS en Dispositivos disponibles?" closed="true" %}}
Asegúrate de que tu iPhone/Mac y el NAS estén en la misma red Wi-Fi. Si la detección automática no funciona, usa la opción de conexión manual e ingresa la dirección IP del NAS y el puerto WebDAV directamente.
{{% /details %}}
