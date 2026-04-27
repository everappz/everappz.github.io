---
title: "Cómo activar el servidor multimedia DLNA en Windows 10 y reproducir tu música en iPhone"
date: 2019-11-26
description: "Activa el servidor DLNA en Windows 10 y transmite tu música al iPhone con la app Evermusic. Guía de configuración paso a paso incluida."
keywords: ["evermusic", "dlna", "windows 10", "streaming de música en iphone", "servidor multimedia", "red local", "upnp"]
tags: ["evermusic", "música", "nube", "iphone", "almacenamiento", "local", "nas", "windows", "wifi", "escuchar", "red", "remoto", "hogar", "en línea", "dlna"]
readingTime: 2
---

{{< author-byline >}}


**Resumen:** Windows 10 tiene un servidor DLNA integrado. Actívalo en la configuración de Red y uso compartido, luego usa la app gratuita **Evermusic** en tu iPhone para transmitir toda tu biblioteca musical por Wi-Fi. No se necesita software de servidor de terceros.

{{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e902db0c9a4c45af9772ce000ef5891e~mv2.jpg" alt="Evermusic + Windows 10 DLNA: Portada" caption="Streaming de música DLNA al iPhone usando Windows 10 y Evermusic" width="800" >}}

DLNA (Digital Living Network Alliance) es una herramienta potente que te permite transmitir fácilmente diversos contenidos multimedia, incluida la música, entre dispositivos compatibles con DLNA en tu red. La buena noticia es que Windows 10, y versiones anteriores, incluyen una función DLNA integrada, eliminando la necesidad de servidores multimedia de terceros. Aquí te explicamos cómo activar el servidor multimedia DLNA en Windows 10 y disfrutar del streaming de música en tu iPhone.

## Cómo activar el servidor multimedia DLNA en Windows 10

1. Haz clic en el botón 'Inicio'.  
2. Selecciona el icono 'Configuración'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_c3a96f130f03415a82559099461d4134~mv2.jpg" alt="Configurar servidor" caption="Abrir Configuración de Windows" width="500" >}}

3. En la pantalla 'Configuración de Windows', elige 'Red e Internet'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_1a9a141499644b399f3b71ffab5952b1~mv2.jpg" alt="Configuración de Windows" caption="Seleccionar Red e Internet" width="500" >}}

4. En 'Red', selecciona 'Centro de redes y recursos compartidos'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_65d1517f23c54a33a2c65dcdf391e518~mv2.jpg" alt="Centro de recursos compartidos" caption="Abrir Centro de redes y recursos compartidos" width="500" >}}

5. En la pantalla 'Centro de redes y recursos compartidos', haz clic en 'Cambiar configuración de uso compartido avanzado' en el menú izquierdo.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_4f1cdb9a11554cf098dede594121f395~mv2.jpg" alt="Configuración de uso compartido avanzado" caption="Cambiar configuración de uso compartido avanzado" width="500" >}}

6. En la pantalla 'Configuración de uso compartido avanzado', desplázate hasta la sección 'Todas las redes' y expándela haciendo clic en la flecha.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_e7f28734af9e43d2ae949abce24f772e~mv2.jpg" alt="Activar detección" caption="Expandir configuración de todas las redes" width="500" >}}

7. Haz clic en 'Activar streaming multimedia' para activar el servidor DLNA.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_cbbd6a55ea484b6f861500dda6a87c10~mv2.jpg" alt="Activar servidor" caption="Activar servidor de streaming multimedia" width="500" >}}

8. Dale un nombre a tu biblioteca multimedia y selecciona los dispositivos autorizados para acceder.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_a6ef0f439bec43f4a669dc5b9e4fe69d~mv2.jpg" alt="Nombre de biblioteca multimedia" caption="Nombra tu biblioteca multimedia DLNA" width="500" >}}

9. Haz clic en 'Aceptar' para confirmar la operación. Ahora, tus carpetas personales como Música, Imágenes y Vídeos serán visibles para cualquier dispositivo de streaming con soporte UPnP.

## Cómo desactivar el servidor multimedia DLNA en Windows 10

1. Haz clic en 'Inicio' y escribe 'services' en el campo de búsqueda.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51f9a32815df49d098d7aa0a87ea2670~mv2.jpg" alt="Servicios de Windows" caption="Abrir Servicios de Windows" width="500" >}}

2. En la pantalla 'Servicios', desplázate para encontrar 'Windows Media Player Network Sharing Service'.  
3. Haz doble clic y establece el 'Tipo de inicio' en 'Manual'.  
4. Detén el servicio haciendo clic en el botón 'Detener'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_5cd01e7879b6466390737e63415faa9c~mv2.jpg" alt="Detener servicio DLNA" caption="Desactivar servicio de uso compartido de red DLNA" width="500" >}}

## Cómo reproducir música desde el servidor DLNA en iPhone

1. Instala la app gratuita **Evermusic** desde el App Store:  
   [App Evermusic](https://apps.apple.com/us/app/evermusic-offline-music-player-cloud-streamer/id885367198?ls=1)

2. Abre la pestaña 'Conexiones' y toca en 'Dispositivos disponibles' en la sección 'Red local'.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_51ea5a3f90d745b188d1a0ca539116e9~mv2.jpg" alt="Conexiones Evermusic" caption="Evermusic: pantalla de Conexiones" width="500" >}}

3. Espera unos segundos mientras se carga la lista de dispositivos y toca en el servidor Windows Media Player DLNA (p. ej., 'MSEDGEWIN10: My Windows Library').

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_281a535137cb409a9721da4a07581546~mv2.jpg" alt="Dispositivos disponibles" caption="Servidores DLNA disponibles en Evermusic" width="500" >}}

4. Verás una lista de carpetas disponibles en el servidor multimedia.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_45b5b6b0435945d1b9914ee1acb71698~mv2.jpg" alt="Carpetas Evermusic" caption="Explorar carpetas compartidas del servidor DLNA" width="500" >}}

5. Abre cualquier carpeta que contenga archivos de audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_dc15136bfd8c4382a23fede8aaf630e5~mv2.jpg" alt="Contenido de carpeta" caption="Ver contenidos de carpetas DLNA compartidas" width="500" >}}

6. Toca cualquier archivo para iniciar el reproductor de audio.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_2f9ba14a07bb4b84b94b2613affeeafa~mv2.jpg" alt="Reproductor de audio" caption="Reproducir archivo de audio desde DLNA en Evermusic" width="500" >}}

7. Para mejorar tu experiencia de audio, toca el icono 'Ecualizador' cerca del indicador de volumen en la parte inferior de la pantalla para activar el ecualizador estilo iPod con preamplificador.

   {{< figure src="/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/21260c_7184e2d07347462aa788052e25074ad2~mv2.jpg" alt="Ecualizador" caption="Usa el ecualizador integrado para una reproducción mejorada" width="500" >}}

## Conclusión

Con el servidor multimedia DLNA en Windows 10 y Evermusic en tu iPhone, puedes disfrutar de streaming de música fluido desde tu computadora a tu dispositivo móvil. ¡Adiós a las limitaciones de almacenamiento y bienvenida la música bajo demanda!

## Preguntas frecuentes

{{% details title="¿Necesito instalar algún software de servidor en Windows 10?" closed="true" %}}
No. Windows 10 incluye un servidor multimedia DLNA integrado. Solo necesitas activar el streaming multimedia en la configuración del Centro de redes y recursos compartidos. No se requiere software de terceros.
{{% /details %}}

{{% details title="¿Mi iPhone necesita estar en la misma red Wi-Fi?" closed="true" %}}
Sí. El streaming DLNA funciona a través de tu red local. Tanto tu PC con Windows 10 como tu iPhone deben estar conectados a la misma red Wi-Fi para que Evermusic descubra el servidor DLNA.
{{% /details %}}

{{% details title="¿Qué formatos de audio puedo transmitir vía DLNA?" closed="true" %}}
El servidor Windows DLNA comparte archivos de tu carpeta Música independientemente del formato. Evermusic soporta MP3, FLAC, AAC, WAV, OGG, AIFF y muchos otros formatos, por lo que puedes reproducir prácticamente cualquier archivo de audio del servidor.
{{% /details %}}

{{% details title="¿Puedo usar Flacbox en lugar de Evermusic?" closed="true" %}}
Sí. Flacbox también soporta navegación y reproducción DLNA/UPnP. Puedes usar cualquiera de las dos apps para descubrir y reproducir música desde tu servidor Windows DLNA.
{{% /details %}}

{{% details title="¿El streaming DLNA usa datos móviles?" closed="true" %}}
No. DLNA funciona completamente en tu red Wi-Fi local. No usa ningún dato móvil. Sin embargo, ambos dispositivos deben permanecer conectados a la misma red durante la reproducción.
{{% /details %}}
