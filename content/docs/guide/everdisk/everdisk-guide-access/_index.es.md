---
title: "Acceso y privacidad"
date: 2026-08-20
description: "Manten seguro lo que compartes con Everdisk: protege el acceso con un usuario y contrasena, cifra la conexion SMB con SMB3 (AES), controla si los dispositivos conectados pueden subir, renombrar y eliminar con la Edicion de archivos, bloquea dispositivos desconocidos, elige entre papelera y eliminacion permanente y entiende por que todo se queda en tu red local."
keywords: ["proteccion con contrasena Everdisk", "cifrado SMB", "cifrado SMB3 AES", "interruptor de edicion de archivos", "bloquear dispositivo", "dispositivos bloqueados", "eliminar archivos permanentemente", "solo red local", "compartir archivos de forma privada", "DLNA sin contrasena", "seguridad de red"]
tags: ["everdisk", "guia", "acceso", "privacidad", "seguridad"]
readingTime: 8
---


Everdisk mantiene tus archivos en tu propia red y te da controles sencillos sobre quien puede acceder a ellos y que puede hacer. Encontraras estos controles en **Ajustes -> Compartir -> Acceso**, mas algunos ajustes relacionados en el gestor de archivos.

## Protege el acceso con un usuario y contrasena

De forma predeterminada, cualquiera de la misma red que tenga tu direccion puede abrir tus archivos compartidos. Para exigir un inicio de sesion:

1. Ve a **Ajustes -> Compartir -> Acceso**.
2. Introduce un **Usuario** y una **Contrasena**.
3. Ahora las conexiones de **Navegador (HTTP)**, **Ordenador (WebDAV)**, **Equipo (avanzado) (SMB)** y **Otras apps y dispositivos (FTP)** piden esos datos antes de mostrar tus archivos.

Deja ambos campos vacios para el acceso abierto. Tu contrasena se guarda de forma segura en el Llavero del dispositivo.

> **DLNA siempre esta abierto.** La conexion de TV y centro multimedia (DLNA) no se puede proteger con contrasena, asi que, una vez activada, cualquier dispositivo de la misma red Wi-Fi puede explorar tu contenido compartido. Desactivala si solo quieres conexiones protegidas, y comparte unicamente en redes de confianza.

## Cifra la conexion SMB (SMB3 / AES)

Un usuario y una contrasena controlan **quien** puede conectarse, pero los datos en si siguen viajando sin cifrar en la mayoria de las conexiones. **SMB es la unica conexion que Everdisk puede cifrar**, lo que codifica cada transferencia para que nadie mas en la misma red pueda leerla.

Para activarlo:

1. Establece un **Usuario** y una **Contrasena** como arriba: las conexiones cifradas no pueden ser anonimas.
2. Ve a **Ajustes -> Compartir** y activa **Requerir cifrado SMB**.
3. **Deten e inicia** la comparticion de nuevo para que el cambio surta efecto.

Entonces cada transferencia SMB queda protegida con **cifrado SMB3 (AES)**. El dispositivo que se conecta debe admitir SMB3: el Finder de un Mac moderno, o **Windows 10 y posteriores**. Es una gran opcion en una Wi-Fi en la que no confias del todo. El Cifrado SMB es una funcion Premium.

## Permitir o bloquear la edicion (Edicion de archivos)

El interruptor de **Edicion de archivos** controla si los dispositivos conectados solo pueden ver tus archivos o tambien cambiarlos.

- **Activado** (el valor predeterminado): los dispositivos conectados pueden **subir, renombrar y eliminar** tus archivos compartidos, asi que tu dispositivo funciona como una unidad de red de doble sentido real.
- **Desactivado**: tus archivos compartidos son de **solo lectura**. Los demas pueden verlos y descargarlos, pero no pueden anadir ni cambiar nada.

Al activarlo aparece una breve advertencia, porque permite que otras personas modifiquen tus archivos. Lleva una insignia de **Importante** mientras esta activado.

## Bloquear un dispositivo

Si ves un dispositivo que no reconoces:

1. En la pantalla de Compartir, buscalo en **Quien esta conectado**.
2. Toca su boton de mas acciones y elige **Bloquear este dispositivo**.

Los dispositivos bloqueados aparecen en **Ajustes -> Compartir -> Acceso -> Dispositivos bloqueados**, donde puedes **desbloquear** uno o **Desbloquear todos**. El bloqueo sigue al dispositivo aunque cambie su direccion de red (para las conexiones de Navegador, Ordenador y TV).

## Papelera frente a eliminacion permanente

Cuando se elimina un archivo (tu en el gestor de archivos, o un dispositivo conectado), normalmente va a una **papelera** recuperable para que puedas recuperarlo.

Si prefieres que los archivos se quiten de inmediato sin posibilidad de recuperacion, activa **Eliminar archivos permanentemente** en **Ajustes -> Gestor de archivos -> Eliminar archivos**. Esta desactivado de forma predeterminada. **Afecta al gestor de archivos del dispositivo** y a **las eliminaciones hechas por la red**; no cambia como gestionan la eliminacion la biblioteca de Fotos ni la de Musica del sistema.

## Todo se queda en local

Everdisk comparte solo por tu **red local**: nada se sube a internet y no hay ninguna cuenta en la nube de por medio. Vale la pena tener en cuenta algunas cosas:

- Everdisk necesita el permiso de **Red local** de iOS para que los dispositivos cercanos puedan encontrarla. Si ese permiso esta desactivado, un aviso explica como volver a activarlo en la app de Ajustes de iOS.
- Para lograr la maxima privacidad, comparte solo mientras estas en una red Wi-Fi **de casa o privada** de confianza, y ten cuidado en el Wi-Fi publico. Un usuario y contrasena ayudan, pero no sustituyen a una red de confianza.
- La **opcion mas privada de todas es un cable USB a un Mac**: los datos van directamente por el cable y nunca pasan por el router ni por internet. Consulta [Conecta tus dispositivos](/docs/guide/everdisk/everdisk-guide-connect).

## Siguientes pasos

- [Compartir](/docs/guide/everdisk/everdisk-guide-sharing): elige que compartir y empieza a compartir.
- [Ajustes](/docs/guide/everdisk/everdisk-guide-settings): todos los ajustes de Acceso y del gestor de archivos en un solo lugar.
