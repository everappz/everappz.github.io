---
title: "Cómo transferir tu biblioteca musical entre dispositivos en Evermusic: guía paso a paso"
description: "Transfiere fácilmente tu biblioteca musical de Evermusic, listas de reproducción, carátulas de álbumes y ajustes de un iPhone, iPad o Mac a otro usando Wi-Fi Drive y herramientas de copia de seguridad."
date: 2024-12-29
tags: ["biblioteca musical", "transferencia", "wifi", "copia de seguridad", "webdav", "restauración"]
keywords: ["transferir biblioteca musical Evermusic", "copia de seguridad y restauración listas de reproducción Evermusic", "Evermusic WiFi Drive", "sincronizar Evermusic entre dispositivos", "mover base de datos Evermusic", "transferencia de archivos Evermusic", "restaurar ajustes del reproductor de audio", "transferencia de música WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Resumen:** Para transferir tu biblioteca de Evermusic a un nuevo dispositivo, crea una copia de seguridad en el dispositivo de origen, inicia Wi-Fi Drive, conecta el segundo dispositivo a la misma red, descarga la copia de seguridad y los archivos de música, y luego restaura desde la copia de seguridad. Todo el proceso toma aproximadamente 10 minutos dependiendo del tamaño de la biblioteca.

En esta guía, te guiaremos a través de la transferencia de toda tu biblioteca musical — incluyendo base de datos, carátulas de álbumes y ajustes — de un dispositivo (iPhone o Mac) a otro. Mientras que la sincronización automática de la biblioteca musical y las listas de reproducción es una función planeada para el futuro, este proceso debe realizarse manualmente por el momento.

## Paso 1: Crear una copia de seguridad en el primer dispositivo

1. **Abre la app en tu primer dispositivo** (el que tiene tu biblioteca musical, listas de reproducción y servicios en la nube conectados).
2. **Navega a Ajustes** y selecciona la opción **Copia de seguridad y restauración**.

![Copia de seguridad y restauración](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. En la pantalla de **Copia de seguridad y restauración**, elige los elementos a incluir en tu archivo de copia de seguridad:
   - **Base de datos** (incluye tu biblioteca musical y listas de reproducción)
   - **Carátulas de álbumes**
   - **Ajustes**

Estas opciones están habilitadas por defecto.

![Opciones de copia de seguridad](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Toca **Copia de seguridad de datos de la aplicación** para comenzar el proceso.

![Copia de seguridad de datos de la aplicación](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Una vez completada la copia de seguridad, aparecerá una alerta informativa.

![Copia de seguridad completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Toca **Mostrar archivo** para revelar el archivo de copia de seguridad en el directorio **Documentos**. Los archivos de copia de seguridad normalmente se guardan en la carpeta **Backup**.

![Mostrar archivo de copia de seguridad](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Paso 2: Iniciar el servidor Wi-Fi Drive

1. Ve a la sección **Conexiones** en la app.
2. Desplázate hacia abajo hasta **Conectar vía Wi-Fi** y tócalo.

![Conectar vía Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. En la siguiente pantalla, toca **Iniciar Wi-Fi Drive**.

- Opcionalmente, puedes establecer un nombre de usuario y contraseña por seguridad, pero no es necesario para redes domésticas.

4. Una vez iniciado, verás las direcciones del servidor disponibles. Esto se puede usar para navegadores de escritorio o apps WebDAV, pero en esta guía, procederemos directamente a los siguientes pasos.

![Wi-Fi Drive iniciado](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Paso 3: Conectar tu segundo dispositivo al primero

1. Abre la app en tu segundo dispositivo (donde quieres transferir la biblioteca).
2. Asegúrate de que ambos dispositivos estén conectados a la misma red Wi-Fi.
3. En el segundo dispositivo, abre la pestaña **Conexiones** y selecciona **Dispositivos disponibles**.

![Dispositivos disponibles](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Deberías ver una conexión WebDAV llamada **Evermusic** (el servidor que iniciamos en el primer dispositivo). Tócala para conectar.

5. Una vez conectado, verás todas las carpetas del primer dispositivo.

![Conectado al primer dispositivo](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Paso 4: Prepararse para la transferencia de archivos

1. En el segundo dispositivo, ve a **Ajustes > Gestor de archivos** y habilita **Guardar archivos descargados en - Preguntar cada vez**.

- Esto asegura que puedas seleccionar la carpeta de destino para cada descarga.

2. Regresa a la pestaña **Conexiones** y navega al servidor WebDAV conectado.

![Preparar transferencia de archivos](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Paso 5: Transferir la copia de seguridad y los archivos de música

1. Abre la carpeta **Backup** en el servidor WebDAV conectado.

![Carpeta de copia de seguridad](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Toca el botón **Más acciones** (tres puntos) junto al archivo de copia de seguridad y selecciona **Descargar**.

3. Crea una carpeta **Backup** en el segundo dispositivo para almacenar los archivos descargados. Confirma tu selección tocando **Hecho**.

![Descargar copia de seguridad](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transfiere archivos de música adicionales:
   - Revisa la carpeta **Descargas** u otras carpetas relevantes en el servidor WebDAV.

![Transferir archivos de música](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Usa la opción **Seleccionar** para elegir archivos, luego toca **Más acciones > Descargar**. Guárdalos en la carpeta correspondiente en el segundo dispositivo para mantener la misma estructura de directorios.

El objetivo es transferir todos los archivos de tu primer dispositivo a tu dispositivo actual, asegurando que la estructura de carpetas permanezca idéntica. De esta manera, los enlaces en tu biblioteca musical y listas de reproducción se mantienen intactos. Ten en cuenta que los archivos locales almacenados fuera del directorio Documentos de la app en tu primer dispositivo deben transferirse por separado. Como la app no puede acceder a estos archivos en modo Wi-Fi Drive, necesitarás usar la app Archivos del sistema para su transferencia.

![Transferencia completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Paso 6: Monitorear el progreso de la transferencia

1. En el segundo dispositivo, ve a la sección **Archivos locales** (o pestaña **Descargas** en iPad/Mac).

2. Toca el botón **Actividad de transferencia** en la esquina superior izquierda para monitorear la cola de transferencia.

![Monitorear transferencia](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Paso 7: Restaurar datos desde la copia de seguridad

1. Una vez que el archivo de copia de seguridad y todos los archivos de audio necesarios se hayan descargado en el segundo dispositivo, abre la carpeta **Backup**.

2. Toca el archivo de copia de seguridad, y aparecerá un mensaje de confirmación.

![Restaurar copia de seguridad](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Nota:** La restauración reemplazará todos los datos actuales de la biblioteca musical, listas de reproducción, ajustes y carátulas de álbumes con los datos de la copia de seguridad.

3. Toca **Restaurar** para comenzar el proceso.

![Proceso de restauración](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Después de completar la restauración, una alerta confirmará el éxito.

![Restauración completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Revisa las secciones **Listas de reproducción** o **Biblioteca musical** para verificar la restauración.

![Verificar restauración](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Paso 8: Reindexar la biblioteca musical

1. Para mejores resultados, reindexa tu biblioteca para asegurar que todos los archivos se detecten correctamente.

2. Ve a **Ajustes > Biblioteca musical > Sincronización de música sin conexión** y selecciona **Iniciar escaneo de carpetas locales**.

Siguiendo estos pasos, transferirás con éxito tu biblioteca musical, listas de reproducción y ajustes a otro dispositivo. Si encuentras algún problema, no dudes en contactar el soporte.

## Preguntas frecuentes

{{% details title="¿Puedo transferir mi biblioteca de Evermusic sin Wi-Fi?" closed="true" %}}
Wi-Fi Drive requiere que ambos dispositivos estén en la misma red Wi-Fi. Actualmente no hay opción de transferencia por Bluetooth o datos móviles. Alternativamente, puedes usar AirDrop o la app Archivos para mover manualmente el archivo de copia de seguridad y las carpetas de música entre dispositivos.
{{% /details %}}

{{% details title="¿Se transferirán las conexiones de servicios en la nube con la copia de seguridad?" closed="true" %}}
La copia de seguridad incluye tu base de datos, listas de reproducción, carátulas de álbumes y ajustes. Las credenciales de inicio de sesión de servicios en la nube no se incluyen por razones de seguridad. Necesitarás reconectar tus cuentas en la nube en el nuevo dispositivo después de la restauración.
{{% /details %}}

{{% details title="¿Qué pasa con mi biblioteca existente en el segundo dispositivo?" closed="true" %}}
Restaurar una copia de seguridad reemplaza todos los datos existentes de la biblioteca musical, listas de reproducción, ajustes y carátulas de álbumes en el segundo dispositivo. Haz una copia de seguridad separada del segundo dispositivo primero si quieres preservar sus datos.
{{% /details %}}

{{% details title="¿Funciona este proceso entre iPhone y Mac?" closed="true" %}}
Sí. Evermusic soporta la transferencia Wi-Fi Drive entre cualquier combinación de iPhone, iPad y Mac. Ambos dispositivos solo necesitan estar en la misma red Wi-Fi.
{{% /details %}}

{{% details title="¿Cuánto tiempo toma la transferencia?" closed="true" %}}
El tiempo de transferencia depende del tamaño de tu biblioteca musical y tu velocidad de Wi-Fi. Una biblioteca típica de unos pocos gigabytes se transfiere en 5-15 minutos a través de una red doméstica estándar.
{{% /details %}}
