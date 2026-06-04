---
title: "Fichiers"
date: 2020-02-01
lastmod: 2026-06-01
description: "Apprenez à utiliser l'onglet Fichiers dans Evervideo sur iPhone, iPad et Mac. Connectez des services cloud, des périphériques NAS, des serveurs multimédias et des flux RTSP en un seul endroit. Gérez les vidéos hors ligne, la file des transferts, les téléchargements, Wi-Fi Drive, iTunes / Finder File Sharing et les lecteurs USB. Inclut iCloud Drive, Google Drive, Dropbox, OneDrive, MEGA, Box, pCloud, Synology, QNAP, Plex, Jellyfin, Emby, Subsonic, Navidrome, SMB, WebDAV, NFS, FTP / SFTP, DLNA et stockage compatible S3."
keywords: [
  "fichiers Evervideo", "connexions Evervideo", "fichiers locaux Evervideo",
  "configuration vidéo cloud iPhone", "connecter Google Drive vidéo", "streaming vidéo SMB",
  "lecteur vidéo WebDAV iOS", "vidéo DLNA iPhone", "streaming vidéo NAS",
  "transfert vidéo Wi-Fi Drive", "iTunes File Sharing Evervideo", "RTSP iPhone",
  "Plex Evervideo", "Jellyfin Evervideo", "Emby Evervideo",
  "Subsonic Evervideo", "Navidrome Evervideo",
  "mode hors ligne vidéo Evervideo", "file de transferts Evervideo",
  "gestionnaire de fichiers Evervideo", "dossier Documents Evervideo",
  "lecteur vidéo Synology", "lecteur vidéo QNAP",
  "lecteur vidéo Apple Time Capsule", "USB DAC vidéo",
  "lecteur vidéo iXpand", "lecteur vidéo S3"
]
tags: ["guide", "evervideo", "fichiers", "connexions", "cloud", "NAS", "Plex", "RTSP"]
readingTime: 14
---

L'onglet Fichiers est le gestionnaire de fichiers tout-en-un d'Evervideo. Contrairement à la plupart des applications vidéo qui séparent le stockage cloud des fichiers locaux dans des onglets différents, Evervideo les fusionne tous deux dans un seul écran défilable afin que vous puissiez passer d'un serveur Plex à un dossier cloud à votre dossier Documents d'iPhone sans naviguer entre les onglets.

L'onglet Fichiers est divisé en sections claires qui apparaissent dans cet ordre sur votre écran :

- **Accès rapide** — récents et favoris pour les fichiers et dossiers que vous avez ouverts le plus récemment.
- **Fichiers dans cette application** — ce qui se trouve dans le dossier Documents sandboxé d'Evervideo.
- **Fichiers sur cet iPhone / iPad / Mac** — vidéos ailleurs sur votre appareil, accessibles via le sélecteur de fichiers système.
- **Stockage cloud** — chaque compte cloud, NAS et serveur multimédia que vous avez connecté.
- **Appareils disponibles** — serveurs et lecteurs découverts automatiquement par Bonjour / mDNS sur votre réseau local.

Dans le coin supérieur droit de l'écran Fichiers se trouve un bouton Transferts (icône de flèches tournantes). Appuyez dessus pour ouvrir la File des transferts où vous surveillez chaque téléchargement et envoi sur toutes vos sources.

{{< cards cols="1">}}
  {{< card title="" subtitle="Fichiers Evervideo sur les stockages connectés" image="/docs/guide/evervideo/img/evervideo-files-connected-storages.webp" >}}
{{< /cards >}}

## Se connecter au stockage cloud

La section Stockage cloud de l'onglet Fichiers est l'endroit où vivent chaque compte connecté, NAS, serveur multimédia et flux — côte à côte, dans une liste défilable unique.

{{< cards cols="1">}}
  {{< card title="" subtitle="Section Stockage cloud d'Evervideo dans l'onglet Fichiers" image="/docs/guide/evervideo/img/evervideo-connections.webp" >}}
{{< /cards >}}

- Ouvrez l'onglet **Fichiers**.
- Faites défiler jusqu'à la section **Stockage cloud**.
- Appuyez sur **Se connecter au stockage cloud** dans le menu.
- Choisissez un service de stockage cloud dans la liste.
- Entrez vos identifiants sur la page d'autorisation officielle fournie par le fournisseur cloud, puis appuyez sur **Fait**.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Connecter un service de stockage cloud" image="/docs/guide/evervideo/img/evervideo-connect-cloud-storage.webp" >}}
{{< /cards >}}

Si vous rencontrez des problèmes, vérifiez votre connexion internet et vos identifiants. Dans la version Premium de l'application, vous pouvez ajouter un nombre illimité de services ; la version gratuite prend en charge jusqu'à trois.

## Services de stockage cloud, serveurs multimédias et protocoles pris en charge

Evervideo prend en charge une gamme exceptionnellement large de sources pour vos vidéos. Tout ce qui suit fonctionne depuis un seul flux Se connecter au stockage cloud.

**Stockage cloud personnel :** iCloud Drive · Dropbox · OneDrive · Google Drive · MEGA · Box · pCloud · Yandex Disk · WD My Cloud Home · MediaFire · TeraCLOUD (InfiniCLOUD) · HiDrive · IceDrive · Koofr · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Internxt · Proton Drive · AliDrive (阿里云盘) · Baidu Pan (百度网盘).

**Serveurs multimédias auto-hébergés :** Plex · Jellyfin · Emby · Subsonic (et chaque serveur compatible Subsonic — Airsonic, Funkwhale, Gonic, Ampache) · Navidrome · Nextcloud (et ownCloud via l'API partagée) · Synology Drive · QNAP.

**NAS et protocoles de partage de fichiers :** SMB (SMB1, SMB2, Auto) · WebDAV (HTTP / HTTPS) · FTP · FTPS · SFTP (SSH File Transfer Protocol, mot de passe ou authentification par clé publique) · NFS · DLNA / UPnP (lecture et téléchargement).

**Flux live et caméras IP :** RTSP — pointez Evervideo sur n'importe quelle URL `rtsp://` et ça joue. Idéal pour les caméras de sécurité, les flux IPTV, les caméras de sonnette, les moniteurs bébé et autres sources live similaires.

**Stockage objet compatible S3 :** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, et tout autre endpoint S3-API.

**Bibliothèques sur l'appareil :** la bibliothèque Photos (toutes les vidéos, enregistrements d'écran, albums photos) et la bibliothèque de l'app Musique (Albums, Genres, Listes de lecture) — les deux s'affichent dans la Médiathèque sans avoir à copier quoi que ce soit.

**Découverte de réseau local :** la section Appareils disponibles liste automatiquement chaque service Bonjour / mDNS sur votre réseau Wi-Fi — serveurs Plex, Jellyfin, Emby, Synology, QNAP, routeurs AirPort avec lecteurs attachés, Apple Time Capsule — vous pouvez donc appuyer pour vous connecter sans saisir d'adresse IP.

Chaque connexion utilise le SDK officiel ou le protocole ouvert du service, avec autorisation OAuth là où c'est pris en charge. Vous pouvez connecter plusieurs comptes du même service (par exemple, deux comptes Google Drive, ou à la fois un serveur Plex et un serveur Jellyfin) et les parcourir côte à côte dans la section Stockage cloud.

## Sécurité et confidentialité

Evervideo utilise uniquement des SDK officiels et des connexions sécurisées pour interagir avec les services cloud connectés. Vos identifiants ne sont pas accessibles à l'application — tous les transferts sont chiffrés TLS.

Lorsque vous entrez vos identifiants, l'application vous montre la page d'autorisation officielle fournie par le fournisseur de service cloud, et l'ensemble du processus d'autorisation se déroule en dehors de l'application. Le fournisseur de service cloud envoie ensuite un auth-token à l'application après une autorisation réussie, et ce token est utilisé pour effectuer des appels API.

Un auth-token est une clé numérique qui permet aux applications tierces d'interagir avec le stockage cloud en votre nom. Le token est stocké sur votre appareil dans le stockage système sécurisé d'Apple (Keychain), qui est chiffré au repos et protégé par le code de votre appareil ou le verrou biométrique. Vous pouvez télécharger des fichiers depuis les services cloud connectés sur votre appareil ; ces fichiers sont placés dans le répertoire Documents de l'app et peuvent être supprimés à tout moment à l'aide du gestionnaire de fichiers intégré.

L'application ne partage aucune information de vos comptes cloud connectés avec Everappz, des annonceurs, ou tout tiers. Vous pouvez révoquer l'accès à votre compte cloud à tout moment en ouvrant la page de paramètres du compte dans votre navigateur web.

## Révoquer l'auth-token

Pour révoquer un auth-token, connectez-vous à votre compte cloud dans un navigateur web et accédez à la page de sécurité ou des applications connectées. Vous pouvez y trouver chaque application tierce connectée à votre compte cloud et en supprimer si vous ne souhaitez plus l'utiliser. Des instructions détaillées pour les comptes Google sont disponibles [ici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Vous pouvez également déconnecter le compte cloud dans l'application elle-même — lorsque vous le faites, l'auth-token est immédiatement supprimé de votre appareil. Si vous désinstallez l'application de votre appareil, toutes les données téléchargées et les tokens d'accès sont automatiquement supprimés avec elle.

## Déconnecter un stockage cloud ou modifier la configuration

- **Accéder aux options de stockage cloud** — localisez le service connecté dans la section **Stockage cloud** de l'onglet Fichiers.
- **Appuyez sur le bouton « ... »** à côté du titre du service pour ouvrir des options supplémentaires :
  - **Renommer** — changer le nom du service cloud tel qu'il apparaît dans votre liste.
  - **Paramètres** — modifier la configuration ou les données d'authentification. Il peut arriver que vous deviez ré-autoriser le service cloud connecté si le token d'autorisation a expiré.
  - **Se déconnecter** — couper complètement la connexion entre l'application et le service cloud. Cela supprime toutes les vidéos associées à ce service de votre médiathèque, mais les laisse intactes sur le serveur.

## Se connecter à un ordinateur ou un NAS

Vous pouvez connecter votre ordinateur, NAS personnel ou autre périphérique réseau en utilisant le protocole SMB, WebDAV, FTP / FTPS, SFTP, NFS ou DLNA. C'est le moyen le plus simple d'intégrer une bibliothèque multimédia domestique existante — qu'elle se trouve sur un Mac, un PC Windows, Synology, QNAP, Apple Time Capsule ou WD My Cloud Home — dans Evervideo sans rien copier.

### Se connecter à un ordinateur via SMB

- Appuyez sur **Se connecter au stockage cloud → SMB**.
- Entrez l'adresse IP de l'ordinateur et le nom du dossier partagé en utilisant le format `smb://adresse-ip-ordinateur/nom-dossier-partage`.
- Choisissez la version du protocole : **Auto**, **SMB1**, ou **SMB2**.
- Entrez votre identifiant et mot de passe (si requis).
- Appuyez sur **Fait**.

Si la connexion est réussie, le partage apparaît dans la section Stockage cloud. Un tutoriel complet sur la connexion de votre Mac ou PC via SMB est disponible [ici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

### Se connecter à un NAS via WebDAV

Toutes les étapes sont identiques à SMB, sauf pour le champ URL. Utilisez `http://nom-serveur` ou `https://nom-serveur` si le serveur prend en charge SSL. WebDAV fonctionne avec Synology, QNAP, Nextcloud, ownCloud, WD My Cloud Home et tout autre serveur avec un endpoint WebDAV.

Un tutoriel complet sur WebDAV est disponible [ici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

### Se connecter via DLNA / UPnP

Partagez une bibliothèque multimédia située sur votre PC Windows ou NAS en utilisant le protocole DLNA / UPnP et accédez-y dans Evervideo comme décrit [ici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA est largement pris en charge, mais il vous permet uniquement de lire ou télécharger des vidéos — vous ne pouvez pas téléverser de fichiers ou créer de nouveaux dossiers sur un serveur DLNA.

### Se connecter via FTP, FTPS ou SFTP

Evervideo prend également en charge les protocoles de transfert de fichiers classiques. Pour connecter un serveur via FTP ou FTPS, appuyez sur Se connecter au stockage cloud → FTP, entrez l'URL hôte au format `ftp://nom-serveur` (ou `ftps://nom-serveur` pour une connexion chiffrée), fournissez votre identifiant et mot de passe, puis appuyez sur Fait. Pour SFTP (SSH File Transfer Protocol), choisissez SFTP à la place et fournissez soit un mot de passe, soit une paire de clés SSH.

### Se connecter à un partage NFS

Evervideo inclut la prise en charge NFS (Network File System) — pratique pour les hôtes Linux, les serveurs BSD et les périphériques NAS qui préfèrent exposer les bibliothèques vidéo via NFS plutôt que SMB. Choisissez NFS dans le menu Se connecter au stockage cloud, entrez l'adresse du serveur et le chemin exporté, et appuyez sur Fait.

## Connecter un serveur Plex Media

Evervideo peut se connecter directement à un serveur Plex Media et parcourir vos bibliothèques Films, Séries TV et Vidéos personnelles. Appuyez sur Se connecter au stockage cloud → Plex, connectez-vous avec votre compte Plex, choisissez un serveur, et la bibliothèque apparaît aux côtés de vos services cloud. Les serveurs Plex sur le même réseau local sont également découverts automatiquement dans la section Appareils disponibles.

## Connecter un serveur Jellyfin ou Emby

Jellyfin (open-source) et Emby (commercial) fonctionnent nativement dans Evervideo. Appuyez sur Se connecter au stockage cloud → Jellyfin ou Emby, entrez l'URL de votre serveur (généralement quelque chose comme `http://ip-serveur:8096`) et vos identifiants, et votre bibliothèque est prête à être diffusée.

## Connecter un serveur Subsonic ou Navidrome

Evervideo parle l'API Subsonic, ce qui signifie qu'il fonctionne avec Subsonic lui-même, Navidrome, et tout autre serveur compatible Subsonic — y compris Airsonic, Funkwhale, Gonic, Logitech Media Server (LMS) et Ampache. Appuyez sur Se connecter au stockage cloud → Subsonic, entrez l'URL du serveur et les identifiants, et la bibliothèque apparaît dans la section Stockage cloud.

## Connecter un flux RTSP (caméras IP, TV en direct, IPTV)

Evervideo dispose d'une prise en charge RTSP native, vous pouvez donc le pointer vers n'importe quelle source RTSP — caméras de sécurité, caméras de sonnette, fournisseurs IPTV, moniteurs bébé, flux de diffusion — et Evervideo tirera et décodera le flux en direct. Appuyez sur Liens en ligne → Ajouter un lien, collez l'URL complète (`rtsp://camera-ip:port/chemin-flux`), fournissez l'identifiant et le mot de passe si requis, et appuyez sur Fait.

## Se connecter au stockage objet compatible S3

Pour les auto-hébergeurs et les utilisateurs avancés utilisant le stockage objet cloud, Evervideo inclut un connecteur compatible S3. Appuyez sur Se connecter au stockage cloud → Stockage S3, puis entrez l'URL du point de terminaison, la région, la clé d'accès, la clé secrète et le nom du bucket. Cela fonctionne avec AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces et tout autre endpoint S3-API.

## Appareils disponibles

Cette section affiche chaque appareil sur votre réseau local auquel vous pouvez vous connecter depuis Evervideo via la découverte Bonjour / mDNS — serveurs Plex, Jellyfin, Emby, Synology, QNAP, routeurs AirPort avec lecteurs attachés, Apple Time Capsule, et ainsi de suite. Pour établir une connexion :

- Faites défiler jusqu'à la section Appareils disponibles dans l'onglet Fichiers.
- Appuyez sur l'appareil auquel vous souhaitez vous connecter.
- Si nécessaire, entrez vos coordonnées pour compléter la connexion.

{{< cards cols="1">}}
  {{< card title="" subtitle="Appareils disponibles Evervideo sur le réseau local" image="/docs/guide/evervideo/img/evervideo-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive vous permet de transférer des fichiers sans fil de votre ordinateur vers votre appareil iOS via n'importe quel navigateur de bureau, Finder ou File Explorer. Votre appareil et votre ordinateur doivent être sur le même réseau Wi-Fi.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo Wi-Fi Drive" image="/docs/guide/evervideo/img/evervideo-wifi-drive.webp" >}}
{{< /cards >}}

### Activer Wi-Fi Drive

- Dans l'onglet Fichiers, faites défiler jusqu'à Stockage cloud → Se connecter via Wi-Fi pour ouvrir l'écran principal de Wi-Fi Drive.
- (Facultatif) Définissez un nom d'utilisateur et un mot de passe pour le serveur web intégré.
- Appuyez sur Démarrer Wi-Fi Drive.

### Accéder à Wi-Fi Drive depuis votre ordinateur

- Ouvrez un navigateur web sur votre ordinateur (Chrome, Firefox, Safari, etc.).
- Entrez l'URL affichée par l'application.
- Faites glisser et déposez des fichiers de votre ordinateur sur la page web — ils commenceront à se transférer vers votre appareil iOS.

Vous pouvez également monter Wi-Fi Drive directement dans **Finder** sur macOS (Aller → Se connecter au serveur…) ou File Explorer sur Windows (Mapper un lecteur réseau…) et traiter votre iPhone ou iPad comme un lecteur réseau ordinaire.

Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes / Finder File Sharing

iTunes File Sharing (maintenant Finder File Sharing sur macOS Catalina et versions ultérieures) vous permet de transférer des fichiers à l'aide d'un câble Lightning ou USB-C. Connectez l'appareil, ouvrez Finder sur Mac (ou iTunes sur Windows), trouvez Evervideo dans la liste des applications, et copiez les fichiers dans son dossier partagé.

## Connecter un lecteur flash USB ou une carte SD

Branchez un lecteur USB ou une carte SD dans votre iPhone, iPad ou Mac via l'adaptateur Lightning-USB / USB-C ou le lecteur de cartes. Ouvrez Fichiers → Fichiers sur cet iPhone → Ouvrir un dossier, naviguez jusqu'au lecteur, et choisissez un fichier vidéo ou un dossier. Evervideo lit les fichiers directement depuis le lecteur sans les copier dans le stockage interne — pratique pour les très grandes bibliothèques 4K.

## Navigation dans les dossiers des stockages connectés

Appuyez sur n'importe quel service cloud connecté pour ouvrir son navigateur de fichiers. Les dossiers affichent des miniatures vidéo lorsqu'elles sont disponibles, et appuyer sur une vidéo démarre immédiatement la lecture tout en continuant à diffuser le reste du fichier en arrière-plan.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Navigation dans les dossiers des stockages connectés" image="/docs/guide/evervideo/img/evervideo-all-connected-device-folders.webp" >}}
{{< /cards >}}

## Accès rapide

La section Accès rapide se trouve en haut de l'onglet Fichiers. Elle vous donne un accès rapide à vos fichiers et dossiers favoris et récemment ouverts — à la fois depuis les services cloud et depuis le stockage sur l'appareil. Chaque fois que vous ouvrez un fichier ou un dossier depuis le cloud, il est ajouté à la liste Récemment ouverts. Vous pouvez marquer les dossiers profondément imbriqués comme Favoris pour y accéder rapidement sans creuser dans la structure de répertoires.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Liens en ligne et accès rapide" image="/docs/guide/evervideo/img/evervideo-connections-online-links.webp" >}}
{{< /cards >}}

## Fichiers dans cette application

Cette section affiche les fichiers et dossiers stockés dans le répertoire Documents sandboxé d'Evervideo — tout ce que vous avez téléchargé depuis le cloud, transféré via Wi-Fi Drive, copié via Finder File Sharing, ou importé depuis une autre application.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Fichiers dans cette application" image="/docs/guide/evervideo/img/evervideo-files-in-this-application.webp" >}}
{{< /cards >}}

### Dossier Documents

Le dossier Documents est la racine de tout ce qui se trouve dans Fichiers dans cette application. Vous pouvez créer des sous-dossiers, renommer des fichiers, les déplacer et les regrouper comme vous le souhaitez.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Fichiers locaux — Dossier Documents" image="/docs/guide/evervideo/img/evervideo-local-files-documents.webp" >}}
{{< /cards >}}

## Fichiers sur cet iPhone / iPad / Mac

Cette section affiche les vidéos situées sur votre appareil mais dans des applications différentes. Vous pouvez les importer dans Evervideo à l'aide du sélecteur de fichiers système :

- Appuyez sur Ouvrir des fichiers… pour sélectionner des fichiers spécifiques.
- Appuyez sur Ouvrir un dossier… pour sélectionner un dossier entier.

Vous pouvez également utiliser Connecter un dossier pour créer un lien vers un dossier sur votre appareil avec un accès lecture / écriture — idéal pour travailler avec un dossier sur iCloud Drive ou un lecteur USB attaché sans rien copier.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Fichiers sur cet appareil" image="/docs/guide/evervideo/img/evervideo-files-on-this-device.webp" >}}
{{< /cards >}}

## Dossiers spéciaux

Dans l'onglet Fichiers, vous verrez plusieurs dossiers spéciaux qu'Evervideo crée et utilise automatiquement :

- **Téléchargements** — chaque fichier téléchargé depuis le cloud apparaît ici par défaut. Personnalisez dans Paramètres → Gestionnaire de fichiers → Enregistrer les fichiers téléchargés dans.
- **Cache du lecteur** — le cache du lecteur multimédia. Par défaut, le lecteur télécharge les vidéos à venir pour une lecture fluide. Vous pouvez désactiver le cache dans les paramètres de l'application ou simplement supprimer ce dossier.
- **iCloud** — les fichiers dans ce dossier se synchronisent sur tous vos appareils connectés au même compte iCloud.
- **Dossiers hors ligne** — lorsque vous marquez un dossier, une liste de lecture, un album ou un genre comme disponible hors ligne, les fichiers sont téléchargés dans ce dossier.

## Barre d'outils supérieure

La barre d'outils supérieure, située sous la barre de navigation, offre plusieurs actions que vous pouvez afficher ou masquer avec un geste de balayage vers le bas :

- **Recherche** — effectuer une recherche dans le dossier ou la section actuel.
- **Continuer la lecture** — si activé dans les paramètres, restaurer la file du lecteur et la dernière position vidéo pour le dossier actuel.
- **Tout lire** — analyser le dossier actuel et ses sous-dossiers et ajouter des fichiers à la file du lecteur.
- **Tout mélanger** — comme Tout lire, mais mélange avant d'ajouter.

## Options de dossier

Lorsque vous ouvrez un dossier, appuyez sur le bouton **« ... »** dans le coin supérieur droit pour ces actions :

- **Sélectionner** — activer le mode de sélection de fichiers.
- **Nouveau dossier** — créer un nouveau dossier dans le dossier actuel.
- **Activer le mode hors ligne** — activer la synchronisation hors ligne pour le dossier actuel. Les nouveaux fichiers ajoutés en ligne sont téléchargés automatiquement.
- **Téléverser des fichiers** — téléverser des fichiers depuis votre appareil vers le dossier en ligne.
- **Rechercher** — rechercher dans le dossier.
- **Trier** — trier les fichiers par nom, taille, date de modification ou métadonnées.
- **Vue grille / liste** — basculer entre la vue tableau et la vue miniatures. La vue miniatures affiche de grands aperçus des affiches vidéo.

## Mode sélection

Appuyez sur **« ... »** dans le coin supérieur droit et choisissez **Sélectionner** pour entrer en mode sélection. Des cases à cocher apparaissent à côté de chaque fichier et dossier. Appuyez pour sélectionner un ou plusieurs éléments, puis effectuez des actions par lots : Lire ensuite, Lire plus tard, Ajouter à la médiathèque, Ajouter à une liste de lecture, Copier, Téléverser, Déplacer, Renommer ou Supprimer.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Mode sélection dans le gestionnaire de fichiers" image="/docs/guide/evervideo/img/evervideo-selection-mode-in-files.webp" >}}
{{< /cards >}}

Si vous préférez traiter le stockage cloud connecté en lecture seule (pour éviter les suppressions accidentelles), activez Paramètres → Gestionnaire de fichiers → Modifier les fichiers en ligne → Désactivé pour masquer toutes les opérations destructives de l'interface.

## Actions sur les fichiers

Appuyez sur l'icône **« ... »** près du titre d'un fichier pour révéler son menu d'actions :

- **Lire ensuite** — insérer le fichier en haut de la file du lecteur.
- **Lire plus tard** — ajouter le fichier en bas de la file du lecteur.
- **Ajouter à la médiathèque** — incorporer le fichier dans votre médiathèque, organisé par Album et Genre.
- **Ajouter à une liste de lecture** — ajouter le fichier à une liste de lecture existante ou en créer une nouvelle.
- **Modifier les tags** — ouvrir l'éditeur de tags intégré pour modifier les métadonnées. Pour les fichiers en ligne, le fichier est temporairement téléchargé, édité, puis ré-uploadé après confirmation.
- **Ajouter aux favoris** — ajouter le fichier à votre liste de favoris pour un accès rapide.
- **Télécharger** — télécharger le fichier ou le dossier sur votre appareil pour une utilisation hors ligne.
- **Renommer** — renommer le fichier directement sur le stockage distant.
- **Déplacer** — déplacer le fichier dans un autre dossier de votre stockage cloud.
- **Ajouter à l'archive** — regrouper le fichier dans un seul fichier ZIP (fonctionnalité Premium).
- **Ouvrir dans** — exporter le fichier vers une autre application compatible via la feuille de partage système.
- **Supprimer** — supprimer définitivement le fichier. **Cette action ne peut pas être annulée.**

## Actions sur les dossiers

Pour chaque dossier dans votre stockage cloud, vous avez de nombreuses actions disponibles en appuyant sur l'icône **« ... »** à côté du titre du dossier.

- **Tout lire** — remplacer la file du lecteur actuel par chaque vidéo dans le dossier.
- **Lire ensuite / Lire plus tard** — ajouter le dossier entier à la file.
- **Ajouter à la médiathèque** — incorporer le contenu du dossier dans votre médiathèque.
- **Ajouter à la liste de lecture** — ajouter le dossier entier à une liste de lecture.
- **Ajouter aux favoris** — ajouter le dossier à vos favoris.
- **Activer le mode hors ligne** — au-delà d'un simple téléchargement, cela surveille en permanence le dossier pour les nouveaux fichiers et les télécharge automatiquement à mesure qu'ils apparaissent en ligne.
- **Télécharger** — télécharger tout le contenu du dossier sur votre appareil pour un accès hors ligne.
- **Renommer / Déplacer** — renommer ou déplacer le dossier sur le stockage distant.
- **Ajouter à l'archive** — regrouper le contenu du dossier dans un fichier ZIP (fonctionnalité Premium).
- **Supprimer** — supprimer définitivement le dossier et son contenu. **Cette action ne peut pas être annulée.**

## File des transferts

Dans le coin supérieur droit de l'onglet Fichiers se trouve un bouton **Transferts** (icône de flèches tournantes). Appuyez dessus pour ouvrir la File des transferts — une liste de chaque téléchargement et envoi actif sur toutes vos sources, avec la progression en temps réel, la vitesse et l'heure d'arrivée estimée par fichier.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — File de transferts de fichiers" image="/docs/guide/evervideo/img/evervideo-file-transfers.webp" >}}
{{< /cards >}}

Vous pouvez mettre en pause, reprendre, réessayer les transferts échoués, réorganiser les éléments pour prioriser des téléchargements spécifiques, ou les annuler individuellement. Vous pouvez également ajuster la vitesse de la file de transferts (tâches parallèles maximales), le type de réseau (Wi-Fi uniquement ou Wi-Fi + cellulaire) et les transferts en arrière-plan dans Paramètres → Gestionnaire de fichiers.

{{< cards cols="1">}}
  {{< card title="" subtitle="Evervideo — Actions sur la file de transferts de fichiers" image="/docs/guide/evervideo/img/evervideo-file-transfers-actions.webp" >}}
{{< /cards >}}

## Mode hors ligne et dossiers hors ligne synchronisés

Le mode hors ligne est une fonctionnalité pratique qui vous permet de regarder vos vidéos préférées même lorsque vous n'êtes pas connecté à Internet. Lorsque vous activez le mode hors ligne pour n'importe quel dossier, liste de lecture, album ou genre, tous les fichiers de cette collection sont automatiquement téléchargés sur votre appareil pour une lecture hors ligne. Ils apparaissent dans la section Dossiers hors ligne.

Lorsque vous ajoutez de nouveaux fichiers au serveur distant, ils sont également automatiquement téléchargés — votre collection hors ligne reste donc à jour sans que vous ayez à faire quoi que ce soit. Pour resynchroniser manuellement, appuyez sur les trois points dans le coin supérieur droit d'un dossier hors ligne et sélectionnez Synchroniser.

Vous pouvez ajuster le délai de synchronisation dans Paramètres → Gestionnaire de fichiers → Dossiers hors ligne synchronisés → Intervalle de temps.

Des instructions détaillées sont disponibles [ici](/docs/howto/play-offline-music-in-evermusic-flacbox-download-sync-from-cloud-to-local-files/).

## Personnalisation

Dans Paramètres → Personnalisation, vous pouvez configurer comment l'onglet Fichiers est présenté :

- **Style de l'écran Fichiers** — Menu simple (affiche directement la liste de dossiers) ou Menu groupé (regroupe le contenu par catégorie — Accès rapide, Dossiers spéciaux, Stockage cloud, etc.).
