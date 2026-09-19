---
title: "Ajustes"
date: 2026-08-20
description: "Un recorrido completo por los ajustes de Everdisk: perfil del dispositivo (nombre y avatar), los cinco servidores de conexion, los controles de acceso, el cifrado SMB (SMB3/AES), la calidad de fotos y video, los puertos personalizados, las miniaturas DLNA, las opciones de red y transferencia, las opciones del gestor de archivos y Premium."
keywords: ["ajustes de Everdisk", "nombre y avatar del dispositivo", "servidores de conexion", "calidad de fotos y video", "puertos personalizados HTTP WebDAV FTP", "miniaturas DLNA", "transferencias en paralelo", "eliminar archivos permanentemente", "cache de miniaturas", "Everdisk Premium"]
tags: ["everdisk", "guia", "ajustes"]
readingTime: 12
---


La pestana **Ajustes** agrupa todo en tres areas principales (**Compartir**, **Red** y **Gestor de archivos**), ademas de Premium, comentarios y enlaces legales. Esta pagina explica cada ajuste y su valor predeterminado.

## Premium

En la parte superior de Ajustes ves tu estado Premium, o un boton de **Desbloquear todas las funciones**. Everdisk es gratis con algunos limites; una compra unica de **Premium Lifetime** los elimina. Consulta [Premium](#premium-lifetime) al final de esta pagina.

## Ajustes de compartir

### General

- **Iniciar la funcion de compartir automaticamente**: empieza a compartir en cuanto abres la app. *(Premium.)*
- **Compartir la carpeta Documentos**: comparte la carpeta Documentos propia de la app. Activado de forma predeterminada.
- **Avisar antes de desconectar**: te recuerda que vuelvas a abrir la app antes de que el sistema la suspenda en segundo plano. Desactivado de forma predeterminada; pide permiso de notificaciones la primera vez.

### Perfil del dispositivo

- **Nombre del dispositivo**: el nombre que otros dispositivos ven de ti en la red. Toca para editarlo. *(Premium.)*
- **Avatar del dispositivo**: el icono y el color de fondo de tu dispositivo. Puedes elegir un icono, un degradado de fondo o **elegir un avatar desde Fotos**. *(Premium.)*
- **Regenerar nombre y avatar** y **Regenerar avatar**: consigue un nombre o un avatar nuevo al azar. *(Gratis.)*

### Acceso

- **Usuario** y **Contrasena**: exige un inicio de sesion para las conexiones de Navegador, Ordenador y Otras apps.
- **Edicion de archivos**: permite que los dispositivos conectados suban, renombren y eliminen. Activado de forma predeterminada.
- **Dispositivos bloqueados**: gestiona los dispositivos que has bloqueado.

Consulta [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access) para ver los detalles.

### Conexiones

Activa o desactiva cada servidor. Los cinco estan activados de forma predeterminada, y cada uno tiene un boton de info (i) con instrucciones de conexion:

- **TV y centro multimedia** (DLNA)
- **Navegador** (HTTP)
- **Ordenador** (WebDAV)
- **Equipo (avanzado)** (SMB): una unidad de red para Mac, Windows y Linux; en un Mac aparece por su cuenta en la barra lateral del Finder. La unica conexion que se puede cifrar.
- **Otras apps y dispositivos** (FTP)

### Fotos

- **Formato**: Original o Mas compatible (JPEG).
- **Calidad**: Original, Alta, Media o Baja.

Cualquier opcion que no sea Original convierte las fotos mientras se comparten, lo que es mas lento. La conversion es una funcion Premium.

### Videos

- **Formato**: Original o Mas compatible (H.264 MP4).
- **Calidad**: Original, Alta, Media o Baja.

La misma idea que con las fotos: Original es lo mas rapido y la conversion es Premium. Baja la calidad si una TV antigua no puede reproducir un video.

### Avanzado

- **Puerto HTTP** (80 de forma predeterminada), **Puerto WebDAV** (8080 de forma predeterminada), **Puerto SMB** (4455 de forma predeterminada), **Puerto FTP** (2121 de forma predeterminada). DLNA elige su puerto automaticamente. *(Cambiar los puertos es Premium; los usuarios gratuitos pueden ver los valores.)*

### Cifrado SMB

- **Requerir cifrado SMB**: cifra cada transferencia SMB con **cifrado SMB3 (AES)** para que nadie mas en la red pueda leer tus archivos. Desactivado de forma predeterminada. Necesita un **usuario y una contrasena** establecidos mas arriba (las conexiones cifradas no pueden ser anonimas) y un cliente que admita SMB3, como el Finder de un Mac moderno o Windows 10 y posteriores. Los cambios surten efecto la proxima vez que inicies la funcion de compartir. *(Premium.)*

### Miniaturas DLNA

- **Mostrar miniaturas**: publica imagenes de vista previa para las TV. Activado de forma predeterminada (gratis).
- Elige que tamanos publicar: **Pequeno (160px)**, **Mediano (640px)**, **Grande (1024px)**, **Extra grande (4096px)**.

## Ajustes de red

- **Transferencias de archivos**: usa **Wi-Fi** solo, o **Wi-Fi y datos moviles**, para las descargas y las subidas. Wi-Fi de forma predeterminada.
- **Limite de transferencias en paralelo**: cuantas transferencias se ejecutan a la vez. 5 de forma predeterminada.
- **Transferencias en segundo plano**: manten las transferencias en marcha mientras usas otras pantallas. Activado de forma predeterminada.
- **Miniaturas de archivos**: si obtener miniaturas de archivos en otros dispositivos solo por Wi-Fi o tambien por datos moviles. Wi-Fi de forma predeterminada.

## Ajustes del gestor de archivos

- **Eliminar archivos permanentemente**: elimina de inmediato sin papelera. Desactivado de forma predeterminada. Consulta [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access).
- **Restablecer todos los mensajes de aviso**: recupera los avisos con consejos que has cerrado.
- **Cache de miniaturas**: mira cuanto espacio usan las miniaturas en cache y **Vaciar la cache de miniaturas**.

## Comentarios y legal

Abajo puedes **Valorar esta app**, **Enviar comentarios**, **Descubrir mas apps** y abrir los **Terminos y condiciones** y la **Politica de privacidad**.

## Premium Lifetime

Everdisk es gratis. Una unica compra de **Premium Lifetime** (un pago unico, no una suscripcion) desbloquea:

- **Carpetas ilimitadas**: comparte mas de 5 carpetas.
- **Conexiones ilimitadas**: guarda mas de 10 servidores en la pestana Dispositivos.
- **Conversion de fotos y video**: comparte en cualquier calidad distinta de Original.
- **Cifrado SMB**: protege las transferencias SMB con cifrado SMB3 (AES).
- **Puertos personalizados**: define tus propios puertos HTTP, WebDAV, SMB y FTP.
- **Inicio automatico de la funcion de compartir**: empieza a compartir automaticamente al abrir la app.
- **Personalizacion del dispositivo**: un nombre de dispositivo, un icono de avatar, un degradado de fondo o una foto de avatar personalizados.

Premium esta vinculado a tu Apple ID. Usa **Restaurar compras** para desbloquearlo en tus demas dispositivos que tengan sesion iniciada con el mismo Apple ID.

## Siguientes pasos

- [Compartir](/docs/guide/everdisk/everdisk-guide-sharing): la pantalla de Compartir en detalle.
- [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access): contrasenas, edicion y bloqueo.
- [Preguntas frecuentes](/docs/faq/everdisk): respuestas rapidas a las dudas mas habituales.
