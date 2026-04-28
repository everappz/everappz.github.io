---
title: "Cómo conectar Synology NAS y escuchar música en tu iPhone o Mac"
date: 2024-09-19
description: "Aprende a conectar tu Synology NAS usando la API nativa o QuickConnect y transmitir música de alta calidad a tu iPhone o Mac con Evermusic y Flacbox."
keywords: ["synology nas", "transmitir música", "quickconnect", "evermusic synology", "flacbox synology", "reproductor de música nas", "música iphone nas"]
tags: ["música", "transmisión", "nas", "synology", "quickconnect"]
readingTime: 4
---

{{< author-byline >}}


**Resumen:** Conecta tu Synology NAS a Evermusic o Flacbox usando la API nativa de Synology -- ya sea manualmente mediante dirección IP o automáticamente mediante QuickConnect ID. QuickConnect te permite transmitir música de forma remota sin redirección de puertos. Ambas aplicaciones soportan FLAC, MP3, WAV y otros formatos de alta resolución.

Si buscas una forma sencilla de conectar tu Synology NAS y disfrutar de tu biblioteca musical en tu iPhone o Mac, las aplicaciones Evermusic y Flacbox son las soluciones perfectas. Estas aplicaciones soportan una amplia gama de formatos de audio, incluyendo FLAC, MP3 y WAV, facilitando la transmisión y escucha de música de alta calidad directamente desde tu Synology NAS.

En esta guía, te mostraremos cómo conectar tu Synology NAS a la aplicación Evermusic o Flacbox usando la API nativa de Synology y la función QuickConnect. Aprovechando la API directa de Synology, puedes acceder de forma segura a tu biblioteca musical fuera de tu red doméstica sin necesidad de configuraciones complicadas como WebDAV, SMB, DLNA. Con QuickConnect, podrás transmitir y gestionar tu música desde cualquier lugar, usando tu iPhone o Mac.

## Paso 1: Configurar permisos de carpeta compartida (Opcional)

1. Abre el **Panel de control** y ve a la sección **Carpeta compartida**.

![Carpeta compartida](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png)

2. Selecciona la carpeta **Música** y haz clic en **Editar**.

3. En la pestaña **Permisos**, configura los permisos. Habilita el acceso de invitados con solo lectura si solo necesitas escuchar música, o lectura/escritura si necesitas modificar archivos. Guarda los cambios.

![Permisos](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_43b09e36fc284a43b867e588da32b314~mv2.png)

## Paso 2: Encontrar la dirección IP del Synology NAS

1. Abre el **Panel de control** y ve a la pestaña **Interfaz de red**.

![Interfaz de red](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png)

2. O usa tu navegador web para visitar [find.synology.com](http://find.synology.com).

![Encontrar Synology](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png)

3. Anota la dirección IP de tu Synology NAS (por ejemplo, 192.168.18.137).

## Paso 3: Encontrar los puertos de red del Synology NAS

Puedes encontrar la documentación oficial de Synology para los puertos de red predeterminados de DSM en este [artículo del Centro de conocimiento de Synology](https://kb.synology.com/en-global/DSM/tutorial/What_network_ports_are_used_by_Synology_services).

Synology DSM utiliza los siguientes puertos predeterminados:
- **HTTP (Acceso web):** Puerto **5000**
- **HTTPS (Acceso web seguro):** Puerto **5001**

Estos son los puertos predeterminados para acceder a la interfaz de DSM.

![Puertos de red](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61d64239cd7e4bfab2530c32b5a8ceee~mv2.png)

## Paso 4: Habilitar la función QuickConnect ID

Un QuickConnect ID de Synology es un identificador único que te permite acceder a tu Synology NAS de forma remota a través de internet sin necesidad de configurar ajustes de red complicados como la redirección de puertos. QuickConnect simplifica el acceso remoto usando los servidores de Synology para establecer una conexión entre tu NAS y tu dispositivo, como tu smartphone o computadora, a través del QuickConnect ID.

**Cómo encontrar o configurar tu QuickConnect ID:**

1. **Inicia sesión en DSM.**
2. Ve a **Panel de control > Acceso externo > QuickConnect**.
3. **Habilita QuickConnect** y crea o visualiza tu QuickConnect ID único.

![QuickConnect](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_504d681f7e5848fabe0ee57fc80e770b~mv2.png)

## Paso 5: Conectar al Synology NAS en tu iPhone/Mac usando Evermusic o Flacbox

[Evermusic](https://apps.apple.com/us/app/evermusic-cloud-music-player/id885367198) y [Flacbox](https://apps.apple.com/us/app/flacbox-hi-res-music-player/id1097564256) son aplicaciones de reproducción de música diseñadas para dispositivos iOS y macOS, cada una ofreciendo características y capacidades únicas para gestionar y disfrutar de tu biblioteca musical.

1. Abre la aplicación Evermusic o Flacbox y ve a la pestaña **Conexiones**.

![Conexiones](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png)

2. Elige **Conectar un servicio en la nube** y selecciona **Synology Drive**.

![Synology Drive](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_eb5e8f1a02b64748a9fa23eee5df7e0d~mv2.jpg)

Tienes dos opciones de conexión: **manual** usando la dirección IP del servidor y el puerto, o **automática** mediante QuickConnect ID.

### Conexión manual

Para el método manual, necesitarás la dirección IP directa y el número de puerto que obtuviste en los pasos anteriores.

1. Ingresa la URL del servidor que obtuviste en el paso 2, usando el siguiente formato: PROTOCOLO://DIRECCIÓN_IP:NÚMERO_PUERTO
   - Usa el **puerto 5000** para HTTP y el **puerto 5001** para conexiones HTTPS.

   Por ejemplo:
   - HTTP: [http://192.168.18.137:5000](http://192.168.18.137:5000)
   - HTTPS: [https://192.168.18.137:5001](https://192.168.18.137:5001)

2. El número de puerto real se puede confirmar en el paso 3 de tu configuración.
3. Ingresa tu **nombre de usuario** y **contraseña** del Synology NAS.
4. Toca **Iniciar sesión** para establecer la conexión.

![Conexión manual](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_8952ec16c92046fd81d62bff4139a97b~mv2.jpg)

### Conexión automática

Para la conexión automática, usarás el **QuickConnect ID** del paso 4. En lugar de ingresar manualmente la dirección IP y el número de puerto de tu Synology NAS, simplemente ingresa el **QuickConnect ID**. La aplicación recuperará automáticamente la información de conexión necesaria.

Este método te permite acceder a tu NAS de forma remota, incluso fuera de tu red doméstica, para que puedas gestionar tus archivos desde internet sin necesidad de configurar redirección de puertos o direcciones IP estáticas.

![Conexión automática](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_68bd2a6bcbf844eea7248cbe1c1cb3fe~mv2.jpg)

## Autenticación de dos factores

A partir de DSM 4.2, Synology introdujo la **verificación en dos pasos** para mejorar la seguridad. Esta función requiere un código de **contraseña de un solo uso (OTP)**, generado por una aplicación de autenticación, además de tus credenciales de inicio de sesión habituales. Si has habilitado la verificación en dos pasos, después de ingresar tu nombre de usuario y contraseña, también necesitarás ingresar el OTP para iniciar sesión en tu sesión de DSM.

Ten en cuenta que una vez que tu sesión expire, la aplicación necesitará ser reautorizada manualmente. Para reautorizar:

1. Ve a la pestaña **Conexiones** en la aplicación.
2. Toca el botón **Más acciones** junto al nombre del servidor.
3. Selecciona **Ajustes** del menú para ingresar el nuevo código de autenticación y completar el proceso de reautorización.

Esto asegura que incluso si accedes a tu NAS desde una red no confiable, tus datos permanecen seguros.

## Paso 6: Navegar y reproducir música

1. Una vez conectado, el dispositivo aparecerá en la lista de **Dispositivos conectados**.

![Dispositivos conectados](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_61446121c6b240f1a2c04ecd4c4badc0~mv2.jpg)

2. Navega a la carpeta **Música** y toca cualquier archivo de audio para iniciar la reproducción.

![Reproducir música](/docs/howto/how-to-connect-synology-nas-and-listen-to-music-on-your-iphone-or-mac/21260c_1702cbbfaa474d5b8c64fb9ca5e77dd4~mv2.jpg)

## Paso 7: Agregar carpeta en la nube conectada a la biblioteca musical

1. Abre la sección **Biblioteca musical** en la aplicación.
2. Elige **Agregar música** y selecciona **Conexiones**.
3. Elige tu servidor NAS conectado y selecciona la carpeta **Música**. Toca **Hecho**.
4. La aplicación escaneará la carpeta de música y agregará los archivos de audio compatibles a la biblioteca musical. Los metadatos se cargarán y tus pistas se agruparán por álbum, artista y género.

## Conclusión

Siguiendo estos pasos, puedes configurar fácilmente una conexión en tu Synology NAS y transmitir toda tu biblioteca musical a tu iPhone o Mac usando Evermusic o Flacbox. Ya sea que estés en casa o en movimiento, disfruta de un acceso fluido y de alta calidad a tus pistas favoritas desde cualquier lugar usando QuickConnect. Aprovecha la flexibilidad y comodidad que ofrecen estas aplicaciones y comienza a gestionar tu colección musical con facilidad en todos tus dispositivos.

Con acceso remoto seguro a través de QuickConnect y soporte para una amplia gama de formatos de audio, nunca estarás lejos de tu música. ¡Ahora, tus archivos almacenados en el NAS están a solo un toque de distancia!

## Preguntas frecuentes

{{% details title="¿Cuál es la diferencia entre la conexión manual y QuickConnect?" closed="true" %}}
La conexión manual usa la dirección IP del NAS y el puerto, que funciona en tu red local. QuickConnect usa el servicio de retransmisión de Synology para establecer una conexión desde cualquier lugar a través de internet, sin redirección de puertos.
{{% /details %}}

{{% details title="¿Puedo transmitir música desde Synology NAS fuera de mi red doméstica?" closed="true" %}}
Sí. Habilita QuickConnect en tu Synology NAS y usa el QuickConnect ID en Evermusic o Flacbox para transmitir música desde cualquier lugar con conexión a internet.
{{% /details %}}

{{% details title="¿Qué formatos de audio son compatibles al transmitir desde Synology NAS?" closed="true" %}}
Evermusic y Flacbox soportan FLAC, MP3, AAC, WAV, ALAC, OGG, WMA, DSD y muchos otros formatos. Todos los formatos compatibles funcionan al transmitir desde Synology NAS.
{{% /details %}}

{{% details title="¿Necesito autenticación de dos factores para conectarme?" closed="true" %}}
No, la autenticación de dos factores es opcional. Sin embargo, si has habilitado la verificación en dos pasos en tu Synology DSM, la aplicación te pedirá una contraseña de un solo uso durante el inicio de sesión. Necesitarás reautorizar cuando la sesión expire.
{{% /details %}}

{{% details title="¿Debo usar la API nativa de Synology, WebDAV o SMB para conectarme?" closed="true" %}}
La API nativa de Synology con QuickConnect es la mejor opción para el acceso remoto. Para uso en red local, SMB es típicamente la opción más rápida. WebDAV funciona bien tanto para acceso local como remoto. Evermusic y Flacbox soportan los tres protocolos.
{{% /details %}}
