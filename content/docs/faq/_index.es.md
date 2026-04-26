---
date: '2025-06-12T17:00:00+00:00'
title: 'Preguntas frecuentes'
description: 'Encuentra respuestas a preguntas comunes sobre Evermusic, Flacbox, Evervideo y Evertag. Explora funciones como streaming en la nube, gestión de archivos, opciones de reproducción, edición de metadatos y más.'
keywords: [
  "Preguntas frecuentes Evermusic", "soporte Flacbox", "ayuda Evervideo", "preguntas Evertag",
  "cómo usar Evermusic", "solución de problemas reproductor de música en la nube", "guía de reproducción sin conexión",
  "soporte editor de etiquetas de audio", "problemas de streaming de vídeo", "tutorial de transferencia de archivos"
]
tags: [
  "FAQ", "ayuda", "soporte", "evermusic", "flacbox", "evervideo", "evertag",
  "configuración en la nube", "problemas de reproducción", "gestión de archivos", "edición de metadatos",
  "solución de problemas", "modo sin conexión", "reproductor de música", "reproductor de vídeo"
]
---


{{< lottie src="/images/juicy-json/juicy-woman-focused-on-online-learning.json" width="85%" >}}

## Aprende a usar nuestras aplicaciones

¿Buscas respuestas o ayuda para usar una de nuestras aplicaciones? Estás en el lugar indicado.

Nuestras páginas de preguntas frecuentes te ayudarán a conectar el almacenamiento en la nube, gestionar archivos de música y vídeo, configurar la reproducción sin conexión, ajustar el ecualizador, corregir metadatos y mucho más.

Explora las preguntas frecuentes de tu aplicación a continuación para comenzar, o navega por las preguntas y respuestas habituales que hemos recibido de los correos electrónicos de los usuarios.

## Elige tu aplicación

{{< cards cols="2">}}

{{< card 
  link="/docs/faq/evervideo" 
  title="Evervideo" 
  subtitle="Reproduce vídeos en 360°, transmite desde iCloud, ve con subtítulos, aplica un ecualizador de vídeo, organiza el contenido con listas de reproducción y descarga vídeos para verlos sin conexión."
  image="/images/app_icons/webp/Evervideo_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< card 
  link="/docs/faq/evermusic"
  title="Evermusic" 
  subtitle="Reproductor de música en la nube con modo sin conexión, ecualizador de audio, crossfade, reproducción sin interrupciones, gestión de listas de reproducción, biblioteca de música completa y gestor de archivos integrado."
  image="/images/app_icons/webp/Evermusic_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/flacbox"
  title="Flacbox" 
  subtitle="Reproductor de audio de alta resolución para iPhone y Mac. Escucha formatos sin pérdida como FLAC, ALAC, APE y DSD. Ajusta la salida con configuración avanzada de audio."
  image="/images/app_icons/webp/Flacbox_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;"  
>}}

{{< card 
  link="/docs/faq/evertag"
  title="Evertag" 
  subtitle="Editor inteligente de etiquetas musicales con edición por lotes. Corrige metadatos faltantes, portadas de álbumes y más. Edita etiquetas ID3, FLAC, APE — más de 120 campos compatibles." 
  image="/images/app_icons/webp/Evertag_Icon-App-1024x1024.webp"
  method="Resize"
  options="200x q80 webp"
  imageStyle="width: 72px; height: auto; margin-left: 1rem; margin-top: 1rem; border-radius: 12px; align-self: start; flex-shrink: 0;" 
>}}

{{< /cards >}}

## Problemas comunes y respuestas

<div class="hx:mt-6"></div>

<div class="hx:w-full">

{{% details title="¿Por qué no puedo iniciar sesión en pCloud en una versión anterior de iOS (15.8.4)?" closed="true" %}}
La página de inicio de sesión web de pCloud puede no mostrarse correctamente en versiones antiguas de iOS como la 15.8.4, lo que impide introducir el correo electrónico y la contraseña en la pantalla de conexión a la nube.<br><br>

Como alternativa, puedes usar el protocolo **WebDAV**, compatible con pCloud y que funciona de forma fiable en todas las versiones de iOS.

**Configuración WebDAV:**<br>
- **Servidores EE. UU.:** `https://webdav.pcloud.com`  
- **Servidores europeos:** `https://ewebdav.pcloud.com`  
- **Nombre de usuario:** Tu dirección de correo electrónico de pCloud  
- **Contraseña:** La contraseña de tu cuenta pCloud  

Abre la aplicación → Conexiones → Conectar con almacenamiento en la nube → Elige **WebDAV** → Introduce tus credenciales y la URL del servidor.

Este método te permitirá conectarte a tu almacenamiento pCloud y acceder a tus archivos sin problemas en dispositivos antiguos.
{{% /details %}}

{{% details title="¿Cómo reproduzco música por AirPlay desde el Mac (macOS)?" closed="true" %}}
La versión macOS de la aplicación no incluye botones integrados de AirPlay, Chromecast ni Bluetooth como en iOS.<br><br>

Para usar **AirPlay** en tu MacBook Pro, sigue estos pasos:

1. Ve a la **esquina superior derecha** de tu pantalla y abre el **Centro de control** (cerca del reloj).  
2. Haz clic en el icono de **Sonido/Volumen**.  
3. En la siguiente pantalla, haz clic en **AirPlay** para ver la lista de dispositivos AirPlay disponibles.  
4. Selecciona el dispositivo deseado para comenzar a transmitir tu música.  

Esto enrutará todo el audio del sistema (incluyendo el de Evermusic o Flacbox) a tu dispositivo AirPlay elegido.
{{% /details %}}

{{% details title="¿Por qué no se ha activado mi compra Premium en el Mac si la compré en el iPhone?" closed="true" %}}
Las compras de por vida y las suscripciones se sincronizan entre iOS y Mac a través de **iCloud**.<br><br>

Para activar Premium en tu Mac:<br>
- Asegúrate de tener la última versión de la aplicación instalada en ambos dispositivos<br>
- Activa **iCloud** en ambos dispositivos<br>
- Inicia la aplicación en tu dispositivo iOS y espera 1 minuto para que se cargue la información de compra<br>
- En tu Mac, instala la aplicación desde el App Store con el **mismo Apple ID**<br>
- Inicia la aplicación y espera unos segundos para que se sincronice la información<br>
- Alternativamente, toca **Restaurar compras** en la configuración de la aplicación en ambos dispositivos<br><br>

Las funciones Premium deberían activarse automáticamente en el Mac.
{{% /details %}}

{{% details title="¿Cómo puedo sincronizar las listas de reproducción automáticamente entre dispositivos?" closed="true" %}}
Actualmente **no hay sincronización automática** para las listas de reproducción.<br><br>

Puedes usar una de las siguientes opciones:<br>
- **Copia de seguridad y restauración** desde la configuración de la aplicación [Cómo transferir tu biblioteca de música entre dispositivos en Evermusic: guía paso a paso](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/)<br>
- **Exportar lista de reproducción a M3U** e importarla en otro dispositivo:<br>
  - [Cómo exportar listas de reproducción](/docs/howto/export-tracks-collection-from-evermusic-flacbox-to-m3u-csv-txt/)<br>
  - [Cómo importar listas de reproducción](/docs/howto/how-to-import-m3u-playlist-to-evermusic-and-flacbox/)<br>
- **Archivar lista de reproducción o álbumes** y transferirlos vía ZIP:<br>
  - [Guía de archivo de listas de reproducción](/docs/howto/how-to-archive-zip-playlists-albums-artists-and-genres-in-evermusic-flacbox-and-transfer-to/)
{{% /details %}}

{{% details title="¿Es seguro usar sus aplicaciones? ¿Puedo desactivar los análisis?" closed="true" %}}
Sí, tu privacidad es nuestra máxima prioridad.<br><br>

- Todos los datos — archivos de música, configuración, inicios de sesión en la nube — se quedan en tu dispositivo<br>
- Las credenciales de inicio de sesión se almacenan de forma segura en el **iOS Keychain**<br>
- Solo recopilamos informes anónimos de errores y uso<br>
- Puedes desactivarlo en **Configuración de la aplicación → Análisis**<br><br>

Más información:<br>
- [Política de privacidad](/legal/privacy-policy/)<br>
- [Seguridad de Apple Keychain](https://support.apple.com/guide/security/keychain-data-protection-secb0694df1a/web)<br><br>

Al usar anuncios personalizados, Google Mobile Ads requiere mostrar la configuración de consentimiento.<br>
Los usuarios Premium no ven anuncios y el SDK de anuncios está completamente desactivado.
{{% /details %}}

{{% details title="¿Sus aplicaciones son compatibles con el Compartir en familia?" closed="true" %}}
Sí, el Compartir en familia es compatible.<br><br>

Para compartir compras integradas en la aplicación:<br>
- Asegúrate de que la compra esté configurada para compartirse con tu grupo familiar<br>
- En el dispositivo del familiar, ve a **Ajustes > Compras > Restaurar compras**<br>
- Esto solicitará los datos de compra a los servidores de Apple y los activará en su dispositivo
{{% /details %}}

{{% details title="¿Cómo acelero la sincronización de metadatos y de la nube?" closed="true" %}}
Para mejorar la velocidad de sincronización, activa las tareas en segundo plano:<br><br>

- **Ajustes → Biblioteca de música → Lectura de metadatos → Lectura de metadatos en segundo plano**<br>
- **Ajustes → Biblioteca de música → Sincronización de música en línea → Sincronización en segundo plano**<br><br>

Además, en macOS, aumenta la velocidad de lectura de metadatos en **Ajustes → Biblioteca de música**.<br>
Si el reproductor está activo (reproduciendo audio), iOS no suspenderá la aplicación, lo que permite una sincronización continua.
{{% /details %}}

{{% details title="¿Cómo puedo cancelar mi suscripción?" closed="true" %}}
Puedes cancelar tu suscripción siguiendo las instrucciones oficiales de Apple:<br>
👉 [Cómo cancelar una suscripción](https://support.apple.com/en-us/118428)
{{% /details %}}

{{% details title="¿Cómo puedo conectarme y transmitir audio desde WD MyCloud EX2 Ultra?" closed="true" %}}

Cuando añades una conexión en la aplicación mediante **Conexiones > Conectar con almacenamiento en la nube > My Cloud Home**, está diseñado oficialmente para admitir dispositivos **WD MyCloud Home**.<br>
WD MyCloud EX2 Ultra utiliza acceso restringido para las aplicaciones.<br><br>

Sin embargo, si te has conectado correctamente a un **WD MyCloud EX2 Ultra**, **WD MyCloud Mirror** u otro modelo de almacenamiento **WD MyCloud**, puedes seguir usándolo con la siguiente solución:<br><br>

1. Abre **Conexiones → Conectar con almacenamiento en la nube → My Cloud Home**<br>
2. Crea una carpeta usando el gestor de archivos integrado<br>
3. Sube archivos de música a esta carpeta<br>
4. Se almacenarán en un "sandbox" accesible solo por la aplicación<br>
5. Ahora puedes transmitirlos o descargarlos directamente<br><br>

⚠️ Solo las carpetas creadas a través de la aplicación serán accesibles desde el NAS.
{{% /details %}}

{{% details title="¿Cómo me conecto a Koofr.eu?" closed="true" %}}
Puedes conectar Koofr usando **WebDAV**.<br><br>

- Guía de configuración WebDAV de Koofr: [blog de koofr.eu](https://koofr.eu/blog/posts/3-ways-to-map-koofr-as-a-network-drive-explained)<br>
- Guía WebDAV de Evermusic/Flacbox: [Cómo conectar almacenamiento NAS con WebDAV y escuchar música en iPhone o Mac](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/)
{{% /details %}}

{{% details title="¿Cuáles son los esquemas de URL de la aplicación?" closed="true" %}}
Aquí están los esquemas compatibles:<br><br>

**Evermusic**<br>
- iOS (icono azul): `lsevermusic://`<br>
- macOS: `lsevermusicmac://`<br>
- iOS (icono rojo): `lsevermusicpro://`<br><br>

**Flacbox**<br>
- iOS: `lsflap://`<br>
- macOS: `lsflapmac://`<br><br>

**Evertag**<br>
- iOS: `lsevertag://`<br>
- macOS: `lsevertagmac://`<br><br>

**Evervideo**<br>
- iOS: `lsevervideo://`<br>
- macOS: `lsevervideomac://`
{{% /details %}}

{{% details title="La música se detiene cuando la aplicación está en segundo plano — ¿cómo lo soluciono?" closed="true" %}}
Si la aplicación falla o se pausa en segundo plano:<br>
- Ve a **Ajustes > Biblioteca de música > Sincronización de música en línea > Sincronización en segundo plano → Desactivar**<br>
- **Ajustes > Biblioteca de música > Lectura de metadatos > Lectura de metadatos en segundo plano → Desactivar**<br>
- **Ajustes > Gestor de archivos > Transferencias en segundo plano → Desactivar**
{{% /details %}}

{{% details title="La reproducción sin interrupciones no funciona — ¿cómo lo soluciono?" closed="true" %}}
La reproducción sin interrupciones depende de la versión de iOS y del motor de audio.<br>
Prueba a cambiar el motor de audio:<br>
- Ve a **Ajustes → Reproductor de audio → General → Procesador de audio**<br>
- Selecciona **Core Audio** para mejor compatibilidad con la reproducción sin interrupciones
{{% /details %}}

{{% details title="¿Por qué la aplicación solo muestra 100 elementos en una lista?" closed="true" %}}
La aplicación usa paginación para el rendimiento.<br>
Para desactivarla:<br>
- Ve a **Ajustes → Personalización → Límite de carga de contenido → Desactivado**<br>
Ahora todos los elementos se cargarán a la vez.
{{% /details %}}

{{% details title="¿Por qué hay caracteres extraños en los metadatos?" closed="true" %}}
Prueba a activar la normalización de metadatos:<br>
- **Ajustes → Biblioteca de música → Lectura de metadatos → Normalizar codificación de metadatos**
{{% /details %}}

{{% details title="¿Por qué la aplicación no puede leer nombres de carpetas con caracteres especiales?" closed="true" %}}
Este es un problema conocido con el **protocolo SMB2**.<br><br>

Prueba las siguientes soluciones:<br>
- Activa **SMB1** en tu servidor y en la configuración de la aplicación<br>
- Usa el **selector de archivos del sistema**:<br>
  - Ve a **Archivos locales > Archivos en este dispositivo > Abrir archivos...**<br>
  - Selecciona carpetas/archivos usando el menú nativo de Apple<br><br>

Alternativamente, conéctate usando **WebDAV** o **DLNA** si tu NAS los admite.
{{% /details %}}

{{% details title="¿Cómo subo y gestiono música en iCloud?" closed="true" %}}
– **¿Cómo subo música a iCloud?**  <br>
Ve a [https://www.icloud.com](https://www.icloud.com) en tu navegador, crea una carpeta y sube tus archivos de música directamente desde tu Mac o PC.<br>

– **¿Cómo gestiono el almacenamiento de iCloud?**  <br>
Tienes dos opciones:  <br>
1. Usa [https://www.icloud.com](https://www.icloud.com) en tu navegador para organizar, subir o eliminar archivos.<br>  
2. En la aplicación, después de conectarte a iCloud mediante **Conexiones → Conectar con almacenamiento en la nube → iCloud Drive**, usa el gestor de archivos integrado para subir, descargar, renombrar carpetas o eliminar archivos directamente en tu almacenamiento iCloud — sin guardarlos en tu dispositivo.<br>

⚠️ Ten cuidado al eliminar archivos. La aplicación los elimina permanentemente (no irán a la papelera y no podrán recuperarse).<br>

Más información aquí: [Cómo transmitir música desde iCloud Drive en mi iPhone o Mac](/docs/howto/how-to-listen-to-music-from-icloud-drive-on-your-iphone-or-mac/)

{{% /details %}}

{{% details title="¿Cómo puedo transferir mi biblioteca de música de 10 GB de Windows 11 a mi iPhone para reproducción sin conexión?" closed="true" %}}

Tienes varias opciones fiables para mover tu biblioteca de música desde tu PC con Windows 11 al iPhone y usarla sin conexión en la aplicación. Elige el método que mejor te convenga:

1. **Mediante conexión por cable (recomendado para bibliotecas grandes)**  <br>
   Usa la aplicación **Apple Devices** en Windows 11 para transferir archivos directamente al iPhone por USB.  
   Sigue la guía de Apple aquí:  
   https://support.apple.com/en-ph/120402 <br>

2. **De forma inalámbrica a través de Wi-Fi Drive**  <br>
   Activa la función **WiFi Drive** en la aplicación y sube tu música a través de un navegador en tu ordenador.  
   Instrucciones paso a paso aquí:  
   [Cómo transferir archivos de música del ordenador al iPhone sin iTunes con WiFi-Drive](/docs/howto/how-to-transfer-music-from-computer-to-iphone-without-itunes/) <br>

3. **De forma inalámbrica con servidor DLNA**  <br>
   Activa el servidor de medios DLNA en tu ordenador Windows y transmite o transfiere tu biblioteca directamente a la aplicación.  
   Guía:  
   [Cómo activar el servidor de medios DLNA en Windows 10 y reproducir música en iPhone](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone/) <br>

4. **De forma inalámbrica con SMB File Sharing**  <br>
   Activa el **uso compartido de archivos SMB** en tu PC y conéctate a él en la aplicación para explorar, descargar o transferir tus archivos carpeta a carpeta.  
   Instrucciones:  
   [Transferir archivos del ordenador al iPhone con el protocolo SMB](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/) <br>

⚠️ Al transferir bibliotecas grandes (10 GB o más), una transferencia USB por cable suele ser la opción más rápida y estable.

{{% /details %}}

</div>
