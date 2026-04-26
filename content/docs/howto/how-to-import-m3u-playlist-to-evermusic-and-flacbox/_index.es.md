---
title: "Cómo importar una lista de reproducción M3U a Evermusic y Flacbox"
date: 2024-01-31
description: "Aprende cómo importar archivos de listas de reproducción M3U, M3U8 y CUE desde la nube, almacenamiento local o dispositivo a Evermusic y Flacbox."
keywords: ["evermusic", "flacbox", "lista de reproducción", "m3u", "m3u8", "cue", "importar", "aplicación de música"]
tags: ["evermusic", "importar", "listas de reproducción", "m3u", "cue"]
readingTime: 3
---

{{< author-byline >}}


**Resumen:** Evermusic y Flacbox admiten la importación de archivos de listas de reproducción M3U, M3U8 y CUE desde almacenamiento en la nube, archivos locales de la aplicación o tu dispositivo. Ve a Listas de reproducción > Más > Importar lista de reproducción, selecciona una fuente, elige tu archivo y la aplicación creará tu lista de reproducción automáticamente.

M3U, que significa MP3 URL o Moving Picture Experts Group Audio Layer 3 Uniform Resource Locator, es un formato de archivo de computadora utilizado para listas de reproducción multimedia. Uno de sus usos principales es crear archivos de listas de reproducción de una sola entrada que apuntan a transmisiones en Internet. Estos archivos ofrecen acceso conveniente al contenido de streaming y se utilizan comúnmente para descargas, correo electrónico y escuchar radio por Internet.

A pesar de su uso generalizado, no existe una especificación formal para el formato M3U; se ha convertido en un estándar de facto. Un archivo M3U es esencialmente un archivo de texto plano que especifica las ubicaciones de uno o más archivos multimedia. Dependiendo de la codificación, se guarda con la extensión "m3u" o "m3u8". Cada entrada en el archivo especifica la ubicación de un archivo multimedia, que puede ser una ruta local absoluta, una ruta local relativa a la ubicación del archivo M3U o una URL. Las entradas están separadas por saltos de línea, y algunos dispositivos requieren saltos de línea representados como CR LF.

Además, los archivos M3U pueden incluir comentarios precedidos por el carácter "#". En M3U extendido, "#" introduce directivas M3U extendidas, que pueden admitir parámetros terminados con dos puntos ":".

En nuestras aplicaciones Evermusic y Flacbox, hemos implementado la funcionalidad de importación de archivos M3U, eliminando la necesidad de crear listas de reproducción manualmente. Esta guía te acompañará en la importación de tus listas de reproducción desde almacenamiento en la nube, archivos locales o archivos en tu dispositivo directamente en la aplicación.

Primero, navega a la sección 'Listas de reproducción'. A continuación, toca el botón 'Más' ubicado en la esquina superior derecha. Del menú que aparece, selecciona la opción 'Importar lista de reproducción'.

![acción de importar lista de reproducción](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_fd95e0ec2f6a49bfb98fc33005b2f70a~mv2.png)

En la siguiente pantalla, elige la ubicación del archivo. Las opciones compatibles incluyen:

- Almacenamiento en la nube conectado;
- Archivos en la aplicación;
- Archivos en tu dispositivo;

![seleccionar ubicación del archivo](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_1a9066303ba74a0980957ced63536683~mv2.png)

Seleccionemos el almacenamiento en la nube conectado y abramos la carpeta que contiene el archivo de la lista de reproducción. Las extensiones de archivo de listas de reproducción compatibles incluyen M3U, M3U8 y CUE. Selecciona el archivo de la lista de reproducción y toca 'Hecho' para confirmar tu selección.

![seleccionar archivo M3U](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_4024ea3ad6d24efdb40f62e599da198a~mv2.png)

La aplicación analizará el archivo de la lista de reproducción y creará una lista de pistas. Luego localizará esos archivos en el almacenamiento y compilará una lista de reproducción final que se importará a la biblioteca de música. Es crucial que tu archivo M3U/CUE contenga las rutas correctas para los archivos multimedia, y los archivos deben estar ubicados en esas rutas en tu almacenamiento.

![lista de reproducción importada](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/21260c_2b56a04c305f496c84ce025769e2ed5c~mv2.png)

La aplicación admite tanto rutas relativas como URLs absolutas de archivos.

Por ejemplo:

Lista de reproducción con rutas relativas:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
080 - Kenny Rogers & The First Edition.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
../tracks/050 - Kenny Rogers & The Second Edition.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
/music/049 - Kenny Rogers & The Third Edition.mp3
```

Lista de reproducción con URLs absolutas:

```plaintext
#EXTM3U

#EXTINF:199, Kenny Rogers & The First Edition
http://mywebdavserver.com/music/track1.mp3

#EXTINF:205, Kenny Rogers & The Second Edition
http://mywebdavserver.com/music/track2.mp3

#EXTINF:173, Kenny Rogers & The Third Edition
http://mywebdavserver.com/music/track3.mp3
```

Si importas un archivo de lista de reproducción ubicado dentro de la aplicación (sección de Archivos locales), no se requieren pasos adicionales.

Sin embargo, si deseas importar una lista de reproducción ubicada en tu dispositivo usando el selector de archivos del sistema, hay una consideración importante a tener en cuenta.

Debido a las políticas de seguridad, la aplicación solo puede acceder al archivo que selecciones usando el selector de archivos del sistema. Sin embargo, el archivo de la lista de reproducción puede incluir enlaces a otros archivos multimedia en tu dispositivo. Para importar una lista de reproducción desde tu dispositivo, debes seleccionar una carpeta que contenga tanto el archivo de la lista de reproducción como todos los archivos multimedia vinculados a ella. En este caso, la aplicación escaneará la carpeta seleccionada, encontrará el archivo de la lista de reproducción, construirá la lista de pistas y la importará a la biblioteca de música.

Además, puedes importar múltiples listas de reproducción a la vez tocando el botón "Más acciones" y seleccionando "Importar listas de reproducción desde una carpeta". La aplicación escaneará el contenido de la carpeta, encontrará los archivos de listas de reproducción compatibles y los importará a la biblioteca.

## Preguntas frecuentes

{{% details title="¿Qué formatos de listas de reproducción admiten Evermusic y Flacbox?" closed="true" %}}
Ambas aplicaciones admiten los formatos de archivo de listas de reproducción M3U, M3U8 y CUE. Estos cubren los estándares de listas de reproducción más comunes utilizados por reproductores de música y software multimedia.
{{% /details %}}

{{% details title="¿Puedo importar listas de reproducción desde almacenamiento en la nube?" closed="true" %}}
Sí. Puedes importar archivos de listas de reproducción desde cualquier servicio de almacenamiento en la nube conectado, incluyendo Google Drive, Dropbox, OneDrive y servidores WebDAV.
{{% /details %}}

{{% details title="¿Por qué faltan algunas pistas después de la importación?" closed="true" %}}
El archivo de la lista de reproducción debe contener rutas correctas a tus archivos multimedia, y esos archivos deben existir en las ubicaciones especificadas en tu almacenamiento. Verifica que las rutas de archivos en tu archivo M3U o CUE coincidan con las ubicaciones reales de los archivos.
{{% /details %}}

{{% details title="¿Puedo importar múltiples listas de reproducción a la vez?" closed="true" %}}
Sí. Usa el botón Más acciones y selecciona "Importar listas de reproducción desde una carpeta". La aplicación escanea la carpeta en busca de todos los archivos de listas de reproducción compatibles y los importa en un solo paso.
{{% /details %}}

{{% details title="¿Necesito crear las listas de reproducción manualmente?" closed="true" %}}
No. La función de importación elimina la creación manual de listas de reproducción. Solo apunta la aplicación a tu archivo M3U, M3U8 o CUE existente y creará la lista de reproducción automáticamente.
{{% /details %}}
