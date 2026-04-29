---
title: "Cómo exportar la colección de pistas a M3U, CSV y TXT en Evermusic y Flacbox"
date: 2024-01-31
description: "Aprende a exportar tus recientes, favoritos, listas de reproducción y álbumes de Evermusic y Flacbox a formatos M3U, CSV o TXT. Perfecto para scrobbling en Last.fm y reproducción en otros dispositivos."
keywords: ["exportar evermusic", "exportar flacbox", "exportar a m3u", "exportar lista de reproducción a csv", "m3u txt csv lista de reproducción", "exportar música"]
tags: ["evermusic", "recientes", "favoritos", "exportar", "m3u", "lista de reproducción", "csv", "txt", "álbum"]
---

{{< author-byline >}}


**Resumen:** Evermusic y Flacbox te permiten exportar cualquier colección de pistas (recientes, favoritos, listas de reproducción, álbumes) a archivos CSV, TXT o M3U. Usa estas exportaciones para hacer scrobbling en Last.fm, respaldar tu biblioteca o reproducir tus listas en otros dispositivos.

## Introducción

Exportar tus recientes, favoritos, álbumes y listas de reproducción de la app a un archivo externo puede ser increíblemente útil. Puedes usar estos archivos para actualizar tu historial de escucha en servicios de scrobbling como [Last.fm](http://Last.fm) o escuchar tus listas de reproducción en dispositivos externos. Con Evermusic y Flacbox, este proceso es fácil. Aquí te mostraremos cómo exportar tus recientes a CSV/TXT y tus listas de reproducción a M3U. Sin embargo, esta funcionalidad está disponible para cualquier colección de pistas dentro de la app.

## Elegir formato

Para exportar tus recientes, abre la sección 'Biblioteca de música' y selecciona el elemento del menú 'Recientes'.

![biblioteca de música](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d7437e96448342ec9a0b2726b10ba1e6~mv2.png)

En la siguiente pantalla, toca el botón 'Más acciones' en la esquina superior derecha y elige 'Exportar lista de canciones'.

![exportar recientes](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_ce62fff9eaf24f20ab1450a4ff62a091~mv2.png)

En la pantalla 'Seleccionar formato de archivo' tienes varias opciones - CSV, TXT, M3U.

- CSV

Esto significa Valores Separados por Comas, perfecto para organizar tus datos en un formato de tabla ordenado. En el archivo de destino, encontrarás parámetros como Nombre del Artista, Nombre del Álbum, Nombre de la Pista, Marca de tiempo (la hora en que escuchaste las pistas), Nombre del Artista del Álbum y Duración de la Pista. Puedes usar ese archivo más tarde para actualizar tu historial de escucha en servicios de scrobbling como [Last.fm](http://Last.fm) como se describe [aquí](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/).

- TXT

Aquí hablamos de un archivo de texto plano. Es simple y directo, con parámetros que incluyen Nombre del Artista, Nombre del Álbum, Nombre de la Pista y Duración. Útil si solo necesitas una lista de pistas en presentación de texto.

- M3U

Este formato es esencialmente la opción preferida para crear listas de reproducción. Es genial porque puedes exportar tu lista de canciones y disfrutar de tus pistas en cualquier dispositivo, incluso si no tienes los archivos originales (si seleccionas la opción de URL absoluta para la exportación de archivos multimedia). En el archivo de salida, encontrarás parámetros como Duración, Nombre del Artista, Nombre de la Pista y Ubicación del Archivo Multimedia.

## Formato CSV

Ahora, seleccionemos CSV y veamos qué recibiremos. Simplemente elige CSV y presiona el botón 'Exportar'.

![seleccionar formato de archivo](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_001c15e241744c1bab444c64f278b6d8~mv2.png)

Una vez completada la exportación, verás una alerta con dos opciones. Tocar 'Mostrar archivo' revelará el archivo resultante en tu directorio de documentos.

![exportación completada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Ahora puedes enviar ese archivo, abrirlo en un editor de texto externo o usarlo para actualizar tu progreso de escucha en [Last.fm](http://Last.fm).

![carpeta de exportación con archivos de resultados](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_d03e11c2cfce443e8e8e3422040a4e8a~mv2.png)

El archivo CSV de salida contendrá campos en el siguiente formato:

```
{ARTIST_NAME},{ALBUM_NAME},{TRACK_NAME},{TIMESTAMP yyyy-MM-dd HH:mm:ss},{ALBUM_ARTIST_NAME},{TRACK_DURATION HH:mm:ss}
```

Por ejemplo:

```
The Everly Brothers,100 Greatest Feel Good,All I Have To Do Is Dream,2024-01-06 23:17:26,The Everly Brothers,00:02:23
```

![archivo csv exportado](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_fcfba9a96e3c4db9bd3b227e625b2383~mv2.png)

## Formato TXT

El archivo TXT de salida contendrá campos en el siguiente formato:

```
{ORDER_NUMBER}. {ARTIST_NAME} - {ALBUM_NAME} - {TRACK_NAME} (DURATION HH:mm:ss)
```

Por ejemplo:

```
22. Queen Omega - Reggae Hits Vol 30 - All For You (00:03:21)
```

![archivo txt exportado](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_f134980fbc2b4443b096e301d7cb6a91~mv2.png)

## Formato M3U

A continuación, te guiaremos a través de la exportación de tu lista de reproducción a formato M3U, que es el estándar de facto para archivos de listas de reproducción. La condición principal para una exportación exitosa de la lista de reproducción es que todos los archivos en la lista deben estar ubicados en el mismo almacenamiento, ya sea en un servicio en la nube como Google Drive, archivos locales o archivos en tu dispositivo. Para comenzar el proceso de exportación, abre cualquier lista de reproducción y toca el botón 'Más acciones' en la esquina superior derecha, luego elige el elemento del menú 'Exportar lista de canciones'.

![pantalla de lista de reproducción](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_1371229150d54151ba525addf7e59448~mv2.png)

En la siguiente pantalla, selecciona el formato de archivo 'M3U', donde encontrarás dos opciones para 'Tipo de ubicación del archivo multimedia':

![pantalla de selección de formato de archivo de exportación](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_57113a1744f94428b75c73ad05462f7f~mv2.png)

1. Si eliges 'Ruta relativa', la lista de reproducción se creará con ubicaciones de archivos multimedia escritas de forma relativa al archivo de la lista de reproducción. Por ejemplo:

    ```
    my track name.mp3
    tracks/track1.mp3
    ../artist/album/track10.mp3
    ```

   En este caso, evita cambiar la ubicación del archivo M3U después de completar la exportación, ya que hacerlo romperá las rutas de los archivos multimedia. Para comenzar la reproducción de tu lista, simplemente toca el archivo de lista de reproducción exportado y la app localizará automáticamente los archivos multimedia en tu almacenamiento e iniciará la reproducción. O incluso puedes exportar tus listas de reproducción al almacenamiento y luego importarlas de nuevo en tu nuevo dispositivo.

2. Si eliges 'URL absoluta', la app generará URLs directas para tus archivos multimedia. Esto te permite reproducir la lista de reproducción en cualquier dispositivo/aplicación sin necesidad de que todos los archivos multimedia estén ubicados en el mismo almacenamiento que el archivo de la lista de reproducción. Esta opción solo es compatible con almacenamiento en la nube capaz de generar URLs directas de archivos. Sin embargo, ten en cuenta que en algunos casos, las URLs generadas pueden tener una vida útil limitada y pueden caducar después de un tiempo. Aquí está la lista de servicios en la nube compatibles: iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, GoogleDrive, WebDav (en modo invitado)  

La URL del archivo multimedia de salida será algo como:

```
https://uc2a69c7b75b6056be42091d92dd.dl.dropboxusercontent.com/cd/0/get/CMVQoDWSpnuUYxuIw0XSjXCzwawE6XnFbao7HggcPFNpHgeiYgVMesITUODm0xY3cbraGWG-ESBiYKmB9alP8W0IyvRqJzQGcjFm8JbnUdxbA3usnJnG0l78HuqUldCw9JnIsBVW3YyyTEDaxnKh9Ee_/file
```

Una vez que hayas seleccionado el 'Tipo de ubicación del archivo multimedia', toca 'Exportar'. La app te pedirá que elijas una carpeta de destino para exportar el archivo M3U. Toca 'Hecho' para confirmar tu selección.

![seleccionar una carpeta](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b3b006951b754f2f90cb030f7fa50274~mv2.png)

La app generará un archivo M3U y lo subirá/moverá a la carpeta de destino.

![subiendo archivo m3u](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_dea69f019bca45c1aa6ba929d15018b7~mv2.png)

Una vez completada la exportación, aparecerá una alerta del sistema con la opción de 'Mostrar archivo'.

![alerta de exportación completada](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_b46e5019cfaf45d0ad0fff8969b87afa~mv2.png)

Tocar esto revelará el archivo exportado en la app.

![archivo m3u exportado en la lista de archivos](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_59aaa264cfcc494e88ca1683796590ba~mv2.png)

Si seleccionaste 'Ruta relativa' como 'Tipo de ubicación del archivo multimedia' en el paso anterior, el archivo de salida estará en el siguiente formato:

```
#EXTM3U
#EXTINF:199, Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In)
080 - Kenny Rogers & The First Edition - Just Dropped In (To See What Condition My Condition Was In).mp3
```

![ejemplo m3u con rutas relativas](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_6b681b8079154631845f5b6f40653a39~mv2.png)

Para la opción 'URL absoluta', la app generará un archivo M3U en el formato:

```
#EXTM3U
#EXTINF:151, DownsiiD - Mehia (Lullaby to a Lost Daughter)
https://cloud.com/dfgfdguh45tgkbfgr/filecontent
```

![ejemplo m3u con URLs absolutas de archivos](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_a64edbada1ef4122bb0d6d92874de34e~mv2.png)

Puedes abrir ese archivo en cualquier dispositivo/aplicación que soporte listas de reproducción M3U.

![lista de reproducción m3u abierta en app externa](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/21260c_16a6ec3d1ee7483b872e6002fbc0c5e9~mv2.png)

## Reflexiones finales

Exportar tus pistas de Evermusic y Flacbox te da control completo sobre tus datos musicales. Ya sea que estés respaldando tu historial de escucha, haciendo scrobbling en Last.fm o disfrutando de listas de reproducción en dispositivos externos, estas opciones de exportación: M3U, CSV y TXT - son herramientas poderosas diseñadas para la flexibilidad y la compatibilidad. Aprovecha estas funciones para mejorar la forma en que organizas, compartes y revisitas tu colección de música en todas las plataformas.

## Preguntas frecuentes

{{% details title="¿Qué formato de exportación debo usar para el scrobbling de Last.fm?" closed="true" %}}
Usa CSV. Incluye marcas de tiempo y metadatos completos requeridos por herramientas de scrobbling como Last.fm-Scrubbler-WPF.
{{% /details %}}

{{% details title="¿Puedo exportar cualquier colección de pistas, no solo listas de reproducción?" closed="true" %}}
Sí. Puedes exportar recientes, favoritos, álbumes, listas de reproducción y cualquier otra colección de pistas en la app usando los mismos pasos.
{{% /details %}}

{{% details title="¿Funcionará mi lista de reproducción M3U en otros dispositivos?" closed="true" %}}
Si eliges la opción de URL absoluta durante la exportación, el archivo M3U se puede reproducir en cualquier dispositivo que soporte listas de reproducción M3U. Ten en cuenta que algunas URLs en la nube pueden caducar con el tiempo.
{{% /details %}}

{{% details title="¿Es gratuita la función de exportación?" closed="true" %}}
Sí. La exportación de colecciones de pistas a M3U, CSV y TXT está disponible tanto en las versiones gratuitas como premium de Evermusic y Flacbox.
{{% /details %}}

{{% details title="¿Qué servicios en la nube soportan la exportación de URL absoluta?" closed="true" %}}
La exportación de URL absoluta es compatible con iCloud Drive, pCloud, PanBaidu, MyCloudHome, DLNA, MediaFire, OneDrive, Box, Dropbox, Google Drive y WebDAV (modo invitado).
{{% /details %}}
