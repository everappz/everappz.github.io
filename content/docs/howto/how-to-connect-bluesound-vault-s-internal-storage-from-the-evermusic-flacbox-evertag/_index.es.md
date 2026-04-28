---
title: "Cómo conectar el almacenamiento interno del Bluesound VAULT desde Evermusic, Flacbox, Evertag"
date: 2022-03-10
description: "Aprenda cómo acceder al disco duro interno del Bluesound VAULT desde Evermusic, Flacbox y Evertag utilizando el protocolo SMB para gestionar, editar y reproducir archivos de audio."
keywords: ["bluesound vault", "conectar almacenamiento smb", "evermusic smb", "flacbox vault", "evertag smb", "almacenamiento nas música", "unidad interna vault"]
tags: ["evermusic", "conectar", "bluesound vault"]
readingTime: 1
---

{{< author-byline >}}


**Resumen:** Conéctese al almacenamiento interno de su Bluesound VAULT a través de SMB usando Evermusic, Flacbox o Evertag. Encuentre la dirección IP del VAULT en la aplicación BluOS, ingrésela como conexión SMB con acceso de invitado y comience a reproducir o gestionar sus archivos de música.

El Bluesound VAULT tiene un disco duro interno y funciona como un almacenamiento conectado a la red (NAS). Acceder al disco duro interno del VAULT le permite agregar/eliminar archivos, editar etiquetas de metadatos desde nuestras aplicaciones Evermusic, Flacbox, Evertag.

**A continuación se muestran los pasos para acceder al disco duro interno de su VAULT:**

1. En la aplicación BluOS, seleccione **Ayuda > Diagnósticos**.

2. Desde la página de **Diagnósticos**, obtenga la **Dirección IP** del VAULT. Esta **Dirección IP** se usará en los siguientes pasos.

3. Abra Evermusic, Flacbox o Evertag.

   ![Aplicaciones Everappz](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_fba6c71e08a34c2ca755fd4e3b21ee6d~mv2.jpg)

4. Abra la pantalla "Conexiones" y seleccione el elemento de menú "Conectar un servicio en la nube".

   ![Pantalla de Conexiones de Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_3828fec0f2794cfb84e43db5344bfe33~mv2.png)

5. Seleccione el servicio en la nube "SMB".

   ![Pantalla de Conectar un Servicio en la Nube de Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_41d5a37fc4004e47875983cf450b25ea~mv2.png)

6. En la "Pantalla de configuración SMB" ingrese la URL en el siguiente formato:

   ```
   SMB://<<VAULT-IP>>
   ```

   Reemplace `<<VAULT-IP>>` con la **Dirección IP** obtenida en el Paso 2.

   **Nota:** Deje los campos de Inicio de sesión y Contraseña en blanco porque el almacenamiento VAULT admite el modo INVITADO.

   ![Pantalla de conexión SMB de Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_f8fc082181d34a97aabc07f766cfc0a9~mv2.png)

7. Toque el botón "Iniciar sesión" para guardar la configuración.

8. Abra el almacenamiento en la nube conectado, navegue dentro de la carpeta con archivos de audio y toque cualquier archivo para iniciar el reproductor de audio.

   ![Pantalla de servidor SMB abierto de Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_7995f7c14e0d457e9a41b0bebe9838ce~mv2.png)

9. También puede editar archivos usando el administrador de archivos integrado.

   ![Pantalla del Administrador de Archivos de Evermusic](/docs/howto/how-to-connect-bluesound-vault-s-internal-storage-from-the-evermusic-flacbox-evertag/21260c_d925743af9384755a17b699b304d70af~mv2.png)

Con estos sencillos pasos, puede acceder fácilmente al disco duro interno de su Bluesound VAULT y tomar el control de su biblioteca de música usando Evermusic, Flacbox o Evertag.

## Preguntas frecuentes

{{% details title="¿Necesito un nombre de usuario y contraseña para conectarme al Bluesound VAULT?" closed="true" %}}
No. El Bluesound VAULT admite acceso de invitado (anónimo) a través de SMB. Deje los campos de Inicio de sesión y Contraseña en blanco al configurar la conexión.
{{% /details %}}

{{% details title="¿Puedo editar etiquetas de música en el Bluesound VAULT?" closed="true" %}}
Sí. Usando Evertag, puede editar etiquetas de metadatos (título, artista, álbum, etc.) de archivos de audio almacenados directamente en el disco duro interno del VAULT.
{{% /details %}}

{{% details title="¿Qué protocolos admite el Bluesound VAULT?" closed="true" %}}
El Bluesound VAULT expone su almacenamiento interno a través de SMB (Server Message Block). Evermusic, Flacbox y Evertag admiten conexiones SMB, lo que facilita la conexión.
{{% /details %}}

{{% details title="¿Puedo transmitir música desde el VAULT sin copiar archivos a mi iPhone?" closed="true" %}}
Sí. Una vez conectado a través de SMB, puede transmitir archivos de audio directamente desde la unidad interna del VAULT sin copiarlos a su dispositivo.
{{% /details %}}
