---
title: "Conecta tus dispositivos"
date: 2026-08-20
description: "Instrucciones paso a paso para conectarte a tu unidad inalambrica Everdisk: mira contenido en una smart TV por DLNA, abre tus archivos en cualquier navegador web, monta tu dispositivo como unidad de red en Finder, Windows o Linux por WebDAV o SMB (con cifrado SMB3/AES opcional), conecta apps de archivos por FTP y transfiere por cable USB a un Mac sin Wi-Fi."
keywords: ["conectarse a Everdisk", "transmitir a la TV DLNA", "abrir archivos en el navegador", "montar unidad de red Finder", "WebDAV Windows Linux", "app de archivos FTP", "transferir por cable USB Mac", "conectar iPhone al ordenador", "unidad de red iPhone"]
tags: ["everdisk", "guia", "conectar"]
readingTime: 11
---


En cuanto tocas **Iniciar** en la pantalla de [Compartir](/docs/guide/everdisk/everdisk-guide-sharing), otros dispositivos pueden conectarse a tus archivos de cinco formas distintas. Elige el metodo que encaje con el dispositivo que quieras usar. En todos los casos, la **direccion** exacta que necesitas aparece en la seccion **Como conectarse** de la pantalla de Compartir.

> Ambos dispositivos tienen que estar en la **misma red Wi-Fi** o, en el caso de un Mac, conectados con un **cable USB** (consulta la ultima seccion).

## Mirar en una TV (DLNA)

Usa esto para mostrar fotos, videos y musica en una smart TV o un reproductor multimedia.

1. En **Ajustes -> Compartir -> Conexiones**, asegurate de que **TV y centro multimedia** esta activado (lo esta de forma predeterminada).
2. En la pantalla de Compartir, toca **Iniciar**.
3. En tu TV, abre su reproductor multimedia integrado o su app de servidor multimedia (puede llamarse Media Player, SmartShare, AllShare o algo parecido).
4. Tu dispositivo aparece en la lista de servidores multimedia con su nombre (por ejemplo, "Speedy-Hare"). Seleccionalo.
5. Explora tus fotos, videos y musica compartidos y empieza a reproducir. Las miniaturas de vista previa aparecen automaticamente.

Notas:

- DLNA no se puede proteger con contrasena, asi que esta conexion queda abierta a cualquiera de la misma red Wi-Fi mientras este activada.
- Si un video no se reproduce en una TV antigua, baja la calidad del video en **Ajustes -> Compartir -> Videos** para que Everdisk lo convierta a un formato mas compatible.

## Abrir en un navegador web (HTTP)

Usa esto para pasar archivos a cualquiera que tenga un navegador web, sin instalar ninguna app.

1. En **Ajustes -> Compartir -> Conexiones**, asegurate de que **Navegador** esta activado.
2. Toca **Iniciar**.
3. En la pantalla de Compartir, copia la direccion de **Navegador** (o muestra su codigo QR).
4. En el otro telefono, tablet u ordenador, abre cualquier navegador web (Safari, Chrome, Edge, Firefox) y escribe esa direccion.
5. La pagina se abre con tus archivos compartidos.

En el navegador, la otra persona puede:

- Cambiar entre la vista de **lista** y la de **cuadricula** y ordenar por nombre, fecha o tamano.
- Ver **miniaturas** reales de fotos, videos, PDF y caratulas de musica.
- Abrir una foto en una **galeria** a pantalla completa con deslizamiento, zoom con los dedos y pase de diapositivas.
- Reproducir musica en un **reproductor** integrado con cola, aleatorio y repeticion.
- **Descargar** cualquier archivo, o descargar una carpeta entera (o varios elementos seleccionados) como un unico **Archive.zip**.
- **Subir** archivos de vuelta a tu dispositivo, solo si activaste la **Edicion de archivos** (consulta [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access)).

## Usarlo como unidad de red (WebDAV)

Usa esto para que tu dispositivo aparezca como un disco normal en un Mac, un PC con Windows o un equipo Linux, y asi puedas arrastrar archivos en los dos sentidos.

**En un Mac (Finder)**

1. En **Ajustes -> Compartir -> Conexiones**, asegurate de que **Ordenador** esta activado.
2. Toca **Iniciar** y anota la direccion de **Ordenador (WebDAV)**.
3. En Finder, elige **Ir -> Conectar al servidor** (o pulsa **Cmd+K**).
4. Escribe la direccion WebDAV exactamente como aparece y haz clic en **Conectar**.
5. Introduce el usuario y la contrasena si definiste alguno; si no, conectate como invitado.
6. Tu dispositivo se abre como cualquier otra unidad de red. Arrastra archivos hacia dentro o hacia fuera.

**En Windows**

1. Abre el **Explorador de archivos**, haz clic derecho en **Este equipo** y elige **Agregar una ubicacion de red** (o asigna una unidad de red).
2. Introduce la direccion WebDAV que muestra Everdisk.
3. Introduce el usuario y la contrasena si definiste alguno.

**En Linux**

1. Abre tu gestor de archivos y elige **Conectar al servidor** (o usa `davs://` / `dav://`).
2. Introduce la direccion WebDAV que muestra Everdisk.

Que la conexion sea de solo lectura o de doble sentido depende del ajuste de **Edicion de archivos**. Con el activado puedes copiar archivos en tu dispositivo y renombrarlos o eliminarlos; con el desactivado, la unidad es de solo lectura.

## Conectar por SMB (unidad de red cifrada)

SMB es una unidad de red para Mac, Windows y Linux, basada en la comparticion de archivos que ya traen esos sistemas, asi que tu dispositivo aparece como una unidad de red normal, y es la unica conexion que puedes cifrar.

1. En **Ajustes -> Compartir -> Conexiones**, asegurate de que **Equipo (avanzado)** (la conexion SMB) esta activado.
2. Toca **Iniciar** y anota la direccion **SMB**, que tiene el aspecto de `smb://192.168.1.20:4455/Share`.
3. Conectate desde tu ordenador:
   - **Mac:** tu dispositivo aparece por su cuenta en la **barra lateral del Finder** en **Ubicaciones** (Red): solo haz clic en el e inicia sesion. Para conectarte a mano, elige **Ir -> Conectar al servidor** (**Cmd+K**) e introduce la direccion.
   - **Windows:** abre el **Explorador de archivos**, haz clic derecho en **Este equipo** y elige **Conectar a unidad de red**, luego introduce `\\<address>\Share` usando el host y el nombre del recurso compartido de la pantalla de Compartir (o escribe la direccion `smb://` en la barra de direcciones).
   - **Linux:** en tu gestor de archivos elige **Conectar al servidor** e introduce la direccion.
4. Introduce el usuario y la contrasena si definiste alguno; si no, conectate como invitado.
5. El recurso compartido se llama **Share**. Con **Edicion de archivos** activada puedes copiar archivos en ambos sentidos; con ella desactivada es de solo lectura.

**Activa el cifrado (recomendado en Wi-Fi no confiable)**

SMB es la unica conexion de Everdisk que se puede cifrar. Para proteger cada transferencia con **cifrado SMB3 (AES)**:

1. En **Ajustes -> Compartir -> Acceso**, establece un **Usuario** y una **Contrasena**: las conexiones cifradas no pueden ser anonimas.
2. En **Ajustes -> Compartir**, activa **Requerir cifrado SMB**.
3. **Deten e inicia** la comparticion de nuevo para que el cambio surta efecto.

Tu cliente debe admitir SMB3: el Finder de un Mac moderno, o **Windows 10 y posteriores**. El Cifrado SMB es una funcion Premium.

## Conectar una app de archivos (FTP)

Usa esto con apps de gestion y transferencia de archivos que trabajan con FTP (por ejemplo, FileZilla o Cyberduck en un ordenador).

1. En **Ajustes -> Compartir -> Conexiones**, asegurate de que **Otras apps y dispositivos** esta activado.
2. Toca **Iniciar** y anota la direccion **FTP**.
3. En tu app de FTP, anade una conexion nueva con esa direccion.
4. Introduce el usuario y la contrasena si definiste alguno, o dejalos vacios para el acceso anonimo.

## Transferir por cable USB (Mac, sin necesidad de Wi-Fi)

Usa esto cuando no haya Wi-Fi, o cuando quieras la transferencia mas rapida y privada. Solo funciona con un **Mac**.

1. Conecta tu iPhone o iPad al Mac con el cable de carga habitual.
2. Si el dispositivo te lo pide, toca **Confiar en este ordenador**.
3. En Everdisk, toca **Iniciar**. Aparece un aviso de **Conexion rapida disponible** y la pantalla de Compartir muestra una direccion adicional con una insignia de **Conexion por cable** que termina en `.local`.
4. En el Mac, abre Finder -> **Ir -> Conectar al servidor** (**Cmd+K**) e introduce esa direccion `.local` (sirve tanto para la conexion de Navegador como para la de Ordenador).
5. Tu dispositivo se abre a traves del cable, mas rapido que por Wi-Fi, y los datos nunca pasan por el router ni por internet.

Notas:

- Usa el **nombre `.local`**, no una direccion IP (las direcciones IP solo funcionan por Wi-Fi), y nunca `localhost`.
- La conexion por cable es **solo para Mac**. Los PC con Windows y los dispositivos Android tienen que usar Wi-Fi.
- Tambien puedes arrastrar archivos a la carpeta de Everdisk con Finder en un Mac, o con la app Dispositivos Apple (o iTunes) en Windows, mediante el uso compartido de archivos estandar de iOS.

## Siguientes pasos

- [Acceso y privacidad](/docs/guide/everdisk/everdisk-guide-access): anade una contrasena, permite subidas, bloquea un dispositivo.
- [Fotos, musica y video](/docs/guide/everdisk/everdisk-guide-media): comparte toda tu biblioteca y ajusta la calidad.
- [Conectarse a servidores](/docs/guide/everdisk/everdisk-guide-devices): accede a otros dispositivos desde Everdisk.
