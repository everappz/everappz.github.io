---
title: "Ajustes"
date: 2020-02-01
lastmod: 2026-06-01
description: "Explora cada ajuste en Evervideo — Reproductor multimedia (Imagen en imagen, decodificación por hardware H.264/HEVC, ecualizador de vídeo, escalado, rotación, puerto de vista VR), Audio (ecualizador, frecuencia de muestreo, canales, buffer IO, modo mixto), Subtítulos (primario/secundario, fuente, archivo externo, libass), Biblioteca multimedia, Gestor de archivos, Wi-Fi Drive, Widgets, Personalización, Idioma, Código de acceso, Copia de seguridad y restauración — para iPhone, iPad y Mac."
keywords: [
  "ajustes Evervideo", "configuración reproductor de vídeo", "actualización Premium Evervideo",
  "ajustes Imagen en imagen", "ajustes ecualizador de vídeo",
  "modo escalado de vídeo", "rotación de vídeo", "decodificador hardware iPhone",
  "ajustes de subtítulos", "subtítulos secundarios iOS", "ajustes libass",
  "archivo externo de subtítulos", "fuente de subtítulos",
  "ajustes ecualizador de audio", "frecuencia de muestreo de salida de audio",
  "canales de salida de audio", "duración del buffer IO", "modo mixto de audio",
  "Wi-Fi Drive vídeo", "widgets Evervideo",
  "copia de seguridad restauración Evervideo", "código de acceso Evervideo",
  "idioma Evervideo", "personalización Evervideo"
]
tags: ["guía", "evervideo", "ajustes"]
readingTime: 16
---


La pantalla de Ajustes es el centro de control de Evervideo. Desde aquí puedes actualizar a Premium, configurar los motores de vídeo y audio (códecs del sistema o FFmpeg), gestionar Imagen en imagen, configurar subtítulos (primarios, secundarios, libass, archivos externos, fuentes), organizar la biblioteca multimedia, configurar el gestor de archivos, activar widgets de la pantalla de inicio, hacer copias de seguridad de tus datos y acceder a ayuda e información legal. Las secciones están agrupadas bajo encabezados: Compras y actualizaciones, Preferencias de la app, Ayuda, Legal y privacidad.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla principal de Ajustes de Evervideo" image="/docs/guide/evervideo/img/evervideo-settings.webp" >}}
{{< /cards >}}

## Actualizar a Premium

Actualiza la aplicación a la versión Premium para eliminar todos los límites. La versión gratuita ofrece una compra única de por vida en la aplicación y dos opciones de suscripción (1 mes y 1 año) para eliminar todas las restricciones y actualizar a Premium.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Actualizar a Premium" image="/docs/guide/evervideo/img/evervideo-upgrade-to-premium.webp" >}}
{{< /cards >}}

**Compartir en familia** está habilitado para todas las compras y planes, por lo que puedes compartir la versión Premium con hasta cinco miembros de tu familia sin coste adicional.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Seleccionar un plan Premium" image="/docs/guide/evervideo/img/evervideo-select-premium-plan.webp" >}}
{{< /cards >}}

## Compartir compras entre iOS y Mac

Las compras de por vida y las suscripciones se comparten entre iOS y Mac usando **iCloud** para sincronizar esta información. Si tienes Premium en tu dispositivo iOS, asegúrate de tener la última versión instalada y de que iCloud esté habilitado. Inicia la app en iOS y espera un minuto para que la información de compra se suba a iCloud, luego inicia la versión Mac — Premium debería activarse automáticamente.

También puedes tocar el botón **Restaurar compras** en los ajustes de la app. Asegúrate de tener conexión a internet y de haber iniciado sesión con la misma cuenta de iCloud y App Store en ambos dispositivos.

## Restaurar compras en un dispositivo nuevo

Para restaurar tu compra en un dispositivo nuevo, usa el menú **Compras → Restaurar compras**. Verás la lista de tus compras. Si no ves todas, confirma que el dispositivo está conectado con el mismo Apple ID que se usó para las compras y asegúrate de que iCloud esté habilitado.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de Compras de Evervideo en Ajustes" image="/docs/guide/evervideo/img/evervideo-purhases-menu-in-settings.webp" >}}
{{< /cards >}}

## Probar Premium gratis

Puedes actualizar a la versión Premium de forma gratuita, por tiempo limitado, usando este menú. Solo tienes que ver un anuncio o contarle a tus amigos sobre la app.

## Actualización de software

Toca **Actualización de software** para comprobar si hay una versión más reciente de Evervideo disponible en el App Store.

## Novedades

Este menú está disponible después de publicar una nueva versión. Muestra un resumen de los cambios y nuevas funciones de la actualización más reciente.

## Reproductor

Todo lo relacionado con la reproducción está aquí — audio, vídeo, subtítulos, dispositivos, personalización, caché y el temporizador de sueño.

### General

Estos ajustes cubren los aspectos fundamentales del reproductor.

- **Modo de repetición** — elige cómo se comporta el reproductor cuando termina un vídeo:
  - **Repetir todo** — reproduce todos los vídeos de la cola de nuevo.
  - **Repetir uno** — repite solo el vídeo actual.
  - **Detener al repetir** — pausa cuando termina el vídeo actual.
  - **Sin repetición** — reproduce la cola una vez sin repetir.
- **Modo aleatorio** — aleatoriza el orden de los vídeos en la cola (**Activado** o **Desactivado**).
- **Guardar posición de reproducción** — guarda y restaura la posición de reproducción de los vídeos en tu biblioteca.
- **Guardar estado del reproductor** — conserva el estado del reproductor antes de cerrar la app, para que puedas retomar donde lo dejaste.

### Vídeo

Configura cómo Evervideo decodifica y renderiza el vídeo.

- **Decodificación hardware H.264** — activa/desactiva la decodificación AVC acelerada por hardware. Úsala cuando la duración de batería y el rendimiento térmico importan; desactívala para compatibilidad con perfiles exóticos.
- **Decodificación hardware H.265 (HEVC)** — lo mismo para HEVC. Los iPhone, iPad y Mac modernos decodifican HEVC eficientemente.
- **Formato de píxel preferido** — elige el formato de píxel que el reproductor presenta al renderizador (los valores predeterminados están ajustados para el dispositivo).
- **FPS preferidos** — establece un FPS de reproducción objetivo. Útil para ajustar una frecuencia de actualización de monitor específica.
- **Modo de escalado de vídeo** — Ajustar / Rellenar / Estirar / Original. Determina cómo la imagen llena el área de visualización.
- **Modo de visualización de vídeo** (iOS / iPadOS) — cómo se presenta el vídeo en la vista del reproductor.
- **Rotación de vídeo** — rota manualmente la imagen 0° / 90° / 180° / 270° (útil para vídeos grabados con orientación incorrecta).
- **Ecualizador de vídeo** — ajusta brillo, contraste, saturación y tono con vista previa en tiempo real. Los presets personalizados pueden **exportarse e importarse**.
- **Puerto de vista VR** (iOS / iPadOS) — para vídeos esféricos de 360°. Arrastra para mirar alrededor, pellizca para hacer zoom.
- **Imagen en imagen (PiP)** (iOS / iPadOS) — activa el soporte PiP; la app cambiará a una ventana de reproductor flotante cuando envíes la app al fondo o toques el botón PiP.

### Audio

Configura la reproducción y la salida de audio.

- **Pista de audio** — elige la secuencia de audio cuando un vídeo tiene varias (comentarios, doblaje, etc.).
- **Ecualizador de audio** — EQ de 10 bandas con presets y preamplificador. Los presets personalizados pueden exportarse/importarse.
- **Frecuencia de muestreo de salida de audio** — 44,1 kHz, 48 kHz, 64 kHz, 88,2 kHz, 96 kHz. Útil con DACs externos.
- **Número de canales de salida de audio** — Mono, Estéreo, 5.1, ITU BS.775-1, SDDS y más.
- **Duración preferida del buffer IO de salida de audio** — el valor típico para reproducción hi-res de baja latencia es alrededor de 5 ms (0,005 s). Ajusta para tu hardware.
- **Modo de salida de audio** (solo iOS) — el modo mixto permite que el audio de Evervideo se mezcle con otras apps.

### Subtítulos

Evervideo incluye soporte completo de subtítulos.

- **Pista de subtítulos** — elige entre las pistas de subtítulos incrustadas en el archivo.
- **Archivo de subtítulos externo** — carga un archivo externo `.srt`, `.vtt`, `.ass` o `.ssa` desde tu dispositivo o cualquier servicio en la nube conectado.
- **Fuente** — elige una fuente para la pista de subtítulos principal.

### Dispositivos (solo iOS/iPadOS)

Elige un dispositivo **AirPlay** o **Google Chromecast** para la salida de vídeo.

### Personalización

- **Estilo de diseño del reproductor** — Mínimo (predeterminado para Evervideo), Inferior, Antiguo, Clásico y más.
- **Acciones de la pantalla principal** — elige qué botones aparecen en la pantalla principal del reproductor.
- **Controles de la pantalla de bloqueo** — Saltar tiempo, Añadir marcador, Añadir a favoritos.
- **Intervalos de tiempo de salto** — elige el intervalo de tiempo para los botones de salto (5 s, 10 s, 15 s, 30 s, etc.).
- **Estilo de desplazamiento de portadas de álbumes** — estilo de desplazamiento preferido para las carátulas.
- **Elementos adicionales** — Información de formato de audio, Control deslizante de volumen.

### Carga de archivos

Configura cómo se transmiten los datos de vídeo desde la red.

- **Tipo de red** — solo Wi-Fi, o Wi-Fi + Datos móviles.
- **Tiempo de precarga** — longitud del buffer para una reproducción más fluida en redes lentas.
- **Usar URL directa** — cuando se admita, usa una URL directa para una carga más rápida.

### Caché de reproducción

Los vídeos en la cola del reproductor se descargan automáticamente para garantizar una reproducción fluida. Puedes desactivar esta opción o configurar el tamaño de la caché aquí.

### Temporizador de sueño

Activa un temporizador para detener automáticamente la reproducción después de un período especificado. Toca el icono de configuración para el **modo preciso** con granularidad minuto a minuto.

## Biblioteca multimedia

Gestiona la sincronización automática, los metadatos, las portadas de álbumes, las listas de reproducción, los recientes y los favoritos.

### Lectura de metadatos

Cuando añades vídeos a la biblioteca, el lector de metadatos los escanea en segundo plano y los organiza por Álbum y Género. Puedes ajustar la velocidad de escaneo, desactivar el lector o activar un re-escaneo completo con **Recargar metadatos**. **Normalizar codificación de metadatos** corrige automáticamente codificaciones de caracteres rotas (común con archivos de PC con Windows).

### Sincronización en línea

Añade automáticamente vídeos de los servicios en la nube y servidores multimedia conectados a tu biblioteca. Elige qué carpetas escanear, configura con qué frecuencia debe sincronizarse la app e inicia/detiene la sincronización manualmente. La sincronización en línea solo se ejecuta mientras la app está activa — para bibliotecas grandes, usa la versión de escritorio y luego transfiere la biblioteca sincronizada con **Copia de seguridad y restauración**.

### Sincronización sin conexión

Cuando marcas una carpeta de la nube como disponible sin conexión, aparece en **Archivos → Carpetas sin conexión** y se descarga automáticamente. Los archivos nuevos añadidos en línea también se descargan. Configura el intervalo de tiempo e inicia sincronizaciones manuales desde esta pantalla.

### Personalización

- **Estilo de pantalla de biblioteca multimedia** — Menú simple, Menú agrupado, Menú con pestañas.
- Activa/desactiva la visualización de grandes portadas de álbumes en las pantallas de detalles.

### Portadas de álbumes

- **Tipo de red** — Wi-Fi o Wi-Fi + Datos móviles.
- **Cargar portadas de álbumes para archivos en línea** — obtiene la carátula incrustada de los archivos en la nube (usa datos adicionales).
- **Buscar en la carpeta** — usa imágenes JPEG/PNG en la misma carpeta cuando un vídeo no tiene portada incrustada.
- **Calidad de portada** — ajusta la resolución a la que se almacenan en caché las portadas.
- **Mostrar en carpeta** / **Eliminar todo** — gestiona la caché de carátulas.

### Listas de reproducción

Activa la adición del mismo vídeo a una lista de reproducción dos veces (desactivado por defecto).

### Recientes

Gestiona la lista de vídeos reproducidos recientemente — cambia el tamaño, elimina o exporta como M3U / CSV / TXT.

### Favoritos

- **Edición simultánea** — sincroniza los favoritos entre la biblioteca multimedia y la sección de archivos.
- **Eliminar lista** — borra la lista de favoritos.
- **Exportar lista de canciones** — exporta los favoritos como M3U / CSV / TXT.

### Eliminar biblioteca multimedia

Borra la base de datos de la biblioteca multimedia. Tus archivos de vídeo y audio en el almacenamiento permanecen intactos.

## Código de acceso

Protege Evervideo con un **código de acceso numérico de 4 dígitos**. Cuando está habilitado, se te pedirá que introduzcas el código cada vez que la app se inicie. Combínalo con Face ID / Touch ID de iOS en el dispositivo para mayor protección.

## Gestor de archivos

Controla cómo se transfieren, almacenan y previsualizan los archivos.

- **Transferencias de archivos** — preferencia de red (solo Wi-Fi o Wi-Fi + Datos móviles).
- **Número máximo de tareas paralelas** — establece el número de hilos de descarga paralelos.
- **Tareas de transferencia de archivos** — ve las cargas y descargas actualmente activas.
- **Transferencias en segundo plano** — permite descargas mientras la app está en segundo plano.
- **Guardar archivos descargados en** — directorio de descargas predeterminado.
- **Carpetas sin conexión sincronizadas** — gestiona las carpetas en modo sin conexión.
- **Intervalo de tiempo** — con qué frecuencia se comprueban las carpetas sin conexión para detectar cambios.
- **Mostrar nombres completos de archivos** — muestra extensiones en el gestor de archivos.
- **Editar archivos en línea** — desactiva para cambiar al modo de solo lectura para los servicios en la nube conectados.
- **Copiar archivos al abrir** — cómo manejar los archivos importados de otras apps.
- **Miniaturas de archivos** — gestiona las miniaturas de archivos generadas.
- **Eliminar archivos temporales** — limpia la carpeta de caché de la aplicación.

## Wi-Fi Drive

Activa Wi-Fi Drive para transferir archivos de un ordenador a tu dispositivo usando un navegador web de escritorio, Finder o Explorador de archivos. Las instrucciones detalladas están disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Widgets

Activa los widgets para que la app actualice los datos de los widgets durante la reproducción. Las actualizaciones de widgets requieren energía adicional, por lo que el interruptor está desactivado por defecto — actívalo solo si usas widgets en la pantalla de inicio o de bloqueo.

Puedes añadir widgets de Evervideo manteniendo pulsada la pantalla de inicio o de bloqueo, tocando **+**, buscando **Evervideo** y eligiendo un tamaño de widget. Los widgets muestran el vídeo que se está reproduciendo y enlazan directamente al reproductor en pantalla completa. Los widgets también funcionan en macOS en el Centro de notificaciones.

## Personalización

Personaliza la interfaz de usuario según tus preferencias.

- **Icono de la aplicación** — icono alternativo para la pantalla de inicio (Premium).
- **Esquema de colores** — Oscuro, Claro o Predeterminado (sigue la apariencia del sistema).
- **Estilo de fondo** — Portada de álbum difuminada o color sólido.
- **Apariencia de los elementos en la lista** — ajuste automático de la altura de fila; muestra miniaturas más pequeñas.
- **Límite de carga de contenido** — activa/desactiva la paginación.
- **Estilo de pantalla de archivos** — Menú simple o Menú agrupado.
- **Estilo de pantalla de biblioteca multimedia** — Simple / Agrupado / Menú con pestañas.
- **Estilo de pantalla del reproductor** — Mínimo / Inferior / Antiguo / Clásico.
- **Estilo del menú contextual** — menú del sistema o estilo de hoja inferior.

## Ventana

Disponible en Mac y Catalyst. Configura las preferencias relacionadas con la ventana, como el tamaño predeterminado y el comportamiento al iniciar.

## Pantalla

Elige si la pantalla debe permanecer activa mientras usas la aplicación.

## Accesibilidad

Activa el **Modo de texto** para ocultar imágenes en la interfaz de usuario. El modo de texto se activa automáticamente cuando VoiceOver está activo.

## Idioma

Cambia el idioma de la aplicación y anula el predeterminado del sistema. El cambio se aplica después de cerrar completamente y volver a abrir Evervideo. Se admiten más de 120 idiomas.

## Copia de seguridad y restauración

Haz una copia de seguridad de todos los datos de tu aplicación o mígralos a otro dispositivo. Elige qué incluir:

- **Base de datos** — las entradas de tu biblioteca multimedia, listas de reproducción, valoraciones, favoritos, historial de visualización. Los archivos sin conexión no se incluyen para mantener el tamaño del archivo manejable.
- **Portadas de álbumes** — tu carátula almacenada en caché.
- **Ajustes** — los ajustes de tu aplicación.

Toca **Hacer copia de seguridad de los datos** para iniciar la copia de seguridad. Para restaurar en un dispositivo nuevo, mueve el archivo de copia de seguridad a través de iCloud Drive, AirDrop o cualquier servicio en la nube conectado y ábrelo en el nuevo dispositivo.

## Ayuda

Accede a la guía de la aplicación para obtener asistencia y orientación sobre el uso efectivo de la app.

## Preguntas frecuentes

Encuentra respuestas a preguntas comunes en la sección de Preguntas frecuentes.

## Enviar comentarios

Envía tus comentarios a nuestro equipo de soporte directamente desde la app, con información de diagnóstico adjunta automáticamente.

## Compartir esta aplicación

Comparte Evervideo con tus amigos para difundir la palabra.

## Descubrir más aplicaciones

Explora otras aplicaciones de Everappz.

## Términos y condiciones

Lee los términos y condiciones antes de usar la aplicación.

## Política de privacidad

Lee la política de privacidad para entender nuestras prácticas de manejo de datos.

## Análisis y recopilación de datos

Comprueba qué servicios están habilitados para análisis y recopilación de datos y desactiva los que no desees.

## Avisos legales

Información sobre cada biblioteca utilizada en la aplicación junto con el número de versión e información de compilación de la app.
