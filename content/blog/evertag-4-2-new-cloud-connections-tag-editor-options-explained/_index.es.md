---
title: "Evertag 4.2: nuevas conexiones de nube y opciones del editor de etiquetas"
date: 2026-05-09
description: "Evertag 4.2 añade conexiones a Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP y NFS, renueva Wi-Fi Drive y actualiza la interfaz para Liquid Glass. Esta entrada también explica todas las opciones del editor de etiquetas — incluyendo ID3v2.4 frente a ID3v2.3, escalado de la carátula, etiquetas duplicadas, modos de subida a la nube y los ajustes correctos para Spotify y otros servicios de streaming."
keywords: ["Evertag 4.2", "actualización Evertag", "editor de etiquetas ID3 iPhone", "ID3v2.4 vs ID3v2.3", "editar etiquetas FLAC iOS", "editar etiquetas MP3 iPhone", "editar carátulas iOS", "editor de etiquetas para Spotify", "editor de etiquetas Plex", "editor de etiquetas Apple Music", "editor de etiquetas en la nube Evertag", "editor de etiquetas Internxt", "editor de etiquetas Proton Drive", "editor de etiquetas QNAP", "editor de etiquetas Nextcloud", "editor de etiquetas Amazon S3", "editor de etiquetas SFTP iPhone", "editor de etiquetas FTP audio", "editor de etiquetas NFS iPhone", "Wi-Fi Drive editor de etiquetas", "duplicar etiquetas ID3", "escalado de carátula", "diseño Liquid Glass", "editor de metadatos de audio iOS 2026"]
tags: ["Evertag", "Evertag 4.2", "Editor de etiquetas", "ID3", "ID3v2.4", "ID3v2.3", "Etiquetas FLAC", "Etiquetas MP3", "Carátula", "Internxt", "Proton Drive", "QNAP", "Nextcloud", "Amazon S3", "SFTP", "FTP", "NFS", "Wi-Fi Drive", "Liquid Glass", "Novedades"]
cascade:
  type: docs
authors:
  - name: "Anna Kosenko"
    link: "https://www.linkedin.com/in/anna-kosenko-kosenko/"
    image: "/images/about/anna-kosenko-administrator-everappz.webp"
---

{{< author-byline >}}

**TL;DR:** [Evertag 4.2](/products/evertag) es una actualización mayor del editor de etiquetas de audio para iPhone, iPad y Mac. Hemos eliminado errores clave de edición de etiquetas y añadido más de 6 nuevas conexiones a la nube y a servidores: **Internxt**, **Proton Drive**, **QNAP**, **Nextcloud**, **Amazon S3**, además de los protocolos **FTP**, **SFTP** y **NFS**. Wi-Fi Drive estrena interfaz renovada, modo de selección múltiple, una cola de subida más inteligente y transferencias más rápidas. Toda la app está afinada para el diseño **Liquid Glass**. Esta entrada también profundiza en los ajustes del editor de etiquetas — explicando **ID3v2.4 frente a ID3v2.3**, **escalado de la carátula**, **etiquetas duplicadas**, **modos de subida a la nube**, **eliminación del archivo descargado** y exactamente qué opciones elegir si preparas audio para **Spotify**, **Apple Music**, **Plex**, **Jellyfin** o cualquier otro servicio de streaming.

---

## ¡Hola a todos!

Llega una gran actualización de Evertag. Hemos eliminado errores clave de edición de etiquetas y añadido **más de 6 nuevas conexiones a la nube y a servidores** para que gestionar los metadatos de tu audio sea más fácil que nunca, ya viva tu biblioteca en una nube centrada en la privacidad, en un NAS autoalojado o en un servidor genérico FTP/SFTP/NFS.

[Descarga Evertag 4.2 desde el App Store](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) o actualiza desde tu versión actual.

## Soporte ampliado de nube y servidores

Evertag se conecta ahora de forma nativa a un abanico más amplio de opciones de nube y almacenamiento autoalojado. Puedes editar etiquetas ID3, MP4, FLAC, OGG y APE en archivos que vivan en cualquier lugar.

### Almacenamiento en la nube centrado en la privacidad: Internxt y Proton Drive

Si te importan el cifrado de extremo a extremo y el almacenamiento de conocimiento cero, dos de las nubes más respetadas con foco en privacidad ya son nativas en Evertag:

- **Internxt** — nube española de código abierto, con cifrado post-cuántico y conforme al RGPD. Plan gratuito disponible.
- **Proton Drive** — almacenamiento con cifrado de extremo a extremo de los creadores de Proton Mail y Proton VPN, con sede en Suiza. Plan gratuito disponible y planes de pago para bibliotecas más grandes.

Ahora puedes editar metadatos directamente sobre archivos de audio guardados en cualquiera de los dos servicios — el archivo permanece cifrado en tránsito y solo las nuevas etiquetas se vuelven a escribir.

### Soluciones autoalojadas: QNAP, Nextcloud, Amazon S3

Para usuarios que gestionan su propia infraestructura:

- **QNAP** — conexión nativa por API a dispositivos NAS QNAP. Edita etiquetas en archivos de tu QNAP por Wi-Fi local o acceso remoto.
- **Nextcloud** — conecta con cualquier instancia Nextcloud autoalojada o gestionada.
- **Amazon S3** — apunta Evermusic… apunta Evertag a cualquier bucket S3 (o almacenamiento compatible con S3 como Backblaze B2, Wasabi, MinIO, Cloudflare R2) y edita metadatos en su sitio.

### Nuevos protocolos de red: FTP, SFTP, NFS

Evertag 4.2 añade tres protocolos clásicos para usuarios con servidores propios, homelabs o NAS genéricos:

- **SFTP (SSH File Transfer Protocol)** — la opción correcta para **editar etiquetas de forma remota y segura desde tu propio servidor**. SFTP funciona sobre SSH, así que toda la transferencia (autenticación y datos de audio) está cifrada. Si tienes un VPS, un servidor dedicado o una máquina Linux en casa con acceso SSH, puedes editar etiquetas en archivos remotos sin exponer nada más. Admite autenticación con contraseña y con clave.
- **FTP** — el estándar histórico de transferencia de archivos. Útil para NAS domésticos antiguos que exponen FTP pero no tienen API nativa.
- **NFS (Network File System)** — el protocolo de uso compartido de facto en Linux y la mayoría de los NAS. Menor sobrecarga que SMB con el mismo hardware.

> **Consejo:** SFTP es el protocolo que querrás para editar a distancia por internet abierto. FTP y NFS son mejores en tu red local — manténlos fuera de internet salvo que los envuelvas en una VPN.

## Mejoras de Wi-Fi Drive

[**Wi-Fi Drive**](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive/) es la función integrada de Evertag para transferir archivos de audio de forma inalámbrica entre el ordenador y el iPhone o iPad — sin iTunes, sin cables y sin cuenta en la nube. Ambos dispositivos deben estar en la misma red Wi-Fi.

En Evertag 4.2, Wi-Fi Drive estrena:

- **Interfaz renovada y moderna** — más limpia, más fácil de leer de un vistazo y actualizada para Liquid Glass.
- **Modo de selección múltiple** — elige varios archivos o carpetas y actúa sobre ellos en bloque.
- **Cola de subida más inteligente** — mejor información de progreso y mayor resistencia a interrupciones de red.
- **Velocidad y fiabilidad mejoradas** — transferencias más rápidas para bibliotecas grandes.

Es la forma más rápida de mover un lote de archivos de audio del ordenador al teléfono, editar sus etiquetas y devolverlos — sin servicios de terceros.

## Ajustes del editor de etiquetas: análisis a fondo

Esta es la parte que la mayoría de usuarios no leen — y la que decide si tus etiquetas funcionan en todas partes o solo en algunas apps. Abre Evertag y entra en la sección de **ajustes del editor de etiquetas de audio**. Aquí tienes lo que hace cada opción y cuál elegir según lo que quieras lograr.

### Escalado de la carátula

Cuando guardas la carátula del álbum dentro de un archivo de audio, Evertag puede escalar la imagen antes de incrustarla. Las opciones son:

- **Pequeño** — menor impacto en el tamaño del archivo, calidad de imagen más baja.
- **Mediano** — opción equilibrada para la mayoría de usuarios.
- **Grande** — alta calidad, ideal para reproductores con pantallas grandes y CarPlay.
- **Extra grande** — calidad muy alta, aumento notable del tamaño del archivo.
- **Original (Desactivado)** — incrusta la carátula a su resolución original. **Sin escalado.**

**Por qué importa:**

- **Más calidad = archivo más grande.** Una carátula de 3.000 × 3.000 píxeles puede añadir varios MB a cada pista. Multiplicado por todo un álbum, el coste en disco se acumula rápido.
- **Algunos reproductores no manejan bien imágenes incrustadas muy grandes.** Dispositivos antiguos, ciertos sistemas de coche y algunos reproductores de escritorio heredados pueden atascarse con carátulas mayores de ~1.500 px o no mostrarlas.
- **Para la mayoría de flujos en la nube y de streaming**, **Mediano** o **Grande** es el punto óptimo. Usa **Original** solo cuando necesites calidad de archivo o prepares archivos para un reproductor en el que confíes.

> La opción **Original** forma parte de la mejora de personalización premium de Evertag. Los tamaños estándar (Pequeño/Mediano/Grande/Extra grande) son gratuitos.

### Opciones de guardado de etiquetas: ID3v2.4 frente a ID3v2.3

Es el ajuste más importante para la compatibilidad. ID3v2 es el formato de metadatos dentro de los archivos MP3. Hay dos versiones muy usadas y se diferencian en detalles sutiles pero importantes.

#### ID3v2.4

- Más reciente, admite **codificación de texto UTF-8** — manejo correcto de escrituras no latinas (chino, ruso, japonés, árabe, hebreo, etc.).
- Más tipos de marco (volumen relativo, presets de ecualizador, etc.).
- **Recomendado para reproductores modernos** que lo soportan.

#### ID3v2.3

- Más antiguo pero **el ID3 con mayor compatibilidad universal**.
- No admite UTF-8 directamente (usa UTF-16 para texto Unicode).
- **Recomendado cuando necesitas máxima compatibilidad** con reproductores antiguos, equipos de coche y ciertas apps de escritorio.

#### Cuándo activar ID3v2.4 en Evertag

- Usas **reproductores de audio modernos** como Evermusic, Plex, Jellyfin, Navidrome, foobar2000, VLC, Apple Music (versiones actuales) o reproductores Android modernos. ✅ **Activa ID3v2.4.**
- Tu biblioteca contiene **caracteres no latinos** (chino, coreano, japonés, ruso, árabe, griego, hebreo). ✅ **Activa ID3v2.4** — UTF-8 los maneja con mucha más limpieza.

#### Cuándo desactivar ID3v2.4 en Evertag (usar ID3v2.3)

- Preparas archivos para un **equipo de coche o cabezal antiguo** que no lee etiquetas v2.4.
- Ves **texto ilegible o etiquetas vacías** en algunas apps tras editar — eso es una señal clara de que ahí no se soporta v2.4. Vuelve a v2.3.
- Apuntas a **reproductores de escritorio heredados** o reproductores portátiles antiguos (primeros iPods, ciertos reproductores MP3 de los 2000–2010).

> **Regla práctica:** si tus etiquetas se ven correctamente en todas partes con v2.4, déjalo activado. Si incluso un solo reproductor importante muestra caracteres erróneos, espacios en blanco o no lee las etiquetas, desactiva v2.4 y vuelve a guardar.

#### Etiquetas duplicadas

Cuando activas **Etiquetas duplicadas**, Evertag escribe los campos de metadatos comunes (título, artista, álbum, etc.) en **las secciones ID3v1 e ID3v2** del archivo. Esto mejora la compatibilidad con reproductores muy antiguos que solo leen ID3v1 (la etiqueta original de 128 bytes al final del archivo).

- **La mayoría de usuarios no lo necesitan.** Los reproductores modernos leen ID3v2 primero.
- **Actívalo solo si** tratas con hardware vintage o software específico que ignora ID3v2.

### Actualizar archivos en línea: cómo gestiona Evertag las ediciones en la nube

Cuando editas etiquetas en un archivo guardado en una nube conectada (Google Drive, Dropbox, OneDrive, iCloud, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, SFTP, etc.), Evertag tiene que volver a subir el archivo modificado. Tú controlas cómo:

- **Mostrar mensaje de confirmación** *(predeterminado, recomendado)* — Evertag pregunta antes de subir. Mejor para usuarios cautos y bibliotecas compartidas.
- **Actualizar automáticamente los metadatos del archivo** — sube en silencio tras cada edición. Mejor para usuarios solos con conexiones rápidas y fiables que editan mucho.
- **No actualizar los metadatos del archivo** — Evertag edita solo la copia local. Útil para previsualizar cambios sin enviarlos a la nube.

### Editar archivos en línea: limpieza del archivo local

Para editar un archivo remoto, Evertag lo descarga primero al dispositivo. Después de editar, eliges qué pasa con esa copia local:

- **Eliminar siempre el archivo descargado** — Evertag borra el archivo temporal tras editar. **Recomendado** si vas justo de almacenamiento o trabajas con archivos ajenos.
- **No eliminar el archivo descargado** — conserva el archivo editado en tu dispositivo. Útil si quieres una copia offline y otra en la nube.

### Botones de la pantalla principal

La pantalla principal del editor de etiquetas de Evertag puede mostrar u ocultar botones para operaciones individuales. Activa solo los que realmente uses para mantener la interfaz enfocada:

- **Buscar etiquetas automáticamente** — encuentra metadatos faltantes en línea a partir de la huella de audio del archivo.
- **Buscar etiquetas manualmente** — busca por título/artista cuando la búsqueda automática falla.
- **Buscar carátula** — encuentra e incrusta carátulas de alta calidad.
- **Guardar carátula** — exporta la carátula incrustada a tu fototeca o archivos.
- **Normalizar codificación** — corrige texto no latino mal codificado por encodings antiguos (muy útil para pistas en cirílico, chino y japonés ripeadas con software heredado).
- **Eliminar etiquetas de audio** — borra todas las etiquetas del archivo. Útil antes de etiquetar de cero.

### Mostrar etiquetas extendidas

Activa esto para mostrar todo el conjunto de campos de metadatos más allá del básico título/artista/álbum/año — incluyendo BPM, director, artista original, estado de ánimo, copyright, codificador, comentarios, letras y más. Función para usuarios avanzados; la mayoría de los casuales no la necesita.

### Editar archivos simultáneamente

Activado, Evertag te permite editar metadatos en **varios archivos seleccionados a la vez** — establece el mismo artista del álbum, año o género para todo un álbum en una sola operación. Es la forma más rápida de poner orden en una biblioteca grande y desordenada.

## Editar etiquetas para Spotify, Apple Music y plataformas de streaming

Una pregunta habitual: «edité mis etiquetas en Evertag, subí los archivos y el servicio de streaming muestra metadatos erróneos. ¿Qué pasa?».

Respuesta corta: **los servicios de streaming no siempre respetan tus etiquetas locales**. Apple Music y Spotify tienen sus propias bases de datos internas — cuando reconocen una pista, sobrescriben los metadatos mostrados con los suyos. Pero para los **archivos subidos**, tus archivos locales (la función «Biblioteca» de Apple Music, los Archivos locales de Spotify) y las **subidas de distribuidor a plataformas de streaming**, tus etiquetas sí importan. Aquí tienes cómo configurar Evertag en cada caso:

### Preparar archivos para Apple Music (Cloud Music Library / iTunes Match)

- **ID3v2.4: ON** — Apple Music maneja UTF-8 correctamente.
- **Carátula: Grande** — las apps de Apple muestran bien las carátulas grandes; Original es excesivo.
- **Etiquetas duplicadas: OFF** — no son necesarias.
- Asegúrate de rellenar correctamente **Artista del álbum** — Apple Music lo usa para agrupar.

### Preparar archivos para los Archivos locales de Spotify

Los Archivos locales de Spotify solo muestran archivos bien etiquetados. Las etiquetas que lee Spotify son limitadas.

- **ID3v2.4: ON** en la mayoría de los casos. Si una pista no aparece correctamente en Spotify tras editar, **prueba a guardar con ID3v2.4 OFF** (es decir, como ID3v2.3) — el parser de Spotify ha sido históricamente conservador con v2.4.
- **Carátula: Mediana o Grande** — Spotify la reescala de todos modos.
- Rellena al menos **Título**, **Artista**, **Álbum** y **Número de pista**.

### Preparar archivos para subida por distribuidor (DistroKid, TuneCore, CD Baby, etc.)

Si eres artista y subes tu propio trabajo a las plataformas de streaming, tu distribuidor suele leer las etiquetas pero también pide los metadatos en su interfaz. En cualquier caso:

- **ID3v2.3** suele ser la opción más segura — muchas tuberías de distribuidor se construyeron hace años y prefieren el formato antiguo.
- Incrusta carátula **Grande** (la mayoría de distribuidores exigen ≥ 1.400 × 1.400 px — consulta sus pautas).
- No te apoyes en etiquetas extendidas — los distribuidores solo leen los campos principales.

### Preparar archivos para Plex, Jellyfin, Navidrome, Subsonic, Emby

Estos servidores multimedia autoalojados son muy tolerantes. Leen tanto v2.3 como v2.4 sin problemas y manejan UTF-8 bien.

- **ID3v2.4: ON** está bien.
- **Carátula: Grande** o **Extra grande** — estos servidores envían la carátula a clientes móviles y pantallas CarPlay, así que la calidad importa.
- **Artista del álbum** muy recomendado — es lo que Plex/Jellyfin usan para agrupar álbumes por artista correctamente.

### Preparar archivos para equipos de coche y hardware antiguo

- **ID3v2.4: OFF** (usa ID3v2.3) — los cabezales antiguos a menudo no soportan v2.4.
- **Carátula: Mediana** — muchos visualizadores de coche se atascan con carátulas grandes incrustadas.
- **Etiquetas duplicadas: ON** — algunos equipos de coche antiguos solo leen el respaldo ID3v1.

## Otras mejoras

### Diseño Liquid Glass

La interfaz de Evertag 4.2 se afina al nuevo material **Liquid Glass** de Apple en toda la app — superficies translúcidas, animaciones más suaves y controles refinados que encajan de forma natural en iOS, iPadOS y macOS.

### Bibliotecas de conexión actualizadas

Hemos refrescado las bibliotecas internas que Evertag usa para hablar con **WebDAV**, **SMB**, **DLNA**, **Dropbox**, **Google Drive**, **OneDrive** y otros servicios. Resultado: menos fallos de conexión en casos límite, mejor compatibilidad con versiones de servidor recientes y mayor fiabilidad al editar etiquetas en archivos remotos.

### Correcciones de traducción y localización

Múltiples arreglos de idioma en la interfaz a partir del feedback directo de los usuarios. Mejor encaje del texto en botones pequeños en varios idiomas.

### Pequeñas mejoras inspiradas en tus comentarios

Muchas mejoras menores basadas en reseñas del App Store y correos a support@everappz.com. Leemos cada mensaje.

## Consigue Evertag 4.2

[**Descarga Evertag en el App Store**](https://apps.apple.com/app/evertag-audio-files-tag-editor/id1498082611) o actualiza desde el App Store. Evertag es una descarga gratuita con mejoras opcionales dentro de la app para funciones avanzadas. Las nuevas conexiones de nube, los protocolos de red, las mejoras de Wi-Fi Drive y la interfaz Liquid Glass forman parte de la actualización base.

Si te gusta la app, deja una valoración en el App Store — ayuda mucho. ¿Tienes comentarios o un problema? Escríbenos a **support@everappz.com**. Leemos cada mensaje.

## Preguntas frecuentes

{{% details title="¿Qué hay de nuevo en Evertag 4.2?" closed="true" %}}
Evertag 4.2 añade más de 6 nuevas conexiones a la nube y servidores (Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, FTP, SFTP, NFS), un Wi-Fi Drive renovado con selección múltiple y una cola de subida más inteligente, actualizaciones de la interfaz Liquid Glass, bibliotecas de conexión actualizadas, correcciones clave en la edición de etiquetas y mejoras en la traducción.
{{% /details %}}

{{% details title="¿Debo usar ID3v2.4 o ID3v2.3 en Evertag?" closed="true" %}}
Usa **ID3v2.4** para reproductores modernos (Evermusic, Plex, Jellyfin, Apple Music, foobar2000, VLC, apps Android modernas) y para bibliotecas con caracteres no latinos — el soporte UTF-8 implica etiquetas más limpias en chino, coreano, japonés, ruso, árabe y hebreo. Usa **ID3v2.3** si tus etiquetas se ven incorrectamente en algunas apps, si apuntas a equipos de coche antiguos o si una tubería de distribuidor de streaming rechaza v2.4. Siempre puedes cambiar y volver a guardar.
{{% /details %}}

{{% details title="¿Por qué mis etiquetas se ven mal en Spotify después de editar?" closed="true" %}}
Spotify muestra principalmente metadatos de su propio catálogo — tus etiquetas locales solo se usan para «Archivos locales» o para contenido que has subido como artista. Si etiquetas archivos para Archivos locales de Spotify y no aparecen correctamente, prueba a desactivar ID3v2.4 en Evertag y guardar como ID3v2.3 — el parser de Spotify ha sido históricamente conservador con v2.4.
{{% /details %}}

{{% details title="¿Qué tamaño de carátula debo elegir en Evertag?" closed="true" %}}
Para la mayoría de usuarios: **Grande**. Se ve perfecto en teléfonos, iPads, Macs y pantallas de coche modernas sin inflar demasiado los archivos. Usa **Mediana** si tienes una biblioteca enorme y quieres ahorrar disco. Usa **Original** (sin escalado) solo para másteres de archivo o cuando necesites máxima calidad — pero ten en cuenta que algunos reproductores antiguos tienen problemas con carátulas incrustadas muy grandes. **Original** forma parte de la mejora de personalización premium de Evertag.
{{% /details %}}

{{% details title="¿Las carátulas más grandes harán mis archivos más pesados?" closed="true" %}}
Sí. Incrustar una carátula de 3.000 × 3.000 px puede añadir varios megabytes a un solo archivo de audio. En una biblioteca de 1.000 pistas, eso suma gigabytes. Si vas justo de almacenamiento, usa Mediana o Grande; si reproduces desde un NAS donde el tamaño no importa, Extra grande u Original están bien.
{{% /details %}}

{{% details title="¿Qué son las etiquetas duplicadas y debo activarlas?" closed="true" %}}
Las etiquetas duplicadas escriben los metadatos básicos en las secciones ID3v1 (legado de 128 bytes) e ID3v2 (moderna) del archivo. Actívalas solo si apuntas a reproductores muy antiguos o hardware que lea ID3v1. Para todo lo moderno (smartphones, ordenadores, equipos de coche recientes), déjalas desactivadas.
{{% /details %}}

{{% details title="¿Evertag edita las etiquetas directamente en archivos en la nube?" closed="true" %}}
Sí. Conéctate a tu nube (Google Drive, Dropbox, OneDrive, iCloud Drive, Internxt, Proton Drive, QNAP, Nextcloud, Amazon S3, etc.) o vía FTP/SFTP/NFS, abre un archivo y edita las etiquetas como si fuera local. Evertag descarga el archivo, aplica tus cambios y vuelve a subir la versión actualizada. Puedes elegir entre los modos «Preguntar siempre», «Subir automáticamente» o «No subir» en los ajustes.
{{% /details %}}

{{% details title="¿Puedo editar etiquetas FLAC en iPhone con Evertag?" closed="true" %}}
Sí. Evertag admite FLAC, MP3, M4A/MP4, AIFF, WAV, OGG, APE y otros formatos importantes con soporte completo de lectura/escritura de etiquetas, incluida la carátula incrustada.
{{% /details %}}

{{% details title="¿Cómo edito etiquetas de forma segura en mi servidor doméstico con SFTP?" closed="true" %}}
Abre Evertag, ve a Conexiones, elige SFTP e introduce el nombre de host o IP del servidor, el puerto (normalmente 22), el usuario y, o bien una contraseña, o una clave SSH privada. Evertag listará tus carpetas remotas y editará las etiquetas directamente con cifrado de extremo a extremo sobre SSH.
{{% /details %}}

{{% details title="¿Puedo editar etiquetas en varios archivos a la vez?" closed="true" %}}
Sí. Activa **Editar archivos simultáneamente** en los ajustes. Selecciona varios archivos, abre el editor de etiquetas y cualquier campo que cambies se aplicará a todos los archivos seleccionados. Es la forma más rápida de fijar el mismo artista del álbum, año o género en todo un álbum.
{{% /details %}}

{{% details title="¿La actualización a Evertag 4.2 es gratuita?" closed="true" %}}
Sí. Evertag es una descarga gratuita en el App Store y la 4.2 es una actualización gratis para todos los usuarios actuales. Las nuevas integraciones en la nube, las mejoras de Wi-Fi Drive y la interfaz Liquid Glass forman parte de la actualización base.
{{% /details %}}

{{% details title="¿En qué dispositivos está disponible Evertag 4.2?" closed="true" %}}
Evertag 4.2 funciona en iPhone, iPad y Mac. La sincronización con iCloud Drive mantiene tus ajustes de edición de etiquetas consistentes entre dispositivos.
{{% /details %}}
