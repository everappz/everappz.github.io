---
date: 2020-01-01
title: 'Flacbox'
description: "Apprenez à utiliser Flacbox — le lecteur de musique en nuage pour iPhone, iPad et Mac, compatible FLAC haute résolution, DSD, ALAC et FFmpeg. Connectez iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, NAS, WebDAV, SMB et DLNA. Diffusez et téléchargez de l'audio haute résolution, modifiez les métadonnées, écoutez des livres audio, scrobblez vers Last.fm, utilisez Apple CarPlay et les widgets de l'écran d'accueil, et personnalisez l'égaliseur à 10 bandes."
keywords: [
  "guide utilisateur Flacbox", "comment utiliser Flacbox", "lecteur de musique haute résolution iPhone", "lecteur FLAC iPhone",
  "lecteur DSD iOS", "lecteur ALAC Mac", "application de musique sans perte", "lecteur de musique en nuage iPhone",
  "lecteur FLAC hors ligne Mac", "gestionnaire de bibliothèque musicale", "éditeur de balises audio",
  "lecteur FLAC CarPlay", "application audio Chromecast", "musique AirPlay 2",
  "widgets Flacbox", "Flacbox CarPlay", "lecteur de musique FFmpeg iOS",
  "lecteur de livres audio iPhone", "signets audio iOS", "application de correction de hauteur tonale",
  "taux d'échantillonnage de sortie audio", "DAC externe iPhone", "DAC USB Mac",
  "application Synology musique", "application QNAP musique", "lecteur de musique NAS iPhone",
  "lecteur de musique WebDAV", "streaming musique SMB", "lecteur DLNA musique",
  "musique iCloud Drive", "FLAC Google Drive", "lecteur FLAC Dropbox",
  "transfert de musique Wi-Fi Drive", "import liste de lecture M3U", "scrobbling Last.fm"
]
tags: ["flacbox", "guide", "haute résolution", "FLAC", "FFmpeg", "nuage", "CarPlay", "widgets"]
---


### Bienvenue dans le guide Flacbox

Flacbox est un lecteur de musique haute résolution pour iPhone, iPad et Mac qui vous permet de transformer votre stockage en nuage préféré, vos serveurs NAS et vos serveurs multimédias en votre propre service de streaming personnel.

Flacbox se connecte à une liste de sources remarquablement étendue, le tout dans une seule application :

- **Stockage en nuage personnel :** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · pCloud · Yandex Disk · MediaFire · WD My Cloud Home · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Serveurs auto-hébergés :** Plex · Jellyfin · Emby · Subsonic (et chaque serveur compatible Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (et ownCloud via l'API partagée) · Synology Drive · QNAP.
- **Protocoles NAS et partage de fichiers :** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP / FTPS · SFTP (authentification par mot de passe ou clé publique) · NFS · DLNA / UPnP (lecture et téléchargement). Fonctionne avec Apple Time Capsule, Synology, QNAP, WD My Cloud, tout hôte Linux Samba / NFS / SSH, ou un dossier partagé sur votre Mac ou PC Windows.
- **Stockage objet compatible S3 :** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, et tout autre point de terminaison S3-API.
- **Découverte sur le réseau local :** La section Appareils disponibles liste automatiquement chaque service Bonjour / mDNS sur votre Wi-Fi — serveurs Plex, Jellyfin, Emby, Synology, QNAP, routeurs AirPort avec disques attachés, Time Capsule — pour vous permettre de vous connecter sans saisir d'adresse IP.

Là où la plupart des applications de musique se limitent au moteur audio intégré d'Apple, Flacbox intègre **FFmpeg** aux codecs système pour vous permettre de lire des formats non pris en charge nativement par iOS — WMA, OGG, OPUS, APE, DSD, DSF, DFF, TTA, MPC, WV, ainsi que la famille habituelle MP3 / AAC / M4A / WAV / AIFF / ALAC / FLAC. Combiné à un taux d'échantillonnage de sortie configurable (44,1 / 48 / 64 / 88,2 / 96 kHz), une sortie multicanal (Mono → 5.1 → SDDS → ITU BS.775-1), un réglage du tampon d'E/S et une correction de hauteur tonale, Flacbox offre aux audiophiles un niveau de contrôle que la plupart des applications musicales grand public ne proposent tout simplement pas.

### Profitez d'un streaming fluide et d'une lecture hors ligne

Flacbox dispose d'une mise en mémoire tampon intelligente pour un streaming fluide et d'un gestionnaire de téléchargement intégré pour vous permettre de télécharger des listes de lecture, artistes, albums, dossiers ou pistes individuels sur votre appareil pour une utilisation hors ligne. Lorsque le stockage vient à manquer, supprimez les fichiers mis en cache en un seul geste et continuez à diffuser depuis le nuage. Le mode hors ligne pour les dossiers, listes de lecture, albums et artistes synchronise également automatiquement les nouvelles pistes dès leur apparition dans le nuage, de sorte que votre collection hors ligne reste toujours à jour.

### Bibliothèque musicale organisée automatiquement

Lorsque vous importez des pistes audio, Flacbox analyse leurs métadonnées et les organise dans une bibliothèque musicale claire — regroupées par Chansons, Chansons non lues, Albums, Artistes d'albums, Artistes, Genres et Compositeurs. Utilisez la recherche intégrée pour trouver n'importe quoi en quelques secondes, filtrez par source (nuage en ligne / hors ligne / appareil) et choisissez entre les dispositions de bibliothèque Simple / Groupée / À onglets. Pour les bibliothèques avec des compilations de différents artistes, Flacbox propose des vues dédiées Tous les albums / Albums exclusifs / Albums solos pour afficher les bons résultats sans bruit.

### Corrigez les métadonnées et taguez votre musique

Si vous rencontrez des balises corrompues ou des encodages désordonnés (un problème courant pour les fichiers rippés ou anciens), l'éditeur de balises ID3 intégré peut les corriger — manuellement ou avec des recherches automatiques MusicBrainz. Vous pouvez également normaliser les encodages de caractères cassés (idéal pour les balises cyrilliques, japonaises ou chinoises provenant de PC Windows), rechercher la pochette d'album manquante et écrire les modifications dans le fichier original dans le nuage automatiquement. Pour une édition en lot plus poussée, installez notre application complémentaire Evertag.

### Transferts faciles depuis Mac, PC ou NAS

Déplacez de la musique entre votre ordinateur et votre iPhone ou iPad avec l'un de ces outils : SMB, WebDAV, DLNA, Wi-Fi Drive (glisser-déposer dans n'importe quel navigateur de bureau), iTunes / Finder File Sharing via un câble Lightning ou USB-C, clés USB ou clés iXpand Flash Drive. Vous avez un Apple Time Capsule, WD My Cloud, Synology, QNAP ou tout autre NAS exposant SMB / WebDAV / DLNA / FTP / SFTP ? Connectez-le une seule fois et diffusez toute votre bibliothèque sans occuper de stockage sur l'appareil.

### Personnalisez votre son avec l'égaliseur

Flacbox inclut un égaliseur à 10 bandes avec des préréglages de style iPod (Acoustique, Renforcement des basses, Classique, Dance, Rock, Pop, Jazz et bien d'autres), un préamplificateur et la possibilité d'enregistrer vos propres préréglages. Que vous fassiez des réglages pour une paire d'IEM audiophile, un HomePod mini ou une autoradio, vous pouvez façonner le son exactement comme vous le souhaitez.

### Adapté aux livres audio

Flacbox est un excellent lecteur de livres audio — plusieurs signets par piste, vitesse de lecture à grain fin (0,02× à 3,00×), reprise de la lecture exactement là où vous vous êtes arrêté, boutons de saut personnalisables et minuteur de sommeil qui s'estompe doucement à l'heure du coucher. Les marqueurs de chapitres M4B et les fichiers longs sont entièrement pris en charge.

### Streamez partout — y compris dans votre voiture et sur l'écran d'accueil

Diffusez de la musique vers Apple TV / HomePod via AirPlay 2, envoyez-la vers les enceintes Google Chromecast et les téléviseurs compatibles Cast, et emportez tout avec vous avec Apple CarPlay. Utilisez les widgets de l'écran d'accueil sur iPhone et iPad pour voir la piste en cours d'un coup d'œil, et le scrobbling Last.fm pour conserver votre historique d'écoute entre les applications.

### Confidentialité et sécurité

Flacbox utilise uniquement les SDK officiels et les connexions OAuth de chaque fournisseur de nuage — votre mot de passe n'atteint jamais l'application. Les jetons d'accès sont stockés chiffrés dans le Keychain iOS, tous les transferts sont protégés par TLS, et la révocation de l'accès dans votre compte nuage ou la suppression de Flacbox de l'appareil supprime tout instantanément. Protégez votre bibliothèque avec un code d'accès optionnel pour une couche de confidentialité supplémentaire.

### Prise en main de Flacbox

Ce guide vous accompagne à travers chaque partie de Flacbox sur iPhone, iPad et Mac — depuis la connexion des services nuage, l'organisation de votre bibliothèque, le transfert de fichiers et la gestion des listes de lecture, jusqu'au réglage fin de l'égaliseur et la configuration du moteur audio. Utilisez les cartes ci-dessous pour accéder directement à la section dont vous avez besoin.

{{< cards cols="2">}}

{{< card icon="map" link="/docs/guide/flacbox/flacbox-guide-navigation" title="Navigation" subtitle="Barre d'onglets sur iPhone, menu gauche sur iPad et Mac, mini lecteur, widgets, CarPlay." >}}

{{< card icon="cloud" link="/docs/guide/flacbox/flacbox-guide-connections" title="Connexions" subtitle="iCloud, Google Drive, Dropbox, OneDrive, NAS, WebDAV, SMB, DLNA." >}}

{{< card icon="collection" link="/docs/guide/flacbox/flacbox-guide-music-library" title="Bibliothèque musicale" subtitle="Chansons, Albums, Artistes, Genres, Compositeurs — synchronisation, recherche, modification des métadonnées." >}}

{{< card icon="music-note" link="/docs/guide/flacbox/flacbox-guide-playlists" title="Listes de lecture" subtitle="Créez, importez M3U / M3U8 / CUE, réorganisez et exportez vers M3U / CSV / TXT." >}}

{{< card icon="folder" link="/docs/guide/flacbox/flacbox-guide-local-files" title="Fichiers locaux" subtitle="Musique hors ligne, clés USB, Wi-Fi Drive, gestionnaire de fichiers, dossiers hors ligne." >}}

{{< card icon="play" link="/docs/guide/flacbox/flacbox-guide-player" title="Lecteur audio" subtitle="Sortie haute résolution, égaliseur, hauteur tonale, signets, AirPlay, Chromecast, vitesse, minuteur de sommeil." >}}

{{< card icon="adjustments" link="/docs/guide/flacbox/flacbox-guide-settings" title="Paramètres" subtitle="Moteur audio, bibliothèque, gestionnaire de fichiers, CarPlay, widgets, personnalisation, langue, sauvegarde." >}}

{{< card icon="question-mark-circle" link="/docs/faq/flacbox" title="FAQ" subtitle="Trouvez des réponses aux 50 questions les plus courantes sur Flacbox." >}}

{{< /cards >}}
