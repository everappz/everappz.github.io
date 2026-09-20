---
title: "Cómo configurar un servidor WebDAV en iPhone y iPad para acceder a archivos y compartirlos"
description: "Convierte tu iPhone o iPad en un servidor WebDAV con Everdisk y móntalo como una unidad de red en el Finder del Mac, el Explorador de archivos de Windows, Linux, Android u otro iPhone por Wi-Fi. Configuración completa, la dirección y el puerto WebDAV, y conexión paso a paso para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "webdav", "unidad de red", "compartir archivos", "iphone", "ipad", "mac", "windows", "linux", "wifi"]
keywords: ["servidor WebDAV iPhone", "servidor WebDAV iPad", "cómo configurar WebDAV en iPhone", "montar iPhone como unidad de red", "conectar iPhone WebDAV Mac Finder", "WebDAV Explorador de archivos Windows iPhone", "iphone unidad de red Windows", "WebDAV Linux iPhone", "acceder a archivos del iPhone desde el ordenador", "webdav iphone a iphone", "compartir archivos iPhone WebDAV", "asignar unidad de red iphone", "transferir archivos iphone webdav", "dirección puerto webdav iphone"]
readingTime: 9
---

{{< author-byline >}}

WebDAV convierte una carpeta en una unidad de red que un ordenador puede abrir en su gestor de archivos normal. Funciona sobre el mismo protocolo web que usa tu navegador, por lo que viaja bien entre Mac, Windows y Linux sin controladores especiales. Con [Everdisk](/products/everdisk) puedes ejecutar un servidor WebDAV en tu iPhone o iPad, de modo que el teléfono aparece como un disco que puedes explorar, del que copiar y al que copiar desde casi cualquier ordenador.

WebDAV es la mejor elección cuando Windows entra en juego, porque el Explorador de archivos de Windows se conecta a él de forma limpia. Esta guía cubre la configuración y cómo conectarte desde un Mac, Windows, Linux, Android y un segundo iPhone.

## Qué necesitas

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Un ordenador u otro dispositivo en la **misma red Wi-Fi**.
- Los archivos que quieras compartir, en la carpeta Documentos de Everdisk o en carpetas que añadas.

## Configura el servidor WebDAV en Everdisk

### Paso 1: Elige qué compartir y define el acceso

Abre Everdisk, ve a la pestaña **Compartir** y toca **Qué compartir**. La carpeta Documentos se comparte de forma predeterminada. Añade más con **Añadir carpeta** y **Añadir archivo**.

Abre **Ajustes**, luego **Compartir** y luego **Acceso**. Activa **Edición de archivos** si quieres que los ordenadores conectados puedan copiar archivos en tu teléfono y renombrarlos o eliminarlos, o desactívala para un disco de solo lectura. Establece aquí un **Usuario** y una **Contraseña** si quieres un inicio de sesión, o déjalos vacíos para el acceso de invitado.

### Paso 2: Activa el servidor WebDAV

Ve a **Ajustes**, luego **Compartir** y luego **Conexiones**, y activa **Ordenador**. Ese es el servidor WebDAV (lleva la etiqueta WebDAV).

### Paso 3: Empieza a compartir y anota la dirección

Vuelve a la pestaña **Compartir** y toca **Iniciar**. La sección **Cómo conectarse** muestra la dirección WebDAV. Tiene este aspecto:

```
http://192.168.1.20:8080
```

El número después de los dos puntos es el **puerto**, que es **8080** de forma predeterminada. La primera parte es la dirección de tu iPhone en la Wi-Fi, así que la tuya será distinta. Mantén Everdisk abierto en pantalla mientras haya un dispositivo conectado.

## Conéctate desde un Mac

1. Abre **Finder**, elige **Ir**, luego **Conectarse al servidor** (o pulsa **Command y K**).
2. Escribe la dirección WebDAV que se muestra en Everdisk, por ejemplo `http://192.168.1.20:8080`.
3. Haz clic en **Conectar**, luego elige **Invitado** o introduce tu **Usuario** y **Contraseña**.

Tu iPhone se abre en una ventana del Finder y se comporta como una carpeta normal. Copia archivos en cualquier dirección si Edición de archivos está activada.

## Conéctate desde Windows

Windows tiene un cliente WebDAV integrado, así que esto funciona desde el Explorador de archivos.

1. Abre el **Explorador de archivos**, haz clic derecho en **Este equipo** en la barra lateral y elige **Agregar una ubicación de red** (también puedes usar **Conectar a unidad de red**).
2. Cuando te pida la dirección, escribe la misma dirección WebDAV de Everdisk, por ejemplo `http://192.168.1.20:8080`, y luego haz clic en **Siguiente**.
3. Introduce tu **Usuario** y **Contraseña** si estableciste uno.

El dispositivo aparece entonces bajo Este equipo como una ubicación de red que puedes abrir y de la que copiar archivos. Si Windows se niega a conectarse la primera vez, asegúrate de que el servicio **WebClient** está en ejecución (busca Servicios en el menú Inicio, encuentra WebClient y ponlo a iniciarse), y luego inténtalo de nuevo.

## Conéctate desde Linux

1. Abre tu gestor de archivos y elige **Conectarse al servidor** u **Otras ubicaciones**.
2. Introduce la dirección con un prefijo WebDAV, por ejemplo `dav://192.168.1.20:8080` (usa `davs://` solo si configuraste TLS).
3. Conéctate como invitado o introduce tu inicio de sesión.

## Conéctate desde Android

Android no tiene un explorador WebDAV del sistema, así que usa un gestor de archivos compatible:

1. Instala una app como **Solid Explorer** o **CX File Explorer**.
2. Añade una nueva conexión **WebDAV**.
3. Introduce el host y el **puerto 8080**, elige el esquema `http` y añade tu inicio de sesión si estableciste uno.

## Conéctate desde otro iPhone o iPad

La app Archivos de iOS no incluye un cliente WebDAV, así que usa una de estas opciones:

- **La propia pestaña Dispositivos de Everdisk.** En el segundo dispositivo, abre Everdisk, ve a **Dispositivos**, toca **Nueva conexión**, elige **WebDAV** e introduce la dirección, por ejemplo `http://192.168.1.20:8080`. Es la ruta más sencilla y no necesita nada más.
- **Una app WebDAV** como Documents de Readdle, que puede añadir una conexión WebDAV con la misma dirección e inicio de sesión.

## ¿Prefieres un enlace rápido en lugar de una unidad?

Si solo necesitas coger un archivo rápido y no quieres montar una unidad, activa la conexión **Navegador** en Ajustes, Compartir, Conexiones. Everdisk te da entonces una dirección web que puedes abrir en cualquier navegador de cualquier dispositivo para explorar y descargar tus archivos. Es la forma más rápida de entregar un archivo a un PC con Windows, un Chromebook o el teléfono de un amigo.

## Solo lectura o lectura y escritura

El interruptor **Edición de archivos** en Ajustes, Compartir, Acceso decide esto. Activado significa que los ordenadores conectados pueden subir, renombrar y eliminar. Desactivado significa que el disco es de solo lectura, así que los demás pueden ver y copiar tus archivos, pero no cambiarlos.

## Formas reales en que la gente usa esto

- **Copiar archivos a tu iPhone desde un PC con Windows** asignándolo como ubicación de red y arrastrándolos.
- **Descargar fotos y documentos a un portátil** usando el gestor de archivos que ya conoces, sin cable y sin iTunes.
- **Editar un documento en su sitio** desde tu Mac, abriéndolo directamente desde el teléfono y guardándolo de vuelta.
- **Mover una carpeta entre un iPhone y un iPad** usando la pestaña Dispositivos de Everdisk en el dispositivo receptor.

## Algunos consejos

- Mantén Everdisk abierto mientras haya un dispositivo conectado. Bloquear el teléfono mucho tiempo puede pausar la app.
- En Windows, si la conexión falla, inicia el servicio WebClient y prueba la dirección de nuevo.
- WebDAV y SMB se montan ambos como unidades de red. Usa WebDAV cuando Windows esté involucrado, y [SMB](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) cuando quieras la velocidad del Finder y cifrado.
- Para las transferencias más rápidas, mantén la calidad de fotos y vídeos en Original en Ajustes.

## Preguntas frecuentes

{{% details title="¿Cuál es la dirección y el puerto WebDAV de mi iPhone?" closed="true" %}}
Después de empezar a compartir, Everdisk muestra la dirección en la pantalla Compartir. Tiene el aspecto http://192.168.1.20:8080. El 8080 es el puerto que Everdisk usa para WebDAV, y la primera parte es la dirección de tu iPhone en la Wi-Fi, así que la tuya será distinta.
{{% /details %}}

{{% details title="¿Cómo me conecto a mi WebDAV del iPhone desde Windows?" closed="true" %}}
Abre el Explorador de archivos, haz clic derecho en Este equipo y elige Agregar una ubicación de red o Conectar a unidad de red. Introduce la dirección WebDAV de Everdisk, por ejemplo http://192.168.1.20:8080, y luego introduce tu inicio de sesión si estableciste uno. Si Windows no se conecta, asegúrate de que el servicio WebClient está en ejecución (busca Servicios, encuentra WebClient, inícialo) e inténtalo de nuevo.
{{% /details %}}

{{% details title="¿Puedo usar WebDAV entre dos iPhones?" closed="true" %}}
Sí, pero la app Archivos de iOS no tiene cliente WebDAV, así que usa Everdisk en el segundo dispositivo. Abre la pestaña Dispositivos, toca Nueva conexión, elige WebDAV e introduce la dirección que se muestra en el primer teléfono. Una app WebDAV como Documents de Readdle también funciona.
{{% /details %}}

{{% details title="¿WebDAV necesita contraseña?" closed="true" %}}
No, el inicio de sesión es opcional. Deja el Usuario y la Contraseña vacíos en Ajustes, Compartir, Acceso para el acceso de invitado, o establécelos si quieres que las conexiones inicien sesión.
{{% /details %}}

{{% details title="¿Otras personas pueden cambiar mis archivos por WebDAV?" closed="true" %}}
Solo si lo permites. El interruptor Edición de archivos en Ajustes, Compartir, Acceso controla esto. Activado permite que los dispositivos conectados suban, renombren y eliminen. Desactivado hace que el disco sea de solo lectura, así que los demás pueden ver y copiar, pero no cambiar nada.
{{% /details %}}

{{% details title="¿WebDAV o SMB, cuál es la diferencia?" closed="true" %}}
Ambos montan tu iPhone como una unidad de red. WebDAV funciona sobre el protocolo web y se conecta de forma limpia desde el Explorador de archivos de Windows, que es su punto fuerte principal. SMB es la compartición de archivos nativa en Mac, Linux y dispositivos NAS, suele ser más rápida en un Mac, y es la única conexión de Everdisk que puede cifrar las transferencias. Everdisk puede ejecutar ambas a la vez.
{{% /details %}}

{{% details title="¿Por qué se desconecta mi unidad WebDAV?" closed="true" %}}
Tu iPhone es el servidor, e iOS pausa las apps que permanecen demasiado tiempo en segundo plano. Mantén Everdisk abierto en pantalla mientras haya un dispositivo conectado, y conéctalo a la corriente para transferencias largas. Confirma también que ambos dispositivos siguen en la misma Wi-Fi.
{{% /details %}}

{{% details title="¿Puedo conectarme por WebDAV sin Wi-Fi?" closed="true" %}}
Sí, si conectas tu iPhone a un Mac con un cable. Everdisk muestra entonces una dirección de conexión por cable adicional que el Mac conectado puede abrir en el Finder, y que funciona incluso sin nada de Wi-Fi. Por cable, solo ese Mac puede acceder al dispositivo.
{{% /details %}}

{{% details title="¿Everdisk es gratis?" closed="true" %}}
Sí, Everdisk se descarga gratis y el servidor WebDAV está incluido. Una compra opcional única Premium añade extras como puertos personalizados y conversión de fotos y vídeos. Puedes configurar WebDAV y compartir archivos sin pagar.
{{% /details %}}

¿Listo para probarlo? [Descarga Everdisk en la App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) y monta tu iPhone como unidad en un par de minutos. ¿Preguntas o comentarios? Escríbenos a **support@everappz.com**.
