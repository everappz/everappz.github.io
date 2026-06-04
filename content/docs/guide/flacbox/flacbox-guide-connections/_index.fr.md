---
title: "Connexions"
date: 2020-02-01
description: "Apprenez à connecter des services cloud et des appareils NAS à Flacbox. Diffusez de la musique haute résolution depuis iCloud Drive, Dropbox, Google Drive, OneDrive, MEGA, Box, pCloud, Synology Drive, Yandex Disk et bien plus encore. Utilisez SMB, WebDAV, DLNA, FTP / SFTP, Wi-Fi Drive, iTunes / Finder File Sharing et des clés USB."
keywords: [
  "configuration cloud Flacbox", "connecter Google Drive à Flacbox", "streaming musique SMB",
  "lecteur iOS WebDAV", "application musique DLNA", "streaming audio NAS", "Wi-Fi Drive iPhone",
  "transférer des fichiers vers iPhone", "Flacbox iTunes File Sharing", "connecter NAS à iPhone",
  "application musique Synology Drive", "application musique QNAP", "application musique Bluesound",
  "Flacbox pCloud", "Flacbox MEGA", "Flacbox OneDrive", "Flacbox Yandex Disk",
  "Flacbox HiDrive", "Flacbox MediaFire", "application musique scrobbling Last.fm",
  "musique iXpand Flash Drive", "DAC USB iPhone"
]
tags: ["guide", "flacbox", "connexions", "nuage", "NAS"]
readingTime: 12
---


Sur cet écran, vous pouvez connecter toutes les sources contenant votre musique. Vous pouvez intégrer des services cloud populaires tels que Dropbox, Google Drive, iCloud Drive, OneDrive, MEGA, Box, pCloud, Yandex Disk, Synology Drive et bien d'autres, ainsi que votre Mac, PC ou NAS via des protocoles standard. Que votre collection soit hébergée sur un service adapté au streaming comme Dropbox ou sur un NAS personnel comme un Synology, QNAP, Buffalo, Apple Time Capsule ou WD My Cloud Home, Flacbox se connecte à tous depuis un seul écran.

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran Connexions de Flacbox" image="/docs/guide/flacbox/img/connections-main.webp" >}}
{{< /cards >}}

## Se connecter au stockage en nuage

- Ouvrez l'onglet **Connexions**.
- Sélectionnez **Se connecter au stockage en nuage** dans le menu.
- Choisissez un service de stockage en nuage dans la liste.
- Saisissez vos identifiants sur la page d'autorisation officielle fournie par le fournisseur de nuage, puis appuyez sur **Fait**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Ajouter un service de stockage en nuage" image="/docs/guide/flacbox/img/add-cloud-storage.webp" >}}
{{< /cards >}}

Si vous rencontrez des problèmes, vérifiez votre connexion internet et vos identifiants. Dans la version Premium de l'application, vous pouvez ajouter un nombre illimité de services ; la version gratuite prend en charge jusqu'à trois services.

## Services de stockage en nuage, serveurs multimédias et protocoles pris en charge

Flacbox prend en charge un éventail exceptionnellement large de sources pour votre musique. Tout ce qui suit fonctionne depuis un seul écran **Se connecter au stockage en nuage**.

**Stockage en nuage personnel :** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Serveurs auto-hébergés :** Plex · Jellyfin · Emby · Subsonic (et chaque serveur compatible Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (et ownCloud via l'API partagée) · Synology Drive · QNAP.

**Protocoles NAS et partage de fichiers :** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, authentification par mot de passe ou clé publique) · NFS · DLNA / UPnP (lecture et téléchargement).

**Stockage objet compatible S3 :** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, et tout autre point de terminaison S3-API.

**Découverte sur le réseau local :** La section Appareils disponibles liste automatiquement chaque service Bonjour / mDNS sur votre réseau Wi-Fi pour vous permettre de vous connecter sans saisir d'adresse IP.

Chaque connexion utilise le **SDK officiel ou le protocole ouvert** du service, avec une autorisation OAuth là où elle est prise en charge. Vous pouvez connecter plusieurs comptes d'un même service (par exemple, deux comptes Google Drive, un Dropbox personnel et un professionnel, ou à la fois un serveur Plex et un serveur Jellyfin) et les parcourir côte à côte dans l'écran Connexions.

## Sécurité et confidentialité

Nous utilisons uniquement des SDK officiels et des connexions sécurisées pour interagir avec les services cloud connectés. Votre identifiant et votre mot de passe ne sont pas accessibles à l'application — tous les transferts sont chiffrés par TLS.

Lorsque vous saisissez vos identifiants, l'application vous affiche la page d'autorisation officielle fournie par le fournisseur de service cloud, et l'ensemble du processus d'autorisation se déroule en dehors de l'application. Le fournisseur de service cloud envoie ensuite un jeton d'authentification à l'application après une autorisation réussie, et ce jeton est utilisé pour effectuer des appels API.

Un jeton d'authentification est une clé numérique qui permet à des applications tierces d'interagir avec le stockage en nuage en votre nom. Le jeton est stocké sur votre appareil dans le système de stockage sécurisé d'Apple (Keychain), chiffré au repos et protégé par le code d'accès ou le verrouillage biométrique de votre appareil. Vous pouvez télécharger des fichiers depuis les services cloud connectés sur votre appareil ; ces fichiers sont placés dans le répertoire Documents de l'application et peuvent être supprimés à tout moment via le gestionnaire de fichiers intégré.

L'application ne partage aucune information de vos comptes cloud connectés avec Everappz, des annonceurs ou un tiers. Vous pouvez révoquer l'accès à votre compte cloud à tout moment en ouvrant la page des paramètres du compte dans votre navigateur web.

## Révoquer un jeton d'authentification

Pour révoquer un jeton d'authentification, connectez-vous à votre compte cloud dans un navigateur web et accédez à la page de sécurité ou des applications connectées. Vous pouvez y trouver chaque application tierce connectée à votre compte cloud et en supprimer certaines si vous ne souhaitez plus les utiliser. Des instructions détaillées pour les comptes Google sont disponibles [ici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Vous pouvez également déconnecter le compte cloud depuis l'application elle-même — dans ce cas, le jeton d'authentification est immédiatement supprimé de votre appareil. Si vous désinstallez l'application, toutes les données téléchargées et tous les jetons d'accès sont automatiquement supprimés avec elle.

## Déconnecter un stockage en nuage ou modifier sa configuration

- **Accédez aux options du stockage en nuage** — localisez le service connecté dans l'écran **Connexions**.
- **Appuyez sur le bouton «&nbsp;...&nbsp;»** à côté du titre du service pour ouvrir les options supplémentaires :
  - **Renommer** — modifier le nom du service cloud tel qu'il apparaît dans votre liste.
  - **Paramètres** — modifier la configuration ou les données d'authentification. Vous devrez parfois réautoriser le service cloud si le jeton d'autorisation a expiré.
  - **Se déconnecter** — rompre complètement la connexion entre l'application et le service cloud. Cela supprime de la bibliothèque musicale de l'application toutes les chansons associées à ce service, mais les laisse intactes sur le serveur.

## Se connecter à un ordinateur ou un NAS

Vous pouvez également connecter votre ordinateur, votre NAS personnel ou d'autres périphériques réseau en utilisant les protocoles SMB, DLNA ou WebDAV. C'est la façon la plus simple d'intégrer une bibliothèque musicale existante — qu'elle se trouve sur un Mac, un PC Windows, un Synology ou un NAS — dans Flacbox sans rien copier.

## Se connecter à un ordinateur via SMB

- Appuyez sur **Se connecter au stockage en nuage → SMB**.
- Saisissez l'adresse IP de l'ordinateur et le nom du dossier partagé dans le champ URL au format `smb://adresse-ip-ordinateur/nom-dossier-partage`.
- Choisissez la version du protocole : **Auto**, **SMB1** ou **SMB2**.
- Saisissez votre identifiant et votre mot de passe (si nécessaire).
- Appuyez sur **Fait**.

Si la connexion est réussie, vous verrez le stockage connecté dans la section **Stockage en nuage**. Un tutoriel complet sur la façon de connecter votre Mac ou PC via SMB est disponible [ici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

## Se connecter à un NAS via WebDAV

Toutes les étapes sont identiques à SMB, à l'exception du champ URL. L'URL doit être au format `http://nom-serveur` ou `https://nom-serveur` si le serveur prend en charge SSL. WebDAV fonctionne avec **Synology, QNAP, Nextcloud, ownCloud** et de nombreux autres serveurs — partout où un point de terminaison WebDAV est disponible.

Un tutoriel complet sur la connexion d'un NAS via WebDAV est disponible [ici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

## Se connecter à un ordinateur ou un NAS via DLNA

Vous pouvez également partager une bibliothèque musicale située sur votre PC Windows ou votre NAS personnel à l'aide du protocole DLNA / UPnP et accéder à cette bibliothèque dans l'application comme décrit [ici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA est un protocole populaire et largement pris en charge, mais il permet uniquement de lire ou de télécharger de la musique — vous ne pouvez pas téléverser des fichiers ni créer de nouveaux dossiers sur un serveur DLNA.

## Se connecter à un NAS ou serveur via FTP, FTPS ou SFTP

Flacbox prend également en charge les protocoles de transfert de fichiers classiques. Pour connecter un serveur via FTP ou FTPS, appuyez sur **Se connecter au stockage en nuage → FTP**, saisissez l'URL de l'hôte au format `ftp://nom-serveur` (ou `ftps://nom-serveur` pour une connexion chiffrée), indiquez vos identifiants, puis appuyez sur **Fait**. Pour **SFTP** (SSH File Transfer Protocol), choisissez **SFTP** et fournissez soit un mot de passe, soit une paire de clés SSH. Ces deux options fonctionnent avec les NAS, les hôtes Linux et tout serveur disposant d'un démon FTP / FTPS / SSH.

## Se connecter à un partage NFS

Flacbox inclut la prise en charge de **NFS** (Network File System) — pratique pour les hôtes Linux, les serveurs BSD et les NAS qui préfèrent exposer leurs bibliothèques musicales via NFS plutôt que SMB. Sélectionnez **NFS** dans le menu **Se connecter au stockage en nuage**, saisissez l'adresse du serveur et le chemin exporté, puis appuyez sur **Fait**.

## Connecter un serveur Plex Media

Flacbox peut se connecter directement à un Plex Media Server et parcourir votre bibliothèque musicale par Artistes, Albums, Genres et Listes de lecture. Appuyez sur **Se connecter au stockage en nuage → Plex**, connectez-vous avec votre compte Plex, choisissez un serveur, et la bibliothèque apparaît aux côtés de vos services cloud. Les serveurs Plex sur le même réseau local sont également découverts automatiquement dans la section **Appareils disponibles**.

## Connecter un serveur Jellyfin ou Emby

**Jellyfin** (open source) et **Emby** (commercial) fonctionnent tous les deux nativement dans Flacbox. Appuyez sur **Se connecter au stockage en nuage → Jellyfin** ou **Emby**, saisissez l'URL de votre serveur (par exemple `http://ip-serveur:8096`) et vos identifiants, et votre bibliothèque musicale est prête à être diffusée. Comme pour Plex, les bibliothèques sur le réseau local sont listées automatiquement dans **Appareils disponibles**.

## Connecter un serveur Subsonic ou Navidrome

Flacbox parle le protocole Subsonic API, ce qui signifie qu'il fonctionne avec **Subsonic** lui-même, **Navidrome**, et tout autre serveur compatible Subsonic — y compris Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS), Ampache. Appuyez sur **Se connecter au stockage en nuage → Subsonic**, saisissez l'URL du serveur et vos identifiants, et la bibliothèque apparaît dans l'écran Connexions. C'est la façon la plus simple de donner à Flacbox accès à une collection musicale auto-hébergée sans exposer le partage de fichiers sous-jacent.

## Se connecter au stockage objet compatible S3

Pour les auto-hébergeurs et les audiophiles utilisant le stockage en nuage, Flacbox inclut un connecteur compatible S3. Appuyez sur **Se connecter au stockage en nuage → Stockage S3**, puis saisissez l'URL du point de terminaison, la région, la clé d'accès, la clé secrète et le nom du bucket. Cela fonctionne avec AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces et tout autre service exposant un point de terminaison S3-API.

## Appareils disponibles

Cette section affiche tous les appareils sur votre réseau local auxquels vous pouvez vous connecter depuis Flacbox via la découverte Bonjour. Pour établir une connexion, suivez ces étapes :

- Ouvrez l'application et accédez à la section **Appareils disponibles** sous Connexions.
- Appuyez sur l'appareil auquel vous souhaitez vous connecter.
- Si nécessaire, saisissez vos identifiants pour terminer la connexion.

C'est la façon la plus rapide de découvrir un partage SMB, WebDAV ou DLNA sur votre réseau domestique sans saisir d'adresses IP manuellement.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Appareils disponibles sur le réseau local" image="/docs/guide/flacbox/img/available-devies.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive est une technologie pratique qui permet des transferts de fichiers sans fil depuis votre ordinateur vers votre appareil iOS via n'importe quel navigateur de bureau. Pour utiliser cette fonctionnalité efficacement, assurez-vous que votre appareil et votre ordinateur sont connectés au même réseau Wi-Fi. Voici un guide étape par étape pour utiliser Wi-Fi Drive.

### Activer Wi-Fi Drive

- Ouvrez l'application et accédez à l'onglet **Connexions**.
- Sélectionnez **Se connecter via Wi-Fi** pour accéder à l'écran principal de Wi-Fi Drive.
- (Optionnel) Définissez un nom d'utilisateur et un mot de passe pour le serveur web intégré afin de protéger l'accès.
- Appuyez sur **Démarrer Wi-Fi Drive** pour activer Wi-Fi Drive.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox Wi-Fi Drive" image="/docs/guide/flacbox/img/wifi-drive.webp" >}}
{{< /cards >}}

### Accéder à Wi-Fi Drive depuis votre ordinateur

- Sur votre ordinateur (de bureau ou portable), ouvrez un navigateur web (tel que Chrome, Firefox ou Safari).
- Dans la barre d'adresse du navigateur, saisissez l'URL fournie par l'application.

### Transférer des fichiers sans fil

Une fois que la page web correspondant à votre appareil iOS s'ouvre dans le navigateur, vous pouvez facilement glisser-déposer des fichiers depuis votre ordinateur vers la page web. Les fichiers déposés commenceront à se transférer vers votre appareil iOS et seront accessibles dans Flacbox.

Vous pouvez également monter Wi-Fi Drive directement dans le Finder sur macOS (Aller → Se connecter au serveur…) ou dans l'Explorateur de fichiers sur Windows (Connecter un lecteur réseau…) et utiliser votre iPhone ou iPad comme un lecteur réseau ordinaire.

Des instructions détaillées sur le transfert de fichiers sans fil via Wi-Fi Drive sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (désormais Finder File Sharing sur macOS Catalina et versions ultérieures) est une autre façon de transférer des fichiers depuis un ordinateur vers un appareil à l'aide d'un câble Lightning ou USB-C.

- Connectez l'appareil à l'ordinateur avec un câble et lancez **Finder** sur Mac (ou **iTunes** sur Windows).
- Ouvrez **Emplacements → Votre appareil connecté → Fichiers** et trouvez l'application Flacbox.
- Appuyez sur l'icône de l'application pour voir tous les dossiers partagés.
- Copiez des fichiers de l'ordinateur vers le dossier partagé sur l'appareil par glisser-déposer.

Des instructions détaillées sur l'utilisation de Finder File Sharing sont disponibles [ici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

## Connecter une clé USB

Si vous disposez d'une carte SD ou d'une clé USB, vous pouvez la connecter à l'aide d'un adaptateur Lightning vers USB / lecteur de carte SD ou d'une clé USB-C (sur iPad et iPhone 15 / 16 / 17 / Pro). L'application prend en charge les lecteurs de carte certifiés Apple et les iXpand Flash Drive. Avec un iXpand Flash Drive, insérez-le dans le port Lightning et ouvrez l'application — vous verrez un message «&nbsp;Périphérique externe connecté&nbsp;» avec les informations de l'appareil. Appuyez sur l'icône de la clé USB pour accéder au dossier de musique et appuyez sur n'importe quel fichier audio pour commencer la lecture.

Nous avons des instructions détaillées sur la façon de connecter une clé USB à votre iPhone et d'écouter de la musique ou de gérer des fichiers qui s'y trouvent [ici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestionnaire de fichiers

Une fois que vous avez connecté un service de stockage en nuage, appuyez sur son icône pour afficher tous les fichiers et dossiers disponibles. Vous pouvez utiliser le gestionnaire de fichiers intégré pour travailler avec ces fichiers — télécharger, renommer, déplacer, téléverser, supprimer, et plus encore. Lorsque vous lancez un téléchargement, le fichier apparaît dans la file de transfert. Pour ouvrir la file de transfert, accédez à l'onglet Fichiers locaux et appuyez sur l'icône des flèches en rotation dans le coin supérieur gauche. Tous les fichiers et dossiers téléchargés sont disponibles dans la section Fichiers locaux.

## Barre d'outils supérieure

La barre d'outils supérieure, située sous la barre de navigation, offre plusieurs actions utiles pour un accès facile. Vous pouvez l'afficher ou la masquer d'un simple geste de balayage vers le bas.

- **Rechercher** — effectuer une recherche rapide dans le répertoire actuel, ce qui facilite la localisation de fichiers ou dossiers spécifiques.
- **Reprendre la lecture** — si activée dans les paramètres de l'application, cette option restaure la file de l'audio player et la dernière position média pour le dossier actuel. Un moyen pratique de reprendre là où vous vous étiez arrêté.
- **Tout lire** — parcourt le dossier actuel et ses sous-dossiers, puis ajoute tous les fichiers audio trouvés à une nouvelle file de l'audio player. Utile pour lire toutes les pistes d'un répertoire.
- **Tout mélanger** — comme Tout lire, mais mélange les fichiers avant de les ajouter à la file de l'audio player. Idéal pour redécouvrir un ancien dossier de musique.

## Options de dossier

Lorsque vous ouvrez un dossier, vous trouverez un ensemble d'actions pratiques accessibles en appuyant sur le bouton **«&nbsp;...&nbsp;»** dans le coin supérieur droit.

- **Sélectionner** — activer le mode de sélection de fichiers. Cela vous permet de choisir un ou plusieurs fichiers dans le dossier et d'effectuer des actions sur toute la sélection.
- **Nouveau dossier** — créer un nouveau dossier dans le dossier actuel. Idéal pour garder votre bibliothèque bien structurée.
- **Activer le mode hors ligne** — activer le mode hors ligne pour le dossier actuel. Le mode hors ligne va au-delà d'un simple téléchargement : il surveille activement le dossier pour détecter les modifications. Si vous ajoutez de nouveaux fichiers en ligne, ils apparaîtront automatiquement sur votre appareil.
- **Téléverser des fichiers** — téléverser des fichiers depuis votre appareil vers le dossier en ligne. Ils sont ainsi accessibles de n'importe où via le même service cloud.
- **Rechercher** — rechercher des fichiers spécifiques dans le dossier actuel.
- **Trier** — trier les fichiers par nom, taille, date de modification ou par métadonnées. Le mode de tri par défaut reflète l'ordre de tri sur le serveur, mais vous pouvez le modifier selon vos préférences.
- **Vue grille / liste** — basculer entre la vue tableau et la vue miniatures. La vue tableau affiche une liste compacte ; la vue miniatures affiche de grandes prévisualisations d'illustration pour une identification visuelle rapide.

## Modifier des fichiers en ligne

Lorsque vous devez gérer plusieurs fichiers dans votre stockage en nuage, utilisez le **mode de sélection** pour simplifier vos actions :

- **Activer le mode de sélection** — appuyez sur le bouton **«&nbsp;...&nbsp;»** dans le coin supérieur droit et choisissez **Sélectionner**.
- **Choisir des fichiers** — des cases à cocher apparaissent à côté de chaque fichier et dossier. Appuyez pour sélectionner un ou plusieurs éléments.
- **Effectuer des actions** — une fois les fichiers ou dossiers sélectionnés, vous aurez accès à Lire ensuite, Lire plus tard, Ajouter à la bibliothèque musicale, Ajouter à une liste de lecture, Copier, Téléverser, Déplacer, Renommer et Supprimer.

Si vous préférez utiliser le stockage en nuage connecté en lecture seule (pour éviter les suppressions accidentelles), activez Paramètres → Gestionnaire de fichiers → Modifier les fichiers en ligne → Désactivé pour masquer toutes les opérations destructives de l'interface.

## Actions sur les fichiers

Appuyez sur l'icône **«&nbsp;...&nbsp;»** près du titre d'un fichier pour afficher son menu d'actions :

- **Lire ensuite** — insérer le fichier en haut de la file de l'audio player, afin qu'il soit lu juste après la piste actuelle.
- **Lire plus tard** — ajouter le fichier en bas de la file de l'audio player.
- **Ajouter à la bibliothèque musicale** — intégrer le fichier dans votre bibliothèque musicale, organisée par artiste, album, genre ou compositeur.
- **Ajouter à une liste de lecture** — ajouter le fichier à une liste de lecture existante ou en créer une nouvelle.
- **Modifier les balises audio** — ouvrir l'éditeur de balises intégré pour modifier les métadonnées. Pour les fichiers en ligne, la piste est temporairement téléchargée, modifiée, puis retéléversée après confirmation.
- **Ajouter aux favoris** — ajouter le fichier à vos favoris pour un accès rapide.
- **Télécharger** — télécharger le fichier ou le dossier sur votre appareil pour une utilisation hors ligne.
- **Renommer** — renommer le fichier directement sur le stockage distant.
- **Déplacer** — déplacer le fichier vers un autre dossier dans votre stockage en nuage.
- **Ouvrir dans** — exporter le fichier vers une autre application compatible. Le fichier est téléchargé sur votre appareil, puis la feuille de partage système apparaît.
- **Supprimer** — supprimer définitivement le fichier de votre stockage en nuage. **Cette action est irréversible.**

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Plus d'actions pour un fichier dans le stockage en nuage connecté" image="/docs/guide/flacbox/img/more-actions-for-file-in-connected-cloud-storage.webp" >}}
{{< /cards >}}

Si la liste des actions dépasse l'espace disponible à l'écran, faites simplement défiler vers le bas dans le menu des actions pour accéder aux options supplémentaires.

## Actions sur les dossiers

Pour chaque dossier de votre stockage en nuage, de nombreuses actions sont disponibles en appuyant sur l'icône **«&nbsp;...&nbsp;»** à côté du titre du dossier. Si vous ne voyez pas toutes les actions, faites défiler vers le bas pour en afficher davantage.

- **Tout lire** — remplacer la file actuelle de l'audio player par tous les éléments du dossier sélectionné.
- **Lire ensuite** — ajouter l'intégralité du dossier en haut de la file de l'audio player.
- **Lire plus tard** — ajouter le contenu du dossier en bas de la file de l'audio player.
- **Ajouter à la bibliothèque musicale** — intégrer le contenu du dossier dans votre bibliothèque musicale.
- **Ajouter à une liste de lecture** — ajouter l'intégralité du dossier à une liste de lecture. Vous avez également la possibilité de créer une nouvelle liste de lecture dont le nom est automatiquement tiré du nom du dossier.
- **Ajouter aux favoris** — ajouter le dossier à vos favoris pour un accès rapide.
- **Activer le mode hors ligne** — au-delà d'un simple téléchargement, cette option surveille continuellement le dossier pour détecter les nouveaux fichiers et les télécharge automatiquement au fur et à mesure qu'ils apparaissent en ligne.
- **Télécharger** — télécharger tout le contenu du dossier sur votre appareil pour un accès hors ligne.
- **Renommer** — renommer le dossier directement sur le stockage distant.
- **Déplacer** — déplacer le dossier vers un autre emplacement dans votre stockage en nuage.
- **Archiver (ZIP)** — regrouper le contenu du dossier dans un seul fichier ZIP (fonctionnalité Premium).
- **Supprimer** — supprimer définitivement le dossier et son contenu de votre stockage en nuage. **Cette action est irréversible.**

## Accès rapide

La section Accès rapide est située en haut de l'écran. Elle vous donne un accès rapide à vos fichiers favoris et récemment ouverts depuis les services cloud connectés. Chaque fois que vous ouvrez un fichier ou un dossier depuis le nuage, il est ajouté à la liste Récemment ouverts. Pour effacer cette liste, ouvrez Récents, appuyez sur le bouton Plus d'actions et choisissez Supprimer la liste. Vous pouvez également marquer des dossiers profondément imbriqués comme Favoris pour y accéder rapidement sans devoir parcourir l'arborescence.

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Liens en ligne et accès rapide" image="/docs/guide/flacbox/img/online-links.webp" >}}
{{< /cards >}}

## Autres services

Cette section affiche des fonctionnalités supplémentaires qui améliorent votre expérience. Actuellement, l'application prend en charge le scrobbling **Last.fm** — une fois connecté, vos statistiques de lecture sont automatiquement envoyées à votre compte Last.fm. Vous pouvez ensuite visiter votre profil Last.fm pour consulter les analyses d'écoute et obtenir des recommandations musicales personnalisées. Des instructions de configuration détaillées sont disponibles [ici](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).

{{< cards cols="1">}}
  {{< card title="" subtitle="Flacbox — Connexion Last.fm" image="/docs/guide/flacbox/img/last-fm-connect.webp" >}}
{{< /cards >}}
