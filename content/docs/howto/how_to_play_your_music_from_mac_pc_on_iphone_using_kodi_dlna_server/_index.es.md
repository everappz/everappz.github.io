---
title: "Cómo reproducir tu música desde Mac / PC / Linux / NAS en iPhone usando el servidor Kodi DLNA"
date: 2025-07-25
description: "Transmite música desde tu ordenador o NAS a tu iPhone por Wi-Fi usando Kodi DLNA y la app Evermusic."
keywords: ["servidor kodi dlna", "transmitir música a iphone", "reproducir música desde nas", "evermusic dlna", "música de mac a iphone", "música de windows a iphone", "kodi dlna iphone", "transmisión de audio dlna"]
tags: ["dlna", "kodi", "evermusic", "iphone", "transmisión de música", "mac", "nas", "linux", "red local"]
readingTime: 5
---

{{< author-byline >}}


**Resumen:** Instala Kodi en tu Mac, PC, Linux o NAS, activa su servidor DLNA/UPnP y transmite toda tu biblioteca musical a iPhone o iPad usando la app gratuita Evermusic o Flacbox por Wi-Fi. Sin suscripciones necesarias.

## Introducción

Si tienes un **Mac, PC con Windows, máquina Linux o dispositivo NAS**, puedes transformarlo fácilmente en un **servidor de música personal** en casa usando [Kodi](https://kodi.tv/), una plataforma multimedia gratuita y de código abierto. Con el servidor **DLNA/UPnP** integrado de Kodi, puedes transmitir toda tu biblioteca musical a cualquier cliente compatible con DLNA — incluyendo tu iPhone o iPad.

En esta guía, te mostraremos paso a paso cómo:

- Instalar Kodi en tu Mac o PC  
- Configurar tus carpetas de música para compartir  
- Activar el servidor de música DLNA  
- Acceder a esa música usando la app **Evermusic** o **Flacbox** para iOS

Esta configuración es 100% gratuita — sin suscripciones, solo tu propia música transmitida por tu red Wi-Fi. Ya sea que intentes organizar tu gran colección de MP3, escuchar FLAC por Wi-Fi, o simplemente disfrutar de tu música local sin sincronizar vía iTunes, esta configuración es perfecta para ti.

## Descargar e instalar Kodi en tu Mac / PC / Linux / NAS

Primero, visita el sitio web oficial de Kodi:

🔗 https://kodi.tv/

{{< cards cols="1">}}
{{< card subtitle="Página principal de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/1_kodi_main_page.webp" >}}
{{< /cards >}}

Haz clic en **Descargas** y desplázate para encontrar la versión para tu ordenador.
Elige tu sistema operativo. En este ejemplo, usaremos **macOS**.

{{< cards cols="1">}}
{{< card subtitle="Página de descargas de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/2_kodi_downloads_page.webp" >}}
{{< /cards >}}

Haz clic en **Intel (x86/64)** si tienes un Mac con Intel o **Apple Silicon** para M1, M2, M3 Mac para iniciar la descarga.

{{< cards cols="1">}}
{{< card subtitle="Elige el instalador de macOS" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/3_kodi_macos_downloads.webp" >}}
{{< /cards >}}

Espera un momento mientras se descarga el instalador.

{{< cards cols="1">}}
{{< card subtitle="Kodi descargado" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/4_kodi_downloaded.webp" >}}
{{< /cards >}}

Una vez descargado, localiza el archivo `.dmg` en tu carpeta de **Descargas**.

{{< cards cols="1">}}
{{< card subtitle="Instalar Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/5_kodi_installer_in_downloads_folder.webp" >}}
{{< /cards >}}

Haz doble clic en el archivo descargado para ejecutar el instalador.
Arrastra Kodi a tu carpeta de **Aplicaciones** para instalar.

{{< cards cols="1">}}
{{< card title="" subtitle="Instala Kodi arrastrándolo a Aplicaciones" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/6_install_kodi_mac.webp" >}}
{{< /cards >}}

Abre Kodi. Es posible que necesites permitirlo en **Preferencias del Sistema → Seguridad y Privacidad → Abrir de todas formas**.

{{< cards cols="1">}}
{{< card subtitle="Pantalla principal de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/7_kodi_main_screen.webp" >}}
{{< /cards >}}

## Añadir música a la biblioteca de Kodi

Haz clic en el **icono de engranaje** (Ajustes) desde la pantalla de inicio.

{{< cards cols="1">}}
{{< card subtitle="Ajustes de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/8_kodi_settings.webp" >}}
{{< /cards >}}

Navega a **Ajustes de medios → Biblioteca**. Activa **Actualizar biblioteca al inicio** para la biblioteca de vídeo y música para indexación automática.

{{< cards cols="1">}}
{{< card subtitle="Ajustes de biblioteca" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/9_kodi_library_settings.webp" >}}
{{< /cards >}}

Luego ve a la sección **Música** y haz clic en **Añadir música**.

{{< cards cols="1">}}
{{< card subtitle="Añadir carpeta de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/12_kodi_add_music_folder.webp" >}}
{{< /cards >}}

Navega y selecciona la carpeta donde está almacenada tu música.

{{< cards cols="1">}}
{{< card subtitle="Elegir fuente de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/13_kodi_add_music_source.webp" >}}
{{< /cards >}}

Añade la fuente de música a Kodi.

{{< cards cols="1">}}
{{< card subtitle="Añadir fuente de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/14_kodi_music_source_added.webp" >}}
{{< /cards >}}

Confirma y deja que Kodi escanee tu biblioteca musical.

{{< cards cols="1">}}
{{< card subtitle="Confirmar fuentes de música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/15_kodi_add_media_to_library_confirmation.webp" >}}
{{< /cards >}}

Espera un momento mientras tu biblioteca se escanea y construye completamente.

{{< cards cols="1">}}
{{< card subtitle="Escaneando biblioteca musical" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/16_kodi_scanning_library.webp" >}}
{{< /cards >}}

## Activar el servidor DLNA de Kodi

Ve a **Ajustes → Servicios → UPnP/DLNA**.

Activa la opción: **Compartir mis bibliotecas**.

Kodi ahora funciona como servidor DLNA en tu red Wi-Fi local.

{{< cards cols="1">}}
{{< card subtitle="Activar DLNA en Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/21_kodi_enable_dlna_server.webp" >}}
{{< /cards >}}

## Abrir biblioteca de Kodi

Haz clic derecho para cerrar la ventana de ajustes y abrir la biblioteca principal de Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Clic derecho para acceder a la biblioteca de Kodi" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/17_right_mouse_click_move_to_settings_and_main_library_showing_music.webp" >}}
{{< /cards >}}

## Descargar app de transmisión de música para iOS

Obtén una app cliente DLNA gratuita para iOS que te permite transmitir música desde una amplia gama de servicios de almacenamiento en la nube y servidores DLNA.

- Usa **Evermusic** si tu colección es principalmente MP3 y otros formatos de audio estándar.
- Elige **Flacbox** si tienes una biblioteca de música de alta resolución en formatos como FLAC, ALAC o DSD.

Ambas apps están disponibles para **iOS** y **macOS**, y son gratuitas.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descargar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descargar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

## Añadir fuente DLNA

Una vez descargada la app iOS, abre la sección **Todas las Conexiones**.

{{< cards cols="1">}}
{{< card title="" subtitle="Barra lateral principal de la app Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/18_evermusic_app_main_sidebar.webp" >}}
{{< /cards >}}

Desplázate hacia abajo y toca **Red local - Dispositivos disponibles** para descubrir servidores DLNA.
En esta sección, verás todos los dispositivos disponibles en tu red local. Tu **servidor Kodi DLNA** debería aparecer aquí. Toca el servidor Kodi para conectarte.

{{< cards cols="1">}}
{{< card title="" subtitle="Dispositivos DLNA disponibles en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/19_evermusic_app_available_devices.webp" >}}
{{< /cards >}}

Evermusic mostrará las carpetas de la biblioteca compartidas a través de Kodi.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical de Kodi en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/22_evermusic_app_kodi_dlna_music_library.webp" >}}
{{< /cards >}}

Navega a la carpeta **Canciones** para ver todos los archivos de audio disponibles en tu servidor DLNA.

{{< cards cols="1">}}
{{< card title="" subtitle="Canciones listadas desde carpeta remota" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/23_evermusic_app_songs_on_remote_folder.webp" >}}
{{< /cards >}}

Toca cualquier archivo de audio para comenzar a transmitir instantáneamente.

{{< cards cols="1">}}
{{< card title="" subtitle="Archivo MP3 reproduciéndose en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/24_evermusic_app_playing_mp3.webp" >}}
{{< /cards >}}

Regresa a la sección **Conexiones**. El servidor DLNA añadido aparecerá aquí ahora. Toca su icono para reconectarte en cualquier momento. También puedes conectar otros servicios en la nube desde esta pantalla usando los mismos pasos.

También puedes activar el **scrobbling de Last.fm** aquí. Las estadísticas de reproducción se guardarán en tu cuenta de Last.fm, proporcionando recomendaciones musicales personalizadas más adelante.

{{< cards cols="1">}}
{{< card title="" subtitle="Conexiones en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/25_evermusic_app_connections_with_dlna.webp" >}}
{{< /cards >}}

## Construir biblioteca musical

Tanto **Evermusic** como **Flacbox** te permiten añadir música a tu biblioteca y organizarla por **etiquetas de metadatos** como artistas, álbumes, géneros y compositores.

Para empezar, abre la sección **Biblioteca musical**. Desplázate hacia abajo hasta **Herramientas y preferencias** y toca **Añadir música**.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical de Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/26_evermusic_library_music.webp" >}}
{{< /cards >}}

Selecciona la fuente de música — en este caso, elige **Conexiones**.

{{< cards cols="1">}}
{{< card title="" subtitle="Añadir música nueva en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/27_evermusic_add_music.webp" >}}
{{< /cards >}}

Encuentra el **servidor Kodi DLNA** en las Conexiones y toca para ver carpetas y archivos.

{{< cards cols="1">}}
{{< card title="" subtitle="Elegir servidor DLNA para importar música" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/28_evermusic_select_dlna_server.webp" >}}
{{< /cards >}}

Elige las carpetas o archivos que deseas añadir y toca **Hecho**.

{{< cards cols="1">}}
{{< card title="" subtitle="Seleccionar carpeta de música para añadir" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/29_evermusic_select_music_folder.webp" >}}
{{< /cards >}}

La app escaneará los archivos seleccionados y los organizará usando metadatos en secciones como Artistas, Álbumes, Géneros y Compositores.

{{< cards cols="1">}}
{{< card title="" subtitle="Biblioteca musical con categorías" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/30_evermusic_library_with_categories.webp" >}}
{{< /cards >}}

## Crear listas de reproducción

También puedes crear tus propias listas de reproducción.

Primero, abre la pestaña **Listas de reproducción**.

{{< cards cols="1">}}
{{< card title="" subtitle="Pestaña de listas de reproducción en Evermusic" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/31_evermusic_playlists_tab.webp" >}}
{{< /cards >}}

Toca el botón **más (+)** y elige **Nueva lista de reproducción**.

{{< cards cols="1">}}
{{< card title="" subtitle="Crear una nueva lista de reproducción" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/32_evermusic_create_playlist.webp" >}}
{{< /cards >}}

Introduce un nombre para tu lista de reproducción y toca **Guardar**.

{{< cards cols="1">}}
{{< card title="" subtitle="Introducir nombre de lista de reproducción" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/33_evermusic_enter_playlist_name.webp" >}}
{{< /cards >}}

A continuación, elige una fuente para añadir canciones — aquí, seleccionamos la **Biblioteca**.

{{< cards cols="1">}}
{{< card title="" subtitle="Añadir canciones a la nueva lista de reproducción" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/34_evermusic_add_songs_to_playlist.webp" >}}
{{< /cards >}}

Selecciona las canciones que deseas y toca **Hecho** para añadirlas.

{{< cards cols="1">}}
{{< card title="" subtitle="Añadir música de la biblioteca a la lista de reproducción" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/35_evermusic_add_songs_from_library_to_playlist.webp" >}}
{{< /cards >}}

Las pistas seleccionadas aparecerán ahora en la lista de reproducción creada.

{{< cards cols="1">}}
{{< card title="" subtitle="Lista de reproducción creada mostrada en la lista" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/36_evermusic_created_playlist.webp" >}}
{{< /cards >}}

Por defecto, las canciones están disponibles para transmisión. Para escuchar sin conexión, activa el **Modo sin conexión** — la app descargará todas las pistas de la lista de reproducción.

{{< cards cols="1">}}
{{< card title="" subtitle="Modo sin conexión activado para la lista de reproducción" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/37_evermusic_offline_mode_enabled_playlist.webp" >}}
{{< /cards >}}

Toca el botón **Más acciones** para explorar opciones adicionales. Puedes:

- Archivar la lista de reproducción  
- Cambiar la portada del álbum  
- Reordenar pistas  
- Y más funciones útiles

{{< cards cols="1">}}
{{< card title="" subtitle="Más acciones de lista de reproducción disponibles" image="/docs/howto/how_to_play_your_music_from_mac_pc_on_iphone_using_kodi_dlna_server/38_evermusic_more_actions_for_playlist.webp" >}}
{{< /cards >}}


## Conclusión

Con **Evermusic** y **Flacbox**, convertir tu iPhone, iPad o Mac en un potente reproductor de música DLNA es fácil. Ya sea que almacenes tu música en la nube, en un NAS o en un servidor multimedia doméstico como **Kodi**, estas apps te permiten transmitir, organizar y disfrutar de tu colección sin límites.

- Transmite MP3 o FLAC de alta resolución directamente desde tu **servidor Kodi DLNA**  
- Crea una biblioteca musical personal agrupada por metadatos (álbumes, géneros, compositores)  
- Crea y gestiona **listas de reproducción personalizadas**  
- Activa el **modo sin conexión** para escuchar en movimiento  
- Conéctate a **múltiples servicios en la nube** y **dispositivos de red local**  
- Registra tus hábitos de escucha con la **integración de Last.fm**

Ya seas un audiófilo o un oyente casual, Evermusic y Flacbox ofrecen todo lo que necesitas para una transmisión y organización musical sin interrupciones.

{{< cards cols="1">}}
{{< card link="https://apps.apple.com/app/apple-store/id885367198?pt=95781850&ct=everappzcom&mt=8" title="Descargar Evermusic" icon="download" tag="Free" >}}
{{< card link="https://apps.apple.com/app/apple-store/id1097564256?pt=95781850&ct=everappzcom&mt=8" title="Descargar Flacbox" icon="download" tag="Free" >}}
{{< /cards >}}

Empieza a construir tu experiencia musical personal hoy.

## Preguntas frecuentes

{{% details title="¿Es Kodi gratuito como servidor DLNA?" closed="true" %}}
Sí. Kodi es completamente gratuito y de código abierto. Funciona en macOS, Windows, Linux y muchos dispositivos NAS.
{{% /details %}}

{{% details title="¿Soportan Evermusic y Flacbox la transmisión de FLAC por DLNA?" closed="true" %}}
Sí. Flacbox está optimizado para formatos de alta resolución como FLAC, ALAC y DSD. Evermusic también soporta la reproducción de FLAC junto con MP3 y otros formatos estándar.
{{% /details %}}

{{% details title="¿Puedo escuchar sin conexión después de transmitir desde Kodi?" closed="true" %}}
Sí. Activa el Modo sin conexión en cualquier lista de reproducción, y la app descargará todas las pistas a tu dispositivo para escuchar sin conexión de red.
{{% /details %}}

{{% details title="¿Necesito una suscripción premium para usar DLNA?" closed="true" %}}
La versión gratuita soporta hasta 3 conexiones de nube o red. Premium elimina este límite y te permite conectar servicios y servidores DLNA ilimitados.
{{% /details %}}

{{% details title="¿Mi iPhone necesita estar en la misma red Wi-Fi que Kodi?" closed="true" %}}
Sí. La transmisión DLNA funciona a través de tu red local. Tanto el servidor Kodi como tu dispositivo iOS deben estar conectados a la misma red Wi-Fi.
{{% /details %}}

{{% details title="¿Puedo usar esta configuración con un NAS en lugar de un Mac o PC?" closed="true" %}}
Sí. Muchos dispositivos NAS (Synology, QNAP, etc.) soportan Kodi o tienen su propio servidor DLNA integrado. Evermusic y Flacbox pueden conectarse a cualquier servidor DLNA/UPnP estándar.
{{% /details %}}
