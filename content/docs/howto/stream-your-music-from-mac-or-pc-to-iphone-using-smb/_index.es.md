---
title: "Transmite tu música desde Mac o PC al iPhone usando SMB"
description: "Aprende cómo transmitir tu colección de música desde Mac o Windows PC a tu iPhone o iPad usando Evermusic y el protocolo SMB. Una guía sencilla paso a paso para conectar y disfrutar del audio sin sincronizar."
date: 2016-05-29
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transmitir música de Mac a iPhone", "streaming audio SMB iOS", "configuración Evermusic SMB", "conectar música PC iPhone", "compartir música Mac iOS", "streaming archivos SMB Windows", "acceso Evermusic carpetas PC"]
aliases:
  - /post/stream-your-music-from-mac-or-pc-to-iphone-using-smb/
  - /single-post/Stream-your-music-from-MAC-or-PC-to-iPhone-using-SMB/
---

{{< author-byline >}}


**Resumen:** Usa la aplicación Evermusic para iPhone o iPad para transmitir música desde tu Mac o Windows PC a través de tu red local usando SMB. Sin sincronización, sin copias -- solo activa el uso compartido de archivos en tu computadora, conéctate en la app y reproduce. La configuración toma menos de 5 minutos.

¿Te estás ahogando en un mar de música en tu MAC o PC y quieres disfrutarla sin complicaciones en tu iPhone o iPad? No busques más que Evermusic. Con Evermusic, es increíblemente simple conectar tu computadora usando el protocolo SMB y transmitir tus melodías favoritas sin preocuparte por ocupar espacio adicional en el dispositivo o lidiar con problemas de sincronización. Aquí tienes una guía paso a paso para comenzar:

## Paso 1: Activa el protocolo SMB en tu computadora

![Evermusic - Soporte SMB - Pantalla de compartir en Mac](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

### Si usas MAC

- Abre Preferencias del Sistema -> Compartir.
- Activa el servicio de Compartir Archivos.
- En la sección "Carpetas compartidas", agrega tu carpeta de música, selecciona un usuario y establece los niveles de permisos (Lectura y Escritura o Solo Lectura).
- Para mayor comodidad, puedes seleccionar "Todos: Solo Lectura" para la carpeta de música, haciéndola fácilmente accesible en Evermusic.
- No olvides recordar la URL de tu computadora (smb://192.168.xx.xx) para los siguientes pasos.

![Evermusic - Soporte SMB - Pantalla de compartir archivos](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

- Toca "Opciones" y activa "Compartir archivos y carpetas usando SMB."
- Activa "Compartir archivos de Windows" para las cuentas disponibles.

![Evermusic - Soporte SMB - Pantalla de compartir archivos y carpetas](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

### Si usas un Windows PC

![Evermusic - Soporte SMB - Compartir archivos en Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

- Haz clic derecho en tu carpeta de música.
- Selecciona "Propiedades."
- Abre la pestaña "Compartir."
- Haz clic en "Compartir..."
- Elige las personas con las que quieres compartir y establece sus niveles de permisos.
- Al igual que con MAC, puedes optar por "Todos: Lectura" para la carpeta de música seleccionada.
- Haz clic en "Hecho" para guardar tu configuración.

![Evermusic - Soporte SMB - Carpeta compartida en Windows](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Paso 2: Agrega tu computadora automáticamente

- Ahora, abre Evermusic y ve a la pestaña "Conexiones" ("Red" si usas una versión antigua de la app).
- Si ves tu computadora en la sección "Dispositivos disponibles" ("Recursos compartidos disponibles" si usas una versión antigua de la app) y seleccionaste "Todos: Solo Lectura" en el paso anterior, simplemente toca tu computadora y se conectará automáticamente.
- Si esto no sucede, puedes agregar tu computadora manualmente.

![Evermusic - Soporte SMB - Pantalla de conexión de cuenta](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_b1a1b89d7756458c952957fc2dd05582~mv2.jpg)

## Paso 3: Agrega tu computadora manualmente

- Toca "Conectar un servicio en la nube" ("Agregar cuenta" si usas una versión antigua de la app)
- Selecciona "SMB" de la lista de servidores disponibles en la siguiente pantalla.
- En la pantalla de configuración de "SMB":
  - Ingresa la URL del servidor con la ruta de la carpeta compartida. Puedes ingresar el nombre del servidor o la IP del servidor. Por ejemplo:
  
    ```
    smb://ameleshko.local/Music/
    smb://192.168.0.102/Music/
    smb://192.168.0.102/
    ```
  
  - Ingresa tu Usuario y Contraseña o deja estos campos en blanco si seleccionaste "Todos: Solo Lectura" en el paso anterior.
  - El campo "WORKGROUP" es opcional y debe usarse si tienes un dominio Active Directory.

![Evermusic - Soporte SMB - Pantalla de ingreso de credenciales](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_9e043c2fa28d4932a7e7fb7e01df6923~mv2.jpg)

Una vez que hayas conectado tu cuenta SMB, aparecerá en la sección "Servicios en la nube" ("Cuentas"). Abre la cuenta conectada tocándola, navega a la carpeta de música y toca cualquier archivo de audio para iniciar el reproductor.

![Evermusic - Soporte SMB - Pantalla de abrir carpeta conectada](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_d517e0d9a8ae4d5d973f0b42e396dc71~mv2.jpg)

Disfruta de tu colección de música sin problemas en tu iPhone o iPad con Evermusic.

![Evermusic - Soporte SMB - Pantalla del reproductor de audio](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/21260c_fa2058e0ed9d48e0921b7229e5747f02~mv2.jpg)

## Paso 4: Solución alternativa para SMB2

Si encuentras problemas al navegar carpetas o reproducir archivos que contienen símbolos especiales (como ü, ö, é), esto puede estar relacionado con el protocolo SMB2. Estamos trabajando activamente para resolver este problema.

Como solución temporal, intenta habilitar SMB 1 en tu servidor y en la configuración de la app. Alternativamente, puedes conectarte a tu servidor SMB usando el menú de apertura de archivos del sistema. Así es cómo:

1. Navega a "Archivos locales."
2. Desplázate hacia abajo hasta la sección "Archivos en este dispositivo" y toca "Abrir archivos..." o "Abrir carpetas..."
3. Localiza tu servidor y selecciona los archivos o carpetas que necesitas.
4. Toca "Abrir" para confirmar tu selección.

## Paso 5: Solución alternativa con WebDAV

Adicionalmente, puedes intentar conectarte a tu NAS usando los protocolos WebDAV o DLNA si son compatibles.

Siguiendo estos pasos, puedes evitar los problemas relacionados con símbolos especiales en los nombres de archivos y continuar disfrutando de tus archivos multimedia.

P.D. También puedes transferir archivos de audio desde tu MAC/PC a tu iPhone usando Compartir Archivos de iTunes y reproducir archivos de audio locales. Aprende más sobre esta función en nuestra guía: [Cómo reproducir archivos de iTunes en iPhone](/docs/howto/how-to-play-local-itunes-files-on-my-iphone).

## Preguntas frecuentes

{{% details title="¿Puedo transmitir música desde mi PC a mi iPhone sin iTunes?" closed="true" %}}
Sí. Evermusic se conecta a tu PC a través de SMB en tu red Wi-Fi local. No se requiere iTunes. Solo activa el uso compartido de archivos en tu PC y conéctate en la app.
{{% /details %}}

{{% details title="¿El streaming SMB usa datos móviles?" closed="true" %}}
No. SMB funciona a través de tu red Wi-Fi local. No se necesita conexión a Internet ni datos móviles.
{{% /details %}}

{{% details title="¿Qué formatos de audio soporta Evermusic a través de SMB?" closed="true" %}}
Evermusic soporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC y otros formatos de audio comunes. Los archivos se reproducen directamente desde el recurso compartido SMB.
{{% /details %}}

{{% details title="¿Puedo transmitir música desde un NAS a mi iPhone?" closed="true" %}}
Sí. Si tu NAS soporta SMB (la mayoría lo hace, incluyendo Synology, QNAP y WD My Cloud), puedes conectarte a él usando los mismos pasos de esta guía.
{{% /details %}}

{{% details title="¿Necesito mantener mi computadora encendida mientras transmito?" closed="true" %}}
Sí. Como Evermusic transmite archivos directamente desde tu computadora, debe estar encendida y conectada a la misma red que tu iPhone.
{{% /details %}}

{{% details title="¿Hay un límite de tamaño de archivo para el streaming SMB?" closed="true" %}}
No. Evermusic transmite archivos de cualquier tamaño a través de SMB. Los archivos grandes sin pérdida (FLAC, WAV) funcionan sin problemas.
{{% /details %}}
