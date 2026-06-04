---
title: "Connexions"
date: 2020-02-01
description: "Aprèn a connectar serveis al núvol i dispositius NAS a Flacbox. Reprodueix música d'alta resolució des de iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk i més. Usa SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, compartició de fitxers iTunes / Finder i unitats de memòria USB."
keywords: [
  "configuració del núvol Flacbox", "connectar Google Drive a Flacbox", "streaming de música SMB",
  "reproductor WebDAV iOS", "app de música DLNA", "streaming d'àudio NAS", "Wi-Fi Drive iPhone",
  "transferir fitxers a iPhone", "Flacbox iTunes File Sharing", "connectar NAS a iPhone",
  "app de música Synology Drive", "app de música QNAP", "app de música Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "app de música amb scrobbling Last.fm",
  "música iXpand Flash Drive", "USB DAC iPhone"
]
tags: ["guia", "flacbox", "connexions", "núvol", "NAS"]
readingTime: 12
---


En aquesta pantalla, pots connectar totes les fonts que contenen la teva música. Pots integrar serveis al núvol populars com Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive i molts més, així com el teu Mac, PC o NAS a través de protocols estàndard. Tant si la teva col·lecció viu en un servei compatible amb streaming com Dropbox o en un NAS personal com un Synology, QNAP, Buffalo, Apple Time Capsule o WD My Cloud Home, Flacbox es connecta a tots ells des d'una sola pantalla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Pantalla de Connexions de Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Connectar a l'Emmagatzematge al Núvol

- Obre la pestanya **Connexions**.
- Selecciona **Connectar a l'emmagatzematge al núvol** del menú.
- Tria un servei d'emmagatzematge al núvol de la llista.
- Introdueix les teves credencials a la pàgina d'autorització oficial proporcionada pel proveïdor del núvol i toca **Fet**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Afegir un servei d'emmagatzematge al núvol a Flacbox" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Si trobes algun problema, comprova la teva connexió a Internet i el teu usuari / contrasenya. En la versió Premium de l'app, pots afegir un nombre il·limitat de serveis; la versió gratuïta admet fins a tres.

## Serveis d'Emmagatzematge al Núvol, Servidors Multimèdia i Protocols Compatibles

Flacbox admet una gamma excepcionalment àmplia de fonts per a la teva música. Tot el que hi ha a continuació funciona des d'una sola pantalla **Connectar a l'emmagatzematge al núvol**.

**Emmagatzematge al núvol personal:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidors autoallotjats:** Plex · Jellyfin · Emby · Subsonic (i tots els servidors compatibles amb Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud via l'API compartida) · Synology Drive · QNAP.

**Protocols NAS i de compartició de fitxers:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, contrasenya o autenticació per clau pública) · NFS · DLNA / UPnP (reproducció i descàrrega).

**Emmagatzematge d'objectes compatible amb S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre servei que exposi un endpoint S3-API.

**Descoberta a la xarxa local:** La secció Dispositius disponibles llista automàticament tots els serveis Bonjour / mDNS de la teva xarxa Wi-Fi perquè puguis connectar-te amb un toc sense escriure una adreça IP.

Cada connexió utilitza el **SDK oficial o el protocol obert** del servei, amb autorització OAuth on sigui compatible. Pots connectar múltiples comptes del mateix servei (per exemple, dos comptes de Google Drive, un Dropbox personal juntament amb un de feina, o un servidor Plex i un Jellyfin) i navegar-los junts a la pantalla Connexions.

## Seguretat i Privadesa

Usem només SDK oficials i connexions segures per interactuar amb els serveis al núvol connectats. El teu usuari i contrasenya no són accessibles per a l'aplicació — totes les transferències estan xifrades amb TLS.

Quan introdueixes el teu usuari i contrasenya, l'aplicació et mostra la pàgina d'autorització oficial proporcionada pel proveïdor del servei al núvol, i tot el procés d'autorització té lloc fora de l'aplicació. El proveïdor del servei al núvol envia aleshores un token d'autenticació a l'aplicació després d'una autorització correcta, i aquest token s'utilitza per fer crides a l'API.

Un token d'autenticació és una clau digital que permet a aplicacions de tercers interactuar amb l'emmagatzematge al núvol en el teu nom. El token es guarda al teu dispositiu en l'emmagatzematge segur del sistema d'Apple (Keychain), que està xifrat en repòs i protegit pel codi del teu dispositiu o bloqueig biomètric. Pots descarregar fitxers dels serveis al núvol connectats al teu dispositiu; aquests fitxers es col·loquen al directori Documents de l'app i es poden eliminar en qualsevol moment amb el gestor de fitxers integrat.

L'aplicació no comparteix cap informació dels teus comptes al núvol connectats amb Everappz, anunciants o cap tercer. Pots revocar l'accés al teu compte al núvol en qualsevol moment obrint la pàgina de configuració del compte al teu navegador web.

## Rebutjar el Token d'Autenticació

Per revocar un token d'autenticació, inicia sessió al teu compte al núvol en un navegador web i navega a la pàgina de seguretat o d'aplicacions connectades. Allà pots trobar totes les aplicacions de tercers connectades al teu compte al núvol i eliminar qualsevol d'elles si ja no vols usar-les. Les instruccions detallades per a comptes de Google estan disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

També pots desconnectar el compte al núvol des de l'aplicació mateixa — quan ho fas, el token d'autenticació s'elimina immediatament del teu dispositiu. Si desinstal·les l'aplicació del teu dispositiu, totes les dades descarregades i els tokens d'accés s'eliminen automàticament amb ella.

## Desconnectar un Emmagatzematge al Núvol o Canviar la Configuració

- **Accedeix a les opcions d'emmagatzematge al núvol** — localitza el servei connectat a la pantalla **Connexions**.
- **Toca el botó "..."** al costat del títol del servei per obrir opcions addicionals:
  - **Canviar nom** — canvia el nom del servei al núvol tal com apareix a la teva llista.
  - **Configuració** — modifica la configuració o les dades d'autenticació. De vegades pot ser necessari reautoritzar el servei al núvol connectat si el token d'autorització ha caducat.
  - **Desconnectar** — talla completament la connexió entre l'app i el servei al núvol. Això elimina totes les cançons associades a aquest servei de la teva biblioteca musical de l'app, però les deixa intactes al servidor.

## Connectar a un Ordinador o NAS

També pots connectar el teu ordinador, NAS personal o altres dispositius de xarxa usant els protocols SMB, DLNA o WebDAV. Aquesta és la manera més fàcil de portar una biblioteca de música domèstica existent — tant si viu en un Mac, un Windows PC, una caixa Synology o un NAS — a Flacbox sense copiar res.

## Connectar a un Ordinador Usant SMB

- Toca **Connectar a l'emmagatzematge al núvol → SMB**.
- Introdueix l'adreça IP de l'ordinador i el nom de la carpeta compartida al camp URL amb el format `smb://computer-ip-address/shared-folder-name`.
- Tria la versió del protocol: **Auto**, **SMB1** o **SMB2**.
- Introdueix el teu usuari i contrasenya (si és necessari).
- Toca **Fet**.

Si la connexió és correcta, veuràs l'emmagatzematge connectat a la secció **Emmagatzematge al núvol**. Hi ha un tutorial complet sobre com connectar el teu Mac o PC usant SMB disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Connectar a un NAS Usant WebDAV

Tots els passos són els mateixos que per a SMB, excepte el camp URL. L'URL ha d'estar en el format `http://server-name` o `https://server-name` si el servidor admet SSL. WebDAV funciona amb **Synology, QNAP, Nextcloud, ownCloud** i molts altres servidors — a qualsevol lloc on hi hagi un endpoint WebDAV disponible.

Hi ha un tutorial complet sobre com connectar un NAS usant WebDAV disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Connectar a un Ordinador o NAS Usant DLNA

També pots compartir una biblioteca de música ubicada al teu Windows PC o NAS personal usant el protocol DLNA / UPnP i accedir-hi a l'app com es descriu [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA és un protocol popular i àmpliament compatible, però només permet reproduir o descarregar música — no pots pujar fitxers ni crear noves carpetes en un servidor DLNA.

## Connectar a un NAS o Servidor Usant FTP, FTPS o SFTP

Flacbox també admet els protocols clàssics de transferència de fitxers. Per connectar un servidor via FTP o FTPS, toca **Connectar a l'emmagatzematge al núvol → FTP**, introdueix l'URL del host amb el format `ftp://server-name` (o `ftps://server-name` per a una connexió xifrada), proporciona el teu usuari i contrasenya i toca **Fet**. Per a **SFTP** (SSH File Transfer Protocol), tria **SFTP** i proporciona una contrasenya o un parell de claus SSH. Ambdós funcionen amb dispositius NAS, hosts Linux i qualsevol servidor que tingui un daemon FTP / FTPS / SSH.

## Connectar a un Recurs Compartit NFS

Flacbox inclou compatibilitat amb **NFS** (Network File System) — pràctic per a hosts Linux, servidors BSD i dispositius NAS que prefereixen exposar biblioteques de música via NFS en lloc de SMB. Selecciona **NFS** al menú **Connectar a l'emmagatzematge al núvol**, introdueix l'adreça del servidor i la ruta exportada i toca **Fet**.

## Connectar un Plex Media Server

Flacbox es pot connectar directament a un Plex Media Server i navegar per la teva biblioteca de música per Artistes, Àlbums, Gèneres i Llistes de reproducció. Toca **Connectar a l'emmagatzematge al núvol → Plex**, inicia sessió amb el teu compte de Plex, tria un servidor i la biblioteca apareix al costat dels teus serveis al núvol. Els servidors Plex a la mateixa xarxa local també es descobreixen automàticament a la secció **Dispositius disponibles**.

## Connectar un Servidor Jellyfin o Emby

Tant **Jellyfin** (codi obert) com **Emby** (comercial) funcionen de manera nativa a Flacbox. Toca **Connectar a l'emmagatzematge al núvol → Jellyfin** o **Emby**, introdueix l'URL del teu servidor (alguna cosa com `http://server-ip:8096`) i les credencials, i la teva biblioteca de música està llesta per reproduir. Com amb Plex, les biblioteques a la xarxa local es llisten automàticament a **Dispositius disponibles**.

## Connectar un Servidor Subsonic o Navidrome

Flacbox parla l'API de Subsonic, cosa que significa que funciona amb **Subsonic** mateix, **Navidrome** i tots els altres servidors compatibles amb Subsonic — incloent Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Toca **Connectar a l'emmagatzematge al núvol → Subsonic**, introdueix l'URL del servidor i les credencials, i la biblioteca apareix a la pantalla de Connexions. Aquesta és la manera més fàcil de donar a Flacbox accés a una col·lecció de música autoallotjada sense exposar el recurs compartit de fitxers subjacent.

## Connectar a Emmagatzematge d'Objectes Compatible amb S3

Per als autoallotjadors i audiòfils que usen emmagatzematge d'objectes al núvol, Flacbox inclou un connector compatible amb S3. Toca **Connectar a l'emmagatzematge al núvol → Emmagatzematge S3**, i introdueix l'URL del endpoint, la regió, la clau d'accés, la clau secreta i el nom del bucket. Funciona amb AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre servei que exposi un endpoint S3-API.

## Dispositius Disponibles

Aquesta secció mostra tots els dispositius a la teva xarxa local als quals pots connectar-te des de Flacbox via descoberta Bonjour. Per establir una connexió, segueix aquests passos:

- Obre l'app i ves a la secció **Dispositius disponibles** sota Connexions.
- Toca el dispositiu al qual vols connectar-te.
- Si cal, introdueix les dades d'inici de sessió per completar la connexió.

Aquesta és la manera més ràpida de descobrir una compartició SMB, WebDAV o DLNA a la teva xarxa domèstica sense escriure adreces IP manualment.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositius disponibles a la xarxa local a Flacbox" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive és una tecnologia convenient que permet transferències de fitxers sense fils des del teu ordinador al teu dispositiu iOS via qualsevol navegador d'escriptori. Per usar aquesta funció de manera efectiva, assegura't que el teu dispositiu i ordinador estiguin connectats a la mateixa xarxa Wi-Fi. Aquí hi ha una guia pas a pas sobre com usar Wi-Fi Drive.

### Activar Wi-Fi Drive

- Obre l'aplicació i ves a la pestanya **Connexions**.
- Selecciona **Connectar via Wi-Fi** per accedir a la pantalla principal de Wi-Fi Drive.
- (Opcional) Estableix un nom d'usuari i contrasenya per al servidor web integrat per protegir l'accés.
- Toca **Iniciar Wi-Fi Drive** per activar Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive de Flacbox" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Accedir a Wi-Fi Drive al teu Ordinador

- Al teu ordinador (d'escriptori o portàtil), obre un navegador web (com Chrome, Firefox o Safari).
- A la barra d'adreces del navegador, introdueix l'URL proporcionat per l'aplicació.

### Transferir Fitxers Sense Fils

Un cop la pàgina web corresponent al teu dispositiu iOS s'obre al navegador, pots fàcilment arrossegar i deixar anar fitxers des del teu ordinador a la pàgina web. Els fitxers que deixis anar començaran a transferir-se al teu dispositiu iOS i seran accessibles dins Flacbox.

També pots muntar Wi-Fi Drive directament a Finder al macOS (Anar → Connectar al servidor…) o a l'Explorador de fitxers al Windows (Mapejar unitat de xarxa…) i tractar el teu iPhone o iPad com una unitat de xarxa regular.

Hi ha instruccions detallades sobre com transferir fitxers sense fils usant Wi-Fi Drive disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Compartició de Fitxers iTunes / Finder

La compartició de fitxers iTunes (ara Compartició de fitxers Finder al macOS Catalina i posteriors) és una altra manera de transferir fitxers d'un ordinador a un dispositiu usant un cable Lightning o USB-C.

- Connecta el dispositiu a l'ordinador amb un cable i executa **Finder** al Mac (o **iTunes** al Windows).
- Obre **Ubicacions → El teu dispositiu connectat → Fitxers** i busca l'app Flacbox.
- Toca la icona de l'app per veure totes les carpetes compartides.
- Copia fitxers de l'ordinador a la carpeta compartida del dispositiu usant arrossegar i deixar anar.

Hi ha instruccions detallades sobre com usar la Compartició de fitxers Finder disponibles [aquí](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connectar una Unitat de Memòria USB

Si tens una targeta SD o una unitat USB, pots connectar-la usant un lector Lightning a USB / targeta SD o una unitat USB-C (a iPad i iPhone 15 / 16 / 17 / Pro). L'app admet lectors de targetes certificats per Apple i iXpand Flash Drives. Amb un iXpand Flash Drive, insereix-lo al port Lightning i obre l'aplicació — veuràs un missatge de Dispositiu extern connectat i la informació del dispositiu. Toca la icona del llapis de memòria per accedir a la carpeta de música i toca qualsevol fitxer d'àudio per començar a reproduir.

Tenim instruccions detallades sobre com connectar una unitat de memòria USB al teu iPhone i escoltar música o gestionar fitxers ubicats en ella [aquí](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestor de Fitxers

Un cop has connectat un servei d'emmagatzematge al núvol, toca la seva icona per veure tots els fitxers i carpetes disponibles. Pots usar el gestor de fitxers integrat per treballar amb aquests fitxers — descarregar, canviar nom, moure, pujar, eliminar i més. Quan inicia una descàrrega, el fitxer apareix a la cua de transferència. Per obrir la cua de transferència, ves a la pestanya Fitxers locals i toca la icona de fletxes rotatives a la cantonada superior esquerra. Tots els fitxers i carpetes descarregats estan disponibles a la secció Fitxers locals.

## Barra d'Eines Superior

La barra d'eines superior, convenientment situada sota la barra de navegació, ofereix diverses accions útils per a un accés fàcil. Pots mostrar-la o ocultar-la amb un simple gest de lliscar cap avall.

- **Cerca** — realitza una cerca ràpida dins del directori actual, facilitant la localització de fitxers o carpetes específics.
- **Continuar reproducció** — si està activat als ajustos de l'aplicació, restaura la cua del reproductor d'àudio i l'última posició multimèdia de la carpeta actual. Una manera pràctica de continuar des d'on ho vas deixar.
- **Reproduir tot** — escaneja la carpeta actual i les seves subcarpetes, i afegeix tots els fitxers d'àudio trobats a una nova cua del reproductor. Útil quan vols reproduir tots els temes d'un directori.
- **Reproduir tot aleatori** — com Reproduir tot, però barreja els fitxers abans d'afegir-los a la cua del reproductor d'àudio. Ideal per redescobrir una carpeta de música antiga.

## Opcions de Carpeta

Quan obres una carpeta, trobaràs un conjunt útil d'accions disponibles tocant el botó **"..."** a la cantonada superior dreta.

- **Seleccionar** — activa el mode de selecció de fitxers. Permet triar un o més fitxers dins la carpeta i realitzar accions en tota la selecció.
- **Nova carpeta** — crea una nova carpeta a la carpeta actual. Ideal per mantenir la teva biblioteca ben estructurada.
- **Activar el mode fora de línia** — activa el mode offline per a la carpeta actual. El mode offline va més enllà de la descàrrega simple: monitora activament la carpeta per detectar canvis. Si afegeixes nous fitxers en línia, apareixeran automàticament al teu dispositiu.
- **Pujar fitxers** — puja fitxers des del teu dispositiu a la carpeta en línia. Això els fa accessibles des de qualsevol lloc via el mateix servei al núvol.
- **Cerca** — cerca fitxers específics dins de la carpeta actual.
- **Ordenar** — ordena els fitxers per nom, mida, data de modificació o per metadades. El mode d'ordenació per defecte reflecteix l'ordre d'ordenació del servidor, però pots canviar-lo per adaptar-lo a les teves preferències.
- **Vista de quadrícula / llista** — commuta entre la vista de taula i la vista de miniatures. La vista de taula mostra una llista compacta; la vista de miniatures mostra grans previsualitzacions de portades per a una identificació visual ràpida.

## Editar Fitxers en Línia

Quan necessites gestionar múltiples fitxers al teu emmagatzematge al núvol, usa el **Mode de selecció** per simplificar les teves accions:

- **Activar el mode de selecció** — toca el botó **"..."** a la cantonada superior dreta i tria **Seleccionar**.
- **Triar fitxers** — apareixen caselles de selecció al costat de cada fitxer i carpeta. Toca per seleccionar un o diversos elements.
- **Realitzar accions** — un cop has seleccionat els fitxers o carpetes, tindràs accés a Reproduir a continuació, Reproduir més tard, Afegir a la biblioteca musical, Afegir a una llista de reproducció, Copiar, Pujar, Moure, Canviar nom i Eliminar.

Si prefereixes tractar l'emmagatzematge al núvol connectat com a només lectura (per evitar eliminacions accidentals), activa Configuració → Gestor de fitxers → Editar fitxers en línia → Desactivat per ocultar totes les operacions destructives de la interfície d'usuari.

## Accions sobre Fitxers

Toca la icona **"..."** prop del títol d'un fitxer per revelar el seu menú d'accions:

- **Reproduir a continuació** — insereix el fitxer a la part superior de la cua del reproductor, de manera que es reprodueix just després de la pista actual.
- **Reproduir més tard** — afegeix el fitxer a la part inferior de la cua del reproductor.
- **Afegir a la biblioteca musical** — incorpora el fitxer a la teva biblioteca musical, organitzada per artista, àlbum, gènere o compositor.
- **Afegir a una llista de reproducció** — afegeix el fitxer a una llista de reproducció existent o crea'n una de nova.
- **Editar etiquetes d'àudio** — obre l'editor d'etiquetes integrat per modificar metadades. Per als fitxers en línia, la pista es descarrega temporalment, s'edita i es torna a pujar després de confirmar.
- **Afegir als favorits** — afegeix el fitxer a la teva llista de favorits per a un accés ràpid.
- **Descarregar** — descarrega el fitxer o carpeta al teu dispositiu per a ús offline.
- **Canviar nom** — canvia el nom del fitxer directament a l'emmagatzematge remot.
- **Moure** — trasllada el fitxer a una carpeta diferent dins del teu emmagatzematge al núvol.
- **Obrir amb** — exporta el fitxer a una altra app compatible. El fitxer es descarrega al teu dispositiu i apareix el full de compartició del sistema.
- **Eliminar** — elimina permanentment el fitxer del teu emmagatzematge al núvol. **Aquesta acció no es pot desfer.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Més accions per a un fitxer a l'emmagatzematge al núvol connectat a Flacbox" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Si la llista d'accions supera l'espai de pantalla disponible, simplement desplaça't cap avall dins del menú d'accions per accedir a les opcions addicionals.

## Accions sobre Carpetes

Per a cada carpeta del teu emmagatzematge al núvol, tens una gran varietat d'accions disponibles tocant la icona **"..."** al costat del títol de la carpeta. Si no veus totes les accions, desplaça't cap avall per revelar-ne més.

- **Reproduir tot** — substitueix la cua del reproductor actual per tots els elements de la carpeta seleccionada.
- **Reproduir a continuació** — afegeix tota la carpeta a la part superior de la cua del reproductor.
- **Reproduir més tard** — afegeix el contingut de la carpeta a la part inferior de la cua del reproductor.
- **Afegir a la biblioteca musical** — incorpora el contingut de la carpeta a la teva biblioteca musical.
- **Afegir a la llista de reproducció** — afegeix tota la carpeta a una llista de reproducció. També tens l'opció de crear una nova llista de reproducció; el seu nom s'omple automàticament amb el nom de la carpeta.
- **Afegir als favorits** — afegeix la carpeta als teus favorits per a un accés ràpid.
- **Activar el mode fora de línia** — més que una descàrrega simple, monitorea contínuament la carpeta per detectar nous fitxers i els descarrega automàticament en el moment en què apareixen en línia.
- **Descarregar** — descarrega tots els continguts de la carpeta al teu dispositiu per a accés offline.
- **Canviar nom** — canvia el nom de la carpeta directament a l'emmagatzematge remot.
- **Moure** — trasllada la carpeta a una ubicació diferent dins del teu emmagatzematge al núvol.
- **Arxivar (ZIP)** — agrupa el contingut de la carpeta en un sol fitxer ZIP (funció Premium).
- **Eliminar** — elimina permanentment la carpeta i el seu contingut del teu emmagatzematge al núvol. **Aquesta acció no es pot desfer.**

## Accés Ràpid

La secció Accés ràpid es troba a la part superior de la pantalla. Et dona accés ràpid als teus fitxers favorits i oberts recentment dels serveis al núvol connectats. Sempre que obres un fitxer o carpeta del núvol, s'afegeix a la llista d'Oberts recentment. Per netejar aquesta llista, obre Recents, toca el botó Més accions i tria Eliminar llista. També pots marcar carpetes profundament niades com a Favorits per accedir-hi ràpidament sense navegar per l'estructura de directoris.

{{< cards cols="1">}}
  {{< card title="" subtitle="Enllaços en línia i accés ràpid a Flacbox" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Altres Serveis

Aquesta secció mostra funcions extra que milloren la teva experiència. Actualment, l'app admet el scrobbling de **Last.fm** — quan está connectat, les teves estadístiques de reproducció s'envien automàticament al teu compte de Last.fm. Després pots visitar el teu perfil de Last.fm per veure anàlisi d'escolta i obtenir recomanacions de música personalitzades. Hi ha instruccions de configuració detallades disponibles [aquí](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Connexió a Last.fm a Flacbox" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
