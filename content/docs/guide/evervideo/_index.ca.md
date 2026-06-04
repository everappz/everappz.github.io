---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: "Aprèn a usar Evervideo — el reproductor de vídeo al núvol tot en un per a iPhone, iPad i Mac. Reprodueix i descarrega vídeos des d'iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP/SFTP, DLNA i S3 — a més de Plex, Jellyfin, Emby, Subsonic i Navidrome. Picture-in-Picture, subtítols primaris i secundaris, equalitzadors d'àudio i vídeo, transmissions RTSP de càmeres IP, Chromecast, AirPlay 2, descodificació per maquinari H.264/HEVC, integració de biblioteca de Fotos i Apple Music, i un reproductor compacte sempre visible."
keywords: [
  "guia Evervideo", "com usar Evervideo", "reproductor de vídeo al núvol iPhone", "reproductor de vídeo Mac",
  "reproductor MKV iOS", "reproductor de vídeo FFmpeg", "reproductor HEVC iPhone",
  "Picture-in-Picture vídeo iPhone", "reproductor PiP vídeo iPad",
  "reproductor RTSP iPhone", "visor càmera IP", "reproductor DLNA vídeo",
  "client Plex iPhone", "client Jellyfin iOS", "client Emby iPad",
  "reproductor subtítols iOS", "subtítols SRT VTT ASS", "subtítols secundaris iPhone",
  "equalitzador vídeo iOS", "equalitzador àudio reproductor vídeo", "DAC extern vídeo",
  "reproduir vídeo Google Drive", "reproduir vídeo Dropbox",
  "reproduir vídeo OneDrive", "reproduir vídeo iCloud Drive",
  "reproduir vídeo MEGA", "reproduir vídeo NAS",
  "Chromecast vídeo iPhone", "AirPlay 2 vídeo", "reproductor vídeo iCloud",
  "reproductor vídeo biblioteca Fotos", "reproductor vídeo Apple Music",
  "transferència vídeo Wi-Fi Drive", "llista de reproducció vídeo M3U",
  "Evervideo Premium", "aplicació vídeo Family Sharing"
]
tags: ["evervideo", "guia", "reproductor de vídeo", "PiP", "subtítols", "RTSP", "núvol", "FFmpeg"]
---


### Benvingut a la guia d'Evervideo

Evervideo és un reproductor de contingut multimèdia al núvol complet per a iPhone, iPad i Mac que converteix qualsevol compte d'emmagatzematge al núvol, NAS o servidor multimèdia en la teva biblioteca personal, sense necessitat de tornar a carregar res i mantenint el control total dels teus fitxers.

Construït sobre un motor de reproducció personalitzat basat en FFmpeg amb descodificació H.264 i HEVC accelerada per maquinari, Evervideo reprodueix pràcticament qualsevol contenidor i còdec modern — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS i els formats FFmpeg de llarga cua — amb qualitat total, amb memòria intermèdia intel·ligent per a una transmissió fluida per Wi-Fi o dades mòbils. Picture-in-Picture manté el vídeo sobre qualsevol altra aplicació, el reproductor compacte sempre visible permet continuar veient mentre navegues per la biblioteca, i Chromecast i AirPlay 2 envien la reproducció al televisor, HomePod o sistema d'altaveus amb una sola pulsació.

Evervideo es connecta a una llista remarkablement àmplia de fonts, tot des d'una sola aplicació:

- **Emmagatzematge al núvol personal:** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Servidors multimèdia allotjats localment:** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (i ownCloud via l'API compartida) · Synology Drive · QNAP.
- **Protocols NAS i de compartició de fitxers:** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP/HTTPS) · FTP · FTPS · SFTP (contrasenya o autenticació de clau pública) · NFS · DLNA · UPnP.
- **Transmissions en directe i de càmeres IP:** RTSP — apunta Evervideo a qualsevol URL RTSP (`rtsp://camera-ip/stream`) i simplement reprodueix.
- **Emmagatzematge d'objectes compatible amb S3:** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces i qualsevol altre punt final d'API S3.
- **Fonts al dispositiu:** la biblioteca de Fotos (Tots els vídeos, Curts/Mitjans/Llargs, Gravacions de pantalla, i els teus Àlbums de fotos), la biblioteca de l'app Música (Àlbums, Gèneres, Llistes de reproducció), unitats USB/SD i Fitxers locals.

### Un reproductor per a tots els formats i còdecs

On la majoria d'apps iOS s'aturen a H.264/H.265 dins de MP4/MOV, Evervideo inclou FFmpeg al costat dels còdecs del sistema d'Apple perquè puguis reproduir formats que el sistema no reconeix — contenidors MKV, VP9, AV1, MPEG-2, OGG, Vorbis i molts més — i canvia automàticament entre la descodificació per maquinari H.264/HEVC i la descodificació per programari en funció del fitxer i el dispositiu.

Pots triar la pista de vídeo (còpies Blu-ray de múltiples fluxos), la pista d'àudio (pistes de comentaris, doblatges alternatius) i la pista de subtítols. Els fitxers de subtítols externs SRT, VTT i ASS/SSA es carreguen amb una sola pulsació; l'estil avançat ASS/SSA es renderitza correctament gràcies a la biblioteca libass inclosa.

### Subtítols intel·ligents

- **Selecció de pista de subtítols** perfecta per a l'aprenentatge d'idiomes.
- **Fitxers de subtítols externs** (`.srt`, `.vtt`, `.ass`, `.ssa`) carregats des de qualsevol lloc del dispositiu o des del núvol.
- **libass** per a la renderització completa d'estils ASS/SSA.
- **Selecció de font per pista i global** per als subtítols.
- **Selecció de pista d'àudio** tria el doblatge, comentari o pista del director.
- **Selecció de pista de vídeo** per a fitxers de múltiples angles o versions.

### Ajusta la imatge i el so

Dos equalitzadors, un al costat de l'altre: un equalitzador d'àudio per ajustar els greus i aguts (amb importació/exportació de presets personalitzats), i un equalitzador de vídeo per ajustar la brillantor, el contrast, la saturació i el to (també amb importació/exportació). Tots dos motors també exposen controls audiòfils: freqüència de mostreig de sortida d'àudio, nombre de canals, durada del buffer IO i mode mixt — per a usuaris amb DACs externs i receptors de cinema a casa.

### Cast, AirPlay i Picture-in-Picture

- **Picture-in-Picture (PiP):** continua veient mentre uses altres apps.
- **AirPlay 2:** envia vídeo a Apple TV, HomePod o qualsevol altaveu/televisió compatible amb AirPlay 2.
- **Google Chromecast:** retransmet directament a un Chromecast o televisió habilitada per a Cast.
- **Reproductor compacte:** un mini reproductor persistent a la part superior de cada pantalla per poder navegar per la biblioteca sense perdre el vídeo.

### Privadesa i seguretat

Evervideo usa SDKs oficials i inicis de sessió basats en OAuth de cada proveïdor al núvol, de manera que la teva contrasenya no arriba mai a l'app. Els tokens d'accés es guarden xifrats al Keychain iOS/MacOS, cada transferència està protegida per TLS, i revocar l'accés des del teu compte al núvol (o eliminar Evervideo del dispositiu) esborra tot de manera instantània. Protegeix la teva biblioteca amb un codi d'accés opcional de 4 dígits per a una capa addicional de privadesa.

### Primers passos amb Evervideo

Aquesta guia t'explica cada part d'Evervideo a iPhone, iPad i Mac — des de connectar serveis al núvol, navegar per la biblioteca, descarregar i transferir fitxers, gestionar llistes de reproducció, fins a ajustar el reproductor multimèdia, els equalitzadors, els subtítols i Picture-in-Picture. Usa les targetes de sota per saltar directament a la secció que necessites.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navegació" subtitle="Barra de pestanyes a iPhone, menú lateral a iPad i Mac, reproductor multimèdia compacte sempre visible." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Fitxers" subtitle="Una pestanya unificada per al núvol, NAS, transmissions RTSP, fitxers locals, unitats USB i la cua de transferències." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Biblioteca multimèdia" subtitle="Navega per Àlbums, Gèneres, Recents, Preferits — a més de la biblioteca de Fotos iOS i la biblioteca Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Llistes de reproducció" subtitle="Crea llistes de reproducció des del núvol, local, Fotos o biblioteca de Música, importa M3U/M3U8/CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Reproductor multimèdia" subtitle="Picture-in-Picture, pistes d'àudio i vídeo, subtítols, equalitzadors d'àudio i vídeo, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Configuració" subtitle="Motor d'àudio, descodificador de vídeo, subtítols, biblioteca, gestor de fitxers, ginys, personalització, idioma, còpia de seguretat." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="Preguntes freqüents" subtitle="Troba respostes a les preguntes més habituals sobre Evervideo." >}}

{{< /cards >}}
