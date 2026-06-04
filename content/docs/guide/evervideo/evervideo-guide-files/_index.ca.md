---
title: "Fitxers"
date: 2020-02-01
lastmod: 2026-06-01
description: "Aprèn a usar la pestanya Fitxers d'Evervideo a iPhone, iPad i Mac. Connecta serveis al núvol, dispositius NAS, servidors multimèdia i transmissions RTSP en un sol lloc. Gestiona vídeos fora de línia, la cua de transferències, descàrregues, Wi-Fi Drive, compartició de fitxers iTunes/Finder i unitats USB. Inclou iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP/SFTP, DLNA i emmagatzematge compatible amb S3."
keywords: [
  "fitxers Evervideo", "connexions Evervideo", "fitxers locals Evervideo",
  "configuració vídeo núvol iPhone", "connectar Google Drive vídeo", "transmissió vídeo SMB",
  "reproductor vídeo WebDAV iOS", "DLNA vídeo iPhone", "transmissió vídeo NAS",
  "transferència vídeo Wi-Fi Drive", "compartició fitxers iTunes Evervideo", "RTSP iPhone",
  "Evervideo Plex", "Evervideo Jellyfin", "Evervideo Emby",
  "Evervideo Subsonic", "Evervideo Navidrome",
  "mode fora de línia vídeo Evervideo", "cua transferències Evervideo",
  "gestor fitxers Evervideo", "carpeta Documents Evervideo",
  "reproductor vídeo Synology", "reproductor vídeo QNAP",
  "reproductor vídeo Apple Time Capsule", "USB DAC vídeo",
  "reproductor vídeo iXpand", "reproductor vídeo S3"
]
tags: ["guia", "evervideo", "fitxers", "connexions", "núvol", "NAS", "Plex", "RTSP"]
readingTime: 14
---

La pestanya Fitxers és el gestor de fitxers tot en un d'Evervideo. A diferència de la majoria d'apps de vídeo que separen l'emmagatzematge al núvol dels fitxers locals en pestanyes diferents, Evervideo fusiona tots dos en una sola pantalla desplaçable perquè puguis moure't d'un servidor Plex a una carpeta al núvol i a la carpeta Documents de l'iPhone sense canviar de pestanya.

La pestanya Fitxers es divideix en seccions clares que apareixen en aquest ordre a la pantalla:

- **Accés ràpid** — recents i preferits per als fitxers i carpetes que has obert més recentment.
- **Fitxers d'aquesta aplicació** — el que hi ha a la carpeta Documents protegida per sandbox d'Evervideo.
- **Fitxers en aquest iPhone/iPad/Mac** — vídeos en altres llocs del dispositiu, accessibles a través del selector de fitxers del sistema.
- **Emmagatzematge al núvol** — cada compte al núvol, NAS i servidor multimèdia que tens connectat.
- **Dispositius disponibles** — servidors i unitats descoberts automàticament per Bonjour/mDNS a la xarxa local.

A la cantonada superior dreta de la pantalla Fitxers hi ha un botó Transferències (icona de fletxes giratòries). Toca'l per obrir la cua de transferències on monitoritzes cada descàrrega i càrrega de totes les fonts.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fitxers d'Evervideo en emmagatzemaments connectats" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Connectar a l'emmagatzematge al núvol

La secció d'emmagatzematge al núvol de la pestanya Fitxers és on viu cada compte connectat, NAS, servidor multimèdia i transmissió — un al costat de l'altre, en una llista desplaçable.

{{< cards cols="1">}}
  {{< card title="" subtitle="Secció d'emmagatzematge al núvol a la pestanya Fitxers d'Evervideo" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Obre la pestanya **Fitxers**.
- Desplaça't fins a la secció **Emmagatzematge al núvol**.
- Toca **Connectar a l'emmagatzematge al núvol** al menú.
- Tria un servei d'emmagatzematge al núvol de la llista.
- Introdueix les teves credencials a la pàgina d'autorització oficial del proveïdor al núvol i toca **Fet**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Connectar un servei d'emmagatzematge al núvol a Evervideo" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Si trobes algun problema, comprova la teva connexió a Internet i les teves credencials. A la versió Premium de l'app, pots afegir un nombre il·limitat de serveis; la versió gratuïta admet fins a tres.

## Serveis d'emmagatzematge al núvol, servidors multimèdia i protocols compatibles

Evervideo admet una gamma excepcionalment àmplia de fonts per als teus vídeos. Tot el que hi ha a continuació funciona des d'un sol flux de connexió a l'emmagatzematge al núvol.

**Emmagatzematge al núvol personal:** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Servidors multimèdia allotjats localment:** Plex · Jellyfin · Emby · Subsonic (i cada servidor compatible amb Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (i ownCloud via l'API compartida) · Synology Drive · QNAP.

**Protocols NAS i de compartició de fitxers:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP/HTTPS) · FTP · FTPS · SFTP (protocol de transferència de fitxers SSH, contrasenya o autenticació de clau pública) · NFS · DLNA/UPnP (reproducció i descàrrega).

**Transmissions en directe i de càmeres IP:** RTSP — apunta Evervideo a qualsevol URL `rtsp://` i simplement reprodueix. Ideal per a càmeres de seguretat, càmeres de timbre, proveïdors IPTV, monitors de nadons i fonts en directe similars.

**Emmagatzematge d'objectes compatible amb S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre punt final d'API S3.

**Biblioteques al dispositiu:** la biblioteca de Fotos (tots els vídeos, gravacions de pantalla, àlbums de fotos) i la biblioteca de l'app Música (Àlbums, Gèneres, Llistes de reproducció) — tots dos apareixen dins la biblioteca multimèdia perquè no hagis de copiar res.

**Descoberta a la xarxa local:** la secció Dispositius disponibles llista automàticament cada servei Bonjour/mDNS a la xarxa Wi-Fi — servidors Plex, Jellyfin, Emby, Synology, QNAP, encaminadors AirPort amb unitats adjuntes, Apple Time Capsule — perquè puguis tocar per connectar sense escriure una adreça IP.

Cada connexió usa l'SDK oficial o el protocol obert del servei, amb autorització basada en OAuth on s'admet. Pots connectar múltiples comptes del mateix servei (per exemple, dos comptes de Google Drive, o un servidor Plex i un de Jellyfin) i navegar-hi un al costat de l'altre a la secció d'emmagatzematge al núvol.

## Seguretat i privadesa

Evervideo usa únicament SDKs oficials i connexions segures per interactuar amb els serveis al núvol connectats. El teu nom d'usuari i contrasenya no són accessibles a l'aplicació — totes les transferències estan xifrades amb TLS.

Quan introdueixes el teu nom d'usuari i contrasenya, l'aplicació et mostra la pàgina d'autorització oficial del proveïdor de servei al núvol, i tot el procés d'autorització té lloc fora de l'aplicació. El proveïdor de servei al núvol envia un token d'autenticació a l'aplicació després d'una autorització correcta, i aquest token s'usa per fer crides a l'API.

Un token d'autenticació és una clau digital que permet a aplicacions de tercers interactuar amb l'emmagatzematge al núvol en nom teu. El token es guarda al dispositiu a l'emmagatzematge segur del sistema d'Apple (Keychain), que està xifrat en repòs i protegit per la contrasenya del dispositiu o el bloqueig biomètric. Pots descarregar fitxers dels serveis al núvol connectats al dispositiu; aquests fitxers es col·loquen al directori Documents de l'app i es poden eliminar en qualsevol moment usant el gestor de fitxers integrat.

L'aplicació no comparteix cap informació dels teus comptes al núvol connectats amb Everappz, anunciants o tercers. Pots revocar l'accés al teu compte al núvol en qualsevol moment obrint la pàgina de configuració del compte al navegador web.

## Revocar el token d'autenticació

Per revocar un token d'autenticació, inicia sessió al teu compte al núvol en un navegador web i navega fins a la pàgina de seguretat o aplicacions connectades. Allà pots trobar cada aplicació de tercers connectada al teu compte al núvol i eliminar-ne qualsevol si ja no vols usar-la. Les instruccions detallades per a comptes de Google estan disponibles [aquí](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

També pots desconnectar el compte al núvol dins la mateixa aplicació — quan ho fas, el token d'autenticació s'elimina immediatament del dispositiu. Si desinstal·les l'aplicació del dispositiu, totes les dades descarregades i els tokens d'accés s'eliminen automàticament.

## Desconnectar un emmagatzematge al núvol o canviar la configuració

- **Accedeix a les opcions d'emmagatzematge al núvol** — localitza el servei connectat a la secció **Emmagatzematge al núvol** de la pestanya Fitxers.
- **Toca el botó "..."** al costat del títol del servei per obrir opcions addicionals:
  - **Reanomena** — canvia el nom del servei al núvol tal com apareix a la llista.
  - **Configuració** — modifica la configuració o les dades d'autenticació. A vegades pot ser necessari tornar a autoritzar el servei al núvol connectat si el token d'autorització ha caducat.
  - **Desconnectar** — talla completament la connexió entre l'app i el servei al núvol. Això elimina tots els vídeos associats a aquell servei de la biblioteca multimèdia, però els deixa intactes al servidor.

## Connectar a un ordinador o NAS

Pots connectar el teu ordinador, NAS personal o un altre dispositiu de xarxa usant el protocol SMB, WebDAV, FTP/FTPS, SFTP, NFS o DLNA. Aquesta és la manera més fàcil d'introduir una biblioteca multimèdia domèstica existent — tant si es troba en un Mac, un PC amb Windows, un Synology, un QNAP, un Apple Time Capsule o un WD My Cloud Home — a Evervideo sense copiar res.

### Connectar a un ordinador usant SMB

- Toca **Connectar a l'emmagatzematge al núvol → SMB**.
- Introdueix l'adreça IP de l'ordinador i el nom de la carpeta compartida usant el format `smb://computer-ip-address/shared-folder-name`.
- Tria la versió del protocol: **Auto**, **SMB1** o **SMB2**.
- Introdueix el nom d'usuari i la contrasenya (si cal).
- Toca **Fet**.

Si la connexió és correcta, el recurs compartit apareix a la secció d'emmagatzematge al núvol. Un tutorial complet sobre com connectar el Mac o PC usant SMB està disponible [aquí](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Connectar a un NAS usant WebDAV

Tots els passos són els mateixos que per a SMB, excepte el camp URL. Usa `http://server-name` o `https://server-name` si el servidor admet SSL. WebDAV funciona amb Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home i qualsevol altre servidor amb un punt final WebDAV.

Un tutorial complet sobre WebDAV està disponible [aquí](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Connectar via DLNA/UPnP

Comparteix una biblioteca multimèdia al PC amb Windows o NAS usant el protocol DLNA/UPnP i accedeix-hi dins d'Evervideo tal com es descriu [aquí](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA té un suport ampli, però només permet reproduir o descarregar vídeos — no es poden carregar fitxers ni crear carpetes noves en un servidor DLNA.

### Connectar usant FTP, FTPS o SFTP

Evervideo també admet protocols clàssics de transferència de fitxers. Per connectar un servidor via FTP o FTPS, toca Connectar a l'emmagatzematge al núvol → FTP, introdueix l'URL del host en la forma `ftp://server-name` (o `ftps://server-name` per a una connexió xifrada), proporciona el nom d'usuari i la contrasenya i toca Fet. Per a SFTP (protocol de transferència de fitxers SSH), tria SFTP en comptes i proporciona una contrasenya o un parell de claus SSH.

### Connectar a un recurs compartit NFS

Evervideo inclou suport NFS (sistema de fitxers de xarxa) — útil per a amfitrions Linux, servidors BSD i dispositius NAS que prefereixen exposar biblioteques de vídeo via NFS en lloc de SMB. Tria NFS al menú Connectar a l'emmagatzematge al núvol, introdueix l'adreça del servidor i el camí exportat, i toca Fet.

## Connectar un Plex Media Server

Evervideo es pot connectar directament a un Plex Media Server i navegar per les biblioteques de Pel·lícules, Programes de televisió i Vídeos domèstics. Toca Connectar a l'emmagatzematge al núvol → Plex, inicia sessió amb el compte Plex, tria un servidor, i la biblioteca apareix al costat dels serveis al núvol. Els servidors Plex a la mateixa xarxa local es descobreixen automàticament a la secció Dispositius disponibles.

## Connectar un servidor Jellyfin o Emby

Tant Jellyfin (codi obert) com Emby (comercial) funcionen de manera nativa a Evervideo. Toca Connectar a l'emmagatzematge al núvol → Jellyfin o Emby, introdueix l'URL del servidor (normalment quelcom com `http://server-ip:8096`) i les credencials, i la biblioteca estarà llesta per reproduir.

## Connectar un servidor Subsonic o Navidrome

Evervideo parla l'API de Subsonic, el que significa que funciona amb Subsonic, Navidrome i cada altre servidor compatible amb Subsonic — incloent Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) i Ampache. Toca Connectar a l'emmagatzematge al núvol → Subsonic, introdueix l'URL del servidor i les credencials, i la biblioteca apareix a la secció d'emmagatzematge al núvol.

## Connectar una transmissió RTSP (càmeres IP, televisió en directe, IPTV)

Evervideo té suport natiu de RTSP, de manera que pots apuntar-lo a qualsevol font RTSP — càmeres de seguretat, càmeres de timbre, proveïdors IPTV, monitors de nadons, feeds de difusió — i Evervideo extraurà i descodificarà la transmissió en directe. Toca Enllaços en línia → Afegir enllaç, enganxa l'URL completa (`rtsp://camera-ip:port/stream-path`), proporciona el nom d'usuari i la contrasenya si cal, i toca Fet.

## Connectar a l'emmagatzematge d'objectes compatible amb S3

Per a allotjadors i usuaris avançats que usen emmagatzematge d'objectes al núvol, Evervideo inclou un connector compatible amb S3. Toca Connectar a l'emmagatzematge al núvol → Emmagatzematge S3, i introdueix l'URL del punt final, la regió, la clau d'accés, la clau secreta i el nom del bucket. Funciona amb AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre punt final d'API S3.

## Dispositius disponibles

Aquesta secció mostra tots els dispositius a la xarxa local als quals et pots connectar des d'Evervideo via descoberta Bonjour/mDNS — servidors Plex, Jellyfin, Emby, Synology, QNAP, encaminadors AirPort amb unitats adjuntes, Apple Time Capsule, etc. Per establir una connexió:

- Desplaça't fins a la secció Dispositius disponibles a la pestanya Fitxers.
- Toca el dispositiu al qual vols connectar-te.
- Si cal, introdueix les teves dades d'inici de sessió per completar la connexió.

{{< cards cols="1">}}
  {{< card title="" subtitle="Dispositius disponibles a la xarxa local a Evervideo" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive et permet transferir fitxers sense fils des de l'ordinador al dispositiu iOS via qualsevol navegador d'escriptori, Finder o Explorador de fitxers. El dispositiu i l'ordinador han d'estar a la mateixa xarxa Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Wi-Fi Drive a Evervideo" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Activar Wi-Fi Drive

- A la pestanya Fitxers, desplaça't fins a Emmagatzematge al núvol → Connectar via Wi-Fi per obrir la pantalla principal de Wi-Fi Drive.
- (Opcional) Estableix un nom d'usuari i contrasenya per al servidor web integrat.
- Toca Iniciar Wi-Fi Drive.

### Accedir a Wi-Fi Drive des de l'ordinador

- Obre un navegador web a l'ordinador (Chrome, Firefox, Safari, etc.).
- Introdueix l'URL mostrada per l'aplicació.
- Arrossega i deixa anar fitxers de l'ordinador a la pàgina web — començaran a transferir-se al dispositiu iOS.

També pots muntar Wi-Fi Drive directament al **Finder** de macOS (Anar → Connectar al servidor…) o a l'Explorador de fitxers de Windows (Mapejar unitat de xarxa…) i tractar l'iPhone o iPad com una unitat de xarxa normal.

Les instruccions detallades estan disponibles [aquí](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## Compartició de fitxers iTunes/Finder

La compartició de fitxers d'iTunes (ara Compartició de fitxers Finder a macOS Catalina i posteriors) et permet transferir fitxers usant un cable Lightning o USB-C. Connecta el dispositiu, obre el Finder al Mac (o iTunes a Windows), troba Evervideo a la llista d'apps i copia fitxers a la carpeta compartida.

## Connectar una unitat USB o targeta SD

Connecta una unitat USB o targeta SD a l'iPhone, iPad o Mac via l'adaptador Lightning-to-USB/USB-C o el lector de targetes. Obre Fitxers → Fitxers en aquest iPhone → Obrir carpeta, navega fins a la unitat i tria un fitxer de vídeo o una carpeta. Evervideo reprodueix els fitxers directament des de la unitat sense copiar-los a l'emmagatzematge intern — útil per a biblioteques 4K molt grans.

## Navegació per carpetes en emmagatzemaments connectats

Toca qualsevol servei al núvol connectat per obrir el seu navegador de fitxers. Les carpetes mostren miniatures de vídeo quan estan disponibles, i tocar un vídeo inicia la reproducció immediatament mentre continua transmetent la resta del fitxer en segon pla.

{{< cards cols="1">}}
  {{< card title="" subtitle="Navegació per carpetes en emmagatzemaments connectats a Evervideo" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Accés ràpid

La secció d'accés ràpid es troba a la part superior de la pestanya Fitxers. Et proporciona accés ràpid als fitxers i carpetes preferits i oberts recentment — tant de serveis al núvol com d'emmagatzematge al dispositiu. Quan obres un fitxer o carpeta del núvol, s'afegeix a la llista d'obertures recents. Pots marcar carpetes profundament niades com a Preferits per accedir-hi ràpidament sense haver de navegar per l'estructura de directoris.

{{< cards cols="1">}}
  {{< card title="" subtitle="Enllaços en línia i accés ràpid a Evervideo" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Fitxers d'aquesta aplicació

Aquesta secció mostra els fitxers i carpetes emmagatzemats al directori Documents protegit per sandbox d'Evervideo — tot el que has descarregat del núvol, transferit via Wi-Fi Drive, copiat a través de Compartició de fitxers Finder o importat d'una altra app.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fitxers d'aquesta aplicació a Evervideo" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Carpeta Documents

La carpeta Documents és l'arrel de tot dins de Fitxers d'aquesta aplicació. Pots crear subcarpetes, reanomenar fitxers, moure'ls i organitzar-los com vulguis.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fitxers locals d'Evervideo — Carpeta Documents" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Fitxers en aquest iPhone/iPad/Mac

Aquesta secció mostra els vídeos ubicats al dispositiu però en aplicacions diferents. Pots importar-los a Evervideo usant el selector de fitxers del sistema:

- Toca Obrir fitxers… per seleccionar fitxers específics.
- Toca Obrir carpeta… per seleccionar una carpeta completa.

També pots usar Connectar una carpeta per crear un enllaç a una carpeta del dispositiu amb accés de lectura/escriptura — perfecte per treballar amb una carpeta a iCloud Drive o una unitat USB adjunta sense copiar res.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fitxers en aquest dispositiu a Evervideo" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Carpetes especials

Dins de la pestanya Fitxers veuràs diverses carpetes especials que Evervideo crea i usa automàticament:

- **Descarregues** — cada fitxer descarregat del núvol apareix aquí per defecte. Personalitza a Configuració → Gestor de fitxers → Desar fitxers descarregats a.
- **Memòria cau del reproductor** — la memòria cau del reproductor multimèdia. Per defecte, el reproductor descarrega els vídeos pròxims per a una reproducció fluida. Pots desactivar la memòria cau a la configuració de l'app o simplement eliminar aquesta carpeta.
- **iCloud** — els fitxers d'aquesta carpeta es sincronitzen a tots els dispositius connectats al mateix compte iCloud.
- **Carpetes fora de línia** — quan marques una carpeta, llista de reproducció, àlbum o gènere com a disponible fora de línia, els fitxers es descarreguen a aquesta carpeta.

## Barra d'eines superior

La barra d'eines superior, ubicada sota la barra de navegació, ofereix diverses accions que pots mostrar o amagar amb un gest de desplaçament cap avall:

- **Cerca** — realitza una cerca dins de la carpeta o secció actual.
- **Continuar reproducció** — si s'activa a la configuració, restaura la cua del reproductor i l'última posició del vídeo per a la carpeta actual.
- **Reproduir-ho tot** — escaneja la carpeta actual i les subcarpetes i afegeix els fitxers a la cua del reproductor.
- **Reproduir aleatòriament** — com Reproduir-ho tot, però barreja abans d'afegir.

## Opcions de carpeta

Quan obres una carpeta, toca el botó **"..."** a la cantonada superior dreta per a aquestes accions:

- **Seleccionar** — activa el mode de selecció de fitxers.
- **Nova carpeta** — crea una nova carpeta dins de la carpeta actual.
- **Activar el mode fora de línia** — activa la sincronització fora de línia per a la carpeta actual. Els fitxers nous afegits en línia es descarreguen automàticament.
- **Carregar fitxers** — carrega fitxers del dispositiu a la carpeta en línia.
- **Cerca** — cerca dins de la carpeta.
- **Ordenar** — ordena els fitxers per nom, mida, data de modificació o metadades.
- **Vista en quadrícula/llista** — commuta entre la vista de taula i la vista de miniatures. La vista de miniatures mostra grans previsualitzacions del pòster del vídeo.

## Mode de selecció

Toca **"..."** a la cantonada superior dreta i tria **Seleccionar** per entrar al mode de selecció. Apareixen caselles de verificació al costat de cada fitxer i carpeta. Toca per seleccionar un o diversos elements i realitza accions en lot: Reproduir a continuació, Reproduir més tard, Afegir a la biblioteca multimèdia, Afegir a una llista de reproducció, Copiar, Carregar, Moure, Reanomenar o Eliminar.

{{< cards cols="1">}}
  {{< card title="" subtitle="Mode de selecció al gestor de fitxers d'Evervideo" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Si prefereixes tractar l'emmagatzematge al núvol connectat com a només lectura (per evitar eliminacions accidentals), activa Configuració → Gestor de fitxers → Editar fitxers en línia → Desactivat per amagar totes les operacions destructives de la interfície.

## Accions de fitxer

Toca la icona **"..."** a prop del títol d'un fitxer per revelar el menú d'accions:

- **Reproduir a continuació** — insereix el fitxer a la part superior de la cua del reproductor.
- **Reproduir més tard** — afegeix el fitxer al final de la cua del reproductor.
- **Afegir a la biblioteca multimèdia** — incorpora el fitxer a la biblioteca multimèdia, organitzat per àlbum i gènere.
- **Afegir a una llista de reproducció** — afegeix el fitxer a una llista de reproducció existent o crea'n una de nova.
- **Editar etiquetes** — obre l'editor d'etiquetes integrat per modificar metadades. Per als fitxers en línia, el fitxer es descarrega temporalment, s'edita i es torna a carregar després de confirmar.
- **Afegir als preferits** — afegeix el fitxer a la llista de preferits per a un accés ràpid.
- **Descarregar** — descarrega el fitxer o carpeta al dispositiu per a ús fora de línia.
- **Reanomenar** — reanomena el fitxer directament a l'emmagatzematge remot.
- **Moure** — mou el fitxer a una carpeta diferent dins de l'emmagatzematge al núvol.
- **Afegir a l'arxiu** — empaqueta el fitxer en un sol fitxer ZIP (funció Premium).
- **Obrir amb** — exporta el fitxer a una altra app compatible via el full de compartició del sistema.
- **Eliminar** — elimina permanentment el fitxer. **Aquesta acció no es pot desfer.**

## Accions de carpeta

Per a cada carpeta de l'emmagatzematge al núvol, tens moltes accions disponibles tocant la icona **"..."** al costat del títol de la carpeta.

- **Reproduir-ho tot** — substitueix la cua actual del reproductor per tots els vídeos de la carpeta.
- **Reproduir a continuació / Reproduir més tard** — afegeix tota la carpeta a la cua.
- **Afegir a la biblioteca multimèdia** — incorpora el contingut de la carpeta a la biblioteca multimèdia.
- **Afegir a la llista de reproducció** — afegeix tota la carpeta a una llista de reproducció.
- **Afegir als preferits** — afegeix la carpeta als preferits.
- **Activar el mode fora de línia** — més enllà d'una descàrrega simple, monitora contínuament la carpeta per buscar fitxers nous i els descarrega automàticament quan apareixen en línia.
- **Descarregar** — descarrega tots els continguts de la carpeta al dispositiu per a accés fora de línia.
- **Reanomenar / Moure** — reanomena o mou la carpeta a l'emmagatzematge remot.
- **Afegir a l'arxiu** — empaqueta el contingut de la carpeta en un fitxer ZIP (funció Premium).
- **Eliminar** — elimina permanentment la carpeta i el seu contingut. **Aquesta acció no es pot desfer.**

## Cua de transferències

A la cantonada superior dreta de la pestanya Fitxers hi ha un botó **Transferències** (icona de fletxes giratòries). Toca'l per obrir la cua de transferències — una llista de cada descàrrega i càrrega activa de totes les fonts, amb progrés en temps real, velocitat i ETA per fitxer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Cua de transferències de fitxers d'Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Pots pausar, reprendre, reintentar transferències fallides, reordenar elements per prioritzar descàrregues específiques o cancel·lar-les individualment. També pots ajustar la velocitat de la cua de transferències (màxim de tasques en paral·lel), el tipus de xarxa (només Wi-Fi o Wi-Fi + Dades mòbils) i les transferències en segon pla a Configuració → Gestor de fitxers.

{{< cards cols="1">}}
  {{< card title="" subtitle="Accions a la cua de transferències de fitxers d'Evervideo" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Mode fora de línia i carpetes fora de línia sincronitzades

El mode fora de línia és una funció pràctica que et permet veure els teus vídeos preferits fins i tot quan no tens connexió a Internet. Quan actives el mode fora de línia per a qualsevol carpeta, llista de reproducció, àlbum o gènere, tots els fitxers d'aquella col·lecció es descarreguen automàticament al dispositiu per a reproducció fora de línia. Apareixen a la secció Carpetes fora de línia.

Quan afegeixis nous fitxers al servidor remot, també es descarreguen automàticament — de manera que la col·lecció fora de línia es manté actualitzada sense que hagis de fer res. Per tornar a sincronitzar manualment, toca els tres punts a la cantonada superior dreta d'una carpeta fora de línia i selecciona Sincronitzar.

Pots ajustar el temps d'espera de sincronització a Configuració → Gestor de fitxers → Carpetes offline sincronitzades → Interval de temps.

Les instruccions detallades estan disponibles [aquí](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personalització

A Configuració → Personalització pots configurar com es presenta la pestanya Fitxers:

- **Estil de pantalla de fitxers** — Menú pla (mostra directament la llista de carpetes) o Menú agrupat (agrupa el contingut per categoria — Accés ràpid, Carpetes especials, Emmagatzematge al núvol, etc.).
