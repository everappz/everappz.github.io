---
title: "Ajustes"
date: 2020-02-01
description: "Explora cada ajuste en Flacbox — desde preferencias de reproducción, motor de audio FFmpeg / sistema, salida de audio Hi-Res, ajustes del ecualizador, corrección de tono, duración del búfer IO, sincronización de metadatos, control de listas de reproducción, transferencias de archivos, widgets de pantalla de inicio, Apple CarPlay, personalización de UI, idioma, código de acceso, backup y restauración, y actualización a Premium."
keywords: [
  "ajustes Flacbox", "configuración reproductor de audio", "actualización premium Flacbox",
  "WiFi Drive", "sincronización de metadatos", "ecualizador", "velocidad de reproducción",
  "duplicados en lista", "ajustes gestor de archivos", "sincronización música offline",
  "editor de etiquetas de audio", "modo oscuro", "restaurar compras", "ajustes de backup",
  "ajustes widgets Flacbox", "ajustes CarPlay Flacbox",
  "ajustes FFmpeg Flacbox", "ajustes frecuencia de muestreo Flacbox",
  "ajustes corrección de tono Flacbox", "búfer IO Flacbox",
  "código de acceso Flacbox", "idioma Flacbox", "personalización Flacbox",
  "análisis Flacbox"
]
tags: ["guía", "flacbox", "ajustes"]
readingTime: 16
---


La pantalla de Ajustes es el centro de control de Flacbox. Desde aquí puedes actualizar a Premium, configurar el motor de audio (códecs del sistema o FFmpeg), gestionar tu biblioteca de música, configurar el gestor de archivos, personalizar el editor de etiquetas de audio, activar widgets de pantalla de inicio y Apple CarPlay, hacer copias de seguridad de tus datos y acceder a ayuda e información legal. Las secciones están agrupadas bajo los encabezados: Compras y Actualizaciones, Preferencias de la App, Ayuda y Legal y Privacidad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla Principal de Ajustes de Flacbox" image="/docs/guide/flacbox/img/settings-main.webp" >}}
{{< /cards >}}

## Actualizar a Premium

Actualiza la app a la versión Premium para eliminar todos los límites. La versión gratuita ofrece una compra única de por vida y dos opciones de suscripción (1 mes y 1 año) para eliminar todas las restricciones y actualizar a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Actualizar a Premium" image="/docs/guide/flacbox/img/upgrade-to-premium.webp" >}}
{{< /cards >}}

**Compartir en Familia** está habilitado para todas las compras y planes, para que puedas compartir la versión Premium con hasta cinco miembros de tu familia sin coste adicional.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Seleccionar un Plan Premium" image="/docs/guide/flacbox/img/select-premium-plan.webp" >}}
{{< /cards >}}

Puedes leer más sobre compras y la versión Premium aquí: [¿Cuál es la diferencia entre Flacbox y Flacbox Premium?](/docs/faq/flacbox/what-is-the-difference-between-flacbox-and-flacbox-premium/)

## Compartir Compras Entre iOS y Mac

Las compras de por vida y las suscripciones se comparten entre iOS y Mac, usando iCloud para sincronizar esta información. Si tienes la versión Premium en tu dispositivo iOS, asegúrate de tener instalada la última versión y que iCloud esté activado. Inicia la app en iOS y espera un minuto para que tu información de compra se suba a iCloud.

También puedes intentar tocar el botón Restaurar Compras en los ajustes de la app. Después, instala la última versión desde el App Store en tu Mac e inicia la app. Asegúrate de tener conexión a internet y de usar la misma cuenta de iCloud y App Store en Mac que usaste en iOS. Espera un minuto para que la app descargue la información de compra de iCloud.

## Restaurar Compras en un Nuevo Dispositivo

Para restaurar tu compra en un nuevo dispositivo, usa el menú Compras → Restaurar Compras. Verás la lista de tus compras. Si no ves todas, confirma que el dispositivo está conectado al mismo Apple ID que se usó para las compras y asegúrate de que iCloud esté activado.

## Probar Premium Gratis

Puedes actualizar a la versión Premium gratis, por tiempo limitado, usando este menú. Solo mira un anuncio o cuéntales a tus amigos sobre la app para obtener Premium gratis.

## Compras

Puedes restaurar compras anteriores desde este menú. Si encuentras errores de activación, intenta activar la opción Restaurar Compras al Iniciar la App.

## Actualización de Software

Toca Actualización de Software para comprobar si hay una versión más reciente de Flacbox disponible. La app comparará tu versión instalada con la última del App Store.

## Novedades

Este menú está disponible después de lanzar una nueva versión. Muestra un resumen de los cambios y nuevas funciones.

## Reproductor de Audio

Esta sección configura el reproductor de audio y el motor de audio subyacente, incluyendo la elección de FFmpeg / códec del sistema y las opciones de salida de audio Hi-Res.

### General

Estos ajustes cubren los aspectos fundamentales del reproductor de audio — cola de reproducción, salida de audio y guardado del estado del reproductor.

- **Modo de Repetición** — elige cómo se comporta el reproductor cuando termina una pista:
  - **Repetir Todo** — reproduce en bucle todas las pistas de tu cola.
  - **Repetir Una** — repite solo la pista actual.
  - **Repetir Stop** — pausa la reproducción cuando termina la pista actual.
  - **Sin Repetición** — permite que tu cola se reproduzca sin repetir.
- **Modo Aleatorio** — aleatoriza el orden de las pistas. Puedes activarlo (**Aleatorio activado**) o desactivarlo (**Aleatorio desactivado**).
- **Códec de Audio** — elige el motor de audio para la reproducción:
  - **Códec del Sistema + FFmpeg** — prioriza el códec del sistema donde sea posible. La corrección de tono y la frecuencia de muestreo pueden estar limitadas.
  - **FFmpeg** — fuerza el códec FFmpeg para todos los archivos, desbloqueando la corrección de tono y la frecuencia de muestreo.
- **Frecuencia de Muestreo de Salida de Audio** — ajusta para optimizar la calidad del sonido, especialmente útil con un DAC externo. Valores disponibles: **44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz** y **96 kHz**.
- **Número de Canales de Salida de Audio** — para sistemas multicanal con DAC externo: Mono, Estéreo, Centro / Izquierda / Derecha, Centro / Izquierda / Derecha / Surround, ITU BS.775-1, 5.1 Surround y SDDS.
- **Duración del Búfer IO Preferido de Salida de Audio** — configura la duración del búfer. Valor típico para minimizar latencia: **5 milisegundos (0,005 segundos)**.
- **Modo de Salida de Audio (solo iOS)** — configura la salida de audio mixta. Instrucciones detalladas [aquí](/docs/howto/how-to-record-video-while-playing-music-on-iphone).
- **Guardar Posición de Reproducción** — guarda y restaura la posición de reproducción.
- **Guardar Estado del Reproductor de Audio** — preserva el estado del reproductor antes de cerrar la app.

Con ambos **Guardar Posición de Reproducción** y **Guardar Estado del Reproductor de Audio** activados, abre cualquier carpeta, álbum, artista o género y verás un botón **Continuar Reproducción** en la parte superior.

### Personalización

La Personalización te permite personalizar el aspecto del reproductor, cambiar los controles disponibles y configurar los controles de salto de tiempo.

- **Estilo de Pantalla del Reproductor de Audio** — configura el posicionamiento de los elementos.
- **Estilo de Desplazamiento de Portadas** — configura el estilo de desplazamiento preferido.
- **Elementos Adicionales** — activa elementos extra. Información de Formato de Audio muestra info de audio sobre la portada; Deslizador de Volumen muestra el control de volumen bajo los controles.
- **Acciones de Pantalla Principal** — configura qué botones son visibles: Modo Repetir y Aleatorio, Canción Siguiente y Anterior, Saltar Tiempo, Temporizador de Sueño, Google Chromecast, AirPlay y Bluetooth, Ecualizador de Audio, Buscar, Marcadores, Velocidad, Añadir Marcador, Añadir a Favoritos, Comentarios y más.
- **Controles de Reproducción en la Pantalla de Bloqueo** — elige qué controles aparecen. Valores posibles: Saltar Tiempo, Añadir Marcador, Añadir a Favoritos.
- **Botones de Saltar Tiempo** — elige el intervalo de tiempo para los botones de salto.

### Carga de Archivos

Puedes cambiar el tipo de red usado para cargar canciones. Opciones disponibles: **Wi-Fi**, **Wi-Fi y Datos Móviles**.

- **Tiempo de Precarga** — establece el intervalo de almacenamiento en búfer.
- **Usar URL Directa** — cuando está activado, se usa una URL directa si el servidor lo admite.

### Ecualizador de Audio

Configura el ecualizador de 10 bandas, preajustes y preamplificador. Lee más [aquí](/docs/howto/how-to-use-the-audio-equalizer-on-your-iphone-ipad-mac-with-evermusic-and-flacbox).

### Velocidad de Reproducción

Ajusta la velocidad de **0,02× a 3,00×**. Toca el icono de configuración para **modo preciso**.

### Corrección de Tono

Cambia los ajustes usando valores predefinidos o **modo preciso**. Disponible en la ruta FFmpeg, rango de **-1000 a +1000**.

### Caché de Reproducción

Las canciones se descargan automáticamente. Puedes desactivar esto para evitar duplicados.

### Temporizador de Sueño

Activa un temporizador para detener la reproducción automáticamente. Toca el icono de configuración para **modo preciso**.

## Biblioteca

Tus ajustes de biblioteca — sincronización automática, lectura de metadatos, carga de portadas, listas de reproducción, recientes y favoritos — están aquí.

### Lectura de Metadatos

Cuando añades pistas, el **lector de metadatos** comienza a trabajar. Este proceso de fondo lee todos los metadatos y organiza por Artista, Álbum, Género y Compositor.

El lector de metadatos **solo actualiza metadatos en tu biblioteca** y no altera los archivos. Para editar metadatos en los archivos, usa el **editor de etiquetas** integrado.

Con **Lectura de Metadatos en Segundo Plano** activado, el lector continúa en modo de fondo.

**Recargar metadatos** marca todos los archivos como con metadatos faltantes para actualizar.

**Iniciar Lectura de Metadatos** activa el lector manualmente.

### Sincronización en Línea

La sincronización automática en línea añade pistas de servicios en la nube automáticamente.

La sincronización en línea solo funciona cuando la app está en primer plano. Puedes elegir con qué frecuencia se ejecuta. Configurar el intervalo en **Inmediatamente** activa una sincronización cada vez que abres la app.

### Sincronización Sin Conexión

Configura la sincronización de música sin conexión.

#### Carpetas offline sincronizadas

Cuando marcas una carpeta en línea como disponible sin conexión, aparece aquí. El contenido se descarga en **Archivos Locales → Carpetas Sin Conexión**.

#### Intervalo de Tiempo

Elige con qué frecuencia la app comprueba las carpetas sin conexión.

#### Iniciar Escaneo de Carpetas Locales

Escanea todas las carpetas locales en el directorio **Documents** de la app.

### Personalización

Configura el estilo de pantalla de biblioteca. Tres opciones: **Menú Simple, Menú Agrupado, Menú con Pestañas**.

### Portadas de Álbumes

Configura cómo la app carga y almacena artwork.

- **Tipo de Red** — elige **Wi-Fi** o **Wi-Fi y Datos Móviles**.
- **Cargar Portadas para Archivos en Línea** — carga portadas integradas para archivos en la nube.
- **Buscar en la Carpeta** — si una pista no tiene portada integrada, busca imágenes JPEG o PNG en la misma carpeta.
- **Calidad de Portada** — selecciona la calidad de las portadas almacenadas.
- **Mostrar en Carpeta** — abre la carpeta donde se almacenan las portadas en caché.
- **Eliminar Todo** — elimina las portadas en caché para liberar espacio.

### Listas de Reproducción

Activa la opción de añadir la misma canción dos veces. Por defecto, esta opción está desactivada.

### Recientes

Gestiona tu lista de canciones reproducidas recientemente.

- **Eliminar Lista** — elimina toda la lista.
- **Cambiar Tamaño de Lista** — establece el número de elementos.
- **Exportar Lista de Canciones** — exporta como M3U, CSV o TXT. Instrucciones [aquí](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/).

### Favoritos

Gestiona la lista de canciones favoritas.

- **Edición Simultánea** — cuando está activado, añadir a favoritos lo añade tanto en la biblioteca como en la sección de archivos.
- **Eliminar Lista** — elimina toda la lista de favoritas.
- **Exportar Lista de Canciones** — exporta como M3U, CSV o TXT.

### Eliminar Biblioteca Musical

Borra la base de datos de la biblioteca. Los archivos en el almacenamiento no se ven afectados.

## Código de Acceso

Activa la pantalla de código de acceso para proteger los datos de la app con un código numérico de 4 dígitos. Combínalo con Face ID / Touch ID para mayor protección.

## Gestor de Archivos

La sección Gestor de Archivos controla cómo se transfieren, almacenan y previsualizan los archivos.

### Transferencias de Archivos

Elige tu preferencia de red para descargar archivos.

### Número Máximo de Tareas Paralelas

Establece el número de hilos de descarga paralelos.

### Tareas de Transferencia de Archivos

Muestra las tareas de carga y descarga activas actualmente.

### Transferencias en Segundo Plano

Permite descargas mientras la app está en segundo plano.

### Guardar Archivos Descargados En

Elige el directorio de descargas predeterminado.

### Carpetas Offline Sincronizadas

Gestiona la sincronización offline para carpetas seleccionadas. Lee más [aquí](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

### Intervalo de Tiempo

Elige con qué frecuencia se sincronizan las carpetas sin conexión.

### Mostrar Nombres de Archivo Completos

Muestra los nombres de archivo completos incluyendo extensiones.

### Editar Archivos en Línea

Desactiva la edición de archivos en línea para cambiar a modo de solo lectura.

### Copiar Archivos al Abrir

Especifica cómo la app maneja los archivos importados de otras aplicaciones.

### Miniaturas de Archivos

Gestiona y elimina miniaturas de archivos generadas para liberar espacio.

### Eliminar Archivos Temporales

Vacía la carpeta de caché de la app para recuperar espacio.

## Editor de Etiquetas de Audio

Configura el editor de etiquetas de audio integrado.

### Escalado de Portada de Álbum

Elige el método de escalado al guardar una portada en etiquetas de audio.

### Actualizar Archivos en Línea

Cuando está activado, la app actualiza automáticamente los metadatos de un archivo en el servidor en la nube tras editarlo.

### Eliminar Archivo Después de Editar en Línea

Elige si la app debe eliminar la copia descargada después de editar un archivo en línea.

### Botones de Pantalla Principal

Elige qué botones son visibles en la pantalla principal del editor de etiquetas.

Para edición por lotes de muchos archivos a la vez, instala nuestra app complementaria **Evertag**.

## Widgets

Activa widgets para que la app actualice los datos durante la reproducción. Actívalo solo si usas widgets en tu Pantalla de Inicio o Pantalla de Bloqueo.

Puedes añadir widgets de Flacbox manteniendo pulsada tu Pantalla de Inicio o Pantalla de Bloqueo, tocando **+**, buscando **Flacbox** y eligiendo un tamaño de widget.

## CarPlay

Cambia los ajustes de CarPlay aquí.

### Ordenar

Configura las opciones de ordenación para todas las pantallas de CarPlay.

### Límite de Carga de Contenido

Elige si la app usa paginación en la pantalla de CarPlay.

### Color Degradado de Iconos del Menú

Selecciona el esquema de colores para la pantalla de inicio de CarPlay.

### Mostrar Imágenes

Desactiva las imágenes en la pantalla de CarPlay para optimizar la velocidad de carga.

### Pausar Reproducción al Conectar

Activa esto para evitar audio repentino y fuerte al conectar el dispositivo a CarPlay.

## Wi-Fi Drive

Activa **Wi-Fi Drive** para transferir archivos desde un ordenador. Instrucciones detalladas [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Personalización

Personaliza la interfaz de usuario según tus preferencias.

### Icono de Aplicación

Elige un icono alternativo para tu Pantalla de Inicio (Premium).

### Esquema de Color

Elige el tema de la interfaz y activa el modo oscuro.

### Estilo de Fondo

Modifica el estilo de fondo. La única opción actual es **Portada de Álbum Difuminada**.

### Apariencia de los Elementos de la Lista

Ajusta cómo se muestran los elementos en las listas.

### Límite de Carga de Contenido

Por defecto la app usa paginación. Puedes desactivarla para cargar todo a la vez.

### Estilo de Pantalla de Archivos Locales

Cambia el estilo de presentación de la sección **Archivos Locales**.

### Estilo de Pantalla de Biblioteca Musical

Personaliza el aspecto de la pantalla **Biblioteca Musical**.

### Estilo de Pantalla del Reproductor de Audio

Configura el aspecto de la pantalla del **Reproductor de Audio**.

### Estilo del Menú Contextual

Elige el estilo del menú contextual que aparece al tocar el botón **Más Acciones**.

## Ventana

Disponible en Mac y Catalyst. Configura preferencias relacionadas con la ventana.

## Pantalla

Elige si la pantalla debe permanecer activa mientras usas la app.

## Accesibilidad

Activa el **Modo Texto** para ocultar todas las imágenes. Se activa automáticamente cuando VoiceOver está activo.

## Idioma

Cambia el idioma de la app. El cambio se aplica después de cerrar completamente y volver a abrir Flacbox. Los idiomas admitidos actualmente incluyen: Afrikáans, Akan, Albanés, Amhárico, Árabe, Armenio, Asamés, Aymara, Azerbaiyano, Bambara, Bengalí, Vasco, Bielorruso, Bosnio, Búlgaro, Birmano, Catalán, Cebuano, Chino (Simplificado), Chino (Tradicional), Corso, Croata, Checo, Danés, Divehi, Dogri, Neerlandés, Inglés, Esperanto, Estonio, Ewe, Filipino, Finlandés, Francés, Gallego, Ganda, Georgiano, Alemán, Griego, Guaraní, Gujarati, Criollo Haitiano, Hausa, Hawaiano, Hebreo, Hindi, Hmong, Húngaro, Islandés, Igbo, Ilocano, Indonesio, Irlandés, Italiano, Japonés, Javanés, Kannada, Kazajo, Jemer, Kinyarwanda, Coreano, Krio, Kurdo, Kurdo Soraní, Kirguís, Lao, Latín, Letón, Lingala, Lituano, Luxemburgués, Macedonio, Maithili, Malgache, Malayo, Malayalam, Maltés, Maorí, Maratí, Mizo, Mongol, Nepalí, Sotho del Norte, Noruego Bokmål, Nyanja, Odia, Oromo, Pastún, Persa, Polaco, Portugués, Punjabi, Rumano, Ruso, Samoano, Sánscrito, Gaélico Escocés, Serbio, Shona, Sindhi, Cingalés, Eslovaco, Esloveno, Somalí, Sotho del Sur, Español, Sundanés, Suajili, Sueco, Tayiko, Tamil, Tártaro, Telugu, Tailandés, Tsonga, Turco, Turcomano, Ucraniano, Urdu, Uigur, Uzbeko, Vietnamita, Galés, Xhosa, Yidis, Yoruba, Zulú.

## Backup y Restauración

Usa esta función para hacer copias de seguridad de todos los datos de la app o migrarlos a otro dispositivo. Puedes elegir qué incluir:

- **Base de Datos** — todas tus pistas en la biblioteca, incluyendo listas de reproducción.
- **Portadas de Álbumes** — todas tus portadas en caché.
- **Ajustes** — todos los ajustes de la app.

Toca **Hacer Copia de Seguridad de los Datos** para iniciar. Para restaurar en un nuevo dispositivo, mueve el archivo de copia de seguridad usando un servicio en la nube o iCloud.

Instrucciones detalladas: [Cómo Transferir tu Biblioteca Musical Entre Dispositivos](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide).

## Ayuda

Accede a la guía de la app para obtener asistencia.

## Preguntas Frecuentes

Encuentra respuestas a preguntas comunes en la sección de FAQ.

## Enviar Comentarios

¿Tienes comentarios o necesitas ayuda? Envía tus comentarios a nuestro equipo de soporte directamente desde la app.

## Compartir Esta App

Comparte la app con tus amigos para correr la voz.

## Descubrir Más Apps

Explora otras apps de Everappz.

## Términos y Condiciones

Describe los términos de uso de la app. Por favor, léelos antes de usar la app.

## Política de Privacidad

Visita la página de política de privacidad para entender nuestras prácticas de manejo de datos.

## Análisis y Recopilación de Datos

Comprueba qué servicios están habilitados para análisis y recopilación de datos y desactiva los que no quieras.

## Avisos Legales

Contiene información sobre cada biblioteca usada en la app junto con el número de versión e información de compilación.
