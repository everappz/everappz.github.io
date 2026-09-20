---
title: "Cómo configurar un servidor FTP en iPhone y iPad para transferir archivos"
description: "Convierte tu iPhone o iPad en un servidor FTP con Everdisk y transfiere archivos desde un Mac, un PC con Windows, Linux, Android, una app FTP como FileZilla u otro iPhone por Wi-Fi. Configuración completa, la dirección y el puerto ftp, acceso de invitado y conexión paso a paso para cada dispositivo."
date: 2026-09-19
tags: ["everdisk", "ftp", "transferencia de archivos", "filezilla", "cyberduck", "iphone", "ipad", "mac", "windows", "wifi"]
keywords: ["servidor FTP iPhone", "servidor FTP iPad", "cómo configurar FTP en iPhone", "app servidor ftp iphone", "conectar FileZilla al iPhone", "Cyberduck iPhone FTP", "transferir archivos iPhone FTP", "ftp iphone al ordenador", "ftp iphone a iphone", "conectar al FTP del iPhone desde Windows", "dirección puerto ftp iphone", "ftp anónimo iphone", "compartir archivos iphone ftp", "ftp iphone para cámara nas"]
readingTime: 9
---

{{< author-byline >}}

FTP es el viejo fiable de la transferencia de archivos. Lleva décadas en uso, y precisamente por eso es tan útil: casi todo lo que puede hablar con un servidor lo entiende. Cámaras, smart TVs, routers, unidades de red, herramientas de automatización y todas las apps FTP de escritorio hablan FTP. Con [Everdisk](/products/everdisk) puedes ejecutar un servidor FTP en tu iPhone o iPad, de modo que el teléfono se convierte en un lugar al que esos dispositivos y apps pueden conectarse para mover archivos.

Recurre a FTP cuando las otras opciones no encajan, por ejemplo con un dispositivo antiguo o una app que solo sabe conectarse por FTP. Esta guía cubre la configuración y cómo conectarte desde un Mac, Windows, una app FTP, Linux, Android y un segundo iPhone.

## Qué necesitas

- Un iPhone o iPad con [Everdisk](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) instalado.
- Un ordenador, una app o un dispositivo en la **misma red Wi-Fi**.
- Los archivos que quieras compartir, en la carpeta Documentos de Everdisk o en carpetas que añadas.

## Configura el servidor FTP en Everdisk

### Paso 1: Elige qué compartir y define el acceso

Abre Everdisk, ve a la pestaña **Compartir** y toca **Qué compartir**. La carpeta Documentos se comparte de forma predeterminada. Añade más con **Añadir carpeta** y **Añadir archivo**.

Abre **Ajustes**, luego **Compartir** y luego **Acceso**. Activa **Edición de archivos** si quieres que la gente pueda subir, renombrar y eliminar, o desactívala para permitir solo descargas. Establece un **Usuario** y una **Contraseña** si quieres un inicio de sesión, o déjalos vacíos para que cualquiera pueda conectarse como invitado.

### Paso 2: Activa el servidor FTP

Ve a **Ajustes**, luego **Compartir** y luego **Conexiones**, y activa **Otras apps y dispositivos**. Ese es el servidor FTP (lleva la etiqueta FTP).

### Paso 3: Empieza a compartir y anota la dirección

Vuelve a la pestaña **Compartir** y toca **Iniciar**. La sección **Cómo conectarse** muestra la dirección FTP. Tiene este aspecto:

```
ftp://192.168.1.20:2121
```

El número después de los dos puntos es el **puerto**, que es **2121** de forma predeterminada. La primera parte es la dirección de tu iPhone en la Wi-Fi, así que la tuya será distinta. Mantén Everdisk abierto en pantalla mientras haya un dispositivo conectado.

## Conéctate desde un Mac

1. Abre **Finder**, elige **Ir**, luego **Conectarse al servidor** (o pulsa **Command y K**).
2. Escribe la dirección FTP que se muestra en Everdisk, por ejemplo `ftp://192.168.1.20:2121`.
3. Haz clic en **Conectar**, luego elige **Invitado** o introduce tu **Usuario** y **Contraseña**.

El Finder monta el recurso compartido FTP para que puedas explorar y copiar archivos a tu Mac. Ten en cuenta que el Finder abre FTP como solo lectura. Cuando quieras subir desde un Mac, usa una app FTP como se describe más abajo.

## Conéctate desde Windows

1. Abre el **Explorador de archivos** y haz clic en la barra de direcciones de arriba.
2. Escribe la dirección FTP de Everdisk, por ejemplo `ftp://192.168.1.20:2121`, y pulsa **Enter**.
3. Introduce tu **Usuario** y **Contraseña** si estableciste uno, o continúa como invitado.

Los archivos compartidos aparecen en la ventana y puedes copiarlos a tu PC.

## Conéctate con una app FTP (FileZilla, Cyberduck)

Para subidas y control total, una app FTP es la mejor herramienta. **FileZilla** y **Cyberduck** son gratuitas y funcionan en Windows, Mac y Linux.

1. Abre la app y crea una nueva conexión.
2. Establece el **Host** en la dirección Wi-Fi de tu iPhone, y el **Puerto** en **2121**.
3. Para el inicio de sesión, introduce tu **Usuario** y **Contraseña**, o elige **Anónimo** si no estableciste ninguno.
4. Conéctate y arrastra archivos en ambos sentidos (las subidas necesitan Edición de archivos activada).

## Conéctate desde Linux

1. Abre tu gestor de archivos y elige **Conectarse al servidor** u **Otras ubicaciones**.
2. Introduce la dirección, por ejemplo `ftp://192.168.1.20:2121`.
3. Conéctate como invitado o con tu inicio de sesión.

También puedes usar cualquier cliente FTP de Linux desde el terminal, apuntándolo al mismo host y puerto 2121.

## Conéctate desde Android

Android no tiene un explorador FTP del sistema, así que usa una app:

1. Instala un cliente FTP como **AndFTP**, **FTPCafe**, o un gestor de archivos con soporte FTP como **Solid Explorer**.
2. Añade una conexión con el host, el **puerto 2121** y tu inicio de sesión o Anónimo.
3. Explora y transfiere.

## Conéctate desde otro iPhone o iPad

La app Archivos de iOS no incluye un cliente FTP, así que usa una de estas opciones en el segundo dispositivo:

- **La propia pestaña Dispositivos de Everdisk.** Abre Everdisk, ve a **Dispositivos**, toca **Nueva conexión**, elige **FTP** e introduce la dirección, por ejemplo `ftp://192.168.1.20:2121`. Es la ruta más sencilla.
- **Una app FTP dedicada** para iOS, usando el mismo host, puerto 2121 e inicio de sesión.

## Conecta otros equipos: cámaras, TVs, routers y NAS

Aquí es donde FTP brilla. Muchos dispositivos tienen un cliente FTP integrado que puede enviar o recoger archivos:

- **Las cámaras** que suben fotos por FTP pueden enviarlas directamente a tu iPhone.
- **Las smart TVs, routers, cajas NAS y herramientas de automatización** compatibles con FTP pueden conectarse de la misma forma.

Apúntalos a la dirección Wi-Fi de tu iPhone, el puerto **2121** y tu inicio de sesión (o Anónimo), usando la dirección que se muestra en Everdisk.

## Solo lectura o lectura y escritura

El interruptor **Edición de archivos** en Ajustes, Compartir, Acceso controla esto. Activado permite que la gente suba, renombre y elimine. Desactivado significa que solo pueden descargar. Elige solo lectura cuando entregas archivos y no quieres que se cambie nada en tu teléfono.

## Formas reales en que la gente usa esto

- **Conectar FileZilla a tu iPhone** y meter un lote de archivos en el teléfono de una sola vez.
- **Dejar que una app o dispositivo antiguo que solo habla FTP** alcance tus archivos cuando nada más consigue conectarse.
- **Recibir fotos de una cámara** que sube por FTP.
- **Mover archivos entre un iPhone y un iPad** usando la pestaña Dispositivos de Everdisk en el dispositivo receptor.

## Algunos consejos

- Mantén Everdisk abierto mientras haya un dispositivo conectado, ya que iOS pausa las apps en segundo plano al cabo de un rato.
- Para subir desde un Mac, usa FileZilla o Cyberduck en lugar del Finder, porque el Finder abre FTP como solo lectura.
- Deja el inicio de sesión vacío para la mayor compatibilidad, y luego conéctate como Anónimo, que la mayoría de los clientes FTP ofrecen.
- FTP no cifra su tráfico. En una red en la que no confíes, usa el [servidor SMB con cifrado](/docs/howto/how-to-set-up-smb-server-on-iphone-ipad-for-file-sharing/) en su lugar.

## Preguntas frecuentes

{{% details title="¿Cuál es la dirección y el puerto FTP de mi iPhone?" closed="true" %}}
Después de empezar a compartir, Everdisk muestra la dirección en la pantalla Compartir. Tiene el aspecto ftp://192.168.1.20:2121. El 2121 es el puerto que Everdisk usa para FTP, y la primera parte es la dirección de tu iPhone en la Wi-Fi, así que la tuya será distinta.
{{% /details %}}

{{% details title="¿Cómo conecto FileZilla o Cyberduck a mi iPhone?" closed="true" %}}
Abre la app y crea una nueva conexión. Establece el Host en la dirección Wi-Fi de tu iPhone y el Puerto en 2121. Introduce tu Usuario y Contraseña, o elige Anónimo si no estableciste ninguno en Everdisk. Conéctate y podrás arrastrar archivos en ambos sentidos cuando Edición de archivos esté activada.
{{% /details %}}

{{% details title="¿Puedo conectarme al FTP de mi iPhone desde Windows?" closed="true" %}}
Sí. Abre el Explorador de archivos, haz clic en la barra de direcciones, escribe la dirección FTP de Everdisk (por ejemplo ftp://192.168.1.20:2121) y pulsa Enter. Introduce tu inicio de sesión si estableciste uno, o continúa como invitado. Para subidas y más control, usa una app FTP como FileZilla en su lugar.
{{% /details %}}

{{% details title="¿Necesito un inicio de sesión para FTP?" closed="true" %}}
No, el inicio de sesión es opcional. Deja el Usuario y la Contraseña vacíos en Ajustes, Compartir, Acceso, y conéctate como Anónimo, que la mayoría de los clientes FTP ofrecen. Establece un inicio de sesión si quieres que las conexiones inicien sesión primero.
{{% /details %}}

{{% details title="¿Por qué solo puedo descargar y no subir por FTP?" closed="true" %}}
Dos razones son comunes. Primera, el interruptor Edición de archivos en Ajustes, Compartir, Acceso debe estar activado para permitir subidas, cambios de nombre y eliminaciones. Segunda, el Finder del Mac abre FTP como solo lectura, así que usa una app FTP como FileZilla o Cyberduck cuando quieras subir.
{{% /details %}}

{{% details title="¿Puedo usar FTP entre dos iPhones?" closed="true" %}}
Sí. Inicia el servidor FTP en el primer iPhone. En el segundo, abre Everdisk, ve a la pestaña Dispositivos, toca Nueva conexión, elige FTP e introduce la dirección que se muestra en el primer teléfono. Una app FTP dedicada para iOS también funciona, ya que la app Archivos de iOS no incluye un cliente FTP.
{{% /details %}}

{{% details title="¿FTP es seguro?" closed="true" %}}
El FTP simple no cifra su tráfico, así que trátalo como una herramienta para redes de confianza, como tu Wi-Fi doméstica. En una red que no controlas, usa el servidor SMB con Requerir cifrado SMB activado, que protege cada transferencia.
{{% /details %}}

{{% details title="¿Qué dispositivos pueden conectarse por FTP?" closed="true" %}}
Casi cualquier cosa con un cliente FTP. Eso incluye ordenadores Mac, Windows y Linux, apps FTP como FileZilla y Cyberduck, gestores de archivos de Android, y hardware como cámaras, smart TVs, routers, cajas NAS y herramientas de automatización. Ese amplio alcance es la razón principal para elegir FTP.
{{% /details %}}

{{% details title="¿Por qué se cayó mi conexión FTP?" closed="true" %}}
Tu iPhone es el servidor, e iOS pausa las apps que permanecen demasiado tiempo en segundo plano. Mantén Everdisk abierto en pantalla mientras haya un dispositivo conectado, y conéctalo a la corriente para transferencias largas. Asegúrate también de que ambos dispositivos siguen en la misma Wi-Fi.
{{% /details %}}

{{% details title="¿Everdisk es gratis?" closed="true" %}}
Sí, Everdisk se descarga gratis y el servidor FTP está incluido. Una compra opcional única Premium añade extras como puertos personalizados y conversión de fotos y vídeos. Puedes configurar FTP y transferir archivos sin pagar.
{{% /details %}}

¿Listo para probarlo? [Descarga Everdisk en la App Store](https://apps.apple.com/app/apple-store/id6751851132?pt=95781850&ct=everappzcom&mt=8) y conecta tu primer cliente FTP en un par de minutos. ¿Preguntas o comentarios? Escríbenos a **support@everappz.com**.
