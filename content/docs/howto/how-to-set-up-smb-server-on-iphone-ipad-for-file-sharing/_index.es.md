---
title: "Cómo configurar un servidor SMB en iPhone y iPad para compartir archivos"
description: "Convierte tu iPhone o iPad en un servidor de archivos SMB con Everdisk y ábrelo como una unidad de red desde un Mac, otro iPhone, Linux o Android por Wi-Fi. Configuración completa, la dirección y el puerto smb, cifrado SMB3 opcional y conexión paso a paso para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "smb", "compartir archivos", "unidad de red", "iphone", "ipad", "mac", "finder", "cifrado", "wifi"]
keywords: ["servidor SMB iPhone", "servidor SMB iPad", "cómo configurar SMB en iPhone", "compartir SMB iPhone", "conectar iPhone SMB Mac Finder", "smb iphone a iphone", "app Archivos iOS conectar a servidor SMB", "compartir archivos iPhone SMB", "iphone unidad de red Finder", "cifrado SMB3 iOS", "compartir smb iPhone Android", "conectar a SMB desde Linux", "iphone como unidad de red", "compartir archivos entre iphones wifi", "asignar iphone como unidad de red"]
readingTime: 10
---

{{< author-byline >}}

SMB es la compartición de archivos integrada en macOS, Windows y Linux, y en casi todas las unidades de red (NAS). Cuando te conectas a una carpeta compartida de otro ordenador y se abre como un disco normal en Finder o el Explorador de archivos, eso es SMB haciendo el trabajo. Con [Everdisk](/products/everdisk) puedes poner un recurso compartido SMB en tu iPhone o iPad, de modo que el propio teléfono aparece como una unidad de red que otros dispositivos exploran, de la que copian y a la que copian.

Esta es la opción a la que recurrir cuando quieres que tu iPhone se comporte como un disco de verdad, no como una página web. Es rápida, arrastra y suelta en ambos sentidos, y es el único tipo de conexión de Everdisk que puede cifrar cada transferencia. Esta guía cubre la configuración y cómo conectarte desde un Mac, otro iPhone o iPad, Linux, Android y Windows.

## Qué necesitas

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Otro dispositivo en la **misma red Wi-Fi**.
- Los archivos que quieras compartir, en la carpeta Documentos de Everdisk o en carpetas que añadas.

## Configura el servidor SMB en Everdisk

### Paso 1: Elige qué compartir y quién puede escribir

Abre Everdisk, ve a la pestaña **Compartir** y toca **Qué compartir**. La carpeta Documentos se comparte de forma predeterminada. Añade más con **Añadir carpeta** y **Añadir archivo**, y activa tu biblioteca de Fotos o de Música si también quieres que estén disponibles.

Decide si los demás dispositivos solo pueden leer tus archivos o también cambiarlos. Abre **Ajustes**, luego **Compartir** y luego **Acceso**, y configura **Edición de archivos**. Con ella activada, los dispositivos conectados pueden copiar archivos en tu teléfono y renombrarlos o eliminarlos. Con ella desactivada, el recurso compartido es de solo lectura.

Si quieres un inicio de sesión, establece un **Usuario** y una **Contraseña** en la misma pantalla de Acceso. Deja ambos vacíos para permitir el acceso de invitado.

### Paso 2: Activa el servidor SMB

Ve a **Ajustes**, luego **Compartir** y luego **Conexiones**, y activa **Equipo (avanzado)**. Ese es el servidor SMB (lleva la etiqueta SMB).

### Paso 3: Empieza a compartir y anota la dirección

Vuelve a la pestaña **Compartir** y toca **Iniciar**. La sección **Cómo conectarse** muestra ahora la dirección SMB. Tiene este aspecto:

```
smb://192.168.1.20:4455/Share
```

Tres cosas que hay que saber sobre esa dirección:

- El número después de los dos puntos es el **puerto**. Everdisk usa **4455** de forma predeterminada.
- El recurso compartido se llama **Share**.
- La primera parte es la dirección de tu iPhone en la Wi-Fi, así que será distinta en tu red.

Mantén Everdisk abierto mientras haya dispositivos conectados, porque iOS pausa las apps que permanecen demasiado tiempo en segundo plano.

## Conéctate desde un Mac

Este es el caso más fluido, porque macOS habla SMB de forma nativa.

La forma más rápida: abre **Finder** y mira en la barra lateral, en **Ubicaciones** o **Red**. Everdisk se anuncia en la Wi-Fi, así que tu iPhone suele aparecer ahí por su cuenta. Haz clic en él, luego en **Conectar como** y elige **Invitado**, o introduce tu inicio de sesión.

Para conectarte a mano:

1. En Finder, elige **Ir**, luego **Conectarse al servidor** (o pulsa **Command y K**).
2. Escribe la dirección SMB que se muestra en Everdisk, por ejemplo `smb://192.168.1.20:4455/Share`.
3. Haz clic en **Conectar**, luego elige **Invitado** o introduce tu **Usuario** y **Contraseña**.

Tu iPhone se abre en una ventana del Finder. Copia archivos hacia dentro o hacia fuera arrastrándolos, igual que con cualquier otro disco (si Edición de archivos está activada).

## Conéctate desde otro iPhone o iPad

iOS y iPadOS pueden abrir recursos compartidos SMB en la app **Archivos** integrada, lo que hace que las transferencias de teléfono a teléfono sean limpias y rápidas.

En el segundo dispositivo:

1. Abre la app **Archivos**.
2. Toca el botón **más** (los tres puntos, arriba a la derecha en el iPhone) y elige **Conectarse al servidor**.
3. Introduce la dirección SMB de Everdisk, por ejemplo `smb://192.168.1.20:4455/Share`.
4. Elige **Invitado**, o **Usuario registrado** e introduce tu inicio de sesión.
5. El recurso compartido aparece bajo Ubicaciones en Archivos. Explora y copia en cualquier dirección.

También puedes usar la propia pestaña **Dispositivos** de Everdisk en el segundo dispositivo, que incluye un cliente SMB. Abre Everdisk, ve a **Dispositivos**, toca **Nueva conexión**, elige **SMB** e introduce la dirección.

## Conéctate desde Linux

1. Abre tu gestor de archivos (Files/Nautilus en GNOME, Dolphin en KDE).
2. Elige **Otras ubicaciones** o **Conectarse al servidor**.
3. Introduce la dirección, por ejemplo `smb://192.168.1.20:4455/Share`.
4. Conéctate como invitado, o introduce tu inicio de sesión.

Desde un terminal también puedes ejecutar `smbclient //192.168.1.20/Share -p 4455` e introducir tu inicio de sesión cuando te lo pida.

## Conéctate desde Android

Android no tiene un explorador SMB del sistema, así que usa un gestor de archivos compatible con SMB:

1. Instala una app como **CX File Explorer**, **Solid Explorer** o **X-plore File Manager**.
2. Añade una nueva conexión **SMB** o **LAN**.
3. Introduce el host (la dirección Wi-Fi de tu iPhone), fija el **puerto en 4455** y el nombre del recurso compartido **Share**.
4. Conéctate como invitado o con tu inicio de sesión, y luego explora y copia.

## Conéctate desde Windows

Windows puede leer recursos compartidos SMB, con una salvedad que conviene saber de entrada. El Explorador de archivos integrado solo habla con SMB en el puerto estándar y no te deja escribir un puerto personalizado en la ruta, y Everdisk usa el puerto 4455. Así que la ruta simple de **Conectar a unidad de red** a menudo no llegará a él.

Tienes dos buenas opciones en Windows:

- Usa un gestor de archivos o un cliente SMB que te permita fijar un puerto personalizado, y apúntalo a la dirección de tu iPhone con el puerto **4455** y el nombre del recurso compartido **Share**.
- O conéctate desde Windows usando uno de los otros servidores de Everdisk en su lugar. La [configuración de WebDAV](/docs/howto/how-to-set-up-webdav-server-on-iphone-ipad-for-file-access-and-sharing/) y la [configuración de FTP](/docs/howto/how-to-set-up-ftp-server-on-iphone-ipad-for-file-transfers/) funcionan bien desde el Explorador de archivos de Windows, y el enlace de navegador funciona en cualquier navegador.

Si aun así quieres probar Conectar a unidad de red: abre el **Explorador de archivos**, haz clic derecho en **Este equipo**, elige **Conectar a unidad de red** e introduce el host y el nombre del recurso compartido que se muestran en Everdisk. Si no puede conectarse, es la limitación de puerto de antes, así que cambia a WebDAV o FTP.

## Activa el cifrado para una Wi-Fi de poca confianza

SMB es la única conexión de Everdisk que puede cifrar cada transferencia, lo que importa en una Wi-Fi que no controlas del todo, como la de una cafetería o la red de una oficina.

1. En **Ajustes**, **Compartir**, **Acceso**, establece un **Usuario** y una **Contraseña**. Las conexiones cifradas no pueden ser anónimas, así que este paso es obligatorio.
2. En **Ajustes**, **Compartir**, activa **Requerir cifrado SMB**.
3. Detén y vuelve a iniciar la compartición para que el cambio surta efecto.

Cada transferencia SMB queda entonces protegida con **cifrado SMB3 (AES)**. El dispositivo que se conecta necesita admitir SMB3, cosa que hacen tanto el Finder de un Mac moderno como Windows 10 o posterior. El cifrado SMB forma parte de la compra única Premium.

## Solo lectura o lectura y escritura

El interruptor **Edición de archivos** en Ajustes, Compartir, Acceso controla esto para todos los servidores, incluido SMB. Actívalo y los dispositivos conectados podrán subir, renombrar y eliminar. Desactívalo y solo podrán explorar y copiar archivos desde tu teléfono. Elige solo lectura cuando entregas archivos a alguien y no quieres que cambie nada.

## Formas reales en que la gente usa esto

- **Mover una carpeta grande a tu iPhone desde un Mac** arrastrándola a la ventana del Finder, más rápido que una subida web.
- **Sacar un día de fotos y vídeos de tu teléfono** a un portátil sin iTunes ni cable.
- **Enviar archivos entre dos iPhones** a través de la app Archivos, sin una tercera app en ninguno de los dos lados.
- **Trabajar con un archivo en su sitio**, abriendo un documento directamente desde el teléfono en una app de tu Mac y guardándolo de vuelta.

## Algunos consejos

- Mantén Everdisk abierto mientras haya un dispositivo conectado. Bloquear el teléfono mucho tiempo puede pausar la app y cortar la conexión.
- Si un Mac no ve el teléfono en la barra lateral del Finder, conéctate a mano con Conectarse al servidor y la dirección smb completa.
- Para la mejor velocidad en transferencias grandes, mantén la calidad de fotos y vídeos en Original en Ajustes.
- En una red de poca confianza, activa Requerir cifrado SMB y desactiva los demás servidores mientras trabajas.

## Preguntas frecuentes

{{% details title="¿Cuál es la dirección y el puerto SMB de mi iPhone?" closed="true" %}}
Después de empezar a compartir, Everdisk muestra la dirección en la pantalla Compartir. Tiene el aspecto smb://192.168.1.20:4455/Share. El 4455 es el puerto que Everdisk usa para SMB, y Share es el nombre de la carpeta compartida. La primera parte es la dirección de tu iPhone en la Wi-Fi, así que la tuya será distinta.
{{% /details %}}

{{% details title="¿Puedo conectarme a mi recurso compartido SMB del iPhone desde Windows?" closed="true" %}}
El Explorador de archivos de Windows solo se conecta a SMB en el puerto estándar y no acepta un puerto personalizado en la ruta, mientras que Everdisk usa el puerto 4455. Así que la ruta simple de Conectar a unidad de red a menudo no llegará a él. Usa un gestor de archivos que te permita fijar un puerto personalizado, o conéctate desde Windows con WebDAV, FTP o el enlace de navegador en su lugar. Todas esas opciones funcionan desde Windows sin problemas de puerto.
{{% /details %}}

{{% details title="¿Cómo comparto archivos entre dos iPhones con SMB?" closed="true" %}}
Inicia el servidor SMB en el primer iPhone en Everdisk. En el segundo iPhone, abre la app Archivos, toca el botón más, elige Conectarse al servidor e introduce la dirección smb que se muestra en Everdisk (por ejemplo smb://192.168.1.20:4455/Share). Conéctate como Invitado o con tu inicio de sesión, y el recurso compartido aparece en Archivos. También puedes usar la propia pestaña Dispositivos de Everdisk en el segundo teléfono.
{{% /details %}}

{{% details title="¿Mi iPhone aparece automáticamente en la barra lateral del Finder del Mac?" closed="true" %}}
Normalmente sí. Everdisk anuncia el recurso compartido SMB en tu Wi-Fi, así que tu iPhone suele aparecer bajo Ubicaciones o Red en la barra lateral del Finder. Haz clic en él y elige Conectar como, luego Invitado o tu inicio de sesión. Si no aparece, conéctate a mano con Ir, Conectarse al servidor y la dirección smb completa.
{{% /details %}}

{{% details title="¿Necesito una contraseña para usar SMB?" closed="true" %}}
No, el inicio de sesión es opcional. Deja el Usuario y la Contraseña vacíos en Ajustes, Compartir, Acceso para permitir el acceso de invitado. Establécelos si quieres que las conexiones inicien sesión. Un usuario y una contraseña solo son obligatorios si activas Requerir cifrado SMB, porque las conexiones cifradas no pueden ser anónimas.
{{% /details %}}

{{% details title="¿La conexión SMB está cifrada?" closed="true" %}}
Puede estarlo. SMB es la única conexión de Everdisk que admite cifrado. Establece un usuario y una contraseña, y luego activa Requerir cifrado SMB en Ajustes, Compartir. Cada transferencia queda entonces protegida con SMB3 (AES). El otro dispositivo necesita admitir SMB3, cosa que hacen los Mac modernos y Windows 10 o posterior. El cifrado es una función Premium.
{{% /details %}}

{{% details title="¿La gente puede cambiar o eliminar mis archivos por SMB?" closed="true" %}}
Solo si lo permites. El interruptor Edición de archivos en Ajustes, Compartir, Acceso controla esto. Con él activado, los dispositivos conectados pueden subir, renombrar y eliminar. Con él desactivado, el recurso compartido es de solo lectura y los demás pueden explorar y copiar archivos desde tu teléfono, pero no cambiar nada.
{{% /details %}}

{{% details title="¿Por qué se cayó mi conexión SMB?" closed="true" %}}
Tu iPhone es el servidor, e iOS pausa las apps que permanecen demasiado tiempo en segundo plano. Mantén Everdisk abierto en pantalla mientras haya un dispositivo conectado, y conecta el teléfono a la corriente durante las transferencias largas. Asegúrate también de que ambos dispositivos siguen en la misma Wi-Fi.
{{% /details %}}

{{% details title="SMB, WebDAV o FTP, ¿cuál debería usar?" closed="true" %}}
Usa SMB cuando quieras que el teléfono se comporte como una unidad de red de verdad en un Mac, otro iPhone, Linux o un NAS, y cuando quieras cifrado. Usa WebDAV cuando quieras una unidad de red que también funcione bien desde Windows. Usa FTP para la mayor compatibilidad con dispositivos y apps antiguos. Everdisk puede ejecutarlos todos a la vez, así que no te quedas atado a uno solo.
{{% /details %}}

{{% details title="¿Everdisk es gratis?" closed="true" %}}
Sí, Everdisk se descarga gratis y el servidor SMB está incluido. La compra opcional única Premium añade cifrado SMB, puertos personalizados y algunos otros extras. Puedes configurar SMB y compartir archivos sin pagar.
{{% /details %}}

¿Listo para probarlo? [Descarga Everdisk en la App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) y abre tu iPhone en el Finder en aproximadamente un minuto. ¿Preguntas o comentarios? Escríbenos a **support@everappz.com**.
