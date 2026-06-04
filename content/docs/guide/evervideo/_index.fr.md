---
date: 2020-01-01
lastmod: 2026-06-01
title: 'Evervideo'
description: "Apprenez à utiliser Evervideo — le lecteur vidéo cloud tout-en-un pour iPhone, iPad et Mac. Diffusez et téléchargez des vidéos depuis iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB, NFS, FTP / SFTP, DLNA et S3 — ainsi que Plex, Jellyfin, Emby, Subsonic et Navidrome. Picture-in-Picture, sous-titres primaires et secondaires, égaliseurs audio et vidéo, flux RTSP de caméras IP, Chromecast, AirPlay 2, décodage matériel H.264 / HEVC, intégration des bibliothèques Photos et Apple Music, et un lecteur compact toujours visible."
keywords: [
  "guide Evervideo", "comment utiliser Evervideo", "lecteur vidéo cloud iPhone", "lecteur vidéo Mac",
  "lecteur MKV iOS", "lecteur vidéo FFmpeg", "lecteur HEVC iPhone",
  "Picture-in-Picture vidéo iPhone", "lecteur PiP vidéo iPad",
  "lecteur RTSP iPhone", "visionneuse caméra IP", "lecteur vidéo DLNA",
  "client Plex iPhone", "client Jellyfin iOS", "client Emby iPad",
  "lecteur sous-titres iOS", "sous-titres SRT VTT ASS", "sous-titres secondaires iPhone",
  "égaliseur vidéo iOS", "égaliseur audio lecteur vidéo", "DAC externe vidéo",
  "diffuser vidéo depuis Google Drive", "diffuser vidéo depuis Dropbox",
  "diffuser vidéo depuis OneDrive", "diffuser vidéo depuis iCloud Drive",
  "diffuser vidéo depuis MEGA", "diffuser vidéo depuis NAS",
  "Chromecast vidéo iPhone", "AirPlay 2 vidéo", "lecteur vidéo iCloud",
  "lecteur vidéo bibliothèque Photos", "lecteur vidéo Apple Music",
  "transfert vidéo Wi-Fi Drive", "playlist vidéo M3U",
  "Evervideo Premium", "app vidéo Family Sharing"
]
tags: ["evervideo", "guide", "lecteur vidéo", "PiP", "sous-titres", "RTSP", "cloud", "FFmpeg"]
---


### Bienvenue dans le guide Evervideo

Evervideo est un lecteur multimédia cloud complet pour iPhone, iPad et Mac qui transforme n'importe quel compte de stockage cloud, NAS ou serveur multimédia en votre bibliothèque multimédia personnelle, sans avoir besoin de ré-uploader quoi que ce soit et tout en conservant un contrôle total sur vos fichiers.

Construit sur un moteur de lecteur personnalisé basé sur FFmpeg avec décodage matériel accéléré H.264 et HEVC, Evervideo lit pratiquement tous les conteneurs et codecs modernes — MP4, MKV, AVI, MOV, FLV, WMV, WebM, TS, M2TS et les nombreux formats FFmpeg — en pleine qualité, avec une mise en mémoire tampon intelligente pour une diffusion fluide via Wi-Fi ou réseau cellulaire. Picture-in-Picture maintient votre vidéo au-dessus de toutes les autres applications, le lecteur compact toujours visible vous permet de continuer à regarder tout en parcourant votre bibliothèque, et Chromecast et AirPlay 2 envoient la lecture sur votre TV, HomePod ou système audio en un seul geste.

Evervideo se connecte à une liste remarquablement large de sources, le tout depuis une seule application :

- **Stockage cloud personnel :** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Serveurs multimédias auto-hébergés :** Plex · Jellyfin · Emby · Subsonic · Navidrome · Nextcloud (et ownCloud via l'API partagée) · Synology Drive · QNAP.
- **NAS et protocoles de partage de fichiers :** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (mot de passe ou authentification par clé publique) · NFS · DLNA · UPnP.
- **Flux live et caméras IP :** RTSP — pointez Evervideo sur n'importe quelle URL RTSP (`rtsp://camera-ip/stream`) et ça joue.
- **Stockage objet compatible S3 :** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, et tout autre endpoint S3.
- **Sources sur l'appareil :** la bibliothèque Photos (Toutes les vidéos, Courtes / Moyennes / Longues, Enregistrements d'écran, plus vos Albums Photo), la bibliothèque de l'app Musique (Albums, Genres, Listes de lecture), lecteurs USB / SD, et Fichiers locaux.

### Un lecteur pour tous les formats et codecs

Là où la plupart des applications iOS s'arrêtent à H.264 / H.265 dans MP4 / MOV, Evervideo intègre FFmpeg aux côtés des codecs système d'Apple pour lire les formats non reconnus par le système — conteneurs MKV, VP9, AV1, MPEG-2, OGG, Vorbis, et bien d'autres — et bascule automatiquement entre le décodage matériel H.264 / HEVC et le décodage logiciel selon le fichier et l'appareil.

Vous pouvez choisir la piste vidéo (rips Blu-ray multi-flux), la piste audio (pistes de commentaires, doublages alternatifs) et la piste de sous-titres. Les fichiers de sous-titres externes SRT, VTT et ASS / SSA se chargent en un tap ; le rendu avancé ASS / SSA est correctement affiché grâce à libass intégré.

### Sous-titres intelligents

- **Sélection de piste de sous-titres** parfaite pour l'apprentissage des langues.
- **Fichiers de sous-titres externes** (`.srt`, `.vtt`, `.ass`, `.ssa`) chargés depuis n'importe où sur votre appareil ou depuis le cloud.
- **libass** pour un rendu ASS / SSA entièrement stylisé.
- **Sélection de police par piste et globale** pour les sous-titres.
- **Sélection de piste audio** — choisissez le doublage, le commentaire ou la piste du réalisateur.
- **Sélection de piste vidéo** pour les fichiers multi-angles ou multi-versions.

### Ajustez l'image et le son

Deux égaliseurs, côte à côte : un égaliseur audio pour régler les basses et les aigus (avec importation / exportation de préréglages personnalisés), et un égaliseur vidéo pour ajuster la luminosité, le contraste, la saturation et la teinte (également avec importation / exportation). Les deux moteurs exposent également des contrôles audiophiles : taux d'échantillonnage de sortie audio, nombre de canaux, durée du tampon IO et mode mixte — pour les utilisateurs avec des DAC externes et des récepteurs home cinéma.

### Cast, AirPlay et Picture-in-Picture

- **Picture-in-Picture (PiP) :** continuez à regarder pendant que vous utilisez d'autres applications.
- **AirPlay 2 :** envoyez la vidéo vers Apple TV, HomePod ou n'importe quel haut-parleur / TV AirPlay 2.
- **Google Chromecast :** diffusez directement vers un Chromecast ou une TV compatible Cast.
- **Lecteur compact :** un mini-lecteur persistant au-dessus de chaque écran pour parcourir votre bibliothèque sans perdre la vidéo.

### Confidentialité et sécurité

Evervideo utilise des SDK officiels et des connexions OAuth de chaque fournisseur cloud afin que votre mot de passe n'atteigne jamais l'application. Les jetons d'accès sont stockés chiffrés dans le Keychain iOS/macOS, chaque transfert est protégé par TLS, et révoquer l'accès depuis votre compte cloud (ou supprimer Evervideo de l'appareil) supprime tout instantanément. Protégez votre bibliothèque avec un code à 4 chiffres optionnel pour une couche de confidentialité supplémentaire.

### Premiers pas avec Evervideo

Ce guide vous guide à travers chaque partie d'Evervideo sur iPhone, iPad et Mac — de la connexion aux services cloud, la navigation dans votre bibliothèque, le téléchargement et le transfert de fichiers, la gestion des listes de lecture, jusqu'au réglage fin du lecteur multimédia, des égaliseurs, des sous-titres et de Picture-in-Picture. Utilisez les cartes ci-dessous pour accéder directement à la section dont vous avez besoin.<br><br>

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/evervideo/evervideo-guide-navigation" title="Navigation" subtitle="Barre d'onglets sur iPhone, menu gauche sur iPad et Mac, lecteur multimédia compact toujours visible." >}}

{{< card icon="folder" link="/docs/guide/evervideo/evervideo-guide-files" title="Fichiers" subtitle="Un onglet unifié pour le cloud, NAS, flux RTSP, fichiers locaux, lecteurs USB et la file de transferts." >}}

{{< card icon="collection" link="/docs/guide/evervideo/evervideo-guide-video-library" title="Médiathèque" subtitle="Parcourez par Albums, Genres, Récents, Favoris — plus la bibliothèque iOS Photos et la bibliothèque Apple Music." >}}

{{< card icon="music-note" link="/docs/guide/evervideo/evervideo-guide-playlists" title="Listes de lecture" subtitle="Créez des listes de lecture depuis le cloud, les fichiers locaux, Photos ou la bibliothèque Musique, importez M3U / M3U8 / CUE." >}}

{{< card icon="play" link="/docs/guide/evervideo/evervideo-guide-player" title="Lecteur multimédia" subtitle="Picture-in-Picture, pistes audio et vidéo, sous-titres, égaliseurs audio + vidéo, AirPlay, Chromecast." >}}

{{< card icon="adjustments" link="/docs/guide/evervideo/evervideo-guide-settings" title="Paramètres" subtitle="Moteur audio, décodeur vidéo, sous-titres, bibliothèque, gestionnaire de fichiers, widgets, personnalisation, langue, sauvegarde." >}}

{{< card icon="question-mark-circle" link="/docs/faq/evervideo" title="FAQ" subtitle="Trouvez des réponses aux questions les plus fréquentes sur Evervideo." >}}

{{< /cards >}}
