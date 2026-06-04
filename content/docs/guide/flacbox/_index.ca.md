---
date: 2020-01-01
title: 'Flacbox'
description: "Aprèn a usar Flacbox — el reproductor de música al núvol d'alta resolució compatible amb FLAC, DSD, ALAC i FFmpeg per a iPhone, iPad i Mac. Connecta iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB i DLNA. Reprodueix i descarrega àudio d'alta resolució, edita metadades, escolta audiollibres, fes scrobbling a Last.fm, usa Apple CarPlay i ginys de pantalla d'inici, i personalitza l'equalitzador de 10 bandes."
keywords: [
  "guia d'usuari Flacbox", "com usar Flacbox", "reproductor de música alta resolució iPhone", "reproductor FLAC iPhone",
  "reproductor DSD iOS", "reproductor ALAC Mac", "app de música sense pèrdues", "reproductor de música al núvol iPhone",
  "reproductor FLAC offline Mac", "gestor de biblioteca musical", "editor d'etiquetes d'àudio",
  "reproductor FLAC CarPlay", "app d'àudio Chromecast", "música AirPlay 2",
  "ginys Flacbox", "Flacbox CarPlay", "reproductor de música FFmpeg iOS",
  "reproductor d'audiollibres iPhone", "marcadors d'àudio iOS", "app de correcció de to",
  "freqüència de mostreig de sortida d'àudio", "DAC extern iPhone", "USB DAC Mac",
  "app de música Synology", "app de música QNAP", "reproductor de música NAS iPhone",
  "reproductor de música WebDAV", "streaming de música SMB", "reproductor de música DLNA",
  "música iCloud Drive", "Google Drive FLAC", "reproductor FLAC Dropbox",
  "transferència de música Wi-Fi Drive", "importació de llista M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "guia", "alta resolució", "FLAC", "FFmpeg", "núvol", "CarPlay", "ginys"]
---


### Benvingut a la guia de Flacbox

Flacbox és un reproductor de música d'alta resolució per a iPhone, iPad i Mac que et permet convertir el teu emmagatzematge al núvol favorit, els NAS i els servidors multimèdia en el teu propi servei de streaming personal.

Flacbox es connecta a una llista extraordinàriament àmplia de fonts, totes en una sola app:

- **Emmagatzematge al núvol personal:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidors autoallotjats:** Plex · Jellyfin · Emby · Subsonic (i tots els servidors compatibles amb Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (i ownCloud mitjançant l'API compartida) · Synology Drive · QNAP.
- **Protocols NAS i de compartició de fitxers:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (contrasenya o autenticació per clau pública) · NFS · DLNA / UPnP (reproducció i descàrrega). Funciona amb Apple Time Capsule, Synology, QNAP, WD My Cloud, qualsevol host Linux Samba / NFS / SSH, o una carpeta compartida al teu Mac o Windows PC.
- **Emmagatzematge d'objectes compatible amb S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre punt de connexió S3-API.
- **Descoberta a la xarxa local:** La secció Dispositius disponibles llista automàticament tots els serveis Bonjour / mDNS de la teva Wi-Fi — servidors Plex, Jellyfin, Emby, Synology, QNAP, routers AirPort amb unitats connectades, Time Capsule — perquè puguis connectar-te amb un toc sense escriure una adreça IP.

Mentre la majoria de reproductors de música es limiten al motor d'àudio integrat d'Apple, Flacbox inclou **FFmpeg** juntament amb els còdecs del sistema per poder reproduir formats que iOS no admet de fàbrica — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, a més de la família habitual MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. Combinat amb una freqüència de mostreig de sortida d'àudio configurable (44,1 / 48 / 64 / 88,2 / 96 kHz), sortida multicanal (Mono → 5.1 → SDDS → ITU BS.775-1), ajust del buffer IO i correcció de to, Flacbox ofereix als audiòfils un control que la majoria d'apps de música de consum simplement no ofereixen.

### Gaudeix del Streaming Fluid i la Reproducció Offline

Flacbox disposa d'un buffer intel·ligent per a un streaming fluid i un gestor de descàrregues integrat perquè puguis baixar llistes de reproducció, artistes, àlbums, carpetes o pistes individuals al teu dispositiu per a ús offline. Quan l'emmagatzematge s'esgota, elimina els fitxers en memòria cau amb un sol toc i continua fent streaming des del núvol. El mode offline per a carpetes, llistes de reproducció, àlbums i artistes també sincronitza automàticament les pistes noves en el moment en què apareixen al núvol, de manera que la teva col·lecció offline sempre es manté actualitzada.

### Biblioteca Musical Organitzada Automàticament

Quan importes pistes d'àudio, Flacbox n'escaneja les metadades i les organitza en una biblioteca musical neta — agrupades per Cançons, Cançons no reproduïdes, Àlbums, Artistes d'àlbum, Artistes, Gèneres i Compositors. Usa la cerca integrada per trobar qualsevol cosa en segons, filtra per font (núvol en línia / offline / dispositiu), i tria entre els dissenys de biblioteca Simple / Agrupat / Per pestanyes. Per a biblioteques amb compilacions de 'diversos artistes', Flacbox ofereix vistes dedicades Tots els àlbums / Àlbums exclusius / Àlbums en solitari per mostrar els resultats correctes sense soroll.

### Corregeix Metadades i Etiqueta la Teva Música

Si trobes etiquetes corruptes o codificacions desordenades (un problema habitual en fitxers rippats o antics), l'editor d'etiquetes ID3 integrat les pot netejar — manualment o amb cerques automàtiques a MusicBrainz. També pots normalitzar codificacions de caràcters trencades (ideal per a etiquetes en ciríl·lic, japonès o xinès provinents de PC Windows), cercar portades d'àlbum que falten, i escriure els canvis de tornada al fitxer original al núvol automàticament. Per a una edició per lots més profunda, instal·la la nostra app complementària Evertag.

### Transferències Fàcils des de Mac, PC o NAS

Mou música entre el teu ordinador i el teu iPhone o iPad amb qualsevol d'aquestes eines: SMB, WebDAV, DLNA, Wi-Fi Drive (arrossega i deixa anar a qualsevol navegador d'escriptori), compartició de fitxers iTunes / Finder per un cable Lightning o USB-C, unitats de memòria USB o iXpand Flash Drives. Tens un Apple Time Capsule, WD My Cloud, Synology, QNAP o qualsevol altre NAS que exposi SMB / WebDAV / DLNA / FTP / SFTP? Connecta't una vegada i transmet tota la teva biblioteca sense ocupar cap espai al dispositiu.

### Personalitza el So amb l'Equalitzador

Flacbox inclou un equalitzador de 10 bandes amb preajustos estil iPod (Acústic, Potenciador de greus, Clàssic, Dance, Rock, Pop, Jazz i molts més), un preamplificador, i la capacitat de desar els teus propis preajustos. Tant si estàs ajustant el so per a uns auriculars IEM d'audiòfil, un HomePod mini o un equip de so de cotxe, pots modelar el so exactament com t'agrada.

### Compatible amb Audiollibres

Flacbox és un excel·lent reproductor d'audiollibres — múltiples marcadors per pista, velocitat de reproducció de gra fi (0,02× a 3,00×), continuació de la reproducció per reprendre exactament on ho vas deixar, botons de salt personalitzables i un temporitzador de son que s'esvaeix suaument a l'hora d'anar a dormir. Les marques de capítol M4B i els fitxers llargs estan totalment suportats.

### Reprodueix a Qualsevol Lloc — Inclòs el Teu Cotxe i la Pantalla d'Inici

Reprodueix música a Apple TV / HomePod via AirPlay 2, envía-la als altaveus Google Chromecast i televisions compatibles amb Cast, i porta-ho tot a la carretera amb Apple CarPlay. Usa ginys de pantalla d'inici a iPhone i iPad per veure la pista actual d'un cop d'ull, i el scrobbling de Last.fm per mantenir el teu historial d'escolta a totes les apps.

### Privadesa i Seguretat

Flacbox utilitza només SDK oficials i inicis de sessió basats en OAuth de cada proveïdor al núvol — la teva contrasenya mai arriba a l'app. Els tokens d'accés es guarden xifrats al iOS Keychain, totes les transferències estan protegides per TLS, i revocar l'accés al teu compte al núvol o eliminar Flacbox del dispositiu ho elimina tot immediatament. Protegeix la teva biblioteca amb un codi d'accés opcional per a una capa addicional de privadesa.

### Primers Passos amb Flacbox

Aquesta guia t'explica cada part de Flacbox a iPhone, iPad i Mac — des de connectar serveis al núvol, organitzar la teva biblioteca, transferir fitxers i gestionar llistes de reproducció, fins a ajustar l'equalitzador i configurar el motor d'àudio. Usa les targetes de sota per saltar directament a la secció que necessites.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navegació" subtitle="Barra de pestanyes a iPhone, Menú esquerre a iPad i Mac, reproductor en miniatura, ginys, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Connexions" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Biblioteca musical" subtitle="Cançons, Àlbums, Artistes, Gèneres, Compositors — sincronitza, cerca, edita metadades." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Llistes de reproducció" subtitle="Crea, importa M3U / M3U8 / CUE, reordena i exporta a M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Fitxers locals" subtitle="Música offline, unitats USB, Wi-Fi Drive, gestor de fitxers, carpetes offline." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Reproductor d'àudio" subtitle="Sortida d'alta resolució, equalitzador, to, marcadors, AirPlay, Chromecast, velocitat, temporitzador de son." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Configuració" subtitle="Motor d'àudio, biblioteca, gestor de fitxers, CarPlay, ginys, personalització, idioma, còpia de seguretat." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="Preguntes freqüents" subtitle="Troba respostes a les 50 preguntes més habituals sobre Flacbox." >}}

{{< /cards >}}
