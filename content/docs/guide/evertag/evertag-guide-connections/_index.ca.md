---
title: "Connexions"
date: 2020-02-01
description: "Aprèn a connectar emmagatzematge al núvol, NAS i el teu ordinador a Evertag. Accedeix i edita fitxers d'àudio directament des de l'emmagatzematge al núvol, NAS personal o Mac/PC."
keywords: [
  "configuració al núvol Evertag", "connectar iCloud a Evertag", "accés a fitxers SMB iOS",
  "editor d'etiquetes d'àudio WebDAV", "edició de metadades NAS", "Wi-Fi Drive Evertag",
  "transferir fitxers d'àudio a iPhone", "iTunes File Sharing Evertag", "editar etiquetes FLAC des del núvol"
]
tags: ["guia", "evertag", "connexions"]
readingTime: 11
---


En aquesta pantalla, pots connectar diverses fonts que contenen els teus fitxers d'àudio. Pots integrar serveis populars al núvol com Google Drive, Dropbox, OneDrive, iCloud i d'altres, així com connectar el teu Mac o PC. A més, tens l'opció d'editar fitxers d'àudio ubicats a Apple Time Capsule, WD Cloud Home o qualsevol NAS compatible amb SMB o WebDAV.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Connexions d'Evertag" image="/docs/guide/evertag/img/connections.webp" >}}
{{< /cards >}}

## Accés ràpid

A la part superior de la pantalla de Connexions trobaràs una llista d'**Accés ràpid**. Qualsevol carpeta al núvol que afegeixis als favorits — fins i tot una enterrada a diversos nivells de profunditat — apareix aquí perquè puguis accedir-hi sense navegar per les carpetes principals cada vegada.

## Connectar a l'emmagatzematge al núvol

- Obre la pestanya 'Connexions'  
- Selecciona 'Connectar a l'emmagatzematge al núvol' del menú  
- Tria un servei d'emmagatzematge al núvol de la llista  
- Introdueix les teves credencials i toca 'Fet'.

Si trobes algun problema, assegura't de comprovar la connexió a Internet i el nom d'usuari/contrasenya.  
A la versió Premium de l'aplicació, pots afegir un nombre il·limitat de serveis.

## Serveis d'emmagatzematge al núvol compatibles

Actualment, l'aplicació és compatible amb els serveis d'emmagatzematge al núvol més populars: iCloud Drive, Google Drive, Dropbox, OneDrive, Box, MEGA, Yandex.Disk, pCloud, Synology Drive, MediaFire, WD My Cloud Home, InfiniCLOUD (TeraCLOUD), HiDrive, OpenDrive, MyDrive, Put.io, Cloud Mail.ru, Baidu Pan (百度网盘), així com qualsevol servidor SMB o WebDAV.

## Seguretat i privadesa

Utilitzem només SDK oficials i connexions segures per interactuar amb els serveis al núvol connectats. El teu nom d'usuari i contrasenya no són accessibles per a l'aplicació. Totes les sol·licituds de l'aplicació al servei al núvol estan xifrades.

Quan introdueixes el teu nom d'usuari i contrasenya, l'aplicació et mostra la pàgina d'autorització oficial proporcionada pel proveïdor del servei al núvol, i tot el procés d'autorització es produeix fora de l'aplicació. El proveïdor del servei al núvol envia un token d'autenticació a l'aplicació després d'una autorització correcta, i aquest token s'utilitza per fer crides a l'API.

Un token d'autenticació és una clau digital que permet a les aplicacions de tercers interactuar amb l'emmagatzematge al núvol. El token d'autenticació s'emmagatzema al teu dispositiu en un emmagatzematge del sistema segur anomenat Keychain. Pots descarregar els teus fitxers del servei al núvol connectat al dispositiu, i aquests fitxers es col·locaran al directori "Documents" de l'aplicació. Pots eliminar aquests fitxers en qualsevol moment utilitzant el gestor de fitxers integrat.

L'aplicació no comparteix cap informació del compte al núvol connectat. Pots revocar l'accés al teu compte al núvol en qualsevol moment obrint la pàgina de configuració del compte al teu navegador web.

## Revocar el token d'autenticació

Inicia sessió al teu compte en un navegador web i navega fins a la pàgina de configuració. Allà, pots trobar totes les aplicacions de tercers connectades al teu compte al núvol i eliminar-ne qualsevol si ja no vols utilitzar aquella aplicació. Les instruccions detallades estan disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

També pots desconnectar els comptes al núvol connectats a l'aplicació, i el token d'autenticació també s'eliminarà del teu dispositiu. Si elimines l'aplicació del teu dispositiu, totes les dades descarregades i els tokens d'accés també s'eliminaran.

## Desconnectar un emmagatzematge al núvol o canviar la configuració

- Accedeix a les opcions d'emmagatzematge al núvol: primer, localitza l'emmagatzematge al núvol que vols gestionar a la interfície de l'aplicació.  
- Toca el botó '...': al costat del títol del servei, veuràs un botó '...'. Toca'l per accedir a opcions addicionals.  
  - **Reanomenar**: si vols canviar el nom del servei al núvol tal com apareix a la teva llista, selecciona 'Reanomenar'.  
  - **Configuració**: per modificar la configuració o les dades d'autenticació del servei al núvol, tria 'Configuració'. De vegades, pot ser necessari reautoritzar el servei al núvol connectat si el token d'autorització ha caducat.  
  - **Desconnectar**: si vols tallar completament la connexió entre l'aplicació i el servei al núvol, selecciona 'Desconnectar'. Tingues en compte que triar aquesta opció eliminarà totes les cançons associades a aquest servei al núvol de la teva biblioteca musical de l'aplicació, però romandran al servidor.

## Connectar a l'ordinador o NAS

També pots connectar el teu ordinador, NAS personal o altres dispositius de xarxa utilitzant el protocol SMB, DLNA o WebDAV.

## Connectar a l'ordinador mitjançant SMB

- Toca "Connectar a l'emmagatzematge al núvol" → SMB.  
- Introdueix l'adreça IP de l'ordinador i el nom de la carpeta compartida al camp URL utilitzant el format smb://computer-ip-address/shared-folder-name  
- Tria la versió del protocol: automàtic, SMB1, SMB2  
- Introdueix el nom d'usuari i la contrasenya (si és necessari)  
- Toca "Fet".

Si la connexió és correcta, veuràs l'emmagatzematge connectat a la secció "Emmagatzematge al núvol".  
Hi ha un tutorial complet sobre com connectar el teu Mac o PC mitjançant SMB disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connectar a NAS mitjançant WebDAV

Tots els passos són iguals excepte el camp URL.  
L'URL ha d'estar en el format http://server-name, o https://server-name si el servidor és compatible amb SSL.  
Hi ha un tutorial complet sobre com connectar NAS mitjançant el protocol WebDAV disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Dispositius disponibles

Aquesta secció mostra tots els dispositius de la teva xarxa local als quals pots connectar-te a través de l'aplicació.  
Per establir una connexió amb un dispositiu, segueix aquests passos:

- Obre l'aplicació i ves a la secció "Dispositius disponibles".  
- Toca el dispositiu al qual et vols connectar de la llista.  
- Si cal, introdueix les teves dades d'inici de sessió per completar la connexió.

## Wi-Fi Drive

Wi-Fi Drive és una tecnologia còmoda que permet transferències de fitxers sense fil des del teu ordinador al teu dispositiu iOS a través d'un navegador d'escriptori.  
Per utilitzar aquesta funció de manera eficaç, assegura't que el teu dispositiu i ordinador estiguin connectats a la mateixa xarxa Wi-Fi.  
Aquí tens una guia pas a pas sobre com utilitzar Wi-Fi Drive.

## Activar Wi-Fi Drive

- Obre l'aplicació i ves a la pestanya "Connexions".  
- Selecciona "Connectar via Wi-Fi" per accedir a la pantalla principal de Wi-Fi Drive.  
- Toca "Iniciar Wi-Fi Drive" per activar Wi-Fi Drive.

## Accedir a Wi-Fi Drive des del teu ordinador

- Al teu ordinador (d'escriptori o portàtil), obre un navegador web (com Chrome, Firefox o Safari).  
- A la barra d'adreces del navegador, introdueix l'URL proporcionat per l'aplicació.

## Transferir fitxers sense fil

Un cop la pàgina web corresponent al teu dispositiu iOS s'obre al navegador, pots arrossegar i deixar anar fàcilment fitxers des del teu ordinador a la pàgina web.  
Els fitxers que arrosseguis i deixis anar començaran a transferir-se al teu dispositiu iOS i seran accessibles dins l'aplicació.

Les instruccions detallades sobre com transferir fitxers sense fil utilitzant Wi-Fi Drive estan disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing és una altra tecnologia que et permet transferir fitxers d'un ordinador a un dispositiu utilitzant l'aplicació Finder al teu Mac i un cable Lightning.  
- Simplement connecta el dispositiu a l'ordinador mitjançant un cable i executa l'aplicació Finder al teu Mac.  
- Obre "Ubicacions" → "El teu dispositiu connectat" → "Fitxers" → i troba l'aplicació actual.  
- Toca la icona de l'aplicació per veure totes les carpetes compartides.  
- Copia fitxers de l'ordinador a la carpeta compartida del dispositiu mitjançant arrossegar i deixar anar.

Les instruccions detallades sobre com utilitzar iTunes File Sharing estan disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connectar una targeta USB

Si tens una targeta SD o un llapis USB, pots connectar-lo utilitzant un lector de targetes Lightning o USB-C a l'iPhone/iPad, o connectar-lo directament a un Mac. L'aplicació actualment és compatible amb lectors de targetes Apple Certified. Tenim instruccions detallades sobre com connectar una targeta USB al teu iPhone o iPad i gestionar els fitxers ubicats en ella, disponibles [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it). Les unitats connectades apareixen a la secció **Accessoris externs** de la pantalla de Connexions.

## Gestor de fitxers

Un cop has connectat un servei d'emmagatzematge al núvol, toca la seva icona per veure tots els fitxers i carpetes disponibles. Pots utilitzar el gestor de fitxers integrat per treballar amb aquests fitxers — descarregar, reanomenar, moure i molt més. Quan inicies una descàrrega, el fitxer apareixerà a la cua de transferència. Per veure la cua de transferència, ves a la pestanya "Fitxers locals" i toca les fletxes giratòries a la cantonada superior esquerra. Tots els fitxers i carpetes descarregats estan disponibles a la secció "Fitxers locals".

## Barra d'eines superior

La barra d'eines superior, convenientment ubicada sota la barra de navegació, ofereix diverses accions útils per a un accés fàcil. Pots mostrar o amagar aquesta barra d'eines amb un simple gest de lliscar cap avall. Aquí tens les accions disponibles:

- **Cercar**: aquesta opció et permet realitzar una cerca ràpida dins del directori actual, facilitant la localització de fitxers o carpetes específics.  

## Opcions de carpeta

Quan obres una carpeta dins l'aplicació, trobaràs un pràctic conjunt d'accions disponibles tocant el botó "..." a la cantonada superior dreta de la pantalla.  
Aquí tens un desglossament d'aquestes accions:

- **Seleccionar**: activa el mode de selecció de fitxers. Aquest mode et permet triar un o més fitxers dins la carpeta, facilitant la realització d'accions sobre els elements seleccionats.  
- **Nova carpeta**: crea una nova carpeta dins la carpeta actual. Aquesta funció et permet organitzar els teus fitxers i mantenir la teva biblioteca ben estructurada.   
- **Pujar fitxers**: puja fitxers des del teu dispositiu a la carpeta en línia. Aquesta acció et permet transferir fitxers al núvol o servidor, fent-los accessibles des de qualsevol lloc.  
- **Cercar**: cerca fitxers específics dins la carpeta actual. Especialment útil per localitzar ràpidament elements específics en una col·lecció gran.  
- **Ordenar**: ordena fitxers dins la carpeta per criteris com el nom, la mida o la data d'edició. El mode d'ordenació predeterminat sol reflectir l'ordre d'ordenació al servidor, però pots canviar-lo per adaptar-lo a les teves preferències.  
- **Vista en quadrícula/llista**: canvia entre dos modes de visualització: vista de taula i vista de miniatures. La vista de taula presenta els fitxers en una llista, mentre que la vista de miniatures mostra representacions visuals dels fitxers, facilitant la identificació del contingut d'una ullada.

{{< cards cols="1">}}
  {{< card title="" subtitle="Ordenació de carpetes al núvol d'Evertag" image="/docs/guide/evertag/img/cloud-storage-sort.webp" >}}
{{< /cards >}}

## Editar fitxers en línia

Quan necessites gestionar múltiples fitxers dins del teu emmagatzematge al núvol en aquesta aplicació, pots utilitzar el mode de selecció per agilitar les teves accions. Segueix aquests passos per a una gestió de fitxers eficaç:

- **Activar el mode de selecció**: obre l'aplicació al teu dispositiu i navega fins a la secció que conté el teu emmagatzematge al núvol. Cerca la cantonada superior dreta on trobaràs el botó "..." (el·lipsi). Toca'l i tria l'element de menú "Seleccionar" per activar el mode de selecció.  
- **Triar fitxers**: veuràs caselles de selecció al costat de cada fitxer o carpeta de la llista. Tria un o diversos fitxers o carpetes simplement tocant les caselles de selecció al costat d'ells.  
- **Realitzar diverses accions**: un cop has seleccionat els fitxers o carpetes que vols gestionar, tindràs accés a diverses accions adaptades a les teves necessitats:

{{< cards cols="1">}}
  {{< card title="" subtitle="Selecció de fitxers d'Evertag" image="/docs/guide/evertag/img/cloud-storage-file-select.webp" >}}
{{< /cards >}}

## Accions de fitxer

A prop del títol del fitxer, notaràs un símbol de punts suspensius "..." (tres punts) — serveix com a menú d'accions.  
Toca'l per revelar una llista d'accions disponibles:

- **Editar etiquetes d'àudio**: seleccionant aquesta opció, pots accedir a l'editor d'etiquetes integrat, que et permet modificar les etiquetes d'àudio del fitxer escollit. El fitxer es descarregarà temporalment a un directori temporal i després es pujarà a l'emmagatzematge després de confirmar els canvis.  
- **Afegir als Favorits**: aquesta acció afegeix el fitxer a la teva llista de fitxers favorits per a un accés ràpid i còmode.  
- **Descarregar**: tria aquesta acció per descarregar el fitxer o carpeta al teu dispositiu, fent-lo accessible per a ús sense connexió.  
- **Reanomenar**: aquesta opció et permet reanomenar el fitxer directament a l'emmagatzematge remot, permetent la nomenclatura personalitzada de fitxers.  
- **Moure**: opta per aquesta acció per traslladar el fitxer a una carpeta diferent dins del teu emmagatzematge al núvol, ajudant a mantenir una estructura de fitxers organitzada.  
- **Obrir a**: utilitza aquesta acció per exportar el fitxer a una altra aplicació compatible. El fitxer es descarregarà al teu dispositiu i apareixerà el diàleg de compartició per a una compartició o interacció posterior.  
- **Eliminar**: tingues precaució amb aquesta acció, ja que elimina permanentment el fitxer del teu emmagatzematge al núvol. **Aquesta eliminació no es pot desfer**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcions de fitxer d'Evertag" image="/docs/guide/evertag/img/cloud-storage-file-options.webp" >}}
{{< /cards >}}

Si la llista d'accions supera l'espai disponible de la pantalla, simplement desplaça't cap avall dins del menú d'accions per accedir a opcions addicionals.

## Accions de carpeta

Per a cada carpeta del teu emmagatzematge al núvol, tens diverses accions disponibles. Per accedir a aquestes opcions, simplement toca la icona de punts suspensius "..." situada al costat del títol de la carpeta. Si no veus totes les accions, desplaça't cap avall per revelar més opcions. Aquí tens les accions disponibles:

- **Afegir als Favorits**: utilitza aquesta acció per afegir la carpeta a la teva llista de fitxers favorits per a un accés ràpid i còmode.  
- **Descarregar**: descarrega tot el contingut de la carpeta al teu dispositiu per accedir-hi sense connexió.  
- **Reanomenar**: reanomena la carpeta directament a l'emmagatzematge remot.  
- **Moure**: trasllada la carpeta a una ubicació diferent dins del teu emmagatzematge al núvol.  
- **Eliminar**: tingues precaució amb aquesta acció, ja que elimina permanentment la carpeta i el seu contingut del teu emmagatzematge al núvol. **Aquesta acció no es pot desfer**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Opcions de carpeta d'Evertag" image="/docs/guide/evertag/img/cloud-storage-folder-options.webp" >}}
{{< /cards >}}
