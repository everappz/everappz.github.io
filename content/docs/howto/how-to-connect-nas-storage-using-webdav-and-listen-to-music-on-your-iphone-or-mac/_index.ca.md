---
title: "Com connectar l'emmagatzematge NAS mitjançant WebDAV i escoltar música al vostre iPhone o Mac"
date: 2024-07-28
description: "Apreneu a configurar WebDAV al vostre Synology NAS i reproduir música en streaming al vostre iPhone o Mac amb Evermusic o Flacbox. Seguiu la nostra guia pas a pas."
keywords: ["connectar nas", "webdav synology", "streaming música nas", "evermusic webdav", "flacbox webdav", "webdav iphone", "webdav mac"]
tags: ["música", "streaming", "emmagatzematge", "nas", "connectar", "webdav"]
readingTime: 2
---

{{< author-byline >}}


**Resum:** Instal·leu i activeu WebDAV al vostre Synology NAS, configureu els permisos de la carpeta compartida i connecteu-vos des d'Evermusic o Flacbox utilitzant l'adreça IP del NAS i el port WebDAV (per defecte 5005/5006). Podeu reproduir en streaming i gestionar tota la vostra biblioteca musical sense copiar fitxers al vostre dispositiu.

Descobriu com connectar el vostre emmagatzematge NAS mitjançant WebDAV i reproduir en streaming la vostra biblioteca musical al vostre iPhone o Mac sense esforç. WebDAV (Web-based Distributed Authoring and Versioning) és un protocol que us permet gestionar i compartir fitxers per Internet. En configurar WebDAV al vostre NAS, podeu accedir i reproduir en streaming la vostra col·lecció musical, assegurant que sempre tingueu les vostres cançons preferides a l'abast.

En aquesta guia, us mostrarem com configurar una connexió WebDAV en un dels servidors NAS més populars, Synology NAS. Seguiu els nostres passos senzills per configurar WebDAV al vostre Synology NAS, i podreu navegar, reproduir en streaming i gestionar la vostra biblioteca musical directament des del vostre iPhone o Mac.

## Pas 1: Instal·lar WebDAV a Synology NAS

1. Inicieu sessió al vostre Synology NAS i obriu el **Centre de paquets**.
2. Cerqueu "webdav" i instal·leu el paquet WebDAV si encara no està instal·lat. Obriu el servidor WebDAV per configurar-lo.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_1d6c299738f34ab6bf6444d0180d7a17~mv2.png" alt="Instal·lar WebDAV a Synology" width="600" >}}

## Pas 2: Configurar el servidor WebDAV

1. A la pàgina de configuració de WebDAV, marqueu les caselles per **Activar HTTP**, **Activar HTTPS**, **Activar WebDAV anònim** i **Activar DavDepthInfinity**.
2. Feu clic a **Aplicar** per desar els canvis. Anoteu els números de port per a les connexions HTTP i HTTPS, que són 5005 i 5006 per defecte.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_61268a79aab046fdb50bf0e24495958b~mv2.png" alt="Configurar els paràmetres de WebDAV" width="600" >}}

## Pas 3: Configurar els permisos de la carpeta compartida

1. Obriu el **Tauler de control** i aneu a la secció **Carpeta compartida**.
2. Seleccioneu la carpeta **Música** i feu clic a **Editar**.
3. A la pestanya **Permisos**, configureu els permisos. Activeu l'accés de convidat amb només lectura si només necessiteu escoltar música, o lectura/escriptura si necessiteu modificar fitxers. Deseu els canvis.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_599ebfa896164704ba4497524286ea58~mv2.png" alt="Permisos de la carpeta compartida" width="600" >}}

## Pas 4: Trobar l'adreça IP del Synology NAS

1. Obriu el **Tauler de control** i aneu a la pestanya **Interfície de xarxa**, o utilitzeu el vostre navegador web per visitar [find.synology.com](http://find.synology.com).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_51839801a6f44035b08b3a4b7d33f142~mv2.png" alt="Trobar l'adreça IP del NAS" width="600" >}}

2. Anoteu l'adreça IP del vostre Synology NAS (p. ex., 192.168.18.137).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_5bfb1db8e04d4eddb8ff5238f8b214da~mv2.png" alt="Adreça IP del Synology NAS" width="600" >}}

## Pas 5: Connectar-se a Synology NAS amb Evermusic/Flacbox

1. Obriu l'aplicació Evermusic o Flacbox i aneu a la pestanya **Connexions**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_d2dedf2cc0614bbe818f89e9d165411c~mv2.png" alt="Pestanya Connexions a Evermusic" width="600" >}}

2. Per a la connexió automàtica, trobeu el vostre Synology NAS a la secció **Dispositius disponibles** i toqueu-lo per connectar-vos.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7536b0b169674a9199784da275b1cf6b~mv2.png" alt="Llista de dispositius disponibles" width="600" >}}

3. Per a la connexió manual, trieu **Connectar un servei al núvol** i seleccioneu **WebDAV**. Introduïu l'adreça del servidor en el format: PROTOCOL_NAME://IP_ADDRESS:PORT_NUMBER (p. ex., [https://192.168.18.137:5006](https://192.168.18.137:5006)).

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_45ecc52850874ca18d7be50d086365fc~mv2.png" alt="Configuració manual de WebDAV" width="600" >}}

4. Deixeu els camps d'inici de sessió i contrasenya buits per a l'accés de convidat, o introduïu les vostres credencials de Synology. Toqueu **Iniciar sessió**.

## Pas 6: Navegar i reproduir música

1. Un cop connectat, el dispositiu apareixerà a la llista d'**Accessoris connectats**.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_2cadbe057eed4e0eba098b767014de29~mv2.png" alt="Dispositius connectats a Evermusic" width="600" >}}

2. Navegueu fins a la carpeta **Música** i toqueu qualsevol fitxer d'àudio per iniciar la reproducció.

{{< figure src="/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac/21260c_7a9da6bb9cef4585a7cc76839283d3a5~mv2.png" alt="Navegant per la carpeta de música" width="600" >}}

## Pas 7: Afegir la carpeta al núvol connectada a la biblioteca musical

1. Obriu la secció **Biblioteca musical** a l'aplicació.
2. Trieu **Afegir música** i seleccioneu **Connexions**.
3. Trieu el vostre servidor NAS connectat i seleccioneu la carpeta **Música**. Toqueu **Fet**.
4. L'aplicació escanejarà la carpeta de música i afegirà els fitxers d'àudio compatibles a la biblioteca musical. Es carregaran les metadades i les vostres pistes s'agruparan per àlbum, artista i gènere.

## Conclusió

Seguint aquests passos, podeu configurar fàcilment una connexió WebDAV al vostre Synology NAS i reproduir en streaming la vostra biblioteca musical al vostre iPhone o Mac amb Evermusic o Flacbox. Gaudiu d'un accés fluid a les vostres cançons preferides en qualsevol moment.

## Preguntes freqüents

{{% details title="Quins dispositius NAS suporten WebDAV?" closed="true" %}}
La majoria de marques populars de NAS suporten WebDAV, incloent Synology, QNAP, TrueNAS i Western Digital. Consulteu la documentació del fabricant del vostre NAS per a les instruccions de configuració de WebDAV.
{{% /details %}}

{{% details title="Quina diferència hi ha entre WebDAV i SMB per al streaming de música des de NAS?" closed="true" %}}
WebDAV funciona sobre HTTP/HTTPS i és més adequat per a l'accés remot per Internet. SMB és normalment més ràpid en xarxes locals. Evermusic i Flacbox suporten ambdós protocols, així que trieu segons si necessiteu accés local o remot.
{{% /details %}}

{{% details title="Necessito un nom d'usuari i contrasenya per a WebDAV a Synology?" closed="true" %}}
No, si activeu l'accés anònim a WebDAV i configureu els permisos de convidat a la carpeta compartida. Per a una millor seguretat, podeu utilitzar les vostres credencials de Synology.
{{% /details %}}

{{% details title="Puc reproduir en streaming FLAC i altres formats d'alta resolució des de NAS via WebDAV?" closed="true" %}}
Sí. Tant Evermusic com Flacbox suporten FLAC, ALAC, WAV, DSD i altres formats d'alta resolució quan es reprodueixen en streaming des de l'emmagatzematge NAS via WebDAV.
{{% /details %}}

{{% details title="Per què l'aplicació no pot trobar el meu NAS a Dispositius disponibles?" closed="true" %}}
Assegureu-vos que el vostre iPhone/Mac i el NAS estiguin a la mateixa xarxa Wi-Fi. Si la descoberta automàtica no funciona, utilitzeu l'opció de connexió manual i introduïu l'adreça IP del NAS i el port WebDAV directament.
{{% /details %}}
