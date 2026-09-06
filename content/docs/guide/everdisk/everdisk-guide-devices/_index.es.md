---
title: "Conectarse a servidores"
date: 2026-08-20
description: "Usa la pestana Dispositivos de Everdisk para conectarte a otros servidores de tu red. Anade y explora servidores DLNA, WebDAV, FTP y SFTP y unidades NAS, reproduce audio y video, descarga archivos y crea, sube, renombra, mueve o elimina en los servidores que lo permitan."
keywords: ["pestana Dispositivos de Everdisk", "conectar a NAS", "cliente DLNA iPhone", "cliente WebDAV iPhone", "cliente FTP iPhone", "cliente SFTP iPhone", "explorar servidor de red", "reproducir desde NAS", "descargar desde servidor", "conectar nube WebDAV"]
tags: ["everdisk", "guia", "dispositivos", "conexiones"]
readingTime: 9
---


Everdisk no es solo una unidad inalambrica: tambien es un cliente para los demas dispositivos de tu red. La pestana **Dispositivos** te permite conectarte a servidores **DLNA**, **WebDAV**, **FTP** y **SFTP**, incluidas unidades NAS y servidores multimedia, para luego explorar, reproducir y descargar sus archivos.

## La pantalla de Dispositivos

La pestana Dispositivos tiene dos partes:

- **Conexiones**: los servidores que ya has guardado.
- **Dispositivos disponibles**: los servidores que Everdisk encuentra automaticamente en tu red local.

Para conectarte a algo que Everdisk ya encontro, solo tienes que tocarlo en **Dispositivos disponibles**. Para anadir un servidor a mano, toca el boton de **mas (+)** o **Nueva conexion**.

## Anadir una conexion nueva

Toca **Nueva conexion** y elige el tipo de servidor al que quieres acceder:

- **DLNA / UPnP**: lo mejor para servidores multimedia. Reproduce video, musica y fotos desde bibliotecas multimedia, unidades de almacenamiento en red y TV y ordenadores compatibles con DLNA. DLNA es de solo lectura: puedes explorar, reproducir y descargar, pero no puedes subir ni cambiar archivos.
- **WebDAV**: conectate a servidores de archivos, unidades de almacenamiento en red y unidades en la nube compatibles con WebDAV. Lectura y escritura cuando el servidor lo permite.
- **FTP**: habitual en routers, unidades de almacenamiento en red y alojamiento web. El puerto predeterminado es el 21 (990 para FTPS seguro); puedes indicar un puerto personalizado en la direccion, por ejemplo `ftp://host:2121`. Deja el usuario y la contrasena vacios para el acceso anonimo.
- **SFTP**: conectate de forma segura por SSH. El puerto predeterminado es el 22; usa un puerto personalizado en la direccion si hace falta, por ejemplo `sftp://host:2222`.

> Everdisk se conecta solo a estos protocolos de red local y de direccion directa. No inicia sesion en cuentas en la nube como Google Drive o Dropbox. Una unidad en la nube solo es accesible si ese servicio ofrece una direccion **WebDAV** que puedas escribir.

## Introducir la direccion e iniciar sesion

En el editor de conexion, rellena:

- **Titulo**: un nombre amigable para la conexion.
- **URL / direccion**: la direccion del servidor (se muestran ejemplos para cada tipo).
- **Usuario** y **Contrasena**: deja ambos vacios si el servidor permite el acceso anonimo.

En WebDAV puedes permitir certificados no validos si tu servidor usa uno autofirmado. Si no se puede verificar la identidad de un servidor seguro, Everdisk te pide que confirmes antes de confiar en el.

Los usuarios gratuitos pueden guardar hasta **10** conexiones. Premium elimina el limite.

## Explorar, reproducir y descargar

Una vez conectado, toca el servidor para abrirlo:

- **Explora** las carpetas en lista o cuadricula, ordenalas y mira las miniaturas. Los servidores DLNA tambien muestran los detalles y las caratulas de la musica.
- **Reproduce** audio y video. El audio va a la cola del minireproductor; el video se reproduce a pantalla completa. El desplazamiento funciona mientras se reproduce un archivo en streaming.
- **Descarga** archivos a tu dispositivo. Selecciona varios a la vez para una descarga por lotes. Las descargas aparecen en **Transferencias de archivos** y llegan a tu carpeta **Documentos**.
- La opcion **Info** de cualquier elemento muestra su tipo, tamano, fecha, ruta y detalles multimedia.

## Cambiar archivos en un servidor

En los servidores que permiten la escritura (**WebDAV, FTP y SFTP**) tambien puedes gestionar archivos:

- **Nueva carpeta**
- **Subir archivos** desde tu dispositivo
- **Renombrar**, **Mover** y **Eliminar** (uno o varios elementos a la vez)

Los servidores **DLNA** son de solo lectura, asi que estas acciones no estan disponibles ahi.

## Controla tus transferencias

Las descargas y las subidas se ejecutan en segundo plano y aparecen en **Transferencias de archivos**, que abres desde la parte superior izquierda de la pestana **Documentos**. Ahi puedes seguir el progreso y pausar, reanudar, reintentar, cancelar o borrar tareas. Tambien puedes ajustar las transferencias en [Ajustes -> Red](/docs/guide/everdisk/everdisk-guide-settings) (solo Wi-Fi o Wi-Fi y datos moviles, cuantas se ejecutan a la vez y si continuan en segundo plano).

## Siguientes pasos

- [Archivos y documentos](/docs/guide/everdisk/everdisk-guide-files): gestiona todo lo que descargas.
- [Fotos, musica y video](/docs/guide/everdisk/everdisk-guide-media): reproduce lo que transmites.
- [Ajustes](/docs/guide/everdisk/everdisk-guide-settings): limites de conexion y opciones de transferencia.
