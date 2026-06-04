---
title: "Ajustes"
date: 2020-01-01
description: "Explora todos los ajustes de Evermusic, incluyendo configuración de audio, sincronización de biblioteca musical, carpetas sin conexión, metadatos, personalización, accesibilidad, widgets, CarPlay y opciones de copia de seguridad."
keywords: [
  "Evermusic", "ajustes", "configuración de audio", "sincronización de biblioteca musical",
  "carpetas sin conexión", "ecualizador", "crossfade", "reproducción sin pausas",
  "procesador de audio", "ajustes de lista de reproducción", "actualización premium",
  "restaurar compras", "gestor de archivos", "editor de etiquetas", "WiFi Drive",
  "voiceover", "copia de seguridad de la app", "accesibilidad", "localización",
  "widgets", "CarPlay", "audio espacial", "tono de audio"
]
tags: ["evermusic", "guía", "ajustes"]
readingTime: 16
---


La pantalla de **Ajustes** es el centro de control de Evermusic. Desde aquí puedes actualizar a Premium, configurar el reproductor de audio, gestionar tu biblioteca musical, configurar el gestor de archivos, personalizar la interfaz, activar widgets y CarPlay, hacer copias de seguridad de tus datos y acceder a ayuda e información legal. Las secciones están agrupadas bajo encabezados: **Compras y actualizaciones**, preferencias de la app, **Ayuda** y **Legal y privacidad**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Ajustes de Evermusic" image="/docs/guide/evermusic/evermusic-guide-settings/img/settings-main-screen.webp" >}}
{{< /cards >}}

## Compras y Actualizaciones

### Actualizar a Premium

Actualiza la aplicación a la versión Premium para eliminar todos los límites. La versión gratuita ofrece una compra única de por vida y dos opciones de suscripción que desbloquean el conjunto completo de funciones.

Family Sharing está habilitado para todas las compras y planes, por lo que puedes compartir la versión Premium con los miembros de tu familia.

Puedes leer más sobre compras y la versión Premium aquí: [¿Cuál es la diferencia entre Evermusic y Evermusic Premium?](/docs/faq/evermusic/what-is-the-difference-between-evermusic-and-evermusic-premium/).

#### Evermusic Free (Icono Azul) vs Evermusic Pro (Icono Rojo)

Evermusic está publicado en la App Store bajo dos iconos/colores diferentes:

- **Evermusic Free (icono azul)** está dividido en **dos apps separadas en la App Store con diferentes bundle IDs** — una para **iOS/iPadOS** y una dedicada para **macOS** (binario Universal que se ejecuta tanto en **Apple Silicon como en Intel Macs**). Las compras Premium dentro de la app se **comparten entre las apps azules de iOS y Mac a través de iCloud** — compra Premium en iPhone y se activa automáticamente en Mac (y viceversa), siempre que ambos dispositivos usen el mismo Apple ID con iCloud activado.
- **Evermusic Pro (icono rojo)** es una **única app en la App Store** con un **único bundle ID** que se ejecuta en **iPhone, iPad y Apple Silicon Macs (M1 y posteriores)**. Tiene la **misma funcionalidad que Evermusic Free con un plan Premium activado**. La app roja **no es compatible con Intel Macs**, por lo que su precio es ligeramente inferior al de la compra Premium equivalente en la app azul. Evermusic Pro también **no recopila ningún diagnóstico ni análisis de usuario en absoluto** — los análisis están completamente deshabilitados en la compilación, sin opción de activación.

Debido a que los bundle IDs difieren entre azul y rojo, una compra Premium activada en la app azul no desbloquea la app roja de forma gratuita, y viceversa. Si ya usas la app azul con Premium activado, no es necesario instalar la app roja — ya tienes todo lo que Pro ofrece.

### Compartir Compras Entre iOS y Mac

Las compras de por vida y las suscripciones se comparten entre iOS y Mac usando iCloud. Si ya tienes Premium en iOS, asegúrate de tener la última versión instalada y de que iCloud esté activado. Inicia la app en iOS y espera un minuto para que la información de tu compra se suba a iCloud.

También puedes tocar **Restaurar Compras** en los ajustes de la app. Después, instala la última versión de la app desde la App Store en tu Mac e iníciala. Asegúrate de tener conexión a internet y de haber iniciado sesión con la misma cuenta de iCloud y App Store en ambos dispositivos. Espera un minuto para que la app descargue la información de compra desde iCloud. La versión Premium debería activarse en tu Mac automáticamente.

### Restaurar Compras en un Dispositivo Nuevo

Para restaurar tu compra en un dispositivo nuevo, usa **Compras → Restaurar Compras**. Verás la lista de tus compras. Si falta algo, verifica que el dispositivo esté conectado a la misma cuenta de iTunes que se usó para realizar las compras y que iCloud esté activado.

### Probar Premium Gratis

Puedes actualizar a la versión Premium de forma gratuita por tiempo limitado usando este menú. Mira un breve anuncio o comparte la app con amigos para desbloquear Premium temporalmente.

### Compras

Restaura compras anteriores desde este menú. Si encuentras errores de activación, intenta activar la opción **Restaurar Compras al Iniciar la App**.

### Actualización de Software

Toca **Actualización de Software** para comprobar si hay una versión más reciente de Evermusic disponible. La app comparará tu versión instalada con la última versión en la App Store y te informará si se recomienda una actualización.

### Novedades

Este menú estará disponible después de que se publique una nueva versión. Muestra un resumen de los cambios y nuevas funciones incluidas en la actualización más reciente.

## Ajustes del Reproductor de Audio

Todos los ajustes del reproductor de audio están agrupados aquí: ecualizador, reproducción con crossfade, caché del reproductor de audio, carga de canciones y más. Los ajustes están organizados en subsecciones lógicas.

### General

Esta subsección contiene ajustes generales de cola de reproducción, salida de audio y guardado de estado.

#### Modo de Repetición

Especifica el comportamiento del reproductor de audio cuando una pista finaliza la reproducción:

- **Repetir Todo** – repite en bucle todas las pistas de tu cola del reproductor.
- **Repetir Una** – repite solo la pista actual.
- **Repetir Parar** – pausa la reproducción cuando termina la pista actual.
- **Sin Repetición** – deja que tu cola se reproduzca sin repetir.

#### Modo Aleatorio

Reproduce las pistas en un orden aleatorio. Esto baraja la cola y reproduce las pistas de una en una en el nuevo orden. Valores disponibles: **Aleatorio desactivado** y **Aleatorio activado**.

#### Procesador de Audio

Valores posibles: **AVFoundation** y **CoreAudio**. De forma predeterminada, se usa AVFoundation. Debido a un problema conocido con AVFoundation en iOS 17.0–17.6, el crossfade y el ecualizador de audio no se pueden usar al mismo tiempo. Para disfrutar de ambos en esas versiones de iOS, cambia al procesador de audio CoreAudio.

Si experimentas problemas con la reproducción sin pausas usando AVFoundation, prueba también CoreAudio. Las únicas limitaciones de CoreAudio son la transmisión por internet de algunas emisoras de radio y ciertos formatos de audio, ya que no admite todos los formatos de audio del sistema (como M4A y algunos otros).

#### Frecuencia de Muestreo de Salida de Audio

Establece la frecuencia de muestreo de salida de audio de 8 KHz a 384 KHz. Esta opción solo está disponible cuando se selecciona el procesador CoreAudio.

#### Número de Canales de Salida de Audio

Establece el número de canales de salida de audio — **MONO** o **ESTÉREO**. Esta opción solo está disponible cuando se selecciona el procesador CoreAudio.

#### Algoritmo de Tono de Audio

Elige el algoritmo utilizado para la corrección de tono. Los valores disponibles son **Time Domain**, **Spectral** y **Varispeed**. Útil si ajustas la velocidad de reproducción y quieres controlar la calidad de audio resultante.

#### Audio Espacial

El audio espacial utiliza métodos psicoacústicos para crear una experiencia de audio más envolvente en auriculares y configuraciones de altavoces compatibles. Valores posibles: **Desactivado**, **Mono y Estéreo**, **Multicanal**, **Mono Estéreo Multicanal**.

#### Modo de Salida de Audio

Disponible solo en iOS. Te permite activar el modo mixto para que el audio de esta aplicación se mezcle con otras aplicaciones. Puedes encontrar instrucciones sobre cómo usar el **Modo mixto** [aquí](/docs/howto/how-to-record-video-while-playing-music-on-iphone).

#### Guardar Posición de Reproducción

Asegura que la aplicación guarde y restaure la posición de reproducción de las canciones en tu biblioteca musical.

#### Guardar Estado del Reproductor de Audio

Guarda el estado del reproductor de audio antes de cerrar la aplicación, facilitando la reanudación desde donde lo dejaste.

Una vez que ambas funciones estén activadas, abre cualquier carpeta, álbum, artista o género. Verás una acción **Continuar Reproducción** en la parte superior de la pantalla, junto con la última canción guardada y la posición de reproducción. Toca **Continuar Reproducción** para restaurar. Para reanudar la reproducción de un archivo individual, simplemente tócalo.

### Personalización

Personaliza el aspecto de la pantalla del reproductor de audio, elige qué controles son visibles en el reproductor, la pantalla de bloqueo y la barra de estado, y configura los botones de salto de tiempo.

#### Estilo de Pantalla del Reproductor de Audio

Configura la posición de las barras de herramientas y los controles principales en el reproductor de audio.

#### Estilo de Desplazamiento de Portadas de Álbumes

Elige el estilo de desplazamiento de las portadas de álbumes en la pantalla del reproductor de audio.

#### Elementos Adicionales

Activa elementos extra en la pantalla del reproductor de audio. **Información de Formato de Audio** muestra la información técnica de la pista que se está reproduciendo encima de la portada; **Control Deslizante de Volumen de Audio** muestra el control deslizante de salida de audio debajo de los controles de reproducción.

#### Acciones de la Pantalla Principal

Configura qué botones son visibles en la pantalla principal del reproductor de audio. Las opciones disponibles incluyen Modo de Repetición y Aleatorio, Siguiente y Anterior Canción, Salto de Tiempo, Temporizador de Reposo, Google Chromecast, AirPlay y Bluetooth, Ecualizador de Audio, Búsqueda, **Marcadores**, Velocidad, Añadir Marcador, Añadir a **Favoritos**, **Comentarios** y más.

#### Controles de Reproducción en la Pantalla de Bloqueo

Elige qué controles extra están habilitados en la pantalla de bloqueo. Valores posibles: **Salto de Tiempo**, **Añadir Marcador** y **Añadir a Favoritos**.

#### Intervalos de Salto de Tiempo

Selecciona los intervalos de tiempo utilizados por los botones de Salto de Tiempo hacia adelante y hacia atrás.

### Carga de Archivos

Elige el tipo de red utilizado para transmitir canciones. Opciones disponibles: **Wi-Fi** y **Wi-Fi y Datos Móviles**.

#### Tiempo de Precarga

Establece el intervalo de tiempo de almacenamiento en búfer. Aumenta este valor si tienes una conexión de red deficiente.

#### Usar URL Directa

Cuando está activado, se usa una URL directa para cargar la canción si el servidor lo admite. Esto puede acelerar la carga de canciones, pero puede afectar ligeramente la estabilidad de la reproducción.

#### Optimizar Carga de Archivos

Cuando está activado, el sistema optimiza la carga de canciones para el procesador de audio AVFoundation, lo que puede mejorar la estabilidad de la reproducción. La app usa la tecnología descrita [aquí](/blog/audio-streaming-and-caching-in-ios-using-avassetresourceloader-and-avplayer/).

### Ecualizador de Audio

Configura el ecualizador de audio. Puedes leer más sobre presets y configuraciones de EQ [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Dispositivos

Conéctate a un dispositivo AirPlay o Google Chromecast (solo iOS).

### Velocidad de Reproducción

Ajusta la velocidad de reproducción del reproductor de audio. Para un control más preciso, activa el control deslizante preciso tocando el icono de configuración en la esquina superior derecha.

### Reproducción con Crossfade

El crossfade permite que las canciones fluyan sin interrupciones en una mezcla continua — la siguiente canción comienza a reproducirse unos segundos antes de que termine la actual. El crossfade no está disponible para AirPlay y Google Chromecast. En esta pantalla, elige cuánto tiempo se reproducen simultáneamente la canción actual y la siguiente. Si experimentas problemas con el crossfade y el ecualizador de audio al mismo tiempo, cambia el procesador de audio como se describe arriba.

### Reproducción Sin Pausas

La reproducción sin pausas asegura que las canciones se reproduzcan sin ninguna interrupción o silencio entre ellas. Es perfecta para música clásica, grabaciones en vivo y álbumes conceptuales. Si tienes problemas con la reproducción sin pausas, cambia el procesador de audio como se describe arriba.

### Caché de Reproducción

Las canciones en la cola del reproductor de audio se descargan automáticamente para una reproducción fluida. Si descargas archivos de audio manualmente, puedes deshabilitar esta opción para evitar duplicados. También puedes configurar el tamaño de la caché del reproductor de audio aquí. Lee más sobre el modo sin conexión y la caché de reproducción aquí: [Reproducir Música Sin Conexión en Evermusic y Flacbox: Descargar y Sincronizar de la Nube a Archivos Locales](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Temporizador de Reposo

Activa un temporizador para detener la reproducción después de un tiempo de espera especificado. Para un control más preciso, activa el modo preciso tocando el icono de configuración en la esquina superior derecha.

## Biblioteca

Los ajustes de la biblioteca musical — sincronización automática, lectura de metadatos, carga de portadas de álbumes, listas de reproducción, recientes y favoritos — están aquí.

### Lectura de Metadatos

Cuando añades pistas a la biblioteca, el lector de metadatos las procesa en segundo plano y las organiza por Artista, Álbum, Género y Compositor. Puedes ajustar la velocidad de lectura de metadatos para cargar datos más rápido (a costa de más batería). También puedes deshabilitar completamente el lector de metadatos y mostrar nombres de archivos en lugar de información de etiquetas.

El lector de metadatos solo actualiza la base de datos de la biblioteca musical; no altera los archivos almacenados en tu cuenta en la nube o en el almacenamiento local. Si necesitas editar los metadatos de archivos de audio, usa el editor de etiquetas integrado a través de la acción correspondiente en el menú de opciones.

Cuando la opción **Lectura de Metadatos en Segundo Plano** está activada, el lector continúa trabajando en modo de segundo plano. Si la app consume demasiada energía durante la reproducción, iOS puede suspenderla.

Si tienes una colección musical grande, es recomendable realizar la sincronización de metadatos en la versión de escritorio de la aplicación. Luego puedes transferir la biblioteca musical sincronizada a iOS usando la función **Copia de Seguridad y Restauración**.

Cuando la opción **Normalizar Codificación de Metadatos** está activada, la app normaliza automáticamente la codificación de metadatos para todas las canciones. Esto soluciona problemas donde la codificación de etiquetas de audio está dañada (por ejemplo, después de editar archivos en un PC con Windows) y evita que aparezcan caracteres incorrectos en la información de las pistas.

**Recargar Metadatos** marca cada archivo de tu biblioteca musical como que tiene metadatos faltantes, lo que hace que el lector de metadatos actualice cada registro.

**Iniciar Lectura de Metadatos** activa el lector de metadatos manualmente. El progreso se muestra debajo de la acción.

### Sincronización en Línea

La sincronización automática de música en línea añade pistas de los servicios en la nube conectados a la biblioteca musical automáticamente. Para activarla, abre los ajustes de la biblioteca musical y selecciona las carpetas de sincronización.

Con esta opción activada, la aplicación escanea las carpetas seleccionadas, identifica los archivos de audio compatibles y los añade a tu biblioteca. Inicia o detén la sincronización con la acción de menú correspondiente.

La sincronización en línea solo se ejecuta cuando la app está en primer plano, por lo que sincronizar una biblioteca grande puede llevar algún tiempo. Para acelerar el proceso, mantén la app abierta, conéctate a una fuente de energía y activa **Pantalla → Siempre Activa** en los ajustes.

Alternativamente, realiza la sincronización en línea en la versión de escritorio de la app y transfiere la biblioteca musical a iOS usando **Copia de Seguridad y Restauración**.

También puedes elegir con qué frecuencia se ejecuta la sincronización en línea. Establecer el intervalo en **Inmediatamente** activa una sincronización cada vez que abres la aplicación.

### Sincronización Sin Conexión

Configura la sincronización de música sin conexión.

#### Carpetas Sin Conexión Sincronizadas

Cuando marcas una carpeta en línea en tu servidor en la nube como disponible sin conexión (usando el menú **Más Acciones**), aparece aquí. El contenido de la carpeta se descarga en **Archivos Locales → Carpetas sin conexión**. Cuando la carpeta en línea cambia (archivos añadidos, eliminados o actualizados), la app comprueba los cambios y actualiza la copia local en tu dispositivo.

En esta pantalla puedes iniciar manualmente la sincronización de carpetas sin conexión, revelar la carpeta sin conexión en su carpeta contenedora y deshabilitar el modo sin conexión para la carpeta. Deshabilitar el modo sin conexión elimina todas las copias locales de archivos de tu dispositivo.

#### Intervalo de Tiempo

Elige con qué frecuencia la app comprueba las carpetas sin conexión en busca de modificaciones.

#### Iniciar Escaneo de Carpetas Locales

Escanea todas las carpetas locales en el directorio de Documentos de la aplicación en busca de archivos de audio compatibles. Los archivos encontrados se añaden a la biblioteca musical automáticamente. Los archivos ubicados en tu dispositivo pero fuera del directorio de Documentos de la aplicación deben añadirse a la biblioteca musical manualmente, ya que la app no puede acceder a ellos debido a las restricciones de seguridad de iOS/macOS.

**Importante:** Es recomendable iniciar periódicamente la sincronización de música sin conexión para mantener tu biblioteca musical actualizada con tus archivos locales.

### Personalización

Configura el estilo de la pantalla de la biblioteca musical. Hay tres opciones disponibles: **Menú simple**, **Menú agrupado** y **Menú por pestañas**. También puedes activar o desactivar las portadas de álbumes en la pantalla de detalles del álbum.

### Portadas de Álbumes

Elige cómo la aplicación carga y almacena las portadas de álbumes.

- **Tipo de red** — elige **Wi-Fi** o **Wi-Fi y Datos Móviles** para las descargas de portadas.
- **Cargar Portadas de Álbumes para Archivos en Línea** — cuando está activado, se cargan portadas de álbumes incrustadas para archivos almacenados en almacenamiento en la nube. Esto puede usar datos de red adicionales.
- **Buscar en la Carpeta** — cuando está activado, si una pista no tiene portada incrustada, la app busca imágenes JPEG o PNG en la misma carpeta y las usa como portada del álbum.
- **Calidad de Portada** — selecciona la calidad de las portadas de álbumes almacenadas en tu dispositivo.
- **Mostrar en Carpeta** — abre la carpeta donde se almacenan en caché las portadas de álbumes para que puedas gestionarlas o hacer copias de seguridad de ellas.
- **Eliminar Todo** — elimina las portadas de álbumes almacenadas en caché para liberar espacio de almacenamiento y forzar a la app a recargarlas a pedido.

### Listas de Reproducción

Activa la opción para añadir la misma canción a una lista de reproducción dos veces. De forma predeterminada, esta opción está desactivada.

### Recientes

Gestiona tu lista de canciones reproducidas recientemente.

- **Eliminar Lista** — elimina toda la lista de canciones reproducidas recientemente.
- **Cambiar Tamaño de Lista** — establece el número de elementos que aparecen en la lista.
- **Exportar Lista de Canciones** — exporta tu lista de canciones reproducidas recientemente como M3U, CSV o TXT. Las instrucciones detalladas están disponibles [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritos

Gestiona la lista de tus canciones favoritas.

- **Edición Simultánea** — cuando está activado, añadir una canción a favoritos la añade tanto en la biblioteca musical como en la sección de archivos simultáneamente.
- **Eliminar Lista** — elimina toda la lista de canciones favoritas.
- **Exportar Lista de Canciones** — como en Recientes, exporta favoritos como M3U, CSV o TXT.

### Eliminar Biblioteca Musical

Borra la base de datos de la biblioteca musical. Tus archivos de música en el almacenamiento no se ven afectados.

## Código de Acceso

Activa la pantalla de protección con contraseña si quieres proteger los datos de tu aplicación.

## Gestor de Archivos

La sección Gestor de Archivos controla cómo se transfieren, almacenan y previsualizan los archivos.

### Transferencias de Archivos

Elige tu preferencia de red para descargar archivos a tu dispositivo.

### Número Máximo de Tareas Paralelas

Establece el número de hilos de descarga paralelos. Un número más alto acelera las descargas pero requiere más batería.

### Tareas de Transferencia de Archivos

Muestra las tareas de carga y descarga actualmente activas.

### Transferencias en Segundo Plano

Permite descargas mientras la app está en segundo plano. Si las transferencias en segundo plano consumen mucha energía, iOS puede suspender la app.

### Guardar Archivos Descargados En

Elige el directorio de descargas predeterminado, o haz que la app te pregunte cada vez.

### Carpetas Sin Conexión Sincronizadas

Gestiona la sincronización sin conexión para las carpetas seleccionadas. Para activar la sincronización sin conexión, toca el botón de tres puntos junto a una carpeta y selecciona **Modo Disponible Sin Conexión**. Los nuevos archivos añadidos a la carpeta en la nube se descargan automáticamente a tu dispositivo. Lee más sobre los modos sin conexión [aquí](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervalo de Tiempo

Elige con qué frecuencia se sincronizan las carpetas sin conexión. **Inmediatamente** activa una sincronización cada vez que abres la app.

### Mostrar Nombres de Archivo Completos

Muestra los nombres de archivo completos, incluidas las extensiones, en el gestor de archivos.

### Editar Archivos en Línea

Deshabilita la edición de archivos en línea para cambiar al modo de solo lectura para los servicios en la nube conectados y evitar eliminaciones accidentales. Esta acción elimina las operaciones de edición de archivos de la interfaz de usuario.

### Copiar Archivos al Abrir

Especifica cómo la app gestiona los archivos importados desde otras aplicaciones.

### Miniaturas de Archivos

Gestiona y elimina las miniaturas de archivos generadas para liberar espacio de almacenamiento.

### Eliminar Archivos Temporales

Limpia la carpeta de caché de la aplicación para recuperar espacio de almacenamiento.

## Editor de Etiquetas de Audio

Configura el editor de etiquetas de audio integrado.

### Escalado de Portada de Álbum

Elige el método de escalado utilizado cuando se guarda una portada de álbum en las etiquetas de audio.

### Actualizar Archivos en Línea

Cuando está activado, la aplicación actualiza automáticamente los metadatos de un archivo en el servidor en la nube después de que termines de editarlo.

### Eliminar Archivo Después de Editar en Línea

Elige si la aplicación debe eliminar la copia descargada después de terminar la edición de un archivo en línea en un servidor en la nube.

### Botones de Pantalla Principal

Elige qué botones son visibles en la pantalla principal del editor de etiquetas de audio.

## Widgets

Activa los widgets para que la app actualice los datos del widget durante la reproducción. Las actualizaciones de widgets requieren energía adicional, así que activa esto solo si realmente usas widgets en tu Pantalla de Inicio o Pantalla de Bloqueo.

Puedes leer más sobre los widgets de Evermusic en la [guía de Navegación](/docs/guide/evermusic/evermusic-guide-navigation/).

## CarPlay

Cambia los ajustes de CarPlay aquí. Este menú también está disponible dentro de la interfaz de CarPlay para que puedas ajustar la experiencia mientras conduces.

### Ordenar

Configura las opciones de ordenación para todas las pantallas de CarPlay.

### Límite de Carga de Contenido

Elige si la app usa paginación en la pantalla de CarPlay. La paginación mantiene los menús respondiendo en dispositivos con memoria limitada y bibliotecas grandes.

### Color de Degradado de Iconos del Menú

Selecciona el esquema de color para la pantalla de inicio de CarPlay.

### Mostrar Imágenes

Deshabilita las imágenes en la pantalla de CarPlay para optimizar la velocidad de carga y reducir el uso de memoria en bibliotecas grandes.

### Pausar Reproducción al Conectar

Activa esto para evitar audio repentino y fuerte cuando conectas tu dispositivo a CarPlay.

## Wi-Fi Drive

Activa Wi-Fi Drive para transferir archivos desde un ordenador a tu dispositivo usando un navegador web de escritorio. Las instrucciones detalladas sobre cómo usar Wi-Fi Drive están disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalización

Personaliza la interfaz de usuario según tus preferencias.

### Icono de Aplicación

Elige un icono de aplicación alternativo para tu Pantalla de Inicio.

### Esquema de Color

Elige el tema de la interfaz de usuario y activa el modo oscuro. Cuando se selecciona **Predeterminado**, la aplicación sigue la configuración de apariencia de todo el dispositivo.

### Estilo de Fondo

Modifica el estilo de fondo de la aplicación. Actualmente, la única opción es **Portada de Álbum Difuminada**, que usa la portada de la pista que se está reproduciendo como fondo difuminado de la app.

### Apariencia de Elementos en la Lista

Ajusta cómo se muestran los elementos en las listas. Útil en pantallas pequeñas — puedes dejar que la app ajuste automáticamente la altura de las filas según el contenido, o mostrar iconos más pequeños en las celdas de la lista para dar más espacio al texto.

### Límite de Carga de Contenido

De forma predeterminada, la aplicación usa paginación para acelerar la carga de contenido. Puedes deshabilitar la paginación para cargar todo a la vez.

### Estilo de la Pantalla de Archivos Locales

Cambia el estilo de presentación de la sección **Archivos Locales**.

### Estilo de la Pantalla de Biblioteca Musical

Personaliza el aspecto de la pantalla de **Biblioteca Musical**.

### Estilo de la Pantalla del Reproductor de Audio

Configura el aspecto de la pantalla del **Reproductor de Audio**.

### Estilo del Menú Contextual

Elige el estilo del menú contextual que aparece cuando tocas el botón **Más Acciones**.

## Ventana

Disponible en Mac y Catalyst. Configura las preferencias relacionadas con la ventana, como el tamaño predeterminado y el comportamiento al iniciar.

## Pantalla

Elige si la pantalla debe mantenerse activa mientras usas la aplicación. Útil cuando escaneas bibliotecas grandes o realizas trabajos prolongados de edición de etiquetas.

## Accesibilidad

Activa el **Modo Texto** para ocultar todas las imágenes en la interfaz de usuario. El Modo Texto se activa automáticamente cuando VoiceOver está activo y también es útil para configuraciones muy pequeñas o solo de texto.

## Idioma

Cambia el idioma de la aplicación y anula el predeterminado del sistema. Actualmente la app admite las siguientes localizaciones: Afrikaans, Akan, Albanés, Amhárico, Árabe, Armenio, Asamés, Aymara, Azerbaiyano, Bambara, Bengalí, Vasco, Bielorruso, Bosnio, Búlgaro, Birmano, Catalán, Cebuano, Chino Simplificado, Chino Tradicional, Corso, Croata, Checo, Danés, Dhivehi, Dogri, Holandés, Inglés, Esperanto, Estonio, Ewe, Filipino, Finlandés, Francés, Gallego, Ganda, Georgiano, Alemán, Griego, Guaraní, Gujarati, Criollo Haitiano, Hausa, Hawaiano, Hebreo, Hindi, Hmong, Húngaro, Islandés, Igbo, Iloko, Indonesio, Irlandés, Italiano, Japonés, Javanés, Kannada, Kazajo, Jemer, Kinyarwanda, Coreano, Krio, Kurdo, Kurdo Sorani, Kirguís, Laosiano, Latín, Letón, Lingala, Lituano, Luxemburgués, Macedonio, Maithili, Malgache, Malayo, Malabar, Maltés, Māori, Marathi, Mizo, Mongol, Nepalés, Sotho del Norte, Noruego Bokmål, Nyanja, Odia, Oromo, Pastún, Persa, Polaco, Portugués, Punjabi, Rumano, Ruso, Samoano, Sánscrito, Gaélico Escocés, Serbio, Shona, Sindhi, Cingalés, Eslovaco, Esloveno, Somalí, Sotho del Sur, Español, Sundanés, Suajili, Sueco, Tayiko, Tamil, Tártaro, Telugu, Tailandés, Tsonga, Turco, Turcomano, Ucraniano, Urdu, Uigur, Uzbeko, Vietnamita, Galés, Xhosa, Yidis, Yoruba, Zulú.

## Copia de Seguridad y Restauración

Haz una copia de seguridad de todos los datos de tu aplicación o migrala a otro dispositivo. Puedes elegir qué incluir:

- **Base de datos** — todas las pistas y listas de reproducción de tu biblioteca musical. Las pistas sin conexión no se incluyen para mantener el tamaño de la copia de seguridad manejable.
- **Portadas de Álbumes** — todas tus portadas de álbumes almacenadas en caché.
- **Ajustes** — todos los ajustes de tu aplicación.

Toca **Hacer Copia de Seguridad de los Datos de la Aplicación** para iniciar la operación de copia de seguridad. Los datos de la aplicación se escriben en un único archivo que puedes usar más tarde para restaurar el estado de la aplicación en un dispositivo nuevo o después de reinstalar la app.

Para restaurar los datos de la aplicación en un dispositivo nuevo, mueve el archivo de copia de seguridad al nuevo dispositivo usando un servicio en la nube conectado o iCloud y ábrelo en el nuevo dispositivo.

Tenemos una guía detallada paso a paso aquí: [Cómo Transferir tu Biblioteca Musical Entre Dispositivos en Evermusic: Guía Paso a Paso](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ayuda

Abre la guía de la aplicación para obtener asistencia y orientación sobre cómo usar la app de forma efectiva.

## Preguntas Frecuentes

Encuentra respuestas a preguntas comunes en la sección de FAQ.

## Enviar Comentarios

¿Tienes comentarios o necesitas ayuda? Envía tus comentarios a nuestro equipo de soporte directamente desde la app.

## Compartir Esta App

Comparte la aplicación con tus amigos para ayudar a difundirla.

## Descubrir Más Apps

Explora otras apps de Everappz.

## Términos y Condiciones

Describe los términos y condiciones para usar la aplicación. Por favor, léelos antes de usar la aplicación.

## Política de Privacidad

Visita la página de política de privacidad para entender nuestras prácticas de manejo de datos. Por favor, léela antes de usar la aplicación.

## Análisis y Recopilación de Datos

Comprueba qué servicios están habilitados para análisis y recopilación de datos y desactiva los que no desees.

En **Evermusic Free (icono azul)**, los análisis y diagnósticos están habilitados de forma predeterminada para ayudarnos a mejorar la app — puedes desactivarlos aquí en cualquier momento. **Evermusic Pro (icono rojo) no incluye ningún análisis ni diagnóstico en absoluto** — la sección está vacía (u oculta) porque no se recopila nada, y no hay opción de activación.

## Avisos Legales

Contiene información sobre cada biblioteca utilizada en la aplicación junto con el número de versión de la app e información de compilación.
