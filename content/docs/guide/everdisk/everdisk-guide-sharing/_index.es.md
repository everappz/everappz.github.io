---
title: "Compartir"
date: 2026-08-20
description: "Aprende como funciona la funcion de compartir en Everdisk: toca Iniciar para convertir tu iPhone o iPad en una unidad inalambrica, elige que compartir (archivos, carpetas, fotos y musica), pon en marcha los cinco servidores (DLNA, HTTP, WebDAV, SMB, FTP), cifra la conexion SMB con SMB3 (AES), consulta las direcciones de conexion, mira quien esta conectado y manten la funcion activa por Wi-Fi o cable USB."
keywords: ["compartir con Everdisk", "unidad inalambrica iPhone", "empezar a compartir", "compartir archivos iPhone", "compartir fotos en red", "DLNA HTTP WebDAV FTP", "que compartir", "como conectarse", "manten la app abierta", "compartir por Wi-Fi o cable USB"]
tags: ["everdisk", "guia", "compartir"]
readingTime: 9
---


La pestana **Compartir** es el corazon de Everdisk. Es donde conviertes tu iPhone o iPad en una unidad inalambrica, eliges exactamente lo que quieres compartir y obtienes las direcciones que usan otros dispositivos para conectarse. Es la primera pestana que ves al abrir la app.

## Iniciar y detener la funcion de compartir

En el centro de la pantalla de Compartir hay un boton redondo y grande.

- Toca **Iniciar** para poner en linea todos tus servidores activados a la vez. El boton muestra **Iniciando...** y luego **Detener** cuando la funcion ya esta activa.
- Toca **Detener** para volver a dejarlo todo sin conexion. Los dispositivos conectados se desconectan.

Mientras la funcion esta activa, los archivos, las fotos y la musica que hayas elegido estan disponibles para cualquier dispositivo de la misma red que se conecte con uno de los cinco metodos de abajo.

> La funcion de compartir solo se ejecuta mientras la app esta abierta. Consulta **Manten la app abierta**, cerca del final de esta pagina, para entender por que y como mantener activas las transferencias grandes.

## Elige que compartir

Antes de empezar, toca el encabezado **Que compartir** para abrir tres grupos. Puedes compartir cualquier combinacion de ellos, pero tienes que elegir al menos un elemento para poder empezar.

**Archivos y carpetas**

- La carpeta **Documentos** propia de la app se comparte de forma predeterminada. Puedes dejar de compartirla si lo prefieres.
- Toca **Anadir carpeta** para compartir una carpeta de cualquier parte de tu dispositivo, o **Anadir archivo** para compartir archivos sueltos.
- Cada elemento compartido tiene un boton de **Info** y un boton de **Dejar de compartir**.

**Fotos y videos**

- Activa **Permitir acceso a toda la biblioteca de fotos** para compartir toda tu biblioteca de fotos y videos, o
- toca **Anadir fotos** para elegir a mano solo las fotos y los videos que quieras compartir.

**Musica**

- Activa **Permitir acceso a toda la biblioteca de musica** para compartir toda tu biblioteca de musica, o
- toca **Anadir pistas** para compartir solo canciones concretas.
- Las pistas protegidas (DRM) o guardadas solo en la nube no se pueden compartir.

Si intentas empezar sin nada seleccionado, Everdisk muestra un aviso de **Nada que compartir**. Si cambias lo que compartes mientras la funcion esta activa, tienes que **detener y volver a iniciar** para aplicar el cambio.

## Los cinco servidores

Everdisk comparte el mismo contenido de cinco formas a la vez. Cada una esta pensada para un tipo de dispositivo distinto y se puede activar o desactivar en **Ajustes -> Compartir -> Conexiones**. De forma predeterminada, las cinco estan activadas.

- **TV y centro multimedia (DLNA)**: para smart TV y reproductores multimedia. Descubren tu dispositivo por si solos y muestran tus fotos, videos y musica con miniaturas de vista previa.
- **Navegador (HTTP)**: para cualquier telefono, tablet u ordenador. La otra persona abre un enlace en su navegador web para explorar y descargar tus archivos. No hay que instalar nada.
- **Ordenador (WebDAV)**: para un Mac, un PC con Windows o un equipo Linux. Tu dispositivo aparece como una unidad de red normal, asi que puedes arrastrar archivos en ambos sentidos.
- **Equipo (avanzado) (SMB)**: una unidad de red para Mac, Windows y Linux. En un Mac aparece por su cuenta en la barra lateral del Finder; en Windows, abrela en el Explorador de archivos con una direccion `smb://`. Es la unica conexion que puedes **cifrar**, con cifrado SMB3 (AES).
- **Otras apps y dispositivos (FTP)**: para apps de archivos y usuarios avanzados que trabajan con FTP.

Para ver instrucciones de conexion paso a paso de cada tipo, consulta [Conecta tus dispositivos](/docs/guide/everdisk/everdisk-guide-connect).

## Como conectarse y direcciones de conexion

Despues de tocar Iniciar, la seccion **Como conectarse** muestra una tarjeta por cada servidor activo con la **direccion** exacta que hay que escribir en el otro dispositivo. Cada direccion es facil de copiar: tocala para copiarla, usa el boton **Compartir** para enviarla o toca el boton de **info (i)** para ver instrucciones detalladas de cada protocolo.

- La tarjeta de DLNA muestra una direccion de descripcion del dispositivo que termina en `/device-desc.xml` para los reproductores que la piden.
- Cuando tu dispositivo esta conectado a un Mac con cable, aparece una direccion adicional con una insignia de **Conexion por cable** que usa el nombre `.local` de tu dispositivo.

Tambien puedes abrir la direccion como un **codigo QR** para que la camara de otro dispositivo salte directamente a ella.

## Quien esta conectado

La seccion **Quien esta conectado** muestra en tiempo real los dispositivos conectados a ti en ese momento. Toca el boton de mas acciones junto a cualquier dispositivo para **Bloquear este dispositivo** si no lo reconoces. Los dispositivos bloqueados se gestionan en [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access).

## El nombre y el avatar de tu dispositivo

Cada dispositivo tiene un nombre amigable (como "Speedy-Hare") y un avatar de color. Este es el nombre que una TV, un ordenador u otra app muestra para tu dispositivo en la red, asi que es facil de reconocer. Puedes regenerar el nombre y el avatar gratis, o poner un nombre, un icono o una foto de avatar personalizados con Premium. Consulta [Ajustes](/docs/guide/everdisk/everdisk-guide-settings).

## Compartir por Wi-Fi o por cable USB

La funcion de compartir puede ejecutarse en dos situaciones:

- **Por Wi-Fi**: tu dispositivo y los demas estan en la misma red Wi-Fi.
- **Por cable USB**: tu dispositivo esta conectado a un **Mac** con cable, incluso sin nada de Wi-Fi. Es mas rapido que el Wi-Fi y sigue funcionando en un avion, en un hotel o en una red bloqueada.

Si no hay ni Wi-Fi ni cable disponibles, el boton **Iniciar** se desactiva y aparece un aviso de **Sin conexion Wi-Fi**. Si la conexion se cae mientras compartes, Everdisk detiene la funcion automaticamente y te avisa. Toca el boton de info en cualquiera de estos avisos para ver una explicacion completa.

## Manten la app abierta

Como tu iPhone o iPad actua de servidor, **la funcion de compartir solo funciona mientras Everdisk esta abierta en pantalla**. Si cierras la app o bloqueas el dispositivo durante mucho tiempo, el sistema puede pausar la app y la funcion se detiene.

Para transferencias grandes:

- Manten Everdisk abierta y en primer plano.
- Conecta tu dispositivo a la corriente.
- Pon **Bloqueo automatico** en **Nunca** en la app de Ajustes de iOS mientras haces la transferencia.

Puedes activar **Avisar antes de desconectar** (en Ajustes -> Compartir) para que Everdisk te recuerde volver a abrir la app antes de que el sistema la suspenda. Toca el boton de info en el aviso de **Manten la app abierta** para ver mas detalles.

## Siguientes pasos

- [Conecta tus dispositivos](/docs/guide/everdisk/everdisk-guide-connect): conecta una TV, un ordenador, un navegador, un telefono o un cable USB.
- [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access): anade una contrasena y controla la edicion.
- [Ajustes](/docs/guide/everdisk/everdisk-guide-settings): activa o desactiva servidores y ajusta la calidad.
