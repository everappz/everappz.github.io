---
title: "Cómo configurar un servidor multimedia DLNA/UPnP en iPhone y iPad para transmitir"
description: "Convierte tu iPhone o iPad en un servidor multimedia DLNA/UPnP con Everdisk y transmite fotos, vídeos y música a una smart TV, una videoconsola, VLC o Kodi por Wi-Fi. Configuración completa y cómo conectarte desde TVs Samsung, LG y Sony, Windows, Mac, Linux, Android y otro iPhone."
date: 2026-09-19
tags: ["everdisk", "dlna", "upnp", "servidor multimedia", "transmisión", "smart tv", "iphone", "ipad", "wifi"]
keywords: ["servidor DLNA iPhone", "servidor UPnP iPad", "cómo configurar DLNA en iPhone", "transmitir a smart TV desde iPhone", "servidor multimedia DLNA iOS", "transmitir vídeos a la TV sin cable", "ver fotos del iPhone en la TV", "DLNA iPhone TV Samsung", "DLNA iPhone TV LG", "DLNA iPhone Sony Bravia", "VLC DLNA iPhone", "servidor multimedia Kodi DLNA", "servidor multimedia UPnP AV iOS", "transmitir música a la TV desde iPhone", "app servidor multimedia iPhone"]
readingTime: 9
---

{{< author-byline >}}

DLNA (también llamado UPnP AV) es el motor silencioso que hay detrás de la mayoría de las smart TVs. Es un lenguaje compartido que permite a una TV o a un reproductor multimedia encontrar una biblioteca multimedia en la misma red Wi-Fi y reproducir desde ella, sin nada que instalar en la TV. Si tu iPhone o iPad puede actuar como esa biblioteca, tus fotos, vídeos y música aparecen en la pantalla grande por su cuenta.

Esta guía muestra cómo convertir tu iPhone o iPad en un servidor multimedia DLNA/UPnP usando [Everdisk](/products/everdisk), y cómo abrir esa biblioteca desde una smart TV, una videoconsola, VLC, Kodi, un ordenador, un teléfono Android e incluso un segundo iPhone. Todo funciona por tu red Wi-Fi local, así que no se sube nada a ningún sitio.

## Qué necesitas

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Una TV, un reproductor o un ordenador en la **misma red Wi-Fi** que tu dispositivo.
- Las fotos, vídeos o música que quieras reproducir, ya en tu iPhone (en la app Fotos, la app Música o la carpeta Documentos de Everdisk).

## Configura el servidor DLNA en Everdisk

### Paso 1: Elige qué compartir

Abre Everdisk y ve a la pestaña **Compartir**. Toca **Qué compartir** y elige tu contenido:

- Activa **Permitir acceso a toda la biblioteca de fotos** para compartir todos los álbumes, o toca **Añadir fotos** para elegir algunas.
- Activa **Permitir acceso a toda la biblioteca de música** para compartir tus canciones, o toca **Añadir canciones** para una selección.
- Añade cualquier carpeta o archivo con **Añadir carpeta** y **Añadir archivo**. La carpeta Documentos de la propia app se comparte de forma predeterminada.

Necesitas tener al menos un elemento seleccionado antes de poder empezar a compartir.

### Paso 2: Activa TV y centro multimedia (DLNA)

Ve a **Ajustes**, luego **Compartir** y luego **Conexiones**. Asegúrate de que **TV y centro multimedia** esté activado. Está activado de forma predeterminada y lleva la etiqueta DLNA. Este es el servidor que buscan las TVs y los reproductores.

### Paso 3: Empieza a compartir

De vuelta en la pestaña **Compartir**, toca el botón grande **Iniciar**. Tu dispositivo ya es un servidor multimedia en tu Wi-Fi. Aparece ante los demás dispositivos con su nombre amistoso, el que se muestra como nombre de tu dispositivo en la app (algo como "Speedy-Hare" hasta que lo cambies).

La transmisión DLNA siempre está abierta, así que no hay contraseña que introducir en la TV. Mantén Everdisk abierto en pantalla mientras miras, porque iOS pausa las apps que se envían por completo a segundo plano.

## Reproduce en una smart TV

Este es el caso más habitual, y normalmente lleva unos treinta segundos.

1. Pon la TV en la **misma red Wi-Fi** que tu iPhone.
2. Abre el reproductor multimedia integrado de la TV. El nombre depende de la marca: **Media Player**, **Gallery**, **SmartShare** (LG), **AllShare** o **SmartThings** (Samsung), **Content Share** o **SimplyShare**.
3. Busca la lista de servidores multimedia o fuentes. Tu dispositivo aparece ahí por su nombre.
4. Selecciónalo, entra en tus fotos, vídeos o música y pulsa reproducir.

Las miniaturas de vista previa aparecen automáticamente, así que puedes encontrar el álbum de vacaciones o la película adecuados sin adivinar.

### Qué TVs funcionan

La mayoría de las TVs de **Samsung, LG, Sony BRAVIA, Panasonic (con firmware VIERA), Philips y Hisense** tienen DLNA integrado y funcionan de inmediato. **Las videoconsolas PlayStation y Xbox y la mayoría de los receptores AV** también.

Algunas plataformas lo dejan fuera: **las TVs Roku, Amazon Fire TV, Vizio SmartCast y Google TV a secas** sin una app multimedia del fabricante. Si tu TV es una de estas y no encuentra tu dispositivo, esa suele ser la razón. En esas TVs, instala una app de reproductor DLNA como VLC o Kodi, o accede a tus archivos a través de un navegador web con la [guía de configuración de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/).

Algunas marcas mantuvieron DLNA funcionando incluso después de quitar el logotipo oficial de DLNA, así que si parece que falta, busca uno de los nombres de reproductor multimedia de arriba.

## Reproduce en VLC o Kodi en Windows, Mac y Linux

VLC y Kodi son gratuitos, funcionan en todos los sistemas de escritorio y hablan bien DLNA. Son la forma fiable de abrir tu biblioteca de Everdisk en un ordenador.

**VLC (Windows, Mac, Linux):**

1. Abre VLC.
2. Muestra la lista de reproducción (en Windows y Linux pulsa **Ctrl+L**, en Mac abre la **Playlist** desde el menú Ver).
3. En la barra lateral, abre **Universal Plug'n'Play** dentro de Red local.
4. Tu dispositivo aparece en la lista. Entra en él y elige un archivo.

**Kodi (Windows, Mac, Linux):**

1. Ve a **Vídeos**, **Música** o **Imágenes**, luego **Archivos** y luego **Añadir origen** (o **Examinar**).
2. Elige **Dispositivos UPnP**.
3. Selecciona tu dispositivo y explora tu biblioteca.

En Windows también puedes abrir **Windows Media Player**, desplegar **Otras bibliotecas** en la barra lateral, y tu dispositivo aparece ahí.

## Reproduce en Android

Los teléfonos y tablets Android no tienen un explorador DLNA del sistema, así que usa una app:

- **VLC para Android**: abre el menú lateral, toca **Red local** y tu dispositivo aparece bajo los servidores UPnP.
- **BubbleUPnP** o una app UPnP similar: tu dispositivo aparece en la lista de servidores, y estas apps también pueden enviar la reproducción a una TV.

## Reproduce en otro iPhone o iPad

Dos dispositivos, una sola biblioteca. Supongamos que las fotos están en tu iPhone y quieres verlas en tu iPad.

- La ruta más sencilla es la propia pestaña **Dispositivos** de Everdisk en el segundo dispositivo. Funciona como cliente DLNA además de como servidor. Abre Everdisk en el iPad, ve a **Dispositivos** y tu iPhone aparece bajo **Dispositivos disponibles**. Tócalo para explorar y reproducir.
- Cualquier app de reproductor DLNA para iOS también funciona, como VLC o un explorador UPnP. Abre su vista de red local y elige tu iPhone.

## Reproduce en una videoconsola

- **PlayStation 5 y 4**: abre la app **Media** (Galería multimedia) y tu dispositivo aparece como un servidor multimedia que puedes explorar.
- **Xbox**: usa una app de reproductor multimedia compatible con DLNA y luego elige tu dispositivo en la lista de servidores.

## Si tu dispositivo no aparece en la lista

Algunos reproductores te permiten añadir un servidor multimedia por dirección en lugar de esperar a que se detecte. En la pantalla **Compartir** de Everdisk, la tarjeta DLNA muestra una dirección de descripción del dispositivo que termina en `/device-desc.xml`. Introduce esa dirección en el campo de añadir servidor del reproductor.

Si aun así no aparece, comprueba tres cosas: que ambos dispositivos están en la misma Wi-Fi (no en una red de invitados que bloquee el tráfico entre dispositivos), que Everdisk está abierto y la compartición iniciada, y que **TV y centro multimedia** está activado en Ajustes.

## Si un vídeo no se reproduce

DLNA entrega el archivo a la TV tal cual, y la TV tiene que poder decodificarlo. Si un clip se niega a reproducirse, es probable que esa TV no admita su formato. Dos soluciones:

- Abre **Ajustes**, luego **Compartir** y luego **Vídeos**, y baja la **Calidad**. Everdisk convierte entonces el vídeo a un formato más compatible mientras se transmite. (La conversión es una función Premium).
- O abre el mismo archivo en un navegador web usando el enlace de navegador de Everdisk, que es más tolerante con los formatos.

## Formas reales en que la gente usa esto

- **Noche de cine en familia.** Los vídeos grabados con tu teléfono se reproducen en la TV del salón sin cable ni Apple TV.
- **Fotos de vacaciones en la pantalla grande.** Abre tu biblioteca de Fotos en la TV y pasa las del viaje con todos en la sala.
- **Música de fondo en una fiesta.** Apunta un altavoz DLNA o un receptor AV a tu biblioteca de Música y deja que suene.
- **Ver en la TV de un hotel** que tenga reproductor multimedia, una vez que ambos dispositivos estén en la Wi-Fi de la habitación.

## Algunos consejos

- Mantén Everdisk abierto mientras transmites. Si bloqueas el teléfono mucho tiempo, iOS puede pausar la app y la reproducción se detiene.
- Conecta el teléfono a la corriente para sesiones de película largas.
- Para la transmisión más rápida, mantén **Formato** y **Calidad** en **Original** en Ajustes, y bájalos solo si una TV concreta tiene problemas con un archivo.
- DLNA es solo transmisión. Nadie del lado de la TV puede cambiar ni eliminar tus archivos. Para transferencia de archivos en ambos sentidos, usa el servidor [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/), [WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) o [FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) en su lugar.

## Preguntas frecuentes

{{% details title="¿Cuál es la diferencia entre DLNA y UPnP?" closed="true" %}}
Están muy relacionados. UPnP es el estándar de red subyacente, y DLNA es el perfil multimedia construido encima que las TVs y los reproductores usan para compartir y reproducir fotos, vídeos y música. En el uso diario las palabras son intercambiables. Cuando activas TV y centro multimedia en Everdisk, tu dispositivo se convierte en un servidor multimedia DLNA/UPnP que cualquier cliente DLNA puede explorar.
{{% /details %}}

{{% details title="¿Necesito instalar algo en mi TV?" closed="true" %}}
No. Si tu TV admite DLNA, ya tiene un reproductor multimedia que puede encontrar tu dispositivo en la Wi-Fi. Solo instalas Everdisk en el iPhone o iPad que contiene el contenido. Si tu TV no admite DLNA, instala un reproductor como VLC o Kodi en un dispositivo conectado a ella.
{{% /details %}}

{{% details title="¿Por qué mi iPhone no aparece en la TV?" closed="true" %}}
Comprueba que ambos dispositivos están en la misma red Wi-Fi. Las redes de invitados y algunas redes de oficina o de hotel impiden que los dispositivos se vean entre sí, lo que detiene DLNA. Luego confirma que Everdisk está abierto con la compartición iniciada, y que TV y centro multimedia está activado en Ajustes, Compartir, Conexiones. Si la TV aún no lo encuentra, añade el servidor a mano usando la dirección de descripción del dispositivo que termina en /device-desc.xml.
{{% /details %}}

{{% details title="¿La transmisión DLNA necesita contraseña?" closed="true" %}}
No. DLNA siempre está abierto a cualquiera de la misma Wi-Fi mientras esté activado, por eso no hay inicio de sesión en el lado de la TV. Eso está bien en una red doméstica de confianza. En una red en la que no confíes, desactiva TV y centro multimedia cuando termines, o usa el servidor SMB con cifrado en su lugar.
{{% /details %}}

{{% details title="¿Puedo transmitir a un Chromecast o Roku?" closed="true" %}}
Chromecast y Roku no actúan como reproductores DLNA de fábrica, así que no encontrarán tu dispositivo directamente. La solución es instalar una app DLNA que pueda hacer cast, como VLC o BubbleUPnP en un teléfono, y enviar la reproducción al Chromecast o Roku desde ahí. En la mayoría de las demás smart TVs, DLNA funciona sin nada de esto.
{{% /details %}}

{{% details title="Un vídeo se reproduce sin sonido o no se abre. ¿Qué puedo hacer?" closed="true" %}}
Es un formato que la TV no puede decodificar. Abre Ajustes, Compartir, Vídeos en Everdisk y baja la Calidad para que la app convierta el vídeo a un formato más compatible mientras se transmite. También puedes abrir el mismo archivo a través del enlace de navegador, que admite más formatos.
{{% /details %}}

{{% details title="¿Puedo transmitir música, no solo vídeo?" closed="true" %}}
Sí. Activa Permitir acceso a toda la biblioteca de música, o añade pistas concretas, y luego empieza a compartir. Tus canciones aparecen en cualquier altavoz DLNA, receptor AV o TV, con carátula y detalles de la pista. La música siempre se comparte en su calidad original.
{{% /details %}}

{{% details title="¿La app tiene que quedarse abierta mientras miro?" closed="true" %}}
Sí. Tu iPhone actúa como servidor, e iOS pausa las apps que se envían por completo a segundo plano durante mucho tiempo. Mantén Everdisk en pantalla mientras transmites, y conéctalo a la corriente para sesiones largas.
{{% /details %}}

{{% details title="¿Cómo transmito de un iPhone a otro iPad?" closed="true" %}}
Empieza a compartir en el iPhone, luego abre Everdisk en el iPad y ve a la pestaña Dispositivos. El iPhone aparece bajo Dispositivos disponibles como servidor multimedia. Tócalo para explorar y reproducir. Everdisk funciona como cliente DLNA y como servidor, así que no necesitas otra app.
{{% /details %}}

{{% details title="¿Everdisk es gratis?" closed="true" %}}
Sí, Everdisk se descarga gratis y el servidor multimedia DLNA está incluido. Una compra opcional única Premium de por vida añade extras como la conversión de fotos y vídeos para TVs antiguas, puertos personalizados y más. Puedes configurar y usar la transmisión DLNA sin pagar.
{{% /details %}}

¿Listo para probarlo? [Descarga Everdisk en la App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) y transmite tu primer álbum a la TV en un par de minutos. ¿Preguntas o comentarios? Escríbenos a **support@everappz.com**.
