---
title: "Connexions"
date: 2020-01-01
description: "Aprèn a connectar serveis al núvol, ordinadors, dispositius NAS i gestionar els teus fitxers de música amb Evermusic. Guia pas a pas per a Wi-Fi Drive, SMB, DLNA, WebDAV, compartició de fitxers iTunes i molt més."
keywords: [
  "Evermusic", "reproductor música al núvol", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "compartició fitxers iTunes",
  "connectar emmagatzematge al núvol", "transferència música iPhone", "gestor fitxers iOS"
]
tags: ["evermusic", "guide", "connections"]
readingTime: 11
---


A la pantalla de Connexions pots connectar cada font que contingui la teva música — serveis al núvol populars, servidors multimèdia allotjats, el teu Mac o PC, un NAS personal, Apple Time Capsule, WD My Cloud Home, fins i tot una unitat flaix USB — i usar-los tots des d'una interfície unificada. Connexions també és on configures l'Accés ràpid a carpetes al núvol profundament niades i on autentiques Last.fm per al scrobbling.

La pantalla està dividida en seccions clarament etiquetades perquè escali des d'un únic compte d'iCloud Drive fins a una biblioteca distribuïda a través de múltiples núvols i dispositius NAS: Accés ràpid a la part superior (les teves carpetes al núvol favorites), Emmagatzematge al núvol (els comptes que has afegit), Xarxa local (dispositius descoberts via Bonjour), Ordinador (Wi-Fi Drive, compartició de fitxers iTunes, SMB), Accessoris externs (unitats flaix USB connectades) i Altres serveis (Last.fm i similars).

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Connexions d'Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Connectar a l'emmagatzematge al núvol

- Obre la pestanya Connexions.
- Selecciona Connectar a l'emmagatzematge al núvol del menú.
- Tria un servei d'emmagatzematge al núvol de la llista.
- Inicia sessió a la pàgina d'autorització oficial del proveïdor (Evermusic mai veu la teva contrasenya).
- Toca Fet.

{{< cards cols="1">}}
  {{< card title="" subtitle="Selector de proveïdor d'emmagatzematge al núvol" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Si trobes problemes, verifica la teva connexió a Internet i les credencials d'inici de sessió, i assegura't que l'autenticació de dos factors estigui configurada correctament per a aquest servei.  
A la versió Premium de l'app pots afegir un nombre il·limitat de serveis. Els usuaris gratuïts poden connectar un únic compte al núvol alhora.

## Serveis d'emmagatzematge al núvol compatibles

Evermusic suporta la línia completa de serveis populars al núvol i allotjats. Els usuaris gratuïts obtenen el mateix catàleg de proveïdors però amb el límit d'un compte; Premium desbloqueja comptes il·limitats i elimina la majoria d'altres límits.

- **Comptes al núvol personals:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidors allotjats i biblioteques multimèdia:** Plex · Jellyfin · Emby · Subsonic (i tots els servidors compatibles amb Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i Owncloud, via l'API compartida) · Synology Drive · QNAP.
- **Protocols NAS i compartició de fitxers:** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (contrasenya o autenticació per clau pública), NFS i DLNA (només lectura — reproducció i descàrrega).
- **Emmagatzematge d'objectes compatible amb S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage o qualsevol punt final de l'API S3.
- **Descoberta a la xarxa local:** la secció de dispositius disponibles llista automàticament qualsevol dispositiu a la teva Wi-Fi que s'anunciï via Bonjour / mDNS — servidors Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, encaminadors AirPort amb discs adjunts, i similars.

## Seguretat i privacitat

Utilitzem només l'SDK oficial i la connexió segura per interactuar amb els serveis al núvol connectats. El teu nom d'usuari i contrasenya no estan disponibles per a l'aplicació. Totes les sol·licituds de l'aplicació al servei al núvol estan xifrades.

Quan introdueixes el teu nom d'usuari i contrasenya, l'aplicació et mostra la pàgina d'autorització oficial que proporciona el proveïdor del servei al núvol i tot el procés d'autorització es fa fora de l'aplicació. El proveïdor del servei al núvol envia un testimoni d'autenticació a l'aplicació després d'una autorització satisfactòria i aquest testimoni s'utilitza per fer crides a l'API.

El testimoni d'autenticació és una clau digital que permet a aplicacions de tercers interactuar amb l'emmagatzematge al núvol. El testimoni d'autenticació s'emmagatzema al teu dispositiu en un emmagatzematge de sistema segur anomenat Keychain. Pots descarregar els teus fitxers del servei al núvol connectat al dispositiu i aquests fitxers es col·locaran al directori 'Documents' de l'app. Pots eliminar aquests fitxers en qualsevol moment mitjançant el gestor de fitxers integrat.

L'aplicació no comparteix cap informació del compte al núvol connectat. Pots revocar l'accés al teu compte al núvol en qualsevol moment obrint la pàgina de configuració del compte al teu navegador web.

## Rebutjar el testimoni d'autenticació

Inicia sessió al teu compte al navegador web i navega a la pàgina de configuració. Allà pots trobar totes les aplicacions de tercers que estan connectades al teu compte al núvol i eliminar qualsevol d'elles si ja no vols usar aquesta aplicació. Les instruccions detallades estan disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

També pots desconnectar els comptes al núvol connectats a l'aplicació i el testimoni d'autenticació també s'eliminarà del teu dispositiu. Si elimines l'aplicació del teu dispositiu, totes les dades descarregades i els testimonis d'accés també s'eliminaran.

## Desconnectar un emmagatzematge al núvol o canviar la configuració

- Accedeix a les opcions d'emmagatzematge al núvol: primer, localitza l'emmagatzematge al núvol que vols gestionar dins de la interfície de l'app.
- Toca el botó '...': al costat del títol del servei, veuràs un botó '...'. Toca'l per accedir a opcions addicionals.
  - **Canviar nom**: si vols canviar el nom del servei al núvol tal com apareix a la teva llista, selecciona 'Canviar nom.'
  - **Configuració**: per modificar la configuració o les dades d'autenticació del servei al núvol, tria 'Configuració.' De vegades, pot ser que hagis de tornar a autoritzar el servei al núvol connectat si el testimoni d'autorització ha caducat.
  - **Desconnectar**: si vols trencar completament la connexió entre l'app i el servei al núvol, selecciona 'Desconnectar.' Tingues en compte que triar aquesta opció eliminarà totes les cançons associades a aquest servei al núvol de la biblioteca de música de l'app, però romandran al servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de més accions de l'emmagatzematge al núvol connectat" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Connectar a l'ordinador o NAS

També pots connectar el teu ordinador, NAS personal o altres dispositius de xarxa utilitzant el protocol SMB, DLNA o WebDAV.

## Connectar a l'ordinador mitjançant SMB

- Toca "Connectar a l'emmagatzematge al núvol" → SMB.
- Introdueix l'adreça IP de l'ordinador i el nom de la carpeta compartida al camp URL utilitzant el format smb://computer-ip-address/shared-folder-name
- Tria la versió del protocol: Auto, SMB1, SMB2
- Introdueix el nom d'usuari i la contrasenya (si cal)
- Toca "Fet".

Si la connexió és satisfactòria, veuràs l'emmagatzematge connectat a la secció "Emmagatzematge al núvol".  
Un tutorial complet sobre com connectar el teu MAC o PC mitjançant SMB està disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuració de connexió SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Connectar al NAS mitjançant WebDAV

Tots els passos són els mateixos excepte el camp URL.  
L'URL ha de tenir el format http://server-name o https://server-name si el servidor admet SSL.
Un tutorial complet sobre com connectar NAS mitjançant el protocol WebDAV està disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuració de connexió WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Connectar a l'ordinador o NAS mitjançant DLNA

També pots compartir una biblioteca de música ubicada al teu Windows PC o NAS personal utilitzant el protocol DLNA i accedir a aquesta biblioteca a l'app tal com es descriu [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA és un protocol popular i àmpliament utilitzat, però només permet reproduir o descarregar música. No pots pujar fitxers ni crear noves carpetes al servidor.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuració de connexió DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Dispositius disponibles

Aquesta secció mostra tots els dispositius dins de la teva xarxa local als quals pots connectar-te a través de l'aplicació.  
Per establir una connexió amb un dispositiu, segueix aquests passos:

- Obre l'app i vés a la secció "Dispositius disponibles".
- Toca el dispositiu al qual vols connectar-te de la llista.
- Si cal, introdueix les teves dades d'inici de sessió per completar la connexió.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositius disponibles a la xarxa local" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive 

Wi-Fi Drive és una tecnologia còmoda que permet transferències de fitxers sense fil des del teu ordinador al teu dispositiu iOS via un navegador d'escriptori.  
Per usar aquesta funció de manera efectiva, assegura't que el teu dispositiu i l'ordinador estiguin connectats a la mateixa xarxa Wi-Fi.   
Aquí tens una guia pas a pas sobre com usar Wi-Fi Drive.

## Activar Wi-Fi Drive

- Obre l'aplicació i vés a la pestanya "Connexions".
- Selecciona "Connectar via Wi-Fi" per accedir a la pantalla principal de Wi-Fi Drive.
- Toca "Iniciar Wi-Fi Drive" per activar Wi-Fi Drive.

## Accedir a Wi-Fi Drive des del teu ordinador

- A l'ordinador (d'escriptori o portàtil), obre un navegador web (com Chrome, Firefox o Safari).
- A la barra d'adreces del navegador, introdueix l'URL proporcionat per l'aplicació.

## Transferir fitxers sense fil

Un cop la pàgina web corresponent al teu dispositiu iOS s'obri al navegador, pots fàcilment arrossegar i deixar anar fitxers des del teu ordinador a la pàgina web.  
Els fitxers que arrosseguis i deixis anar començaran a transferir-se al teu dispositiu iOS i seran accessibles dins de l'aplicació.

{{< cards cols="1">}}
  {{< card title="" subtitle="Configuració del servidor Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Les instruccions detallades sobre com transferir fitxers sense fil mitjançant WiFi-Drive estan disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Compartició de fitxers iTunes

La compartició de fitxers iTunes és una altra tecnologia que et permet transferir fitxers de l'ordinador al dispositiu utilitzant l'app Finder al teu Mac i un cable Lightning.   
- Simplement connecta un dispositiu a l'ordinador mitjançant un cable i executa l'app Finder al teu Mac. 
- Obre "Ubicacions" → "El teu dispositiu connectat" → "Fitxers" → i troba l'app Evermusic. 
- Toca la icona de l'app per veure totes les carpetes compartides. 
- Copia fitxers de l'ordinador a la carpeta compartida del dispositiu mitjançant arrossegar i deixar anar.   

Les instruccions detallades sobre com usar la compartició de fitxers iTunes estan disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Compartició de fitxers iTunes / Finder al Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Connectar una targeta USB

Si tens una targeta SD, pots connectar-la mitjançant un lector de targetes Lightning. L'app suporta actualment lectors de targetes Apple Certified i iXpand Flash Drives. Si tens un iXpand Flash Drive - insereix-lo al port Lightning i obre l'aplicació. Veuràs un missatge 'Dispositiu extern connectat' i informació del dispositiu. Simplement toca la icona de la unitat flaix per accedir a la carpeta de música i toca qualsevol fitxer d'àudio per començar a reproduir. Tenim instruccions detallades sobre com connectar una targeta USB a l'iPhone i escoltar música o gestionar fitxers ubicats en ella, disponibles [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de fitxers

Un cop has connectat un servei d'emmagatzematge al núvol, toca la seva icona per veure tots els fitxers i carpetes disponibles. Pots usar el gestor de fitxers integrat per treballar amb aquests fitxers — descarregar, canviar nom, moure i molt més. Quan inicies una descàrrega, el fitxer apareixerà a la cua de transferència. Per veure la cua de transferència, vés a la pestanya "Fitxers locals" i toca les fletxes giratòries a la cantonada superior esquerra. Tots els fitxers i carpetes descarregats estan disponibles a la secció "Fitxers locals".

## Barra d'eines superior

La barra d'eines superior, convenientment ubicada sota la barra de navegació, ofereix diverses accions útils per a un accés fàcil. Pots mostrar o ocultar aquesta barra d'eines amb un simple gest de lliscar cap avall. Aquí teniu les accions disponibles:

- **Cerca**: Aquesta opció et permet realitzar una cerca ràpida dins del directori actual, facilitant la localització de fitxers o carpetes específics.
- **Continuar reproducció**: Si s'activa a la configuració de l'aplicació, aquesta funció restaura la cua del reproductor d'àudio i l'última posició multimèdia per a la carpeta actual. És una manera pràctica de reprendre on ho vas deixar a la teva biblioteca de música.
- **Reproduir tot**: En seleccionar aquesta acció, l'app escanejarà la carpeta actual i les seves subcarpetes, afegint tots els fitxers d'àudio trobats a una nova cua del reproductor. Això és útil quan vols reproduir tota la música dins d'un directori particular.
- **Reproduir aleatòriament**: Similar a "Reproduir tot", aquesta acció escaneja la carpeta actual i les seves subcarpetes però barreja els fitxers abans d'afegir-los a la cua del reproductor d'àudio. És una manera excel·lent de gaudir de la teva música en ordre aleatori per a una mica de varietat.

{{< cards cols="1">}}
  {{< card title="" subtitle="Barra d'eines superior dins d'una carpeta al núvol" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Opcions de carpeta

Quan obres una carpeta dins de l'app, trobaràs un conjunt pràctic d'accions disponibles tocant el botó "..." a la cantonada superior dreta de la pantalla.   
Aquí tens un desglossament d'aquestes accions:

- **Seleccionar**: Activa el mode de selecció de fitxers. Aquest mode et permet triar un o més fitxers dins de la carpeta, facilitant realitzar accions sobre elements seleccionats.
- **Nova carpeta**: Crea una nova carpeta dins de la carpeta actual. Aquesta funció et permet organitzar els teus fitxers i mantenir la teva biblioteca ben estructurada.
- **Activar el mode sense connexió**: Activa el mode sense connexió per a la carpeta actual. El mode sense connexió va més enllà de la simple descàrrega; monitora activament la carpeta per detectar canvis. Si afegeixes nous fitxers a la carpeta en línia, l'app els descarregarà automàticament al teu dispositiu. Això assegura que la teva biblioteca local estigui actualitzada amb els canvis al servidor.
- **Pujar fitxers**: Puja fitxers des del teu dispositiu a la carpeta en línia. Aquesta acció et permet transferir fitxers al núvol o servidor, fent-los accessibles des de qualsevol lloc.
- **Cerca**: Cerca fitxers específics dins de la carpeta actual. Això és especialment útil per localitzar ràpidament elements específics en una col·lecció gran.
- **Ordenar**: Ordena els fitxers dins de la carpeta per criteris com el nom, la mida o la data d'edició. El mode d'ordenació predeterminat normalment reflecteix l'ordre d'ordenació al servidor, però pots canviar-lo per adaptar-lo a les teves preferències.
- **Vista graella/llista**: Canvia entre dos modes de visualització: vista de taula i vista de miniatures. La vista de taula presenta els fitxers en una llista, mentre que la vista de miniatures mostra representacions visuals dels fitxers, facilitant identificar el contingut d'un cop d'ull.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de més accions de la carpeta actual" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Editar fitxers en línia

Quan necessites gestionar múltiples fitxers dins del teu emmagatzematge al núvol a Evermusic, pots usar el mode de selecció per agilitzar les teves accions. Segueix aquests passos per a una gestió efectiva de fitxers:

- **Activar el mode de selecció**: Obre l'app al teu dispositiu i navega a la secció que conté el teu emmagatzematge al núvol. Busca la cantonada superior dreta on trobaràs el botó "..." (punts suspensius). Toca'l i tria l'element de menú "Seleccionar" per activar el mode de selecció.
- **Tria fitxers**: Notaràs que apareixen caselles de verificació al costat de cada fitxer o carpeta llistats. Tria un o múltiples fitxers o carpetes simplement tocant les caselles de verificació al seu costat.
- **Realitza diverses accions**: Un cop hagis seleccionat els fitxers o carpetes que vols gestionar, tindràs accés a diverses accions adaptades a les teves necessitats:

{{< cards cols="1">}}
  {{< card title="" subtitle="Mode de selecció per a fitxers en línia" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Accions de fitxer

A prop del títol del fitxer, notaràs un símbol de punts suspensius "..." (tres punts) — aquest serveix com a menú d'accions.  
Toca'l per revelar una llista d'accions disponibles:

- **Reproduir a continuació**: Opta per aquesta acció per inserir el fitxer triat a la part superior de la teva cua del reproductor, assegurant que es reprodueixi immediatament després de l'element que s'està reproduint actualment.
- **Reproduir més tard**: Seleccionar aquesta opció afegeix el fitxer a la part inferior de la teva cua del reproductor, assegurant que es reprodueixi després de la cua existent.
- **Afegir a la biblioteca de música**: Aquesta acció et permet incorporar el fitxer a la teva biblioteca de música, fent-lo fàcilment accessible i organitzat per artista, àlbum, gènere o compositor.
- **Afegir a una llista de reproducció**: Usa aquesta acció per afegir el fitxer a una llista de reproducció existent o crear-ne una de nova.
- **Editar etiquetes d'àudio**: En seleccionar aquesta opció, pots accedir a l'editor d'etiquetes integrat d'Evermusic, permetent-te modificar les etiquetes d'àudio del fitxer triat. El fitxer es descarregarà temporalment a un directori temporal i després es pujarà a l'emmagatzematge un cop confirmis els canvis.
- **Afegir als favorits**: Aquesta acció afegeix el fitxer a la teva llista de fitxers favorits per a un accés ràpid i còmode.
- **Descarregar**: Tria aquesta acció per descarregar el fitxer o carpeta al teu dispositiu, fent-lo accessible per a ús sense connexió.
- **Canviar nom**: Aquesta opció et permet canviar el nom del fitxer directament a l'emmagatzematge remot, permetent una nomenclatura personalitzada de fitxers.
- **Moure**: Opta per aquesta acció per reubica el fitxer a una carpeta diferent dins del teu emmagatzematge al núvol, ajudant a mantenir una estructura de fitxers organitzada.
- **Obrir amb**: Usa aquesta acció per exportar el fitxer a una altra app compatible. El fitxer es descarregarà al teu dispositiu i apareixerà el diàleg de Compartir per a més compartició o interacció.
- **Eliminar**: Procedeix amb precaució amb aquesta acció, ja que elimina permanentment el fitxer del teu emmagatzematge al núvol. Aquesta eliminació no es pot desfer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menú de més accions per a un sol fitxer" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Si la llista d'accions supera l'espai disponible a la pantalla, simplement desplaça't cap avall dins del menú d'accions per accedir a opcions addicionals.

## Accions de carpeta

Per a cada carpeta al teu emmagatzematge al núvol, tens diverses accions disponibles. Per accedir a aquestes opcions, simplement toca la icona de punts suspensius "..." ubicada al costat del títol de la carpeta. Si no veus totes les accions, desplaça't cap avall per revelar més opcions. Aquí teniu les accions disponibles:

- **Reproduir tot**: Substitueix la cua actual del reproductor per tots els elements de la carpeta seleccionada.
- **Reproduir a continuació**: Afegeix tota la carpeta a la part superior de la cua del reproductor, just després de l'element que s'està reproduint actualment.
- **Reproduir més tard**: Afegeix el contingut de la carpeta a la part inferior de la cua del reproductor.
- **Afegir a la biblioteca de música**: Aquesta acció incorpora perfectament el contingut de la carpeta a la teva biblioteca de música, fent-lo fàcilment accessible i organitzat per artista, àlbum, gènere o compositor.
- **Afegir a una llista de reproducció**: Pots incloure tota la carpeta en una llista de reproducció. També tens l'opció de crear una nova llista de reproducció i el nom de la carpeta s'assignarà automàticament.
- **Afegir als favorits**: Usa aquesta acció per afegir la carpeta a la teva llista de fitxers favorits per a un accés ràpid i còmode.
- **Activar el mode sense connexió**: En activar el mode sense connexió per a una carpeta seleccionada, l'aplicació va més enllà de la simple descàrrega. Escaneja contínuament per detectar canvis i si s'afegeixen nous fitxers a la carpeta en línia, es descarregaran automàticament a l'app.
- **Descarregar**: Descarrega tot el contingut de la carpeta al teu dispositiu per a l'accés sense connexió.
- **Canviar nom**: Canvia el nom de la carpeta directament a l'emmagatzematge remot.
- **Moure**: Reubica la carpeta a una ubicació diferent dins del teu emmagatzematge al núvol.
- **Eliminar**: Procedeix amb precaució amb aquesta acció ja que elimina permanentment la carpeta i el seu contingut del teu emmagatzematge al núvol. Aquesta acció no es pot desfer.


## Accés ràpid

La secció d'Accés ràpid es troba a la part superior de la pantalla. Et proporciona accés ràpid als teus fitxers favorits i als oberts recentment des de serveis al núvol connectats.
Cada cop que obres un fitxer o carpeta del núvol, s'afegeix a la llista "Obert recentment". Per netejar aquesta llista, obre "Recents", toca el botó "Més accions" i tria "Eliminar llista". També pots marcar carpetes profundament niades com a Favorites per accedir-hi ràpidament sense recórrer l'estructura de directoris.

## Altres serveis

Aquesta secció mostra funcions addicionals que milloren la teva experiència. Actualment, l'app suporta el scrobbling de Last.fm. Quan estigui connectat, les teves estadístiques de reproducció s'envien automàticament al teu compte de Last.fm. Pots visitar el teu perfil de Last.fm més tard per veure les analítiques d'escolta i obtenir recomanacions musicals personalitzades. Les instruccions detallades de configuració estan disponibles [aquí](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
