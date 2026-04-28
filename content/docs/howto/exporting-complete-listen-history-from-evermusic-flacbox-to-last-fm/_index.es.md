---
title: "Exporta tu historial de escucha completo de Evermusic y Flacbox a Last.fm"
date: 2024-01-30
description: "Aprende a exportar tu historial de música de Evermusic y Flacbox y subirlo a Last.fm usando archivos CSV y la herramienta Last.fm Scrubbler para Windows."
keywords: ["evermusic", "flacbox", "lastfm", "historial de música", "scrobbling", "exportar pistas", "csv", "scrubbler"]
tags: ["evermusic", "flacbox", "recientes", "lastfm", "exportar", "scrobbler"]
readingTime: 5
---

{{< author-byline >}}


**Resumen:** Exporta tu historial de escucha de Evermusic o Flacbox como archivo CSV, luego súbelo a Last.fm usando la herramienta gratuita Last.fm-Scrubbler-WPF en Windows. El scrobbling automático también está disponible de forma nativa en ambas apps.

**Actualización:** ¡El scrobbling automático ya está disponible! Más información aquí: [/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm)

El scrobbling es una forma sencilla de guardar automáticamente detalles básicos como el título y el artista de la canción que estás reproduciendo en un servicio en línea. Más tarde, puedes revisar tu historial de escucha.

[Last.fm](https://www.last.fm/home), impulsado por un sistema de recomendación musical llamado Audioscrobbler, ofrece este servicio de forma gratuita. Crea un perfil detallado de tu gusto musical registrando las pistas que escuchas, ya sea de estaciones de radio por internet, tu computadora o diversos dispositivos de música portátiles. Puedes visitar el sitio web más tarde para recibir recomendaciones de nuevos artistas o álbumes que coincidan con tu gusto musical.

Puedes subir tu historial de escucha a [Last.fm](http://Last.fm) desde las aplicaciones Evermusic y Flacbox usando una herramienta gratuita, y te guiaremos a través del proceso.

Abre la sección 'Biblioteca de música' de la aplicación y desplázate hasta la sección 'Acceso rápido'. Toca el elemento del menú 'Recientes'.

![pantalla de la biblioteca de música](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_515ff6fa1fa447d29da56f0998302e4e~mv2.png)

En la pantalla 'Recientes' toca el botón 'Más' en la esquina superior derecha para activar el menú 'Más acciones'. Toca el elemento del menú 'Exportar lista de canciones'.

![pantalla de recientes](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_762ce17498ed43d2a4402ef0d1fd250b~mv2.png)

En la pantalla 'Seleccionar formato de archivo' tienes la posibilidad de seleccionar el formato del archivo de destino. Opciones disponibles - CSV, TXT, M3U.

![pantalla de selección de formato de archivo](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_589bfdb833c24877a1c8e3f13d6830fa~mv2.png)

CSV: Significa Valores Separados por Comas, perfecto para organizar tus datos en un formato de tabla ordenado. En el archivo de destino, encontrarás parámetros como Nombre del Artista, Nombre del Álbum, Nombre de la Pista, Marca de Tiempo (la hora en que escuchaste las pistas), Nombre del Artista del Álbum y Duración de la Pista.

TXT: Aquí hablamos de un archivo de texto plano. Es simple y directo, con parámetros que incluyen Nombre del Artista, Nombre del Álbum, Nombre de la Pista y Duración.

M3U: Este formato es esencialmente el estándar para crear listas de reproducción. Es genial porque puedes exportar tu lista de canciones y disfrutar de tus pistas en cualquier dispositivo, incluso si no tienes los archivos originales (siempre que selecciones la opción de URL absoluta para los archivos multimedia). En el archivo de salida, encontrarás parámetros como Duración, Nombre del Artista, Nombre de la Pista y Ubicación del Archivo Multimedia.

Para nuestra tarea, seleccionar CSV es el camino correcto. Usaremos este archivo con el software gratuito Last.fm-Scrubbler-WPF para subir nuestro historial de escucha al servicio [Last.fm](http://Last.fm). Simplemente elige CSV y pulsa el botón 'Exportar'.

![pantalla de exportación completada](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fb3fcd41b94b468c955283c9e64a5ccd~mv2.png)

Después de completar la exportación, simplemente toca el botón 'Mostrar archivo', y la app revelará el archivo creado en tu carpeta de documentos. Luego, toca el botón 'Más acciones' junto al nombre del archivo y selecciona la opción 'Abrir en' del menú. Nuestro siguiente paso es copiar el archivo exportado a tu computadora de escritorio. Puedes hacerlo fácilmente seleccionando la opción AirDrop del menú 'Abrir en'.

![más acciones para el archivo exportado](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_f536f740deec4cefbcd90fa5c2c3a492~mv2.png)

A continuación, usaremos un cliente gratuito de código abierto de [Last.FM](http://Last.FM) que solo está disponible en la plataforma Windows. Este cliente te permite actualizar eficientemente tu historial de escucha en [Last.FM](http://Last.FM) usando el archivo CSV que acabamos de exportar.

Ahora, si no estás usando actualmente una computadora con Windows, no te preocupes. Puedes acceder a este cliente instalando VirtualBox en tu Mac y usando el archivo de imagen oficial del entorno de desarrollo de Windows.

Esto es lo que necesitas hacer:

- Instala VirtualBox desde el siguiente enlace: [Descargar VirtualBox](https://www.virtualbox.org/wiki/Downloads)

- Descarga e instala el entorno de desarrollo de Windows desde este enlace: [Entorno de desarrollo de Windows](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)

En tu computadora con Windows (o la app VirtualBox con la imagen de desarrollo de Windows) descarga e instala [Last.fm-Scrubbler-WPF](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF) - software gratuito de código abierto disponible en GitHub. Probamos la versión 1.28 que puedes descargar aquí: [https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28](https://github.com/SHOEGAZEssb/Last.fm-Scrubbler-WPF/releases/tag/B1.28)

![página de descarga de Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5d6c84d8bdee485f897aa22586a57f55~mv2.png)

En la sección 'Assets' toca en [Last.fm-Scrubbler-WPF-Beta-1.28.zip](http://Last.fm-Scrubbler-WPF-Beta-1.28.zip) para descargar el archivo de instalación. Descomprime el archivo descargado y abre la carpeta descomprimida.

- IMPORTANTE

Esta app todavía está en beta. Los creadores de la app no han realizado muchas pruebas. Recomiendan intentar hacer scrobble en una cuenta de prueba primero y ver si las cosas que quieres hacer scrobble funcionan correctamente. Especialmente si haces scrobble de muchas pistas a la vez. Por favor, ten cuidado con tus cuentas.

Ejecuta Last.fm-Scrubbler-WPF.exe

![Last.fm-Scrubbler-WPF](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_a6d8eb1310c34e19a51479af6687e010~mv2.png)

En la pantalla principal de la aplicación, simplemente toca en 'No conectado', ubicado en la esquina inferior izquierda, para activar la pantalla 'Agregar cuenta'.

![pantalla de agregar cuenta](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_131ab8d5992246e2b34e52e9524123e2~mv2.png)

Ingresa tus credenciales de inicio de sesión.

![pantalla de ingreso de credenciales](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_6886c14a62e5476f8119c7402d45ec0c~mv2.png)

Toca el botón 'Iniciar sesión' para agregar tu cuenta.

![Toca el botón Iniciar sesión para agregar tu cuenta.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_df441de5f5724852bf19fdbfa8642db4~mv2.png)

Abre la pestaña 'File Parse Scrobbler' para comenzar a importar el archivo CSV desde la app Evermusic.

![Abre la pestaña File Parse Scrobbler para comenzar a importar el archivo CSV desde la app Evermusic.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_ed50cac3149741c59ebccf65dc03843a~mv2.png)

Elige 'Parser: CSV' y toca el botón 'Configuración'.

En la siguiente pantalla, puedes elegir el orden de los parámetros en tu archivo CSV.

Los campos individuales pueden estar encerrados entre comillas y DEBEN estar encerrados entre comillas si el campo contiene alguno de los delimitadores establecidos. Por ejemplo:

"ArtistWith, CommaInTheName", Album, Track, 06/13/2016 19:54, AlbumArtist, 00:02:33

Así que deja todas las configuraciones por defecto, lo único que necesitas cambiar es habilitar la casilla de verificación en el campo 'Has Fields Enclosed In Quotes'.

Toca 'Guardar y cerrar' para aplicar los cambios.

![elegir el orden de los parámetros en tu archivo CSV.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_fd30ebaa4ef547b08e5314c6d44c9fc7~mv2.png)

El scrobbling de análisis de archivos tiene dos modos. Se pueden cambiar con el ComboBox 'Scrobbling Mode'.

Modo Normal: En este modo, las pistas se harán scrobble con la marca de tiempo del scrobble analizado. Solo los scrobbles más recientes de 14 días se pueden hacer scrobble.

Modo de Importación: En este modo, las pistas se harán scrobble con la marca de tiempo calculada a partir del 'Tiempo de Finalización' y la duración seleccionada entre cada pista. Esto permite hacer scrobble de las pistas incluso si la marca de tiempo del scrobble analizado es más antigua de 14 días. Por lo tanto, la primera pista (la de arriba) en el archivo CSV se hará scrobble con el 'Tiempo de Finalización'.

Elige un archivo CSV previamente generado desde la app Evermusic en el campo 'File:' y toca 'Parse'. En algunos casos, puedes ver una alerta de error diciendo que algunos scrobbles no pudieron ser analizados. Está bien si tienes algunas pistas sin metadatos completos como el Nombre del Artista.

![algunos scrobbles no pudieron ser analizados](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_7b7b485f106c4fbe8287c82b65b0cf32~mv2.png)

Toca el botón 'Seleccionar todo' para seleccionar todas las pistas analizadas.

![Toca el botón Seleccionar todo para seleccionar todas las pistas analizadas.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_8364b0734ea44375a1906de2a6a5391f~mv2.png)

Toca el botón 'Vista previa' para verificar todos los cambios que se publicarán en el servidor.

![Toca el botón Vista previa para verificar todos los cambios que se publicarán en el servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c02268681c6e4b51aa7e48e178d34be0~mv2.png)

Toca el botón 'Scrobble' para subir todos los cambios al servidor.

![Toca el botón Scrobble para subir todos los cambios al servidor.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_5e1aeac472344d1899c8103b04922a7e~mv2.png)

Anteriormente Last.fm-Scrubbler-WPF no tenía un límite diario de scrobbles. Esto ha cambiado ya que algunas personas usaron Scrubbler para hacer scrobble de tantas pistas que causó problemas en la página de Last.fm. El límite de scrobbling es actualmente de 2800 scrobbles por día. Cuando intentes hacer scrobble de más, recibirás un mensaje de error. Hay planes para agregar una 'cola de scrobbling', así que si necesitas hacer scrobble de más de 2800 pistas, se agregarán a una cola y se harán scrobble automáticamente después de un tiempo. Puedes verificar cuántos scrobbles te quedan en la vista de selección de usuario.

Una vez que todos los registros se hayan subido exitosamente al servidor, verás un mensaje en la parte inferior de la ventana de la app confirmando: 'Pistas seleccionadas scrobbleadas exitosamente.'

![Pistas seleccionadas scrobbleadas exitosamente.](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_c7c943f9994741eabbbab49de8ed6380~mv2.png)

Ahora puedes abrir tu perfil en la página de [Last.fm](http://Last.fm) y verificar todos los cambios.

![tu perfil en la página de Last.fm](/docs/howto/exporting-complete-listen-history-from-evermusic-flacbox-to-last-fm/21260c_1c065f759f624deea69a814e1b72c8bf~mv2.png)

## Preguntas frecuentes

{{% details title="¿Puedo hacer scrobble automáticamente sin exportar archivos CSV?" closed="true" %}}
Sí. Tanto Evermusic como Flacbox ahora admiten scrobbling automático a Last.fm. Consulta la guía: [Cómo hacer scrobble a Last.fm](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
{{% /details %}}

{{% details title="¿Qué pasa si mi CSV tiene pistas de más de 14 días?" closed="true" %}}
Usa el Modo de Importación en Last.fm-Scrubbler-WPF. Recalcula las marcas de tiempo desde el Tiempo de Finalización, permitiéndote hacer scrobble de las pistas independientemente de su fecha original.
{{% /details %}}

{{% details title="No tengo una computadora con Windows. ¿Puedo usar Last.fm-Scrubbler?" closed="true" %}}
Sí. Instala VirtualBox en tu Mac y descarga la imagen gratuita del entorno de desarrollo de Windows de Microsoft. Ejecuta Last.fm-Scrubbler-WPF dentro de la máquina virtual.
{{% /details %}}

{{% details title="¿Por qué no se analizan algunos scrobbles?" closed="true" %}}
Las pistas que carecen de metadatos esenciales (como el nombre del artista) no pueden ser analizadas. Esto es esperado y no afecta a otras pistas en el archivo.
{{% /details %}}

{{% details title="¿Hay un límite diario de scrobbling?" closed="true" %}}
Sí. Last.fm-Scrubbler-WPF permite hasta 2.800 scrobbles por día. Si necesitas hacer más, divide el proceso en varios días.
{{% /details %}}
