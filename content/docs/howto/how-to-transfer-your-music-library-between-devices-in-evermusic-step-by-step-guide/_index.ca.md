---
title: "Com transferir la teva biblioteca musical entre dispositius a Evermusic: guia pas a pas"
description: "Transfereix fàcilment la teva biblioteca musical d'Evermusic, llistes de reproducció, caràtules d'àlbums i configuració d'un iPhone, iPad o Mac a un altre utilitzant Wi-Fi Drive i eines de còpia de seguretat."
date: 2024-12-29
tags: ["biblioteca musical", "transferència", "wifi", "còpia de seguretat", "webdav", "restauració"]
keywords: ["transferir biblioteca musical Evermusic", "còpia de seguretat i restauració llistes de reproducció Evermusic", "Evermusic WiFi Drive", "sincronitzar Evermusic entre dispositius", "moure base de dades Evermusic", "transferència de fitxers Evermusic", "restaurar configuració del reproductor d'àudio", "transferència de música WebDAV iOS"]
readingTime: 3
---

{{< author-byline >}}


**Resum:** Per transferir la teva biblioteca d'Evermusic a un nou dispositiu, crea una còpia de seguretat al dispositiu d'origen, inicia Wi-Fi Drive, connecta el segon dispositiu a la mateixa xarxa, descarrega la còpia de seguretat i els fitxers de música, i després restaura des de la còpia de seguretat. Tot el procés dura uns 10 minuts depenent de la mida de la biblioteca.

En aquesta guia, et guiarem a través de la transferència de tota la teva biblioteca musical — incloent base de dades, caràtules d'àlbums i configuració — d'un dispositiu (iPhone o Mac) a un altre. Tot i que la sincronització automàtica de la biblioteca musical i les llistes de reproducció és una funció prevista per al futur, aquest procés s'ha de fer manualment de moment.

## Pas 1: Crear una còpia de seguretat al primer dispositiu

1. **Obre l'aplicació al teu primer dispositiu** (el que té la teva biblioteca musical, llistes de reproducció i serveis al núvol connectats).
2. **Navega a Configuració** i selecciona l'opció **Còpia de seguretat i restauració**.

![Còpia de seguretat i restauració](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_44dbabc06ba844c0b665f17ac01fec84~mv2.png)

3. A la pantalla de **Còpia de seguretat i restauració**, tria els elements a incloure al fitxer de còpia de seguretat:
   - **Base de dades** (inclou la teva biblioteca musical i llistes de reproducció)
   - **Caràtules d'àlbums**
   - **Configuració**

Aquestes opcions estan activades per defecte.

![Opcions de còpia de seguretat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_160d11e81b104384a5fef09ae196c260~mv2.png)

4. Toca **Còpia de seguretat de les dades de l'aplicació** per començar el procés.

![Còpia de seguretat de les dades de l'aplicació](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_5bab30ce6d7b4fcf8b67ad6bd18b5f21~mv2.png)

5. Un cop completada la còpia de seguretat, apareixerà una alerta informativa.

![Còpia de seguretat completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_cc751d3e710941479102d286d0504a80~mv2.png)

Toca **Mostrar fitxer** per revelar el fitxer de còpia de seguretat al directori **Documents**. Els fitxers de còpia de seguretat normalment es guarden a la carpeta **Backup**.

![Mostrar fitxer de còpia de seguretat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_d857f23f0ad94ae8851f93baed15aeb1~mv2.png)

## Pas 2: Iniciar el servidor Wi-Fi Drive

1. Ves a la secció **Connexions** de l'aplicació.
2. Desplaça't cap avall fins a **Connectar via Wi-Fi** i toca-ho.

![Connectar via Wi-Fi](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_7241696cb6a54f8d95d15cb9592bbeed~mv2.png)

3. A la pantalla següent, toca **Iniciar Wi-Fi Drive**.

- Opcionalment, pots establir un nom d'usuari i contrasenya per seguretat, però no és necessari per a xarxes domèstiques.

4. Un cop iniciat, veuràs les adreces del servidor disponibles. Això es pot utilitzar per a navegadors d'escriptori o aplicacions WebDAV, però en aquesta guia, procedirem directament als passos següents.

![Wi-Fi Drive iniciat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_11ed60c4073640cc9aafda20cec8431c~mv2.png)

## Pas 3: Connectar el teu segon dispositiu al primer

1. Obre l'aplicació al teu segon dispositiu (on vols transferir la biblioteca).
2. Assegura't que ambdós dispositius estiguin connectats a la mateixa xarxa Wi-Fi.
3. Al segon dispositiu, obre la pestanya **Connexions** i selecciona **Dispositius disponibles**.

![Dispositius disponibles](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_4d9abdd7dd80409caabfeca89535754d~mv2.png)

4. Hauries de veure una connexió WebDAV anomenada **Evermusic** (el servidor que hem iniciat al primer dispositiu). Toca-la per connectar.

5. Un cop connectat, veuràs totes les carpetes del primer dispositiu.

![Connectat al primer dispositiu](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_3075c7ee8dfb41f6a2496f8be0673d37~mv2.png)

## Pas 4: Preparar-se per a la transferència de fitxers

1. Al segon dispositiu, ves a **Configuració > Gestor de fitxers** i activa **Desar fitxers descarregats a - Preguntar cada vegada**.

- Això assegura que puguis seleccionar la carpeta de destinació per a cada descàrrega.

2. Torna a la pestanya **Connexions** i navega al servidor WebDAV connectat.

![Preparar per a la transferència de fitxers](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_fb325a9cc68d419389ee76cd19b821d5~mv2.png)

## Pas 5: Transferir la còpia de seguretat i els fitxers de música

1. Obre la carpeta **Backup** al servidor WebDAV connectat.

![Carpeta de còpia de seguretat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_91254ba6f64649adbc8a759899a8618a~mv2.png)

2. Toca el botó **Més accions** (tres punts) al costat del fitxer de còpia de seguretat i selecciona **Descarregar**.

3. Crea una carpeta **Backup** al segon dispositiu per emmagatzemar els fitxers descarregats. Confirma la teva selecció tocant **Fet**.

![Descarregar còpia de seguretat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ffd617db2ab64bbcb580b70aa94fe3df~mv2.png)

4. Transfereix qualsevol fitxer de música addicional:
   - Comprova la carpeta **Descarregues** o altres carpetes rellevants al servidor WebDAV.

![Transferir fitxers de música](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_6536aba207bc4ff98af139f7dc8a2f45~mv2.png)

- Utilitza l'opció **Seleccionar** per triar fitxers, després toca **Més accions > Descarregar**. Desa'ls a la carpeta corresponent al segon dispositiu per mantenir la mateixa estructura de directoris.

L'objectiu és transferir tots els fitxers del teu primer dispositiu al dispositiu actual, assegurant que l'estructura de carpetes es mantingui idèntica. D'aquesta manera, els enllaços a la teva biblioteca musical i llistes de reproducció es mantenen intactes. Tingues en compte que els fitxers locals emmagatzemats fora del directori Documents de l'aplicació al teu primer dispositiu s'han de transferir per separat. Com que l'aplicació no pot accedir a aquests fitxers en mode Wi-Fi Drive, hauràs d'utilitzar l'aplicació Fitxers del sistema per a la seva transferència.

![Transferència completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_352edb4aeb584d53b8646d7bf779de02~mv2.png)

## Pas 6: Monitoritzar el progrés de la transferència

1. Al segon dispositiu, ves a la secció **Fitxers locals** (o pestanya **Descarregues** a iPad/Mac).

2. Toca el botó **Activitat de transferència** a la cantonada superior esquerra per monitoritzar la cua de transferència.

![Monitoritzar transferència](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_82c35eccb18245fe8e1135ab86532a52~mv2.png)

## Pas 7: Restaurar dades des de la còpia de seguretat

1. Un cop el fitxer de còpia de seguretat i tots els fitxers d'àudio necessaris s'hagin descarregat al segon dispositiu, obre la carpeta **Backup**.

2. Toca el fitxer de còpia de seguretat, i apareixerà un missatge de confirmació.

![Restaurar còpia de seguretat](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_480c20fc3d664307b135881d04444fb5~mv2.png)

- **Nota:** La restauració reemplaçarà totes les dades actuals de la biblioteca musical, llistes de reproducció, configuració i caràtules d'àlbums amb les dades de la còpia de seguretat.

3. Toca **Restaurar** per començar el procés.

![Procés de restauració](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_469647cffde34ae7a448f7928d1436a9~mv2.png)

4. Després de completar la restauració, una alerta confirmarà l'èxit.

![Restauració completada](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_c6ca2dc848b64a26a30b511e9e4b79cd~mv2.png)

Comprova les seccions **Llistes de reproducció** o **Biblioteca musical** per verificar la restauració.

![Verificar restauració](/docs/howto/how-to-transfer-your-music-library-between-devices-in-evermusic-step-by-step-guide/21260c_ff3f96fe50f845b392ef24f2de03a794~mv2.png)

## Pas 8: Reindexar la biblioteca musical

1. Per obtenir els millors resultats, reindexa la teva biblioteca per assegurar-te que tots els fitxers es detectin correctament.

2. Ves a **Configuració > Biblioteca musical > Sincronització de música fora de línia** i selecciona **Iniciar escaneig de carpetes locals**.

Seguint aquests passos, transferiràs amb èxit la teva biblioteca musical, llistes de reproducció i configuració a un altre dispositiu. Si trobes algun problema, no dubtis a contactar per obtenir suport.

## Preguntes freqüents

{{% details title="Puc transferir la meva biblioteca d'Evermusic sense Wi-Fi?" closed="true" %}}
Wi-Fi Drive requereix que ambdós dispositius estiguin a la mateixa xarxa Wi-Fi. Actualment no hi ha opció de transferència per Bluetooth o dades mòbils. Alternativament, pots utilitzar AirDrop o l'aplicació Fitxers per moure manualment el fitxer de còpia de seguretat i les carpetes de música entre dispositius.
{{% /details %}}

{{% details title="Es transferiran les connexions als serveis al núvol amb la còpia de seguretat?" closed="true" %}}
La còpia de seguretat inclou la teva base de dades, llistes de reproducció, caràtules d'àlbums i configuració. Les credencials d'inici de sessió dels serveis al núvol no s'inclouen per raons de seguretat. Hauràs de reconnectar els teus comptes al núvol al nou dispositiu després de la restauració.
{{% /details %}}

{{% details title="Què passa amb la meva biblioteca existent al segon dispositiu?" closed="true" %}}
Restaurar una còpia de seguretat reemplaça totes les dades existents de la biblioteca musical, llistes de reproducció, configuració i caràtules d'àlbums al segon dispositiu. Fes una còpia de seguretat separada del segon dispositiu primer si vols preservar les seves dades.
{{% /details %}}

{{% details title="Funciona aquest procés entre iPhone i Mac?" closed="true" %}}
Sí. Evermusic suporta la transferència Wi-Fi Drive entre qualsevol combinació d'iPhone, iPad i Mac. Ambdós dispositius només han d'estar a la mateixa xarxa Wi-Fi.
{{% /details %}}

{{% details title="Quant de temps triga la transferència?" closed="true" %}}
El temps de transferència depèn de la mida de la teva biblioteca musical i la velocitat del teu Wi-Fi. Una biblioteca típica d'uns quants gigabytes es transfereix en 5-15 minuts a través d'una xarxa domèstica estàndard.
{{% /details %}}
