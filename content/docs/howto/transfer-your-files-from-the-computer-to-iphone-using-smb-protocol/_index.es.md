---
title: "Transferir archivos del ordenador al iPhone usando el protocolo SMB"
description: "Aprende a transferir y acceder a archivos grandes desde tu Mac o Windows PC a tu iPhone o iPad usando Evermusic y el protocolo SMB. Una guía paso a paso para streaming fluido y gestión de archivos."
date: 2022-03-17
readingTime: 3
tags: ["cloud", "streaming", "computer", "mp3", "file", "downloader", "manager", "pc", "mac", "sharing", "windows", "smb"]
keywords: ["transferir archivos a iPhone SMB", "transmitir música del PC en iPhone", "conectar Mac a iPhone SMB", "configuración Evermusic SMB", "acceder a archivos del ordenador iPhone", "compartir música Windows iOS", "transferencia de archivos SMB Evermusic"]
aliases:
  - /post/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/
---

{{< author-byline >}}


**Resumen:** Usa Evermusic en tu iPhone o iPad para acceder a archivos almacenados en tu Mac o Windows PC a través de tu red local mediante SMB. Sin cables, sin iTunes, sin necesidad de subir a la nube. Activa la compartición de archivos en tu ordenador, conéctate desde la app y navega o reproduce tus archivos de forma inalámbrica.

¿Tienes una extensa colección de archivos grandes en tu MAC o PC y deseas acceder a ellos fácilmente desde tu iPhone o iPad? Nuestras aplicaciones proporcionan una solución sencilla.

Sigue estos pasos para habilitar el acceso fluido entre tu ordenador y tu dispositivo iOS usando el protocolo SMB:

## Paso 1: Activar el protocolo SMB en tu ordenador

**Para MAC:**

1. Abre "Preferencias del Sistema" en tu MAC.
2. Haz clic en "Compartir".
3. Activa el servicio "Compartir archivos".
4. Añade tu carpeta de música a la sección "Carpetas compartidas". Añade un usuario y elige el nivel de permisos (Lectura y escritura o Solo lectura). Puedes optar por "Todos: Solo lectura" para la carpeta de música añadida.

   ![Pantalla de configuración del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_4c8f67e6cad0498080909244213f84af~mv2.png)

5. Recuerda la URL del ordenador (smb://192.168.xx.xx), ya que la usarás en los siguientes pasos.
6. Haz clic en "Opciones" y activa "Compartir archivos y carpetas mediante SMB".

   ![Pantalla de compartición de archivos del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_32c05fd0930a4ec28256afe40c0ba8a5~mv2.png)

7. Activa "Compartición de archivos de Windows" para las cuentas disponibles.

   ![Pantalla de compartición SMB del Mac](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_26acaa067aae40788465c1698b0458dc~mv2.png)

**Para Windows PC:**

1. Haz clic derecho en tu carpeta de música.
2. Selecciona "Propiedades".
3. Navega a la pestaña "Compartir".
4. Haz clic en "Compartir..."
5. Elige las personas con quienes quieres compartir la carpeta y especifica el nivel de permisos. Puedes seleccionar "Todos: Lectura" para la carpeta de música elegida.

   ![Pantalla de compartición SMB de Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_c503c5d0d1f44daeb14d5a4cadfe9ac2~mv2.png)

6. Haz clic en "Hecho".
7. Haz clic en "Hecho" en la ventana "Compartir archivos" y recuerda la ruta de la carpeta.

   ![Carpeta compartida SMB de Windows](/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_350e2dca694b41bcade8f455acc4e481~mv2.png)

## Paso 2: Conectar tu dispositivo iOS

1. Abre la app en tu iPhone o iPad.
2. Ve a la pestaña "Conexiones".

   {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_1b1864a302194414a6ec4dc14f95bfaf~mv2.png"
  alt="Pantalla de Conexiones de Evermusic"
  caption="Pantalla de Conexiones de Evermusic"
  width="400"
>}}

*Si tu ordenador aparece en la sección "Dispositivos disponibles":*

Si tu ordenador es visible en la sección "Dispositivos disponibles" y seleccionaste "Todos: Solo lectura" en el paso anterior, simplemente toca tu ordenador y se conectará automáticamente.

*Si tu ordenador no aparece automáticamente:*

1. Toca "Conectar un servicio en la nube".
2. Selecciona "SMB" en la pantalla "Conectar un servicio en la nube".

   
{{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_fd5a7b81f9cf427e99ccb0024c0a686c~mv2.jpeg"
  alt="Pantalla de Conectar un servicio en la nube de Evermusic"
  caption="Pantalla de Conectar un servicio en la nube de Evermusic"
  width="400"
>}}

3. En la pantalla "Conexión SMB", introduce la URL del servidor con la ruta de la carpeta compartida. Puedes usar el nombre del servidor o la IP del servidor:

   ```
   smb://ameleshko.local/Music/ 
   smb://192.168.0.102/Music/ 
   smb://192.168.0.102/
   ```

4. Introduce tu nombre de usuario y contraseña o deja estos campos en blanco si seleccionaste "Todos: Solo lectura" en el paso anterior.
5. El campo "WORKGROUP" es opcional y debe usarse si tienes un Active Directory Domain.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_b6a9a4ad317447768f7f38b41bc07aca~mv2.png"
  alt="Pantalla del conector SMB de Evermusic"
  caption="Pantalla del conector SMB de Evermusic"
  width="400"
>}}

6. Una vez que hayas conectado tu ordenador usando el protocolo SMB, aparecerá en la sección "Servicios en la nube" de la pantalla "Conexiones".
7. Abre el servicio conectado y navega a la carpeta deseada.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_ed605ed873184662bbc26e75651cc8d8~mv2.png"
  alt="Carpeta SMB abierta en Evermusic"
  caption="Carpeta SMB abierta en Evermusic"
  width="400"
>}}

8. Puedes utilizar el gestor de archivos integrado para editar tus archivos según sea necesario.

  {{< figure
  src="/docs/howto/transfer-your-files-from-the-computer-to-iphone-using-smb-protocol/21260c_a514e7cbd5ba43aa9a49646a5cf138b4~mv2.jpeg"
  alt="Gestor de archivos de Evermusic"
  caption="Gestor de archivos de Evermusic"
  width="400"
>}}

## Paso 3: Solución para carpetas SMB2 con caracteres especiales

A veces puedes encontrar problemas con carpetas que contienen caracteres especiales al usar el protocolo SMB2. Aquí tienes algunos pasos para resolver este problema:

1. **Activar SMB 1:**  
   • Como solución temporal, intenta activar SMB 1 en tu servidor y en la configuración de la app. Esto puede ayudar a evitar los problemas relacionados con caracteres especiales en los nombres de las carpetas.

2. **Usar el menú de apertura de archivos del sistema:**  
   • Navega a "Archivos locales".  
   • Desplázate hacia abajo hasta la sección "Archivos en este dispositivo".  
   • Toca "Abrir archivos..." o "Abrir carpetas...".  
   • Localiza tu servidor y selecciona los archivos o carpetas que necesitas.  
   • Toca "Abrir" para confirmar tu selección.

3. **Protocolos alternativos:**  
   • Si el problema persiste, considera conectarte a tu NAS usando los protocolos WebDAV o DLNA si tu NAS soporta estas opciones. Estos protocolos pueden manejar los caracteres especiales de manera más adecuada.

Siguiendo estos pasos, puedes mitigar los problemas con caracteres especiales en los nombres de las carpetas al usar el protocolo SMB2.

## Conclusión

Con estos pasos, puedes acceder fácilmente a tu gran colección de archivos desde tu MAC o PC en tu iPhone o iPad usando nuestras aplicaciones.

## Preguntas frecuentes

{{% details title="¿Puedo acceder a archivos en mi PC desde mi iPhone sin iTunes?" closed="true" %}}
Sí. Evermusic se conecta a tu ordenador mediante SMB en tu red Wi-Fi local. No se necesita sincronización con iTunes o Finder. Activa la compartición de archivos en tu PC y conéctate directamente desde la app.
{{% /details %}}

{{% details title="¿Funciona el acceso a archivos SMB a través de Internet?" closed="true" %}}
No. SMB es un protocolo de red local. Tu iPhone y tu ordenador deben estar en la misma red Wi-Fi. Para acceso remoto, sube archivos a un servicio en la nube como Google Drive o Dropbox y conéctate a él en Evermusic.
{{% /details %}}

{{% details title="¿Qué tipos de archivos puedo acceder mediante SMB?" closed="true" %}}
Evermusic soporta MP3, FLAC, AAC, WAV, AIFF, OGG, WMA, ALAC y otros formatos de audio. También puedes navegar y gestionar archivos no audio usando el gestor de archivos integrado.
{{% /details %}}

{{% details title="¿Puedo transferir archivos desde un NAS a mi iPhone usando SMB?" closed="true" %}}
Sí. La mayoría de dispositivos NAS (Synology, QNAP, WD My Cloud y otros) soportan SMB. Conéctate a tu NAS usando los mismos pasos de esta guía.
{{% /details %}}

{{% details title="¿Necesito copiar archivos a mi iPhone para reproducirlos?" closed="true" %}}
No. Evermusic transmite archivos directamente desde tu ordenador o NAS a través de la red. Los archivos no se copian a tu iPhone a menos que elijas descargarlos para reproducción sin conexión.
{{% /details %}}

{{% details title="¿Es segura la compartición de archivos SMB?" closed="true" %}}
La compartición de archivos SMB funciona solo en tu red local. Otros dispositivos en redes diferentes no pueden acceder a tus carpetas compartidas. Para mayor seguridad, usa un nombre de usuario y contraseña en lugar del acceso anónimo (Todos).
{{% /details %}}
