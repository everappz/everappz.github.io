---
title: "Connexions"
date: 2020-01-01
description: "Apprenez à connecter des services cloud, des ordinateurs, des appareils NAS et à gérer vos fichiers musicaux avec Evermusic. Guide étape par étape pour Wi-Fi Drive, SMB, DLNA, WebDAV, iTunes File Sharing et bien plus."
keywords: [
  "Evermusic", "lecteur musique cloud", "streaming NAS", "Wi-Fi Drive",
  "SMB", "WebDAV", "DLNA", "iTunes File Sharing",
  "connecter stockage cloud", "transfert musique iPhone", "gestionnaire fichiers iOS"
]
tags: ["evermusic", "guide", "connexions"]
readingTime: 11
---


Sur l'écran Connexions, vous pouvez connecter toutes les sources contenant votre musique — services cloud populaires, serveurs multimédia auto-hébergés, votre Mac ou PC, un NAS personnel, Apple Time Capsule, WD My Cloud Home, même une clé USB — et les utiliser depuis une interface unifiée. Connexions est aussi l'endroit où vous configurez l'accès rapide aux dossiers cloud profondément imbriqués et où vous authentifiez Last.fm pour le scrobbling.

L'écran est divisé en sections clairement étiquetées pour s'adapter d'un seul compte iCloud Drive à une bibliothèque répartie sur plusieurs clouds et NAS : Accès rapide en haut (vos dossiers cloud favoris), Stockage cloud (les comptes que vous avez ajoutés), Réseau local (appareils découverts par Bonjour), Ordinateur (Wi-Fi Drive, iTunes File Sharing, SMB), Accessoires externes (clés USB connectées) et Autres services (Last.fm et similaires).

{{< cards cols="1">}}
  {{< card title="" subtitle="Écran Connexions d'Evermusic" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-main.webp" >}}
{{< /cards >}}

## Se connecter au stockage cloud

- Ouvrez l'onglet Connexions.
- Sélectionnez Se connecter au stockage cloud dans le menu.
- Choisissez un service de stockage cloud dans la liste.
- Connectez-vous sur la page d'autorisation officielle du fournisseur (Evermusic ne voit jamais votre mot de passe).
- Appuyez sur Terminé.

{{< cards cols="1">}}
  {{< card title="" subtitle="Sélecteur de fournisseur de stockage cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-add-storage.webp" >}}
{{< /cards >}}

Si vous rencontrez des problèmes, vérifiez votre connexion Internet et vos identifiants, et assurez-vous que l'authentification à deux facteurs est correctement configurée pour ce service.  
Dans la version Premium de l'application, vous pouvez ajouter un nombre illimité de services. Les utilisateurs gratuits peuvent connecter un seul compte cloud à la fois.

## Services de stockage cloud pris en charge

Evermusic prend en charge la gamme complète de services cloud populaires et auto-hébergés. Les utilisateurs gratuits accèdent au même catalogue de fournisseurs mais avec la limite d'un seul compte ; Premium déverrouille des comptes illimités et supprime la plupart des autres limites.

- **Comptes cloud personnels :** iCloud Drive · Google Drive · Dropbox · OneDrive · Box · MEGA · Yandex.Disk · pCloud · MediaFire · WD My Cloud Home · InfiniCLOUD (TeraCLOUD) · HiDrive · OpenDrive · MyDrive · Put.io · Cloud Mail.ru · Icedrive · Koofr · Proton Drive · Internxt · AliDrive (阿里云盘) · Baidu Pan (百度网盘).
- **Serveurs auto-hébergés et bibliothèques multimédia :** Plex · Jellyfin · Emby · Subsonic (et tout serveur compatible Subsonic — Airsonic, Funkwhale, Gonic, Logitech Media Server, Ampache) · Navidrome · Nextcloud (et Owncloud, via l'API partagée) · Synology Drive · QNAP.
- **NAS et protocoles de partage de fichiers :** SMB (SMB1, SMB2, Auto), WebDAV (HTTP / HTTPS), FTP / FTPS, SFTP (authentification par mot de passe ou clé publique), NFS et DLNA (lecture seule — lecture et téléchargement).
- **Stockage objet compatible S3 :** AWS S3, Backblaze B2, Wasabi, Cloudflare R2, MinIO, DigitalOcean Spaces, Linode Object Storage, IBM Cloud Object Storage ou tout point de terminaison API S3.
- **Découverte réseau local :** la section Appareils disponibles liste automatiquement tous les appareils sur votre Wi-Fi qui s'annoncent via Bonjour / mDNS — serveurs Plex, Jellyfin, Emby, Synology, QNAP, WD My Cloud Home, Apple Time Capsule, routeurs AirPort avec disques attachés, etc.

## Sécurité et confidentialité

Nous utilisons uniquement le SDK officiel et une connexion sécurisée pour interagir avec les services cloud connectés. Votre identifiant et mot de passe ne sont pas accessibles par l'application. Toutes les requêtes de l'application vers le service cloud sont chiffrées.

Lorsque vous entrez vos identifiants, l'application vous affiche la page d'autorisation officielle fournie par le fournisseur de service cloud et tout le processus d'autorisation se déroule en dehors de l'application. Le fournisseur envoie un jeton d'authentification à l'application après une autorisation réussie et ce jeton est utilisé pour effectuer les appels API.

Le jeton d'authentification est une clé numérique qui permet aux applications tierces d'interagir avec le stockage cloud. Il est stocké sur votre appareil dans un système de stockage sécurisé appelé Keychain. Vous pouvez télécharger vos fichiers depuis le service cloud connecté vers l'appareil et ces fichiers seront placés dans le répertoire « Documents » de l'application. Vous pouvez les supprimer à tout moment en utilisant le gestionnaire de fichiers intégré.

L'application ne partage aucune information du compte cloud connecté. Vous pouvez révoquer l'accès à votre compte cloud à tout moment en ouvrant la page des paramètres du compte dans votre navigateur web.

## Révoquer le jeton d'authentification

Connectez-vous à votre compte dans le navigateur web et accédez à la page des paramètres. Vous y trouverez toutes les applications tierces connectées à votre compte cloud et pourrez en supprimer si vous ne souhaitez plus utiliser cette application. Des instructions détaillées sont disponibles [ici](/docs/howto/how-to-disconnect-third-party-app-from-your-google-account).

Vous pouvez également déconnecter les comptes cloud connectés dans l'application et le jeton d'authentification sera également supprimé de votre appareil. Si vous supprimez l'application de votre appareil, toutes les données téléchargées et les jetons d'accès seront également supprimés.

## Déconnecter un stockage cloud ou modifier la configuration

- Accédez aux options de stockage cloud : localisez d'abord le stockage cloud que vous souhaitez gérer dans l'interface de l'application.
- Appuyez sur le bouton '...' : à côté du titre du service, vous verrez un bouton '...'. Appuyez dessus pour accéder aux options supplémentaires.
  - **Renommer** : si vous souhaitez changer le nom du service cloud tel qu'il apparaît dans votre liste, sélectionnez 'Renommer'.
  - **Paramètres** : pour modifier la configuration ou les données d'authentification du service cloud, choisissez 'Paramètres'. Parfois, vous devrez peut-être réautoriser le service cloud connecté si le jeton d'autorisation a expiré.
  - **Se déconnecter** : si vous souhaitez couper complètement la connexion entre l'application et le service cloud, sélectionnez 'Se déconnecter'. Sachez que cette option supprimera toutes les chansons associées à ce service cloud de la bibliothèque musicale de l'application, mais elles resteront sur le serveur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Plus d'actions pour le stockage cloud connecté" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-storage-more-actions.webp" >}}
{{< /cards >}}

## Se connecter à un ordinateur ou un NAS

Vous pouvez également connecter votre ordinateur, un NAS personnel ou d'autres appareils réseau en utilisant les protocoles SMB, DLNA ou WebDAV.

## Se connecter à un ordinateur via SMB

- Appuyez sur « Se connecter au stockage cloud » → SMB.
- Entrez l'adresse IP de l'ordinateur et le nom du dossier partagé dans le champ URL au format smb://adresse-ip-ordinateur/nom-dossier-partage
- Choisissez la version du protocole : Auto, SMB1, SMB2
- Entrez l'identifiant et le mot de passe (si requis)
- Appuyez sur « Terminé ».

Si votre connexion est réussie, vous verrez le stockage connecté dans la section « Stockage cloud ».  
Un tutoriel complet sur la façon de connecter votre Mac ou PC via SMB est disponible [ici](/docs/howto/stream-your-music-from-mac-or-pc-to-iphone-using-smb/).

{{< cards cols="1">}}
  {{< card title="" subtitle="Paramètres de connexion SMB" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-smb-settings.webp" >}}
{{< /cards >}}

## Se connecter à un NAS via WebDAV

Toutes les étapes sont identiques, sauf pour le champ URL.  
L'URL doit être au format http://nom-serveur, ou https://nom-serveur si le serveur prend en charge SSL.
Un tutoriel complet sur la connexion d'un NAS via le protocole WebDAV est disponible [ici](/docs/howto/how-to-connect-nas-storage-using-webdav-and-listen-to-music-on-your-iphone-or-mac).

{{< cards cols="1">}}
  {{< card title="" subtitle="Paramètres de connexion WebDAV" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-webdav-settings.webp" >}}
{{< /cards >}}

## Se connecter à un ordinateur ou NAS via DLNA

Vous pouvez également partager une bibliothèque musicale sur votre PC Windows ou NAS personnel en utilisant le protocole DLNA et accéder à cette bibliothèque dans l'application comme décrit [ici](/docs/howto/how-to-enable-dlna-media-server-on-windows-10-and-play-your-music-on-iphone). DLNA est un protocole populaire et largement utilisé, mais il vous permet uniquement de lire ou de télécharger de la musique. Vous ne pouvez pas téléverser des fichiers ni créer de nouveaux dossiers sur le serveur.

{{< cards cols="1">}}
  {{< card title="" subtitle="Paramètres de connexion DLNA" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-dlna-settings.webp" >}}
{{< /cards >}}

## Appareils disponibles

Cette section affiche tous les appareils de votre réseau local auxquels vous pouvez vous connecter via l'application.  
Pour établir une connexion avec un appareil, suivez ces étapes :

- Ouvrez l'application et accédez à la section « Appareils disponibles ».
- Appuyez sur l'appareil auquel vous souhaitez vous connecter dans la liste.
- Si nécessaire, entrez vos identifiants de connexion pour compléter la connexion.

{{< cards cols="1">}}
  {{< card title="" subtitle="Appareils disponibles sur le réseau local" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-available-devices.webp" >}}
{{< /cards >}}

## Wi-Fi Drive

Wi-Fi Drive est une technologie pratique qui permet les transferts de fichiers sans fil de votre ordinateur vers votre appareil iOS via un navigateur de bureau.  
Pour utiliser efficacement cette fonctionnalité, assurez-vous que votre appareil et votre ordinateur sont connectés au même réseau Wi-Fi.   
Voici un guide étape par étape pour utiliser Wi-Fi Drive.

## Activer Wi-Fi Drive

- Ouvrez l'application et accédez à l'onglet « Connexions ».
- Sélectionnez « Se connecter via Wi-Fi » pour accéder à l'écran principal de Wi-Fi Drive.
- Appuyez sur « Démarrer Wi-Fi Drive » pour activer Wi-Fi Drive.

## Accéder à Wi-Fi Drive sur votre ordinateur

- Sur votre ordinateur (de bureau ou portable), ouvrez un navigateur web (tel que Chrome, Firefox ou Safari).
- Dans la barre d'adresse du navigateur, entrez l'URL fournie par l'application.

## Transférer des fichiers sans fil

Une fois que la page web correspondant à votre appareil iOS s'ouvre dans le navigateur, vous pouvez facilement glisser-déposer des fichiers de votre ordinateur vers la page web.  
Les fichiers que vous glissez-déposez commenceront à être transférés vers votre appareil iOS et seront accessibles dans l'application.

{{< cards cols="1">}}
  {{< card title="" subtitle="Paramètres du serveur Wi-Fi Drive" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-wifidrive-settings.webp" >}}
{{< /cards >}}

Des instructions détaillées sur la façon de transférer des fichiers sans fil via WiFi-Drive sont disponibles [ici](/docs/howto/how-to-transfer-files-wirelessly-from-a-computer-to-an-iphone-using-wifi-drive).

## iTunes File Sharing

iTunes File Sharing est une autre technologie qui vous permet de transférer des fichiers de l'ordinateur vers l'appareil en utilisant l'application Finder sur votre Mac et un câble Lightning.   
- Connectez simplement un appareil à l'ordinateur avec un câble et lancez l'application Finder sur votre Mac. 
- Ouvrez « Emplacements » → « Votre appareil connecté » → « Fichiers » → et trouvez l'application Evermusic. 
- Appuyez sur l'icône de l'application pour voir tous les dossiers partagés. 
- Copiez les fichiers de l'ordinateur vers le dossier partagé sur l'appareil par glisser-déposer.   

Des instructions détaillées sur l'utilisation du partage de fichiers iTunes sont disponibles [ici](/docs/howto/how-to-play-local-itunes-files-on-my-iphone/).

{{< cards cols="1">}}
  {{< card title="" subtitle="iTunes / Finder File Sharing sur Mac" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-itunes-file-sharing.webp" >}}
{{< /cards >}}

## Connecter une clé USB

Si vous avez une carte SD, vous pouvez la connecter en utilisant un lecteur de carte Lightning. L'application prend actuellement en charge les lecteurs de carte certifiés Apple et les iXpand Flash Drives. Si vous avez un iXpand Flash Drive - insérez-le dans le port Lightning et ouvrez l'application. Vous verrez un message « Appareil externe connecté » avec les informations de l'appareil. Appuyez simplement sur l'icône de la clé pour accéder au dossier de musique et appuyez sur n'importe quel fichier audio pour commencer la lecture. Des instructions détaillées sur la façon de connecter une clé USB à l'iPhone et d'écouter de la musique ou de gérer les fichiers sur celle-ci sont disponibles [ici](/docs/howto/how-to-connect-a-usb-flashcard-to-the-iphone-and-listen-to-music-or-manage-files-located-on-it).

## Gestionnaire de fichiers

Une fois que vous avez connecté un service de stockage cloud, appuyez sur son icône pour afficher tous les fichiers et dossiers disponibles. Vous pouvez utiliser le gestionnaire de fichiers intégré pour travailler avec ces fichiers — télécharger, renommer, déplacer, et plus encore. Lorsque vous démarrez un téléchargement, le fichier apparaîtra dans la file de transfert. Pour afficher la file de transfert, accédez à l'onglet « Fichiers locaux » et appuyez sur les flèches rotatives dans le coin supérieur gauche. Tous les fichiers et dossiers téléchargés sont disponibles dans la section « Fichiers locaux ».

## Barre d'outils supérieure

La barre d'outils supérieure, pratiquement située sous la barre de navigation, offre plusieurs actions utiles pour un accès facile. Vous pouvez afficher ou masquer cette barre d'outils en utilisant un simple geste de glissement vers le bas. Voici les actions disponibles :

- **Rechercher** : cette option vous permet d'effectuer une recherche rapide dans le répertoire actuel, facilitant la localisation de fichiers ou dossiers spécifiques.
- **Continuer la lecture** : si activée dans les paramètres de l'application, cette fonctionnalité restaure la file d'attente du lecteur audio et la dernière position multimédia pour le dossier actuel. C'est une façon pratique de reprendre là où vous en étiez dans votre bibliothèque musicale.
- **Tout lire** : en sélectionnant cette action, l'application analysera le dossier actuel et ses sous-dossiers, ajoutant tous les fichiers audio trouvés à une nouvelle file d'attente du lecteur. Cela est utile lorsque vous souhaitez lire toute la musique dans un répertoire particulier.
- **Lecture aléatoire** : similaire à « Tout lire », cette action analyse le dossier actuel et ses sous-dossiers mais mélange les fichiers avant de les ajouter à la file d'attente du lecteur audio. C'est une excellente façon de profiter de votre musique dans un ordre aléatoire pour un peu de variété.

{{< cards cols="1">}}
  {{< card title="" subtitle="Barre d'outils supérieure dans un dossier cloud" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-top-toolbar.webp" >}}
{{< /cards >}}

## Options du dossier

Lorsque vous ouvrez un dossier dans l'application, vous trouverez un ensemble pratique d'actions disponibles en appuyant sur le bouton « ... » dans le coin supérieur droit de l'écran.   
Voici une description de ces actions :

- **Sélectionner** : activez le mode de sélection de fichiers. Ce mode vous permet de choisir un ou plusieurs fichiers dans le dossier, facilitant l'exécution d'actions sur les éléments sélectionnés.
- **Nouveau dossier** : créez un nouveau dossier dans le dossier actuel. Cette fonctionnalité vous permet d'organiser vos fichiers et de maintenir votre bibliothèque bien structurée.
- **Activer le mode hors ligne** : activez le mode hors ligne pour le dossier actuel. Le mode hors ligne va au-delà du simple téléchargement ; il surveille activement les changements dans le dossier. Si vous ajoutez de nouveaux fichiers au dossier en ligne, l'application les téléchargera automatiquement sur votre appareil. Cela garantit que votre bibliothèque locale reste à jour avec les changements sur le serveur.
- **Téléverser des fichiers** : téléversez des fichiers de votre appareil vers le dossier en ligne. Cette action vous permet de transférer des fichiers vers le cloud ou le serveur, les rendant accessibles de partout.
- **Rechercher** : recherchez des fichiers spécifiques dans le dossier actuel. Cela est particulièrement utile pour localiser rapidement des éléments spécifiques dans une grande collection.
- **Trier** : triez les fichiers dans le dossier par critères tels que le nom, la taille ou la date de modification. Le mode de tri par défaut reflète généralement l'ordre de tri sur le serveur, mais vous pouvez le modifier selon vos préférences.
- **Vue grille/liste** : basculez entre deux modes d'affichage : vue tableau et vue miniature. La vue tableau présente les fichiers sous forme de liste, tandis que la vue miniature affiche des représentations visuelles des fichiers, facilitant l'identification du contenu en un coup d'œil.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Plus d'actions pour le dossier actuel" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-folder-options.webp" >}}
{{< /cards >}}

## Modifier les fichiers en ligne

Lorsque vous avez besoin de gérer plusieurs fichiers dans votre stockage cloud sur Evermusic, vous pouvez utiliser le mode de sélection pour simplifier vos actions. Suivez ces étapes pour une gestion efficace des fichiers :

- **Activer le mode de sélection** : ouvrez l'application sur votre appareil et accédez à la section contenant votre stockage cloud. Recherchez dans le coin supérieur droit le bouton « ... » (points de suspension). Appuyez dessus et choisissez l'élément de menu « Sélectionner » pour activer le mode de sélection.
- **Choisir des fichiers** : vous remarquerez des cases à cocher apparaissant à côté de chaque fichier ou dossier répertorié. Choisissez un ou plusieurs fichiers ou dossiers en appuyant simplement sur les cases à cocher à côté d'eux.
- **Effectuer diverses actions** : une fois que vous avez sélectionné les fichiers ou dossiers à gérer, vous aurez accès à plusieurs actions adaptées à vos besoins.

{{< cards cols="1">}}
  {{< card title="" subtitle="Mode de sélection pour les fichiers en ligne" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-selection-mode.webp" >}}
{{< /cards >}}

## Actions sur les fichiers

Près du titre du fichier, vous remarquerez un symbole de points de suspension « ... » (trois points) — ceci sert de menu d'actions.  
Appuyez dessus pour révéler une liste d'actions disponibles :

- **Lire ensuite** : choisissez cette action pour insérer le fichier choisi en haut de votre file d'attente du lecteur, en veillant à ce qu'il soit lu immédiatement après l'élément en cours de lecture.
- **Lire plus tard** : la sélection de cette option ajoute le fichier en bas de votre file d'attente du lecteur, en veillant à ce qu'il soit lu après la file d'attente existante.
- **Ajouter à la bibliothèque musicale** : cette action vous permet d'incorporer le fichier dans votre bibliothèque musicale, le rendant facilement accessible et bien organisé par artiste, album, genre ou compositeur.
- **Ajouter à une playlist** : utilisez cette action pour ajouter le fichier à une playlist existante ou en créer une nouvelle.
- **Modifier les balises audio** : en sélectionnant cette option, vous pouvez accéder à l'éditeur de tags intégré d'Evermusic, vous permettant de modifier les tags audio pour le fichier choisi. Le fichier sera temporairement téléchargé dans un répertoire temporaire, puis téléversé vers le stockage après que vous ayez confirmé les modifications.
- **Ajouter aux favoris** : cette action ajoute le fichier à votre liste de fichiers favoris pour un accès rapide et pratique.
- **Télécharger** : choisissez cette action pour télécharger le fichier ou dossier sur votre appareil, le rendant accessible hors ligne.
- **Renommer** : cette option vous permet de renommer le fichier directement sur le stockage distant, permettant une dénomination personnalisée des fichiers.
- **Déplacer** : choisissez cette action pour déplacer le fichier vers un autre dossier dans votre stockage cloud, aidant à maintenir une structure de fichiers organisée.
- **Ouvrir dans** : utilisez cette action pour exporter le fichier vers une autre application compatible. Le fichier sera téléchargé sur votre appareil, puis la boîte de dialogue de partage apparaîtra pour un partage ou une interaction supplémentaire.
- **Supprimer** : soyez prudent avec cette action, car elle supprime définitivement le fichier de votre stockage cloud. Cette suppression ne peut pas être annulée.

{{< cards cols="1">}}
  {{< card title="" subtitle="Menu Plus d'actions pour un seul fichier" image="/docs/guide/evermusic/evermusic-guide-connections/img/connect-single-folder-more-options.webp" >}}
{{< /cards >}}

Si la liste des actions dépasse l'espace disponible à l'écran, faites simplement défiler vers le bas dans le menu des actions pour accéder aux options supplémentaires.

## Actions sur les dossiers

Pour chaque dossier dans votre stockage cloud, vous disposez de diverses actions. Pour accéder à ces options, appuyez simplement sur l'icône de points de suspension « ... » située à côté du titre du dossier. Si vous ne voyez pas toutes les actions, faites défiler vers le bas pour en révéler davantage. Voici les actions disponibles :

- **Tout lire** : remplacez la file d'attente actuelle du lecteur par tous les éléments du dossier sélectionné.
- **Lire ensuite** : ajoutez l'intégralité du dossier en haut de la file d'attente du lecteur, juste après l'élément en cours de lecture.
- **Lire plus tard** : ajoutez le contenu du dossier en bas de la file d'attente du lecteur.
- **Ajouter à la bibliothèque musicale** : cette action intègre de manière transparente le contenu du dossier dans votre bibliothèque musicale, le rendant facilement accessible et bien organisé par artiste, album, genre ou compositeur.
- **Ajouter à une playlist** : vous pouvez inclure l'intégralité du dossier dans une playlist. Vous avez également la possibilité de créer une nouvelle playlist et le nom du dossier lui sera automatiquement attribué.
- **Ajouter aux favoris** : utilisez cette action pour ajouter le dossier à votre liste de fichiers favoris pour un accès rapide et pratique.
- **Activer le mode hors ligne** : en activant le mode hors ligne pour un dossier sélectionné, l'application va au-delà du simple téléchargement. Elle analyse continuellement les changements et si de nouveaux fichiers sont ajoutés au dossier en ligne, ils seront automatiquement téléchargés dans l'application.
- **Télécharger** : téléchargez tout le contenu du dossier sur votre appareil pour un accès hors ligne.
- **Renommer** : renommez le dossier directement sur le stockage distant.
- **Déplacer** : déplacez le dossier vers un autre emplacement dans votre stockage cloud.
- **Supprimer** : soyez prudent avec cette action car elle supprime définitivement le dossier et son contenu de votre stockage cloud. Cette action ne peut pas être annulée.


## Accès rapide

La section Accès rapide est située en haut de l'écran. Elle vous donne un accès rapide à vos fichiers favoris et récemment ouverts depuis les services cloud connectés.
Chaque fois que vous ouvrez un fichier ou un dossier depuis le cloud, il est ajouté à la liste « Récemment ouverts ». Pour effacer cette liste, ouvrez « Récents », appuyez sur le bouton « Plus d'actions » et choisissez « Supprimer la liste ». Vous pouvez également marquer des dossiers profondément imbriqués comme Favoris pour y accéder rapidement sans parcourir la structure de répertoires.

## Autres services

Cette section affiche des fonctionnalités supplémentaires qui améliorent votre expérience. Actuellement, l'application prend en charge le scrobbling Last.fm. Lorsqu'il est connecté, vos statistiques de lecture sont automatiquement envoyées à votre compte Last.fm. Vous pouvez visiter votre profil Last.fm ultérieurement pour consulter les analyses d'écoute et obtenir des recommandations musicales personnalisées. Des instructions de configuration détaillées sont disponibles [ici](/docs/howto/how-to-scrobble-your-music-history-from-evermusic-or-flacbox-to-last-fm).
